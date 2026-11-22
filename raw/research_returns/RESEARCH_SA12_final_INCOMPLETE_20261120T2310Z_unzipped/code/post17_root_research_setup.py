"""Preserve exact source extraction and completed post17 root audit notes."""
from pathlib import Path
from datetime import datetime,timezone
import tarfile,gzip,hashlib,json
root=Path(__file__).resolve().parents[1]
base=root/'sources/Lieblich2007_moduli';src=base/'source.tar';dst=base/'source'
dst.mkdir(exist_ok=True)
try:
 with tarfile.open(src) as a:
  members=a.getmembers()
  for m in members:
   assert (dst/m.name).resolve().is_relative_to(dst.resolve())
   assert not m.issym() and not m.islnk()
  a.extractall(dst,filter='data')
except tarfile.ReadError:
 (dst/'source.tex').write_bytes(gzip.decompress(src.read_bytes()))
files=[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in dst.rglob('*') if p.is_file()]
now=datetime.now(timezone.utc).isoformat()
record={'utc':now,'source_url':'https://arxiv.org/src/math/0411337v2','extracted_files':files,'scope':'Primary source retained; extraction itself is not a proof read.'}
(root/'code/output/post17_root_research_setup.json').write_text(json.dumps(record,indent=2)+'\n')
notes='''# Root post17 audits and remaining projective-count research

INCOMPLETE. Actor:/root, GPT-6 Astra Pro, SA12 run1; inherited effort setting is not independently exposed. All items below are separate from the frozen checkpoint17 manuscript.

## Actual complete proof audits

At12:45UTC root freshly read the entire actual file D_local_Brauer_zero_surface_transfer.tex. PASS: fixed complete normal surface slices and their actual morphisms, connected-cover detection, finite-normalization PGL descent with the fixed double-product component cost, and the selected-simple-kernel conclusion. Earlier complete audits of the connectedness/slice inputs, SGA1 IX4.7 and Lucchini--Marion--Tracey Proposition2.6 are reused. This is a closure of the one Brauer-zero main reduction, not another movement event.

At12:46UTC root freshly read the complete sparse-DVR fragment in two contiguous ranges, covering every statement and proof. PASS: the p-rank-one primitive residue argument, Noetherian universal regular-sequence proof of the box basis, all-ring base change, the Jacobian/Fitting stratum, two-variable Newton iteration with nilpotent coefficient rings, exact finite unpointed Isom existence, and the explicit O(n) coordinate and polynomial-degree counts when delta/e is bounded. Root also freshly read the entire displayed written proofs of Stacks Lemma10.68.4(tag00LJ), Lemma49.11.1(tag0FKX), and Lemmas49.12.1--49.12.3(tag0BWB). Source URLs:https://stacks.math.columbia.edu/tag/00LJ, https://stacks.math.columbia.edu/tag/0FKX, https://stacks.math.columbia.edu/tag/0BWB. The fixed residue polynomial and uncontrolled global coefficient poles remain explicit. These local presentations do not give the constrained surface-extension count.

## Search and primary reading on nonzero Brauer classes

At12:49UTC root searched the queries `"twisted sheaves" "bounded" "Brauer" "period" Chern surfaces` and `"Brauer" "uniform" "twisted" "Frobenius" representations`. The results included Lieblich's period-index and moduli papers and Huybrechts--Mattei's2025 splitting theorem. No exact uniform quadratic representation-count result was located. This search is not exhaustive and supports no priority claim.

Root opened the primary abstract and full HTML of Lieblich, *Moduli of twisted sheaves*, arXiv:math/0411337v2(8July2005; journal:Duke Mathematical Journal138(2007),23--118), and downloaded the complete author TeX source. At12:50UTC root freshly read the complete statement and proof of Proposition2.3.2.9, with the preceding definitions and Lemma2.3.2.8; and Lemma3.2.3.10, Definitions3.2.3.11--12, Proposition3.2.3.13 and Corollary3.2.3.15 with all their written proofs. The source explicitly proves boundedness for a fixed gerbe using a chosen twisted locally free V and End(V). It does not state a presentation uniform in gerbe order or anchor rank. The constant in Lemma3.2.3.7 is expressly allowed to depend on the gerbe and a splitting cover. Thus these results alone do not remove our remaining count gate. This reading does not claim that the entire65-page source or every cited prerequisite has been read. Primary URLs:https://arxiv.org/abs/math/0411337v2 and https://arxiv.org/html/math/0411337v2.

Root read the introduction through Section1.3 of Huybrechts and Mattei, *Splitting unramified Brauer classes by abelian torsors and the period-index problem*, Mathematische Annalen392(2025),2913--2932, doi:10.1007/s00208-025-03161-2, on the publisher's open primary page. Theorem1.1 fixes an abelian variety over the function field but varies the splitting torsor with the Brauer class; Theorem1.2 bounds the index by a fixed power of the period. Their proofs have NOT been freshly read in this pass, and neither result is used to claim a uniform representation count or a completed reduction. The generic torsor and period-index bounds do not by themselves control our boundary extension or finite-presentation constants.

## Proposed route, not a theorem

For a complete normal surface, the proved Picard/base-change argument gives vanishing of prime-to-p Brauer torsion on a fixed smooth resolved neighbourhood. It is natural to describe puncture Brauer classes by residues on the exceptional components, then seek a bounded-number cyclic-symbol or scalar-digit presentation. Component residues need not extend as compatible global characters, and the exact purity sequence and any uniform presentation must still be proved. D is investigating this route. No main movement is claimed from it.
'''
(root/'parts/D/post17_research/ROOT_POST17_AUDIT_RESEARCH.md').write_text(notes)
print(json.dumps(record,indent=2))
