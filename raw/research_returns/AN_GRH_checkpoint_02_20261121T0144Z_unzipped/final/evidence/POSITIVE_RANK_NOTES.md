# Positive-rank theta follow-up

## Findings ready for integration

- **A07:** The prime-order incidence bridge fails over arbitrary finitely generated fields of characteristic two even in each positive-rank genus-two stratum. The proof is a direct consequence of the published Ozman–Pries Theorem 1.1(2), p. 456 / Theorem 8.3, p. 473, with finite-coefficient descent. It does not give a finite-field counterexample.
- **A09:** An exact rank-one finite-field witness, with a new direct principal-divisor identity and two independent arithmetic verifications. The curve is recovered row **A1 B.39**, working identifier **B.LIT7**. The new proof uses a point over F16 and a Kummer equation, not an unverified repetition of its F64 Lang-cover calculation.
- **A10:** Every nonordinary genus-two curve in characteristic two has no nonzero 3-torsion point on its Raynaud theta divisor. This includes rank one, extending the rank-zero scope of the recovered cubic-cover observation.
- **A11:** Prime-power incidence is enough: n = ell^r, exact-order-n point on theta, and <2,-1> = (Z/n)^× imply a primitive-zero relative degree-ell Prym and the collision-pencil contradiction. The full revised proof passed the effective_galois agent's independent review.

**A08** remains in the separate file `work/effective_galois/finite_prime_avoidance.tex`. I read its entire proof independently and passed it; its event is included here. It excludes a uniform finite prime list for finite-field curves of either positive rank, with the curve allowed to vary with the list.

## Concrete certificate

For C: Y²+X²Y = X⁵+X and P = infinity, use

    k = F2[u,v]/(u²+u+1, v²+u²v+1) = F16,
    R = (u,v),
    A(X) = u(v+1)(X⁶+X³) + u²v X⁵ + u X⁴
           + (uv+1) X² + u X + u²,
    B(X) = X⁴ + u X³ + X + 1.

The identity

    A² + X²AB + (X⁵+X)B² = (X+u)^13

and the evaluations F(R)=0, F(iota R)=u for F=A+BY prove div(F)=13(R-P). All pole/zero and exact-order arguments are in the LaTeX proof. The cover W^13=F is a geometrically connected pointed mu13-torsor over F16; after extension to F4096 the deck group is constant cyclic13. This construction is not asserted to equal the recovered F64 arithmetic model.

The producer `theta13_direct.py` uses finite-field arithmetic and Taylor linear algebra. The verifier `verify_theta13_norm.py` uses SymPy polynomial reduction over F2 and does not import the producer. Both final runs passed; their JSON outputs contain all coefficients and check results. Draft assertion and backend failures, and their corrections, are recorded in the event ledger rather than omitted.

The small counts C(F2)=C(F4)=4 yield H2(U)=U⁴+U³+2U+4 and #J(F2)=8. Thus all four F2-points have identical prime-to-two abelian Kummer classes, whereas A09+A11 separate their full point-section classes. Root is running a separate exact count check.

## Strongest attempted generalization

Poonen Theorem 1.8 applies because the genus-two theta support is a translating Abel curve generating J. It allows a prescribed ell-power primary component and zero at every other prime in a density-one set S containing any initial finite set. Hence a theta point can be obtained with order ell^r m, where every prime of m is outside S. This proves infinitely many odd-order theta points, including for ordinary split Jacobians, but does not make m=1.

The extra factor is sometimes forced: choose ell=3,r=1 on a nonordinary genus-two curve. A10 excludes exact order3, so every theta point supplied with that prescribed component must have m>1.

Two attempted removals were checked. Multiplication by m moves the point to [m](Theta), which need not be Theta. Passing to the intermediate cyclic-m cover leaves relative characters of all conductors ell*d for d|m, not only the primitive ell*m block. A zero Frobenius arrow on one original line does not annihilate these other blocks. Even <2,-1> = U_(ell*m) only controls the primitive block. When n has at least two prime factors, lcm of all proper divisors is n, so no nonidentity deck element acts only on that primitive part. For prime powers the lcm is n/ell; that is exactly the useful A11 case.

## Source scope and exact locators

1. **Ozman–Pries 2019:** Asian J. Math. 23(3), 455–478, DOI 10.4310/AJM.2019.v23.n3.a5. Use Theorem 1.1(2), p456 / Theorem 8.3, p473. Primary URL: https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0003/AJM-2019-0023-0003-a005.pdf . Web refs `turn492954356view0`, `turn810328930view1`.
2. **Yang 2021:** Journal of Algebra 587, 263–294, DOI 10.1016/j.jalgebra.2021.07.032. Primary author PDF: https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/RTOC.pdf . Theorem1.1 quotes Nakajima Proposition4 for every prime-to-p cyclic degree on the generic curve. Theorem3.5 itself gives the all-degree new-ordinarity statement: the unpointed étale case has ramification divisor D=0, automatically Frobenius stable by Definition3.3/Lemma3.2. This defeats A11's incidence condition on a generic ordinary curve. For a generic rank-one stratum, §3.6.2 / Corollary3.6 remain prime-degree only. Web refs `turn705827939view1`, `turn703148011view0`.
3. **Poonen 2005:** IMRN2005 no24, 1487–1498, Theorem1.8. Primary author PDF: https://math.mit.edu/~poonen/papers/multiples.pdf . Web ref `turn209835672view1`.
4. **Pop–Saïdi 2003:** MSRI41, 107–118, §2, Proposition2.1 and Proposition2.3 (not “Corollary2.3”). Primary URL https://library.slmath.org/books/Book41/files/pop.pdf . Their Section2 is over the algebraic closure of a finite field; their proof constructs pairwise coprime orders. Ozman–Pries Theorem8.2(3)'s summary is not used as a prime-degree existence input. Web ref `turn998441511view0`.

The original Nakajima paper, Adv. Stud. Pure Math. **2** (1983), 69–88, was not recovered. The primary MSJ volume index confirms the bibliographic correction from the incorrect volume/year in Pop–Saïdi; the original Project Euclid endpoint presented an additional-security check. No original theorem text is claimed to have been read. The all-degree conclusion is instead supported directly by Yang Theorem3.5 as above.

## Remaining gate

No universal finite-field proof or finite-field positive-rank counterexample has been produced. The sharpened sufficient question is whether a positive-rank genus-two finite-field curve must admit an exact odd-prime-power theta point satisfying <2,-1> = units. Generic results and finite-prime avoidance do not decide it. Neither Hooley's prime distribution theorem nor Poonen's projection theorem supplies this incidence statement.

## Packaging

Include the LaTeX source, bibliography supplement, this note, both scripts, both JSON check outputs, event TSV, and manifest. Exclude downloaded external article PDFs and their text extractions; they are working source copies, not deliverables. No root final files were edited by this follow-up.
