# Cote 136: further routes inspected in this run

Recorded by root, GPT-6 Astra Pro, effort not exposed, 2026-11-21.
This note records research attempts and source scope. It is not an additional
proved reduction of the original integral question.

## Arithmetic gluing attempt

The checked p-local constructions do not immediately spread to a finite
principal-open cover of Spec Z. Their coefficient lattices use infinitely
many integers which are units away from a fixed prime. Inverting a single
finite integer does not invert all of them. A separate finite-presentation
argument for every stage would need compatible transition maps and the
uniform-in-simplex bounds of the original admissibility condition.

An infinite product of the local constructions does not solve that
uniformity problem. The local truncation cutoff can grow with the prime;
at a fixed weight, a local model whose cutoff is larger than that weight
still retains the constant coefficient row. The fact that only finitely
many primes divide the factorials in each fixed weight is therefore not,
by itself, a proof of one uniform admissible global presentation.
No global source or common target has been obtained by this attempt.

## Positive-degree relative cells

A finite linear staircase gives an absolute weightwise bicomplex with
vertical cohomology k in degree zero and acyclic horizontal rows through
any prescribed finite form degree. Explicit recursive horizontal
primitives can map it to each target once the required target rows are
acyclic. The missing step is an actual relative strict PD extension of
the already constructed algebra, with compatible simplicial maps and
uniform bounds, while retaining the coefficient H0 and both target maps.

A pointwise torsion-pair repair can create a new degree-zero cycle with
different coefficient residues in two targets. That observation alone
does not establish an obstruction in the simplicial category: the
putative differing constant residue may fail the simplicial identities.
No general relative existence or nonexistence theorem is claimed.

## Literature route and exact scope

Guillén Santos, F., Navarro, V., Pascual, P., & Roig, A. (2008).
Monoidal functors, acyclic models and chain operads. *Canadian Journal
of Mathematics, 60*(2), 348–378. https://doi.org/10.4153/CJM-2008-017-7

The published primary PDF was inspected at §9.1 and Theorem 9.2,
pp. 373–374; the preceding acyclic-models theorem is Theorem 8.1.
The version-dependent theorem numbers must not be taken from the
preprint without translation. The comparison furnished there is a weak
comparison in a category of contravariant monoidal functors. It does not
by itself supply a common source in the present strict, weight-graded
PD category. The whole proof of this external theorem was not checked
in this run, and it has not been promoted as a new finding.

Cartan's 1976 *Théories cohomologiques*, *Inventiones Mathematicae, 35*,
261–271, DOI 10.1007/BF01390140, was located bibliographically. The
complete primary article was not retrieved. No theorem number or
purported uniqueness conclusion from it is treated as verified.
The scanned/transcribed lecture-plan material in *Unpublished Works*
edited by Mateo Carmona, pp. 51–55, discusses divided powers and
semisimplicial ideas but did not supply a verified solution or an exact
new archive cote. It has not generated a new question row.

## Prior-work reconciliation

The supplied `INTAKE_RESEARCH_SA08_C3_D031_20261120.md` explicitly
reports substantial prior work on these routes. Its Part A proofs were
not supplied, and the intake itself describes its reading as statement
level rather than complete proof checking. In particular:

- A-S09-26 reports the tensor/Hadamard prime-power row-zero obstruction.
  AQ-136-TENSOR is a complete proof checked in the present run of the
  tensor assertion; no novelty is claimed, and the stronger unseen
  Hadamard-closure assertion is not certified by that proof.
- A-S09-29 and A-S09-30 report countable-category gates for common sources
  and terminal localization. Their full proofs remain unavailable here.
- A-L05, A-L07, AT12, AT27–29b and A-S09-31 report bar constructions,
  failures of primitive lifting or strict truncation, and specified
  finite-degree repairs. They inform route selection; they are not
  silently substituted for a proof of the all-simplex integral gate.
- The intake's arithmetic-gluing discussion already identifies the need
  for compatible local repair depths tending to infinity with the prime.

Thus the new route audit changes neither integral question's status.
The checked rational, p-local and positive-characteristic results and
the separately checked counterexamples retain their explicitly stated
scope.

## Cenkl–Porter obstruction: checked scope, 2026-11-21T04:40:28.356317+00:00

Cenkl, B. (1989). Cohomology operations from higher products in the de Rham complex. *Pacific Journal of Mathematics, 140*(1), 21–33. https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf

Root read the definition in section 5, printed p.31, and Theorem 2 with its full proof on pp.32–33, including direct visual inspection of all three pages. The theorem addresses an unweighted, naturally commutative cochain functor computing ordinary R-cohomology; its conclusion is a²∈2R for every a∈R. The cup-one calculation rules out this unweighted problem over the integers. It supplies no uniqueness theorem or strict common-source construction for the present weighted divided-power category, and it does not refute the checked weighted standard model. No claim of all-prime divisibility or a Q-algebra conclusion is taken from this theorem. The article credits the result jointly to Cenkl and Porter.

The earlier repeat search for Cartan1976 reached the publisher and EuDML bibliographic entry but not its full text. A further official Göttingen digital-volume route is now being inspected; no conclusion from Cartan is used before its actual pages have been read.

## Cartan recovery and operation route: 2026-11-21T05:07:58.158988+00:00

The earlier nonretrieval status above is superseded. The complete official article was recovered at https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0035/LOG_0030.pdf. Physical1 is the repository cover; physical2–12 are printed261–271. Archive_questions visually read the entire article, and root directly inspected printed261,262,266,267. Cartan's section4 defines linear simplicial cochain maps without multiplicativity; Theorem2p266 is an integration theorem. Theorem3p267 gives multiplicativity under cycle-module flatness. It does not prove strict PD common sources. AQ-136-CARTAN-SCOPE records the exact limits.

The subsequently whole-checked AQ-136-MULTIPLICATIVE removes flatness for the cohomology product via cycle spaces and integral smash Kunneth. AQ-136-PD-RIGIDITY identifies fixed divided-power operations over the integers for all X, using finitely many local common sources and universal-space finite homology. Root directly read HatcherSSAT Lemma1.10 and complete proofpp15–16. The operation route therefore does not distinguish integral components in this scope; it neither proves their connectedness nor the absence of localization loops.

## Infinite arithmetic gluing test — 2026-11-21T05:28:39.927796+00:00

Root reread the entire p-local construction and the finite semilocal arithmetic gluing proof. The naive choice of B_(p^e) at every prime cannot be the family of local targets of one integral admissible source. Here is the complete obstruction: suppose E is integral admissible and for every prime p there is a coefficient-preserving strict map E tensor Z_(p) → B_(p^e), with e≥1. Choose w beyond the global form-zero horizontal acyclicity cutoff, then p>w. Since p^e>w, the target weight-w form-zero row is exactly constant Z_(p) T^[w]. The coefficient cycle of E in this row is a horizontal boundary because H0(E^(w,0))=0. Flat localization preserves this, and a simplicial linear map sends a boundary to a boundary. Its image would be the nonzero constant coefficient T^[w] in the target, whose H0 is Z_(p), contradiction. The same proof applies to any unbounded sequence of such local N with coefficient rings Z_(p).

This is an obstruction only to these prescribed local standard models. Actual fixed targets C,D have one global horizontal cutoff, and need not share this incompatible low-weight behavior. Thus the argument does not refute integral common-source existence, and is not counted as an original-gate reduction. Replacing the large-prime low-weight pieces, and then retaining compatible strict maps and a uniform cutoff, remain necessary steps for this route. Root read this complete argument after writing it; no formal certificate is claimed.
