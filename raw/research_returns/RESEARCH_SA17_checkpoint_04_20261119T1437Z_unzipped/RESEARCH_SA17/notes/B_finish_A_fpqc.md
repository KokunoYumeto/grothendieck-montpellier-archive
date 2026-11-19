# Focused A branch from the B researcher

Run: RESEARCH_SA17_FINISH, 2026-11-19. Model: GPT-6 Astra (OpenAI,
ChatGPT Pro mode), agent `dieudonne`. We record this branch separately from
the A owner's files. No priority claim is made.

## Scope and state, 13:54 UTC

The candidate is the functor on F_p[t]-algebras

    P(R) = alpha_p(R^h_(t)).

The earlier record establishes its filtered-colimit compatibility, fppf
descent, fpqc separatedness, and fpqc descent over noetherian G-rings.
The all-ring fpqc equalizer remains unproved. This branch checked two
possible source-based shortcuts and one new obstruction. The obstruction
does settle a property of the candidate: **P fails the strengthened
noetherian adic condition 4, for every prime p.** Thus this candidate cannot
refute L2, even if its remaining fpqc descent gate is settled.

## Independent audit of the adic obstruction proposed by the root agent

Let A_0=F_p[t], K=F_p(t), H=(A_0)^h_(t), and K^h=Frac(H). The ring H embeds
in F_p[[t]]: Stacks 0EM7, Lemma 15.12.4, gives a faithfully flat map from H
to the t-adic completion, so it is injective. In particular H is a domain.

Choose infinitely many pairwise distinct monic irreducibles q_n in F_p[t]
other than t, indexed by n>=1. Their nonzero constant terms imply that they
are units in H. Put r_n=t/q_n. Since r_n lies in tH, the polynomial
X^p-X-r_n has a unique root f_n in tH, by the simple-root Hensel property.

For every N the classes r_1,...,r_N are linearly independent over F_p in
K/(F-1)K. Indeed, a nonzero sum of them has a pole of order exactly one at
any q_j with nonzero coefficient. For g in K, a pole of g of order e>0
gives a pole of g^p-g of order pe; if g has no pole at q_j, neither does
g^p-g. Thus such a sum cannot be g^p-g.

Consequently [K(f_1,...,f_N):K]=p^N. Here is the elementary Galois argument,
so that the use of Artin--Schreier theory has no hidden degree assumption.
The field L_N=K(f_1,...,f_N) is the splitting field of the separable
polynomials X^p-X-r_i. Its Galois group embeds into F_p^N by
sigma -> (sigma(f_i)-f_i)_i. If the image were proper, a nonzero F_p-linear
functional (c_i) would vanish on it. Then g=sum c_i f_i would be fixed and
would belong to K, while g^p-g=sum c_i r_i, contradicting the preceding
pole calculation. Hence the image is F_p^N and the degree is p^N.

Set R=A_0[[s]], A=R[epsilon]/(epsilon^2), and J=(s). The ring A is
noetherian and J-adically complete. Henselization of a pair commutes with
finite algebra base change: if B is finite over D, then B tensor_D D^h
is henselian for the extended ideal (the idempotent criterion, Stacks
09XI), is ind-etale over B, and has the required quotient; the universal
property gives the canonical isomorphism with B^h. This applies both to
quotients and to the square-zero algebra. Therefore

    A^h_(t) = R^h_(t)[epsilon]/(epsilon^2),
    (A/s^N A)^h_(t) = H[s,epsilon]/(s^N,epsilon^2).

These isomorphisms are compatible with all reduction maps. The second
one can also be obtained by first identifying R/s^N with A_0[s]/s^N and
then applying the finite base-change assertion to A_0 -> H.

For N>=1 put

    z_N = epsilon * sum_(1<=n<N) f_n s^n.

Because epsilon^2=0 and p>=2, each z_N is an alpha_p point. The points z_N
are compatible under reduction. Suppose they lift to z in P(A).
The ring R is reduced. Every etale R-algebra is reduced (Stacks 033B),
and a filtered colimit of reduced rings is reduced: a nilpotence equation
is witnessed at some stage, where its element is zero. Thus R^h_(t) is
reduced. Writing z=b+epsilon a, the equation z^p=0 gives b^p=0 and hence
b=0. It follows that a in R^h_(t) has reductions

    a mod s^N = sum_(1<=n<N) f_n s^n

in H[s]/s^N for every N.

Choose one finitely presented etale R-algebra C, a map C -> R^h_(t), and
c in C mapping to a. Such a choice exists by the defining filtered etale
presentation of henselization (Stacks 0EM7, Lemma 15.12.1). Reduction gives
a map C/sC -> H, hence a map (C/sC) tensor_(A_0) K -> K^h. Its source is
an etale algebra of finite presentation over the field K, so it is a
finite product of finite separable field extensions. Its image is
therefore one finite separable field L/K inside K^h.

The standard coefficientwise homomorphism R=A_0[[s]] -> L[[s]], together
with C/sC -> L, lifts uniquely to compatible R-algebra maps
C -> L[s]/s^N, by formal etaleness of C/R. Taking the inverse limit gives
C -> L[[s]]. After the inclusion L[[s]] -> K^h[[s]], this map is the
unique lift of the same map C/sC -> K^h. The maps obtained from
C -> R^h_(t) -> H[s]/s^N -> K^h[s]/s^N are also such lifts. Uniqueness at
each N identifies them. In particular the image of c in L[[s]] is the
series sum_(n>=1) f_n s^n. Thus every f_n belongs to the single finite
field extension L, contradicting [K(f_1,...,f_N):K]=p^N for large N.

This proves that

    P(A) -> lim_N P(A/s^N A)

is not surjective. The proof includes p=2: no division by 2 occurs, and
the square-zero identity already gives epsilon^p=0. It does not use fpqc
descent of P. The counterexample is infinite, so no finite computation
can replace its unbounded-degree argument. The root agent owns its paper
statement, result id and check-event integration; we sent the complete
audit to the root before writing this record.

## Source checks for the all-ring fpqc gate

### Henselian positive loops do not formally specialize

We opened K. Cesnavicius, *The affine Grassmannian as a presheaf quotient*,
arXiv:2401.04314v3 (18 May 2025), Proposition 3, printed pp. 2--3. It proves
fpqc descent for B -> X(B{u}) with u an independent polynomial variable
and X affine (and then quasi-affine). The key injectivity concerns

    B'{u} tensor_(B{u}) B'{u} -> (B' tensor_B B'){u}.

The proof uses M. Raynaud--L. Gruson, *Criteres de platitude et de
projectivite*, Invent. Math. 13 (1971), I, Corollary 3.2.6, printed p. 18.
We opened the original-volume source and its indexed text. That corollary
gives universal injectivity over the coefficient ring of a finitely
presented flat module when the relevant relative associated points are
met. In the application the coefficient ring is B' tensor_B B', and the
fibres are etale algebras over a polynomial ring in the independent u.
The statement is not universal injectivity as a module over
(B' tensor_B B')[u]. Consequently passage to the quotient u-t is not a
base change for the coefficient ring in that application. It does not
prove the corresponding map for t-henselizations. We have no proof that
the needed stronger purity holds.

### The p-henselian cohomology theorem has a different hypothesis

We opened K. Cesnavicius--P. Scholze, *Purity for flat cohomology*, Annals
of Math. 199 (2024), 51--180; arXiv:1912.10932. The checked places are
Claim 5.3.5.3, Theorem 5.5.2, Corollary 5.5.3, Remark 5.6.8 and Corollary
5.6.9. The p-henselian statement in Corollary 5.5.3 uses that the finite
flat p-primary group becomes etale after inverting p and uses the
corresponding p-adic continuity. It does not apply to alpha_p after
henselizing along an unrelated element t in characteristic p. The
general henselian-pair comparison in Corollary 5.6.9 concerns higher
cohomology (and an H^1 surjectivity assertion), not the H^0 assertion
needed here. No source theorem from those locations closes this gate.

### A general finitary-fppf-to-fpqc principle is false

We reopened Stacks 0ATE (Section 110.78) and 0ATF (Lemma 110.78.1).
The construction supplies a strictly henselian regular local ring R of
characteristic p, its faithfully flat absolute integral closure R^+,
and a finite R-algebra S embedded in R^+ such that a point of Spec S
cannot exist over a flat finitely presented R-algebra whose spectrum
meets the closed point of Spec R. The two assertions immediately before
Lemma 110.78.1 give this obstruction via the absence of finite flat
algebras receiving S. We use the nonempty/closed-fibre version: the zero
algebra or an algebra supported away from the closed point is irrelevant
to a covering and must not be included in the assertion.

Let Q be the fppf image sheaf of h_(Spec S) -> * on R-algebras. Explicitly,
Q(T) is the singleton if Spec S has a point fppf locally over T, and is
empty otherwise. This functor commutes with filtered colimits: a finite
fppf covering and its S-points descend to a finite stage, since S/R and
the covering algebras are finitely presented, and flatness and
surjectivity descend after enlarging that stage. Thus Q is a finitary
fppf sheaf. However Q(R)=empty and Q(R^+) is a singleton. Since Q is
subterminal, its two sections on the double overlap automatically agree.
It is not an fpqc sheaf. This rules out a general implication from
finitarity plus fppf descent; additional structure of P would be needed.

## Direct nilpotent-cocycle attempt and its exact failure

After replacing a henselian base R and a faithfully flat cover B by its
t-henselization, the datum is b in B with b^p=0, such that

    (1+t c)(b tensor 1 - 1 tensor b)=0

in C=B tensor_R B for some finite sum c=sum u_i tensor v_i. This is the
kernel criterion for C -> C^h_(t). It is stronger than merely saying that
the difference lies in every t^n C. We tried to turn the nilpotence into a
finite etale equation over R. The finite R-algebra R[b] alone does not
solve this: R[b] tensor_R R[b] -> B tensor_R B need not be injective.

The pure inclusion R -> B admits partial R-linear splittings on any
specified finite collection of module relations. Applying one to the
first factor of the displayed equation and its multiples b^k yields
finite expressions c_k in B with c_(k+1)=b c_k, c_p=0, and
c_0=1+t sum lambda(u_i)v_i a unit. This proves no new descent statement:
the coefficients lambda(u_i b^k) remain independent R-elements and the
identities do not force b into R. A global retraction over a complete
noetherian local R does give the earlier successful argument, but no
general retraction has been constructed. We do not treat this attempt as
a proof or as a refutation of fpqc descent.

## Search record

Searches included the exact phrases "fppf sheaf"/"filtered colimits"/
"fpqc sheaf", "finitary sheaves"/"fpqc", French variants with "faisceau"
and "limites inductives", "henselization fpqc sheaf faithfully flat ring
equalizer", and "flat ring maps"/"filtered colimits"/"finitely
presented". We relied only on opened primary sources. No novelty or
exhaustiveness claim follows from a negative search.

Downloaded research copies and extracted text for the Cesnavicius and
Cesnavicius--Scholze sources are in references/B_finish_sources. The
Raynaud--Gruson volume PDF is a source-retrieval intermediate, not a new
mathematical deliverable. The all-ring fpqc equalizer remains open in this
branch. The root's newly audited adic obstruction is independent of that
gate and excludes this candidate from L2.
