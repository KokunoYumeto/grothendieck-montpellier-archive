#!/usr/bin/env python3
"""Promote fully audited C.3bs without editing root-owned integration files."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import csv, hashlib, json
start=perf_counter()
base=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
draft=base/'C3_component_lifting_no_top_dual_cohomology_draft.tex'
final=base/'C3_component_lifting_no_top_dual_cohomology.tex'
original=draft.read_text()
if not original.startswith('% C.3bs. Complete restricted extension;'):
    raise SystemExit('Expected the complete audited draft, not an earlier pointer.')
archive=base/'output/C3_component_lifting_no_top_dual_cohomology_audited_draft.tex'
archive.write_text(original)
final.write_text(original.replace('% C.3bs. Complete restricted extension; unregistered pending full audits.',
                                  '% C.3bs. Complete root and two-peer audits passed; restricted theorem.',1)
                .replace('(complete draft).}', '(Proved).}',1))
draft.write_text('% Superseded after complete root and two independent peer audits.\n'
                 '% Final: agents/real_weil/C3_component_lifting_no_top_dual_cohomology.tex\n'
                 '% Full audited draft retained in output/C3_component_lifting_no_top_dual_cohomology_audited_draft.tex.\n')
path=base/'results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
if any(row['id']=='C.3bs' for row in rows):raise SystemExit('Duplicate registration refused.')
row=dict.fromkeys(fields,'')
row.update({'id':'C.3bs',
 'statement':'For a projective SNC surface in positive characteristic with H2 of its dual complex zero and surjective joint rational Picard restriction, its top gamma K0 is the direct sum of component CH0 and proper-perfect-family relations are exactly all component degree-zero classes; negative rational-edge C3bm configurations with H2=0 have B2_Q=0 even with triple points',
 'status':'Proved under the stated dual-cohomology and Picard-restriction hypotheses; restricted extension of C3br',
 'where_proved':'C3_component_lifting_no_top_dual_cohomology.tex: C.3bs, DC.1–DC.6',
 'depends_on':'C3bq canonical closed-union totalization and ET9 energy; all-degree constant K_j(P) right inverse; C3br exact Pic-times-unit kernel and proper graph corrections; GH/TT/Levine/Weibel/Quillen/Pedrini–Weibel source chain; C3bm presentation',
 'manuscript_pages_settled':'14:106-109',
 'notes':'Includes triple points and arbitrary component Albanese kernels, but requires H2(dual,Q)=0. Canonical geometric coherence retained; both pi0T/pi1T injections proved on whole fixed-parameter coefficient groups. No H2-nonzero, unrestricted positive-genus, higher-dimensional or resolution-existence claim. Full root/two-peer audits.22 exact bounded matrix checks0.055610326s; clean draft four-pass build2.819458861s. No duplicate source keys.'})
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows([row]+rows)
who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run /root/real_weil; effort setting not exposed'
events=[
 ('targeted proof check','Owner entire DC.1–DC.6 proof and all three saved full root/peer receipts read; PASS. All-j constant parameter splitting gives both T injections; exact component kernel, actual graph correction, degree quotient and negative rational-edge consequence checked. Nonzero H2 and wider scopes excluded.'),
 ('targeted proof check','C3bs_SOURCE_AUDIT.md finalized. Reuses exact freshly completed bq/br GH/TT/Levine/Weibel/Quillen/PW/Stacks primary scopes; no new external theorem or extra fresh source opening claimed. New homotopy step proved directly.'),
 ('computation or formal certificate','Author22-case exact matrix certificate completed2026-11-19T18:21:11.100634UTC in0.05561032599507598s; all pass, including two excluded-H2 negative controls. No geometric or universal theorem inferred from samples.'),
 ('computation or formal certificate','Draft four-pass standalone assembly completed2026-11-19T18:21:13.559045UTC in2.8194588610058418s; all exits0, PDF151241bytes, no undefined/overfull diagnostics. Document assembly only; no peer/root rerun implied.')]
with (base/'CHECK_EVENTS.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for kind,outcome in events:writer.writerow(['C.3bs',now,who,kind,outcome])
with (base/'REPORT.md').open('a') as f:
    f.write(f'\n\n## C.3bs finalized ({now})\n\n'
    'C3_component_lifting_no_top_dual_cohomology.tex is fully root/two-peer audited and registered. '
    'It extends the exact component-family correction to SNC surfaces with triple points when H² of the dual complex vanishes and the joint rational Picard restriction is onto. '
    'The constant-parameter rational right inverse gives both homotopy-group injections needed for actual coherent descent. '
    'Negative rational double curves supply the Picard criterion by the full triple-sensitive energy identity; all component degree-zero groups are removed, including Albanese kernels. '
    'The normal strict-local threefold consequence is B²_Q=0 under these exact hypotheses. '
    'Nonzero H² and the higher-dimensional analogue remain outside; this restricted theorem is not itself a universal main-gate closure. '
    'Exact prior source scopes,22-case matrix certificate/runtime, clean build and all complete receipts are in C3bs_SOURCE_AUDIT.md. Root owns bundle and master integration.\n')
with (base/'SOURCE_AUDIT.md').open('a') as f:
    f.write('\n\n### C.3bs: coherent component lifting under vanishing dual H²\n\n'
    'C3bs_SOURCE_AUDIT.md records the new direct all-degree constant-pullback argument and the explicitly reused complete bq/br primary chain. '
    'No additional source theorem or duplicate bibliography key is introduced. All three full receipts pass; the unproved nonzero-H² extension is kept outside.\n')
record={'completed_utc':now,'runtime_seconds':perf_counter()-start,'result_id':'C.3bs',
        'final':str(final),'sha256':hashlib.sha256(final.read_bytes()).hexdigest(),
        'archived_draft':str(archive),'owner_events_added':len(events),'root_integration_changed':False}
(base/'output/C3bs_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
