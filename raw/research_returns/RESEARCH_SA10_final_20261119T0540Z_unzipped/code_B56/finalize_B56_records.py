#!/usr/bin/env python3
"""Record the final independent B5 scope audit and source checks."""
from pathlib import Path
import csv
import datetime
import io
import json
import time

started = time.perf_counter()
work = Path(__file__).resolve().parents[1]
manifest_path = work / "agent_B56.md"
manifest = manifest_path.read_text()
manifest = manifest.replace(
    "The shape-only comparison has the exact constant-space tests B5.6.2.",
    "The pro-space comparison has the exact mapping-space tests B5.6.2; the original Artin--Mazur comparison is precisely q of the hypercomplete shape, with exact pi0 tests B5.6.3--4."
)
manifest = manifest.replace(
    "Grandis 2001, DHI 2004 (arXiv v2 and LaTeX source), HTT, Barnea--Schlank v9, Curtis 1971, Stacks 019G, and Kerodon 00ZA/00ZH/00ZK are opened and used.",
    "Grandis 2001, DHI 2004 (arXiv v2 and LaTeX source), HTT, Barnea--Schlank v9, Barnea--Harpaz--Horel 2017 Theorem6.0.4 pp625--626, Curtis 1971, Stacks 019G, and Kerodon 00ZA/00ZH/00ZK are opened and used. The requested Haine1811.01119v6 is fully opened; Definition1.1.4 and Theorem1.1.7 p8 are cited in C1_collage_B.tex for the flag-Segal framework, not used as a premise in B5."
)
if "## Final B.5 scope audit" not in manifest:
    manifest += """

## Final B.5 scope audit

`B5_scope_audit.md` records exact request coverage and all implication directions. The primary BHH theorem explicitly identifies the hypercompleted shape; no inference from local weak equivalence to full nonhypercomplete shape remains. Full flatness still gives the stronger pre-hypercompletion assertion. Symmetric full Hyp implies hypercover strictly; ordinary flatness and hypercover are incomparable. The Artin--Mazur criterion applies pi0 after the limit of mapping spaces and applies q after the pro-space colimit.

`B56.tex` is the directly maintained authoritative proof, with separate B.5 and B.6 section headings. `code_B56/sync_B56_mirrors.py/.out` records the final normalization and regenerated TeX/Markdown mirrors. No hidden generator is required to reconstruct the source. The complete C5 Hurewicz proof and its separate references remain preserved.
"""
manifest_path.write_text(manifest)

result_path = work / "results_B56.csv"
with result_path.open(newline="") as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row["id"] == "B5.6":
        row["statement"] = "Exact slice-shape comparison and original Artin-Mazur pro-homotopy criterion; full Hyp gives pre-hypercompletion descent."
        row["notes"] = "B5.6.2 pro-space mapping tests; B5.6.3-4 AM=q(hypercomplete shape), locally connected, exact pi0 tests. BHH Th6.0.4 plus Barnea-Schlank Remark8.5(2). No q-colimit or pi0-limit interchange."
    if row["id"] == "B5.5":
        row["notes"] = "Ordinary flatness and hypercover incomparable; symmetric full Hyp implies hypercover strictly; symmetric hypercovers need not satisfy forest."
with result_path.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

event_path = work / "CHECK_EVENTS_B56.tsv"
with event_path.open(newline="") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    event_fields = reader.fieldnames
    events = list(reader)
who = "GPT-6 Astra (OpenAI, ChatGPT Pro mode); inherited effort; /root/hypercovers_finite_sets"
new_events = [
    ("B5.6-final-scope", "targeted proof check", "Audited actual B56.tex against exact B5 request: full Hyp lift first to associated 1-localic infinity-topos then hypercompletion; exact AM formula and pi0 criterion added; no local-weak-to-full-shape inference. B5_scope_audit.md records all directions."),
    ("B5.6-BHH", "used and rechecked in this run", "Opened full BHH2017 primary PDF, Theorem6.0.4 pp625-626 and Corollary6.0.5p626. Derived realization is shape of hypercompletion; combined opened Barnea-Schlank Remark8.5(2)p65 for all locally connected topoi."),
    ("B5.5-symmetric-direction", "independent re-proof", "In symmetric indexing, flat systems are inhabited E^S, hence Cech hypercovers with all positive matching maps isomorphisms. Strictness follows symmetric continuous-simplex counterexample. Ordinary flatness and hypercovers remain incomparable."),
    ("C1.B2-Haine", "used and rechecked in this run", "Opened requested Haine1811.01119v6 full PDF: Definition1.1.4 and Theorem1.1.7p8 identify decollages with conservative categories. B agent independently opened and cites after C1.B2; not a premise for B5 or substitute for geometric Exit proof."),
    ("C1.03-repaired-review", "targeted proof check", "Rechecked selected-prefix maps and corrected mapping-cylinder presentation: all final and nonfinal nerve face relations generated, all generators standard realization identifications, universal property now agrees. Earlier omitted-prefix counterexample resolved."),
    ("C1.B1-B3-independent-review", "targeted proof check", "Reviewed directed collage pushout, crossing-arrow left fibration, homotopy-fibre flag model, outer-face positive-radius collar homotopy, and recursive conically smooth bundle hypotheses. Remaining-label naturality distinguished from deleted outer-face inclusion; no new gap found."),
    ("B56-final-source", "computation or formal certificate", "Authoritative directly maintained B56.tex has parallel B5/B6 sections; sync_B56_mirrors.py/out regenerates identical TeX mirror and Markdown, runtime0.176059078s at05:17:33UTC. All proof source and scripts preserved."),
    ("C5H.1-Mazur-original-search", "targeted source check", "Original Mazur1961 DOI10.2307/1970288 identified, but JSTOR PDF/DOI paths inaccessible and landing page provides no paper text; original remains not opened. Additionally opened Zeeman1962 Annals76 pp235-236 via LMS, contextual only. The used existence/group sources remain opened Zeeman1964p347 and Rolfsen11E.3p356."),
    ("Final-register-audit", "computation or formal certificate", "Read-only audit of actual recursively included paper inputs at05:20:44UTC:74 statement headings=74 unique CSV rows; every exact ID has source and aggregate check events. All36 cited keys present among40 bibkeys, no duplicate keys or missing access-status labels. FINAL_register_audit_B56.md/json and audit_final_register.py/out; runtime0.010835391s.")
]
existing = {row["statement_id"] for row in events}
added = []
for statement_id, kind, outcome in new_events:
    if statement_id not in existing:
        events.append(dict(statement_id=statement_id, date="2026-11-19", who=who, type=kind, outcome=outcome))
        added.append(statement_id)
with event_path.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=event_fields, delimiter="\t")
    writer.writeheader()
    writer.writerows(events)
print(json.dumps({
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "result_rows": len(rows), "check_event_rows": len(events),
    "new_event_ids": added,
    "seconds": round(time.perf_counter() - started, 9)
}, indent=2))
