"""Register the separately qualified finite-field theorem and actual checks."""
from pathlib import Path
import csv
import json
import time
from datetime import datetime, timezone

start = time.perf_counter()
base = Path(__file__).resolve().parents[1]
columns = ["id","statement","status","where_proved","depends_on","manuscript_pages_settled","notes"]
row = ["C.3ac",
       "Abelian rational Chow hard Lefschetz over Fpbar is classical; under the cited2026 CM-Hodge theorem rational and numerical equivalence agree and strict B holds",
       "Known with derivation", "finite_field_abelian.tex, paragraph C.3ac",
       "Kunnemann1993 Theorems7.1/7.3; Soule1984 Theorem7; C.5a; for the strengthened clause D.4c-e, Milne1999 Theorem7.1 with erratum, Kahn2003 Theorem1.10, Milne2002 Theorem3.3",
       "14:44-47;14:107-112",
       "Unconditional part settles both abelian C3 injectivities and A/A′/A″ over Fpbar. The stronger CH_Q=num_Q, Griffiths=0 and strict positivity are explicitly qualified by the same2026 primary preprint theorem input as D4e. No arbitrary nonconstant function-field claim, no complex-gate closure, and no image criterion with unrestricted source varieties."]
with (base/"finite_field_results.csv").open("w",newline="") as file:
    writer=csv.writer(file); writer.writerow(columns); writer.writerow(row)
who="GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/cycles"
events=[
 (who,"used and rechecked in this run","Opened complete Kunnemann1993 primary GDZ PDF and visually read printed99-102. Exact hard Lefschetz locator is Theorem7.3, not item7.2, which is a definition. Theorem7.1 has i!=2r, and passage to Fpbar uses finite data and compatible projectors."),
 (who,"used and rechecked in this run","Retrieved full Soule1984 primary through official GDZ volumeMETS LOG_0047, then visually read pp317-318 and339-344. Theorem7 is p339; Theorem8 is p341; Corollary3 in3.5.5 p343 assumes varieties constant from the finite field."),
 (who,"failed route and correction","A tempting reading of Kunnemann section8 as covering every abelian variety over a global function field was rejected after opening original Soule3.5.5. The manuscript retains its constant-variety hypothesis and makes no nonconstant extension claim."),
 (who,"used and rechecked in this run","Opened complete published Kahn2003 PDF and original images pp981-982, plus Definition1 p978. Theorem1.10 is rational=num under BOTH abelian type and Tate; Theorem1.4, Proposition1.5, Lemma1.6, Proposition1.7 and Lemma1.9 were read with the proof."),
 (who,"used and rechecked in this run","Freshly opened Milne1999 author PDF, author erratum, vanHoften-Sempliner2026 primary PDF TheoremI, and Milne2002 published-layout arXiv PDF. Retained cofinal-CM-field correction and D4e's explicit2026 theorem-input qualification."),
 (who,"targeted proof check","Checked Chow colimit, ample descent, Gysin exponents, ordinary localization, numerical-triviality descent, products/projectors, and the restricted semisimple-category assertion. Stronger field clause does not follow from Kunnemann grading alone."),
 ("GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/frobenius","independent targeted proof and source check","Complete typed proof/source pass received; independently viewed Kunnemann99-100, Kahn978/982 and Soule343. Review is agents/frobenius/C3ac_finite_field_independent_REVIEW.md; independent event file retained by that owner."),
 ("GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root","independent targeted proof and source check","Complete root proof pass received; root freshly opened/read Kahn published978/981-982 and visually checked Kunnemann100. Integration authorized with unchanged2026 qualification."),
 (who,"retrieval and OCR audit","Public GDZ direct download succeeded despite web-tool failure for Soule. Initial OCR with default OpenMP oversubscribed and was interrupted; its page images were already usable. Re-run with OMP_THREAD_LIMIT=1 completed30 pages/58025 characters in20.98761765100062 seconds; OCR is navigational only and decisive formulas were visually read.")]
events.append((who,"typesetting verification","Standalone four-pass LuaLaTeX/BibTeX build completed without diagnostics at 08:44:28 UTC, runtime 2.8330785040016053 seconds. A short prose overflow was repaired. An intermediate rerun caught duplicate bibliography entries after the root bibliography had absorbed the new file; the wrapper now uses the root bibliography alone. Full logs retained."))
with (base/"finite_field_CHECK_EVENTS.tsv").open("w",newline="") as file:
    writer=csv.writer(file,delimiter="\t")
    writer.writerow(["statement_id","date","who_model_effort_run","type","outcome"])
    for actor,kind,result in events:writer.writerow(["C.3ac","2026-11-19",actor,kind,result])
record={"utc":datetime.now(timezone.utc).isoformat(),"rows":1,"events":len(events),"runtime_seconds":time.perf_counter()-start}
(base/"output"/"register_finite_field.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))
