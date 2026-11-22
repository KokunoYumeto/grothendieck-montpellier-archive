"""Record the final source and cross-review audit; no numerical claims are inferred."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]

def rewrite(name, old, new):
    path = ROOT / name
    value = path.read_text()
    assert value.count(old) == 1, (name, old[:90], value.count(old))
    path.write_text(value.replace(old, new))

rewrite("sections/part_a7.tex", r"$(\bar c,1)$", r"$(\bar{c},1)$")

path = ROOT / "sections/part_a5.tex"
path.write_text(path.read_text() + r"""

\paragraph{The base in L7.}
The quotient-stack presentation and its coarse invariant already descend
to $\Z[1/2]$. Indeed ordered four-pointed curves, their relabelling
action, and the displayed function $J$ are defined over that ring; the
same integrality and normality proof computes its invariant ring.
Adjoining $i$ is needed for the particular displayed octahedral
matrices, not for the existence of this moduli stack or its coarse
space. No averaging by $|\mathfrak S_3|$ is used at characteristic $3$.
""")

criterion = r"""\begin{proposition}[Known: the precise smooth-curve cyclotomic criterion]
\label{A6-cyclotomic-detection}
Let $U/k$ be a smooth affine geometrically connected hyperbolic curve
over a number field, with $\Pi=\pi_1(U)$ and geometric kernel $\Delta$.
For $1\ne z\in\Delta$, the element $z$ belongs to a conjugate of a cusp
inertia group if and only if there is a closed subgroup $N\subset\Pi$
whose image in $G_k$ is open and such that
\[
 nzn^{-1}=z^{\chi(n)}\qquad(n\in N).
\]
Here $\chi$ is the cyclotomic character pulled back from $G_k$.
\end{proposition}
\begin{proof}
This is \cite[Theorem (2.1.1), pp.~94--97]{Nakamura1994A567}.
For a cusp, its decomposition group gives $N$ by the local Kummer
description. Conversely, Lemma~(2.1.4) there says that a nonperipheral
$z$ survives outside the span of cusp classes in the mod-$\ell$
abelianization of some open subgroup $H\subset\Delta$ containing $z$.
After a finite extension of $k$, realize $H$ by an \'etale cover $V$
and make $N\cap\pi_1(V)$ surject onto the base Galois group.
The image of $z$ in the Tate module of the compactification's Jacobian
would then be cyclotomic. At good reduction its Frobenius eigenvalue
would have absolute value $q$, while the Jacobian eigenvalues have
absolute value $\sqrt q$. Thus that image is zero. The kernel is the
span of cusp classes, contradicting the choice of $H$.
\end{proof}
This detects elements belonging to inertia, including their powers;
it does not make all procyclic subgroups into a finite set. Its
hypotheses concern smooth affine curves with their usual arithmetic
action. For the framed singular-logarithmic action, the applicable
statement above is Lemma~\ref{A6-graphic}.

"""
rewrite("sections/part_a6.tex",
        r"\begin{proposition}[Refuted literally; clarified geometric reading of NB 048]",
        criterion + r"\begin{proposition}[Refuted literally; clarified geometric reading of NB 048]")

path = ROOT / "sections/part_a6.tex"
value = path.read_text()
start = value.index("The 1990 Nakamura article and the 1997 Ihara")
end = value.index("\n\n", start)
historical = r"""The historical links in L6 can also be made more precise.
The authors' survey \cite[\S2.4, pp.~7--8 of the author PDF]{NakamuraTamagawaMochizuki2001A567}
attributes to Nakamura's 1990 paper the recovery of a hyperbolic
genus-zero curve over a field finitely generated over $\Q$ from its
arithmetic fundamental group: peripheral recovery is followed by
Kummer recovery of cross-ratios. The opened 1994 paper supplies the
precise inertia theorem stated above.

For Ihara--Nakamura, their opened 1995 conference summary
\cite[\S\S1.2--1.4, Theorem $2'$ and Theorems 3A--3B]{IharaNakamura1995A567}
reproduces the introduction to the deformation paper. With a
maximally degenerate curve whose components are three-pointed rational
lines, specified tangential structure and an ordering of its nodes,
it constructs distinguished formal smoothing parameters. On their
diagonal it compares Galois actions on the resulting smooth curve's
tangential fundamental groupoid with that of the three-punctured
line, and obtains the corresponding constant-field inclusion for
Oda's problem (equality in the stated punctured pro-$\ell$ case).
This is a degeneration and Galois-action comparison, not the
full-faithfulness assertion of Theorem~\ref{A6-anabelian}.

The mathematical pages of the original 1990 article and the full
1997 article remained inaccessible after publisher, author and archive
attempts. Their bibliography entries retain that status. The 1995
summary announces the quoted deformation results and is not presented
as an opened copy of the full 1997 proof; all proof inputs for our
reconstruction theorem are the full sources identified above."""
path.write_text(value[:start] + historical + value[end:])

rewrite("sources/part_a567.bib",
        "Definitions 1.1 and 2.3, Theorem 1.6",
        "Definitions 1.1 and 2.3, Proposition 1.2(ii), Theorem 1.6")
rewrite("sources/part_a567.bib",
        "Theorem B, Theorem 4.8(iv), Proposition 4.10(ii)",
        "Theorem B, Definition 4.4, Proposition 4.5, Theorem 4.8(iv),(v), Proposition 4.10(ii)")
path = ROOT / "sources/part_a567.bib"
path.write_text(path.read_text() + r"""
@article{Nakamura1994A567,
 author={Nakamura, Hiroaki},
 title={Galois Rigidity of Pure Sphere Braid Groups and Profinite Calculus},
 journal={Journal of Mathematical Sciences, The University of Tokyo},
 volume={1}, number={1}, year={1994}, pages={71--136},
 url={https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf},
 note={Opened full published PDF; Section2.1, Theorem(2.1.1), Lemmas(2.1.2),(2.1.4), and proof, pp.93--97; full profinite case used. Exact theorem reopened during final audit}
}
@article{NakamuraTamagawaMochizuki2001A567,
 author={Nakamura, Hiroaki and Tamagawa, Akio and Mochizuki, Shinichi},
 title={The {Grothendieck} Conjecture on the Fundamental Groups of Algebraic Curves},
 journal={Sugaku Expositions}, volume={14}, number={1},
 year={2001}, pages={31--53},
 url={https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Grothendieck%20Conjecture%20on%20the%20Fundamental%20Groups%20of%20Algebraic%20Curves.pdf},
 note={Opened full author translation; Section2.4, author-PDF pp.7--8, gives the authors' retrospective account of Nakamura1990. Publication metadata checked on Nakamura's Osaka faculty bibliography. Translation of Sugaku50(1998),113--129}
}
@article{IharaNakamura1995A567,
 author={Ihara, Yasutaka and Nakamura, Hiroaki},
 title={On the Universal Field of Definition of the {Galois--Teichm\"uller} Tower: Deformation of Maximally Degenerate Curves and {Oda}'s Conjecture},
 journal={RIMS K\^oky\^uroku}, volume={925}, year={1995}, pages={129--133},
 url={https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0925-16.pdf},
 note={Opened complete five-page conference summary; title translated from Japanese. Its English Section1 reproduces the deformation-paper introduction. Sections1.2--1.4, Theorem2-prime and Theorems3A--3B read. This is an announcement/summary, not the full1997 proof}
}
""")

path = ROOT / "notes/part_a567.md"
value = path.read_text().replace(
    "Any quasi-cyclotomic constituent satisfying ψ^b=χ^a",
    "Any Q-cyclotomic constituent satisfying ψ^b=χ^a")
value += """

## Final source audit and cross-review, 19 November 2026 after 12:17 UTC

### A6(a) hypotheses and normal-torus globalization

The precise distinction in Mochizuki2007 Definition2.3 is now corrected:
Q-cyclotomic means a positive power equals an integral power of chi
on an open subgroup; quasi-cyclotomic means equality with chi on an
open subgroup. The associated-weight argument uses Q-cyclotomic.

Mochizuki2007 Proposition1.2(ii) makes each vertex group
commensurably terminal, hence self-normalizing in the geometric group.
After splitting the graph over L, the arithmetic normalizer surjects
onto G_L and has that geometric vertex group as kernel. Its induced
outer action is the actual action on the punctured normalization.
Centre-freeness identifies the extension with the pullback
Aut(Delta_v) x_Out(Delta_v) G_L. Mochizuki1999 TheoremA explicitly
includes the full profinite arithmetic assertion, so it is not being
extrapolated from its geometrically pro-p clause.

The full2012 paper was converted to local text and re-read at
Definition4.4, Proposition4.5, Theorem4.8(iv),(v), Proposition4.10(ii),
Lemma5.4 and Theorem5.7. The twist kernel statements allow arbitrary
semi-graphs, including loops. The geometric monodromy theorem is used
over Kbar[[t]], with separably closed residue field of characteristic0,
so all primes are allowed. Galois equivariance follows from the
functorial synchronization and its node-wise uniqueness.

The normal-torus functor is now explicitly globalized. On T_J the
tautological normal vectors v_j give units a_j=dx_j(v_j). Local charts
x_j/a_j agree because changing x_j to u_j*x_j changes a_j to
(u_j restricted to S_J)*a_j. Thus the pullback logarithmic structure
has a global N^J chart, and its pro-Kummer roots define the desired
finite-cover functor. The overlap rule also gives Galois descent when
branches are permuted. Composition for nested strata is the canonical
homotopy of Hoshi--Matsumoto--Nakayama2026 Proposition3.
Their Proposition2 and Remark1 give exactly the first-order chart
dependence. Fresh opened ref: turn131690314view0.

The parent reports independently reading HoshiRIMS1558 Cor3.9 and
PropA.10, Temkin1.1.15, and the log-ring weak-factorization derivation,
and agreeing with their stated applications. Earlier paragraphs and
events recording a requested review are historical, not current gates.

### Historical L6 sources recovered

The original1990 and1997 texts retain their honest not-opened status.
Three further primary sources were opened:

- Nakamura1994 full published PDF:
  https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf .
  Section2.1, Theorem(2.1.1), Lemmas(2.1.2),(2.1.4), pp93--97.
  Fresh refs turn807807931view2 and turn393176829view0.
  It gives an exact cyclotomic-normalizer test for membership in the
  union of cusp inertia groups of a smooth affine hyperbolic curve
  over a number field. The new numbered proposition
  A6-cyclotomic-detection states the full-profinite specialization and
  derives it using the all-cover mod-l detection lemma and Weil weights.
  It is not silently applied to the limiting action of a singular log curve.
- Nakamura--Tamagawa--Mochizuki2001, the authors' own survey, Section2.4,
  author-PDF pp7--8, fresh ref turn484472058view1. It attributes the
  genus-zero arithmetic reconstruction over fields finitely generated
  over Q to Nakamura1990 and explains inertia plus Kummer cross-ratios.
  This is an opened retrospective account, not an opened1990 proof.
- Ihara--Nakamura1995, RIMS Kokyuroku925,129--133:
  https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0925-16.pdf .
  Fresh ref turn484472058view0. Sections1.2--1.4 reproduce the English
  deformation-paper introduction, with exact Theorem2-prime and
  Theorems3A--3B. The additional tangential structure and node ordering
  are essential to its formal coordinates and Galois-groupoid comparison.
  This supports L6's historical connection without importing an
  unavailable proof or confusing Oda's constant-field assertion with
  complete stable-log reconstruction.

### Independent analytic re-proof requested by the parent

I read part_a2b_secondary.tex, part_a2_limits.tex and part_a1_range.tex
in full, independently of their author's review, and found no
substantive gap in the stated unbordered/fixed-compactification claims.
The checks were as follows.

1. In the seam coordinate zeta=x+iy, log|w|=-y/lambda. Its variation
   gives h=c-V_y and seam normal velocity V. Differentiating continuity
   of the first spatial derivatives, with second derivatives1 on the
   core and0 on the cylinder, gives h_y(flat)-h_y(core)=V.
   The Green identities have the stated signs; their sum is
   pi*sum(dot s_i dot F_i)=E_h+E_V. Using V_b and h_a in the two
   boundary identities proves the full bilinear symmetry, not merely
   positivity of a quadratic form. Zero energy forces h=0 on the
   nonempty core and then c_i=0 by bounded harmonic uniqueness.
2. Collars extend the inverse cap map to radius exp(a_i/lambda_i);
   rescaling its source disc gives the precise stated bound on its
   first coefficient. This is uniform in all other boundary lengths.
   The cusp decay gives zero truncated Green boundary terms.
3. The area comparison projects cylinder excursions nonexpansively
   onto the core, so every peripheral test circle has length at least
   L_i. Cauchy--Schwarz and the relation
   w_i=(r_i(E_i)/r_i(s))*zeta_i+O(zeta_i^2) give the signs and
   constant2g-2+n in the renormalized-area deficit.
4. Zero-weight faces are valid: choose Solynin's B to be the positive
   marked points, A the remaining marked points, all other systems
   empty, and only peripheral circle homotopy classes. I independently
   opened his Theorem2.1/(2.27), printedp32, and the definitions on
   p21. The strict uniqueness clause is explicit. Poles at A have
   order at most1 and may disappear upon collision with a zero.
   The sole edit to the author's A2b file clarifies this last phrase.
   Source refs turn142272209view0, turn465666776view0/1:
   https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=1040&what=fullt .
5. On a boundary ray p>=0, the derivative upper bounds imply
   S(s0+tp)>=S(s0+t(p+epsilon*1))-t*epsilon*sum b_i.
   The support supremum proves K(p+epsilon*1)->K(p), including when
   the b_i or their sum are negative. This closes the recession step.
6. An unbounded sublevel sequence gives a normalized nonnegative
   direction p; convex segment comparison contradicts the positive
   recession slope. The closed convex extension is bounded below by
   an affine support. Along b+t*1, lower semicontinuity and convexity
   give convergence to its finite boundary value, while the uniform
   collar bound makes the inward derivative tend to minus infinity.
   Thus the minimizer is interior. The positive Hessian supplies the
   real-analytic inverse and the support inequalities describe exactly
   the logarithmic radius image.
7. In the cap-limit argument, zero-weight summands are removed using
   their upper bounds, not an unjustified lower bound. Positive
   coefficients and all other upper bounds then give a lower bound for
   each positive-weight radius. Normal families give nonconstant
   disjoint kernel limits. Strebel uniqueness identifies them, and an
   additional positive-radius zero-weight disc would be an open subset
   of the critical graph, impossible.
8. The graph Hessian sum A_v^T Hess(S_v) A_v counts both branches of
   a loop and is positive definite because every nonzero edge vector
   has a nonzero incidence image. The same coercivity and collar
   proof applies. The actual seam phases supply the full S1 variables;
   fully marked real twists require the explicitly stated quotient.
   Common length1 gives intrinsic shadow circles. Radial contraction
   to this circle bundle stays in the log-convex image, is equivariant,
   and is a common deformation retraction of the image and the full
   nonzero-tensor bundle. Thus the orbifold pi1 claim is justified.

For analytic dependence I independently inspected Mondello's actual
source sources/mondello/Triang-submitted.tex, lines3535--3541
(thm:grafting), which states a real-analytic diffeomorphism on every
finite topological stratum. Its setup explicitly permits cusp ends
(lines3494--3508; reduction at4074--4088). Smooth complex seam charts
and the normalized Beltrami parameter theorem supply the needed
parameter smoothness; the metric's C1,1 regularity is not mistaken
for C2 smoothness across the interface.

### R4/R5 final completeness audit

Re-read the exact supplied transcriptions for084--089 and091--101.
No interpreted-condition gate remains for A5/A7. The ambiguous erased
word on086 does not affect the algebraically closed projective-line
statement, and the091 corollary is independently disproved under the
weaker visible hypotheses, so no decipherment is used to rescue it.
The091 category proposition has now been broadened to arbitrary
possibly noncommutative rings and left modules, exactly as its opening
line states; central localization at2 makes the existing proof valid.
The rank-one corollary is kept over the explicitly specified
commutative rings. The100 count now also displays all three nonsplit
matrices [[1,c],[0,-1]], c=1,omega,1+omega. The topology proof uses
chi(quotient)=(chi(torus)+chi(fixed circles))/2=0 and the boundary
count, so the annulus/Mobius classification is explicit.

L7's stack and coarse descriptions descend to Z[1/2]; i is only used
for the chosen octahedral matrix model. Generic V4 inertia, bad-prime3
invariant-ring issues, and the unrelated characteristic5 six-set
exception remain separated. No characteristic2 theorem is asserted.
"""
path.write_text(value)

path = ROOT / "checks/part_a567_results.csv"
with path.open(newline="") as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
assert "A6-cyclotomic-detection" not in {r["id"] for r in rows}
new_row = {
 "id":"A6-cyclotomic-detection",
 "statement":"For smooth affine hyperbolic curves over number fields, a nontrivial geometric element lies in cusp inertia exactly when it has an open-image cyclotomic normalizer",
 "status":"Known",
 "where_proved":"sections/part_a6.tex:A6-cyclotomic-detection",
 "depends_on":"Nakamura1994 Theorem(2.1.1) and Lemma(2.1.4); Weil weights",
 "manuscript_pages":"67/049b; L6",
 "notes":"Exact full-profinite source opened and derivation written; detects elements in inertia, not a bijection for all procyclic subgroups; no automatic singular-log application"
}
rows.insert(next(i for i,r in enumerate(rows) if r["id"]=="A6-three-classes"),new_row)
for row in rows:
    if row["id"]=="A7-gluing-modules":
        row["notes"]="Arbitrary possibly noncommutative ring and left modules; 2 central; no finite-generation assumption"
    if row["id"]=="A6-anabelian":
        row["notes"]="Fixed base frame/section essential; exact source hypotheses re-read; parent reports independent review of algebraic chain; no ordinary-pi1 claim"
    if row["id"]=="A5-moduli":
        row["notes"]="Stack versus coarse scheme; characteristics3 and5 handled; both descriptions descend to Z[1/2], with i only for the chosen octahedral model"
with path.open("w",newline="") as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

events = [
("A5-faces","final proof audit","Individual face orbit has8 elements, antipodal face-pair orbit4; stabilizers C3 and S3, latter complementary toV4."),
("A6-kummer","final proof audit","Normal projective model reduces infinite divisibility to the constant number field; all valuations and the finitely generated unit group separate1."),
("A6-graphic","exact source-hypothesis audit","Mochizuki2007 Definition2.3 and Cor2.7(ii) re-read; Q-cyclotomic terminology corrected; associated-weight argument checked on every characteristic cover."),
("A6-normal-kummer","exact source-hypothesis audit","HM2012 Def4.4 Prop4.5 Thm4.8(iv),(v) Prop4.10(ii) Lem5.4 Thm5.7 re-read; arbitrary graph loops included; apply monodromy overKbar[[t]]."),
("A6-anabelian","arithmetic extension and global tangential audit","Vertex self-normalizer fromMoch2007 Prop1.2(ii), centre-free extension pullback, full-profinite Moch1999 clause, and normal-torus chart descent made explicit."),
("A6-cyclotomic-detection","opened exact theorem and derivation","Nakamura1994 Thm2.1.1/Lem2.1.4 pp94-97 opened; finite-cover mod-l obstruction plus Weil weights supplies the precise smooth-curve criterion."),
("A6-log-specialization","parent independent review reported","Parent explicitly reports checking RIMS1558 Cor3.9 pp31-32 and PropA.10 pp57-58 and agreeing with the characteristic-zero application."),
("A6-SNC-existence","parent independent review reported","Parent explicitly reports independently reading Temkin1.1.15 and agreeing with the stated application."),
("A6-canonical-compactification","parent independent review reported","Parent reports independently checking the log-pluricanonical weak-factorization calculation; universal ample-SNC existence remains excluded."),
("L6","additional primary sources opened","Nakamura1994 full proof and NTM2001 author survey opened; IharaNakamura1995 announcement opened with exact theorem scopes; originals1990/1997 not falsely marked read."),
("A5-moduli","final base audit","The quotient stack and invariant ring descend toZ[1/2]; adjoining i serves the explicit octahedral representation, and characteristic3 uses no averaging."),
("A7-gluing-modules","exact transcription scope correction","091 allows noncommutative rings; statement broadened to left modules over any ring, proof using central2 unchanged."),
("A7-PID-count","explicit representatives and completeness audit","Added the three matrices with c=1,omega,1+omega and checked their eigenlattice/gluing residues; no remaining count proviso gate."),
("A7-real-topology","formal topological classification audit","Boundary is fixed circles; quotient Euler characteristic0 gives annulus orMobius, while free orientation-reversing quotient isKlein bottle."),
("A2b-regularity","independent source and proof review","Read Mondello actual theorem finite-stratum real-analytic diffeomorphism, including cusp zeros; checked smooth seam charts versus metric C1,1."),
("A2b-energy","independent re-proof","Re-derived cap variation, seam-jump sign, both Green identities, positive energy, and mixed-variation symmetry; no gap found."),
("A2b-recession","independent re-proof and source check","Collar coefficient bound and zero-weight recession sandwich checked; Solynin2.1 includes at-most-simple zero-weight poles."),
("A2b-image","independent re-proof","Bounded sublevels by normalized escape direction; lsc boundary limit and minus-infinite inward derivative; positive Hessian gives analytic inverse."),
("A2-strebel-deficit","independent re-proof","Nonexpanding cylinder collapse, peripheral length minimum, annular CauchySchwarz and reduced-area signs give exact constant2g-2+n."),
("A2-cap-limit","independent re-proof","Positive-weight radii bounded below, disjoint nonconstant kernel limits attain unique Strebel maximum; empty-interior graph forces zero-weight collapse."),
("A2-explicit-limits","independent calculation review","Checked Koebe map pullback and derivative4; three-pole equal-weight graph and lune conformal radius4/(3sqrt3)."),
("A2-nonbox","independent proof review","Two-weight Strebel half-planes have radii1; strictness by collars and individual Koebe suprema exclude a Cartesian product."),
("A1-graph-range","independent re-proof","Loop branches counted twice; incidence-Hessian positive definite; convex image and intrinsic common-circle equivariant deformation retraction checked."),
("A1-small-ranges","independent proof review","Supports give exact0<|q|<16 for separating0-4 and0<|q|<1 for irreducible1-1, with all phases.")
]
path = ROOT / "checks/part_a567_events.tsv"
with path.open("a") as stream:
    for ident,kind,outcome in events:
        stream.write("\t".join([ident,"2026-11-19","GPT-6 Astra (OpenAI), part_a567, this run",kind,outcome])+"\n")

labels = set()
texts = []
for name in ("part_a5.tex","part_a6.tex","part_a7.tex"):
    value=(ROOT/"sections"/name).read_text()
    texts.append(value)
    labels.update(re.findall(r"\\label\{(A[567]-[^}]+)\}",value))
result_ids={r["id"] for r in rows}
event_ids={line.split("\t")[0] for line in path.read_text().splitlines()[1:]}
bib=(ROOT/"sources/part_a567.bib").read_text()
bib_keys=set(re.findall(r"@\w+\{([^,]+),",bib))
cites=set()
for value in texts:
    for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}",value):
        cites.update(group.split(","))
assert labels==result_ids, (labels-result_ids,result_ids-labels)
assert labels<=event_ids, labels-event_ids
assert cites<=bib_keys, cites-bib_keys
print("Numbered A5-A7 statements:",len(labels))
print("Every statement has a result row and at least one event row.")
print("All",len(cites),"citation keys have bibliography entries.")
print("Independent A1/A2 review events added:",sum(e[0].startswith(("A1-","A2")) for e in events))
print("Original inaccessible sources retain their not-opened status.")
