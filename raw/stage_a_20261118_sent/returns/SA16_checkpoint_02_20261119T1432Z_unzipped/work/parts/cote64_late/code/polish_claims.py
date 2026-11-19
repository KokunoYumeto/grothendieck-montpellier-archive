"""Human-authored wording edits and exact locator expansion; no verdict inference."""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
C=json.loads((B/'claims.json').read_text()); K=json.loads((B/'claim_keys.json').read_text()); by={x['id']:x for x in C}
def edit(key,**kw):by[K[key]].update(kw)
fates={
'square':'The rotation group is elementary; the author already deleted the star that would turn the group into a two-point torsor. LG-GROUP.',
'fixedpin':'The fixed-square isomorphism torsor is standard descent. Antieau–Meier give the Legendre root atlas; the separate symmetric normalization belongs to C-SA16-505. LG-PIN.',
'residual':'Classical elliptic stabilizers; the restriction to even permutations is checked independently. Characteristic 3 needs its own fixed-scheme analysis. LG-PIN.',
'rootstorsors':'Torsor descent is standard; an independent pair of inverse functors is supplied. LG-PIN.',
'ellipticroots':'The Legendre root atlas supplies the split local model. Descent for a cubic étale J and the exact tangent-square identification remain comparison obligations. LG-PIN.',
'choosei':'Elementary trivialization of a torsor after explicitly choosing i. LG-PIN.',
'gradedderivation':'An invariant derivation raises pole order by at most one and gives a degree-one derivation of the Rees ring. LG-ALG.',
'symbol':'The displayed all-degree coefficient 1 fails the Leibniz rule. Ordinary principal parts give the corrected coefficient −n. LG-ALG.',
'kernel':'The differential-kernel theorem gives the exact filtered correction in positive characteristic; the page imposes no characteristic-zero restriction. LG-ALG.',
'Reeskernel':'The graded ring requires a correction even in characteristic zero. It must be distinguished from the filtered union. LG-ALG.',
'parity':'Polynomial bases verify the parity filtration. The uncertain target indices and signs remain scan questions. LG-ALG.',
'wpbasis':'A nonzero tangent vector is necessary; scan 115 states that hypothesis explicitly. The corrected construction is standard. LG-ALG.',
'monic':'The normalization of ε_n is unstated. Two coherent alternatives have different cubic leading coefficients, so no unique ink correction follows. LG-ALG.',
'restriction':'The author completes this argument on scan 106. The restriction map and its kernel have been independently checked. LG-ALG.',
'cubicsigns':'Standard cubic factorization; the literal degree-two and negative-constant alternatives are incompatible with the surrounding formulas. LG-ALG.',
'differentialalgebra':'The derivation of the quotient algebra is standard. Two ambiguous printed alternatives fail the defining relation. LG-ALG.',
'det':'The author supplies distinctness on scans 110–111. The divisor group law gives the exact determinant criterion. LG-ALG.',
'secant':'The chord formula is checked on its stated domain, including the negative-sum convention. LG-ALG.',
'affinewp':'The branch quotient determines x up to an affine change; a fixed nonzero tangent vector leaves only translation. LG-ALG.',
'Mobius':'Translation by nonzero two-torsion descends to the stated Möbius involution. The exact rational-function identity has been checked. LG-ALG.',
'fourdivision':'The chord law gives twelve points of exact order four over an algebraically closed field of characteristic different from two. LG-ALG.',
'divisionbad':'The radical assembled on scan 118 contradicts the correct identity on scan 116. LG-ALG.',
'level4map':'Conrad, Proposition 3.2, supplies a canonical map from ordered level-four data to ordinary Legendre structure. Its equality with the symmetric normalization in equation 73 is not identified in the sources opened. LG-PIN.',
'weight':'Tensor weight gives independence of the tangent basis. It does not define a connection. LG-LINEAR.',
'lattice':'The lattice description already appears in Grothendieck’s Cartan X introduction (1961). Hain provides a modern detailed treatment. LG-AN.',
'complexstructure':'Linear algebra gives the bijection. The second expression in equation 8 requires an inverse. LG-AN.',
'circle':'Faithfulness forces the two weights to be ±1. The orientation and invariant-metric statements follow by elementary real linear algebra. LG-AN.',
'orientation':'The negative determinant confirms the author’s withdrawal on scan 135 and his revised line convention on scan 139. LG-AN.',
'antiholo':'The literal first-draft parameter is antiholomorphic. The second draft supplies a holomorphic period parameter. LG-AN.',
'analyticfine':'Representation by the framed family is classical; Hain, Sections 2.3–2.4, provide the precise modern comparison. LG-AN.',
'rightaction':'The matrix convention and its conversion from a right action to a left action have been independently checked. LG-AN.',
'cocycle':'The universal automorphy-factor identity is checked directly; compare Hain, Section 2. LG-AN.',
'semidirect':'The exact action on lattice translations depends on their written order and has been checked. LG-AN.',
'cover':'The stack covering is standard. The literal assertion that the total family is that universal cover is false. LG-AN.',
'mappingclass':'The mapping-class action on rank-two homology is classical. It does not require the erroneous rank-one parenthesis. LG-AN.',
'outer':'Bux–Ershov–Rapinchuk, Section 3, recall Out(F2)≅GL2(Z), with a reference back to Magnus–Karrass–Solitar (1966), Section 3.5. LG-AN.',
'frames':'The double-frame parameterization follows from lattices; Hain, Proposition 5.16, identifies the Hodge line with the cotangent line. LG-AN.',
'free':'The diagonal central pair has fixed points, in agreement with the author’s correction. LG-AN.',
'split':'The cancelled multiplication formula is valid for every split extension. Its surrounding specific diagram remains unidentified. LG-GROUP.',
'squareclasses':'Kummer theory and unique factorization give the canonical representative. LG-ARITH.',
'DVR':'Under the DVR hypothesis the criterion is elementary and is proved here. The manuscript’s term “anneau jauge” remains undeciphered. LG-ARITH.',
'nonsquare':'A one-dimensional regularity argument proves normality. This does not imply that the extension is étale. LG-ARITH.',
'dyadic':'The first-order obstruction and the missing integral generator have been independently verified. LG-ARITH.',
'completion':'Exactness of completion identifies the T-adic object. Equality with the local completion requires b≠0 in the stated argument. LG-ARITH.',
'node':'Tangent-cone separability is standard. The unrestricted claim of an ordinary node fails. LG-ARITH.',
'global':'Serre’s R1 and S2 criterion strengthens the allowance of finitely many exceptions to global normality under the stated hypotheses. LG-ARITH.',
'generic':'The quadratic integral generator and Serre’s criterion prove the precise sufficiency assertion. No source with this exact specialized formulation was located. LG-ARITH.',
'sign':'The test fails if Q means the unsigned primitive factor. There is no sign error if Q abbreviates the full radicand P. LG-ARITH.',
'modfour':'Comparing coefficients proves the criterion modulo four and refutes the literal equivalence modulo two. LG-ARITH.',
'infinity':'The coordinate change forces the opposite sign. The normalization of the corrected chart is étale on the stated open set. LG-ARITH.',
'tangentcone':'The final incomplete calculation is compatible with the tangent-cone test. LG-ARITH.',
'scratchdiagram':'The cancelled diagram supplies insufficient data for an exact group-extension assertion. LG-GROUP.'}
for key,val in fates.items():
 x=by[K[key]]; old=x['fate'];x['fate']=val
 if x['present_status']==old:x['present_status']=val
edit('fixedpin',**{'class':'E'},statement='Assume 2 is invertible on S. Fix E/S and α:μ4*≅ω_J. Isomorphisms from its tangent line to the specified root line that respect the square form a μ2-torsor, locally nonempty for the étale topology. This asserts no global section.')
edit('allpin',statement='Allowing α to vary gives a μ4-torsor L_E/S with L_E/S/μ2≅μ4*∧ω_J. The naive torsor Q_E/S has quotient ω_J, and the proposed comparison is L_E/S≅Q_E/S∧μ4 Q0.')
edit('baseaction',statement='For 2 invertible, μ4×S3 acts on U03×μ4* through g on U03 and sgn(g)λ² on μ4*. The stabilizer of a chosen i is the fibre product D3′.')
edit('rootstorsors',statement='If a line L on S has a chosen square root (T0,β0), the groupoid of roots (T,β:T⊗2≅L) is equivalent to the groupoid of μ2-torsors. The functors are Isom_square(T0,T) and twisting T0 by a μ2-torsor.')
edit('RR',statement='For a smooth projective genus-one curve E/k with k-rational O, F_n=H0(E,O(nO)) has dimension n for n≥1, and F0=F1=k. For n≥2, F_n/F_(n−1) is the one-dimensional principal-part line t_E⊗n.')
edit('gradedderivation',statement='A tangent vector δ determines a translation-invariant derivation Dδ with Dδ(F_n)⊂F_(n+1). On R=⊕F_n T^n, the rule D(fT^n)=Dδ(f)T^(n+1) satisfies the graded Leibniz identity.')
edit('parity',statement='In characteristic different from two, negation splits F_n into even and odd parts. The invariant derivation switches parity and raises pole order by at most one. Multiplication respects products of signs. The functions x^j and x^j y have pole orders 2j and 2j+3.')
edit('differentialalgebra',statement='Let char(k)≠2 and A=k[x,y]/(y²−f(x)), with f=x³+a1x²+a2x+a3. Then D(x)=y and D(y)=f′(x)/2 define a derivation. With this D, replacing a2x by a2x² is incompatible; replacing D²(x)=f′/2 by D(x)=f′/2 is also incompatible.')
edit('affinewp',statement='For char(k)≠2, the quotient E/±1 is P1 via a degree-two function x sending O to infinity. The coordinate x is unique up to ax+b with a≠0. Fixing its principal part by a nonzero δ fixes a. If char(k)≠3, translating x makes the sum of the three finite branch values zero.')
edit('fourdivision',statement='Over an algebraically closed field of characteristic different from two, the halves of ε=(r,0) have x=r±sqrt((r−u)(r−v)). Each of the two x-values has two nonzero y-values, giving four halves of each ε and twelve points of exact order four. Halves of three distinct nonzero two-torsion points are distinct, so the determinant criterion for sum zero applies.')
edit('weight',statement='If φ_i(λδ)=λ^(−1)φ_i(δ), then φ_i(δ)δ is independent of the nonzero tangent basis δ. The resulting vectors sum to zero and give the same kernel line when nonzero. Their tensor-square normalization is a separate condition.')
edit('lattice',statement='Over C, an elliptic curve is V/H with V a complex line and H a lattice of rank two. Its underlying real Lie group is H_R/H. Conversely such a lattice quotient is a complex elliptic curve.')
edit('complexstructure',statement='A complex structure J on a real vector space V corresponds to a complex subspace L⊂V_C for which Re:L→V is a real isomorphism, by J=−Re∘i∘Re^(−1). Its inverse is L={x+iJx:x∈V}=ker(V_C→V_J). In real dimension two, these are exactly the nonreal lines in P(V_C).')
edit('analyticfine',statement='For a holomorphic family of complex elliptic curves with an oriented global basis of H1≅Z², the period ratio τ is a holomorphic map into the upper half-plane. The family is canonically the pullback of (H×C)/Z². An automorphism preserving the homology basis is the identity.')
edit('cocycle',statement='For g∈SL2(Z), the map (τ,z)↦((aτ+b)/(cτ+d),z/(cτ+d)) defines a left action on H×C and descends through lattice translations. Its denominator satisfies j(g,hτ)j(h,τ)=j(gh,τ).')
edit('mappingclass',statement='The orientation-preserving mapping-class group of an oriented torus with one marked point is SL2(Z), acting on H1≅Z².')
edit('outer',statement='For Π=π1(E minus O)≅F2, its abelianization is Z² and its outer automorphism group preserving the peripheral orientation is SL2(Z). The pages request an explicit outer action. In a chosen free basis, lifts S:(x,y)↦(y,x^(−1)) and T:(x,y)↦(x,xy) give it modulo inner automorphisms.',present_status='The identification is classical. The explicit lifts are earlier-run additions checked here. The first draft’s rank-one parenthesis is refuted; R-C-SA16-550 replaces it by rank two.')
edit('squareclasses',statement='Every class in Q(T)^*/Q(T)^{*2} has a unique representative εqQ, where ε=±1, q is a positive squarefree integer, and Q is a product of distinct primitive irreducible integer polynomials with positive leading coefficients. The empty product is allowed. A genuine quadratic field extension excludes the trivial square class.')
edit('nonsquare',statement='For a DVR A with residue field k of characteristic two, if a is a unit and its residue is nonsquare, B=A[S]/(S²−a) is a DVR with maximal ideal πB and residue field k(sqrt(abar)). The residue extension is inseparable, so B/A is not étale.')
edit('tangentcone',statement='Over a residue field of characteristic two, X²+αXY+βY² has two distinct geometric linear factors exactly when α≠0. The incomplete calculation on scan 157 gives no further global normality theorem.')
edit('scratchdiagram',statement='The cancelled diagram appears to have kernel ker(F2^A→F2) and quotient S_A, but the set A, the action, and the extension class are not defined in the fragment. Only the general split-extension multiplication identity can be checked.')
status={
 'tensor':'Refuted as written. R-C-SA16-502 gives (M^sharp)⊗2≅(M⊗2)^b. On P1_C with trivial torsors the literal formula equates degrees two and one.',
 'symbol':'R-C-SA16-518 gives gr_n(Dδ)=−n μδ for ordinary principal parts, or −nc μδ after ε_n=c^n pp_n. No multiplicative convention makes every coefficient equal to one.',
 'kernel':'R-C-SA16-519 gives the pth-power filtered kernel. For nonzero δ over an algebraically closed field of odd characteristic p, x^p∈F_(2p) is a nonconstant kernel element. It also belongs to F_(2p+1), refuting the proposed rescue p∤n.',
 'Reeskernel':'R-C-SA16-520 gives ker(D)=k[S] in characteristic zero and R^p[S] over a perfect field of characteristic p, where R=⊕F_nT^n and S=1T. The filtered union has kernel k or F∞^p, respectively.',
 'wpbasis':'R-C-SA16-522 requires δ≠0. At δ=0 the prescribed x lies in F1 and y=0, so the displayed bases fail. For δ≠0 their distinct pole orders give the bases. This refutes only the locally unqualified literal wording.',
 'monic':'No blanket factor-four correction is adopted. Ordinary principal parts give leading coefficient four; ε_n=(−1/2)^n pp_n gives a monic cubic. Both conventions leave the all-degree error in C-SA16-518.',
 'divisionbad':'R-C-SA16-534 has −3uv inside a1r+2a2−3uv and constant a2−2uv. Distinct roots 1,2,3 over Q give the correct radical 2 and the written radical −34.',
 'level4map':'The request on scan 93 resumes on scan 118. Equations 83b and 83c separate the line and its scale. Conrad settles a canonical ordered construction; the exact symmetric comparison remains a finite archival task, not an established modern open conjecture.',
 'antiholo':'R-C-SA16-543 uses a holomorphic period parameter τ. Scan 139 explicitly questions analytic naturality. With the homology frame fixed, periods must depend holomorphically on the base.',
 'cover':'R-C-SA16-548 is the universal orbifold cover H→[H/SL2(Z)]. The total family has fundamental group Z². The coarse j-line also loses the stabilizer data.',
 'DVR':'The theorem is true with the DVR hypothesis. A general regular local ring does not suffice: Q[[x,y]][S]/(S²−xy) is normal although xy∈m². No hypothesis is silently substituted for the uncertain word.',
 'node':'R-C-SA16-559 requires v(2)=1 for an ordinary node in the sense of two distinct geometric tangent lines. The equal-characteristic-two cusp and a ramified mixed-characteristic example satisfy the written square-residue conditions but have doubled tangent lines.',
 'generic':'True for a primitive squarefree radicand defining a quadratic field, with normalization understood. Necessity and sufficiency at the generic points of all integer fibres are proved in proof_notes.md. The original S²=P order is never étale in characteristic two.',
 'sign':'R-C-SA16-562 applies the test to the full signed radicand P=εqQ. If Q is shorthand for P, there is no error. If Q is unsigned, P=−1 and P=3 with Q=1 are counterexamples. The ink is not decided.',
 'modfour':'R-C-SA16-563 uses modulus four. The value λ=2 refutes only the literal equivalence with a square congruence modulo two. The mathematical alternatives are kept distinct from the reading.',
 'infinity':'R-C-SA16-564 uses δ²=1−λT′. At λ=4 and T′=0 the written radicand gives Q(i), ramified at two; this point lies in the stated open set.'}
for key,val in status.items():edit(key,present_status=val,status_detail=val)
# Exact filenames in every physical-line locator.
def normalize(v):
 if isinstance(v,str):
  for p in ('MPL_64_078-115','MPL_64_116-157'):v=v.replace(p+':',p+'_transcription.tex:')
  return v
 if isinstance(v,list):return [normalize(x) for x in v]
 if isinstance(v,dict):return {k:normalize(x) for k,x in v.items()}
 return v
C=normalize(C)
(B/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
I=normalize(json.loads((B/'items.json').read_text()));(B/'items.json').write_text(json.dumps(I,ensure_ascii=False,indent=2)+'\n')
R=normalize(json.loads((B/'refinements.json').read_text()));rb={x['id']:x for x in R}
for key in status:
 id='R-'+K[key]
 if id in rb:rb[id]['qualification']=status[key]
if 'R-C-SA16-550' not in rb:R.append({'id':'R-C-SA16-550','refines':'C-SA16-550','statement':'The once-punctured torus has fundamental group F2 and abelianization Z², of rank two.','attribution':'Independent topological correction; no change to the transcript.'})
rb['R-SA16-L64-Hain315']['statement']='Use the twisted S3 descent action on the Bμ2 Legendre atlas. A literal strict quotient by C2×S3 with C2 trivial on the base cannot be M11: its harmonic stabilizer is C2×C2 instead of C4.'
rb['R-SA16-L64-Hain315']['attribution']='Independent stabilizer comparison in this run; Antieau–Meier, Lemma 4.7, gives the twisted action.'
(B/'refinements.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print('Polished 66 claims and expanded all 99 item locators. Added explicit rank-two refinement.')
