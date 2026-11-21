# Masullo trace comparison — checked research note

Run: TRACE_DET, 2026-11-21 (Europe/Berlin). Agent: `/root/masullo_trace`, GPT-6 Astra Pro; reasoning-effort setting is not exposed in the agent context. These notes distinguish assertions of the supplied draft from deductions checked in this run. No 940-page proof audit, external publication authentication, or formal verification is claimed.

## 1. The actual Hilbert-space setup

Let F be a number field, C_F=A_F^×/F^×, C_F^1=ker|·|_F, and dµ a Haar measure. Write S_0(A_F)={f∈S(A_F):f(0)=f̂(0)=0}, and Θ_f(g)=Σ_{ξ∈F^×}f(ξg). The draft calls the image of Θ, equipped initially with the quotient topology, H_{0,cont}(F^×,S_0(A_F)); this is not étale H^0 or a motive.

For I=[−α,α], α≥0, and s≥0 put

    w_{I,s}(g)=max(|g|_F^{−2α},|g|_F^{2α})(1+|log|g|_F|²)^{s/2},
    W_I^s(C_F)=completion of S_E(C_F) for (∫|f|²w_{I,s}dµ)^{1/2},
    V_{a,I}^s=closure of |·|_F^a H_{0,cont}(F^×,S_0(A_F)) in W_I^s,
    E_{F,a,I}^s=W_I^s(C_F)/V_{a,I}^s.

This last space is the draft's H_{F,a,I}^s. Both its ambient space and its quotient are Hilbert spaces. A compactly supported smooth test function φ∈D(C_F) acts by

    A(φ)f(x)=∫_{C_F}φ(g)f(g^{−1}x)dµ(g),

and descends to E because V is invariant. Exact locators: §1.1.3, pp.11–12; §1.8.2.2, p.43 (S_0 and θ); Definition 10.1.1.1(1), Eq.(10.1.1.3), p.434; Eq.(10.2.2.1), p.445; Definition 9.3.1.1/Eq.(9.3.1.2) for convolution, recalled explicitly on pp.442 and 455.

The spectral functionals have the form

    η_{χ,t,b,m}(g)=χ(g)|g|_F^{b+it}(log|g|_F)^m,

for zeros c=χ|·|_F^{a+b+it}. Theorem 10.2.2.1, Eqs.(10.2.2.4)–(10.2.2.6), p.446, supplies a Markushevich basis; the orbital Schauder bases appear instead in Chapter 7. These basis names should not be conflated.

## 2. Spectral nuclearity: a real cote-1 application

**Draft assertion MAS-SRC-01.** Theorem 10.3.2.1 (Spectral Nuclearity II), pp.453–455, for s>1 and I=[−α,α], asserts convergence of the finite-rank spectral expansions in every Schatten S_p, p≥1 (part (1), Eq.(10.3.2.1)), and that A(φ)∈S_1(E_{F,a,I}^s), continuously in the test function (part (2), Eq.(10.3.2.2)). Its claimed trace is

    Tr A(φ)=Σ_{χ,t,b} N_{I,s}(χ|·|^{a+b+it}) Mφ(χ|·|^{b+it}),
    Mφ(c)=∫_{C_F}φ(g)c(g)dµ(g),

where the sum is over zeros in the closed strip a+I; multiplicity is full in its interior and Sobolev-truncated on the boundary. This is Eq.(10.3.2.3), p.454. Part (3), Eq.(10.3.2.5), is the character-isotype version. Theorem 10.3.1.1, pp.448–453, handles I={0} separately.

**Finding MAS-01 (conditional identification of the abstract trace theorem).** Conditional on MAS-SRC-01, cote 1's trace-class trace and Fredholm determinant theorems apply to each of these A(φ). In particular

    D_φ(w)=det_E(1−wA(φ)),
    D_φ(w)=∏_j(1−wλ_j(A(φ))),
    Tr A(φ)=Σ_jλ_j(A(φ)),
    log D_φ(w)=−Σ_{n≥1}(w^n/n)Tr(A(φ)^n)

for |w|<1/||A(φ)|| in the logarithmic formula (the zero operator is harmless). Algebraic eigenvalue multiplicities are meant. Also A(φ)^n=A(φ^{*n}), because the quotient inherits the convolution-algebra action.

Proof. The theorem's space is a Hilbert quotient by a closed subspace and its explicitly asserted Schatten class is S_1, exactly the hypotheses of the cote-1 result; no upgrade from an unspecified locally convex trace is required. The three standard identities are the trace-class theorem applied to this operator, and the last equality follows by the convolution law and invariance of V. This is an application of the known theorem, not a new proof of it. For the source theorem use cote 1 scans 79–80, Theorem 2 and Corollary 1, formulas (20)–(23), and scans 111–112 for the genus-zero argument; the source includes deleted working text, which must be described as such. Proof checked by rereading the entire deduction and matching the hypotheses to MAS-SRC-01.

The new arithmetic content of Masullo is the identification of the geometric/orbital side and, as intended in the introduction, its independence of arbitrarily narrow positive-width strips. Abstract trace=eigenvalue sum cannot itself establish that arithmetic identification.

**Finding MAS-02 (not a fixed Xi determinant).** No nonconstant entire function D(w) can be D_φ(w) for every allowed test function φ. Proof: 0 is an allowed test function, A(0)=0 and D_0(w)=1. More generally A(tφ)=tA(φ), so D_{tφ}(w)=D_φ(tw). Thus the supplied trace family is not an identification of a single, test-function-independent operator B whose determinant is Xi(√w)/Xi(0). A particular operator could only be identified with B after a separate spectral/intertwining theorem. This finding refutes the universal identification, not the logical possibility of a specially chosen additional construction. Full proof reread and checked.

## 3. The draft's main arithmetic trace formula

**Draft assertion MAS-SRC-02.** Theorem 12.5.1.1 (Trace Formula), pp.519–520, is explicitly called the main theorem. It assumes φ∈D(C_F) and φ|_{C_F^1}=0. Put

    a_v=1/2                 for real v,
    a_v=1/(2π)              for complex v,
    a_v=log(q_v)/µ_v(O_v^×) for finite v,

with the local measures and principal-value regularizations of the draft. Its Eqs.(12.5.1.1)–(12.5.1.3) read

    Σ_v a_v ∫'_{F_v^×} φ(g_v)|g_v|_v^{1/2}/|1−g_v|_v dµ_v(g_v)
      = Mφ(|·|_F^{1/2})+Mφ(|·|_F^{−1/2})
        −Σ_{c,I} N(c) Mφ(c|·|_F^{−1/2}).                         (M12)

At the archimedean places the denominator is printed as |1−g_v|; retain the draft's own normalized absolute-value convention. The local group embeds into the idele class group when evaluating φ. The sum runs over zeros of the completed Hecke L-function c↦L(c) whose real exponent σ(c) belongs to the interior of 1/2+I, and N(c) is full zero multiplicity. The main theorem as printed does not quantify I. Its intended range I=[−α,α], α>0 arbitrary, is explained in §§1.2.1 and 1.4.5–1.4.8, pp.13–15 and 29–31. Preserve this distinction; do not silently repair the theorem.

The geometric operator is a cutoff convolution/projection operator at a=1/2. Definitions 10.4.1.1 and 10.4.1.3, pp.456–457, give the orthogonal projectors P_geom onto V and P_spec=1−P_geom, and P_{ρ,a}^{geom}=M_ρP_geom. The main calculation takes Tr(P_{ρ,1/2}^{geom}A(φ)) as Λ→∞, εΛ=o(1). Definition 10.4.3.7, Eqs.(10.4.3.49)–(10.4.3.50), pp.473–474, writes k_geom(x,y)=φ(xy^{−1})−k_spec(x,y). The trace on the spectral quotient is an ordinary S_1 trace under MAS-SRC-01. The geometric operator before cutoff need not be trace class; its limiting diagonal trace is additional structure, not automatically the trace of an arbitrary untruncated operator. Source §10.4.1, p.456, explicitly says the untruncated convolution and its geometric restriction are otherwise non-nuclear.

**Draft assertion MAS-SRC-03 (different formulation, not interchangeable).** Theorem 13.3.1.1, p.522, instead sums only over σ(c)=1/2, replaces N(c) by N_spec(c)=min{N(c),[F:Q]}, and assumes the first [F:Q] Mellin jets at the indicated central character parameter vanish, Eq.(13.3.1.2). It labels the resulting test space A. Its main trace display is Eqs.(13.3.1.3)–(13.3.1.5). The page has a footnote requesting correction of the statement, and Theorem 13.3.1.2 has a heading but no mathematical statement or proof, with insertion instructions. Therefore cite Theorem 12.5.1.1 as the stated main trace theorem, record 13.3.1.1 separately, and attribute the GRH consequence to the draft's programme/introductory deduction (§1.4.5), conditionally. Do not claim a verified finished numbered 13.3.1.2 GRH theorem. These observations were checked visually against rendered PDF pages 519 and 522, not only text extraction.

## 4. Exact positivity distinctions

### MAS-03: the main test class excludes nonzero convolution squares

For the centered normalization put ψ*(g)=overline{ψ(g^{−1})}. Since C_F is abelian it is unimodular, and for ψ∈D(C_F),

    (ψ*ψ*)(1)=∫_{C_F}|ψ(g)|²dµ(g).

Consequently ψ*ψ* vanishes on C_F^1 only when ψ=0. Proof: 1∈C_F^1, so the required vanishing implies the nonnegative L² norm is zero; continuity of ψ then makes it identically zero. Conversely ψ=0 is immediate. All integrals are finite by compact support. This is a full proof, reread and checked.

It follows that (M12) cannot be directly evaluated on a nonzero Weil-positive convolution-square test. The draft expressly agrees: §1.4.6, p.30, says Weil positivity is not addressed or used, and that removing the vanishing condition is only an a posteriori consequence after obtaining GRH and returning to Weil's explicit formula. This is not a claim that no argument using (M12) could ever imply positivity; the point is that a separate deduction is required.

### MAS-04: positivity of the scalar Weil functional under RH/GRH

Let Z be the set of distinct zeros of the relevant completed L-function, with multiplicities N(c), and η_c=c|·|_F^{−1/2}. Define the centered spectral Weil functional

    W(φ)=Σ_{c∈Z} N(c)Mφ(η_c).

Under GRH each η_c is unitary. For a test ψ in a class where the usual explicit formula gives absolute convergence (in particular a fixed smooth character isotype),

    W(ψ*ψ*)=Σ_{c∈Z}N(c)|Mψ(η_c)|²≥0.                         (P)

Proof. Fubini and Haar invariance give M(ψ*ψ*)(η)=Mψ(η)Mψ*(η). Inversion gives Mψ*(η)=overline{Mψ(overline{η}^{−1})}. If η is unitary, overline{η}^{−1}=η, yielding the summand in (P); absolute convergence permits the sum. In a fixed character component convergence follows from rapid vertical decay of the Mellin transform of a smooth compactly supported test function and the usual O(T log T) zero count. This argument is an elementary consequence of the cited zero-count/explicit-formula background, not an independent proof of those results. Full argument reread and checked.

For F=Q and Riemann/Dirichlet L-functions the stipulated Alpöge theorem supplies the required RH/GRH. The corresponding claim for every Hecke L-function over every number field remains conditional on the stated Masullo GRH claim unless another cited theorem is supplied. In uncentered Weil notation the local side has the opposite sign after annihilating pole terms: positivity of the spectral functional becomes negativity of the local distribution sum. Attached Connes–Consani, Appendix C, Proposition C.1 (source label `mainprop`; the theorem counter is section-numbered after the introduction), states precisely this criterion for ζ. Its Appendix A (label `appenmellinapp`) gives the half-twist and involution conversion.

### MAS-05: scalar/spectral positivity does not establish positivity in the weighted quotient metric

Even if a trace-class operator has nonnegative real eigenvalues and all its positive integer power traces are nonnegative, the operator need not be positive. Counterexample on C² with its usual Hermitian metric:

    T=[[1,1],[0,2]],   T*=[[1,0],[1,2]].

T≠T*, while Tr(T^n)=1+2^n>0 for n≥1 and its eigenvalues are 1,2. Hence it is not positive. This verifies the claimed failure in finite dimension, already a trace-class setting. Full proof checked directly.

In Masullo the continuous translation representation on W_I^s is expressly nonunitary (Remark 10.4.1.4, p.457). Therefore the formal identity A(ψ*ψ*)=A(ψ)A(ψ*) does not automatically equal A(ψ)A(ψ)^†. The preceding counterexample does not prove a particular draft operator is nonpositive; it proves the spectral evidence alone is insufficient. Under the stipulated RH one can form the separate diagonal zero-space model where the operator with eigenvalues |Mψ(η_c)|² is positive, but a unitary identification with the draft's weighted quotient is additional information.

### Three distinct statements

1. Cote 1: trace=eigenvalue sum and determinant product for a trace-class Hilbert operator, with no selfadjointness or positivity hypothesis. Its coefficient bound compares an arbitrary operator with the positive singular-value operator |u|. It does not say u≥0.
2. Weil: positivity of a quadratic scalar distribution on all admissible convolution squares; under RH this becomes a sum of absolute squares.
3. Masullo: conditional trace-class spectral formulas plus an arithmetic geometric-side calculation on a vanishing test class; it claims a route to GRH without using the Weil-positive cone. Its RH consequence then supplies scalar Weil positivity a posteriori. It is not a claimed direct proof that the quotient operator A(φ) is positive for arbitrary φ.

## 5. Boundary multiplicity: a concrete qualification, and a safe way to avoid it

**Finding MAS-BOUND (direct norm calculation).** After choosing a section C_F≃C_F^1×R via u=log|g|_F, a boundary evaluation functional with kernel χ(g)|g|_F^{b+it}(log|g|_F)^m is continuous on W_I^s exactly when its kernel has finite weighted-dual L² norm. Apart from the finite Haar volume of C_F^1, that squared norm is

    ∫_R exp(2bu−2α|u|)|u|^{2m}(1+u²)^{−s/2}du.

For |b|<α this is finite for every nonnegative integer m. For |b|>α it is infinite. For b=±α it is finite exactly when 2m<s−1 (including α=0, where both tails have this condition). Proof: on each tail take the explicit exponential factor. A nonzero positive exponent forces divergence, strictly negative exponents dominate every polynomial, and at the zero exponent the integrand is comparable to |u|^{2m−s}; the p-integral converges exactly if 2m−s<−1. Near u=0 the integrand is locally integrable for m≥0. These cover all cases and prove the equivalence. Full proof reread and checked.

Thus at the boundary the number of allowable derivative orders, for s≥0, is min{N,max(0,ceil((s−1)/2))}, not min{N,floor((s−1)/2)+1} when (s−1)/2 is an integer. For the theorem's stated s>1 the maximum with zero can be omitted. The latter expression is the printed Eq.(10.3.2.4). At s=3,m=1 its proposed endpoint has a logarithmically divergent norm. This identifies an endpoint correction required by the displayed norm, not an audit of the full theorem or an assertion that every zero has multiplicity sufficient to encounter the endpoint. Explicitly, at s=2r+1 with r≥1 the effective caps differ only if N≥r+1; for a simple zero at s=3 they coincide, and no erroneous extra mode is activated.

A direct discontinuity witness avoids relying on the draft's duality theorem. Take b=α>0, t=0, χ=1, s=3 and, for large R, smooth cutoffs κ_R supported in [1,2R], equal to 1 on [2,R], with values in [0,1]. On the logarithmic coordinate set f_R(u)=κ_R(u)e^{−αu}u(1+u²)^{−3/2}. These are smooth compactly supported tests. Their squared weighted norms and their images under the order-one boundary functional are, respectively,

    ||f_R||²=∫κ_R(u)²u²(1+u²)^{−3/2}du,
    L(f_R)=∫κ_R(u)u²(1+u²)^{−3/2}du.

Both are asymptotic to log R up to bounded terms if the cutoffs are taken with fixed transition near 1 and a rescaled transition on [R,2R]. Therefore |L(f_R)|/||f_R|| grows like √log R, so L is not continuous. This whole witness was independently recomputed after the weighted-dual proof. The source's squared-weight convention was checked visually on PDF p.417, Eqs.(9.2.2.34), (9.2.2.40), (9.2.2.41), and the printed multiplicity formula visually on p.454. Theorem 10.3.2.1 on p.453 permits real s>1 without excluding odd integers; although some earlier Paley–Wiener statements use even integers, that restriction is not part of this theorem's stated hypotheses.

For the present comparison one may choose the two strip edges to avoid the zero set of the relevant fixed L-function (countability suffices); then no boundary modes occur and the entire complication disappears. Alternatively choose s>1 away from odd integers. Do not silently replace the printed formula in a quotation of the draft.

## 6. Relation to Grothendieck's frameworks

The arithmetic base is Spec O_F and its places, but the actual category here is weighted Hilbert spaces and nuclear locally convex spaces built from adeles. The divisor exact sequence in §1.2.1, p.13, is explicitly compared in the draft with 0→O_X(−D)→O_X→O_D→0 on the Stein complex line X=C. This is an analytic divisor model, not construction of a constructible ℓ-adic sheaf or a cohomology theory of Spec Z. Orbital subquotients and continuous homology notation cannot, without an extra realization theorem, be identified with an H¹ motive, a crystal, or the cohomology conjectured by Deninger.

The relevant exact archive locator is cote 1 scans 79–80 (trace and determinant) with 111–112 (genus-zero proof). SGA 5's Lefschetz formalism supplies the analogy between local orbital contributions and geometric traces, but the draft does not construct an SGA 5 étale correspondence to which that theorem applies. No EGA/FGA or crystal locator should be invented for an analytic construction. §1.5.1, pp.32–33, states the draft's relation to Connes and Meyer; §1.5.2, p.33, claims realization of the local orbital trace patterns contemplated by Deninger, but does not state construction of Deninger's full cohomology, functoriality, cup products, duality, or polarization.

## 7. Checked source and proof record

The text extraction was checked against visible rendered pages for the main formulas and Chapter 13 qualifications. All six new deductions/counterexamples above were reread in their entirety after writing their proofs. Source theorems remain cited conditional assertions, not independently reproved. The exact check events are in `work/masullo_events.tsv`.
