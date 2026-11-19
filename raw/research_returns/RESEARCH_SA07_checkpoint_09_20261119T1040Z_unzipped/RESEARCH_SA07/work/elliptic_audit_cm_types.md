# Independent audit of E.2.20: eliminating the common local sign

Auditor: OpenAI GPT-6 Astra, elliptic_splitting agent, inherited effort. Date:19November2026. This audit concerns the stated concrete integral abelian diagram and its already established common-scalar property. It does not assert the unresolved full-pure comparison or place-separation conclusion.

## 1. Exact input

Let σ fix Qcm pointwise. Suppose the given integral Betti transport has, for every abelian variety A/Qbar, completion

\[
 \widehat T_A=\lambda\rho_A(\sigma),\qquad
 \lambda\in\prod_p\{1,-1\}\subset\widehat{\mathbb Z}^{\times},
\]

with one common λ, as established in the parent proof. The maps intertwine all labelled endomorphisms, including rational ones after multiplication by an integer. The audited conclusion is λ=1 or λ=−1 as a global scalar.

## 2. Primary sources opened independently

Milne, *Complex Multiplication*,14July2020,108pp, https://www.jmilne.org/math/CourseNotes/CM.pdf, was opened anew (turn818775477view0). Exact passages: Proposition1.23 p16 and Proposition1.26 p17 (turn830608733view0/1); Theorem9.10 p78 (turn830608733view2); Example2.11 p26, Proposition3.6(c)p28 and Corollary7.10 p54 (turn349299575view0/1/2). The existing local primary PDF `work/sources_generation/milne_cm2020.pdf` was also read; the norm pages were independently extracted to `work/sources_elliptic/milne_cm_norms.txt`.

Milne, *Class Field Theory*,v4.03,6August2020, https://www.jmilne.org/math/CourseNotes/CFT.pdf, was opened in full (turn481450726view0). PropositionV.5.2 and its norm diagram, p178, TheoremV.5.3 p179, and the rational cyclotomic description, LemmaV.5.9/SummaryV.5.10 pp180–181, were read (turn141097007view0/1). These supply precisely norm functoriality, triviality on full principal ideles, and the action of unit ideles on cyclotomic fields.

## 3. One idele and all CM types

Fix m, let F=Q(ζ_m+ζ_m^{-1}), and put L=F(i). The field L is finite abelian Galois over Q, is CM, and its complex conjugation c has fixed field F. In particular σ fixes L. Choose a finite idele s of L representing σ on L^ab. Finite ideles suffice because L has only complex infinite places, whose connected multiplicative groups have trivial Artin image.

For a CM type Φ of L, write E_Φ* for its reflex field. It is a subfield of L: every automorphism fixing L fixes Φ, so the stabilizer definition of the reflex field gives this inclusion. Set

\[
 s_\Phi=\operatorname{Nm}_{L/E_\Phi^*}(s).
\]

Norm reciprocity gives Art_(E_Φ*)(s_Φ)=σ restricted to(E_Φ*)^ab. Indeed, L/E_Φ* is abelian because L/Q is abelian, so L lies in(E_Φ*)^ab. The finite-extension norm diagrams of CFT PropositionV.5.2, applied to the finite subextensions containing L and then passed to the inverse limit, give exactly this restriction identity.

The CM theorem9.10 supplies the L-linear quasi-isogeny α_Φ:A_Φ→σA_Φ satisfying

\[
 \widehat\alpha_\Phi\,N_\Phi(s_\Phi)=\rho_{A_\Phi}(\sigma).
\]

Proposition1.23 gives the composition identity

\[
 N_\Phi(s_\Phi)=N_{L,\Phi}(s)
          =\prod_{\varphi\in\Phi}\varphi^{-1}(s).       \tag{1}
\]

The last formula is valid on finite ideles, not just on fractional ideals. The reflex norm is defined in p16 as a determinant, functorially for every Q-algebra R. When the auxiliary field is the Galois field L itself, its summands have determinant φ^{-1}; taking their product proves(1) as an equality of algebraic-torus maps, hence on A_f-points. This avoids transferring an ideal equality to ideles without justification.

Every CM type used here is realized: Example2.11 constructs the polarized torus C^Φ/Φ(O_L), and Corollary7.10 gives its algebraic model over Qbar, with the labelled L-action. Primitivity is unnecessary. Even for an imprimitive type,

\[
 H_1(A_\Phi,\mathbb Q)\simeq L
\]

as an L-module; equivalently it is free of rank one, also stated in Proposition3.6(c).

Both T_Φ and α_Φ intertwine the same labelled L-action on their source and target. Therefore α_Φ^{-1}T_Φ is an L-linear rational automorphism of this rank-one module. Its endomorphism algebra is canonically L, so

\[
 q_\Phi:=\lambda N_{L,\Phi}(s)\in L^\times.           \tag{2}
\]

This does not require T_Φ to be a Hodge isomorphism. It requires exactly the labelled endomorphism naturality already included in the diagram.

## 4. Comparing two types is legitimate

Choose Φ containing the identity embedding and replace that embedding by c, keeping every other choice unchanged. This is again a CM type Ψ. Both equations(2) are statements in the same canonically labelled field L and use the same idele s and common λ. No isomorphism between A_Φ and A_Ψ, and no further coherence between their quasi-isogenies, is needed to divide them. Formula(1) gives

\[
 r:=\frac{s}{c(s)}=\frac{q_\Phi}{q_\Psi}\in L^\times,
 \qquad r\,c(r)=1.                                \tag{3}
\]

The norm-one identity holds first as an idele identity and then in L because the diagonal embedding is injective.

There is an explicit Hilbert90 solution. If r≠−1, take b=1+r; then b/c(b)=r. If r=−1, take b=i. Consequently

\[
 t=s/b\quad\text{satisfies}\quad c(t)=t.
\]

The fixed finite ideles are exactly A_(f,F)^×. This can be seen locally: at a split place the two components must agree, and at a nonsplit place the fixed local field is F_v. The unit condition outside finitely many places is preserved. Thus t is an actual finite idele of F.

## 5. The rational norm and the global sign

The elements φ^{-1}, for φ in a CM type, restrict to every embedding of F exactly once. This follows because c is central and Φ selects one member from each conjugate pair in Gal(L/Q). Since t is fixed by c,

\[
 N_{L,\Phi}(t)=\operatorname{Nm}_{F/\mathbb Q}(t)=u
          \in\mathbb A_{f,\mathbb Q}^{\times}.       \tag{4}
\]

Divide(2) by N_(L,Φ)(b), which belongs to L×. Then λu belongs both to diagonal L× and to the scalar finite ideles of Q. Their intersection is Q×: every Gal(L/Q) element fixes the scalar idele, so it fixes the diagonal element of L; injectivity of the diagonal embedding then places that element in Q. Write λu=a∈Q×. Since λ²=1,

\[
 u=a\lambda.                                      \tag{5}
\]

By norm reciprocity, Art_Q(u) fixes F. The finite principal idele a has Artin image1 when a>0 and complex conjugation when a<0: combine it with its infinite component to form the full principal idele, which has trivial Artin image, and use the real local reciprocity map. Both actions fix the totally real field F. Equation(5) therefore implies that Art_Q(λ) fixes F.

This holds for every m. The explicit cyclotomic description of reciprocity gives

\[
 \lambda\bmod m\in\{1,-1\}\subset(\mathbb Z/m\mathbb Z)^\times
       \quad\text{for every }m.
\]

Inverting the reciprocity convention does not change this statement because λ²=1. The closed subset{1,−1} of Zhat× is the inverse limit intersection of these inverse images. Equivalently, distinct local signs at two odd primes are detected modulo their product; a distinct sign at2 is detected modulo4 times an odd prime. Hence all local signs agree, proving the audited conclusion.

## 6. Verdict and scope

**Audit passes.** The reflex-norm composition, labelled L-linearity, imprimitive-type existence, comparison of different CM types, Hilbert90 descent, scalar-idele intersection and reciprocal-sign convention have all been checked. No hidden compatibility between different CM-type varieties is needed beyond the common λ from the original integral diagram. This proves the parent result E.2.20 at its stated level; it does not construct the remaining integral comparisons for a nontrivial Galois element or settle the full pure/place-separation question.
