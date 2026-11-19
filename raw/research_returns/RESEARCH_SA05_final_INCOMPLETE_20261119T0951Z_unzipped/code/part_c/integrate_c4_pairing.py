"""Integrate the independently audited threefold pairing fragment once."""
from pathlib import Path
import csv
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
part = ROOT / "part_c"
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
main = ROOT / "sections/part_c.tex"
text = main.read_text()
fragment = (part / "c4_pairing_reduction.tex").read_text()
needle = r"\begin{proposition}[The lower-endpoint gate over a trait]"
assert text.count(needle) == 1
if r"\label{c:threefold-pairing-kernel}" not in text:
    text = text.replace(needle, fragment + "\n\n" + needle)
    main.write_text(text)

refs = part / "references.bib"
new_bib = (part / "c4_pairing_sources.bib").read_text()
if "c_msaito2003positivity," not in refs.read_text():
    with refs.open("a") as f:
        f.write("\n" + new_bib + "\n")

source_rows = [
    ["c_msaito2003positivity", "opened complete relevant primary proofs",
     "https://arxiv.org/pdf/math/0006162",
     "Theorem0.2 p2; complete sections1.1-2.7 pp3-9; exact n3 converse section2.7 p9. D independently read complete sections4.1-4.3 pp14-16 and5.1-5.5 pp16-18. Root reread complete sections2.1-2.7."],
    ["c_ito2004threefolds", "opened full relevant primary proof and publisher metadata",
     "https://arxiv.org/pdf/math/0212109",
     "Claim4.4-4.7 and end of Lemma4.3 authorpp11-14; rational-image Hodge index in Claim4.6 pp12-13. D independently read Claim4.6. Theorem1.2 extra Picard-number hypothesis not imported."],
    ["BKahn2023Divisors", "opened complete relevant published primary proof independently of B",
     "https://webusers.imj-prg.fr/~bruno.kahn/preprints/Tate-pour-les-diviseurs-ENT.pdf",
     "Theorem8 pp89-90; actual surface-to-all-dimensions reduction using Morrow, not naive NS weak Lefschetz. Root/B/D separately audited full reduction."],
    ["DMilne2002Polarizations", "opened primary submitted warning; D checked both official author versions",
     "https://www.jmilne.org/math/articles/2002aS.pdf",
     "Submitted Remark4.10 and footnote3 p14; published version Theorem3.3 and Corollary3.4 pp8-9 are abelian only. No transfer of arbitrary geometric positivity from motive-category equality."],
]
sources = part / "sources.tsv"
old_keys = {r[0] for r in csv.reader(sources.open(), delimiter="\t")}
with sources.open("a", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerows(r for r in source_rows if r[0] not in old_keys)

results = part / "results.csv"
old_ids = {r["id"] for r in csv.DictReader(results.open())}
rows = [
    ["c:threefold-pairing-kernel",
     "Exact radical quotient and primitive surface restriction-image criterion for the first threefold monodromy block",
     "Proved reduction; primitive nondegeneracy unresolved",
     "sections/part_c.tex, label c:threefold-pairing-kernel",
     "Rapoport-Zink Satz2.10; c:threefold-weight-gate; Morihiko Saito0.2 and section2.7",
     "12:120-125; C.4",
     "Kernel is rad(R)/(R intersect gamma ker rho). The primitive Gysin condition is automatic by known degree-two monodromy. No general vanishing asserted."],
    ["c:threefold-divisor-split",
     "Orthogonal removal of the rational primitive divisor restriction image; conditional transcendental spectral identification",
     "Proved unconditional splitting; spectral identification conditional on surface Tate",
     "sections/part_c.tex, label c:threefold-divisor-split",
     "Surface Hodge index; Ito Claim4.6; Kahn Theorem8; all-finite-constants divisor Tate",
     "12:120-125; C.4; shared surface-Tate scope",
     "Only rational divisor preimages are removed unconditionally. Under the separate surface-Tate hypothesis the remainder is rho(T1) in T2. No full Frobenius semisimplicity or geometric positivity transfer is inferred."],
    ["c:threefold-pairing-scope",
     "Precise unresolved geometric pairing input and formal counterexample to an invalid scalar-extension positivity inference",
     "Proved scope clarification; actual primitive pairing remains unresolved",
     "sections/part_c.tex, label c:threefold-pairing-scope",
     "c:threefold-pairing-kernel; Q5 isotropic line certificate; Saito0.4/section4.3; Milne submitted Remark4.10",
     "12:120-125; C.4",
     "The negative rational form may have isotropic Q_l subspaces without rational origin. CM Hodge and abstract abelian-motive isomorphisms do not supply arbitrary geometric polarization compatibility."],
]
with results.open("a", newline="") as f:
    w = csv.writer(f)
    w.writerows(r for r in rows if r[0] not in old_ids)

events = part / "CHECK_EVENTS.tsv"
existing = events.read_text()
event_rows = []
for ident in [r[0] for r in rows]:
    event_rows.append([ident, stamp, "GPT-6 Astra (OpenAI), /root/part_c",
        "targeted proof check",
        "Checked the complete written fragment, source scopes, twists, rational divisor image, spectral split and explicit remaining gate; details part_c/c4_pairing_audit.md."])
event_rows += [
 ["c:threefold-pairing-kernel", stamp, "GPT-6 Astra (OpenAI), /root",
  "independent re-proof",
  "Before integration, root passed the complete written kernel/radical proof and independently opened/read Saito Theorem0.2 and complete sections2.1-2.7; no new nondegeneracy assertion."],
 ["c:threefold-pairing-kernel", stamp, "GPT-6 Astra (OpenAI), /root/part_d",
  "independent re-proof",
  "Read every line of the written fragment; independently checked the RZ rows, shared signs, twists and exact Saito n3 primitive-image converse."],
 ["c:threefold-divisor-split", stamp, "GPT-6 Astra (OpenAI), /root",
  "targeted proof check",
  "Full written audit passed rational Gram determinant, orthogonal projection, all-finite-constants Tate and generalized-eigenvalue exclusion. Root had not yet independently reopened Ito at this event."],
 ["c:threefold-divisor-split", stamp, "GPT-6 Astra (OpenAI), /root/part_d",
  "independent re-proof",
  "Full added corollary passed; independently read Ito Claim4.6/full proof pp12-13 and Kahn Theorem8/full proof pp89-90. No full semisimplicity or unconditional rational-origin identification is used."],
 ["c:threefold-pairing-scope", stamp, "GPT-6 Astra (OpenAI), /root/part_c",
  "computation or formal certificate",
  "check_c4_isotropic_ladic_line.py and exact JSON output certify the Q5 isotropic line, six Hensel lifts and scalar Frobenius stability. Formal linear algebra only; not a geometric counterexample."],
 ["c:threefold-pairing-scope", stamp, "GPT-6 Astra (OpenAI), /root/part_d",
  "used and rechecked in this run",
  "Opened both Milne official versions and checked the submitted Remark4.10/footnote3 warning against a general geometric positivity transfer. Detailed independent audit part_d/post05/c4_positivity_scope_audit.md."],
]
with events.open("a", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    for r in event_rows:
        if r[4] not in existing:
            w.writerow(r)

manifest = []
for name, url in [
    ("morihiko_saito2003_positivity.pdf", "https://arxiv.org/pdf/math/0006162"),
    ("ito2004_threefolds.pdf", "https://arxiv.org/pdf/math/0212109"),
]:
    p = part / "sources" / name
    b = p.read_bytes()
    manifest.append({"file": str(p.relative_to(ROOT)), "url": url,
                     "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest(),
                     "recorded": stamp, "status": "opened and relevant complete proofs read"})
(part / "sources/c4_pairing_source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"integrated_labels": [r[0] for r in rows], "timestamp": stamp,
                  "source_manifest": manifest}, indent=2))
