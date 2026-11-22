from pathlib import Path
from datetime import datetime,timezone
import csv,json,time
start=time.perf_counter();b=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
fetch=json.loads((b/'output/fetch_product_curve_sources.json').read_text());build=json.loads((b/'output/compile_product_curve_top.json').read_text())
with (b/'product_curve_top_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']);w.writerow(['C.3ar','For complex strict cones over products of Qbar-defined curves with external ample L and normal degree-one section ring, B^d(Z)_Q=Q and B^d(X)_Q=0','Proved in the stated restricted scope','product_curve_top_quotient.tex, C.3ar','C3ab/ad finite detection and exact Adams calculation; C3ao actual Pic algebraization; BEK2.2/2.3 and 6.1 normalization; CHW6.1/6.2/B.10','14:108-109','Actual proper-curve families; complex coefficients are absorbed into actual Pic deformation parameters, not applied to Chow groups. No integral finiteness or unrestricted rational top closure. Restricted-family result: no main-gate reset.'])
who='GPT-6 Astra (OpenAI); inherited reasoning effort; /root/cycles'
events=[
('targeted proof check','Verified the relative descent edge is an isomorphism, including incoming and outgoing differentials; retained all absolute coefficient forms.'),
('targeted proof check','Constructed actual homogeneous Pic deformations by formal existence, punctured Pic comparison, Cartier extension and exceptional twist.'),
('targeted proof check','Verified the coefficient-one logarithmic-symbol formula and its positive-degree Euler-contraction normalization; no fixed-level pro-isomorphism asserted.'),
('targeted proof check','Verified fibre-evaluation spanning by a degree>2g-2 morphism and absorption of all complex coefficients into the actual Pic parameter a.'),
('targeted proof check','Verified finite successive elimination, actual proper-curve triviality, the degree quotient on Z and localization to X.'),
('primary-source verification','Freshly opened BEK full21-page primary, Lemma2.2/Proposition2.3 and Proposition6.1 proof authorpp3-4/12-13; CHW full29-page primary Th6.1/Cor6.2/B.10 and multiplicativity. Exact URLs/hashes/runtimes in product_curve_top_SOURCE_AUDIT.md.'),
('independent proof/source check received','/root/real_weil full PASS; exact review and events in agents/real_weil/C3ar_product_curves_independent_REVIEW.md and corresponding TSV. Compatible-higher-stage clarification incorporated.'),
('independent proof/source check received','/root/frobenius full PASS; exact review and events in agents/frobenius/C3ar_product_curve_top_independent_REVIEW.md and corresponding TSV.'),
('independent root check received','/root full typed proof and exact primary-source PASS received before this actual registration; root checked BEK pro-only normalization and CHW fixed-weight comparison.'),
('program execution','Fresh source retrieval completed '+fetch['utc']+'; runtime_seconds='+str(fetch['runtime_seconds'])+'; exact SHA256/byte counts retained in output/fetch_product_curve_sources.json.'),
('document validation','Latest four-pass wrapper: '+build['utc']+'; runtime_seconds='+str(build['runtime_seconds'])+'; returncodes='+str([r['returncode'] for r in build['runs']])+'; diagnostics='+str(build['diagnostics'])+'. Full logs retained.'),
('scope check','This is a positive result only for the specified product-of-curves cones over C; the unrestricted rational/complex top quotient remains unresolved by this proof. No main-gate movement claimed.')]
with (b/'product_curve_top_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome']);
 for kind,detail in events:w.writerow(['C.3ar',now,who,kind,detail])
report='''# C.3ar: rational top quotient for complex product-of-curves cones

**Status: proved in the stated restricted scope; not a main-gate reset.**

Let V be a product of smooth projective curves defined over Qbar, basechanged to C, and L an external product of very ample line bundles whose full section ring is normal and generated in degree one. For the strict local cone puncture X and its regular resolution Z, the proof gives B^d(Z)_Q=Q by degree on the exceptional divisor, and B^d(X)_Q=0.

The relative Adams-weight-d group is the direct sum of H^d(V,L^j) tensor Omega_C/Q^(d-1). Actual formal-Pic line bundles, algebraized individually, are multiplied by ordinary point-difference line bundles on the curve factors. High-degree finite maps to P1 make fibre evaluations span each needed H^1(O) tensor db. Every complex coefficient is absorbed into the actual Pic deformation parameter. Thus the argument uses finite sums of actual cycles, without assigning a complex-vector-space structure to Chow groups. Successive leading-degree elimination reaches a finite K0-detecting thickening, where the residual class vanishes.

All three independent proof/source audits passed. The proof does not algebraize arbitrary formal K0 objects, promote a pro-isomorphism to an isomorphism at a fixed level, or claim integral finiteness. The q=0 quintic-cone case is not covered by this Pic-product construction.

## Artifacts

- `product_curve_top_quotient.tex`: full proof.
- `product_curve_top_results.csv`, `product_curve_top_CHECK_EVENTS.tsv`: scoped assertion and actual checks.
- `output/C3ar_check.pdf`, `output/compile_product_curve_top.json`: fresh wrapper and exact diagnostics/runtime.
- `code/fetch_product_curve_sources.py`, `output/fetch_product_curve_sources.json`: primary source files, exact hashes and actual runtime.

No new bibliography key is required: D_Loday1992, D_CortinasHaesemeyerWeibel2009 and D_BlochEsnaultKerz2014 are reused from the independently owned source bibliography.
'''
(b/'product_curve_top_REPORT.md').write_text(report+'\nRegistration UTC: '+now+'\n')
source='''# C.3ar primary-source audit

All exact source inputs named below were opened in their primary full PDFs and the specified statements/proofs read. No statement about reading the entirety of either paper is intended.

- Bloch–Esnault–Kerz, *Deformation of algebraic cycle classes in characteristic zero*, Algebraic Geometry1(3)(2014)290–310, DOI10.14231/AG-2014-015. Full21-page author PDF: https://page.mi.fu-berlin.de/esnault/preprints/helene/112-bek.pdf . Read Lemma2.2 and Proposition2.3, authorpp3–4; Proposition6.1 and its proof, pp12–13; Eq6.5 and Theorem6.2, pp13–14. The first-Chern and logarithmic-symbol normalization is exact. The comparison theorem remains explicitly a pro-isomorphism. Browser refs turn143921303view0, turn306766019view0/1. AppendixB's algebraization warning remains distinct from the actual Pic construction.
- Cortiñas–Haesemeyer–Weibel, *Infinitesimal cohomology and the Chern character to negative cyclic homology*, Math. Ann.344(4)(2009)891–922. Full29-page author PDF: https://arxiv.org/pdf/math/0703133 . Read Theorem6.1/Corollary6.2, authorp15, TheoremB.10 and the preceding multiplicativity comparison, p25, and the multiplicativity argument p16. Browser refs turn143921303view1, turn306766019view2/3. The fixed-weight nilpotent comparison is separate from BEK's pro-level comparison. Its internal file/version date qualification is retained in the existing bibliography.
- Loday, *Cyclic Homology*, first edition(1992), Theorems4.6.7–4.6.8, printed151–152: the exact arbitrary-commutative-Q-algebra calculation is reused from the previously opened primary source record and the certified C3ad proof, whose entire derivation was reread in this pass. No fresh Loday download is claimed after the scratch loss. No smooth HKR theorem is applied to a nonreduced thickening.

## Actual fresh retrieval data

'''
source+='```json\n'+json.dumps(fetch,indent=2)+'\n```\n'
(b/'product_curve_top_SOURCE_AUDIT.md').write_text(source)
p=b/'cycles.tex';s=p.read_text();anchor='\\input{agents/real_weil/C3_top_all_positive_characteristics.tex}';line='\\input{agents/cycles/product_curve_top_quotient.tex}';assert anchor in s
if line not in s:s=s.replace(anchor,anchor+'\n'+line)
p.write_text(s)
record={'utc':now,'runtime_seconds':time.perf_counter()-start,'rows':1,'events':len(events),'integrated':True};(b/'output/register_product_curve_top.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
