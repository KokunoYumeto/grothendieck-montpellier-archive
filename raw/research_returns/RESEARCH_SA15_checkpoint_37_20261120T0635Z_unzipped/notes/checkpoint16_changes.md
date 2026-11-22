This checkpoint advances the proved gates in A.3, A.4, and B.4. The general questions remain explicitly open. All results below were subjected to complete independent proof audits; finite computations certify only their stated algebraic scope.

## All degrees on the fixed supersingular product

For E:y²+y=x³ in characteristic two, X=E² and L=O(3O) external-tensor O(3O), the geometric and arithmetic relative images now agree in every degree. In odd degree they are GL_(9d²−1)(F2). In even degree they are the full stabilizer of the unique invariant covector, F2^(9d²−4) semidirect GL_(9d²−4)(F2), acting in rank9d²−3. The unique proper nonzero invariant subspace in the even case is its covector kernel.

The new even proof identifies the first Frobenius image and its negative reflexive extension. A reduced irreducible determinant for the finite intersection algebra on an odd boundary has degree18ae+9e². Two odd decompositions force irreducibility and reducedness of the global unit-Hasse form for every even degree at least four; the degree-four comparison uses the irreducible restriction factor of degree135. The exact degree-two theorem and the previous all-odd theorem complete all degrees. The marked contact incidence may be inseparable in characteristic two: reducedness is proved from the finite algebra itself, not inferred from separability. Root, monodromy, and the other two agents independently checked the whole argument.

## All mixed elliptic-product ranks, without a modulus exception

For every ordinary elliptic curve E_o, every supersingular elliptic curve E_s, every perfect characteristic-two field and all positive integers a,b,d, the product system O(3ad O) external-tensor O(3bd O) has relative generic stable rank9abd²−1−epsilon(ad). Here epsilon(n) is one for even n and zero for odd n. This closes the residual thin strip, including4 dividing a withb=d=1.

The proof uses the ordinary Frobenius decomposition F_*O=O direct-sum B and two exact evaluation isomorphisms. A two-dimensional kernel-to-cokernel test is a residue matrix [[t,u],[v,t]]. Varying b1 by b1+lambda b2 fixes t and v and changes u by a polynomial with a nonzero linear coefficient. Separate evaluation arguments ensure both that coefficient and v are nonzero. The complete symbolic verification contains13 identities; it does not replace the all-degree proof.

The new positive-index nonproduct result is separate. For a mixed abelian surface with ordinary polarization index a>0, D=chi(M), and L=M³, the odd-degree ranks lie between9Dd²−2^a and9Dd²−2; the even-degree ranks lie between9Dd²−2^(a+1) and9Dd²−2. The a=1 odd-degree formula is exact. The upper bound is a scheme-theoretic Prym obstruction, and the lower bounds descend the actual line bundle through the entire ordinary etale kernel and pull back an index-zero sharp curve. The connected etale pullback multiplies the defect exactly. Sharpness for a>=2 in odd degree and every positive a in even degree remains open. No index-zero ample class on the original surface is assumed.

## Every degree at transcendental ordinary modulus

For X=E_o times E_s with the (3,3) embedding, when j(E_o) is transcendental over F2, the odd-degree geometric and arithmetic groups are GL_(9d²−1)(F2). The even-degree groups are the full pointwise stabilizer of two independent covectors, Hom(F2²,F2^(9d²−4)) semidirect GL_(9d²−4)(F2), in rank9d²−2. Every nonzero invariant subspace contains the irreducible common covector kernel.

The proof treats the geometric generic ordinary modulus. A connected special frame fibre forces a connected geometric generic frame fibre by a normal finite-etale cover argument, requiring no properness of the coefficient open. In even degree two, two exact coefficient points lie in the total arithmetic family image; the geometric generic image is normal there. An actual GL8 block and a degree32 irreducible nonreciprocal Frobenius polynomial give GL32, while the second point excludes every incomplete translation kernel. Normality then yields the whole geometric generic stabilizer. Explicit normalized derivations over F2(t) establish the two arithmetic covectors without a perfect-base shortcut. Every even degree at least four follows from the mixed intersection-Hasse degree argument.

This does not prove the groups for each fixed algebraic ordinary j, including finite-field elliptic curves. Reversing specialization would be invalid. The candidate file was renamed to generic_mixed_product_all_groups.tex upon promotion; its six existing mathematical identifiers retain their suffixes for identity continuity, with visible status Proved. Its final scope remark has the explicit identifier rem:generic-mixed-modulus-gate.

## The sharp unramified dyadic height-two index

The exact least manuscript index is now nu_min(2,1,2)=3, using M(nu)=ker2^(nu+1). Thus16-torsion determines the prime-to-two inertia character in the stipulated potentially good height-two class, and the earlier explicit8-torsion ambiguity makes this sharp. Within the potentially supersingular elliptic subclass,8-torsion already suffices.

The proof first realizes every finite height-two supersingular inertial type by an actual elliptic deformation and excludes mixed height-one/height-two comparisons at16. A graph/logarithm bound narrows the joint good-reduction degrees. The residual images1,C2,C3 are then treated exhaustively. Full rational2-torsion uses explicit Legendre/Kummer matrices; residualC2 passes to the unique rational2-isogeny quotient and compares quadratic-field valuations. ResidualC3 uses the actual marked8-congruence models, with their four Weil-pairing multipliers, and a trace-zero cubic normalization. The source family's universal discriminant identity and all valuation branches are checked exactly. The marked-family exhaustion is justified over every characteristic-zero field, including j=0 and1728, by Chen's finite-group cocycles and Fisher's Hesse family. The corresponding p3,e2,height2 index remains the previously proved value2. Other heights and ramification indices remain open.

## Exact computations and actual runtimes

| Program or certificate | Scope | Author time in seconds | Root rerun in seconds | Other complete reruns |
|---|---|---:|---:|---|
| mixed_thin_residue_checks.py |13 universal residue identities |0.1971881189965643 |0.1764095999969868 |RD0.19381124299980002; monodromy0.08660112699726596 |
| B44 height-two mixed gate |Finite group and height-two reduction algebra |0.07470255399675807 |0.06556921700394014 |OC0.06939755400526337 |
| B45 logarithm gate |192000 logarithm-degree and24576 coefficient-valuation checks |0.0776823170017451 |0.23222537100082263 |OC0.05902020299981814 |
| B46 residual-trivial gate |Universal halving/Kummer identities and valuation branches |0.12948673400387634 |0.35755470999720274 |OC0.3844016500006546 |
| B47 residual-C2 gate |Universal isogeny identities and exhaustive valuation cases |0.20210709299863083 |0.047221027001796756 |monodromy0.15887224199832417 |
| verify_p2_residual_c3_gate.py |8 universal identities,20301 valuation and3721 normalization cases |0.6555589939962374 |0.8482220709993271 |OC0.5984987490010099 |
| mixed_degree_two_group_discovery.py |306 coefficient trials and51 exact characteristic polynomials |4.062721072004933 |Not rerun as a proof |Discovery output retained |
| verify_mixed_degree_two_group.py |Independent coordinate-ring reconstruction of two36-dimensional matrices |0.4645676829968579 |0.4050763330014888 |RD0.3759362999990117; OC0.5512123770022299 |

The current exported-program inventory supplies every exact path, output and scope; author outputs remain byte-for-byte unchanged by the independent reruns. Universal geometric proofs, including the positive-index descent and even boundary arguments, are not mislabeled as computational certificates. All executed exploratory programs and their failures remain in the changed working files, even when unused by the paper.

## Primary-source checks and corrections

Tate's1968 original on residues was opened and Theorems2–3 with their corollary on pp155–156, and Section4 Theorem5 with its corollary on pp157–159 were read. Illusie's1979 original Cartier formula, Theorem2.1.9 and formulas2.1.12–13 p515, were freshly read from the retained original; the web fetch exceeded the file-size limit, which is recorded as a failed retrieval rather than a successful web opening.

Crew's1984 original was opened and Theorem1.5, Corollaries1.7–1.8, equation1.8.2 p36, and Section3's first alternative proof p42 were checked; original pp36 and42 were actually viewed. The exact quotient, isogeny duality and theta-group descent passages in Edixhoven–van der Geer–Moonen were freshly read at4.38/4.40 pp65–66,7.5/7.6 p100, and8.10/8.11 pp116–117. Kantor–Seress Theorem3.6 printed p22 was actually viewed again for the exact transvection alternatives.

For B44, Hewett's1995 Theorem1.4/Corollary1.5 p520 and Tate's1975 reduction table p46 and Section4 pp41–44 were read in the originals. For B45, the published Bondarko original, including Theorem2(8)/equation6 p668, Propositions6/8 pp673–674, Propositions9–12/Lemma3 pp674–676, and all of Proposition16 p681 were freshly read. The coefficient ideal at p2 is2R; no odd-prime hypothesis was imported. A direct hashed URL redirected to a homepage; the cached original succeeded and both outcomes are recorded.

For B48, Chen arXiv1405.6385v3 Theorems1.1–1.4, all Sections2–6, the actual finite-group cocycle/scaling proofs, and Appendix p21 were read. Fisher's original Hesse paper was opened after a direct-URL timeout through its cached original and arXiv copy; Lemma8.4/equation8.1/Remark8.6 pp19–20, Theorem13.2 with proof pp29–30, and the exceptional-j and reverse4 discussions pp30–31 were checked. Chen's Lemma3.2 prints the opposite cusp-sum linear sign from the main models; the proof uses the main-model sign and independently verifies the resulting universal discriminant identity. The Chen-to-Fisher basis matrix has determinant6T, so its smooth-family use excludes no exceptional j-value.

Earlier rejected drafts are retained: B45's first-crossing r0 off-by-one statement and B46's opposite differential sign. Neither is used as a theorem. The source sign discrepancy in B48 is explicit. Further fixed-modulus mixed-product Pfaffian exploration includes an incorrectly chosen preliminary Q-point; its failed program and output are retained, and no monodromy assertion relies on it.

Manuscript scans remain unavailable; quoted manuscript readings are the supplied AI-produced transcriptions. Michel Hua's project remains an unused witness. The work is credited to GPT-6 Astra (OpenAI, ChatGPT Pro mode), with no claim of priority.

## Final checkpoint verification

The complete paper contains402 pages and2934604 bytes. All47 selected pages were actually viewed by the root and three independent reviewers. The selection covers every new subsection, earlier samples, the repaired overflow locations and the final bibliography. The two original overflow pages were also actually viewed by the root and are retained as the specifically discussed problem images.

There were three build attempts. The first stopped on an extra alignment tab in the two-pencil display after29.547 seconds; its full merged source, source fragment, log, console and actual runtime are retained. The first successful build took159.535 seconds and had two boxes above2pt (55.7315pt and24.32054pt), plus one0.41342pt line. Separating the residue matrix from its three entry definitions and shortening the B44 runtime lead-in repaired both large overflows without changing the mathematics. The final successful build took170.182 seconds and has1 overfull boxes, maximum0.41342pt, zero above2pt, and no undefined references, citations or missing glyphs. The before/after counts above2pt are2 and0.

There are453 numbered statements, a net addition of39 since checkpoint15. The42 new identifiers include three existing scope remarks whose content-derived labels changed when the newly proved even-degree consequence replaced the earlier open gate. Root read all three complete old/current pairs; the explicit injective map is in outputs/statement_identity_checkpoint16.json. The first inventory identified three new scope remarks without explicit identifier events; their full passages were then actually checked and all three events recorded. Final coverage confirms every new identifier has an explicit event and every statement has its final number.

The current bibliography has146 entries and the source census147 rows, including the unused Hua witness. The final merged registers and program-export inventory supply their exact counts. Further generic nonordinary-ppav, fixed-modulus mixed-product, positive-index first-image and next-prime inertia investigations are separate post-checkpoint candidates, excluded from the inspected paper and proved outcome table.

The actual review10 is recorded at or after14:50:40UTC; the archive is created only after that review and the scheduled checkpoint time. The next checkpoint is due15:35:40UTC and next hourly review15:50:40UTC.

### Existing scope remarks updated by proved results

| Earlier identifier | Current identifier | Reason |
|---|---|---|
| auto:A_monodromy:abc2304989b0 | auto:A_monodromy:c25cfd1730a5 | Existing scope remark now points to the proved all-even group theorem; all previous failed-witness and computational-scope text is preserved. |
| auto:A_monodromy:c2d3a12ed050 | auto:A_monodromy:1e009f1c7aa8 | Existing scope remark now points to the proved all-even group theorem; all previous failed-witness and computational-scope text is preserved. |
| auto:A_monodromy:d4e480cdd0c6 | auto:A_monodromy:0c2f1cb265b6 | Existing scope remark now points to the proved all-even group theorem; all previous failed-witness and computational-scope text is preserved. |
