# Independent whole-proof audit of root Gaussian section

File audited: `research/gaussian_fourfold.tex`, read in full on 2026-11-21, approximately 10:52–10:56 UTC. Auditor: GPT-6 Astra Pro, /root/sixfolds, inherited effort not exposed. The audit is an independent re-derivation of the new arguments plus a full reading, not a formal proof-assistant verification. Status: **passed, with no mathematical gap found under the stated hypotheses**. The classical input HD-G01 is cited; its published theorem is not reproved here.

## HD-G02: period differential

The source has dimension six and the target dimension four. Riemann–Roch gives both twisted canonical spaces dimension two. A base point for Kη implies η^-1=O(q-p), q≠p, hence a degree-four map with two totally ramified points. Riemann–Hurwitz gives R=12, leaving at most six further branch values. The finite union of relevant Hurwitz strata has dimension at most 8−3=5; its image cannot fill M3. Thus the general exact-order-four pair has a base-point-free first pencil. The pencil trick gives kernel H0(η^-2)=0, since η² is nontrivial. Therefore the codifferential and differential have exact rank four. This proves dominance onto the particular integral-lattice component, not an uncharged identification of all principal components.

## HD-G03 and HD-G04a: support and detection

The full norm kernel has dimension9−3=6, whereas B has dimension4. The induced full-Prym type (1^4,4²) agrees with the classical cyclic formula and with complementarity with p*J(X). The finite map Sym4C→Sym4X takes the inverse canonical-system fibre to precisely the relevant W4/norm-fibre intersection. Its dimension is at most2.

The determinant pullback u*W is injective: each primitive χ-eigenspace has dimension4 and its alternating top tensor is nonzero. Products of two χ-one-forms on the same curve factor vanish because χ² is nontrivial while H²(C) has trivial character. Hence the pullback lands in H¹(C)^{⊗4}, and cup product with the product polarization kills it. Hodge–Riemann makes the real (2,2) subspace positive definite. Schoen's unramified supplier classes span that determinant summand, so one effective irreducible supplier component has nonzero pairing with u*w. Its Abel image must have dimension2; pushforward is a positive integer times the reduced image. The dimension bound makes that image an irreducible intersection component. The second projection image also has dimension2 because its pairing is nonzero. This establishes the exact point needed to use the component Bézout bound without invoking an uncontrolled inverse Lefschetz correspondence.

## HD-G04: integral degree

Independently recalculated:

- deg_(3Θ)W4=3^4·9!/5!=244944;
- deg_(3Θ)T0=3^6·6!·16=8398080;
- p†p=2(1−σ²), eigenvalues0 and4;
- Θ|B=2ξ, so p*ξ≤2Θ;
- δW≤(4/9)·244944·8398080=914248581120.

The division by9 is only conversion from degree for3Θ to degree forΘ on a surface. It never divides an integral cycle. Taking a reduced image lowers degree and preserves detection. The closedness input extends the same integer from the dominant source to its full component.

## HD-WQ: general quadratic division bound

Re-derived the formula independently. Write A=[a]*|W, q=Nm(a)^n, s=Tr_K/Q(a^(2n)), H=4q²−s²>0. If y=ReW[Y], d=<y,y> and y2=Ay, then

    G=d[[1,s/2],[s/2,q²]].

For bj=<δt,yj>, matrix inversion gives

    δHd t=(4q²b1−2s b2)y+(4b2−2s b1)y2.

All coefficients and N=δHd are integers, including when s is odd. The two coefficient dual vectors have squared norms4q²Hd and4Hd. Therefore the degree of either effective sign is at most4δq sqrt(HTd) κD. Using sqrt(d)≤RD/n! gives the stated bound; N≤δHR²D²/(n!)² follows at once. The original extra factor d in the Gram determinant genuinely cancels before assembling integral cycles. No assumption that d divides an arbitrary integer-cycle coefficient is being made. The result is a quadratic detector-to-division comparison in every dimension, with fixed endomorphism/projector data.

## HD-G05: Gaussian constants

Verified the five eigenvalues of I and S and the identity(1+I)(4−S)=16eW. The positive part4Y+4I*Y and negative partS*Y+(IS)*Y both have degree≤8D. Hence d≤64D². The operator[2+i]* has eigenvalues−7±24i, giving

    G=d[[1,−7],[−7,625]], det(G/d)=576.

Its exact formula is

    576δd t=(625b1+7b2)y+(7b1+b2)y2.

The dual vector norms are600sqrt(d) and24sqrt(d). Consequently N≤36864δD² and each sign has degree≤76800δsqrt(T)D². Replacing sqrt(T) by ceil(sqrt(T)) produces the displayed integer constant. This passes independently of the general formula HD-WQ, and improves its Gaussian specialization by using the smaller integral matrix determinant.

## Qualifications retained

- The determinant/polarization/lattice component matters. The extension to both maximal-order principal Gaussian components needs the even/odd lattice argument SF-05 and costs a factor4 in detector degree for fourfolds.
- Theorem W supplies orthogonality, comass and integral endomorphism-projector machinery; those were used as authorized inputs, not silently reproved or generalized beyond their setting.
- The supplier input is only Schoen's unramified construction; no ramified-case repair or unrefereed 2026 source enters.
- This audit does not certify a LaTeX build or publication-source locators that were not independently opened by the auditor. Schoen1988 pp12–13,24–25 and Lange–Ortega§4 p6 were directly read; Mumford's locator is carried from root's source check.


## HD-G06 addendum: complete independent check, 2026-11-21 11:03 UTC

Read the entire inserted proposition and proof after the first audit. The statement passes for integral maximal-order Gaussian action. The primitive homology description is saturated, not merely a finite-index collection of cycles: cut the base into a one-holed torus carrying the cyclic monodromy and a genus-two one-boundary surface. The latter lifts to four disjoint copies. The former lifts to a genus-one surface with four boundary circles; after those circles are glued away, its remaining rank-two homology is deck-invariant. Mayer–Vietoris therefore identifies all anti-invariant homology with the differences of the unaffected handle cycles displayed in HD-G06. Their Jacobian intersection form is twice symplectic, and the half-polarization has the claimed even Hermitian blocks.

For the classification, principal polarization gives a unimodular Hermitian matrix because the determinant of its underlying integral alternating form is the square of the Hermitian determinant. The signature fixes that determinant to +1. Rational splitness, primitive isotropic splitting, reduction of k modulo 2, and the explicit mixed-parity change of basis are valid. The complementary rank-two lattice has determinant −1 and signature (1,1), so its rational splitness is justified. I independently multiplied both displayed S identities. Their two-block determinant has norm16, agreeing with the degree16 of a fourfold isogeny whose pullback polarization is twice principal. The transported complex structure remains positive and belongs to the even-type period domain. Detector degree on an effective surface grows by exactly at most2², and detection is preserved by the rational K-isogeny. Hence D0=3656994324480 is valid on both maximal-order principal types.

The identical induction works in rank six, signature(3,3): the principal even source is U³, the other type is I3,3, the three-block similitude has degree64 and threefold degree factor8. It yields the sixfold principal bound975950559600810393600 established in SF-05. No claim is made here for nonmaximal-order integral actions.


## HD-CM6 / HD-CM4 — complete independent audit, 2026-11-21 12:15 UTC

I read the entire current `research/cm_lattice_transfer.tex`, and the complete HD-COMP proof on which its fourfold corollary relies. This is a whole-proof independent check, including both conductor paragraphs. Outcome: **PASS**, within the explicitly stated split-sixfold and authorized Perry-preprint scope.

The normalized form h(v,w)=E(v,tau w)−bar(tau)E(v,w) has E as its tau coefficient. For a rank-one Hermitian block (a), the underlying alternating form on (v,tau v) is [[0,a],[-a,0]], so no different/discriminant factor is missing. The source first-factor K-basis has lattice (Z+(u/d)Z)^6. Its Hermitian matrix is [[0,kI],[-kI,0]], k=3du/f_s integral because f_s divides d. F=diag(I,kI) gives F*U³F=H_s, and dF sends both raw-lattice summands integrally into O_K^6. The polarization pullback is d²h and the three-cycle degree cost is d^6. Independently, the isogeny degree is (d²)^6 chi(h)=729d^15.

For a split maximal-order target, a saturated isotropic rank-three submodule is a direct summand over the class-number-one PID; a basis extends. The block matrix has Norm(det B)=Delta. For C'=(B*)^-1 C B^-1, both C' and B^-1 have denominators dividing Delta, so T=[[I,-C'/2],[0,B^-1]] and its inverse have denominators dividing 2Delta. This algebra does not require Euclidean division. Multiplying T by 2Delta gives the target isogeny and costs (2Delta)^6 on three-cycles. The product is (2dDelta)^6 D_CM, hence 2^324 d^57 Delta^6.

For the smaller order, Lambda'=f_t O_K Lambda lies between f_t Lambda and Lambda, with index at most f_t^12. The induced isogeny's pulled-back polarization product is I Delta, and pushforward preserves the cycle degree relative to that pullback. This proves the f_t^72 exponent. The fourfold compensation gives Delta² and therefore Delta^12; using a rank-eight integral lattice for its conductor gives f_t^96. HD-COMP's contraction is valid: the off-diagonal graph combinations span W_K(T), and contracting against those combinations isolates a nonzero W_K(A) component. The nef divisor bounds and general translations supply an effective integral detecting cycle with the claimed factor c_K.

Audited file SHA-256: d388a25f8bf4c504547dd54aa3cedcc62c469b47b3a169cbe576320b3f8327dc
