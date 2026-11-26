# Brief: prove or refute a reduction of the Hodge conjecture for abelian varieties

22 November 2026, for an expert who didn't write it. Don't open `SEED_HODGE_DIVISION.md`, the bridge files, the
HODGE_DIVISION returns or their intakes: the check is worth something only if your argument is your own.

Sub-agents allowed: 0
Compute bound: no calculation over 5 GB or 20 minutes; about 120k tokens of work in all.
Notes: keep `agent_notes/<your agent id>_NOTES.md` updated after every step.

## The statement

A special family with a Hodge class (S, θ, t): a connected smooth Shimura variety S with a map to A_(g,N), N ≥ 3, the
pulled-back family of principally polarized abelian g-folds, and a global section t ≠ 0 of R^(2p) f_* Q(p) of type
(p,p) at every point. For s in S, c_t(s) is the least max(M, deg_θ Z^+, deg_θ Z^-) over integers M ≥ 1 and effective
integral cycles with M t_s = [Z^+] − [Z^-]; it is infinity if there are none.

Claimed equivalent:
1. the rational Hodge conjecture holds for every complex abelian variety, in every codimension;
2. in every such family c_t is bounded on the CM points;
3. in every such family there is D such that, for every CM point x and a model over a number field, at infinitely many
   places v the reduction of t_x equals ([Z^+] − [Z^-])/M in ℓ-adic cohomology over the algebraic closure of k(v),
   ℓ prime to v, with effective integral cycles of degree at most D, M unrestricted.

Also claimed: in (2) any one Zariski-dense set of points may replace the CM points; in (3) the places may be required
to lie in any prescribed infinite set of good places; and only published inputs are needed.

## What to do

Try to refute each implication first. In particular: non-principal polarizations and varieties not defined over number
fields; whether every Hodge class really lies in such a family; whether ℓ must be fixed for each x or may vary with v,
given that independence of ℓ of homological equivalence is open in characteristic p; unbounded M; vertical components
of cycle schemes; descent of cycles and degrees; Baire against countable fields. Then give your own proof, or the exact
point that fails, and the exact repaired statement.

Write `reports_20261122/hodge_reduction/INDEPENDENT_CHECK.md`: a verdict on each implication and rider, your proof,
each cited theorem with its locator and whether you opened it, and check events. Report the verdicts in under 200
words. No git, upload, e-mail or post. Don't send the statement to any search.
