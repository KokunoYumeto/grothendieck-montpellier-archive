#!/usr/bin/env python3
"""Narrow parent-authorized PH2 promotion; root owns the CP33 input config."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re

agent = Path(__file__).resolve().parents[1]
root = agent.parents[1]
candidate = agent / "post_CP32_birational_Pfaffian_height_two_counterexample_candidate.tex"
canonical = agent / "birational_Pfaffian_height_two_counterexample.tex"
expected = "f2b37e75b60aba9f39cc6ef4e72388dfd2edbcc9e676ce7c5a8d83930ae19915"
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(candidate) == expected and not canonical.exists()
audits = [
    root / "outputs/root_Pfaffian_height_two_audit.json",
    root / "agents/reduction_descent/outputs/independent_Pfaffian_height_two_audit.json",
]
for p in audits:
    assert expected in p.read_text() and "PASS" in p.read_text()
before = candidate.read_text()
after, number = re.subn(
    r"\\status\{Candidate[^}]*\}",
    lambda _: r"\status{Proved; independent audits passed.}", before
)
assert number == 3
after = after.replace(
    "% Isolated post-CP32 counterexample.  Candidate pending independent full audit.",
    "% Promoted after complete root and reduction/descent proof/code audits."
)
after = after.replace(
    r"\path{agents/monodromy/code/verify_birational_Pfaffian_height_two.py}",
    r"\path{code/monodromy/verify_birational_Pfaffian_height_two.py}"
)
needle = "five cases, proves the assertion for every odd \\(N\\ge5\\).\n"
assert needle in after
after = after.replace(
    needle,
    needle + "The author run passed in \\(0.003415901999687776\\) seconds;\n"
    "the unchanged, author-preserving independent root and reduction/descent\n"
    "reruns passed in \\(0.004231348997564055\\) and\n"
    "\\(0.004291741002816707\\) seconds, respectively.\n"
    "Both reviewers independently rederived the complete uniform proof.\n"
    "The root also checked the stated primary-source comparison; the\n"
    "companion record makes no fresh original-source reading claim.\n"
    "The exact candidate, all programs, outputs and audit records are retained.\n"
)
after = after.replace(
    "Example 2.5, printed page 344, assumes",
    r"Example 2.5, printed page 344 \cite[Example 2.5]{RussoSimis2001Birational}, assumes"
)
after = after.replace(
    "2016, Theorem 9.1, likewise assumes",
    r"2016, Theorem 9.1 \cite[Proposition 4.1 and Theorem 9.1]{KustinPoliniUlrich2016Blowups}, likewise assumes"
)
after = after.replace(
    "Cremona transformations}, Lemma 2.4.1, supplies",
    r"Cremona transformations}, Lemma 2.4.1 \cite[Theorem B and Lemma 2.4.1]{Polishchuk2022Cremona}, supplies"
)
history = agent / "history"
history.mkdir(exist_ok=True)
canonical.write_text(after)
(history / "birational_Pfaffian_height_two_promotion.diff").write_text(
    "".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
             fromfile=str(candidate.relative_to(root)), tofile=str(canonical.relative_to(root))))
)

bib = agent / "references.bib"
bib_before = bib.read_text()
assert "KustinPoliniUlrich2016Blowups" not in bib_before
assert "Polishchuk2022Cremona" not in bib_before
entries = r"""

@misc{KustinPoliniUlrich2016Blowups,
 author={Kustin, Andrew R. and Polini, Claudia and Ulrich, Bernd},
 title={The Equations Defining Blowup Algebras of Height Three Gorenstein Ideals},
 year={2016},
 howpublished={Author manuscript dated 14 October 2016},
 url={https://www.math.purdue.edu/~bulrich/papers/Kustin-Polini-Ulrich-Height-Three.pdf},
 note={Original author manuscript opened. Introduction, full Proposition 4.1 proof on printed page 11, full Theorem 9.1 statement and proof on printed pages 28--29, and initial Remark 9.2 read on 20 November 2026. Height three is an explicit assumption. No theorem about the actual Cartier tensor is imported; no whole-paper or complete-dependency read is claimed. Root independently checked this precise source-comparison scope.}
}

@article{Polishchuk2022Cremona,
 author={Polishchuk, Alexander},
 title={Feigin--Odesskii brackets, syzygies, and Cremona transformations},
 journal={Journal of Geometry and Physics},
 volume={178},
 pages={104584},
 year={2022},
 doi={10.1016/j.geomphys.2022.104584},
 url={https://arxiv.org/pdf/2204.09152},
 note={Original arXiv version 2, dated 30 April 2022, opened. Introduction and Theorem B, section 2.3 including Remarks 2.3.1--2.3.2, and full Lemma 2.4.1 statement and proof on printed pages 7--8 read on 20 November 2026. The geometric elliptic-curve application begins in characteristic zero; the cofactor construction does not assert the reduced-base codimension required here. No such geometric theorem is imported. Root independently checked this precise source-comparison scope.}
}
"""
bib_after = bib_before + entries
(history / "pre_Pfaffian_height_two_references.bib").write_text(bib_before)
(history / "Pfaffian_height_two_references.diff").write_text(
    "".join(difflib.unified_diff(bib_before.splitlines(True), bib_after.splitlines(True),
             fromfile="retained-prior-references.bib", tofile="agents/monodromy/references.bib"))
)
bib.write_text(bib_after)

consolidate = root / "code/consolidate.py"
shared_before = consolidate.read_text()
anchor = "   out.write('\\n\\\\input{sections/A_route_limitations_29}\\n')"
assert shared_before.count(anchor) == 1
assert canonical.name not in shared_before
addition = (
    "   pfaffian_countermodel=a/'monodromy/birational_Pfaffian_height_two_counterexample.tex'\n"
    "   if pfaffian_countermodel.exists() and '\\\\status{Candidate' not in pfaffian_countermodel.read_text():\n"
    "    out.write('\\n'+pfaffian_countermodel.read_text()+'\\n')\n"
)
shared_after = shared_before.replace(anchor, anchor + "\n" + addition.rstrip("\n"))
(history / "pre_Pfaffian_height_two_consolidate.py").write_text(shared_before)
(history / "Pfaffian_height_two_consolidate.diff").write_text(
    "".join(difflib.unified_diff(shared_before.splitlines(True), shared_after.splitlines(True),
             fromfile="retained-prior-consolidate.py", tofile="code/consolidate.py"))
)
consolidate.write_text(shared_after)
now = datetime.now(timezone.utc).isoformat()
record = {
    "status": "PROMOTED",
    "actual_utc": now,
    "candidate": str(candidate.relative_to(root)),
    "candidate_sha256": expected,
    "canonical": str(canonical.relative_to(root)),
    "canonical_sha256": digest(canonical),
    "labels": re.findall(r"\\label\{([^}]+)\}", before),
    "audits": [str(p.relative_to(root)) for p in audits],
    "consolidate_sha256": digest(consolidate),
    "bibliography_sha256": digest(bib),
    "source_keys": ["KustinPoliniUlrich2016Blowups", "Polishchuk2022Cremona"],
    "source_census": "agents/monodromy/outputs/post_CP32_Pfaffian_primary_source_scope.json",
    "scope": "Uniform abstract counterexample only. No actual Cartier realization or monodromy failure; no exact full-image degree changed.",
    "checkpoint_config_owner": "/root",
}
(agent / "outputs/birational_Pfaffian_height_two_promotion.json").write_text(
    json.dumps(record, indent=2) + "\n"
)
with (agent / "CHECK_EVENTS_post_CP16.tsv").open("a") as stream:
    for label in record["labels"]:
        if not label.startswith("subsec:"):
            stream.write("\t".join([label, now, "/root/monodromy",
                "PROMOTED-ROOT-RD-FULL-PROOF-CODE-PASS", record["scope"]]) + "\n")
assert digest(candidate) == expected
print(json.dumps(record, indent=2))
