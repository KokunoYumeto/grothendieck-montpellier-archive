# CX-N13: independent verification of quadratic nonresidues in explicit even extensions

Run CX_GRH. Date: 2026-11-20 UTC. Checker: `/root/koiran_gct`, GPT-6 Astra Pro; inherited effort setting not exposed. Parent `/root` proposed the explicit construction; this note independently checks its complete proof and complexity. The result is already covered by prior literature. Do not present it as a new algorithmic discovery.

## 1. Exact scope and established source

Input: an odd prime p and an explicit field F=F_p[X]/(f), where f is an irreducible polynomial of degree m, or an equivalent effective F_p-basis representation. Polynomial time means polynomial in m log p. In particular, the extension model is part of the input. It is not being constructed from the pair (p,m) by the algorithm below. For characteristic two, every nonzero element is a square and quadratic nonresidues do not exist.

Vishwas Bhargava, Gábor Ivanyos, Rajat Mittal, and Nitin Saxena, *Irreducibility and deterministic r-th root finding over finite fields*, ISSAC 2017, doi:10.1145/3087604.3087620, **Corollary 1.3, PDF p.2**: for constant r dividing gcd(m,p−1), r-th roots in F_{p^m} can be found deterministically in poly(m log p) time. The remark immediately below the corollary and §2 on the same PDF page explicitly require an irreducible polynomial defining F_{p^m}. Theorem1.2 on p2 gives the broader Stickelberger-property result; §3.1, PDF pp3–4, contains the displayed proof of Cor1.3. For r=2, Cor1.3 covers every even m and odd p.

Primary author PDF: https://www.cse.iitk.ac.in/users/nitin/papers/irred-and-rth-root.pdf . Local copy: `work/koiran_bims2017.pdf`; extracted text: `work/koiran_bims2017.txt`. Primary ECCC record: https://eccc.weizmann.ac.il/report/2017/016/ . Web retrievals `turn119189014view0` and `turn593879814view0` expose the precise statement, input remark and proof location. The source statement and its displayed corollary proof were inspected; this note does not claim a complete reproof of the paper's general r-th-root theorem.

The final manuscript should cite this established even-m theorem and give the short all-m transfer in `work/koiran_quadratic_transfer.tex`. The longer construction below is an independent verification of the quadratic case only.

## 2. Two elementary identities

For an odd finite field K of order Q and a quadratic extension L/K, define the quadratic character χ_K(a)=a^{(Q−1)/2} for nonzero a. For y in L×,

χ_L(y) = y^{(Q²−1)/2} = (y^{Q+1})^{(Q−1)/2} = χ_K(N_{L/K}(y)).

Thus y is a nonsquare in L exactly when its norm is a nonsquare in K. More generally, if L/K has odd degree r, every nonsquare a in K stays a nonsquare in L, since

χ_L(a) = χ_K(a)^{1+Q+…+Q^{r−1}} = −1.

These are direct exponent identities. They do not require a discrete logarithm algorithm, primitive-root construction, or factorization of Q−1.

## 3. The half-degree trace-zero construction

Suppose m is even and q0=p^{m/2}≡1 mod4. This includes all m divisible by 4, and also all even m when p≡1 mod4. Let K be the fixed field of y↦y^{q0} in F; it has q0 elements.

Choose x outside K and put u=x−x^{q0}. Then u≠0 and u^{q0}=−u. Consequently u² lies in K and is a nonsquare there: if u²=v² with v in K, characteristic odd implies u=±v, contradicting u outside K. Its norm is −u², which is a nonsquare because −1 is a square in K. The norm identity makes u a nonsquare in F.

Equivalently, a direct check is

u^{(q0²−1)/2} = (u^{q0−1})^{(q0+1)/2} = (−1)^{(q0+1)/2} = −1.

For the stated polynomial-basis input, the class x=X mod f has degree m and hence lies in no proper subfield, so it is a valid choice without search. For a general explicit basis, inspect its basis vectors until one is not fixed by the q0 power map. At least one exists because K is a proper F_p-subspace. Binary exponentiation uses an exponent of bit length O(m log p), so this is deterministic polynomial time.

## 4. Reduction of the remaining case to F_{p²}

The only case left is m=2r with r odd and p≡3 mod4. The fixed field E of the F_p-linear map y↦y^{p²} is the unique F_{p²} subfield. Compute its basis by solving the kernel of the matrix Frobenius²−I in the supplied F_p-basis; this is polynomial-time linear algebra. Pick y in E outside F_p and put

u=y−y^p.

Then u≠0, u^p=−u, and D=u² lies in F_p and is a nonsquare. The same factorization (u−a)(u+a)=0 proves nonsquareness of D. Thus E=F_p(u), u²=D, and this model is obtained inside the supplied field without a prime-field nonresidue oracle. (Indeed, constructing this supplied field in the first place may already encode such information; there is no contradiction with the prime-field search problem.)

It remains to construct a nonsquare b in E. It will remain nonsquare in F because [F:E]=r is odd, by the identity in §2.

## 5. Complete verification of the p≡3 mod4 trace recursion

Let v=v₂(p+1)≥2. Start with a=0. For j=1,…,v−2, replace a by either square root of a+2 in F_p. These roots exist; the argument below proves this for every possible choice of sign. Because p≡3 mod4, each square root of a known square c can be computed as c^{(p+1)/4}. The loop is empty when p=3, or whenever v=2.

At loop end set

d=a+2,
s=(d/D)^{(p+1)/4},
w=(a−2)^{(p+1)/4},
t=u s,
b=(t+w)/2.

We will prove that d is a nonsquare in F_p, a−2 is a nonzero square there, d/D is a square, t²=d, and b is a nonsquare in E.

### 5.1 Intermediate roots exist for all sign choices

For 2≤k≤v, let ζ be a primitive 2^k-th root of unity in an algebraic closure of F_p. Because p≡−1 mod2^k, its trace a=ζ+ζ^{-1} belongs to F_p. At k=2 this trace is zero, which is the algorithm's initial value.

If k<v, choose η with η²=ζ. It has order exactly 2^{k+1}. Since k+1≤v, η^p=η^{-1}, so η+η^{-1} belongs to F_p, and

(η+η^{-1})² = ζ+ζ^{-1}+2 = a+2.

Thus a+2 is a square. It is nonzero: a zero trace would imply η²=−1 and order η=4, whereas k+1≥3. If the algorithm selects the negative square root, it is the trace of −η; this element also has order 2^{k+1}, because multiplying a primitive 2^{k+1}-root by −1 multiplies its exponent by the odd integer 1+2^k. Hence the induction works with either sign at every step. After v−2 iterations, a is the trace of a primitive 2^v-root ζ.

### 5.2 The final radicands have opposite square classes

Choose η with η²=ζ, so η has order 2^{v+1}. Since v₂(p−1)=1, we have v₂(p²−1)=v+1; therefore η belongs to E=F_{p²}. Exact valuation v₂(p+1)=v gives

p≡2^v−1 mod2^{v+1},
η^p=η^{2^v−1}=−η^{-1}.

Put t0=η+η^{-1} and w0=η−η^{-1}. Then

t0^p=−t0,  w0^p=w0,
t0²=a+2,  w0²=a−2.

Both t0 and w0 are nonzero: either vanishing would force η to have order at most 4, while its order is at least 8. Thus w0 lies in F_p× and a−2 is a nonzero square. The element t0 does not lie in F_p, so its square d=a+2 is a nonsquare in F_p; otherwise the two roots of T²−d would already lie in F_p. As D is also a nonsquare, d/D is a square in F_p×. The algorithm's exponents therefore give valid square roots s and w, and t=u s has t²=d and t^p=−t.

### 5.3 The output has norm −1

Since w is in F_p and t^p=−t,

b^p=(−t+w)/2,
bb^p=(w²−t²)/4=((a−2)−(a+2))/4=−1.

This proves b≠0 and b^p=−b^{-1}. Because p≡3 mod4, −1 is a nonsquare in F_p. The norm criterion from §2 therefore makes b a nonsquare in E. Odd extension degree preserves it in F.

### 5.4 Smallest case

For p=3, v=2 and the loop is empty. Choose u²=D=2 in F_9. Then a=0, d=2, s=1, and w=1; hence b=(u+1)/2=2+2u. Directly its norm is 2=−1 in F_3, so it is a nonsquare. No special-case exception to the construction is needed.

### 5.5 Complexity

The fixed-field basis and trace-zero element use polynomial-time F_p-linear algebra and Frobenius exponentiation. The trace recursion has at most log₂(p+1) iterations. Each square root uses one exponentiation with O(log p) exponent bits, and no integer factorization is used beyond extracting the power of two from p+1. Field operations in the supplied degree-m model cost polynomially many bit operations in m log p. Hence the full even-degree algorithm is deterministic polynomial time without any RH premise.

## 6. The final all-m consequence under H_A

For even m, cite BIMS Cor1.3 and convert deterministic square-root extraction to a nonresidue by starting at −1 and repeatedly extracting a square root until Euler's criterion gives −1. The successive orders are 2,4,8,…, so at most v₂(p^m−1) iterations occur. This is an elementary output conversion, not a reproof of the cited general theorem.

For odd m, apply the already established prime-field quadratic-nonresidue search under H_A (CX-N02, r=2). Its output a remains nonsquare in F_{p^m} by the exponent identity in §2. Thus H_A suffices for quadratic nonresidue construction in every explicitly given odd-characteristic finite field. This replaces the quadratic consequence one might otherwise extract from Shoup's stronger Hecke-dependent primitive-root candidate theorem. It does not remove that theorem's Hecke premise for its broader outputs.

## 7. Checks actually performed

The complete proof above was read from start to finish by `/root/koiran_gct` after drafting. Every sign choice in the trace recursion, the exact valuation at the final step, the smallest prime, and the field-model dependence were checked algebraically. This is an independent re-proof of the already-known quadratic special case, not a formal proof-assistant check.

A finite diagnostic implemented arithmetic in F_p[u]/(u²−D), using a least nonsquare D only to construct the small test models. It tested **all 619 primes p≤10000 with p≡3 mod4**, and **all 4989 distinct terminal traces arising from every sign choice** in the recursion. It checked every intermediate radicand is a nonzero square, final d is a nonsquare, a−2 is a nonzero square, the computed norm is −1, and the output satisfies Euler's nonsquare criterion in F_{p²}. All assertions passed. This finite test is evidence of correct implementation and index conventions, not the mathematical proof. Results are in `work/koiran_quadratic_test.json`.

No claims about the larger r-th-root theorem's full proof, a generator of F×, or arbitrary extension construction are inferred from this diagnostic.


## CX-N13 extension: every specified prime r dividing p−1

**Status, 2026-11-20:** parent proposed the extension through BIMS17 Theorem1.2; this agent independently checked the reduction and supplied a direct proof for odd r. The final LaTeX fragment now contains the broader statement. Model: GPT-6 Astra Pro; effort inherited, not exposed.

Assume H_A and an explicit irreducible model F=Fp[X]/f of degree m, with specified prime r|p−1. CX-N02 gives an r-nonresidue a in Fp, hence ζ=a^((p−1)/r) of exact order r. If r does not divide m, then a^((p^m−1)/r)=ζ^(1+p+...+p^(m−1))=ζ^m≠1, because p≡1 modr.

For odd r dividing m, put Q=p^(m/r), σ(u)=u^Q, and K=F_Q. The cyclic group F* has order (Q−1)S, where S=1+Q+...+Q^(r−1), and the image of u↦u^(Q−1) has order S. Since r|S, this image contains ζ. Hence the ζ eigenspace is nonzero. It can be computed as the kernel of σ−ζ I over Fp using the given m-dimensional model; no normal-basis construction or unknown field representation is required. For nonzero u in that kernel, u^(Q−1)=ζ. With Q=1+rt and r odd,

    S=Σ(j=0,...,r−1)Q^j ≡ r+rt*r(r−1)/2 ≡ r (mod r²).

Thus S/r≡1 modr and u^((p^m−1)/r)=ζ^(S/r)=ζ≠1. Matrix computation, kernel solving, and exponentiation are polynomial in m logp. Here r≤m, while the r not dividing m branch uses the order-independent CX-N02 bound and modular powering. The final displayed bound is the stronger uniform poly(m logp). The r=2, even-m case is the known unconditional BIMS result already detailed above. These three cases prove the all-m claim for all r|p−1.

This is a full independent algebraic transfer proof, not a claim to have newly discovered the known root-extraction construction. BIMS17 Theorem1.2 supplies a second cited route when r|m: f satisfies Property1.1 because its only irreducible factor has degree m divisible by r, and ζ lies in Fp. The constant-r restriction of BIMS Cor1.3 concerns its unconditional Pila step, which is unnecessary under H_A.

The argument does not handle r|p^m−1 with r not dividing p−1. In that regime Fp has no r-nonresidue and does not contain ζ_r. The separate source audit in koiran_factoring_gate.md traces the missing cyclotomic/irreducible-polynomial input rather than assuming it away.

**Self-read:** after writing the expanded LaTeX on 2026-11-20, this agent read the complete statement and proof end to end and checked the three cases, nonzero eigenspace, exact exponent congruence, deterministic bit complexity, and supplied-model scope. No additional computational diagnostic for variable r was run or claimed.

**Final refinement and self-read:** the normal-basis existence observation was replaced by the elementary cyclic-group image criterion on the independent reviewer's suggestion. The stated bound was tightened to poly(m logp). The complete revised LaTeX proof was read again end to end; all steps pass.
