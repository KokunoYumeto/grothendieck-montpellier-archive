"""Refresh the fifth checkpoint without fabricating a scheduled progress review."""
from pathlib import Path
import datetime,json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.1':('OPEN: full coherent assertion refuted in every characteristic',
 'thm:A-coherent-restriction-false; lem:A-cyclic-coherent-kernel; thm:A-all-degree-ranges; A1-HIGH',
 'An explicitly specified smooth sixfold and smooth degree-one section have a nonzero full coherent restriction kernel for every prime. The all-degree crystalline assertions outside the two proved ranges, the surface coherent case, and exact intermediate degrees remain.'),
'A.3':('OPEN: exact effective rank and ordinary-product formula proved',
 'prop:effective-generic-rank; thm:product-exact-fixed-covectors; thm:all-X-explicit-positive-rank; thm:relative-ordinarity-fails-smooth',
 'The finite stable-matrix calculation gives the exact generic rank for every specified input and works over a finitely generated field of definition. Products of ordinary elliptic curves have rank d^n times product(a_i) minus one in every degree. A uniform structural formula for arbitrary X remains; relative ordinarity is refuted.'),
'A.4':('OPEN structural classification; exact effective determination proved',
 'thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data; thm:product-exact-fixed-covectors; thm:pn-char2-all-groups; thm:pn-odd-full-groups',
 'For every d>=d_coh, a proved terminating construction gives full geometric and arithmetic matrix lists over finite fields and exact finite constant data over any perfect field. It decides irreducibility for each effective input. Every projective-space image is classified structurally. Ordinary products have exactly n invariant covectors for odd p, and 2^n-1 for p=2, when p divides every a_i*d. Their full images, and a uniform arbitrary-X structural description, remain.'),
'B.3':('OPEN: sharp global minimum and one-level wild gate proved',
 'thm:B-RD12; cor:B-RD13; prop:B-RD20; cor:B-RD21',
 'All tame elliptic levels are classified. At p=3 the least absolute ramification allowing full 3^n torsion and additive reduction is exactly 2*3^(2n-2). For each fixed e the largest bad level is determined except possibly one explicitly identified level. For full9 the only undecided indices are24,30,42,48. Sharp potentially-good higher-dimensional bounds remain; unrestricted higher-level good forcing is already refuted by Tate curves.'),
'B.4':('OPEN: explicit finite bounds and a stronger p=2 obstruction proved',
 'thm:B-RD17; prop:B-RD18; cor:B-RD18; prop:B-RD22; prop:B-RD5',
 'Height1 has least index0. Explicit finite upper and lower bounds hold in every height and prime. At p=2,e=1,h>=2 even M[4] does not determine the prime-to-p character, so the least manuscript index is at least2. The exact least general-height index remains.'),
'E.2':('OPEN: flat characteristic-zero and further singular positive cases proved',
 'prop:DE-E2-flat-charzero; prop:DE-E2-cusps; prop:DE-E2-Fpure; lem:DE-crystal-Fdiv',
 'Over finite-type characteristic-zero fields the equivalence includes all flat quasi-coherent coefficients. Over perfect fields of characteristic p it includes arbitrary coefficients on F-pure schemes and on CM varieties admitting a smooth finite universal-homeomorphism cover, including the non-F-pure cusp. The full relative assertion and arbitrary nonflat characteristic-zero coefficients remain.'),
'Lead A':('REFUTED as full-GL/ordinarity prediction; residue consequence PROVED',
 'thm:product-exact-fixed-covectors; thm:pn-char2-all-groups; thm:relative-ordinarity-fails-smooth; thm:all-X-residue-density',
 'Full GL fails in infinitely many projective-space degrees in characteristic two and for an explicit ordinary abelian surface over F3 in every degree. All eventual point-count residues and positivity are proved. Complete effective image determination is proved; uniform structural classification remains separately visible.')
}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
for r in root:
 if r['id']=='A1-SMALL':
  r['statement']='Small-degree integral assertions, exact coherent degree range and surface case'
  r['notes']='General coherent injectivity is refuted by the independently audited cyclic sixfold in every prime; the integral assertions and stated narrower degree/surface gates remain.'
(w/'notes/root_results.json').write_text(json.dumps(root,indent=2)+'\n')
aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def location(text):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in text.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 05: new results and exact scope\n'
if marker in body:body=body.split(marker)[0]
new=marker+'''
### A.1: a full coherent restriction counterexample in every prime

The unrestricted coherent assertion is now refuted. Starting with the explicitly described Lauritzen–Rao sixfold R, we independently compute its canonical bundle and identify H5(R,L^{-1}) with the dual of a concrete polynomial cokernel. The apolar functional based on (u0*z1-u1*z0)^(p-2) proves nonvanishing for every prime, rather than inferring a general statement from samples. A cyclic cover y^q=b, with q=2 for odd p and q=3 for p=2, turns that nonzero class into an actual restriction kernel. The pullback of L is very ample: the cover is the hypersurface y^q=B in the projective cone, which excludes the vertex. The branch is a fully specified generic form in 896 ambient coordinates over a specified perfect field. The Jacobian and Bertini arguments prove both smoothness assertions. Multiplication by y is an identity between two direct summands of the finite cyclic algebra, so the restriction kernel is nonzero. This also works for every smooth ay+s with a nonzero.

The failure occurs at degree one for this fixed embedding. The previously proved explicit high-degree bound still gives injectivity. The exact intermediate list, the surface case and the integral crystalline assertions are not inferred from this example and remain explicit obligations. The earlier report's statement that no actual coherent kernel had been verified is superseded.

### A.3–A.4: exact product invariants and effective full images

For X equal to a product of n ordinary elliptic curves with product polarization of degrees a_i>=3, the generic relative rank is d^n*product(a_i)-1 for every d>=1. If p divides every a_i*d, the entire geometric invariant covector space has dimension n for odd p and 2^n-1 for p=2. These are equalities, not lower bounds. The proof extends a covector across parameter-space divisors, identifies its lift with an endomorphism of the section space modulo scalars, and solves the Cartier identities using the character decomposition of Frobenius. A proposed intermediate shortcut asserting that Cartier roots preserve character spaces was rejected. The repaired proof raises the identity to the pth power, uses an eigenvector and the linear parameter coefficient, and proves character-space preservation instead. The correction is recorded as part of the audit.

Over F3 the explicit surface built from y²=x³+x²+1 has relative rank9d²-1 and exactly two arithmetic and geometric invariant covectors in every degree. Over F2 the analogous explicit ordinary product has exactly three in every positive even degree. Exact finite calculations give smooth ordinary sections in degrees one and two. The full image on the kernel of these fixed quotients is not claimed to be determined structurally.

A separate theorem gives a terminating exact algorithm for the complete geometric and arithmetic matrix groups from equations over a finite field, for every d>=max(1,reg(omega_X)-1). It constructs the finite étale algebra of Frobenius-fixed frames, obtains a primitive element from a bounded grid, factors by bounded finite polynomial enumeration, and tests every matrix by exact ideal preservation. Extending constants by degree |GL_r(Fp)| suffices to isolate the geometric components. Thus the construction also decides irreducibility. A fully specified extension to a finitely generated field of definition computes finite groups H_geom normal in H0 and a finite Galois constant field E. For any perfect base k, the arithmetic image is exactly rho^{-1}(Gal(E/(E intersection k))). The only residual field datum is that finite intersection; no universal computation over an unpresented noncomputable field is asserted. The report deliberately distinguishes this effective determination from a uniform description of all outputs as familiar finite groups. The latter remains the A.4 structural gate.

### B.3–B.4 and E.2

The higher wild characteristic-three argument proves that the maximum primitive formal valuation is divisible by three. It uses the Hesse-pencil cube-discriminant identity and a lower-ramification leading-coefficient argument. The resulting exact global minimum is e_min(n)=2*3^(2n-2). At each fixed e the largest possible bad full-torsion level lies between two explicit adjacent integers; except for the displayed one-level gap the answer is exact. For full9 the remaining indices are precisely24,30,42,48. This is a strictly smaller gate than the previous unrestricted higher-wild problem.

At p=2,e=1, the curve y²=x(x-1)(x+3) over Q2(zeta3) has E[4] isomorphic to mu4 direct sum Z/4, while its prime-to-2 inertia character differs from that of the split good group. Its discriminant valuation8 forces good-reduction ramification divisible by3, and the order-three trace is -1 instead of2. Therefore even manuscript level1 fails to determine the character in every height at least2. The precise minimum beyond this lower bound is still open.

For E.2, the characteristic-zero result extends to all flat quasi-coherent coefficients by a finite nilpotent filtration argument in the derived category. In characteristic p, a separate theorem covers all quasi-coherent coefficients on integral CM varieties with a smooth finite universal-homeomorphism cover. This includes the cusp k[t²,t³], whose Frobenius is not pure for any prime. The original Ben-Zvi–Nevins statements, including their ordinary pullback convention, were reopened and checked. General relative bases and arbitrary nonflat characteristic-zero coefficients remain open.

### Computational scope and independent checks

`code/coherent_restriction_counterexample.py` passed in0.668855 seconds. It checks all relevant monomial incidence relations for p=2,3,5,7,11,13, the characteristic-two40-to35 matrix of rank34, and cyclic multiplication. Generic smoothness and the all-prime conclusion use the written proofs. The root rerun of `ordinary_abelian_surface.py` took14.158152 seconds and verified four unit Jacobian ideals, Cartier rank36, relative rank35, four independent character components and seven F2-points. The degree-one certificate records the equation and Cartier matrix separately. The root rerun of `product_surface_obstruction.py` took0.047037 seconds and checked the F3 curve and its rational three-torsion.

The root independently read and reran `lang_frame_quartic.py` in0.186606 seconds. For the genuine family x4+y4+z4+x²yz+xz³+txy³+xyz², it verifies all three smoothness charts, its ordinary Hasse matrix, a six-dimensional frame algebra, all six GL2(F2) substitutions and a primitive polynomial. A simple Artin–Schreier pole proves geometric irreducibility, giving exactly diag(1,GL2(F2)) for this restricted family. This is not a claim about the full plane-quartic parameter space. The B.4 certificate checks all16 torsion points, all256 sums and all256 Galois compatibilities with exact arithmetic; a separate independent agent rerun passed. The wild-bound program checks the integer reductions within its stated finite range; it supplements the general proof.

All new theorem promotions follow independent proof checks. The paper and table retain six open main rows with narrower gates. Checkpoint production is not counted as mathematical movement, and the next scheduled substantive review remains due at06:50:40 UTC.

'''
log=w/'notes/ROOT_SEARCH_LOG_05.md'
if log.exists():new+='\n'+log.read_text()+'\n'
new+='\n'+(w/'notes/SOURCE_CENSUS.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+new)
events=w/'notes/root_check_events.tsv';existing=events.read_text()
audits={
'A1-CYCLIC-ROOT':'Complete cyclic-cover restriction-kernel construction; very ampleness via vertex-free projective cone; smooth branch and cover; canonical bundle and sixfold cokernel; all-prime apolar functional. Independent monodromy-agent audit passed.',
'A4-ABELIAN-PRODUCT-ROOT':'Original SannaiTanaka Lemma4.5 checked. Frobenius character splitting, Cartier covectors, exact product rank and all invariant covectors independently re-proved. False unproved Cartier-root weight preservation was repaired by a pth-power eigenvector argument. Exact scripts read and selected certificates independently rerun.',
'A4-FRAME-ALGORITHM-ROOT':'Full finite algorithm audited: stable linearization; finite étale frame algebra degree; bounded primitive grid; finite polynomial factor enumeration; ideal stabilizers; finite constant extension bound; subspace irreducibility tests. Genuine quartic certificate independently executed.',
'A4-PERFECT-CONSTANTS-ROOT':'Separating-basis and shifted-norm factorization; bounded absolute-factor existence tests and terminating coefficient search; coefficient recovery of the finite Galois constant field; exact E-intersection-k formula. Original Stacks037P/037Q/030W/030X checked.',
'B-HIGHER-WILD-ROOT':'Independent proof and original-source audit of Hesse cube discriminant, invariant differential, wild lower break, primitive leading-coefficient contradiction, sharp minimum and one-level fixed-e gate; AnemaTopTuijp Thm1.1/Prop5.1 opened.',
'B-P2-LEVEL4-ROOT':'Independent exact proof check of E[4]=mu4 plus Z/4, minimal discriminant8, potential supersingular good reduction, inertia3 and trace discrepancy; separate obstructions-agent exhaustive finite certificate rerun passed.',
'E2-FLAT-CUSP-ROOT':'Independent nilpotent derived-flatness filtration proof and universal-homeomorphism Frobenius-shift descent; original BenZviNevins2.7/2.11/3.11/4.3/4.5 and Stacks0CNF reopened. General relative scope expressly retained.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with events.open('a') as f:
 for sid,desc in audits.items():
  if sid+'\t' not in existing:f.write('\t'.join([sid,now,'GPT-6 Astra (OpenAI); /root; inherited effort','independent re-proof',desc])+'\n')
print('Fifth-checkpoint current findings, scope and audit records refreshed; no scheduled review fabricated.')
