# Partial perfection separates PD torsion freeness from quasisyntomicity

Research proof, 19 November 2026. Run RESEARCH_SA17_FINISH-20261119,
GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent dieudonne.
This is an original derivation in this run, with no claim of priority.

## Statement and construction

Fix any prime p and put k=F_p. Let

    P = k[a^(1/p^infinity), b^(1/p^infinity)],
    J = ker(P -> k),
    S = k[c,d],
    R = P x_k S.

The maps to k set all displayed variables to zero. Equivalently,
R=P[c,d]/J(c,d). This R is reduced, F-finite and PD torsion free,
but is not quasisyntomic. Consequently it belongs to the documented
positive class PF but not to Q.

## Reducedness and F-finiteness

The fibre product embeds in the product of the two domains P and S,
so it is reduced. Frobenius on P is an isomorphism. The p^2 monomials
c^i d^j for 0<=i,j<p, with the (0,0) monomial interpreted as the unit
of R, generate R over its Frobenius image. To see this without silently
changing the common constant term, write g in S uniquely as
sum h_ij(c,d)^p c^i d^j. For (f,g) in R, choose the coefficient of
the constant monomial to be (f^(1/p),h_00). These have the same
constant term. For each other monomial choose (h_ij(0),h_ij) as its
coefficient in R. Its perfect-component contribution is killed by
the nonconstant monomial. Thus these p^2 generators suffice.

## Failure of quasisyntomicity

The ideal J satisfies J^2=J, since every one of its generators has
arbitrarily deep p-th roots in J. In the presentation A0=P[c,d] -> R,
write I=J(c,d). Then

    I/I^2 = J(c,d)/J(c,d)^2 = J direct-sum J

as an R-module, where the R-action on J factors through R -> P.
The two copies correspond to c,d modulo (c,d)^2.

The P-module J is not flat. The elements a,b form a regular sequence
in P: this follows either from the monomial description, or by the
faithfully flat transition maps of the polynomial rings
k[a^(1/p^n),b^(1/p^n)]. Thus L=(a,b)P has presentation

    0 -> P --u |-> (bu,-au)--> P^2 -> L -> 0.

After tensoring with J, the class of (b,-a) in
J^2/{(bj,-aj):j in J} is a nonzero element of the kernel of
L tensor_P J -> J. It is nonzero because equality with (bj,-aj)
would force j=1 in the domain P, while 1 is not in J. Hence J is
not P-flat. If J were R-flat, base change along R -> P would make
J tensor_R P=J P-flat; therefore J is not R-flat either.

Since P is perfect, L_(P/k)=0, and L_(A0/k)=A0 dc direct-sum A0 dd.
If R were quasisyntomic, L_(R/k) would have Tor amplitude [-1,0].
For this implication from the usual absolute definition, use BMS,
Lemma 4.34 with the perfectoid base k; the primary PDF was opened
at https://people.mpim-bonn.mpg.de/scholze/bms2.pdf, printed page25,
lines1502-1517 in the browser extraction. The transitivity triangle
then gives L_(R/A0) Tor amplitude [-1,0]. Since A0 -> R is surjective,
H^0(L_(R/A0))=0 and H^(-1)(L_(R/A0))=I/I^2, so this module must be
flat over R. The preceding nonflatness contradicts this.

## Torsion removal in an actual universal PD presentation

Let C=Z_p[a,b,c,d], let K=(p,ac,ad,bc,bd), and let D be its ordinary
universal PD envelope relative to the canonical PD ideal (p) in Z_p.
Let sigma be the endomorphism sending a,b to a^p,b^p and fixing c,d
and Z_p. It acts on D by the universal property.

Give a,b bidegrees (1,0),(0,1), and c,d and Z_p bidegree (0,0).
The ring D has a nonnegative bidegree decomposition. Explicitly it
is generated over C by gamma_n(ac), gamma_n(ad), gamma_n(bc),
gamma_n(bd), with the expected bidegrees; the universal PD relations
are homogeneous. Alternatively, scaling a and b gives a coaction
D -> D[t_a,t_b], which gives this grading and avoids relying on a
chosen relation presentation. The degree-(0,0) summand is Z_p[c,d]:
the displayed generators have positive degree, and setting a=b=0
gives a retraction to Z_p[c,d] with the canonical PD ideal (p).

For every homogeneous z of bidegree (u,v),

    sigma^e(z) = a^(u(p^e-1)) b^(v(p^e-1)) z.

This follows on the displayed algebra generators from
gamma_n(a^(p^e-1)ac)=a^(n(p^e-1))gamma_n(ac), and then on every
homogeneous polynomial in them.

After inverting a, the ideal K becomes (p,c,d), and D[1/a] is
Z_p[a,a^(-1),b]<c,d>, a free divided-power polynomial algebra over
a p-torsion-free ring. In particular it is p-torsion free. The same
holds after inverting b. PD envelopes commute with these localizations
by their universal property (or Stacks, Section60.2, flat base change).

Now let z be a homogeneous p-torsion element of D. If u>0, localization
at a shows that a^N z=0 for some N. The formula above kills z after
a sufficiently large iterate of sigma. If u=0 and v>0, use b instead.
If u=v=0, z is already zero because Z_p[c,d] is p-torsion free.
Every element has only finitely many homogeneous components, so every
p-torsion element is eventually killed by an iterate of sigma.

Consequently D_infinity=colim(D --sigma--> D --sigma--> ...) is
p-torsion free. Indeed, if p times a colimit element is zero, it has
a representative that becomes p-torsion at one finite stage; the
preceding argument kills that representative at a later stage.

This is an appropriate universal PD presentation of the asserted
ring, not an appeal to arbitrary-ambient independence. Put

    C_infinity=colim(C --sigma--> C --sigma--> ...),
    A=the p-adic completion of C_infinity.

The ring C_infinity is p-torsion free. Its completion A is p-complete
and p-torsion free, and

    A/p = P[c,d],

which has the p-basis c,d in Lau's strong Frobenius convention.
There is a surjection A -> R. By the universal property, ordinary PD
envelopes commute with the displayed filtered colimit of pairs, so
D_infinity is the universal PD envelope of C_infinity -> R.
The p-completion of D_infinity is the universal p-complete PD envelope
of A -> R: for each n, maps to PD rings killed by p^n factor through
the same reduction of C_infinity and A. These mod-p^n universal
properties identify the completed envelopes. Since completion of a
p-torsion-free ring is p-torsion free, this completed envelope is
p-torsion free. It is a legitimate presentation in Lau, Section4,
and Proposition4.2/Definition4.3 therefore make R PD torsion free.

For completeness, the elementary completion assertion can be checked
directly: if px=0 in lim_n D_infinity/p^n, then a representative of
x_(n+1) lies in p^nD_infinity modulo p^(n+1), by cancellation of p in
D_infinity. Hence x_n=0 for every n. The same argument applies to
C_infinity, and Stacks05GG identifies completion modulo p with the
original quotient modulo p.

## Consequences for the documented union

For U=Q union PF union PE, the established B:closure-reduction now has
an explicit witness R in PF minus Q. Thus:

* U is not stable under finite direct products: R times k[epsilon]/epsilon^2
  is not Q (R is a retract) and is not reduced (so neither PF nor PE).
* U is preserved by etale extensions/localizations, but membership is
  not local for etale covers: the two open-and-closed pieces of that
  same product are individually in U.
* U is not stable under filtered colimits: every R[t_1,...,t_n] lies in
  PF, but R[t_1,t_2,...] lies outside U.
* Even the separate etale-local closure U_et is not stable under
  filtered colimits. This is the already audited strengthened
  B:closure-reduction using a prime where R is non-Q, the augmentation,
  and the infinite embedding dimension at p+(all t_i).
* U_et is stable under finite direct products and etale localization/
  descent, as already proved. No claim about arbitrary infinite direct
  products of U_et is made or needed for the raw-union conclusion.

## Search record and status

Searches before presenting this witness included the exact combinations
"PD torsion free"/"not"/"quasisyntomic", "divided power"/"partial perfection",
and "quasisyntomic"/"perfect"/"fibre product", as well as the earlier
PD-flatness converse searches recorded in B_research.md. These searches
did not supply this construction or a theorem settling the inclusion.
No priority claim is made. The construction and all its deductions are
to be checked directly, independently of absence of search results.


## Independent targeted audit

At 2026-11-19T14:56:38Z, root reported a full targeted proof audit PASS, opening Lau v2 Section4 (Proposition4.2 and Definition4.3) and BMS2 Lemma4.34, printed page25. Integrated into sections/B.tex as B:PD-not-QSyn and B:largest-literature-class; catalog and check events updated.
