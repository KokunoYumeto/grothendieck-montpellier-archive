# Fresh independent review: the actual nonstandard tower specialization test

Reviewer: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC.

## Snapshot and verdict

The complete agent_nonstandard_tower_specialization.md was read, including every proof. The initial reviewed snapshot had SHA-256 e6138d3983de89f387a509071e9f054405c91d1b60b231615ac0d480f21e23d2. One wording clarification was then applied and re-read: “module at tower rank six” distinguishes tower rank from dimension. The resulting 235-line snapshot has SHA-256 59185f2bb1bf8b5521540904e0bf050b668191cf44748abd3a20235a8c9f5afc.

**PASS. No mathematical blocker found.** This is a fresh review of the entire report and an independent reconstruction of the small specialization obstruction. It does not yet cover a later generated final-text insertion.

## Primary-source applicability

The primary PDF arXiv:1201.2209v2 was freshly opened and downloaded as primary_sources/Blasiak_1201_2209.pdf, with a text counterpart. Theorem 5.1 and the entire restriction statement on printed p.14, Proposition 5.2's proof on p.15, and Definition 6.1 with the following scope discussion and Remark 6.2 on p.23 were read directly.

These sources do give the split semisimple two-row quotient, the four simple-label types and the stated restriction rules. Their index-set display is equation (25) in the PDF. The restriction proof derives the off-diagonal formulas from ordinary branching and the signed formulas from symmetric/exterior powers, exactly as used in the report. The complete lengthy irreducibility proof of Theorem 5.1 is cited, not claimed independently re-proved here.

The source explicitly supplies generic seminormal lines up to diagonal scalars and treats compatibility at \(v=1\) as an additional issue. The report's new rank-four calculation is not attributed to that source.

## Generic branching and the six-dimensional test module

A two-row shape has at most two removable corners. The scalar multiplicity in the trace-free symmetric-square restriction is therefore zero or one. Distinct partitions cannot have two distinct common immediate predecessors: the coordinatewise union of those predecessors would have to be both partitions. This rules out duplication when the ordered predecessor pairs are made unordered. Zero signed modules for one-dimensional ordinary factors are correctly omitted.

Thus the path counting statement really counts generic simple dimensions. Its encoding cost is polynomial in the expanded rank \(r\); the report correctly declines to turn this into a bound in \(\log r\) or into a rule for classical Kronecker coefficients.

For the rank-four label \(\{(3,1),(2,2)\}\), ordinary branching gives
\[
(3,1)\downarrow S_3=(3)\oplus(2,1),\qquad
(2,2)\downarrow S_3=(2,1).
\]
The actual rank-three decompositions therefore give the four summands
\(N(\delta),N(D-2),\epsilon_+,\epsilon_-\), of dimensions \(2,2,1,1\). The first one is the ordinary first-factor trivial line tensored with the second-factor standard module, so the particular plane being studied is identified, not merely characterized by its dimension.

The S4 character product was independently recomputed:
\[
(3,1,-1,0,-1)(2,0,2,-1,0)
=(6,0,-2,0,0).
\]
It is the sum of the standard character and its sign twist. Hence the specialized six-dimensional module is exactly \([(3,1)]\oplus[(2,1,1)]\), with each constituent once.

## The regular Hecke projector and saturation

For the convention \((T_i-v)(T_i+v^{-1})=0\), put
\(a=\sum_{w\in S_3}v^{\ell(w)}T_w\).
Pairing terms across a simple reflection verifies
\(T_i a=aT_i=va\). Therefore
\[
a^2=\left(\sum_{w\in S_3}v^{2\ell(w)}\right)a.
\]
The denominator is six at \(v=1\), hence invertible in the specified characteristic-zero DVR. This proves the central idempotence and regularity of the displayed \(p_+\), with the ordinary averaging projector as its special value.

Its image on the fixed Specht tensor lattice is a direct summand. Over the DVR it is free, and its rank is two by either the generic branching or the special-fiber invariant-line calculation. Since \(p_+\) is central in the parabolic ordinary algebra, its first-factor action commutes with both nonstandard generators \(P_1,P_2\). Thus the plane is an actual \(A_3\)-stable regular summand.

The equality
\[
E_R=E_K\cap M_R
\]
is exact: an integral vector in the generic image is fixed by the regular projector and therefore belongs to its integral image. This is the key fixed-lattice fact. It prevents a meromorphic scalar renormalization of a generic line in \(E_K\) from producing a nonzero special vector outside \(E_1\).

The additional \(A_2\) projectors \(P_1/D\) and \(1-P_1/D\) are regular because \(D(1)=4\). They separate the two generic path lines in this plane, so regular nonzero representatives exist. The obstruction is not vacuous through an assumption that the lines cannot be normalized at all.

## Independent reconstruction of the compression

Use the standard sum-zero model \(U\subset\mathbf R^4\) and the pairing sum-zero model \(W\subset\mathbf R^3\). The S3 subgroup fixing the fourth letter has invariant vector
\[
w=(1,1,1,-3),\qquad \|w\|^2=12.
\]
The averaged first-factor projector therefore becomes the orthogonal projector \(p\) onto this line, and \(E_1=\mathbf Rw\otimes W\). This identification is compatible with the actual projector under any equivariant realization of the ordinary Specht modules; it is not a new choice of a different penultimate plane.

For an internal transposition, \(w\) is fixed and \(p\tau p=p\). For an external transposition the dot product is \(-4\), giving \(p\tau p=-p/3\). In the quotient action on pairings, each of the internal and external triples maps bijectively to the three transpositions of S3. Their sum in its three-point permutation module is the all-ones matrix, which kills \(W\).

Writing \(Z\) for the sum of all six transpositions and \(\Pi=p\otimes1\), these exact identities give
\[
\Pi Z\Pi=p\otimes(0-\tfrac13\,0)=0.
\]
On the two specialized irreducibles, the central class sum has eigenvalues
\(6(1)/3=2\) and \(6(-1)/3=-2\).
If a nonzero \(x\in E_1\) lay in either irreducible, then
\(\Pi Z\Pi x=\pm2x\), contradicting the zero compression. Both claimed intersections are consequently zero.

The optional equal-norm refinement also checks: the orthogonal central projectors are \(\frac12(1\pm Z/2)\), whose compressions are \(\Pi/2\). Their projections of any \(x\in E_1\) each have squared norm \(\|x\|^2/2\).

## Conclusion and exact limits

Each of the two generic tower lines through \(N(\delta)\) stays in \(E_K\). Every scalar renormalization that is regular in the fixed lattice and has a nonzero reduction specializes into \(E_1\). Since that plane has zero intersection with both final irreducibles, none of those vectors can become a basis vector in either constituent. A basis partitioned by the two constituents therefore cannot arise from diagonal renormalization of these seminormal lines.

The statement leaves mixing across generic path components, other integral lattices, different canonical-basis constructions and different counting rules open. Mixing only within this particular plane would still stay in it; the report makes no claim that arbitrary mixing always repairs the issue. The conclusion is exactly the stated fixed-lattice diagonal-normalization limitation.

This review used explicit character, idempotent and inner-product calculations; no floating-point sampling or formal-kernel certificate is claimed.

# Fresh review of the F30 regular mixing supplement

Reviewer: /root/rectangular_and_theta. Date: 2026-11-21 UTC. The complete agent_nonstandard_tower_mixing.md was read and checked at SHA-256
7722d1cf31b8804bd18f55e58c968a2158eeb0f03db4b8dad0f7a399e7a03d7e.

**PASS. No mathematical blocker found.** This is a fresh full-proof check of the supplement, using the independently checked rank-three decomposition and original F30 orthogonal compression. It does not yet cover a generated final-text fragment containing the supplement.

The ordinary parabolic projector p+ commutes with each first-factor Hecke generator and hence with the rank-three nonstandard generators. Therefore its complementary rank-two and rank-four summands commute with the regular central block idempotents used to define the two scalar lines and F_R. The latter construction separates E_R first by an ordinary projector; it never requires dividing by the colliding central-root difference. The generic ranks and freeness over the local ring are correct. At specialization the central matrix block is precisely the standard S3 isotypic component, so F is the standard copy in the orthogonal complement of E, as required by the next argument.

The class sum Z commutes with S3. Thus Z(E) lies in the sum of the two standard copies, and the already checked equation Pi_E Z Pi_E=0 removes its E-component. Since Z²=4 and both copies have dimension two, Z exchanges E and F isomorphically. Consequently J=Z/2 is an involutive isometry on E+F, exchanging the planes, and the two graph planes x±Jx are exactly its eigenspaces. The trivial and sign S3 lines occur only in the corresponding 31 and 211 restrictions, respectively; adjoining those lines to the graph planes therefore gives the actual two S4 constituents, not merely arbitrary three-dimensional subspaces.

On each regular standard plane, e=P1/D and 1−e are commuting-with-that-plane rank-one idempotent summands. Their R-bases represent the four actual generic path lines. Since J commutes with s1 at specialization, it identifies corresponding plus and minus lines; all comparison scalars lie in Q*, so the stated constant-unit rescaling is valid over R. Each Hadamard block has determinant −2, a unit, and hence the resulting six vectors remain a basis of the fixed lattice. Their reductions give the claimed bases of the graph planes and final S4 constituents. This uses mixing across two different penultimate summands, exactly the freedom excluded from the earlier diagonal-only obstruction.

The commutant computation is also exact. Split generic simplicity gives End_(A_K)(M_K)=K. An R-linear scalar on the free lattice must have scalar in R, giving End_(A_R)(M_R)=R. At specialization the actual image contains every diagonal adjacent transposition because P_i/2−1=s_i, so its commutant is the S4 commutant k×k. The base-change map is a↦(a,a), with one-dimensional cokernel. Thus neither classical projector is the specialization of an A_R-linear endomorphism. This conclusion does not conflict with the regular mixed basis: its two three-vector spans are direct summands of the underlying free module but cannot be stable under the generically simple nonstandard action.

The construction is correctly limited to this actual rank-four module; no general algorithm, canonical basis, positive multiplication rule, geometric realization or generic projector lift is asserted. No formal-kernel verification was performed.


## Generated F30 final-fragment match

The complete finding_F30.tex fragment, 253 lines, was read and compared with both full reports checked above. One wording correction was requested and applied: \(e=P_1/D\) is now described as the idempotent from tower rank two, not as an idempotent of matrix rank two on the six-dimensional module. Corrected fragment SHA-256:
cc6176fe6f45563b644677d3a73e118cc6ca6e11935a4a10ff0ba0f20e30dac0.

Verdict: **PASS.** The original diagonal-normalization obstruction, actual regular mixing repair, and one-dimensional commutant base-change cokernel all match the checked reports. The coherent dictionary correctly distinguishes regular underlying-bundle automorphisms from endomorphisms commuting with the full deformation algebra. The known path count is correctly a generic simple-dimension count, with complexity measured in expanded tower rank.

At the snapshot in which this check was recorded, the main paper did not yet contain the entire corrected fragment as exact text. Thus this event certifies the generated fragment, not its later insertion. No entire-paper check is implied.

