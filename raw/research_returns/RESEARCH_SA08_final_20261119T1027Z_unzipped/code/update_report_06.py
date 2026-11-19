"""Refresh checkpoint 06 after explicit approval of the integrated paper."""
from pathlib import Path
import json, runpy

root = Path(__file__).resolve().parents[1]
runpy.run_path(str(root/'code/update_report_05.py'), run_name='__main__')
path = root/'RESEARCH_SA08_report.md'
text = path.read_text()
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('| C.3 |'):
        lines[i] = ('| C.3 | Not fully settled; finite-prime case proved | '
                    'C17 proves common sources and terminal localization for finitely many noninvertible rational primes. C30 and C32 give a conditional reduction for arbitrary k to compatible local repairs preserving increasing form-degree ranges, for pair and homotopy-equalizer targets. Those repairs are unproved; Z is still the smallest unsettled base. C31 refutes automatic prescribed bar-boundary extension. |')
text = '\n'.join(lines) + '\n'
text = text.replace('output A_t0_sphere2.json, 26 vectors inspected.',
                    'output A_t0_sphere2.json, 26 vectors inspected; 0.000018 seconds.')

marker = 'Source download, source inspection, OCR, registry consolidation, and packaging scripts are also retained.'
extra = '''Additional mathematical computations completed before checkpoint 06:

- B_bar_arity3_checks.py: the three exhaustive multiplicity patterns aaa, aab and abc, with exact integral differential matrices, chain identities, unimodular basis changes and minor certificates; 0.037688 seconds. C25 proves the actual arity-three extension, including compatibility with prescribed lower arities.
- D_bar_indecomposables.py: five partitions in arity four, 0.018298 seconds; eighteen partitions in arities five and six, 2.240594 seconds; six rank-one cases in arities seven through twelve, 0.209524 seconds. The receipts retain every basis, differential and computed invariant. These finite computations do not assert an all-arity concentration theorem; D032 explicitly refutes the proposed concentration pattern.
- D_bar_mixed_counterexample.py: eight exact checks, 0.020161 seconds. The complete arity-six, multidegree a²b⁴ certificate includes the 11-by-3 incoming matrix, the 18-by-11 next differential, the integral cycle, a doubled boundary and the parity detector. The resulting Z/2 class is a statement about PD indecomposables, not an asserted nonzero target obstruction.
- C_bar_boundary_countercheck.py: two complete normalized complexes for the exterior and tensor squares of K(Z,2), with their face matrices, chain identities, alternating inclusion and exact minor certificates; 0.079041 seconds. The exterior differential has determinant minus two and a unit two-minor, while the tensor differential has primitive image in the required kernel. C31 verifies an actual failed prescribed extension in an admissible Z_(2)-target; it does not refute C3.
- D_pd_cancellation_warning.py: fifteen exact assertions at primes two, three and five, 0.000014 seconds. These check the residual divided-power torsion after the specified naive generator-pair cancellation. The complete receipt and the failed-route analysis are retained; no new general cancellation theorem is inferred.

'''
start = 'Additional mathematical computations completed before checkpoint 06:'
if start in text:
    a = text.index(start); b = text.index(marker, a); text = text[:a] + extra + text[b:]
else:
    text = text.replace(marker, extra + marker)

source_marker = '## Computation record'
source = '''The subsequent source audit opened Dokas–Frankland–Ikonicoff, arXiv:2403.18049v3, Section1, Definition2.6, Example2.9 and Theorem8.2 with its proof; and Kmail–Kozak–Miller, arXiv:2502.05956v2, Sections3–6, especially Lemma5.2 and the distinction between Beck abelianization and the quotient by products and higher divided powers. C26 does not confuse arbitrary triangular differential PD resolutions with genuine cofibrant simplicial resolutions. The arXiv source endpoints were attempted but unavailable; the inspected primary HTML versions and failed fetches are recorded. Sullivan's author-hosted 1970 MIT notes, edited in2005, were opened at Chapter1, Propositions1.17–1.18 and their proofs, printed pp28–30. Their classical completion arithmetic square supplies context; C30 proves the localization-product variant needed here in full. No priority is claimed.

'''
if source not in text:
    text = text.replace(source_marker, source + source_marker)

a = text.index('C.3: special universally flasque theories')
b = text.index('\n\nL7:', a)
gate = '''C.3: special universally flasque theories have contractible nerve; strict common-source equalization is false over every nonzero base. C16–C17 prove common sources and terminal localization for every coefficient ring with finitely many noninvertible rational primes, including the flat-term category and optional q≤w support. Rings with infinitely many noninvertible primes remain undecided, beginning with Z. Common sources and terminal localization remain distinct requested assertions.

The excluded constructions are recorded precisely. Ordinary tensor products have prime-power Tor in unbounded weights (C11). Independently marked free PD disks over Z fail except for the ordinary weight-one disk (D022–D023). Projection-preserving arithmetic gluing with unbounded first flasque weights is impossible (C12). Standard tails are not an initial comparison family (C13). Free linear-disk replacements and free resolutions of coefficient tails have the distinct obstructions in C14–C15. Arbitrary ordinary common-target pushouts can create unbounded degree-one cohomology even rationally (C19). These refute specified constructions, not global uniqueness.

D027–D028 prove the first-row nonfree-image eventual bound and a finite integral H3 class; no higher eventual bound follows from their computations. C18 gives delayed p-local nonlinear closures without compatible target maps. C21 constructs a common global partial model P with free terms, uniform horizontal bounds, correct H0 and a vertical comparison through degree d after inverting floor((d+1)/2)!. It is not claimed admissible integrally. C20's nonzero possible obstruction group is distinguished from C22's actual second quadratic map, which has a simultaneous strict repair.

D029 and C24 give the positive integral bar closure and its relative semifree base-change property. D030 and C25 give the first two actual prescribed extensions. C27 proves every finite-arity extension for K(Z,2), with arbitrary lower choices fixed; C28 gives coordinated absolute finite-arity extensions for general parameters by passing through a contractible free cover. C29 proves a relative extension theorem under its stated dimension bound. None of these supplies one weight meeting infinitely many eventual target bounds or an arbitrary prescribed full boundary. C26 refutes invariance of naive PD indecomposables under arbitrary triangular free differential PD resolutions; D032 refutes a proposed simple arity-homology concentration pattern.

C31 now gives an actual counterexample to automatic prescribed bar-boundary extension, inside an admissible flat Z_(2)-theory. Its obstruction is the failure of the alternating inclusion Λ²K(Z_(2),2)→K(Z_(2),2) tensor K(Z_(2),2) to split. The target is the explicit truncated parameter disk tensored with G4; every admissibility hypothesis is verified. The example concerns a specified low-weight map and is compatible with the proved local uniqueness theorem.

C30 proves conditional infinite arithmetic descent for common sources. For every prime p it assumes an admissible factorization P_p→E_p→A_p,B_p whose first map is an isomorphism in all weights and simplices below a form-degree bound d_p, with d_p tending to infinity. A finite-idempotent repair over R=product_p Z_(p), the pure exact arithmetic sequence, simplicial paths and a mapping-path pullback then give an actual admissible common source over arbitrary k. The flat conclusion here is proved over Z, not asserted for arbitrary base rings.

C32 extends the reduction to terminal localization, with two explicit local repair hypotheses: one for the pair target A×_k B, and one for the homotopy equalizer H(f,g). The latter target has constant eventual vertical cohomology S in degrees zero and one, so it is not silently treated as admissible. The relative-prism hypercohomology comparison extends the arithmetic replacement to these targets. The resulting actual homotopy refinements make parallel maps equal in the localization; common sources then contract every finite zigzag loop. This proves both global assertions if the specified local repairs exist. Neither repair family has been constructed, and no equivalence between this sufficient repair hypothesis and the original conjecture is asserted.

The outstanding constructive task is therefore to produce these compatible local extensions with increasing preserved form-degree ranges, or obtain a different proof or counterexample to C3. The arithmetic and loop arguments are proved conditional tools; they do not change the requested C3 status. At the formal review of09:21 UTC there was no qualifying movement, giving one consecutive no-movement review. The next formal review is due10:21 UTC. It will assess whether the conditional reduction is a strictly smaller gate under the user's rule; no reset is assumed merely from adding results or packaging.'''
text = text[:a] + gate + text[b:]

q = text.index('## Typesetting status')
r = text.index('## Proved obstructions, approaches and remaining gates', q)
section = text[q:r]
section = section.replace('The approved current LuaLaTeX build has ',
    'Build31 exposed a missing display delimiter in D032, which was fixed. Duplicate equation destination warnings were removed by using unique hyperref destinations, and a mathematical bookmark warning in C27 was corrected with an explicit text alternative. Builds34–35 exposed incompatible paragraph-heading breaks in the two new long proofs; explicit bold paragraph labels corrected them. The final build was checked for these warnings as well as overflows and unresolved references. The approved current LuaLaTeX build has ')
text = text[:q] + section + text[r:]
path.write_text(text)
print(json.dumps({'report':path.name,'checkpoint_update':6,
                  'remaining_requested_rows':['C.3','L7'],
                  'formal_no_movement_reviews':1,
                  'next_review_utc':'2026-11-19 10:21:00'}, indent=2))
