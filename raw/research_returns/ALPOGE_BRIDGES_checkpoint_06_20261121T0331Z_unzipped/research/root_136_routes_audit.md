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
