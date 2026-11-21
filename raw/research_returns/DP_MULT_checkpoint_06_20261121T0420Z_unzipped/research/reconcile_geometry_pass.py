#!/usr/bin/env python3
"""Record completed geometry-pass checks, source additions and current gates."""
import csv, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
cp=root/"CHECK_EVENTS.tsv"
with cp.open(newline="") as f:
    r=csv.DictReader(f,delimiter="\t"); fields=r.fieldnames; rows=list(r)
def add(s,who,kind,scope,outcome,evidence,when=now):
    if any(r["evidence"]==evidence for r in rows): return
    n=max(int(r["event_id"].split("-")[1]) for r in rows)+1
    rows.append(dict(zip(fields,[f"DPC-{n:03d}",s,"2026-11-21 UTC",when,who,
      "GPT-6 Astra Pro","not exposed by runtime","DP_MULT_20261121",kind,scope,outcome,evidence])))
with (root/"research/archive_binomial_check_events.tsv").open(newline="") as f:
    for r in csv.DictReader(f,delimiter="\t"):
        n=int(r["event_id"].removeprefix("ABA-CE"))
        if n<35: continue
        kind=("refuted, with the refined statement's id" if n==35 else
              "independent re-proof" if n==38 else "targeted proof check")
        add(r["statement_id"],r["checker"],kind,r["scope"],r["outcome"]+" LIMIT: "+r["limitations"],
            "research/archive_binomial_check_events.tsv:"+r["event_id"],r["utc_time"])
for name,sid in [
    ("DP40_integrated_formal_bound_review_metadata.json","DP40"),
    ("DP43_author_whole_review_metadata.json","DP43"),
    ("DP43_root_whole_read_metadata.json","DP43"),
    ("DP44_root_whole_read_metadata.json","DP44"),
    ("DP45_root_whole_read_metadata.json","DP45"),
    ("DP48_root_whole_read_metadata.json","DP48"),
    ("DP44_formal_bound_review_metadata.json","DP44"),
    ("DP45_formal_bound_review_metadata.json","DP45"),
    ("DP46_author_whole_review_metadata.json","DP46"),
    ("DP46_author_final_review_metadata.json","DP46"),
    ("DP43_final_formal_bound_review_metadata.json","DP43"),
    ("DP44_final_formal_bound_review_metadata.json","DP44"),
    ("DP45_final_formal_bound_review_metadata.json","DP45"),
    ("DP47_final_formal_bound_review_metadata.json","DP47"),
    ("DP48_final_formal_bound_review_metadata.json","DP48"),

    ("DP44_integrated_formal_bound_review_metadata.json","DP44"),
    ("DP45_integrated_formal_bound_review_metadata.json","DP45"),
    ("DP47_formal_bound_review_metadata.json","DP47"),
    ("DP48_formal_bound_review_metadata.json","DP48"),
]:
    p=root/"research"/name
    if not p.exists(): continue
    d=json.loads(p.read_text());scope=d.get("scope",d.get("checks","Complete recorded proof reading"))
    if isinstance(scope,list):scope=" ".join(scope)
    add(sid,d.get("agent",d.get("who",d.get("reviewer","/root/formal_bound"))),
        "targeted proof check",scope,d.get("outcome",d.get("status",d.get("result","PASS"))),
        "research/"+name,d.get("whole_read_completed_utc",d.get("recorded_utc",d.get("time_utc",now))))
for name,sid in [("dp44_rank_global_checks.json","DP44"),("dp47_hyperbolic_pullback_checks.json","DP47")]:
    d=json.loads((root/"research"/name).read_text())
    for e in d["events"]:
        kind="used and rechecked in this run" if "-S" in e["id"] else "targeted proof check"
        add(sid,"/root/step2_higher",kind,e["scope"],e["outcome"],
            "research/"+name+":"+e["id"],e.get("observed_completion_utc",d["recorded_utc"]))
add("DP46","/root","targeted proof check",
    "Read the complete saved variable-ghost, unit-path, primitive-line, invariant-frame and transport proof; found missing plus in UI10 and missing backslash in UI12, then reread the corrected formulas. Mathematical derivation and explicit theta_j exponents checked.",
    "PASS after the recorded display corrections; earlier printed UI10 required correction. Independent complete corrected-version reading is separately recorded.",
    "research/unit_arrow_kernel_invariance_DP46.md:root-complete-reading-and-corrections")
add("DP47","/root","targeted proof check",
    "Read complete saved sections1-7: actual adjunction, invariant bilinear vanishing, trace-one product/sign, integral frame versus quadratic difference, polarized idempotent criterion, unit tensor parameter and nonzero restricted factor.",
    "PASS; local geometric identification under the stated block hypotheses; no global path or cost theorem inferred.",
    "research/hyperbolic_poincare_pullback_DP47.md:root-complete-reading","2026-11-21 02:43:13 UTC")
add("DP44","/root","targeted proof check",
    "Direct source line341 uses Nat division for the Y negative index. Replaced the ambiguous rational-looking (M'-j)/2 by floor((M'-j)/2) in the integrated proof and fragment; reviewed the exact correction.",
    "PASS corrected notation; historical earlier proof-read records retained. The rank restriction argument and all bookkeeping identities are unchanged.",
    "research/DP44_integrated_fragment.tex:Nat-division-correction")
add("AUTHOR-SOURCE-529","/root","computation or formal certificate",
    "Compared the three new local files with exact sizes and hashes in direct author-archive extraction metadata; merged their original members into the prior526 inventory. This is incremental provenance, not a new529-file archive sweep.",
    "529 current modules:526 from the recorded sweep plus3 direct extractions; new file sizes/hashes agree. No Lean execution or full-source proof reading claimed.",
    "research/dp44_added_sources.json:root-incremental-manifest")
with cp.open("w",newline="") as f:
    w=csv.DictWriter(f,fields,delimiter="\t");w.writeheader();w.writerows(rows)

qp=root/"QUESTIONS.tsv"
with qp.open(newline="") as f:
    r=csv.DictReader(f,delimiter="\t");qfields=r.fieldnames;questions=list(r)
for r in questions:
    if r["id"]=="Q3e":
        r["finding_ids_or_counterexample"]="U2; DP21;DP23;DP25-DP48"
        r["current_gate_or_scope"]=(
          "Actual cyclic CM models, optimal directional/codimension bounds, arbitrary-unit primitive mixed-line slopes, and the polarized trace-one hyperbolic pullback are proved. Rational quadratic gauges cannot improve those line slopes. "
          "The old rank/HC/host and generic Spaces data can be rebuilt at any smaller even m>=2; a new endpoint period and its integral ties are the next nonautomatic fields. "
          "For a mixed CM family, construct its actual selected theta/connection/minor/path data, controlled nonvanishing and global links, then compare actual gain and full costs. "
          "Equal-direction sums and primitive ordinary lines are settled local families; arbitrary harmonic selections and the net integer lift saving remain open.")
new=[
 ("Q3ae","Params6-69;DataHost39-109;hostSpacesOfNorm137-142;spacesOfRanks325-386;DP44",
  "Do the numerical and Hermitian-space interfaces themselves force the original even lift count?",
  "refuted as a minimality claim","DP44",
  "Every smaller even m>=2 preserves Ranks/HC/Host and admits actual generic Spaces with the same norm element. New endpoint periods, ExtraNZIn and global links still require instantiation; frozen-data gain/main-term identities give the exact comparison without reversing LinkG."),
 ("Q3af","DP22 Jacobian;Tate1967 connected-etale sequence;ZinkTh5/9;DP45",
  "Is the nonalternating height-six cyclic type an actual integral CM Jacobian example?",
  "proved","DP45",
  "At p=3 or5 mod7, Jac(y²=x⁷−1) has connected height6 dimension3 display with free rank-one CM eigenspaces and arbitrary unit arrows. Exact slopes (p,p²,p³)/((p−1)(p³+1)) and affine loss3 apply integrally."),
 ("Q3ag","Variable ghost display pairing and invariant integral frames;DP46",
  "Does the primitive mixed-line slope depend on choosing unit-one Honda arrows?",
  "refuted","DP46",
  "All arbitrary-unit singleton/complement displays have the same exact slope governed by restricted-p length; explicit unit coefficient and invariant-frame independence proved. Supplied integral CM isomorphisms transport it; no finite twist trivialization is assumed."),
 ("Q3ah","IsCanonGauge174-183;hL185;ExpConjConnectionIntegral40;actual Poincare adjunction;DP47",
  "Can the source trace-one diagonal be identified with an actual primitive polarized block?",
  "proved under explicit integral polarized-block hypotheses","DP47",
  "Conjugate integral idempotents and a p-unit polarization give the hyperbolic block. The trace-one diagonal contains exactly B^(-1), up to an integral unit and quadratic logarithmic gauge. Tensor power kappa needs p∤kappa for the unit-coefficient path theorem."),
 ("Q3ai","Canonical-gauge differences;DP41/42;DP48",
  "Can a rational quadratic canonical-gauge term improve the primitive ordinary-line slope?",
  "refuted","DP48",
  "Over the unramified field the exact coefficient threshold is max(w_k,(s−v(c))/2). Integral quadratic c preserves the slope; nonintegral c strictly worsens it. Nonzero prefactor restriction remains necessary; arbitrary harmonic projections are separate."),
]
ids={r["id"] for r in questions}
for r in new:
    if r[0] not in ids:questions.append(dict(zip(qfields,r)))
with qp.open("w",newline="") as f:
    w=csv.DictWriter(f,qfields,delimiter="\t");w.writeheader();w.writerows(questions)
print(json.dumps({"utc":now,"events":len(rows),"questions":len(questions)}))
