# Uniform supported-cohomology movement and the remaining B1 boundary step

19 November 2026. Source audit and failed-method analysis. This does not
prove or refute the projective-space colimit vanishing, and does not
reduce its universal test class. The first remaining group is

    H^4(F_0 P^4_Fbarq, Q_ell(3))^Gamma,

with continuous cohomology on each finite-type open taken before the
open colimit. Here ell differs from char(Fq).

## The genuinely uniform theorem inspected

Schreieder, *A moving lemma for cohomology with support*, EPIGA,
special volume in honour of C. Voisin, Article 20 (2024), 50 pages,
primary published-version PDF:
https://arxiv.org/pdf/2207.08297v3.

Theorem 5.1, pp. 16--21, applies to a smooth equidimensional scheme U
with a smooth projective compactification, a morphism f:S->U with S
locally equidimensional, and a nowhere dense closed Z in U. It supplies
Z' contained in W contained in U, with Z contained in W and
dim W <= dim Z+1, and

    im[H_Z^*(U,n) -> H_W^*(U,n)]
       contained in im[H_Z'^*(U,n) -> H_W^*(U,n)].

The subsets have the specified proper-intersection conditions with S.
After a precisely bounded shrinking of S, W is compatible with further
localization of U. The analogous statement for Z' is false: Remark 5.2,
p. 16, exhibits a line in P^2 with two subsequently removed points.

This is uniform over classes, not an assertion that one independently
chooses a support for each class. In the proof, Lemmas 5.3--5.4 first
choose a moved diagonal Delta' and a rational-equivalence support
W_(X times X). Equations (5.2)--(5.3) then construct Z' and W solely
from these algebraic data, Z, and the boundary. Step 1 uses the action of
correspondences to treat every supported class at once. Those algebraic
choices do not use the coefficient system. Consequently the same choices
work for every coefficient theory satisfying the stated axioms C1--C4,
including simultaneously the finite ell-power and continuous Z_ell
theories supplied by Proposition 3.2. Rationalization gives the Q_ell
version. No inverse-limit/open-colimit exchange is needed for this
conclusion.

Corollary 6.3, pp. 22--23 (the strengthened form of Corollary 1.4),
does give a single W with

    H_Z^*(X_S,n) -> H_W^*(X_S,n) = 0

for the specified semilocal or sufficiently low-dimensional S. Here
X_S still denotes a colimit over open neighbourhoods of S. It is not a
claim that the displayed vanishing has already occurred on one common
neighbourhood for every element of that colimit. Its finite-level
Gersten consequence is Corollary 6.4, pp. 23--25, whose terms retain that
neighbourhood colimit.

## Applying it to the critical B1 class

Let alpha in H^4(Ubar,Q_ell(3))^Gamma be a representative of the
critical colimit class, with U=P^4 minus a closed boundary D. We may
enlarge D to an effective divisor, since every proper closed subset of
projective space is contained in a hypersurface and restriction preserves
the represented colimit class. The localization boundary is

    delta(alpha) in H_D^5(P^4_bar,Q_ell(3)).

Theorem 1.1 gives W of dimension dim D+1=4, hence W=P^4. The stronger
Theorem 5.1 only bounds dim W above by 4 and does not guarantee a proper
W; indeed its Step 3, p. 20, explicitly takes W=U in codimension one.
On P^4 the image under consideration is then

    H_D^5(P^4_bar,Q_ell(3)) -> H^5(P^4_bar,Q_ell(3)) = 0.

Thus the supported-cohomology inclusion is satisfied with the moved
class zero. This gives no new statement about delta(alpha), and no
nonempty open on which alpha vanishes. In the proof of the open-class
variant, Corollary 6.5(2), pp. 25--26, the comparison open is constructed
inside X minus W. If W=X, that comparison open is empty. Substituting
codimension one into the displayed codimension estimate gives precisely
this zero-codimension loss.

For supports of codimension at least two, the dimension estimate does
provide a proper W, and the theorem gives useful uniform control. The
missing preliminary step in our problem is to replace the arbitrary
divisorial ramification of alpha by such a higher-codimension support
without discarding the same colimit class. The theorem does not supply
that preliminary step.

Corollary 1.6(2), or its proof in Corollary 6.5(2), does not remove it
either: that statement starts with a class which already lifts from
F_j to F_(j+1). At j=0, it moves an already unramified class near a
specified closed curve. It does not prove that an arbitrary class on
F_0 is unramified. Treating its lifting hypothesis as a conclusion would
assume the residue-vanishing step one is trying to prove.

In the explicit two-component smooth-boundary case, the accompanying
note b1_uniform_ramification_obstruction.md computes the fixed-open
motivic comparison cokernel as

    im[Pic(D1 intersect D2)_Q tensor Q_ell
          -> (CH^2(D1)_Q direct_sum CH^2(D2)_Q) tensor Q_ell]
       intersect ker(cycle class).

The new uniform movement theorem does not turn cohomological Gysin
relations in this formula into rational Chow relations. Nor does this
fixed-open formula prove survival under further shrinking. Both logical
directions remain distinct.

## Scope of the primary-source reading

The owner read the complete statement and proof of Theorem 5.1,
including Lemmas 5.3--5.4 and all four steps, pp. 16--21; the full
proofs of Lemmas 4.1--4.6, pp. 11--13; Remark 5.2, p. 16; the full
proofs of Corollaries 6.3--6.5, pp. 22--26; axioms C1--C5 and
Proposition 3.2, pp. 8--10; and the final proof of Proposition 3.2 in
Appendix A.11, p. 44. This is a full reading of the moving argument
relative to its displayed cohomology axioms. The intermediate lemmas
of Appendix A were not all independently reread, and Levine's moving
lemma invoked as Theorem 2.1 was read here as a precise statement,
not independently reproved from its external references.

The coefficient-uniform observation above follows directly from the
order of choices in the written proof; it is not a claim that the paper
separately states a universal coefficient theorem. We use the
compactification hypothesis only for P^4 and its opens. We do not claim
smooth projective compactifications for arbitrary positive-characteristic
varieties.

The source was retrieved by code/capture_post08_sources.py, with the
URL, timestamp, size, SHA256, and text-extraction path recorded in
output/post08_primary_capture.json. The raw primary PDF is excluded
from deliverables.

Part D independently read the complete written note and checked the algebraic
coefficient-uniform choices, the codimension-one escape, the semilocal
colimit distinction, and the absence of any survival claim. D also opened
and read the primary Theorem 5.1 statement, complete Lemmas 5.3--5.4,
equations (5.2)--(5.3), Steps 1 and 3, Remark 5.2 and the Proposition 3.2
statement. That independent source check does not include all of Steps 2
and 4 or the Appendix A proof dependencies.
