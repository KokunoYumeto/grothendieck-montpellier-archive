"""Refresh checkpoint07 findings without rewriting historical reviews."""
from pathlib import Path
import datetime,json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.4':('OPEN: uniform product groups reduced to a geometric irreducibility hypothesis',
 'thm:product-full-group-if-hasse-irreducible; prop:product-hasse-reduced; lem:product-degree-three-block; thm:product-all-degree-transvections; thm:product-char2-all-parities-fixed-quotient; thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data',
 'All projective-space images and complete effective matrix constructions for arbitrary input remain proved. On the fixed ordinary product surface, full groups in degrees1,2,3, all-degree transvection generation, exact parity covectors and geometric Hasse reducedness are proved. A new complete conditional theorem gives the full predicted groups in every d>=3 if its Hasse divisor is geometrically irreducible; it includes a natural GL80 block and all even-degree translations. Geometric irreducibility of that explicit divisor remains unproved for all higher degrees. Actual full product images from degree4 onward and uniform arbitrary-X structural classification remain open.'),
'A.1':('OPEN exact degree ranges; universal integral (a),(b),(c) all refuted',
 'thm:OC-integral-injectivity-counterexample; cor:OC-all-prime-integral-counterexample; thm:OC-explicit-integral-counterexample; cor:OC-surface-exact-degrees; thm:A-all-degree-ranges; A1-HIGH',
 'In every characteristic an explicit very ample threefold has extra crystalline H2 torsion on every smooth degree-one section, refuting(a),(b). A separate characteristic-two threefold with843 root equations has a nonzero crystalline H2 restriction kernel killed by2 for every smooth degree-one section, refuting(c). Coherent injectivity is refuted on surfaces in every prime; its characteristic-two example has kernel dimension1 in degree1 and0 in all higher degrees. The remaining A.1 task is the exact intermediate integral degree ranges in these fixed embeddings, beyond the proved failure and explicit high-degree positive bounds.'),
'B.3':('OPEN: full-nine range and finite elliptic decision test proved; first full27 case unevaluated',
 'prop:B-RD24-finite-test; thm:B-RD23; thm:B-RD12; cor:B-RD13; prop:B-RD20; cor:B-RD21',
 'All tame elliptic levels are classified. At p3, full9 with additive reduction exists exactly when6 divides e and e>=18. The sharp global minimum for full3^n is2*3^(2n-2), and fixed-e wild ambiguity is at most one explicit level. A bounded polynomial formula over Fpbar now decides each remaining elliptic input and proves finite-local-field realization if affirmative. Its first remaining case full27 at e216 is not evaluated. Sharp potentially-good higher-dimensional thresholds remain.')
}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
for r in root:
 if r.get('label')=='open:A-small-degree':
  r['statement']='Exact intermediate integral degree ranges after explicit counterexamples to all three universal assertions'
  r['notes']='A.1(a),(b) are false in every characteristic and(c) is false in characteristic two by explicit degree-one threefolds. Coherent injectivity is false on explicit surfaces, with exact characteristic-two coherent degrees. Exact intermediate integral degree conditions remain.'
(w/'notes/root_results.json').write_text(json.dumps(root,indent=2)+'\n')
aux=(w/'RESEARCH_SA15_paper.aux').read_text() if (w/'RESEARCH_SA15_paper.aux').exists() else ''
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def location(text):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in text.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 07: integral counterexamples and a finite elliptic test\n'
if marker in body:body=body.split(marker)[0]
new=marker+'''
The opening table gives the current status; previous checkpoint sections are dated history. This checkpoint remains INCOMPLETE. It closes all three universal yes/no assertions A.1(a),(b),(c) negatively while retaining their exact-degree obligations.

### A.1(a),(b): explicit integral counterexamples for every prime

For a smooth proper geometrically connected V, write q=h1(O_V), h10=h0(Omega1_V), b=rank_W H1_cris and t=dim H2_cris[p]. Derived crystalline base change in degree0 makes H1_cris free, and degree1 gives h1_dR=b+t. The Hodge and conjugate spectral sequences, without degeneration assumptions, give q-b<=t<=q+h10-b. The exact Cartier and conjugate edge passages in Illusie's1979 original were checked separately from this proof.

Take the previously constructed very ample surface (X,A) with a=h1(A^-1)>0, form Z=X times P1, and embed it with B=A external tensor O(m). For every smooth Y in |B|, the divisor sequence and Kunneth give q(Y)=q(X)+a(m-1). Rational crystalline weak Lefschetz identifies the two first crystalline ranks and makes H2(Z) to H2(Y) rationally injective. Therefore t(Y)-t(Z)>=a(m-1)-h10(X). Choose m so that this is positive. The torsion group on Y then needs strictly more generators than the source torsion, so restriction is not surjective on torsion. Rational injectivity identifies im(u) intersect T(Y) with u(T(Z)); the resulting nonzero torsion quotient embeds in coker(u). Both asserted integral conclusions fail.

The construction is numerical, not conditional on an unknown dimension. In characteristic2 the tame cubic-cover surface has at most35 global one-forms, and the556 ninth-root covers give h10(X)<=591*9^556. Thus m=591*9^556+2 suffices. The fixed X is embedded in P561; the Segre–Veronese product gives the displayed threefold embedding. Independent generic coefficients specify the smooth section over a specified algebraically closed field.

For every prime, put ell=p+1, q0=ell², n0=2 at p2 and n0=p(p-2) otherwise, and g=1+p*ell*n0/2. The first tame cover has at most Bp=g+p+2+p³(p+1)n0/2 global one-forms. The theorem gives an exact finite sum r=h0(L^q0) by Riemann–Roch on the explicitly filtered eigensheaves. The r simultaneous q0th-root covers give h10(X)<=q0^r(Bp+r), so m=q0^r(Bp+r)+2 produces the integral counterexample. The all-prime formulas and local differential inclusions were independently audited, and the arithmetic verifier was independently run for p2,3,5,7,11,13,17,19.

These results prove degree-one failure. They do not yet determine every intermediate integral degree below the existing explicit regularity bound. In particular, coherent equality in degrees>=2 for the characteristic-two surface does not imply integral saturation. Even an isomorphism on p-torsion subgroups would not suffice: multiplication by p maps W/p injectively into W/p² and is an isomorphism on those subgroups.

### A.1(c): an explicit nonzero integral kernel

The additional counterexample begins with the smooth model of y²+y=x843, of genus421, with exact differential divisor840 times infinity. Two explicitly normalized Tango covers, of degrees21 and5, produce a smooth projective threefold R with an ample generated L, H1(L^-2) nonzero, L^445 very ample, and first Betti number842. Every cyclic eigensheaf, local smoothness condition, gluing formula and positive-section sign is derived directly. The very-ample bounds441 and445 follow from explicit filtrations and length-two evaluation vanishing. The exact arithmetic program checks52,026 normalization identities and the displayed degree bounds; h0(L^445)=79,232,578,014 is also calculated.

Choose843 generic sections of L^445, with the first eight defining an immersion into P7, and take all843 independent445th roots. The resulting X is smooth, connected and projective, of degree445^843 over R. The root sections turn A=pullback(L) into a very ample bundle. The direct-sum eigensheaf formula gives h1(A^-1)>=843. Every nontrivial character contributes compact-support H1 on a smooth affine threefold; affine vanishing and Poincare duality make this zero. Hence X still has first Betti number842.

For every smooth hyperplane Y, the coherent restriction kernel has dimension at least843. The natural conjugate edge map puts it into the de Rham restriction kernel. In the crystalline universal-coefficient sequence, H1_cris(X)/2 has dimension842, so some element maps nontrivially to H2_cris(X)[2]. Naturality makes that nonzero torsion element restrict to zero on Y. This proves that integral crystalline restriction need not be injective. The complete proof passed root and reduction-descent audits, with exact SGA4 and Illusie locators checked and the arithmetic certificate independently executed. The theorem asserts degree-one failure; its intervening degree classification remains open.

### A.4: a conditional uniform group theorem with one geometric hypothesis

On the fixed characteristic-two product surface, the full Hasse polynomial is geometrically reduced in every degree. At the generic point of any component, the already proved stable rank drop one gives a right kernel u and left kernel ell with ell(u^[2]) nonzero. Symmetry of Cartier multiplication and beta(u,u)=u^[2] make the derivative of the determinant in direction u nonzero. Repeated factors on a test pencil therefore represent tangencies; they do not imply repeated global components.

The new conditional theorem proves that geometric irreducibility of this divisor would force geometric and arithmetic group GL_(9d²-1)(F2) for every odd d>=3, and the full stabilizer 2^[3(9d²-4)] semidirect GL_(9d²-4)(F2) for every even d>=4. Its proof is complete under that explicit hypothesis, and the hypothesis remains unproved. A saturated invariant subsheaf of the cotangent bundle must receive the entire reduced irreducible determinant divisor: a zero divisor would give a Frobenius-periodic reflexive sheaf, which is locally free by Fitting ideals and trivial by a Lang frame cover, contradicting H0(Omega_P)=0. Every proper invariant quotient is consequently constant, making the common kernel of all known covectors irreducible.

The required large linear subgroup is obtained uniformly from a degree-three curve united with fixed ordinary degree-one curves. Each moving intersection contributes at most S54, and the whole constant-kernel representation is an extension by a2-group, so it cannot share the simple GL80 quotient and its large prime4278255361. Goursat and the independently proved vanishing of H1(GL80,natural or dual) produce an actual natural80 block with trivial complement. This excludes every form-preserving alternative in the checked transvection-group classification. Finally the vanishing of invariant vectors forces the entire translation subgroup in even degree. The root audited each step, including the potentially nonsplit constant-kernel filtration; a quotient surjection alone is not used as a subgroup.

The remaining geometric question is the irreducibility of this particular reduced Hasse divisor. Neither generic stable rank loss one nor a generic-matrix determinantal estimate proves it. The theorem is recorded as a conditional reduction and is not reported as the actual all-degree image classification.

### B.3: exact finite test, with the first wild output still unknown

For every odd p, absolute ramification e and level n, the new proposition gives a finite polynomial test equivalent to the existence of an additive elliptic curve with full rational p^n torsion. The coefficient ring is a length-q Witt ring with a degree-e Eisenstein uniformizer relation. Universal Weierstrass changes detect minimality at bounded precision. A scaled monic division polynomial F and a scaled quadratic G give all nonzero torsion points. Explicit discriminant bounds control every root separation and Jacobian determinant; the adjugate Hensel argument proves that the specified approximate roots lift to the exact required torsion.

Effective elimination over algebraically closed characteristic-p fields decides the finite formula. Its coefficients lie in Fp, so an affirmative result gives a solution over a finite residue field and hence a finite extension of Qp. The proof distinguishes arbitrary perfect residue fields from Fpbar and uses transfer of this finite formula, rather than identifying the two fields. The division-polynomial discriminant constant is defined by an exact rational computation at y²=x³-x; no unproved general closed formula is assumed.

The root independently reran the polynomial certificate in74.23945297700266 seconds. All nine polynomial cases and2000 bound cases passed, including the degree364 polynomial for full27. For p3,e216,n3 the test's conservative precision is459518627 in the uniformizer, corresponding to Witt length2127402. The enormous quantified test has not been evaluated there. Thus the first full27 existence question remains open, as do the sharp higher-dimensional potentially-good thresholds. A finite test is not reported as a numerical yes/no result.
'''
log=w/'notes/ROOT_SEARCH_LOG_07.md'
if log.exists():new+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+new)
events=w/'notes/root_check_events.tsv';existing=events.read_text()
audits={
'A1-INJECTIVITY-ROOT':'Complete independent proof audit: positive-section Tango gluing, normalized eigensheaves and exact differential iteration;843 curve,21/5 covers,441/445 jet bounds;843-root smooth connected very-ample cover; character j_! decomposition, affine H1c vanishing and Betti842; conjugate kernel dimension843 and UCT nonzero H2cris[2] kernel. Read retypeset original SGA4III XII5.1/5.2pp88–89, XIV3.1/3.2p160, XVIII3.2.5/3.2.6.2pp585–587, and Mukai Theorem1 proof/Proposition2.3. Full arithmetic code read and independently executed, outputs/root_A_injectivity_checks.json PASS. Exact intervening degrees not claimed.',
'A4-HASSE-CONDITIONAL-ROOT':'Complete independent line-by-line audit of geometric Hasse reducedness, Frobenius-periodic reflexive triviality, determinant allocation on Omega_P, the boundary GL80 block with whole T0 kernel killed, elementary simplicity, Goursat and natural-dual H1 splitting, form exclusion and all translations. The uniform group theorem is PROVED UNDER the explicitly unproved geometric Hasse-irreducibility hypothesis; no actual higher-degree image classification is inferred without it.',
'A1-INTEGRAL-ROOT':'Full independent audit of crystalline universal-coefficient and two spectral-sequence inequalities, Kunneth q-growth, rational weak Lefschetz, torsion-generator obstruction and torsion intersection. Local tame-log differential inclusion and explicit591*9^556 bound rederived. Original Illusie1979 Cartier0.2.1.9p515, II3.11/3.11.2pp618–619, II6.14p649; NakkajimaYobuko2022v3 Appendix9 Theorem9.1/Corollary9.3pp63–64 read. A.1(a),(b) refuted; injectivity and intermediate degrees not inferred.',
'A1-INTEGRAL-ALL-PRIMES-ROOT':'Independently rederived Bp and exact eigensheaf Riemann–Roch sum r, checked all line degrees exceed2g-2 and the q^r logarithmic bound, read entire all-prime proof, and independently executed A_integral_checks.py. Output outputs/root_A_integral_checks.json PASS for eight primes; p2 exactly recovers35 and556.',
'B-FINITE-ELLIPTIC-ROOT':'Full independent audit of bounded Eisenstein/Witt coefficient rings, minimality translations, both discriminants, exact adjugate Hensel lifting, root separation and finite elimination. Original Burhanuddin section1.1.3pp8–9 and Stacks032A Theorem10.160.8 read. Independent polynomial/bound run PASS74.23945297700266s, output outputs/root_verify_finite_elliptic_test.json. First27/e216 quantified decision not evaluated.'
}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with events.open('a') as f:
 for sid,desc in audits.items():
  if sid+'\t' not in existing:f.write('\t'.join([sid,now,'GPT-6 Astra (OpenAI); /root; inherited effort','independent re-proof',desc])+'\n')
print('Checkpoint07 current findings updated; historical actual reviews preserved.')
