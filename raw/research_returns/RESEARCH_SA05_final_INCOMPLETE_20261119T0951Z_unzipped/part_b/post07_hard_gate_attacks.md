# Part B: attacks after checkpoint 06 and the simply-connected reduction

## 2026-11-19, 07:48–07:53 UTC: individual versus universal Parshin input

We re-read the complete proof of Geisser (1998), Theorem 3.3, printed
p.117, together with Propositions 3.1–3.2 on pp.115–116, from the
previously opened primary PDF. Its hypothesis says that numerical and
rational equivalence agree **over finite fields**, and its conclusion
quantifies all smooth projective varieties. The proof factors higher
Adams eigenspaces through numerical motives and decomposes into simple
motives. This requires control of the endomorphism correspondences; it
does not follow merely from equality of ordinary Chow groups on one X.

We also re-read Kahn (2003), Theorem 1.10, Corollary 2.2 and its complete
explanation, printed pp.982–983. Corollary 2.2 assumes X belongs to
B_tate(k), the class of abelian-type Chow motives satisfying Tate. Its
explanation uses simple motive factors of h(X), exactly the additional
control supplied by Kimura nilpotence in that class. Although its
parenthesis abbreviates the hypothesis as Tate and Beilinson for X,
this is not a separate theorem for arbitrary X without that motivic
scope.

Gregory (arXiv:2302.09867v2), Remark 1.1, pp.1–2, phrases the implication
for an individual X and cites those two results. The published
introduction at the publisher URL below repeats that formulation.
The cited proofs do not establish the stronger pointwise implication
with only the ordinary Chow groups of X controlled. We have neither a
counterexample to that implication nor a proof of it; we therefore
record a gap in this proposed deduction, not a refutation of the
implication. In particular, the newly proved surface-support and
uniruled-threefold ordinary Chow equalities are not silently promoted
to Parshin vanishing or the full Weil-etale comparison.

Exact sources: Geisser,
https://www2.rikkyo.ac.jp/web/geisser/Tate_KtheoryJournal.pdf;
Kahn, opened local primary `primary_sources/part_b/kahn2003.pdf`;
Gregory, https://arxiv.org/pdf/2302.09867 and
https://www.sciencedirect.com/science/article/pii/S0022404923002001.

## 2026-11-19, 07:50–07:54 UTC: new localizing-invariant result

Opened the primary arXiv HTML of Jakub Loewit, *Equivariant localizing
invariants of simple varieties*, arXiv:2507.09392v2 (17 April 2026),
published IMRN 2026(7), rnag058, DOI 10.1093/imrn/rnag058:
https://arxiv.org/html/2507.09392v2.
Read Definition 1.3, Theorem 1.19 and its full proof, Theorem 2.18 and
Example 2.30 with its proof. The hypothesis is membership in a specific
class generated from points by projective-bundle operations and split
abstract-blowup descent. The proof yields rational K-vanishing for that
class through the explicitly proved KH formality. It supplies no
reduction of an arbitrary smooth projective threefold to that class.
Thus it does not remove the codimension-two threefold Chow gate or the
motivic phantom gate. No assertion that every variety is 'simple' is
made. The publisher endpoint failed, but the full primary author
version was actually opened and read in the stated scope.

## 2026-11-19, 07:54–07:58 UTC: field-extension nilpotence is not numerical nilpotence

Searches for Rost nilpotence on finite-field threefolds found Diaz,
*Rost nilpotence and higher unramified cohomology*, Advances in
Mathematics 355 (2019), 106770, DOI 10.1016/j.aim.2019.106770,
arXiv:1807.08163v3. Although the web PDF endpoints failed, local
retrieval obtained the complete primary PDF. We read Conjecture 2.2,
Lemma 2.3 and its full proof, Theorem 2.4 and its full proof, and
Corollary 2.5 with its proof, pp.11–13. Lemma 2.3 says that a cycle
becoming zero after a field extension is torsion. Consequently the
field-extension kernel on rational Chow groups is already zero.
Rost nilpotence therefore does not say that a numerically trivial
rational correspondence is nilpotent: numerical vanishing supplies no
field extension on which the correspondence becomes rationally zero.
This route cannot kill the rational numerical phantom. The source's
later threefold arguments are not used as a theorem on numerical
nilpotence, and no independent audit of every later nilpotence argument
is claimed.

## 2026-11-19, 07:54–08:00 UTC: generic motives and coniveau

Opened the full primary author HTML of Frédéric Déglise, *Generic
motives and motivic cohomology of fields*, arXiv:2408.06233v3,
https://arxiv.org/html/2408.06233v3. The publication is Indagationes
Mathematicae 37(1), 421–487 (2026), DOI 10.1016/j.indag.2025.07.006.
The publisher download was only a 195-byte unavailable-page stub and
is explicitly logged as not obtained; the author HTML was obtained.
Read Proposition 4.2.2 (whose proof refers to a separate earlier
source), full Corollary 4.2.4 and Proposition 4.2.5 proofs, Remark 4.2.6,
Conjecture 4.2.7, full Proposition 4.4.1 proof and Remark 4.4.2, and
Conjecture 5.2.6 with §§5.2.7–5.2.11. Closed-point residue fields in the
generic P¹ decomposition include arbitrary finite extensions. The
higher-transcendence extensions are explicitly nontrivial; the needed
general generation assertion is Conjecture 4.2.7, and positive-characteristic
vanishing in §5.2.11 assumes Beilinson–Parshin. None is an unconditional
dimension reduction of the B1 phantom.

Opened Scavia–Suzuki, *Two coniveau filtrations and algebraic equivalence
over finite fields*, arXiv:2304.08560v2,
https://arxiv.org/pdf/2304.08560v2. Read Theorem 1.2 and its full proof
on p.27, Theorems 1.4–1.5 and their full final proofs on p.29, and the
introductory Question 1.6. Theorem 1.2 assumes equality of integral
coniveau and strong coniveau on H³. Its conclusion controls algebraic
equivalence and specified torsion; it does not prove all rationally
homologically trivial codimension-two cycles algebraically trivial.
The integral surjectivity and unramified-H³ statements likewise do not
prove the injectivity needed by B1. Earlier lemmas cited in the final
proofs were not all independently rechecked. The universal gate is
unchanged.

## 2026-11-19, 07:56–08:00 UTC: an explicit limit-order counterexample

The standalone `kummer_limit_counterexample.md` proves an explicit
failure of exchanging the open-subscheme colimit with the continuous
3-adic inverse limit, already in degree one for P¹ over F̄₂. Its omitted
class is Frobenius invariant and remains omitted after tensoring with
Q₃. The note includes the entire infinite-support proof; a finite exact
polynomial/congruence certificate is saved separately with code and
output. This is a diagnostic of a proposed symbol argument, not a
counterexample to the degree-four projective-space gate.

Opened Jannsen, *Continuous étale cohomology*, Mathematische Annalen
280(2), 207–245 (1988), DOI 10.1007/BF01456052, from the primary repository:
https://epub.uni-regensburg.de/26684/1/jannsen12.pdf.
Read the continuous definition and exact sequence (3.1), pp.216–217,
Theorem 3.2 with full proof, p.217, and the inverse-system Kummer sequence
(3.27) with Lemma 3.26 and its proof, p.222. Surjectivity on the degree-zero
roots-of-unity system removes lim¹ in this particular example; no
general colimit/limit commutation is inferred.

## Current gate and next attempt

The B1 gate is unchanged: under universal Tate and eigenvalue-one
semisimplicity, prove the stated cycle injectivity in codimension m on
dimension 2m-1 for all m>=2; the first case is codimension two on a
threefold. Its projective-space cohomological equivalent must retain
continuous cohomology and its limit order. The next attempt examines
whether generation by symbols or coniveau descent supplies a real
dimension reduction; no such reduction is being assumed.

## 2026-11-19, 08:04–08:17 UTC: the exact endomorphism hypothesis and two rigidity routes

Opened Kahn, *The full faithfulness conjectures in characteristic p*,
https://webusers.imj-prg.fr/~bruno.kahn/preprints/full-faithfulnessIHES7.pdf.
The primary title page is dated **19 September 2012**; search metadata
that made the file look recent is not its publication date. Read
Theorem 8.0.2 and its entire proof, author pp.30–32. The exact assumption
is Beilinson in codimension d on **X×X**, where d=dim X, together with
cohomological Tate in codimension n on X. The first assumption identifies
End(h(X)) with its semisimple numerical algebra. The decomposition into
simple summands then has two cases. A Lefschetz summand L^n has no
higher rational motivic cohomology over the finite field. On every other
summand S, Tate excludes a Frobenius-q^n realization; central Frobenius
minus q^n is nonzero in its division algebra, hence invertible, whereas
it acts by zero on H^i(S,Q(n)). This kills that group. If H^(2n)(S)=0,
the same exclusion uses the weight theorem and the fact that a nonzero
simple summand has nonzero realization: a realization-zero idempotent
is numerically zero and the assumed endomorphism equality makes it
rationally zero. Thus the precise theorem confirms the missing
endomorphism premise in the pointwise attempted argument; it does not
turn the ordinary threefold result into Parshin.

Opened Richarz–Scholbach, *Frobenius rigidity in A¹-homotopy theory*,
Documenta Mathematica 30, 219–244 (2025), DOI 10.4171/DM/988,
https://ems.press/content/serial-article-files/49857.
Read Definition 1.1, Theorems 1.3 and 1.5, Corollary 5.11 with its proof,
Corollaries 5.13 and 5.15 with their proofs, and the full weight-at-most-one
argument: Lemma 5.19, Corollary 5.20, Lemma 5.21, Proposition 5.22,
Proposition 5.24, Theorem 5.17 and Corollary 5.26, printed pp.233–241.
The full cellular Theorem 5.5 proof and every external theorem in these
proofs were not separately rechecked. The cellular result applies to
the K-theory spectrum but does not make M(X) cellular for arbitrary X.
Its absolute-Frobenius field computation is distinct from the partial
Frobenius acting only on coefficients of X. The latter is proved in
weights at most one; the introduction, p.222, explicitly identifies the
uncontrolled cokernel for weights at least two. Thus it does not remove
the first CH² threefold gate.

Opened the complete primary HTML of Ruimy–Tubach–Wolf, *Pro-étale
motives and solid rigidity*, arXiv:2601.07358v1 (12 January 2026),
https://arxiv.org/html/2601.07358v1. Read the complete introduction and
the stated Theorems A–E, including the embedding and coefficient-ring
qualifications. This is a **statement and framework scope audit**, not
an independent check of all the technical six-operation and solidification
proofs. Its realization has completed/solid topological coefficients;
the introduction explicitly distinguishes this from an equivalence of
ordinary rational motives and their realizations. The stated rigidity
does not imply faithfulness on rational Chow groups, and no such claim
is attributed to the source. This route therefore leaves B1 and B5
unchanged.

## 2026-11-19, 08:15–08:18 UTC: finite Frobenius orbits do not control completed eigenvalues

The note `frobenius_completion_counterexample.md` gives a second exact
diagnostic. The torsion-free discrete module C_lc(Z₃,Z), with translation
Fh(x)=h(x+1), is locally finite under F and has no eigenvalue4 after
tensoring with Q. Its 3-adic completion is C(Z₃,Z₃) and contains the
nonzero eigenfunction4^x. A direct valuation calculation gives compatible
finite representatives; code and complete output are saved. This
blocks the proposed inference from finite coefficient-field orbits of
Milnor symbols to the absence of a q-eigenvector after completion.
No identification of this module with a motivic group is asserted.

The possible restriction to canonical cyclic covers was considered but
not counted: a generically finite pullback/trace could encode arbitrary
X in a high-degree general-type cover, leaving precisely the same
uncontrolled Chow kernel. Root directed that it not be treated as a
new mathematical obstruction reduction. No main statement was changed.
