# Independent whole-proof and arithmetic audit: D-HOS-07–10

**Result: PASS.** Checker: /root/imprimitive, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. Date/time: 2026-11-21 20:34:28 UTC.

## Frozen files and review scope

Complete proof read: agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_section.tex, SHA-256 **3fb15463d75bfa8da6167a57e2905b76f6e42a46ec7f7148b641b611d0a47a67**.

The complete carrier construction D-HOS-01–02 was reread, as was the entire author checker check_higher_symplectic_five.py. The separate independent checker in this directory imports neither the author program nor its output or arithmetic helper. Its symbolic matrices are built from the action on basis columns; its finite matrix arithmetic uses python-flint; its cyclotomic norm test uses integer circular convolution. The author program was read before the new program was written, so no claim of a blind implementation is made.

## Whole mathematical review

### D-HOS-07

All signs in the radical definition and group law check. The opposite radical acts on f+w by w+(1+B(w0,w))f, so the chosen pairing −1 produces w exactly. Conjugating central transvections then reaches every direction. The elementary induction generating the symplectic group is complete: two nonzero vectors can be connected through a vector outside two hyperplanes; the displayed radical is a product of three transvections and a central transvection; fixing the first hyperbolic plane reduces to its complement. This includes the two-dimensional base of that induction. Opposite fixed spaces have equal dimensions and intersection V^G=0, proving dim V^Q≤a/2.

### D-HOS-08

The actual central-character model gives a full matrix basis L_w and an exact, phase-free action L_w→L_gw. It remains valid when g has fixed vectors and when its prime order equals the defining characteristic. All nonidentity powers have the same fixed space because they generate the same cyclic subgroup. Thus the exact adjoint trace is q^(2n−2−r), yielding the stated square-root trace bound and Fourier multiplicity estimate.

Every nontrivial central-character isotypic space is invariant and the normalizer is Ω tensor its multiplicity operator. Rescaling Ω to order ell leaves a finite-order multiplicity operator, so eigenvalue convolution is valid. For linear characters, Sp(W) transitivity makes **all** nonzero dual weights equally frequent in the original irreducible G-module. The fixed-weight proportion is strictly below q^(−r), and every other orbit has length ell. This justifies the same bound on this entire summand, even for ell=p. The remaining trivial isotypic space is correctly given the worst possible contribution.

### D-HOS-09

The two involution estimates use the induced radical map λs|W, not simply the restriction of the natural involution. A minus-plane involution gives rank 2n−2 and support≥31a/125; a general noncentral involution, choosing a plane in the smaller eigenspace, gives rank≥4 and support≥6a/25.

For square-zero natural rank2 unipotents, the form-preservation identities for I+N and I+2N give isotropic image and skew-adjointness. Hence ker N=(im N)perp, and a fixed hyperbolic plane exists in the complement of a containing symplectic four-space. The prime5 carrier estimate then gives 8a/25.

The full normalizer reduces to GSp because q=5 is prime, n≥4 has no graph automorphism, and there is no exceptional multiplier. The perfect-cover argument correctly covers a representation killing the central sign. In the nonzero B(v,hv) case the two-plane commutator has trace 2+c²b²/μ and determinant1. The field choices produce trace1 with cube−I for square μ, or trace0 with square−I for nonsquare μ. The complex rank-commutator inequality yields exactly31a/250.

If B(v,hv) vanishes identically, polarization makes h self-adjoint, and h²=μI. Square μ reduces to the preceding involutions. Nonsquare μ yields independent v,hv spanning a totally isotropic plane; the commutator is I+N with rank N=2 and N²=0. The resulting4a/25 is stronger. These cases exhaust every compatible normalizer.

### D-HOS-10

The elementary degree floor is at least250. Tensor-factor convolution and weighted cycle-word orbits extend the support bound to all factor permutations and mixed ranks. The argument does not assume factor transitivity.

Vinroot's restated Wonenburger theorem gives inversion by an anti-symplectic involution. Since−1 is a square in F5, this action is inner, so every ordinary core character is real-valued and selfdual; its Frobenius–Schur sign is irrelevant. Irreducibility makes the tensor core's bilinear-form line unique. The normalizer similitude character must be nontrivial because the original imaginary character field embeds in the inducing character field; equality of those fields is not assumed.

Actual polarized Shapiro and pointed-curve Hurwitz factorization force genus0 and at least12 genuine branch inertias. Product one and generation force two nontrivial multiplier values, each costing at least ceil(e/2). The other ten cost at least31e/250. The exact inequality is e≤25, contradicting e≥250. This is an actual source obstruction for either determinant class, not a dimension-sufficiency claim.

## Independently executed exact certificate

Program: independent_check.py. Output: independent_checked.json. Actual result **PASS**, **0.468551252 seconds**.

- Five exact symbolic identities for a6-dimensional line radical, its group law, transvection factorization, and opposite action.
- All480 GSp2(F5) matrices; all nonzero vectors and all valid parameters in the nonzero quadratic case:19,200 commutator/power checks,9,600 for each multiplier type.
- All4,992 nonsquare self-adjoint four-dimensional vector/parameter cases: independence, actual commutator, rank2, square-zero and fifth power.
- Every nonzero symmetric2×2 quadratic phase over F5 and every nontrivial additive character:96 rank1 and400 rank2 degree25 carriers. Exact cyclotomic trace norms are125 and25 respectively, agreeing with the fixed-space formula; rank2 maximal eigenspace is9.
- Degree125 parity carriers for natural moving rank4 and6 give eigenspaces(65,60) and(63,62).
- All constants31/250,25 and250 checked as exact fractions/integers.

These finite symbolic checks supplement the universal proof; they are not substituted for it. No character-table input or unipotent trace bound is used.

## Primary source checks and exact limits

Freshly opened the complete19-page Vinroot author PDF at https://www.math.wm.edu/~vinroot/gspfactor.pdf and read Theorem1, authorp1, with its char≠2 hypothesis, the actual statement of Wonenburger[10,Theorem2], and the defining similitude convention on authorp2. Published item: C. R. Vinroot, *A factorization in GSp(V)*, Linear and Multilinear Algebra52(2004),385–403, DOI10.1080/03081080412331316079. No claim to have freshly read Wonenburger's original proof is made.

The complete Li–Xia Section2.2.2/Table2.1, authorp14, and Hiss–Husen–Magaard ordinary-cover discussionp4/complete exceptional listp35 were freshly reread in this review session. Li–Xia arXiv reopening returned a disabled-fetch error; its previously retrieved complete local author text was available and read. This retrieval failure does not change the source scope.

The actual intermediate-family factorization and supplied original character-field hypotheses are prior reviewed inputs. No new assertion is made about arbitrary selfdual source characters or inducing representations outside the stated imaginary-character-field framework.

**No mathematical defect or required repair was found.**

