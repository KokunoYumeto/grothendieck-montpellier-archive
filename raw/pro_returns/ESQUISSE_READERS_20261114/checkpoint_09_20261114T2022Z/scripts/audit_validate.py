#!/usr/bin/env python3
"""Check review-record coverage and exact replay, without assigning new outcomes."""
from pathlib import Path
import argparse,collections,hashlib,json,re
from audit_inventory import read_tsv,parse_marks
from audit_editorial_adjudication import needs_editorial

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--complete",action="store_true");args=ap.parse_args()
    edition=Path(__file__).resolve().parent.parent;work=edition.parent
    checks=read_tsv(edition/"CHECK_DECISIONS.tsv") if (edition/"CHECK_DECISIONS.tsv").exists() else []
    diffs=read_tsv(edition/"DIFFERENCES_OUTCOMES.tsv") if (edition/"DIFFERENCES_OUTCOMES.tsv").exists() else []
    coll=read_tsv(edition/"COLLATION.tsv") if (edition/"COLLATION.tsv").exists() else []
    cpath=edition/"records/COLLATION_PAGE_COVERAGE.tsv"
    coverage=read_tsv(cpath) if cpath.exists() else []
    common_path=edition/'records/COLLATION_COMMON_MARKS.tsv'
    common=read_tsv(common_path) if common_path.exists() else []
    annotation_path=edition/'copy2_annotations.json'
    annotations=json.loads(annotation_path.read_text()) if annotation_path.exists() else []
    mpath=edition/'records/MECHANICAL_PATCHES.json'
    mechanical=json.loads(mpath.read_text()) if mpath.exists() else []
    errors=[];pages=[];totals_before=collections.Counter();totals_after=collections.Counter()
    packets={p.stem:json.loads(p.read_text()) for p in (work/"review_packets").glob("*.json")}
    for packet in packets.values():totals_before.update(m["macro"] for m in packet["marks"])
    for path in sorted((edition/"checked_pages").glob("*.tex")):
        key=path.stem;packet=packets[key]
        rpath=edition/"reviews"/(key+".json")
        if not rpath.exists():errors.append(f"{key}: checked file has no explicit review declaration");continue
        review=json.loads(rpath.read_text());current=packet["source_text"]
        if set(review.get("inspected_images",[]))!=set(packet["required_images"]):errors.append(f"{key}: image evidence declaration incomplete")
        if not review.get("full_text_confirmation"):errors.append(f"{key}: full text confirmation absent")
        for i,p in enumerate(review.get("patches",[]),1):
            old,new=p["old"],p["new"]
            matches=[m.start() for m in re.finditer(re.escape(old),current)] if old else []
            if not matches:errors.append(f"{key}: patch {i} does not replay");continue
            chosen=matches if p.get("replace_all") else [matches[int(p.get("occurrence",1))-1]]
            for pos in reversed(chosen):current=current[:pos]+new+current[pos+len(old):]
        current=current.replace("not yet checked by eye.","source transcription; scan review recorded in CHECK_DECISIONS.tsv.")
        current="% Scan-checked edition: both supplied image halves reviewed; see CHECK_DECISIONS.tsv.\n"+current
        # Mechanical cleanup is replayed only through explicit hash transitions.
        # Each transition must start at the exact current visual-review result.
        transitions=[m for m in mechanical if m['key']==key];used=set()
        while True:
            before=hashlib.sha256(current.encode()).hexdigest()
            matches=[(i,m) for i,m in enumerate(transitions) if i not in used and m['before_sha256']==before]
            if not matches:break
            if len({m['after_sha256'] for _,m in matches})>1:
                errors.append(f'{key}: ambiguous mechanical hash transition');break
            i,m=matches[0];used.add(i)
            for j,p in enumerate(m['patches'],1):
                old,new=p['old'],p['new'];positions=[x.start() for x in re.finditer(re.escape(old),current)] if old else []
                if not positions:errors.append(f'{key}: mechanical patch {j} does not replay');continue
                chosen=positions if p.get('replace_all') else [positions[int(p.get('occurrence',1))-1]]
                for pos in reversed(chosen):current=current[:pos]+new+current[pos+len(old):]
            if hashlib.sha256(current.encode()).hexdigest()!=m['after_sha256']:
                errors.append(f'{key}: mechanical after-hash mismatch');break
        actual=path.read_text()
        if current!=actual:errors.append(f"{key}: checked text differs from explicit recorded patches")
        actual_scan=re.findall(r"\\scanpage\{([^}]*)\}",actual)
        if actual_scan!=[packet["metadata"]["cote"]+"/"+packet["metadata"]["site"]]:errors.append(f"{key}: scan marker mismatch")
        required={m["item_id"] for m in packet["marks"]}|{n["item_id"] for n in packet["note_items"]}|{d["difference_id"] for d in packet["differences"]}
        required|={f"L-{key}-{l['line']:03d}" for l in packet['source_lines'] if l['text'].strip() and not l['text'].lstrip().startswith('%')}
        covered={r["source_item_id"] for r in checks if r["key"]==key}
        missing=sorted(required-covered)
        if missing:errors.append(f"{key}: {len(missing)} required review targets absent")
        expected={d["difference_id"] for d in packet["differences"]}
        actual_diff={d["difference_id"] for d in diffs if d["key"]==key}
        if expected!=actual_diff:errors.append(f"{key}: difference outcome coverage mismatch")
        marks=parse_marks(actual,key);totals_after.update(m["macro"] for m in marks)
        pages.append({"key":key,"copy":packet["copy"],"typescript_page":packet["metadata"]["ts_page"],
            "checks":sum(r["key"]==key for r in checks),"target_count":len(required),
            "covered_target_count":len(required&covered),"difference_count":len(expected),
            "sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    for what,rows,idkey in [("decision",checks,"decision_id"),("difference",diffs,"difference_id"),("collation",coll,"collation_id")]:
        counter=collections.Counter(r[idkey] for r in rows)
        if any(n>1 for n in counter.values()):errors.append(f"Duplicate {what} identifiers")
    missing_pages=sorted(set(packets)-{p["key"] for p in pages})
    expected_pairs={k for k,p in packets.items() if p['copy']==2}
    covered_pairs={r['copy2_key'] for r in coverage}
    for c in coverage:
        for number in [1,2]:
            key=c[f'copy{number}_key'];path=edition/'checked_pages'/(key+'.tex')
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=c[f'copy{number}_checked_sha256']:
                errors.append(f"{key}: collation source hash is absent or stale")
            if c[f'copy{number}_images'].split()!=packets[key]['required_images']:
                errors.append(f"{key}: collation image coverage mismatch")
        actual=sum(r['copy2_key']==c['copy2_key'] for r in coll)
        if actual!=int(c['entry_count']):errors.append(f"{c['copy2_key']}: collation locus count mismatch")
        shared=sum(r['copy2_key']==c['copy2_key'] and r['kind']=='handwriting in both copies' for r in coll)
        if shared!=int(c.get('shared_mark_count',0)):errors.append(f"{c['copy2_key']}: common-mark count mismatch")
        apparatus=sum(a.get('copy2_key')==c['copy2_key'] for a in annotations)
        if apparatus!=int(c.get('copy2_annotation_count',0)):errors.append(f"{c['copy2_key']}: copy2 apparatus count mismatch")
        if not c['full_inspection'].strip() or not c['original_transcription_comparison'].strip():
            errors.append(f"{c['copy2_key']}: explicit collation declaration incomplete")
    if len(coverage)!=len(covered_pairs):errors.append('Duplicate collation page-coverage declarations')
    if common!=[r for r in coll if r['kind']=='handwriting in both copies']:errors.append('Shared-mark companion table differs from complete collation')
    if len({a['id'] for a in annotations})!=len(annotations):errors.append('Duplicate copy2 apparatus identifiers')
    for a in annotations:
        if not all(a.get(f) for f in ['text_fr','text_en','kind','source_ids']):errors.append(f"{a.get('id')}: incomplete bilingual copy2 apparatus entry")
    if args.complete and missing_pages:errors.append(f"{len(missing_pages)} pages remain unreviewed")
    if args.complete and len(diffs)!=468:errors.append("Complete edition requires 468 difference outcomes")
    if args.complete and expected_pairs!=covered_pairs:errors.append(f"{len(expected_pairs-covered_pairs)} page pairs remain uncollated")
    editorial_path=edition/'records/EDITORIAL_ADJUDICATIONS.tsv'
    editorial=read_tsv(editorial_path) if editorial_path.exists() else []
    expected_editorial={d['difference_id'] for p in packets.values() if p['key'] in {x['key'] for x in pages} for d in p['differences'] if needs_editorial(d)}
    editorial_ids={r['difference_id'] for r in editorial}
    if args.complete:
        if expected_editorial!=editorial_ids:errors.append('Editorial wording-locus coverage is incomplete or contains unchecked pages')
        if any(r['editorial_outcome'].startswith(('pending','proposed')) for r in editorial):errors.append('Editorial wording decisions remain pending')
        for r in editorial:
            path=edition/'checked_pages'/(r['key']+'.tex')
            if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=r['checked_sha256']:
                errors.append(f"{r['difference_id']}: editorial record source hash is absent or stale")
    report={"status":"complete" if not errors and not missing_pages and covered_pairs==expected_pairs else "in progress" if not errors else "validation errors",
        "checked_pages":len(pages),"expected_pages":len(packets),"images_declared_reviewed":2*len(pages),
        "decision_rows":len(checks),"difference_outcomes":len(diffs),"expected_difference_outcomes":468,
        "collation_rows":len(coll),"collated_page_pairs":len(coverage),"expected_collated_page_pairs":58,
        "editorial_wording_loci":len(editorial),"expected_editorial_wording_loci_checked_pages":len(expected_editorial),
        "source_macro_counts_all_pages":dict(totals_before),
        "checked_macro_counts_reviewed_pages":dict(totals_after),"pages":pages,"unreviewed_pages":missing_pages,"errors":errors}
    (edition/"records/AUDIT_PROGRESS.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in ["pages","unreviewed_pages"]},ensure_ascii=False))
    raise SystemExit(1 if errors else 0)

if __name__=="__main__":main()
