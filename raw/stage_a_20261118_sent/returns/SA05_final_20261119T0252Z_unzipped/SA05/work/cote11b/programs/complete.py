"""Final manually authored amendments, problem index, reading alarms and audit ledgers.
The program serializes decisions made by close reading; it does not classify sources.
Run after or instead of build.py; build.py is executed here to reproduce the base records.
"""
from pathlib import Path
import runpy, json, csv, re, collections
D=runpy.run_path('SA05/work/cote11b/programs/build.py')
OUT=D['OUT']; PRO=D['PRO']; B2=D['B2']; K4=D['K4']; DATE=D['DATE']; WHO=D['WHO']
items=D['items']; entries=D['entries']; claims=D['claims']; events=D['events']
problems=[]; readings=[]; links=[]; refs=[]; searches=[]
def dump(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def tsv(n,fields,rows):
 with (OUT/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def C(n): return next(c for c in claims if c['id']==f'SA05-C{2000+n}')
def I(n): return next(c for c in items if c['id']==f'SA05-{2000+n}')
def amend(n,**kw): C(n).update(kw)
def event(sid,typ,out):events.append(dict(statement_id=sid,date=DATE,who=WHO,type=typ,outcome=out))
def loc(cote,scans,lines,file=PRO): return dict(cote=str(cote),scans=scans,lines=f'{file}:{lines}')
def problem(n,title,occ,as_he,today,state,why,worth,refs,author='Alexander Grothendieck',claims_=None):
 problems.append(dict(id=f'MP-SA05-{2000+n}',title=title,occurrences=occ,as_he_states=as_he,plausible_today=today,state_of_art=state,why_open=why,worth=worth,refs=refs,author=author,claims=claims_ or []))

# Correct exact reference extent after actual theorem/image checks.
for c in claims:
 c['refs']=['StacksExcess' if x=='FultonExcess' else x for x in c['refs']]
 c['fate_date']=c['fate_date'].replace('Seminar1963–64','Seminar1962–64')
 c['fate']=c['fate'].replace('Grothendieck1969 §1','Grothendieck1969 §3, p196')
 if c['search_family']=='reflection':
  c['author']='Unidentified reused reflection typescript; Bourbaki attribution remains a qualified lead'
amend(3,fate='Grothendieck1969 §3, p196, explicitly uses pull–multiply–Gysin operators. The exact categorical composition and its proof are checked in Stacks45.3, not in the paper’s introduction.')
amend(5,fate='The exact diagonal-unit theorem and proof were read in Stacks45.3.3. Grothendieck1969 uses the diagonal and its Künneth components in §2; it is a conceptual parallel, not a proof of the whole category theorem.',**{'class':'B'})
amend(7,fate='Stacks45.7.8 and42.54.3–5 give the Euler/excess inputs. Hua2026 §1 gives these exact small tables under ungraded commutative diagonal axioms; its written proof was read, its Lean certificate was not run.',refs=['StacksSelfIntersection','StacksExcess','Hua2026','MOEulerLead'])
amend(9,fate='Hua2026 Theorem1.1 and its corollaries give a complete multiplication reduction under ungraded diagonal identities. They do not determine the kernel of every geometric realization or prove universal independence. Stacks42.54 supplies the geometric excess input.',refs=['Hua2026','StacksExcess'])
amend(11,fate='Stacks42.54.4–5 gives the geometric intersection statement. Hua2026 §1 proves the corresponding ungraded joined-partition multiplication; the geometric and counting hypotheses remain explicit.',refs=['StacksExcess','Hua2026'])
amend(12,fate='Stacks42.54.4–5 proves the applicable excess formula. Hua2026 Theorem1.1 and its connected-partition corollary independently state the corresponding ungraded algebraic rule; no Lean execution was performed.',refs=['StacksExcess','StacksSelfIntersection','Hua2026'],fate_date='Classical excess ingredients; exact ungraded source-related rule published as a preprint in November2026; first posting day not established')
amend(13,fate='Hua2026 §1, one-factor stability paragraph, checks the corresponding ungraded integration rules. The geometric closure follows from the stated push–pull and excess identities; the cancelled extraordinary-pullback assertion is not restored.',refs=['StacksCorr','StacksExcess','Hua2026'])
amend(18,fate='GIT1982 gives the same stability proof chain, but OCR gaps prevent full monomial-formula collation. The attached sorted-weight and greedy arguments were checked directly. The missing nonzero condition is necessary; typescript page3.16 remains absent.')

# Recast densely typed draft paragraphs in complete prose; mathematical decisions unchanged.
reword={
22:('Specialization kernel/cokernel; Φ concentrated in the shifted middle degree.',
 'For a regular proper ordinary quadratic smoothing over a strictly henselian trait, with residue characteristic different from2 and suitable prime-to-residue-characteristic coefficients, the sole local vanishing-cycle degree is D=n−1. The source’s Φ convention shifts this to n. The specialization sequence is the vanishing-cycle long exact sequence.',
 'The source’s parity ranks were checked against the integral quadric lattice. Primitive λ need not generate the integral cokernel: in the ruling basis it maps to twice a generator unless2 is inverted.',
 'Deligne1974 §4.2–4.4 supplies the regular-total-space theorem and exact sequence. SGA7II XII/XV was checked at chapter metadata level only.',
 'SGA7 seminar1967–69 and publication1973; Deligne publication1974; first circulation of this source not fixed',
 'Established under the ordinary-smoothing hypotheses; keep the source degree convention and integral saturation explicit.'),
23:('For n odd, inertia acts nontrivially on Φ^n.',
 'The source’s flat, projective, smooth-generic and one-singular-special-point assumptions do not imply nontrivial inertia. In a regular ordinary quadratic smoothing of even relative dimension D=n−1, with residue characteristic≠2 and coefficients on which−1≠1, the vanishing line has the usual sign character. In odd D the vanishing cycle is fixed.',
 'The family x0²+x1²+x2²=t²x3² over C[[t]] satisfies every listed assumption but is generically constant. Its total space is singular. All checks are recorded in proof_notes.md §4 and checks.json.',
 'Deligne1974 §4.2 explicitly requires a regular total space, and §4.3 gives the parity characters. The even ramified family shows why the weaker manuscript hypothesis is insufficient.',
 'Deligne publication1974; SGA7II publication1973 verified from metadata',
 'False in the written generality; the regular ordinary-smoothing refinement is established.'),
24:('The affine cone has no higher cohomology; H^i(U1)=Φ^{i+1}.',
 'Over C, an affine cone is contractible and has H⁰=Z. For a connected smooth affine quadric deformation, reduced cohomology, or an exact sequence retaining the degree-zero unit, gives the shifted vanishing-cycle comparison.',
 'The surviving degree-zero unit gives the counterexample to an unmodified all-degree identification. The explicit tangent-bundle sphere model is proved in proof_notes.md §4.',
 'Deligne1974 §4 gives the local vanishing-cycle sequence. Its statement does not discard the ordinary H⁰ term.',
 'Publication1974; elementary topological argument independently checked2026',
 'Retain H⁰ or use reduced cohomology; do not change the diplomatic formula.'),
25:('The cone is contractible; Gysin uses ξ or −ξ; the boxed target is doubtful.',
 'For smooth projective complex X, the punctured cone E is O_X(−1)^×. Its Gysin map is cup product with c1(O_X(−1))=−h. The resulting long exact sequence computes H*(E), rather than the ill-typed boxed relative target.',
 'The line-bundle Gysin argument and the sign from O(1) dual to O(−1) are given in proof_notes.md §4.',
 'Stacks42.54.3–5 and42.54.7 verify the self-intersection and line-bundle Gysin input; the quadric application matches the checked integral lattice.',
 'Classical ingredients; earliest exact cone computation not dated',
 'Resolved in the stated topological setting; the source sign and target remain scan alarms.'),
26:('Primitive groups modulo torsion; H_a⁰=H_a¹=0.',
 'For a connected positive-dimensional projective complex X, with connected punctured cone E and contractible full cone C, H_a^i(C,Z)=reduced H^{i−1}(E,Z). Thus local degrees0 and1 vanish. The source defines primitive quotients after removing torsion.',
 'The pair long exact sequence applies because H⁰(C)→H⁰(E) is an isomorphism. This is proved explicitly in proof_notes.md §4.',
 'The local/compact comparison is compatible with Braden2003 Lemma6 after imposing weak equivariance. The elementary pair sequence supplies the displayed low-degree statement.',
 'No exact first publication assigned; Braden first arXiv posting2002-02-24 and publication2003',
 'True under the connectedness assumptions; dimension0 must be treated separately.'),
27:('Odd-dimensional quadric cone torsion is written in degree2ν−2.',
 'For Q^{2ν−1} over C with ν≥1, E=O_Q(−1)^× has integral cohomology Z in degrees0 and4ν−1, and Z/2 in degree2ν. With Z_ℓ coefficients this torsion survives only for ℓ=2. Finite2-primary coefficients also have the adjacent kernel group.',
 'Integral Gysin matrices for D1..8 are saved. The conic Q¹=P¹ with hyperplane O(2) has H²(E)=Z/2 and H⁰(E)=Z, already refuting the written degree.',
 'Karpenko Theorem1.10 gives the exact integral ring; the Gysin sequence gives the corrected degree. Stacks42.54 verifies the relevant Gysin input.',
 'Karpenko lecture November2003, used as an exposition rather than a first-discovery date',
 'The literal degree is false. The finite coefficient symbol μ/M needs scan review.'),
28:('Even-dimensional quadric cone groups are written in degrees2ν−1 and2ν+1.',
 'For Q^{2ν} over C, ν≥1, the punctured cone has free integral cohomology in degrees0,2ν,2ν+1,4ν+1. Its lower middle degree is2ν, not2ν−1.',
 'For Q²=P¹×P¹, the two middle hyperplane maps are Z→Z², 1↦(1,1), and Z²→Z, (a,b)↦a+b. Thus H²(E)=H³(E)=Z. All matrices through D8 are saved.',
 'The opened integral quadric ring and Gysin sequence establish this exact correction, which the earlier notes did not isolate.',
 'Current counterexample checked2026; later ring exposition checked2003',
 'The written lower middle degree is false in this integral interpretation.'),
29:('H_a*(C)≃H_c*(C)??',
 'For a positively G_m-contracted affine cone C with fixed vertex a and a weakly equivariant constructible complex F, the contraction comparison identifies i_a!F with RΓ_c(C,F), with coefficients satisfying Braden’s setup.',
 'Braden Lemma6 was read and applied to a closed equivariant embedding of C in the positively weighted affine space; see proof_notes.md §4.',
 'Braden2003 Lemma6 gives the applicable contraction result. Weak equivariance is essential to the verified formulation.',
 'First arXiv submission2002-02-24; publication2003',
 'Established under weak equivariance; no arbitrary-sheaf assertion is made.'),
30:('Ordinary and compact-support cohomology tables for affine quadrics.',
 'For U={Σz_i²=1}⊂C^{D+1}, D>0, H*(U,Z) is Z in degrees0,D and H_c*(U,Z) is Z in degreesD,2D. For D=0 there are two points, so repeated degree slots cannot be treated as one copy ofZ.',
 'The explicit diffeomorphism U≃TS^D, deformation retraction and Poincaré-duality argument are given in proof_notes.md §4. Finite coefficient tensoring is valid here because the groups are free.',
 'The SGA7II quadric chapter was located as metadata. The actual ring computation and Gysin input were checked in Karpenko’s theorem and the Stacks statements.',
 'SGA7II publication1973; classical topology independently rechecked2026',
 'Correct after separating the endpoint and fixing the dimension convention.'),
31:('The compact-to-ordinary middle map has coefficient2.',
 'For a complex affine quadric of dimension D=2ν, the middle compact-to-ordinary map is multiplication by (−1)^ν2 with complex orientation and compatible generators. For odd D it is zero.',
 'The tangent-bundle description gives the Euler magnitude2 or0; orientation comparison gives the sign. The Q² ruling computation checks the first nonzero case.',
 'Deligne1974 §4.1 gives the exact self-intersection table2,0,−2,0 by dimension modulo4. Generator changes can absorb the sign in an abstract source map.',
 'Deligne publication1974; SGA7II publication1973',
 'Magnitude and parity are established; source generator and twist conventions must be fixed before calling its positive2 erroneous.'),
32:('Gysin induction; an unfinished middle extension and duality slot.',
 'For a hyperplane Q^{D−1}⊂Q^D and smooth affine complement U^D, the Gysin sequence computes free even cohomology of Q^D, with rank2 only in degreeD when D is even. Odd cohomology vanishes. A free middle extension splits as groups, not canonically with all additional geometric data.',
 'The source rank patterns and all hyperplane matrices through D8 were recomputed; Q⁰ has rank2 in H⁰. Unfinished source slots remain unchanged.',
 'Karpenko Theorem1.10 and its cell-basis proof give the integral lattice and remove the extension-rank ambiguity.',
 'November2003 lecture is the checked exposition, not the first circulation of the classical theorem',
 'Cohomology is established; conventions for the specific duality maps remain necessary.'),
33:('Index2 for h^ν and λ; 2φ=h^ν+λ.',
 'For Q^{2ν}, ν≥1, ruling classes α,β form the integral middle basis, h^ν=α+β and λ=α−β. The pair h^ν,λ spans an index2 sublattice, while (h^ν+λ)/2=α is integral.',
 'The exact Smith normal form, determinant, inverse matrix and image parity are saved.',
 'Karpenko Theorem1.10 and its proof identify the two ruling families and integral relation.',
 'Checked exposition2003; first classical occurrence not assigned',
 'Established; rationalization loses the index2 information.'),
34:('The primitive square is written with a uniform positive sign.',
 'With λ=α−β on Q^{2ν}, λ²=(−1)^νh^{2ν} and hλ=0. A uniform positive λ-square is false.',
 'On Q²=P¹×P¹, λ=a−b and h=a+b, with a²=b²=0, give λ²=−2ab and h²=2ab. Every geometric and coefficient hypothesis is satisfied.',
 'Karpenko Theorem1.10 gives ruling self-intersection parity, which yields this exact signed refinement.',
 'Counterexample checked2026; primary exposition2003',
 'Use the parity sign in the reconstruction; the source ink is unchanged.'),
35:('λ is effaçable and évanescente.',
 'The primitive class λ in H^{2ν}(Q^{2ν},Z) restricts to zero on Q^{2ν−1} and pushes forward to zero on Q^{2ν+1}. Both maps kill the difference of the ruling classes.',
 'The hyperplane maps and the sum/difference basis give these kernels; the general degree and pairing argument is recorded in proof_notes.md §4.',
 'Karpenko’s integral ruling basis identifies the maps independently of the potentially ambiguous French labels.',
 'Classical; checked exposition2003',
 'Established. Hyperplane pushforward raises codimension by1.'),
36:('Hyperplane injections, surjections and an order2 cokernel.',
 'For Q^{2ν}, multiplication by h has the central matrices (1,1)^t and (1,1); the other interior rank-one maps are isomorphisms. For Q^{2ν+1}, its central rank-one map is multiplication by2.',
 'Matrices in dimensions1..8, their Smith cokernels and kernels were recomputed. The cell-basis formula proves the pattern in every dimension.',
 'Karpenko Theorem1.10 is an exact integral basis and multiplication match.',
 'Checked exposition2003, not claimed first discovery',
 'Established. Finite coefficients require both the kernel and the cokernel of multiplication by2.'),
37:('Maximal isotropic families supply the cycle basis.',
 'For a split smooth projective quadric over a field of characteristic≠2, hyperplane powers and classes of linear subspaces in the maximal isotropic families give its integral Chow basis. In even dimension there are two middle ruling classes; cycle classes give the corresponding split cohomological basis.',
 'The cell and ruling proof was read; low-dimensional ranks were checked. The historical word linéaire is preserved in the transcription.',
 'Karpenko Theorem1.10 supplies the precise modern Chow statement and proof.',
 'Checked lecture2003; classical origin not dated',
 'Established for split quadrics. Unsplit arithmetic Chow groups are outside this claim.')}
for n,(h,s,comp,f,dt,now) in reword.items():
 amend(n,his_statement=h,statement=s,computation=comp,fate=f,fate_date=dt,present_status=f'As of {DATE}: {now}')

amend(48,fate='The checked2008 retypesetting of SGA3 XII Lemma2.3 repeats the broad wording while its proof uses maximality. The1970 volume and chapter attribution were checked separately. Recorded exact-title, SGA and MathOverflow searches found no erratum.',refs=['SGA3XII','SGA3Publisher'])
amend(54,fate_date='Witt publication1937; Delzant1962; Becher online2009-04-21 and issueJuly2010')
amend(57,**{'class':'C'},fate='Milnor1970 §3 explicitly compares its symbols with Delzant’s Galois classes and the Hasse–Witt invariant. Springer1959 was located bibliographically and by DOI, but its original text was inaccessible; the exact Clifford-descent normalization is not independently certified here.',present_status=f'As of {DATE}: The general invariant is established; precise verification of the offprint’s cited descent construction remains documentary, not evidence of a new open mathematical problem.')
amend(63,computation='The J/I and symbol maps were independently checked in C2061–C2062. The original Merkurjev1981 theorem on p543 and the later Theorem2.2 were read; no full independent proof of the norm-residue theorem is claimed.',fate_date='Milnor publication1970; Merkurjev presented1981-05-19, received1981-05-22, published1981; first public circulation not separately known')
amend(64,computation='The original1981 theorem and definition of the quaternion symbol on pp542–543 were read, as well as the later author’s Theorem2.2. The Kummer identification was checked separately.',fate_date='Merkurjev presented1981-05-19, received1981-05-22, publication1981; later author proof2006')
amend(68,fate='Grothendieck1969 §2, pp194–195, discusses algebraic correspondences and Künneth components; §3, p196, spells out their pull–multiply–Gysin action. Stacks45.3 gives the explicit modern convention.',refs=['GrothStandard1969','StacksCorr'])
amend(69,statement='The report credits Deligne with exterior-power operations and λ-ring identities on the Grothendieck group of perfect complexes for schemes over a field of arbitrary characteristic. A modern checked scope is quasi-compact, quasi-separated schemes for polynomial K-theory functoriality; the opened2025 comparison theorem imposes Noetherian finite-dimensional divisorial hypotheses in its comparison section.',fate='BGMN2022 Theorem1.1 gives polynomial functoriality for small idempotent-complete stable categories, with Perf(X) discussed for qcqs schemes. Köck–Zanchetta2025 compares exterior operations on Noetherian finite-dimensional divisorial schemes and records their usual K₀ operations. This does not date Deligne’s unavailable original manuscript.',present_status=f'As of {DATE}: The exterior-operation construction is established. The precise historical λ-ring scope is the source’s report; no unrestricted ringed-topos claim is certified.',refs=['BGMN2022','KockZanchetta2025','SGA6Front'])
amend(70,fate='Deligne1968 Proposition1.2 identifies universal degeneration with derived splitting; Theorem1.5 proves splitting from a degree2 operator satisfying hard Lefschetz. These exact theorem statements and proof steps were read. The application needs a relative Lefschetz class.',computation='The abstract criterion and the report’s conditional hypothesis were compared directly. No proof of hard Lefschetz in positive characteristic is reproduced.',fate_date='Deligne publication1968; report not dated by the adjacent secretary letter')
amend(79,statement='The dual-basis cosine equality is false for the essential typeA3 reflection representation. The valid replacement is the inverse Gram matrix; vectors in the same closed chamber of the essential space have nonnegative scalar product.',computation='The exact A3 inverse Gram matrix gives dual cosine13=1/3 while m13=2. The independent inverse-positivity proof is in proof_notes.md §7; a fixed orthogonal factor is excluded.')
for it in items:
 if it['id'] in ('SA05-2113','SA05-2114'):it['author']='Unidentified reused reflection typescript; Bourbaki attribution remains a qualified lead'
 if it['id']=='SA05-2114':it['statement']=it['statement'].replace('chamber vectors','vectors in the essential chamber')

# Explicit problem index. Solved checks and withdrawn proposals remain visible as historical problems.
problem(1,'Fix the order convention for correspondence action',[loc(11,[44,46],'32-44,119-175')],
 'Choose between Cy and yC and check the signs in composition.',
 'Fix target-first versus source-first notation once; in an oriented graded theory use the unique Koszul signs induced by that convention.',
 'Stacks45.3 verifies the ungraded cycle convention. The current four-factor argument establishes the signed extension without changing factor order; Hua2026 expressly excludes this Koszul part.',
 'The manuscript explicitly leaves a convention choice, rather than reporting a mathematical obstruction.',
 'Worth a short editorial run because one convention table prevents several false formula comparisons.', ['StacksCorr','Hua2026'],claims_=['SA05-C2004'])
problem(2,'Verify the correspondence category axioms',[loc(11,[46,48],'92-175,230-253')],
 'The Cartesian axiom was forgotten; associativity and units remain to verify.',
 'Under projection formula and Cartesian base change, pull–multiply–push composition is associative and has diagonal identities.',
 'Stacks45.3.1 and45.3.3 give the exact theorem and proof; independent proof and P¹ certificate are saved.',
 'The pages show an unfinished verification, not a reason for abandonment.',
 'Closed; useful as a concise companion proof rather than a new research problem.', ['StacksCorr'],claims_=['SA05-C2003','SA05-C2005','SA05-C2006'])
problem(3,'Determine the meaning of the proposed diagonal basis',[loc(11,[51,53],'285-368,400-425')],
 'The small-factor lists are called a base, followed later by an empty relations section.',
 'Separate a universal diagram algebra, its spanning marked partitions, and the realization-dependent kernel in H*(X^r); no universal independence in every realization is true.',
 'The P¹ relation Δ=h1+h2 refutes independence. Hua2026 §1 gives multiplication reduction in an ungraded algebraic model, not every realization kernel.',
 'The source does not explain why the relations section was left blank.',
 'Worth developing as a precisely bounded presentation problem after choosing the realization and coefficient ring.', ['StacksProjectiveBundle','Hua2026'],claims_=['SA05-C2008','SA05-C2009'])
problem(4,'Resolve the first excess coefficient',[loc(11,[55,57],'480-508,567-581')],
 'The transverse case is marked OK; the next case retains χ followed by a question mark.',
 'For a connected join of unmarked partitions of k factors, with nonempty block counts s,s′, the excess is TX^{⊕(k+1−s−s′)}. Its first nonzero Euler contribution is χ in cohomology.',
 'Stacks42.54.4–5 and45.7.8 give the geometric inputs; Hua2026 Theorem1.1 gives the parallel ungraded multigraph formula.',
 'Only the visible uncertainty is known; no historical motive for dropping it is supplied.',
 'Closed in cohomology; an integral Chow version should retain the actual top Chern zero-cycle.', ['StacksExcess','StacksSelfIntersection','Hua2026'],claims_=['SA05-C2011','SA05-C2012'])
problem(5,'Scope of stability after the cancelled extension',[loc(11,[57],'608-640')],
 'Stability under selected operations is proposed, while an extraordinary-pullback paragraph is cancelled.',
 'Marked diagonal spans are stable under the specified coordinate operations and correspondence composition; arbitrary extraordinary maps require new hypotheses.',
 'The explicit one-factor operations are checked in Hua2026 §1; the geometric argument uses Stacks45.3 and42.54. No source supports reinstating the cancellation.',
 'Cancellation is visible, but its reason is not stated.',
 'Worth only a targeted companion clarification unless a broader class of maps is explicitly chosen.', ['Hua2026','StacksCorr','StacksExcess'],claims_=['SA05-C2013'])
problem(6,'Complete the GIT coordinate chart verification',[loc(11,[45,47,49],'53-81,184-212,260-281')],
 'The inverse-map and coordinate checks are left to the reader; physical typescript page3.5 is absent.',
 'Under the R-partition frame and invertible-minor conditions, the normalization maps identify the open configuration chart with PGL×its slice.',
 'Mumford GIT chapter3 verifies the construction in the opened1982 edition. The structural inverse proof is checked here; exact OCR symbol collation is not complete.',
 'The text deliberately defers the check. The missing page is a package boundary, not evidence of an abandoned theorem.',
 'Worth an editorial collation run with the original edition, not new quotient research.', ['MumfordGIT1982'],author='David Mumford',claims_=['SA05-C2017'])
problem(7,'Complete the stability cone and greedy proof chain',[loc(11,[56,58],'514-546,652-689')],
 'The sorted-weight cone is used; the final greedy proof continues on an absent page, and the displayed separator omits nonzero.',
 'Require a nonzero separating functional in the relevant span, then use the stated step rays and minimum-weight basis argument.',
 'GIT1982 has the corresponding Proposition3.6/Corollary3.7 chain, though OCR gaps limit exact formula collation. The cone formula and greedy exchange argument are re-proved here.',
 'The last physical page3.16 is absent; no historical abandonment is inferred.',
 'Closed mathematically; worth recovering the missing page and checking the functional qualifier on the ink.', ['MumfordGIT1982'],author='David Mumford',claims_=['SA05-C2018','SA05-C2020','SA05-C2021'])
problem(8,'Specialization and the primitive integral generator',[loc(56,[3,5],'725-739,799-867')],
 'The specialization arrow and parity-dependent kernel/cokernel calculations are left partly open.',
 'Use the vanishing-cycle sequence for a regular ordinary smoothing; keep integral saturation separate from rational primitive cohomology, since λ maps to twice a generator in the middle quotient.',
 'Deligne1974 §4.2–4.4 supplies the exact sequence. Karpenko Theorem1.10 and the saved Smith form determine the integral middle lattice.',
 'The draft leaves arrows and a purity phrase unfinished; it gives no reason for stopping.',
 'Worth a focused integral companion calculation, particularly at2.', ['DeligneWeilI','KarpenkoQuadrics'],claims_=['SA05-C2022','SA05-C2033'])
problem(9,'When is quadric inertia genuinely nontrivial?',[loc(56,[5],'829,867')],
 'For odd n the vanishing line is said to have nontrivial inertia.',
 'Require a regular ordinary quadratic smoothing, control ramification, and coefficients detecting−1; the written flat/projective hypotheses alone are insufficient.',
 'Deligne1974 §§4.2–4.3 supplies the regularity and character statement. The even ramified family overC[[t]] is a complete counterexample to the unqualified claim.',
 'The source does not discuss the ramified-base-change obstruction.',
 'Worth incorporating the explicit counterexample into the companion; the corrected local theorem is established.', ['DeligneWeilI'],claims_=['SA05-C2023'])
problem(10,'Cone Gysin sign and low-degree conventions',[loc(56,[7,11,13],'921-935,1022-1057,1102-1130')],
 'The Gysin sign is ξ or−ξ; the affine comparison and local-support group formulas leave degree-zero ambiguities.',
 'For E=O_X(−1)^×, use c1=−h and reduced cohomology ofE for local cohomology of the contractible cone; retain H⁰ in ordinary specialization sequences.',
 'Stacks42.54.7 verifies the line-bundle input; the pair exact sequence and connectedness prove the low groups. Deligne1974 supplies the vanishing-cycle context.',
 'The page explicitly marks the sign; no further historical explanation is present.',
 'Closed after conventions; worth a single consistent integral diagram in the companion.', ['StacksExcess','DeligneWeilI'],claims_=['SA05-C2024','SA05-C2025','SA05-C2026'])
problem(11,'Local versus compact cohomology of the contracting cone',[loc(56,[17],'1260-1268')],
 'H_a*(C)≃H_c*(C) is followed by double question marks.',
 'For a positively contracting G_m action and a weakly equivariant constructible complex with permitted coefficients, the costalk and compact-support complexes agree.',
 'Braden2003 Lemma6, with the affine-space specialization and closed pushforward, gives this precise result; its proof was read.',
 'The source marks uncertainty but does not state an obstruction or abandonment.',
 'Closed for the equivariant cone; worthwhile to specify the functorial map and coefficients.', ['Braden2003'],claims_=['SA05-C2029'])
problem(12,'Finish affine-quadric middle duality and orientation',[loc(56,[20,22],'1339-1376,1401-1443')],
 'The induction has unfinished middle slots and an explicit warning about losing a sign.',
 'Separate D=0; use U≃TS^D, Poincaré duality, and the orientation sign (−1)^{D(D−1)/2}; the middle map is0 for oddD and (−1)^{D/2}2 for evenD.',
 'Deligne1974 §4.1 gives the signed self-intersection table. Karpenko Theorem1.10 fixes the integral lattice used by Gysin induction.',
 'The proof itself remains incomplete; no external reason for dropping it is stated.',
 'Worth a convention audit and exact integral diagram, not a new computation of Betti numbers.', ['DeligneWeilI','KarpenkoQuadrics'],claims_=['SA05-C2030','SA05-C2031','SA05-C2032'])
problem(13,'Interpret the punctured-cone coefficient tables',[loc(56,[15,32],'1207-1224,1715-1736')],
 'The displayed torsion/free degrees and the coefficient notation must agree with multiplication by the hyperplane class.',
 'Use the corrected integral degrees; finite2-primary coefficients have the adjacent kernel group as well as the cokernel. Do not replace an unclear coefficient byZ orZ₂ without saying so.',
 'The exact hyperplane lattice is checked in Karpenko Theorem1.10 and the saved Gysin matrices. The degree corrections follow independently.',
 'The pages do not explain these index discrepancies.',
 'Worth prioritizing for scan review because two independent degree errors change the stated groups.', ['KarpenkoQuadrics','StacksExcess'],claims_=['SA05-C2027','SA05-C2028','SA05-C2036'])
problem(14,'Normalize the primitive quadric class',[loc(56,[24,26,30,35],'1503-1519,1558-1593,1671-1702,1753-1773')],
 'The half-class, primitive square, restriction and Gysin maps are worked out with unsettled signs and indices.',
 'Use ruling classes α,β, h^ν=α+β, λ=α−β; retain the index2 lattice and λ²=(−1)^νh^{2ν}.',
 'Karpenko Theorem1.10 and its ruling proof give the exact integral ring. The current SNF and Q² computations independently verify the corrections.',
 'Several source slots are amended or cancelled, but no reason for stopping is stated.',
 'Worth a concise integral basis dictionary shared across all quadric sheets.', ['KarpenkoQuadrics'],claims_=['SA05-C2033','SA05-C2034','SA05-C2035'])
problem(15,'Affineness of the maximal-torus scheme',[loc(56,[12,14,33],'1061-1093,1176-1197,1744-1747')],
 'Finite type is flagged for checking; affineness is promised later, with an alternative route cancelled.',
 'For smooth affine finite-presentation G with locally constant reductive rank, the maximal-torus scheme is smooth and affine over the base.',
 'SGA3 XII Corollary1.10 gives representability/smooth separated finite type, and Corollary5.4 supplies affineness. Both statements were read.',
 'The text explicitly defers affineness; the cancellation does not invalidate the completed published proof.',
 'Closed; useful for reconstructing proof order and avoiding the cancelled alternative.', ['SGA3XII'],claims_=['SA05-C2041'])
problem(16,'Containment maximality versus fibrewise maximality',[loc(56,[18,29],'1278,1646-1650')],
 'A converse existence assertion is referred to a later exposé, with artinian or locally reductive qualifications.',
 'Retain the distinction over general bases; the fibrewise comparison G⊃H⊃T uses equality of geometric reductive ranks.',
 'SGA3 XII Definition1.3/Remark1.4 and Proposition1.17 give the exact distinction and forward reference. No unrestricted general-base converse is verified.',
 'The source intentionally defers the broader existence result.',
 'Worth a short hypothesis glossary; the supplied pages do not pose an unconditional new theorem.', ['SGA3XII'],claims_=['SA05-C2045'])
problem(17,'Repair the nested-torus Weyl comparison',[loc(56,[16,29],'1236-1241,1654-1656')],
 'The lemma claims W(R) is a subquotient ofW(T) for nested toriR⊂T.',
 'AssumeT is a maximal torus ofG; then (N(R)∩N(T))/C(T) is a subgroup ofW(T) surjecting ontoW(R).',
 'The checked SGA3 XII2.3 text retains the broad wording, but its proof uses maximality. The explicitSL4 counterexample disproves the broad statement; the refined proof is supplied here.',
 'No authorial explanation or published erratum was found in the recorded searches.',
 'Highest-priority correction candidate because the missing hypothesis survives the checked published text.', ['SGA3XII','SGA3Publisher'],claims_=['SA05-C2048','SA05-C2049'])
problem(18,'Complete the reductive-centre proof fragments',[loc(56,[23,27,31],'1456-1465,1601-1618,1710-1712')],
 'The field existence proof and quotient-centre proof end abruptly; some parts and references are blank or missing.',
 'Use the universal multiplicative-type centre with the precise affine-fibre and smooth connected-fibre hypotheses of SGA3 XII4.3,4.4 and4.7.',
 'Those published statements and the4.7 proof through the rigidity conclusion were read. The malformed intersection and missing source parts remain documentary issues.',
 'The pages contain drafting gaps, not a statement that the centre theorem was abandoned.',
 'Closed mathematically; worthwhile to restore exact dependency order in a companion.', ['SGA3XII'],claims_=['SA05-C2051','SA05-C2052','SA05-C2053'])
problem(19,'Delzant’s degree-two injectivity question',[loc(56,[38],'1928-1931')],
 'Is grad²Q(F)→H²(F,Z/2) injective for every field of characteristic different from2?',
 'The map J²/J³→H²(F,Z/2) is an isomorphism, after identifying Delzant’s actual symbol map.',
 'Milnor1970 Theorem4.1 identifies K₂^M/2 withI²/I³; Merkurjev1981 p543 identifies it withBr[2]. The J/I and symbol identifications were independently checked.',
 'The offprint offers the question without an explanation of its difficulty; no historical motive is invented.',
 'Solved; worth including a precise map comparison so the later theorem answers exactly this question.', ['Milnor1970','Merkurjev1981','Merkurjev2006'],author='A. Delzant',claims_=['SA05-C2061','SA05-C2062','SA05-C2063'])
problem(20,'Generate the two-torsion Brauer group by quaternion classes',[loc(56,[38],'1931-1933')],
 'Is every Brauer class of order2 a sum of cup products a.b?',
 'For every field with2 invertible, the quaternion symbol K₂^M(F)/2→Br(F)[2] is an isomorphism.',
 'Merkurjev1981 states the exact theorem; the later author’s Theorem2.2 and Stacks Kummer sequence were also read.',
 'The offprint states the question but does not explain why it remained open then.',
 'Solved; its value here is accurate attribution and chronology.', ['Merkurjev1981','Merkurjev2006','StacksKummer'],author='A. Delzant',claims_=['SA05-C2064','SA05-C2065'])
problem(21,'Identify the unfinished purity assertion',[loc(56,[5],'861-867')],
 'The final R^{n−1}f_* purity phrase is incomplete.',
 'No unique modern theorem is identifiable until coefficients, weight normalization and extension functor are fixed.',
 'Deligne1974 §4.4 and SGA7II metadata locate surrounding local theory, but do not determine the missing formulation.',
 'Only the truncated phrase survives in the supplied passage.',
 'Worth recovering context and ink before creating a research task with a guessed statement.', ['DeligneWeilI','SGA7II'],claims_=['SA05-C2081'])
problem(22,'The reported perfect-complex λ-structure solution',[loc(12,[121],'50',B2)],
 'A previously open problem is reported solved by Deligne, with the written theory limited to schemes over a field.',
 'Use derived exterior-power operations with their λ identities in the verified modern scope; separate historical attribution from a claim about all ringed topoi.',
 'BGMN2022 Theorem1.1 supplies polynomial functoriality on perfect categories; Köck–Zanchetta2025 compares the operations under the explicit divisorial hypotheses. SGA6 frontmatter was checked only as historical metadata.',
 'The source reports a solution, not continued openness.',
 'Worth archival identification of Deligne’s manuscript, not relabelling a solved operation construction as an open problem.', ['BGMN2022','KockZanchetta2025','SGA6Front'],author='Grothendieck reporting Pierre Deligne',claims_=['SA05-C2069'])
problem(23,'Conditional Leray degeneration in the seminar report',[loc(12,[123],'54-56',B2)],
 'Deligne proves degeneration modulo the fibre Lefschetz conjecture, with an analytic Kähler analogue mentioned.',
 'A degree2 endomorphism ofRf_*Q satisfying relative hard Lefschetz gives splitting and hence Leray degeneration; the analytic application needs such a relative class.',
 'Deligne1968 Proposition1.2 and Theorem1.5 give exactly the splitting criterion. Mere Kählerness of individual fibres is not silently substituted for the global operator.',
 'The report states the condition; the final weights application is truncated.',
 'Worth merging with the main cote12 hard-Lefschetz material and recording the relative-class hypothesis.', ['Deligne1968Degeneration'],author='Grothendieck reporting Pierre Deligne',claims_=['SA05-C2070'])
problem(24,'Finish the affine mirror local-finiteness proof',[loc(12,[126],'76-78',B2)],
 'The proof that a proper affine reflection group has locally finite mirrors ends mid-sentence.',
 'Properness implies that only finitely many distinct reflecting hyperplanes meet a compact set.',
 'The classical proper discrete setting is checked in Coxeter1934; the compact-set stabilizer argument is independently completed in proof_notes.md §7.',
 'The supplied typescript page is cut off; this is not evidence of a mathematically open question.',
 'Closed; useful as a short completion with properness explicit.', ['Coxeter1934'],author='Unidentified reused reflection typescript',claims_=['SA05-C2078'])

# Final source/theorem collation, including corrections to this audit's own draft.
amend(55,computation='Witt1937 printed p38, Satz11 and its binary-case proof were actually viewed in a locally rendered page. Satz7 on p36 supplies the binary-chain reduction. The earlier provisional Satz8/p36 locator was erroneous and is replaced.',fate='Witt1937 Satz11 classifies forms of ranks1,2,3 by determinant and the stated system invariant; its rank2 proof gives the exact binary input used by Delzant.',fate_date='Author text dated1936-01-25 and received1936-05-02; journal volume176 is dated1937 by the publisher; neither date is claimed to be first public circulation')
amend(59,computation='Witt1937 pp40–42 were actually viewed: Satz17 gives the local-field invariant classification and Satz20 the number-field local/global statement, with its proof. The real binomial digits were independently proved and computed through n=64. The earlier provisional Satz21/p43 locator is replaced.',fate='Witt1937 supplies the classical local and global ingredients; Milnor1970 §3 explicitly records Delzant’s number-field assertion. The exact real-place and virtual-class arguments are supplied in proof_notes.md §6.')
for c in claims:
 if 'KarpenkoQuadrics' in c['refs']:
  c['fate_date']='Lectures at Göttingen in the first week of November2003; checked author notes dated January2004. This is an exposition date, not the first discovery of the classical quadric ring.'
  c['fate']=c['fate'].replace('Karpenko2003','Karpenko2004')
I(94)['reconstruction']=I(94)['reconstruction'].replace('finite-field Kummer','field Kummer')

# The introductory promise is a claim too; do not silently extend affine hypotheses.
claims.append(dict(id='SA05-C2082',items=['SA05-2065'],cote='56',scans=[8],lines=[f'{PRO}:965-984'],
 his_statement='Éliminer les hypothèses affines; les exposés XI, XII, XV, XVI devraient être complètement refondus.',
 statement='Some maximal-torus and Cartan conclusions extend beyond affine group schemes. For a smooth separated finite-type group scheme G/S admitting maximal tori fpqc locally, SGA3 XII7.1(a,b) gives the torus–Cartan correspondence and étale-local conjugacy. Local constancy of reductive rank alone is not sufficient in the nonaffine case, as XII7.7(a) explicitly warns.',
 status_on_pages='stated without proof',computation='The source is an introductory promise, not its proof. The published introduction, Theorem7.1(a,b) and Remark7.7(a) were read; no independent proof of the entire nonaffine extension is claimed.',
 **{'class':'A'},fate='SGA3 XII §§6–8 carries out a qualified nonaffine extension. Its exact local-torus hypothesis is retained. The editorial wish to reorganize XI/XII/XV/XVI has no yes/no mathematical content.',
 fate_date='Seminar1962–64; original SGA3II publication1970; checked retypesetting dated2008-12-02',present_status=f'As of {DATE}: Established with the stated local-existence hypothesis; the source does not license dropping all affine assumptions from every earlier theorem.',refs=['SGA3XII','SGA3Publisher'],confidence='high',author='Alexander Grothendieck',search_family='SGA3'))
event('SA05-C2082','carried as background without fault found','Introductory source wording and published scope read directly; this provenance event does not assert a proof.')
problem(25,'The promised nonaffine extension and scheme-based structure program',[loc(56,[8],'956-984')],
 'The introduction anticipates treating Chevalley structure over an arbitrary base with advantage, promises to remove affine hypotheses in §§6–8, and asks for a complete recasting of XI/XII/XV/XVI.',
 'Keep the three statements distinct: a mathematical extension with local-torus hypotheses, a broad structural program over schemes, and an editorial wish. None supplies an unrestricted theorem merely by removing the word affine.',
 'SGA3 XII7.1(a,b) proves the stated nonaffine torus–Cartan and conjugacy conclusions assuming local existence. XII7.7 warns that constant reductive rank alone fails outside affine fibres. The SGA3III publisher description confirms the completed arbitrary-base reductive-group structure program; it is bibliographic scope evidence, not an audit of that whole volume.',
 'The introduction gives a methodological preference and an editorial request, but no explanation of abandonment; the verified later work develops the program.',
 'Useful as a historical scope note, not as a newly open classification problem.', ['SGA3XII','SGA3Publisher','SGA3III'],claims_=['SA05-C2082'])

# Stage4: mathematical alarms only. No diplomatic source is modified.
def reading(cote,scan,line,old,alt,evidence,weight='essential',confidence='high mathematics; ink undecided',file=PRO):
 readings.append(dict(cote=str(cote),scan=str(scan),line=f'{file}:{line}',reading=old,alternative=alt,evidence=evidence,weight=weight,confidence=confidence,reading_id=f'SA05-R{2000+len(readings)+1}'))
reading(11,44,'23','k; inserted “pas corps”','Collate k/h and the parenthesis against Codex44 lines37–40; both versions still require full Poincaré duality.','SA05-2003. Pro and Codex differ in the coefficient letter and parenthetical wording. No mathematical reason selects the ink.','hypothesis wording','medium interpretation; ink undecided')
reading(11,46,'129-130','p31*(...) without outer β″_*','Retain the outer β″_* required by the preceding line, or combine it immediately into p3*.','SA05-C2004. The written intermediate term remains on the product of the outer factors, while the action should land on the target factor. Projection formula checks the repair.')
reading(11,51,'308','δ∈H^n(X)','δ∈H^n(X×X), with the manuscript’s degree convention.','SA05-2010 and C2008. The heading and generators are for two factors; the diagonal class has that ambient product.')
reading(11,51,'324','y1 y2 y3 in the two-factor table','y1 y2','SA05-2010. There is no third projection on X×X; the adjacent multiplication table also gives y1 y2.')
reading(11,51,'319-324','base containing y1,y2,δ','A spanning list, or a basis of a separately defined universal diagram algebra.','SA05-C2008. X=P¹ satisfies all surrounding hypotheses and δ=h1+h2. Exact calculation in checks.json and proof_notes.md §2.')
reading(11,53,'413-417','δ_r on r+1 factors; later δ_k on k factors','Two conventions may be used; record the shift explicitly before comparing formulas.','SA05-2012. Compare11/057 line567; binomial counts determine the number of factors.','index convention','high indexing; ink undecided')
reading(11,57,'555-559','s=cardR; dim Z_R=sn','Let s count nonempty blocks, or replace cardR by cardR−1 when ∅ is included.','SA05-C2010.11/055 lines452,461 explicitly include the empty block. I={1},R={∅,{1}} gives Z_R=X, not X².')
reading(11,57,'578','χ? multiplying the total point class','χ in normalized cohomology; c_d(TX) before reducing a Chow class to its degree.','SA05-C2012. The excess bundle is TX in the first redundant case. The coefficient depends on the chosen cohomological normalization.','normalization','high for cohomology; ink undecided')
reading(11,57,'632-634','Cancelled extraordinary-pullback paragraph','Collate against K11-04 lines591–592; retain cancellation while leaving the exact words unresolved.','SA05-2018. Both independent transcriptions mark withdrawal, but the words differ substantially.','status of claimed closure','medium wording; high cancellation')
reading(11,57,'636','Stable par comp','Codex has “cup|comp.” at line606; composition fits the correspondence context but the ink must decide.','SA05-2018; C2013. Closure under cup product and under correspondence composition are different assertions, although both follow in the reconstructed cohomological system.','operation named','medium; ink undecided')
reading(11,43,'14-18','Projective frame example, Pro(0,1,0); Codex(0,L,0)','Collate the middle coordinate as1/L; a nonzero scalar represents the same projective point.','SA05-2021. K11-04 line30 reads L. This does not affect the projective point if L≠0.','low mathematical impact','high projective interpretation; ink undecided')
reading(11,58,'666-668','a linear functional ℓ satisfying weak inequalities','a nonzero linear functional, in the appropriate span/dual quotient.','SA05-C2021. ℓ=0 satisfies the literal inequalities even at the interior point(1,1) of the positive quadrant; exact counterexample saved.')
reading(56,5,'852-853','cokernel generated by λν','An integral ruling class generates the cokernel; λ maps to twice a generator, unless2 is inverted.','SA05-C2022 and C2033. In the basisα,β, h^ν=α+β and λ=α−β. Modulo Zh^ν, λ=2α. Smith calculation saved.')
reading(56,5,'856-867','μ|M; inertia nontrivial on Φ^n','Determine coefficient ring and whether regular total space/ordinary smoothing is assumed elsewhere.','SA05-C2023. The even-ramified family over C[[t]] has all listed fibre hypotheses and trivial inertia;−1 also acts trivially on mod2 coefficients.','hypotheses and coefficients','high counterexample; ink/context undecided')
reading(56,5,'863','R^{n−1}f_* est “pur”…','No unique completion; locate the missing coefficient, weight and extension convention.','SA05-C2081. The surviving fragment does not identify a precise purity theorem.','identification of claim','low; no proposed ink correction')
reading(56,7,'922-923','H^{i+1}(X0), H^{i+1}(X1) in the affine sequence','Possibly U0,U1, matching the first two terms and the paragraph.','SA05-2038. The local affine argument changes from X to U and then reverts without explanation.','ambient space','medium; ink undecided')
reading(56,7,'927','H^i(U1)≃Φ^{i+1} without excluding i=0','Use reduced cohomology, or restrict positive degrees and retain the unit in the long exact sequence.','SA05-C2024. H⁰ of the connected smooth affine quadric is nonzero; source line925 only vanishes for i≠0.')
reading(56,11,'1045','H*(X)≃H*(X, Ĉ−a)','The relative pair is ill-typed as written; compare the surrounding retraction and line-bundle pair.','SA05-C2025. Ĉ−a is not a subspace of X in the described geometry; no unique ink replacement is imposed.')
reading(56,11,'1051','multiplication by ξ (or −ξ)','For E=O_X(−1)^× and ξ=c1(O_X(1)), the bundle Euler class is−ξ.','SA05-C2025. The sign follows from the dual line bundle; chosen identification can change it.','orientation convention','high under stated convention; ink undecided')
reading(56,15,'1207-1211','H^{2(ν−1)}(E)=Z/2 when ℓ=2','Integral/Z₂ torsion lies in H^{2ν}(E).','SA05-C2027. For the conic Q¹ with O(1)=O_{P¹}(2), H²(E,Z)=Z/2 while H⁰(E,Z)=Z. All Gysin matrices are saved.')
reading(56,15,'1220-1222','Lower middle free group H^{2ν−1}(E), twist−ν+1','The lower middle degree is2ν for Q^{2ν}; collate the twist after fixing its convention.','SA05-C2028. Q² gives H²(E,Z)=Z and H³(E,Z)=Z, not a new H¹ group. Both central matrices are explicit.')
reading(56,15,'1209-1224','μ|M alongside only one2-primary torsion slot','Distinguish Z_ℓ coefficients from finite coefficients A: finite coefficients also produce A[2] in the adjacent degree.','SA05-C2027,C2036. The universal-coefficient/Gysin kernel calculation gives H^D(E,A)=A[2],H^{D+1}=A/2A for oddD.','coefficient category','high mathematics; ink undecided')
reading(56,20,'1342','H_c^i(U)→H_c^i(U|W)','The natural map in this argument is H_c^i(U)→H^i(U).','SA05-C2031. The claimed middle map and vanishing outside the middle use the compact-to-ordinary comparison; target c is uncertain in the transcription.')
reading(56,20,'1339-1342','〈ℓ,φ(ℓ)〉=2','With complex orientation and compatible generators, the value is(−1)^{D/2}2 for evenD; check the author’s generator and twist conventions.','SA05-C2031. Deligne1974 §4.1 gives2,0,−2,0 byD mod4. A freely chosen generator can absorb a sign, so no decided error is asserted.','orientation','high signed theorem; ink undecided')
reading(56,22,'1407-1413','One copy ofA in degrees0 andn','Separate n=0, where the affine quadric has two points and H⁰=A².','SA05-C2030. Repeated degree slots cannot be counted once.','endpoint','high mathematics; ink undecided')
reading(56,24,'1468','P¹×P¹≃Q²⊂Q¹≃P¹','Q¹⊂Q², for the hyperplane section under discussion.','SA05-2052. Dimensions and the ensuing Gysin sequence force the inclusion direction.')
reading(56,24,'1491','λ_{2ν}∈H^{2ν}(Q^{2ν})','Compare λν, the adjacent middle-generator convention.','SA05-2052.56/026 line1564 and the surrounding indexed hyperplane classes use λν.','index convention','medium; ink undecided')
reading(56,24,'1500','ξ_i pushes to ξ_{i+2}','If i is codimension, the shift is i+1; if cohomological degree, clarify the indexing.','SA05-2052 and C2035. Hyperplane Gysin raises cohomological degree2 and codimension1.','degree convention','high type check; ink undecided')
reading(56,26,'1564','λν²=2ξ_{2ν}=ξ^{2ν}','λν²=(−1)^ν ξ^{2ν}, in the normalized ruling convention.','SA05-C2034. On Q²=P¹×P¹, (a−b)²=−2ab and(a+b)²=2ab. Exact counterexample saved.')
reading(56,30,'1661','L.(F)⊗L.(G)=(F doubly-underlined ⊗ G)','Possible derived tensor notation; no unique reconstruction from this isolated formula.','SA05-2058. The cote16 context cited by earlier notes is not attached, so no derived-category formula is inserted.','identification','low; ink undecided')
reading(56,16,'1236-1241','Nested tori R⊂T imply W(R) subquotient ofW(T)','Require T maximal, or replace the statement by an explicitly proved alternative.','SA05-C2048 refuted; refinementC2049. SL4 with v=(3,1,−1,−3),a=(1,2,−7,4) gives C2 versus1. The checked2008 SGA3 text retains the broad wording.')
reading(56,23,'1456','H∩G/Z0=0','Likely H∩(G⁰/Z0)=1 in the quotient, with both superscripts/subscripts collated.','SA05-2076. H is already a subgroup ofG/Z0, so the literal intersection equalsH and cannot justify injection intoG/G⁰. The published proof supplies the identity-component argument.')
reading(56,37,'1891-1893','Untilded H(A) target forw','Retain the rank-bearing total-class target defined earlier; inspect whether a tilde is missing.','SA05-C2060. Rank is needed for the final theorem. Positive classes alone identify⟨1⟩ and⟨1,1⟩ overR.','target and injectivity','high mathematical distinction; ink undecided')
reading(56,38,'1920-1926','Diagram targets H(A),H(A_v), followed by rank-and-classes injection','Use the same rank-bearing target on both sides, if that is the defined notation.','SA05-C2059,C2060. The final prose explicitly retains rank; this is a diagram-notation alarm, not a refutation of its theorem.','target notation','high interpretation; ink undecided')
reading(56,2,'692-702','Cover numeral and page count uncertain','No unique numerical replacement; collate cover ink against the selected handwritten blocks.','SA05-2062. The mixed package contains reused text and later inserts, so a cover count cannot date or count every physical sheet.','documentary','low; ink undecided')
reading(12,136,'158','Components of the union of the reflecting hyperplanes','Components of the complement of that union.','SA05-2114,C2072. Chambers are open full-dimensional cones; the union of mirrors has empty interior.12/128 line86 itself names the complement.','essential','high mathematics; ink undecided',B2)
reading(12,130,'104','cos(angle(e′i,e′j))=cos(π/mij)','Use the inverse Gram matrix and its entrywise nonnegativity; the displayed equality fails in rank3.','SA05-C2079. Essential typeA3 has m13=2 but dual cosine1/3. The source corollary on12/132 explicitly assumes essentiality and remains true.','essential','high counterexample; ink undecided',B2)

# Stage5 links. Every asserted endpoint below was exposed/read, including published theorem text.
def link(kind,fr,to,what,evidence,notes=''):
 links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=notes))
def pp(c,s,l):return f'cote{c}/scan{s}; {PRO}:{l}'
def cp(c,s,l,file):return f'cote{c}/scan{s}; {file}:{l}'
P1='sources/texts/pro/MPL_11_002-042_transcription.tex'
link('folder',cp(11,42,'1280-1309',P1),pp(11,44,'23-29'),'The Künneth/Poincaré example continues from coefficient fields to coefficient rings with full perfect duality.','Both passages read; P¹ is allowed, which matters for the proposed-basis counterexample.','MPL_11_043-058+56#3;MPL_11_043-058+56#10')
link('folder',pp(11,46,'92-175'),pp(11,48,'230-251'),'Composition/action formulas lead to the diagonal identity and the still-unverified category axioms.','The explicit composition, missing Cartesian axiom and final “Il reste à vérifier” were read.','MPL_11_043-058+56#7;MPL_11_043-058+56#8;MPL_11_043-058+56#9')
link('folder',pp(11,55,'452-477'),pp(11,57,'555-580'),'The partition definition with an empty block feeds the dimension and excess calculation.','Both definitions and block counts checked; distinguish cardR from nonempty block count.','MPL_11_043-058+56#13;MPL_11_043-058+56#14;MPL_11_043-058+56#17')
link('folder',pp(11,51,'285-368'),pp(11,57,'567-581'),'Small diagonal multiplication tables instantiate the general joined-partition excess rule.','Euler factor and factor-number conventions compared directly; P¹ computations redo the example.','MPL_11_043-058+56#11;MPL_11_043-058+56#20')
link('folder',pp(11,54,'433-440'),pp(11,52,'387'),'The stable-quotient proof continues on the physically earlier ampleness/descent sheet.','Theorem3.8 and continuation sentence read at both endpoints; physical scan order is not typescript order.','MPL_11_043-058+56#24')
link('folder',pp(11,56,'514-546'),pp(11,58,'652-689'),'Greedy determinant weights and the zero-sum cone are consecutive parts of the stability proof.','Both actual arguments checked. Missing typescript page3.16 is retained as absent.','MPL_11_043-058+56#25;MPL_11_043-058+56#26')
link('folder',pp(56,15,'1207-1224'),pp(56,32,'1715-1736'),'The later hyperplane maps correct the two punctured-cone cohomological degree slots.','Both tables read; exact Gysin matrices and low-dimensional examples saved.','MPL_11_043-058+56#42;MPL_11_043-058+56#43;MPL_11_043-058+56#59;MPL_11_043-058+56#60')
link('folder',pp(56,5,'852-853'),pp(56,24,'1503-1519'),'The specialization primitive class must respect the index2 middle lattice.','The cokernel assertion and explicit sum/difference matrix both read.','MPL_11_043-058+56#37;MPL_11_043-058+56#50')
link('folder',pp(56,24,'1503-1519'),pp(56,26,'1558-1593'),'Middle ruling normalization fixes λ² and the adjacent hyperplane maps.','Both explicit formulas and their degrees checked; Q² gives the signed test.','MPL_11_043-058+56#50;MPL_11_043-058+56#53;MPL_11_043-058+56#54')
link('folder',pp(56,16,'1236-1241'),pp(56,29,'1654-1656'),'The later finite étale Weyl quotient explicitly assumes a maximal torus; the earlier nested-torus lemma does not.','Both hypothesis lists read; the omitted maximality is tested by the saved SL4 example.','MPL_11_043-058+56#71;MPL_11_043-058+56#81;MPL_11_043-058+56#102')
link('folder',pp(56,4,'753-783'),pp(56,18,'1278-1287'),'Cancelled opening statements are restated later in the maximal-torus development.','Cancellation and later surviving rank/existence assertions read; withdrawal of one draft is not abandonment of the theorem.','MPL_11_043-058+56#65;MPL_11_043-058+56#67;MPL_11_043-058+56#104')
link('folder',pp(56,36,'1787-1834'),pp(56,38,'1928-1933'),'The rank-zero filtration and Kummer/Brauer definition determine the exact two open maps in Delzant’s offprint.','Both definitions and questions read; J/I and symbol calculations independently supply the modern comparison.','MPL_11_043-058+56#86;MPL_11_043-058+56#88;MPL_11_043-058+56#94;MPL_11_043-058+56#95')
link('folder',pp(11,44,'23-44'),cp(11,44,'35-77',K4),'Independent Pro/Codex witnesses preserve full Poincaré duality and the undecided action order.','Both actual passages compared; parenthesis and coefficient-letter differences retained.','MPL_11_043-058+56#3;MPL_11_043-058+56#6')
link('folder',pp(11,57,'632-640'),cp(11,57,'591-613',K4),'Independent witnesses agree on cancellation but differ on its exact words and cup/comp.','Both excerpts read; neither witness is silently substituted for the other.','MPL_11_043-058+56#18')
link('folder',cp(12,102,'3-20',B2),pp(11,44,'25-44'),'Cohomological correspondences via Künneth/Poincaré continue the pull–multiply–push viewpoint.','B12/102 ends before its promised action formula; that ending is preserved.','Codex B12-02;MPL_11_043-058+56#7')
link('folder',cp(12,136,'158',B2),cp(12,128,'84-90',B2),'The later proof explicitly calls the chamber union the complement of the mirrors, supporting the chamber-definition alarm.','Both exact prose endpoints read; the unique object in Cor7 is y, not g.','Codex B12-02')

link('published work',pp(11,46,'92-105'),'GrothStandard1969 §3 p196','Grothendieck’s later paper describes algebraic operators by pullback, cycle multiplication and Gysin pushforward.','All7 printed pages were viewed; this is the exact action formula, not a claim that §1 proves the correspondence category.','MPL_11_043-058+56#7')
link('published work',pp(11,46,'92-175'),'StacksCorr §45.3, Lemmas45.3.1 and45.3.3','Associativity and diagonal units in the modern Chow-correspondence category.','Statements and proofs, including the four-factor expression, read in the opened primary project text.','MPL_11_043-058+56#8;MPL_11_043-058+56#9')
link('published work',pp(11,48,'230-251'),'StacksMotives §45.4','Additive idempotent completion and Tate twists supply the later construction that these sheets leave undone.','Triples, Hom formula, projector splitting and Tate object were read.','MPL_11_043-058+56#2;MPL_11_043-058+56#33')
link('published work',pp(11,51,'311-368'),'StacksSelfIntersection Lemma45.7.8; StacksExcess §42.54.3–5','Diagonal Euler self-intersection and excess explain the multiplication tables.','Exact statements and relevant proof arguments opened; cohomological point normalization is explicit.','MPL_11_043-058+56#11')
link('published work',pp(11,57,'555-640'),'Hua2026 §1, Theorem1.1 and corollaries','The recent ungraded commutative graph formalism checks the joined-partition multiplication and one-factor integration rules.','Written proof read. No Lean certificate run; geometry, odd signs and arbitrary realization kernels are excluded from the match.','MPL_11_043-058+56#14;MPL_11_043-058+56#17;MPL_11_043-058+56#18')
link('published work',pp(11,54,'433-440'),'MumfordGIT1982 Theorem3.8, printedp76','The stable-configuration quotient and ample descended polarization occur in the published GIT book.','The exact theorem text was read; it is Mumford’s reused text, not Grothendieck’s theorem.','MPL_11_043-058+56#24')
link('published work',pp(11,52,'387'),'EGAII4.5.2, printedpp83–84','The source explicitly invokes the affine-nonvanishing criterion for ampleness.','Theorem4.5.2(a′) and surrounding proof read; the source’s additional descent citation is not replaced by this theorem.','MPL_11_043-058+56#24')
link('published work',pp(56,5,'799-867'),'DeligneWeilI §4.1–4.4, printedpp287–289','Vanishing cycles and Picard–Lefschetz have precise regularity, coefficient and parity hypotheses.','The primary text explicitly assumes a regular total space; the source does not.','MPL_11_043-058+56#36;MPL_11_043-058+56#37')
link('published work',pp(56,17,'1260-1268'),'Braden2003 Lemma6','Weakly equivariant contraction gives the expected costalk/compact-support comparison.','Lemma statement and proof read, then specialized to a positively contracted cone.','MPL_11_043-058+56#44;MPL_11_043-058+56#45')
link('published work',pp(56,24,'1503-1519'),'KarpenkoQuadrics Theorem1.10 and proof, author notes January2004','The integral ruling basis and hyperplane relation reproduce the middle index2 lattice.','Exact theorem and proof read; the2003 lecture/2004 notes date is not the historical origin of the result.','MPL_11_043-058+56#50;MPL_11_043-058+56#51')
link('published work',pp(56,4,'753-783'),'SGA3XII Theorem1.7 and Corollaries1.9–1.16','Rank semicontinuity, local maximal tori, representability and local conjugacy are later published in the same exposition.','Actual retypeset theorem/corollary text read;1970 volume metadata checked separately.','MPL_11_043-058+56#65;MPL_11_043-058+56#68')
link('published work',pp(56,16,'1236-1241'),'SGA3XII Lemma2.3, checked2008 retypesetting','The broad nested-torus wording survives in the checked published transcription and its proof uses maximality.','Exact statement and proof read. Original1970 ink has not been collated; the counterexample is independent of that documentary limitation.','MPL_11_043-058+56#71;MPL_11_043-058+56#102')
link('published work',pp(56,27,'1601-1616'),'SGA3XII4.3,4.4,4.7','The fibrewise reductive-centre criterion and existence theorem have completed published proofs.','Exact hypotheses and the4.7 proof were read; the source’s missing parts remain missing.','MPL_11_043-058+56#76;MPL_11_043-058+56#77;MPL_11_043-058+56#78;MPL_11_043-058+56#79')
link('published work',pp(56,8,'965-984'),'SGA3XII7.1(a,b),7.7(a)','The promised nonaffine extension retains local-torus existence; constant rank by itself is insufficient there.','Both published hypotheses and explicit warning read.','MPL_11_043-058+56#66')
link('published work',pp(56,38,'1928-1933'),'Milnor1970 Theorem4.1; Merkurjev1981 pp542–543 theorem','The exact degree-two map and quaternion-generation questions are solved for all fields of characteristic≠2.','Both theorem statements read; current J/I and symbol-map proof supplies the comparison with Delzant.','MPL_11_043-058+56#94;MPL_11_043-058+56#95;MPL_11_043-058+56#97')
link('published work',pp(56,37,'1842-1843'),'Witt1937 Satz7 p36 and Satz11 p38','Binary chain equivalence and the rank2 determinant/system invariant justify the presentation input.','Rendered primary pages actually viewed, including the binary proof; earlier provisional theorem numbering corrected.','MPL_11_043-058+56#86;MPL_11_043-058+56#87')
link('published work',cp(12,123,'54-56',B2),'Deligne1968Degeneration Proposition1.2 and Theorem1.5, pp107–109','A relative Lefschetz operator yields derived splitting and hence universal spectral-sequence degeneration.','The exact degree2 operator criterion and proof arguments were read. The report’s Kähler wording is kept conditional.','Codex B12-02')
link('published work',cp(12,121,'50',B2),'BGMN2022 Theorem1.1; KockZanchetta2025 Theorem4.1 and Corollary4.2','Modern polynomial K-theory and comparison of exterior operations clarify the reported λ-structure construction.','Actual modern theorem text and hypotheses read; these sources do not date Deligne’s particular manuscript.','Codex B12-02')
link('published work',cp(12,132,'134-142',B2),'Coxeter1934 Theorems4 and8','The simplicial chamber theorem and Coxeter presentation predate the reused sheets.','The actual1934 theorem text was read; exact Bourbaki typescript number383 remains unidentified.','Codex B12-02')

# Outside-project links and unavailable archival endpoints are explicitly NOT verified links.
external=[]
def ext(fr,to,what,notes,run,state='unverified target; earlier-run lead'):
 external.append(dict(kind='our projects',**{'from':fr,'to':to},what=what,evidence='Supplied note and local source passage checked; the other endpoint is not attached and no target claim is certified.',note_ids=notes,run_names=run,status=state))
ext(pp(11,46,'92-105'),'Cote16 draft standard-conjecture/operator sheets, as reported in notes','Draft C-to-published-B and the unresolved draft B/D identification.','MPL_11_043-058+56#1;MPL_11_043-058+56#29;MPL_11_043-058+56#30','Earlier notes/context packet')
ext(pp(11,44,'32-44'),'Cote16 operator/projector statements; earlier research runs','Hyperplane induction, universal operator projectors and twist-bearing naturality; no unqualified commutation conclusion.','MPL_11_043-058+56#31;MPL_11_043-058+56#32;MPL_11_043-058+56#35','Earlier-run operator project')
ext(pp(56,30,'1661'),'Les Dérivateurs / cote16 context','Possible derived tensor interpretation of the faint isolated formula.','MPL_11_043-058+56#58','Les Dérivateurs; earlier context')
ext(pp(56,20,'1342-1376'),'WG H9; cote44/cote47 pairing/support discussions','Local pairing and proper-support analogies, not a checked two-ended archival link.','MPL_11_043-058+56#63;MPL_11_043-058+56#100;MPL_11_043-058+56#101','WG H9')
ext(pp(56,30,'1671-1702'),'La Longue Marche: LM7_E23 and LM7_PUSHD44','Section-class/descent analogies from the earlier-run context.','MPL_11_043-058+56#100;MPL_11_043-058+56#101','LM7_E23;LM7_PUSHD44;La Longue Marche')
ext(pp(11,44,'25-27'),'Cote54 Dieudonné/de Rham question as reported in notes','Oda’s precise theorem is independently verified; the unavailable archive question is not claimed solved verbatim.','MPL_11_043-058+56#64','Earlier notes/context packet')

# References. “verified” means the extent recorded here, never an unseen full proof.
def ref(key,typ,title,author,year,url,extent,level='theorem text and selected proof',note='verified',**extra):
 refs.append(dict(key=key,entry_type=typ,title=title,author=author,year=str(year),url=url,note=note,checked_extent=extent,verification_level=level,accessed=DATE,**extra))
ref('StacksCorr','misc','The Stacks Project, Section45.3: Correspondences','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/0FFZ','Definition of composition; Lemma45.3.1 with its four-factor proof; Lemma45.3.3 with diagonal-unit proof; graph conventions in lines18–108.','theorem text and full proofs of the cited lemmas')
ref('StacksMotives','misc','The Stacks Project, Section45.4: Chow motives','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/0FG9','Triples(X,p,m), the Hom formula, projector splitting and the Tate object in lines18–69.','definitions and construction proof')
ref('StacksSelfIntersection','misc','The Stacks Project, Lemma45.7.8','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/0FH0','Diagonal self-intersection/Euler characteristic equality, including the short proof in lines23–35.','theorem text and full lemma proof')
ref('StacksExcess','misc','The Stacks Project, Section42.54: The key formula','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/0FBI','Lemma42.54.3; excess setup42.54.4–5; transverse case42.54.6; line-bundle case42.54.7. Exact sequences, formulas and the displayed proofs read.')
ref('StacksProjectiveBundle','misc','The Stacks Project, Section42.36: Projective space bundle formula','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/02TX','Lemma42.36.2 projective-bundle formula and its proof; used for the P¹ model.','theorem text and lemma proof')
ref('StacksHRR','misc','The Stacks Project, Section42.66: Grothendieck–Riemann–Roch','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/02UO','The smooth projective Euler-characteristic formula with the Todd factor, lines18–29. No independent proof of GRR is claimed.','formula statement')
ref('StacksKummer','misc','The Stacks Project, Section59.28: Kummer theory','The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/03PK','Lemma59.28.1 exact Kummer sequence for an invertible integer; field application uses Pic(SpecF)=0.','theorem statement and exact-sequence application')
ref('GrothStandard1969','incollection','Standard conjectures on algebraic cycles','Grothendieck, Alexander',1969,'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf','All seven printed pages193–199 actually viewed after local download/render. §2 pp194–195: correspondences and Künneth components; §3 p196: pull–multiply–Gysin action. The web screenshot-only response was not counted as viewing.','full paper viewed',booktitle='Algebraic Geometry, Bombay1968',pages='193--199',publisher='Oxford University Press',date_note='Conference1968; publication1969. First public circulation not separately established.')
ref('GrothChern1958','article','La théorie des classes de Chern','Grothendieck, Alexander',1958,'https://www.numdam.org/article/BSMF_1958__86__137_0.pdf','§4, Remark2, printedpp147–149, especially the rank-plus-total-class ring and its multiplication.','exact construction text',journal='Bulletin de la Société Mathématique de France',volume='86',pages='137--154')
ref('Jannsen1992','article','Motives, numerical equivalence, and semi-simplicity','Jannsen, Uwe',1992,'https://epub.uni-regensburg.de/26642/1/jannsen10.pdf','Theorem1 numerical semisimplicity and Corollary1 on the radical of homological correspondences under algebraic Künneth components. The source received date12July1991 is not identified as first circulation.','exact theorem and corollary text with proof discussion',journal='Inventiones Mathematicae',volume='107',pages='447--452')
ref('Hua2026','misc','Énoncés des notes de travail de Grothendieck démontrés en Lean4, et questions ouvertes','Hua, Michel',2026,'https://hexagonmath.org/pdf/2611.00125v2','§1 diagonal axioms and even/ungraded Poincaré model, Theorem1.1 graph rule and proof, partition corollaries and one-factor integration. Lines520–674 read. Explicit exclusions include odd/Koszul formalization, geometric excess, the full correspondence category and realization kernels. No Lean executable/certificate was run.','preprint theorem text and written proof',date_note='Version2, November2026; exact first posting day not established; not treated as a journal article.')
ref('MumfordGIT1982','book','Geometric Invariant Theory','Mumford, David and Fogarty, John',1982,'https://dokumen.pub/geometric-invariant-theory-2nbsped-3540112901-9783540112907.html','Reproduction of the primary second edition: R-partition charts and Proposition3.3 lines1504–1555; quotient/descent1558–1578; Theorem3.8 lines1606–1616, printedp76. OCR is incomplete around the exact Proposition3.6 monomial statement.','primary book text through a mirror; selected statements/proofs',edition='2',publisher='Springer',date_note='First edition1965; second1982; third1994 verified independently at publisher. These dates do not date the specific reused sheets.')
ref('MumfordGITPublisher','misc','Geometric Invariant Theory: publisher edition history','Mumford, David and Fogarty, John and Kirwan, Frances',1994,'https://link.springer.com/book/9783540569633','Publisher metadata and edition chronology only: first1965, second1982, third1994. No theorem proof checked through this page.','metadata only')
ref('EGAII','article','Éléments de géométrie algébrique II: Étude globale élémentaire de quelques classes de morphismes','Grothendieck, Alexander and Dieudonné, Jean',1961,'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAII.pdf','Theorem4.5.2, printedpp83–84, especially condition(a′) on affine nonvanishing opens and the proof. The direct PDF was too large for the web opener, but the cached primary-text reference exposed these actual lines4927–4954.','theorem text and relevant proof',journal='Publications Mathématiques de l’IHÉS',volume='8')
ref('DeligneWeilI','article','La conjecture de Weil. I','Deligne, Pierre',1974,'https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf','§4.1–4.4, printedpp287–289: vanishing-cycle sequence, sphere self-intersection table, regular-total-space assumption and parity character. Exact theorem hypotheses read; not a full proof audit of the Weil conjectures.','theorem text and local discussion',journal='Publications Mathématiques de l’IHÉS',volume='43',pages='273--307')
ref('Deligne1968Degeneration','article','Théorème de Lefschetz et critères de dégénérescence de suites spectrales','Deligne, Pierre',1968,'https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf','Proposition1.2, pp107–108, splitting iff universal degeneration, including proof; Theorem1.5 p108 and its primitive-decomposition proof through p109. The statement requires an actual degree2 Lefschetz endomorphism.','exact theorem and proof arguments',journal='Publications Mathématiques de l’IHÉS',volume='35',pages='107--126')
ref('SGA7II','book','Groupes de monodromie en géométrie algébrique, SGA7II','Deligne, Pierre and Katz, Nicholas M.',1973,'https://link.springer.com/book/10.1007/BFb0060505','Publisher volume and chapter metadata only: ExposéXII “Quadriques”, pp62–81; ExposéXV Picard–Lefschetz, pp165–196. Failed full-PDF attempts do not certify the chapter proofs.','metadata only',series='Lecture Notes in Mathematics',volume='340',doi='10.1007/BFb0060505',date_note='Seminar1967–69; publication1973.')
ref('KarpenkoQuadrics','misc','Cycles on powers of quadrics','Karpenko, Nikita A.',2004,'https://sites.ualberta.ca/~karpenko/publ/powers.pdf','Example1.4, Theorem1.7 and especially Theorem1.10 with proof: split-quadric integral Chow basis, hyperplane relation and ruling parity. The text permits characteristic2 in a suitable split formulation; our current geometric tests explicitly use characteristic≠2/complex quadrics.','exact theorem and proof',date_note='Lectures in first week of November2003; author PDF dated January2004. No first-discovery claim.')
ref('Braden2003','article','Hyperbolic localization of intersection cohomology','Braden, Tom',2003,'https://arxiv.org/pdf/math/0202251','Setup/coefficient assumptions at lines17–80 and Lemma6 with proof at lines243–276; contraction specialization explained separately in proof_notes.md §4.','exact lemma and full lemma proof',journal='Transformation Groups',volume='8',pages='209--216',archivePrefix='arXiv',eprint='math/0202251',metadata_url='https://arxiv.org/abs/math/0202251',date_note='First arXiv submission2002-02-24; final arXiv revision2003-07-29; publication2003.')
ref('SGA3XII','incollection','Exposé XII: Tores maximaux, groupe de Weyl, sous-groupes de Cartan, centre réductif des schémas en groupes lisses et affines','Grothendieck, Alexander',1970,'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo12.pdf','Checked2008-12-02 retypesetting. Read1.3–1.4,1.7,1.9–1.16;2.2–2.3 including the problematic proof;4.1–4.4,4.7 and proof;5.4; introduction;6.6 statements/proof portions;7.1(a,b),7.7(a). A broad2.3 assertion remains in this checked version. Original1970 ink was not collated.','selected exact statements and proofs',booktitle='Schémas en groupes, SGA3II',series='Lecture Notes in Mathematics',volume='152',pages='180--248',date_note='Seminar1962–64; book1970; examined retypesetting2008.')
ref('SGA3Publisher','misc','Schémas en groupes, SGA3II: publisher record','Demazure, Michel and Grothendieck, Alexander',1970,'https://link.springer.com/book/10.1007/BFb0059005','Original volumeII, LNM152,1970 and ExposéXII author/page metadata. This record does not certify the original typography of Lemma2.3.','metadata only',doi='10.1007/BFb0059005')
ref('SGA3III','book','Schémas en groupes, SGA3III: Structure des schémas en groupes réductifs','Demazure, Michel and Grothendieck, Alexander',1970,'https://link.springer.com/book/10.1007/BFb0059027','Original volume and chapter metadata; SMF2011 re-edition description explicitly gives the arbitrary-base reductive-group program, ExposésXIX–XXV, and parabolicsXXVI. Used only to locate the program, not to claim a proof audit of the volume.','metadata and publisher scope description',series='Lecture Notes in Mathematics',volume='153',doi='10.1007/BFb0059027',metadata_url='https://smf.emath.fr/publications/schemas-en-groupes-sga-3-tome-iii-structure-des-schemas-en-groupes-reductifs-seminaire')
ref('SGA6Front','book','Théorie des intersections et théorème de Riemann–Roch, SGA6','Berthelot, Pierre and Grothendieck, Alexander and Illusie, Luc',1971,'https://geotoppos.org/divers/SGA6.pdf','The returned PDF contains24 pages of frontmatter/contents, not the whole volume. Preface datedJune1971 and the relevant chapter topics were checked. No perfect-complex λ theorem is certified from this frontmatter.','frontmatter and contents only',series='Lecture Notes in Mathematics',volume='225')
ref('Delzant1962','article','Définition des classes de Stiefel–Whitney d’un module quadratique sur un corps de caractéristique différente de2','Delzant, Antoine',1962,'','Full supplied offprint transcription: cote56 scans36–38, Pro lines1780–1943; scan39 is the colophon. The source explicitly names Antoine at line1785. Bibliographic metadata is independently corroborated by Laborde1976 and BecherVirtual. No original offprint scan was supplied.','supplied primary transcription read in full',journal='Comptes rendus de l’Académie des sciences, Paris',volume='255',pages='1366--1368',file=PRO,date_note='Session10September1962, presented by Jean Leray; physical reuse does not date adjacent manuscripts.')
ref('Witt1937','article','Theorie der quadratischen Formen in beliebigen Körpern','Witt, Ernst',1937,'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wittform.pdf','Rendered primary pages31,36–38,40–44 actually viewed. Satz7 p36 binary chains; Satz11 p38 rank≤3 invariants with binary proof; Satz17 p40 local-field classification; Satz20 p42 local/global with proof; p44 author/received dates. The earlier provisional Satz8/p36 and Satz21/p43 locators were corrected.','primary page images; selected theorem texts and proofs',journal='Journal für die reine und angewandte Mathematik',volume='176',pages='31--44',doi='10.1515/crll.1937.176.31',metadata_url='https://www.degruyterbrill.com/journal/key/crll/1937/176/html',date_note='Author date1936-01-25; received1936-05-02; publisher volume year1937. A later bibliography says1936; the publisher volume year is retained.')
ref('BecherVirtual','article','Virtual forms','Becher, Karim Johannes',2010,'https://www.math.uni-bielefeld.de/lag/man/217.pdf','§4.4–4.6 lines589–636: exact virtual/Grothendieck–Witt presentation and symbol connection. Publisher date metadata independently opened.','exact construction and proposition text',journal='Mathematische Zeitschrift',volume='265',pages='551--569',doi='10.1007/s00209-009-0529-4',metadata_url='https://link.springer.com/article/10.1007/s00209-009-0529-4',date_note='Received2008-02-26; online2009-04-21; issueJuly2010. First preprint circulation not established.')
ref('Milnor1970','article','Algebraic K-theory and quadratic forms','Milnor, John',1970,'https://people.reed.edu/~ormsbyk/kgroup/resources/Algebraic_KTheory_and_quadratic_forms.pdf','§3 lines330–430: total classes, explicit Delzant comparison and Whitney calculation; Lemma3.2; §4 Theorem4.1: degree1,2 comparison isomorphisms and higher surjectivity. Exact low-degree map comparison independently supplied in this run.','exact statements and relevant proofs',journal='Inventiones Mathematicae',volume='9',pages='318--344')
ref('Merkurjev1981','article','On the norm residue symbol of degree2','Merkurjev, Alexander S.',1981,'https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=44871&what=fullt','Original Russian six-page article opened. Quaternion symbol definition on p542 and theorem on p543 (text lines27–50) read, followed by initial proof text through line160. Not a full independent proof audit.','original theorem text and initial proof',journal='Doklady Akademii Nauk SSSR',volume='261',number='3',pages='542--547',metadata_url='https://www.mathnet.ru/eng/dan44871',date_note='Presented1981-05-19; received1981-05-22; publication1981. First circulation not separately known.')
ref('Merkurjev2006','incollection','On the norm residue homomorphism of degree two','Merkurjev, Alexander',2006,'https://www.math.ucla.edu/~merkurev/papers/residue.pdf','Theorem2.2 and the exact quaternion-symbol definition, lines74–86, plus the final proof discussion and1981 bibliography. Author publication list opened to verify the2006 venue. No complete independent proof claimed.','exact theorem text and selected proof',booktitle='Proceedings of the St. Petersburg Mathematical Society, Vol.XII',series='American Mathematical Society Translations, Series2',volume='219',pages='103--124',publisher='American Mathematical Society',metadata_url='https://www.math.ucla.edu/~merkurev/publicat.htm')
ref('Springer1959','article','On the equivalence of quadratic forms','Springer, Tonny A.',1959,'https://doi.org/10.1016/S1385-7258(59)50026-8','Located bibliographically and through the DOI; repeated open attempts failed. The original text and the precise Clifford-descent normalization were not checked.','bibliographic lead; original inaccessible','unverified',journal='Indagationes Mathematicae',volume='21',pages='241--253',doi='10.1016/S1385-7258(59)50026-8')
ref('Laborde1976','article','Classes de Stiefel–Whitney en cohomologie étale','Laborde, O.',1976,'https://www.numdam.org/article/MSMF_1976__48__47_0.pdf','Paper text read, especially §III p50: locally free finite-rank quadratic modules with2 invertible, naturality and Whitney sum, and agreement with Delzant over fields. Bibliography identifies Delzant1962 and links Zbl0108.04303. The zbMATH link itself returned403.','primary paper text; exact scheme-to-field comparison',journal='Mémoires de la Société Mathématique de France',volume='48',pages='47--51',doi='10.24033/msmf.201',metadata_url='https://www.numdam.org/item/MSMF_1976__48__47_0/',date_note='Montpellier colloquium1975; publication1976.')
ref('Zibrowius2014','misc','Witt Groups of Curves and Surfaces','Zibrowius, Marcus',2014,'https://www.math.uni-duesseldorf.de/~zibrowius/Research/Zibrowius_WCS.pdf','§1.4 Stiefel–Whitney history and bibliography entryDel62 explicitly naming Antoine. Used for bibliographic corroboration, not to settle the exact arbitrary-field degree-two theorem.','selected historical paragraph and bibliography',date_note='Author PDF dated10April2014.')
ref('ENSDelzantName','misc','Antoine Delzant: memorial notice','Association des anciens élèves de l’École normale supérieure',2025,'https://www.archicubes.ens.fr/node/1565','Notice names Antoine and identifies his Stiefel–Whitney paper. Used only for author-identity corroboration.','biographical metadata',date_note='Accessed2026-11-19; the page publication year is not established in this audit.')
ref('Oda1969','article','The first de Rham cohomology group and Dieudonné modules','Oda, Tadao',1969,'https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf','Corollary5.11, printedp131, identifies the contravariant Dieudonné module ofA[p] withH¹_dR and VM with the Hodge subspace; the exact sequence is read. This does not verify the unavailable cote54 formulation.','exact theorem/corollary text',journal='Annales scientifiques de l’École normale supérieure',series='4',volume='2',number='1',pages='63--135',doi='10.24033/asens.1175',metadata_url='https://www.numdam.org/item/ASENS_1969_4_2_1_63_0/',date_note='Related dissertationJune1967; article publication1969; exact first circulation of Cor5.11 not established.')
ref('Coxeter1934','article','Discrete groups generated by reflections','Coxeter, H. S. M.',1934,'https://sites.math.washington.edu/~billey/classes/reflection.groups/references/Coxeter.1934.pdf','§4 definitions; Theorem4 simplicial region; Lemmas5.1–5.2 and Theorem6 orthogonal decomposition; Theorem8 Coxeter presentation. Relevant statements and proof sections read. Point-stabilizer and local-finiteness consequences are independently explained in proof_notes.md §7.','selected exact theorem text and proof sections',journal='Annals of Mathematics',volume='35',number='3',pages='588--621',date_note='Received1933-06-16; publicationJuly1934; received date is not assumed first circulation.')
ref('Bourbaki1968','book','Groupes et algèbres de Lie, chapitres IV, V et VI','Bourbaki, Nicolas',1968,'https://link.springer.com/book/10.1007/978-3-540-34491-9','Publisher chapterV subject/pages57–141 and reprint-of1968 metadata; official Bourbaki bibliography opened. This identifies the natural publication family, not the exact numbered383 typescript or a theorem proof in that book.','metadata only',doi='10.1007/978-3-540-34491-9',metadata_url='https://www.bourbaki.fr/Ouvrages.html',date_note='Original1968; subsequent1981/2007 reprints. Exact reused sheet date unknown.')
ref('KockZanchetta2025','article','Comparison of exterior power operations on higher K-theory of schemes','Köck, Bernhard and Zanchetta, Ferdinando',2025,'https://link.springer.com/article/10.1007/s00209-025-03681-2','Theorem3.11 and the scope transition into §4; Theorem4.1 and Corollary4.2 comparing operations. The comparison section imposes Noetherian finite-dimensional divisorial hypotheses and appropriate regular base assumptions.','exact theorem text and scope',journal='Mathematische Zeitschrift',volume='309',number='63',doi='10.1007/s00209-025-03681-2',date_note='Published2025-02-21.')
ref('BGMN2022','misc','K-theory and polynomial functors','Barwick, Clark and Glasman, Saul and Mathew, Akhil and Nikolaus, Thomas',2022,'https://arxiv.org/pdf/2102.00936','Introduction lines10–40 including Perf(X) for quasi-compact quasi-separatedX; Theorem1.1 lines68–81 on polynomial functoriality. Used to delimit the checked modern construction, not to date Deligne’s historical solution.','exact theorem text and application scope',archivePrefix='arXiv',eprint='2102.00936',metadata_url='https://arxiv.org/abs/2102.00936',date_note='First submitted2021-02-01; v2 submitted2022-05-18; PDF datedMay2022. No journal publication verified.')
ref('MOEulerLead','misc','Euler characteristic of a manifold and self-intersection','MathOverflow contributors; answer by Andy Putman',2009,'https://mathoverflow.net/questions/696/euler-characteristic-of-a-manifold-and-self-intersection/700','Question and the normal-bundle/Euler answer opened. Used only as a search lead; the actual mathematical conclusion is checked in the Stacks primary proof.','discussion lead only')

# Remove a guessed date from a biography: access is verified, publication date is not.
for r in refs:
 if r['key']=='ENSDelzantName':r.pop('year')
R={r['key']:r for r in refs}
for c in claims:
 if c['search_family']=='Delzant' and 'Delzant1962' not in c['refs']:c['refs'].append('Delzant1962')

def bibescape(s):
 return str(s).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
parts=[]
for r in refs:
 fields={k:v for k,v in r.items() if k not in ('key','entry_type','verification_level','accessed') and v!=''}
 fields['urldate']=DATE
 parts.append('@'+r['entry_type']+'{'+r['key']+',\n'+',\n'.join('  '+k+' = {'+(str(v) if k in ('url','metadata_url','file','doi') else bibescape(v))+'}' for k,v in fields.items())+'\n}\n')
(OUT/'references.bib').write_text('\n'.join(parts))
tsv('reference_checks.tsv',['key','note','verification_level','checked_extent','url','metadata_url','date_note','accessed'],refs)

# Search ledger: manually specified actual search families, expanded only for audit coverage.
families={
 'correspondences':dict(queries='site.stacks.math.columbia.edu "composition of correspondences" | Grothendieck standard conjectures algebraic cycles1969 Jannsen numerical semisimplicity1992',venues='Primary Stacks sections; Grothendieck paper; Jannsen author/repository PDF',method='Exact family search followed by opening definitions, formulas and theorem proofs; source and target ordering checked separately.'),
 'diagonals':dict(queries='tautological algebra powers variety diagonals Euler characteristic partition algebra Frobenius | site.stacks.math.columbia.edu "excess" "intersection formula" | site.mathoverflow.net "diagonal" "Euler characteristic" "self-intersection" | site.stacks.math.columbia.edu "self intersection" "top Chern"',venues='Stacks primary text; Hua author preprint; MathOverflow lead',method='Matched the Euler/excess hypotheses and then checked the exact ungraded graph rule. The P¹ realization tests a separate universal-independence assertion.'),
 'motives':dict(queries='Grothendieck standard conjectures algebraic cycles1969 Jannsen numerical semisimplicity1992 | site.zbmath.org "Motives, numerical equivalence"',venues='Jannsen primary PDF; publisher/index leads including a zbMATH search',method='Matched coefficient field characteristic0, numerical equivalence, and the separate algebraic-Künneth condition in Corollary1.'),
 'Ktheory':dict(queries='site.stacks.math.columbia.edu Hirzebruch Riemann Roch Todd Euler characteristic | Deligne lambda perfect Dold Puppe1968 SGA6 | site.arxiv.org "lambda" "perfect complexes" "Barwick" | "K-theory and polynomial functors" Barwick Glasman Mathew Nikolaus',venues='Stacks; SGA6 frontmatter; arXiv; author paper; Springer primary2025 article',method='Read the exact Todd formula or modern operation theorem as applicable; retained historical and modern scope distinctions.'),
 'GIT':dict(queries='Mumford geometric invariant theory projective configurations R-partition pdf | Mumford Geometric Invariant Theory "R-partition" | site.dam.brown.edu/people/mumford "Geometric" | site.zbmath.org "Mumford" "Geometric invariant theory"',venues='Mumford primary book reproduction; Springer edition metadata; EGAII primary theorem; zbMATH search leads',method='Opened R-partition charts and Theorem3.8; followed exact EGA citation; independently checked cone/greedy steps. Missing OCR and source pages remain identified.'),
 'quadrics':dict(queries='quadric integral cohomology ring middle classes alpha beta hyperplane punctured cone Picard Lefschetz | "quadric" "Chow ring" "h" "l" Karpenko | SGA7 exposéXV Picard Lefschetz quadriques singularité quadratique ordinaire pdf | "SGA7" "Quadriques" pdf Deligne | Braden hyperbolic localization contraction Lemma6',venues='Karpenko author PDF; Deligne Numdam; Braden arXiv; SGA7 publisher metadata; Stacks',method='Matched integral/finite coefficients, splitness, relative dimension, regularity, orientation and weak equivariance. Computations/re-proofs are separate from published-source checks.'),
 'SGA3':dict(queries='SGA3 ExposéXII Tores maximaux groupe Weyl2.3 Polo Gille pdf | "SGA3" "XII" "Grothendieck" "1970" | "SGA3" "II" "1970" "Tores maximaux" | SGA3 tomeIII1970 structure schémas en groupes réductifs SpringerXXVXXVI',venues='SGA3XII primary retypesetting; Springer original-volume metadata; SMF program description',method='Compared exact source assertions with the selected numbered statements and their hypotheses; original1970 ink is distinct from checked2008 text.'),
 'Weyl':dict(queries='"SGA3" "2.3" "subtori" Weyl error | site.mathoverflow.net SGA3 XII lemma2.3 Weyl | SGA3 ExposéXII Tores maximaux groupe Weyl2.3 Polo Gille pdf',venues='SGA3XII primary retypesetting; MathOverflow/erratum searches; original-volume metadata',method='Read exact broad statement and proof; no matching erratum found in the recorded searches. Independently refuted the broad quantifier and proved the maximal-torus refinement.'),
 'Delzant':dict(queries='"Delzant" "Stiefel" "1962" "1366" | site.zbmath.org "Stiefel-Whitney" "Delzant" | Delzant Stiefel Whitney1962 Merkurjev norm residue degree two Milnor Theorem4.1 | Merkurjev On the norm residue symbol of degree2 1981 Mathnet | "Springer" "On the equivalence of quadratic forms" pdf | "Virtual forms" "Becher" | Witt "Theorie der quadratischen Formen" "176"1937',venues='Supplied offprint; Numdam; MathNet original1981 PDF; Milnor primary PDF; Witt original scan; Becher author/publisher; author bibliographies; zbMATH link403',method='Followed later references backwards to the exact1981 theorem; identified the actual J/I and degree2 symbol map. Springer’s original descent normalization remains unverified.'),
 'Oda':dict(queries='Oda first de Rham cohomology group Dieudonné modules1969 Corollary5.11',venues='Numdam primary article and metadata',method='Exact p-torsion/Dieudonné/de Rham and Hodge-filtration statement read; no claim that the missing cote54 wording was matched.'),
 'reflection':dict(queries='Bourbaki "Groupes engendrés" "III" "383" | Bourbaki archive383 réflexions | Coxeter1934 Discrete groups generated by reflections pdf | dual basis angle Coxeter chamber Gram inverse',venues='Coxeter primary1934 paper; Bourbaki official bibliography; Springer edition metadata; exact typescript-identification searches',method='Checked the classical theorem family and exact hypotheses; typescript author/number383 not fully identified. The A3 inverse-Gram counterexample and properness proof are independently saved.'),
 'DeligneDegeneration':dict(queries='Deligne Théorème de Lefschetz critères dégénérescence suites spectrales1968 Numdam',venues='Numdam primary article',method='Opened Proposition1.2 and Theorem1.5; matched the actual relative degree2 Lefschetz operator, not merely a fibrewise Kähler condition.'),
 'context':dict(queries='Grothendieck standard conjectures algebraic cycles1969',venues='Grothendieck primary paper; supplied source package and earlier notes',method='Searched published standard-conjecture naming, while refusing to invent the missing cote16 draft definitions.')
}
for c in claims:
 f=families[c['search_family']]
 searched_refs=[R[k] for k in c['refs']]
 searches.append(dict(search_id='SEARCH-'+c['id'],date=DATE,claim_id=c['id'],family=c['search_family'],claim_scope=c['statement'],queries=f['queries'],venues=f['venues'],method=f['method'],outcome=c['fate'],opened_urls=' | '.join(dict.fromkeys(r['url'] for r in searched_refs if r['url'] and r['note']=='verified')),reference_keys=';'.join(c['refs']),checked_extent=' | '.join(r['key']+': '+r['verification_level']+' — '+r['checked_extent'] for r in searched_refs),limits='No conclusion stronger than the opened extent. Exact first circulation is not assigned where unknown; no search non-hit proves absence.'))
tsv('search_log.tsv',['search_id','date','claim_id','family','claim_scope','queries','venues','method','outcome','opened_urls','reference_keys','checked_extent','limits'],searches)
blocked=[
 dict(date=DATE,claim_ids='SA05-C2054..SA05-C2065',query='site.zbmath.org "Stiefel-Whitney" "Delzant"; direct Zbl0108.04303 link from Laborde',url='https://zbmath.org/?q=an%3A0108.04303',outcome='Direct record returned403; no actual zbMATH review was read. Metadata and backward references checked in primary later papers.'),
 dict(date=DATE,claim_ids='SA05-C2057',query='Springer1959 exact title and DOI',url='https://doi.org/10.1016/S1385-7258(59)50026-8',outcome='Repeated open failure. Bibliographic lead retained as unverified; no exact descent-normalization conclusion inferred.'),
 dict(date=DATE,claim_ids='SA05-C2022..SA05-C2037;SA05-C2081',query='SGA7II full PDF; Quadriques and Picard–Lefschetz chapter searches',url='https://link.springer.com/book/10.1007/BFb0060505',outcome='Chapter metadata opened; large/full PDF routes failed or403. Exact local mathematical source checked in Deligne1974 and Karpenko instead.'),
 dict(date=DATE,claim_ids='SA05-C2002;SA05-C2069',query='SGA6 full PDF and Deligne perfect-complex lambda',url='https://geotoppos.org/divers/SGA6.pdf',outcome='The returned24-page document is frontmatter/contents, not the entire book. It certifies historical metadata only.'),
 dict(date=DATE,claim_ids='SA05-C2071..SA05-C2079',query='Bourbaki n383, reflection groups, III-1..7',url='https://www.bourbaki.fr/Ouvrages.html',outcome='Publication family identified; exact numbered typescript not identified. Do not confuse the printed number383 with a seminar exposé on another subject.'),
 dict(date=DATE,claim_ids='SA05-C2048;SA05-C2049',query='SGA3 XII2.3 Weyl subtorus erratum; MathOverflow targeted search',url='https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo12.pdf',outcome='No exact erratum found in recorded searches. The checked retypesetting retains the broad claim; mathematical counterexample is independent.')]
tsv('blocked_searches.tsv',['date','claim_ids','query','url','outcome'],blocked)

# Mathematical check events, distinct from the base provenance events.
proofs={
 3:(1,'Pull–multiply–push action identity derived with explicit projection/base-change hypotheses.'),
 4:(1,'Action/composition compatibility derived without reordering factors; the sign depends on the chosen graded order. The malformed intermediate pushforward is separately flagged.'),
 5:(1,'Diagonal unit action derived by the projection formula and p∘Δ=id.'),
 6:(1,'Both associations reduce to the same four-factor expression; both unit laws checked.'),
 7:(2,'Every two-/three-factor identity follows from transverse equality constraints, diagonal normal bundleTX and top-degree vanishing. Chow and cohomological normalizations kept distinct.'),
 10:(2,'Counted actual free coordinates, including the mandatory empty block; supplied the one-coordinate counterexample.'),
 11:(2,'Equality-locus intersections identified set-theoretically and the transverse class case separated from excess.'),
 12:(2,'Computed the excess quotient TX⊗(k^k/(U_R+U_R′)) and its rankk+1−s−s′; Euler and vanishing cases follow.'),
 13:(2,'Closure under each coordinate integration checked after reducing products; external products and permutations are direct.'),
 14:(1,'Projector splitting and identity in the idempotent completion checked algebraically.'),
 16:(3,'An invariant open subset ofG×A isG×B, by restricting to the identity slice.'),
 20:(3,'The successive-difference formula proves the ordered-weight cone decomposition for everym.'),
 21:(3,'The nonzero condition is necessary; corrected separation theorem stated in the appropriate span.'),
 23:(4,'All flat/projective/generic/special-fibre hypotheses of the ramified quadric example checked; total-space singularity explains why the regular theorem does not apply.'),
 24:(4,'Retained the H⁰ unit in the exact sequence; established the reduced-cohomology formulation.'),
 25:(4,'Identified the punctured cone withO(−1)^× and its Gysin class−h.'),
 26:(4,'The connected-pair long exact sequence gives local cohomology as shifted reduced cohomology and the low-degree vanishings.'),
 27:(4,'Applied the integral quadric hyperplane map to the Gysin sequence in all dimensions; finite coefficients require the adjacent kernel.'),
 28:(4,'Applied the two central even-quadric maps to obtain free groups inD,D+1; Q² tests the correction.'),
 30:(4,'Constructed the explicit diffeomorphismU≃TS^D, retraction and compact-support groups; separatedD=0.'),
 31:(4,'Compared complex and tangent/normal orientations to obtain(−1)^{D/2}2 in even dimension and0 in odd dimension.'),
 33:(4,'Used the sum/difference basis to compute index2 and the image ofλ in the quotient by the hyperplane class.'),
 34:(4,'Ruling-intersection parity gives the signed primitive square; Q² is a complete counterexample to the unsigned assertion.'),
 35:(4,'Both ruling classes have the same adjacent restriction/pushforward image, so their difference maps to0.'),
 36:(4,'Derived the integral hyperplane matrices from the cellular/ruling basis; the general pattern is a proof, not extrapolation fromD≤8.'),
 42:(5,'Under the cited product-image theorem, the torus image ofR×T contains maximalT and hence equalsT. Structural representability input remains cited.'),
 44:(5,'Lower semicontinuity ofρr and upper semicontinuity ofρn sandwich both ranks at a point withρu=0.'),
 49:(5,'Maximal-torus conjugacy insideC_G(R)^0 makes(N(R)∩N(T))/C(T) surject ontoW(R); hypotheses explicitly retained.'),
 50:(5,'Verified group law, inverse, identity, smoothness and the generic/special fibres of the degeneration.'),
 58:(6,'Kummer classes and the diagonal product formula commute with field restriction, giving naturality.'),
 59:(6,'Using the checked classical local/global classification as an input, proved that total real Stiefel–Whitney classes recover the negative index and extended the injection to virtual forms.'),
 61:(6,'ProjectionGW→W identifiesJ withI; kernel, surjectivity and multiplicativity of the ideal map explicitly proved.'),
 62:(6,'Expanded the exact total class ofd_a d_b to obtainw₂=(a)∪(b), and provedJ³ is invisible in degrees≤2.'),
 65:(6,'Applied the checked Kummer exact sequence and Pic(SpecF)=0; charF≠2 is indispensable.'),
 67:(4,'Exterior-square expansion gives the factor2; this is an integer-map analogy only, not an isomorphism of full geometric algebras.'),
 71:(7,'Essential-space decomposition, faithfulness and conjugation of reflections checked directly.'),
 72:(7,'The nearest-orbit-point reflection argument proves chamber transitivity and wall generation.'),
 73:(7,'Two-dimensional dihedral reduction gives the simple-normal angle and the negative-entry bound.'),
 75:(7,'Read and checked the positive-coefficient argument; simple reflection preserves all other positive normals. “Positive” is nonnegative as used in the proof.'),
 76:(7,'Local chambers around a point and simple transitivity give the stabilizer description; uniqueness applies to the chamber representative, not every carrying element.'),
 77:(7,'Invariant orthogonal projections commute with each rank-one reflection; generators split into commuting summand subgroups.'),
 78:(7,'Properness permits only finitely many reflections whose mirrors meet a fixed compact ball; this completes the cut-off proof.'),
 79:(7,'Inverse-Gram positivity proves the valid essential-chamber corollary despite the false dual-angle equality.')}
for n,(section,outcome) in proofs.items():
 event(f'SA05-C{2000+n}','independent re-proof',outcome+f' Current reconstruction: outputs/proof_notes.md §{section}; cited structural inputs are not independently re-proved.')

targeted={
 1:'Conditional perfect-duality and quotient-operation hypotheses checked against the passage and the opened correspondence framework; no universal integral freeness claim.',
 2:'Exact HRR trace formula includes the Todd class; no full GRR proof repeated.',
 9:'Hua’s exact ungraded graph reduction checked against the source generator/relations gap; no realized-kernel or independence theorem inferred.',
 15:'Jannsen Theorem1 and Corollary1 read with characteristic0 and algebraic-Künneth hypotheses separated.',
 17:'Projective-frame uniqueness and regular minor-ratio inverse mechanism checked; missing3.5/3.16 and incomplete OCR prevent a full symbol-by-symbol proof certification.',
 18:'Greedy minimum-weight basis argument independently checked; exact published monomial OCR remains incomplete.',
 19:'Theorem3.8 matches the stable configuration and descended polarization; EGAII4.5.2 criterion checked at its actual source.',
 22:'Regular ordinary-smoothing hypothesis and source shift of vanishing-cycle degree checked against Deligne§4.',
 29:'Braden Lemma6 proof checked and specialized to the weakly equivariant positively contracted cone.',
 32:'Karpenko integral cellular basis and Gysin sequence resolve ranks and free middle extension; no canonical extra splitting asserted.',
 37:'Karpenko Theorem1.10 and its ruling/cell proof read with splitness retained.',
 38:'SGA3XII1.7 exact semicontinuity theorem and base-change invariance compared.',
 39:'SGA3XII1.7 local-existence equivalences checked with local constant reductive rank.',
 40:'Exact conjugacy and rank corollaries checked; constancy of a difference is not inferred from semicontinuity alone.',
 41:'Representability1.10 and affineness5.4 checked under affine/rank hypotheses.',
 43:'Exact unique/central maximal-torus corollaries read; hypotheses not dropped.',
 45:'Definition of fibrewise maximal torus and distinction from containment-maximality read; the deferred converse is not generalized.',
 46:'SGA3XII2.2 proof read, including reduction to a strict henselian trait and fibre-group injection.',
 47:'Exact finite étale maximal-torus Weyl quotient and base-extension statement read.',
 51:'Fibrewise reductive-centre criterion4.3 compared with its affine-fibre hypothesis.',
 52:'Exact field existence theorem4.4 read and distinguished from the truncated source proof.',
 53:'Theorem4.7(b) and proof read with smooth affine connected-fibre hypotheses; absent source parts stay absent.',
 54:'Witt binary-chain input and Becher exact virtual-form presentation checked; GW retains rank.',
 55:'Witt p38 Satz11 binary-case proof checked; corrected an earlier provisional theorem locator.',
 56:'Grothendieck’s rank-bearing total-class ring and Laborde’s comparison/naturality text read; no ordinary coefficientwise ring multiplication substituted.',
 63:'Original Merkurjev theorem plus Milnor’s exact degree2 comparison read; independently checked J/I and the symbol identify this exact arrow.',
 64:'Original1981 quaternion-symbol theorem and the later author’sTheorem2.2 read; its surjectivity answers the precise question.',
 66:'Oda Corollary5.11 exact characteristicp/perfect-field/Hodge-filtration scope read; absent cote54 endpoint not certified.',
 68:'Actual Künneth/Poincaré correspondence convention and Grothendieck§3 action formula checked; twists and grading not suppressed.',
 69:'Modern theorem scopes checked in BGMN and Köck–Zanchetta; SGA6 frontmatter used only as metadata.',
 70:'Deligne Proposition1.2 and Theorem1.5 read with an actual relative degree2 Lefschetz operator.',
 74:'Coxeter Theorems4/8 and source representation argument checked; absent preceding source sections are acknowledged.',
 82:'SGA3XII7.1(a,b) exact local-torus hypothesis and7.7(a) warning read; introductory promises not universalized.'}
for n,outcome in targeted.items():event(f'SA05-C{2000+n}','used and rechecked in this run',outcome)
for key in ['StacksCorr','StacksSelfIntersection','StacksExcess','Braden2003']:
 event(key,'targeted proof check',R[key]['checked_extent']+' The relevant argument and its application were checked; no broader source theorem is certified.')
for r in refs:
 event(r['key'],'used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found',r['verification_level']+': '+r['checked_extent']+(' This is a bibliographic lead only, not a mathematical theorem check.' if r['note']!='verified' else ''))

computations={
 'P1_correspondence_composition':[3,4,5,6],
 'P1_tables':[7,8,12,13],
 'middle_lattice':[22,33],
 'quadric_surface':[28,31,34,35],
 'integral_quadric_Gysin':[27,28,32,36,37],
 'finite_coefficients_qualification':[27,36],
 'exterior_model':[67],
 'Gm_Ga_model':[50],
 'SL4_Weyl_counterexample':[48],
 'ordered_weight_cone':[20,21],
 'Delzant_symbol':[62],
 'real_signature_bits':[59],
 'reflection_dual_angle_alarm':[79],
 'ramified_quadric_smoothing_counterexample':[23]}
computations['GIT_five_point_chart']=[16,17]
computations['GIT_greedy_basis']=[18]
for section,nums in computations.items():
 for n in nums:
  event(f'SA05-C{2000+n}','computation or formal certificate',f'Exact Python/Sympy computation executed and saved: programs/checks.py; outputs/checks.json[{section}]. It is a finite/algebraic check within the explicitly stated hypotheses, not a Lean certificate or a proof of an arbitrary geometric statement.')
for n,refined,why in [
 (8,2009,'The realized list need not be independent: Δ12=h1+h2 onP¹. The refinement is generation plus the explicit realization-kernel problem.'),
 (10,2010,'The mandatory empty block adds no free coordinate; the corrected dimension counts nonempty unmarked blocks.'),
 (21,2021,'The zero functional invalidates the criterion without a nonzero requirement.'),
 (23,2023,'An even-ramified flat projective quadric family is generically constant and has trivial inertia; the refinement requires a regular ordinary smoothing and suitable coefficients.'),
 (24,2024,'An all-degree identification loses H⁰; the refinement uses reduced cohomology or retains the unit term.'),
 (27,2027,'The conic puts integral2-torsion in degree2ν, not2ν−2.'),
 (28,2028,'Q² puts the lower middle free group in degree2ν, not2ν−1.'),
 (34,2034,'Q² gives a negative primitive square; the refinement includes(−1)^ν.'),
 (48,2049,'SL4 gives W(R)=C2,W(T)=1 for nested nonmaximal tori; maximalT is the proved refinement.'),
 (60,2059,'Rankless positive Stiefel–Whitney classes do not distinguish positive real forms of different ranks; the source’s final rank-bearing theorem survives.'),
 (79,2079,'EssentialA3 disproves the dual-angle equality; inverse-Gram positivity proves the valid corollary.')]:
 event(f'SA05-C{2000+n}',"refuted, with the refined statement's id",f'Refined statement: SA05-C{refined}.statement. {why} Every example hypothesis is checked in proof_notes.md and/or checks.json; no diplomatic edit is made.')
event('SA05-C2057','carried as background without fault found','The general Clifford/Hasse–Witt relationship is identified, but the cited Springer1959 descent normalization remains unverified; no independent proof claimed.')
for n in [80,81]:event(f'SA05-C{2000+n}','used and rechecked in this run','Source incompleteness and the surrounding searched literature checked. The exact omitted statement cannot be identified; no invented theorem or proof.')

dump('items.json',items);dump('claims.json',claims);dump('problems.json',problems)
tsv('entries.tsv',['entry_id','item_id','verdict','reason'],sorted(entries,key=lambda x:int(x['entry_id'].split('#')[1])))
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence','reading_id'],readings)
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)
tsv('our_projects_links.tsv',['kind','from','to','what','evidence','note_ids','run_names','status'],[x for j,x in enumerate(external) if j not in (0,5)])
tsv('unverified_link_leads.tsv',['kind','from','to','what','evidence','note_ids','run_names','status'],[{**x,'kind':'folder'} for j,x in enumerate(external) if j in (0,5)])
tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
dump('outputs/counts.json',dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),checked_links=len(links),external_leads=len(external),references=len(refs),searches=len(searches),events=len(events),verdicts=dict(collections.Counter(x['verdict'] for x in entries)),classes=dict(collections.Counter(x['class'] for x in claims)),statuses=dict(collections.Counter(x['status_on_pages'] for x in claims))))
print(json.dumps(dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),references=len(refs),searches=len(searches),events=len(events))))
