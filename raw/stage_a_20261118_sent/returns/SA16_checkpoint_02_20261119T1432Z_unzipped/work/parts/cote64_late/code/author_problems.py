"""Individually authored problem records from the complete readings."""
import json
from pathlib import Path
B=Path(__file__).resolve().parents[1]; P=[]
A='MPL_64_078-115_transcription.tex'; Z='MPL_64_116-157_transcription.tex'
def p(title,occ,words,plausible,art,why,worth,refs,items,claims,state):
 P.append(dict(id=f'MP-SA16-{161+len(P)}',title=title,occurrences=occ,as_he_states=words,plausible_today=plausible,state_of_art=art,why_open=why,worth=worth,refs=refs,items=items,claims=claims,closure_status=state,as_of='2026-11-19'))
p('Reconstruct the elliptic curve from branch and pinning data',
 [dict(cote=64,scans=[83],lines=A+':146–154'),dict(cote=64,scans=[94,95],lines=A+':395–483'),dict(cote=64,scans=[102,109],lines=A+':716–747,1044–1077')],
 'The margin on83 asks to make E explicit from the cubic étale cover J, t∈Σ_J minus J, and α:μ4*≅ω_J, using Weierstrass functions.',
 'Over an arbitrary Z[1/2]-scheme, construct the functor and inverse with descent, tangent-square identification, and the exact Q0 twist; after ordering J and choosing i, compare with an ordinary Legendre family.',
 'AntieauMeier2020 Definition4.4, Proposition4.5 and Lemma4.7 give the Legendre root atlas and twisted S3 descent. ConradLevel Definition2.7/Proposition3.1 give the ordinary Legendre moduli problem. The arbitrary-J symmetric tangent normalization is not stated in these exact forms. The cubic construction109 supplies the algebraically closed field model but not the full descent comparison.',
 'The manuscript explicitly defers the construction. No source opened explains historically why the author did not complete this exact comparison; no motive is inferred.',
 'Worth one focused run: the missing comparison is finite, central to the folder, and has explicit modern local models.',
 ['AntieauMeier2020','ConradLevel','MilneEC2021'],['SA16-506','SA16-513','SA16-532'],['C-SA16-505','C-SA16-512','C-SA16-528'],'Partly supplied on the pages; exact comparison remains unfilled, not asserted to be a modern open conjecture.')
p('Make the modular group action explicit',
 [dict(cote=64,scans=[86,89],lines=A+':193–204,248–263'),dict(cote=64,scans=[90,91,92],lines=A+':269–366')],
 'The author asks to identify the modular group and its action on U03×μ4* and on the universal tangent line.',
 'The base action is g on U03 and sgn(g)λ² on μ4*. Fixing i gives D3′=S3×C2 C4; tangent scalar λ and its square must be transported with the stated sign convention.',
 'The author supplies the formulas90–92. The complete finite-group and character computations are independently checked here. AntieauMeier2020 Lemma4.7 supplies a useful twisted-action comparison, but not this exact symmetric strictification.',
 'This is a temporary work request discharged by the following pages. It did not remain an open group-computation problem.',
 'Do not develop separately; use the checked formulas as the equivariance gate for MP-SA16-161 and165.',
 ['AntieauMeier2020','ConradLevel','GroupNamesDic3'],['SA16-507','SA16-508','SA16-509'],['C-SA16-507','C-SA16-508','C-SA16-509','C-SA16-510'],'Closed locally on90–92; exact atlas comparison is separate.')
p('Express the pinning line in three coordinates',
 [dict(cote=64,scans=[96,97,98,99,100],lines=A+':486–706'),dict(cote=64,scans=[120,123,125,126],lines=Z+':222–269,319–346,419–482')],
 'After passing to ψ_i, the author says that it remains to express membership in F_t. The later sheets solve a cyclic linear system for related coordinates.',
 'For three distinct c_i, prove that Σψ_i=Σc_iψ_i=0 is the required line in k^J and compute the cyclic-difference generator, with all tensor variances and signs.',
 'The author gives the two equations on100 and explicit cyclic differences123–126. Independent symbolic elimination verifies them. ConradLevel gives a normalized coordinate comparison, while the tensor-square scale is reserved for MP-SA16-164.',
 'The linear membership question is answered on100 and in the later linear calculation; the author explicitly distinguishes the remaining square condition.',
 'No new research is needed for this linear system; its scan-sensitive signs belong in the companion commentary.',
 ['ConradLevel'],['SA16-516','SA16-517','SA16-560'],['C-SA16-514','C-SA16-538'],'Closed for the line; not a solution of the square scale.')
p('Recover the tensor-square normalization',
 [dict(cote=64,scans=[98,99,100],lines=A+':623–652,683–706'),dict(cote=64,scans=[120,121],lines=Z+':222–289')],
 'Scan100 leaves equation73 to be expressed; scan121 says the condition83c must be returned to. The intended vector must square to the already specified canonical tangent isomorphism.',
 'For the invariant line and orientation covariance already determined, specify a scalar satisfying the tangent-square identity and prove independence of δ and the temporary choice of i. State the base and square-root torsor explicitly.',
 'ConradLevel Proposition3.2 makes a canonical ordered level-four normalization and proves base-change compatibility. AntieauMeier2020 Proposition4.5/Lemma4.7 identify the standard square-root atlas. Neither opened result is an exact match to equations73/83c. Cyclic differences determine proportionality only.',
 'Two explicit deferrals survive through the last relevant calculation126. No later resolution is present in the supplied late packet. The sources give no historical explanation for the omission.',
 'High value for one run: compare the two explicit normalizations and test equivariance before general descent.',
 ['ConradLevel','AntieauMeier2020'],['SA16-516','SA16-538','SA16-560'],['C-SA16-515','C-SA16-535'],'Open on these pages; literature supplies neighboring constructions, not a proved exact identification.')
p('Construct the symmetric relative level-four pinning map',
 [dict(cote=64,scans=[93],lines=A+':382–391'),dict(cote=64,scans=[117,118,120,121],lines=Z+':76–125,222–289')],
 'From sections P_i over the nonzero two-torsion with 2P_i=ε_i and ΣP_i=0, construct canonically a Legendre pinning, functorially in E and compatibly with base change.',
 'Construct this map over arbitrary Z[1/2]-schemes, preserving the symmetric J-indexing, the orientation torsor, and the Q0 twist. Its restriction after choosing order and i should agree with a canonical ordinary Legendre rigidification.',
 'ConradLevel Proposition3.2 proves a canonical ordinary Legendre structure from P∈E[2] and Q4∈E[4] with (P,2Q4) a full level-two structure; negating Q4 negates the differential. Theorem3.3 proves the affine level-four moduli scheme. Zavyalov2019 Theorem3.5 compares ordinary Legendre structure with his specific Γ(2)′. These do not identify the symmetric map without a further calculation.',
 'The request93 is resumed explicitly118; the scale is deferred121. The attachment supplies no completion. No broader failure of level-four representability is inferred.',
 'Highest mathematical priority: a single run can compare the formulas locally and isolate exactly which descent and sign checks remain.',
 ['ConradLevel','AntieauMeier2020','Zavyalov2019'],['SA16-538','SA16-561'],['C-SA16-533','C-SA16-534','C-SA16-535'],'Partly worked out; the last normalization is not completed.')
p('Check restriction to the three branch points',
 [dict(cote=64,scans=[106],lines=A+':914–941')],
 'After identifying the odd kernel, “il reste à voir” asks for injectivity of restriction on F3+≅F2. The page then gives the stronger Vandermonde assertion for the even space spanned by1,x,x².',
 'For distinct branch values, restriction of span(1,x,x²) to k^J is an isomorphism and the kernel of F3→k^J is ky.',
 'The page immediately computes a nonzero Vandermonde determinant and marks the argument complete. The determinant was recomputed symbolically; MilneEC2021 II.1 supplies the standard cubic model.',
 'It is resolved on the same page, so it was not dropped or left open.',
 'No further development; preserve it as a completed self-flagged step.',
 ['MilneEC2021'],['SA16-528'],['C-SA16-524'],'Closed on106.')
p('Find and extend the secant formula for the sum',
 [dict(cote=64,scans=[110,111,112,113],lines=A+':1100–1178,1184–1256')],
 'The author seeks the unique third intersection, first excluding coincidence with an endpoint, then extends the formula and states the final secant domain.',
 'For finite P,Q with x(P)≠x(Q), compute the third intersection and take its negative to obtain P+Q; allow the third point to coincide with P or Q by the polynomial identity.',
 'The page supplies the formula113. MilneEC2021 II.1 gives the chord group law. Independent factorization verifies the coefficients and shows that the intermediate distinctness of the third intersection is unnecessary.',
 'The author removes the unnecessary intermediate exclusion and completes the formula. The tangent case is an earlier-run addition, not a missing page claim.',
 'No new project; the companion should explain the two different distinctness issues clearly.',
 ['MilneEC2021'],['SA16-533','SA16-534','SA16-535'],['C-SA16-529','C-SA16-530'],'Closed by113.')
p('Give another explanation of the complex-structure correspondence',
 [dict(cote=64,scans=[131,132],lines=Z+':546–617'),dict(cote=64,scans=[133,134],lines=Z+':619–682')],
 'The margin requests another explanation after the conjugate-transport correspondence between J and a nonreal line.',
 'Explain the equivalence using a faithful circle subgroup with two conjugate weights, distinguishing J and −J and the odd-dimensional orientation condition.',
 'Scans133–134 provide that explanation. The linear-algebra proof is supplied in proof_notes.md; Hain2008 Section1 provides the lattice background.',
 'The request is followed immediately by the circle-subgroup construction; no unresolved general existence theorem remains.',
 'Useful exposition, but no separate research task is warranted.',
 ['Hain2008'],['SA16-563','SA16-573'],['C-SA16-540','C-SA16-541'],'Closed by133–134, with an inverse-glyph reading to check.')
p('Verify analytic naturality after changing the period convention',
 [dict(cote=64,scans=[135,137,138,139],lines=Z+':687–692,754–879'),dict(cote=64,scans=[143,144,145],lines=Z+':934–1010')],
 'After finding that the first line convention reverses orientation, the author asks whether the resulting moduli functor is analytically natural.',
 'Use a holomorphic period coordinate τ and the oriented lattice frame to prove that the family represents the holomorphic framed moduli functor; keep all right/left action conversions explicit.',
 'The second draft143–145 supplies the coherent holomorphic construction. Hain2008 Sections2.3–2.4 prove holomorphicity of periods and the universal property. GrothCartanX introduction provides the earlier lattice-family approach. The literal −bar(z) first-draft family is antiholomorphic.',
 'The author explicitly withdraws the orientation assertion and starts a consistent second draft. No evidence supports a deeper failure of analytic naturality after that repair.',
 'A short convention concordance is worthwhile for the companion; the universal theorem itself is settled.',
 ['Hain2008','GrothCartanX'],['SA16-564','SA16-565','SA16-566'],['C-SA16-542','C-SA16-543','C-SA16-544','C-SA16-545'],'Resolved mathematically by the second draft; ink alternatives remain.')
p('Write the outer action on the punctured-torus group explicitly',
 [dict(cote=64,scans=[140],lines=Z+':911–918'),dict(cote=64,scans=[150],lines=Z+':1252–1259')],
 'The margin asks to explicate the outer action of Aut_Z^+(H) on Π through the stated identification.',
 'For Π=F2, give automorphisms representing standard generators of SL2(Z), check their homology matrices, peripheral conjugacy, and relations modulo inner automorphisms.',
 'BuxErshovRapinchuk2011 Section3 recalls Out(F2)≅GL2(Z) and points back to Magnus–Karrass–Solitar1966 Section3.5. Nielsen1917 is a historical bibliography lead whose primary text was not accessed. The earlier-run lifts S and T have been checked by exact free-word reduction in this run.',
 'The second draft restates the theorem but does not provide the requested generators. No historical reason for this omission is given.',
 'The discrete problem is already closed by the recorded calculation; further arithmetic or profinite questions require separately specified targets.',
 ['BuxErshovRapinchuk2011','Nielsen1917'],['SA16-569','SA16-570','SA16-577'],['C-SA16-549','C-SA16-550'],'Not expanded on the pages; classical result and explicit solution recorded here.')
p('Test freeness of the product action',
 [dict(cote=64,scans=[152],lines=Z+':1326–1341')],
 'The author first considers a free product action, then notes fixed two-torsion points and deletes the concluding identification.',
 'Separate freeness of the two factors from freeness of their product; the pair (−1,−I) fixes the framed base and has E[2] as fibre fixed points.',
 'The manuscript already corrects the assertion. The fixed-point calculation is exact and agrees with standard elliptic stabilizers in Hain2008. Deleting only the zero section leaves three fixed points.',
 'It is withdrawn because the two-torsion fixed points are noticed in the margin. This is a documented reason on the page.',
 'No open problem remains; preserve the withdrawal and use it to control any proposed quotient description.',
 ['Hain2008'],['SA16-572','SA16-590'],['C-SA16-552'],'Withdrawn in the same text.')
p('Prove the sufficient condition for generic étaleness at every prime',
 [dict(cote=64,scans=[155,156],lines=Z+':1480–1518,1523–1550')],
 'After deriving q=1 and a square congruence for the signed radicand P modulo four, the author states that this condition is sufficient, without giving the proof.',
 'For squarefree primitive P defining a genuine quadratic field, prove that its normalization over Z[T] is generically étale over every integer fibre exactly when q=1 and P=r²+4h. Show the normalized order is Z[T,u]/(u²−ru−h), u=(S+r)/2.',
 'Voight2016 Lemma3.7, Lemma3.10 and Proposition3.13 supply the square-mod-four discriminant and étaleness framework. EGAIV2 Theorem5.8.6 and Stacks031O give R1+S2 normality. The specialized necessity, globalization of the congruence, and sufficiency are independently proved in proof_notes.md.',
 'The text asserts sufficiency rather than marking it doubtful. The proof is absent in this fragment; no source states why it was omitted.',
 'The finite verification is completed in this audit; the companion should retain the proof and the distinction between the original order and its normalization.',
 ['Voight2016','EGAIV2','Stacks031O','Stacks02GI','Stacks02JN'],['SA16-580','SA16-583','SA16-584','SA16-585','SA16-586','SA16-587'],['C-SA16-555','C-SA16-560','C-SA16-561','C-SA16-562','C-SA16-563','C-SA16-564'],'Stated without proof on156; closed by the independent argument here.')
(B/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
print('Authored',len(P),'problem records, MP-SA16-161 through MP-SA16-172.')
