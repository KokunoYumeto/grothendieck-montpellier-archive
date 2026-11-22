"""Update own status and route ledger after the endpoint-image reduction."""
from pathlib import Path
import csv
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
path = ROOT / "STATUS.md"
text = path.read_text()
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith("Checkpoint state:"):
        lines[i] = (f"Checkpoint state: {stamp}, updated through the exact endpoint image/standard-D reduction and the independently audited specified generic Walker counterexample. "
                    "AI-produced by GPT-6 Astra (OpenAI), child task /root/cycles; no person credited, no priority claimed, and no independent-model verification claimed. Root, frobenius, and real_weil supplied independent targeted checks within this same model/run, recorded individually.")
    elif line.startswith("| C.1 |"):
        lines[i] = "| C.1 | INCOMPLETE as a full task; universal A/A′/A″ classifications and exact image-criterion reduction settled | C.1a–n: explicit generic quintic line proof; incidence induction; generic Gysin image; all non-top A′/A″ counterexamples by effective Nori connectivity; exact middle positivity radical; universal cycle-class/finite-rank range; explicit radical correspondences including surfaces; image criterion for a fixed target iff universal D and its Griffiths kernel vanishes | Higher strict B classification and its universal positivity-only implications; truth of the universal standard conjecture D, exactly the remaining endpoint-image gate |"
    elif line.startswith("| C.3 |"):
        lines[i] = line.replace("C.3i–k/m–n", "C.3i–k/m–p").replace(
            "remaining low-degree local restriction assertions", "remaining positive-characteristic ordinary local-surjectivity assertions")
        lines[i] = lines[i].replace("C.3n supplies its stated general-characteristic abelian-image injectivity", "C.3n supplies its stated general-characteristic abelian-image injectivity, C.3o settles all complex ordinary degree-one boundary dimensions, and C.3p proves the stated prime-to-residue torsion surjectivity")
    elif line.startswith("| E.3 |"):
        lines[i] = line.replace("E.3a–q, with E.3r drafted for independent review:", "E.3a–r:").replace(
            "codimension2 settled under CH0 surface support", "codimension2 settled under CH0 surface support; fully specified generic matrix times Legendre fourfold with explicit order2 obstruction")
    elif line.startswith("| Lead E4 |"):
        lines[i] = line.replace("E.3c and E.3j–k", "E.3c, E.3j–k and E.3r").replace(
            "on the same Ottem–Suzuki fourfold", "on the same fully specified geometric-generic Ottem–Suzuki fourfold")
text = "\n".join(lines)+"\n"
text = text.replace("Parent and frobenius reviews requested. Its supplemental results add1 row and events add5 before those reviews.",
                    "Root and frobenius independently passed the complete proof and exact Schoen/Suzuki source hypotheses. The intrinsic mod2 etale class makes the same gamma valid under every complex embedding. Its supplemental results add1 row and events add7 including those reviews.")
text = text.replace("Main50 plus Nori1 plus filtration3 plus explicit1 gives55 own statement rows. Main85 plus Nori2 plus filtration10 plus explicit5 gives102 own check events before subsequent independent audits.",
                    "Those 05:50 counts were55 own statement rows and102 own events before subsequent independent audits; the current totals, including C.1n and the E.3r reviews, are recorded below.")
tables = ["results.csv", "nori_results.csv", "filtration_results.csv", "explicit_walker_results.csv", "endpoint_results.csv"]
event_tables = ["CHECK_EVENTS.tsv", "nori_CHECK_EVENTS.tsv", "filtration_CHECK_EVENTS.tsv", "explicit_walker_CHECK_EVENTS.tsv", "endpoint_CHECK_EVENTS.tsv"]
def rows(name, delimiter):
    with (ROOT/name).open(newline="") as stream:
        return len(list(csv.DictReader(stream, delimiter=delimiter)))
nr = sum(rows(name, ",") for name in tables)
ne = sum(rows(name, "\t") for name in event_tables)
marker = "## Endpoint-image reduction and audited generic counterexample"
if marker not in text:
    text += (f"\n{marker}\n\n"
             "endpoint_image.tex proves C.1n: I(X,r) is equivalent to universal D and G_H^r(X)=0. It includes all algebraically closed fields with a fixed Weil cohomology and rational cycle coefficients. For the universal endpoint targets r=0,1,n this is exactly D. Interior universal failures remain qualified over C. Root passed the endpoint proof; frobenius passed the stronger fixed-target proof and reopened Jannsen Theorem1.\n\n"
             "The source-functional construction uses arbitrary source degree, as required by manuscript14:46. Whole numerical motives avoid any unproved algebraic Kunneth projector. The symbolic degree certificate and Jannsen PDF hash are in output/check_endpoint_image.json, reproduced by code/check_endpoint_image.py. The endpoint supplemental registers add1 row and6 events.\n\n"
             f"Current own-register totals: {nr} statement rows and {ne} check events. Parent and sibling fragment rows are maintained by their owners.\n")
path.write_text(text)

ledger = ROOT / "PROGRESS_LEDGER.md"
marker = "## Endpoint-image gate and Peláez orthogonal-cover audit"
body = (f"\n{marker}\n\nRecorded {stamp}. C.1n gives an exact new reduction: for fixed X,r, the all-source cohomological-image criterion is equivalent to universal numerical=homological equivalence and vanishing of the target Griffiths kernel. For endpoint codimensions it is exactly standard D, even for projective-space targets. The proof works over any algebraically closed field with a fixed Weil cohomology, using rational cycle coefficients. Root and frobenius independently passed the stated proof scopes; Jannsen Theorem1 pp448–449 was reopened and the full PDF retained. No truth of D is asserted.\n\n"
        "E.3r now passed both root and frobenius full proof/source audits. The same gamma works under all complex embeddings by its intrinsic mod2 etale cycle class. All source data, finite certificates and review paths are recorded. This removes the unspecified large-prime/general-coefficient choice from the example; it is an explicitness repair and is not counted by itself as movement of the general E.3 generation gate.\n\n"
        "At the parent’s request, Peláez2602.06185v1 Theorem4.1.4 pp6–7 and the complete proof Proposition4.2.12 pp8–9 were reread. The statement detects zero Albanese action of a correspondence landing in CH0 by an orthogonal-cover factorization. Theorems4.3.1–2 use known zero-cycle Albanese vanishing for square or H*2 relations. None asserts a factorization into correspondence images of Albanese-kernel zero-cycles in an arbitrary target codimension. The missing compact/geometric generation step remains to be proved. Saito Lemma1.7.1(ii), checked again in the original p296 image, gives <E>0*<F>0 subset <E*F>0; it gives A*A subset N, not A*H subset N.\n")
if marker not in ledger.read_text():
    with ledger.open("a") as stream:
        stream.write(body)
source = ROOT / "notes/source_record.md"
marker = "## Endpoint-image and orthogonal-cover exact source checks"
if marker not in source.read_text():
    with source.open("a") as stream:
        stream.write(f"\n{marker}\n\n{stamp}: Jannsen1992 full primary https://epub.uni-regensburg.de/26642/1/jannsen10.pdf reopened; Theorem1 pp448–449 and Hom convention pp447–448. Download312181bytes, SHA256f2a285cb7ba9f53a1dcb3844e41901dd4f8391cc2655b1b8195bc7a62a277fab, preserved with degree certificate.\n\nPeláez2602.06185v1 exact Theorem4.1.4 pp6–7 and proof4.2.12 pp8–9 reread in full. Target is zero-cycles on X and their Albanese; the theorem does not assert the missing zero-cycle-generation property for intermediate cycles. Saito1992 p296 Lemma1.7.1(ii) visually rechecked against the retained primary image.\n")
print(f"Updated own status: {nr} rows, {ne} events at {stamp}")
