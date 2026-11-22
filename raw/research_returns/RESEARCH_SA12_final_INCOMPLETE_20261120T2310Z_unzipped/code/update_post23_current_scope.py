"""Update current outcome qualifications; retain all three requested open rows."""
from pathlib import Path
from datetime import datetime, timezone
import json
root = Path(__file__).resolve().parents[1]
path = root / 'code/assemble.py'
s = path.read_text()
marker = "report=['INCOMPLETE'"
assert marker in s and 'post23_global_scope=' not in s
addition = """post23_global_scope='; unrestricted-period projective representations satisfy q^(C r²) for every fixed normal proper surface minus finite points, with the stated all-dimensional finite-puncture, controlled-centre and finite-normalization closures; every defining-characteristic Lie simple-product quotient is finitely generated in this scope'
post23_global_labels='D:different-Frobenius-invariant-lattice; D:finite-puncture-detecting-curve-local-types; D:curve-integral-unit-jet-comparison; D:curve-fixed-local-linear-growth; D:curve-fixed-local-projective-growth; D:global-finite-puncture-projective-growth; D:global-projective-finite-puncture-closure; D:global-unrestricted-projective-simple-products'
outcomes=[(item,state+post23_global_scope,locator+'; '+post23_global_labels) if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
post23_alternating_scope='; selected alternating multiplicities have polynomial simple-order bounds when the square-sum of whole completed-local orbit sizes is O(n log(n+1)), after omitting orbits factoring through fixed finitely generated local quotients, in particular arbitrary nilpotent-image orbits; unrestricted alternating factors and general crowns remain open'
post23_alternating_labels='D:local-permutation-orbit-energy; D:finite-puncture-local-orbit-factorial-count; D:fixed-local-quotient-alternating-count'
outcomes=[(item,state+post23_alternating_scope,locator+'; '+post23_alternating_labels) if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
"""
s = s.replace(marker, addition + marker, 1)
old = 'Nonabelian crown multiplicities, alternating factors, projective linear or unitary families with unbounded natural centre and nonzero geometric Brauer class in the newly covered global normal surface setting, uncovered cross-characteristic Lie families with order divisible by p, and the remaining semilinear Lie cases require geometric control;'
new = 'General nonabelian crown multiplicities, alternating factors outside the proved whole-local-orbit criterion, original divisorial-boundary projective representations at unbounded geometric period, uncovered cross-characteristic Lie families with order divisible by p, and the remaining semilinear Lie cases require geometric control;'
assert old in s
s = s.replace(old, new)
new_report = [
    'After checkpoint23, one complete global projective reduction is proved. A fixed geometric-generic curve detects all original covers and restricts at its marked points from fixed original completed-local groups. The different-based lattice estimate and all-ring fixed-local-type curve presentation give a uniform quadratic projective count for each retained tuple. The arbitrary-SNC local projective count then bounds the tuples and yields q^(C r²) for every fixed proper normal surface minus finitely many points, without bounding geometric Brauer period. Fixed detecting surfaces and finite normalization give the stated higher-dimensional and nonnormal closures. Every defining-characteristic Lie simple-product quotient is therefore finitely generated in this scope. All ten supporting and consequence units, including the separate alternating lemma/theorem below, have their actual four-reader audit records; precise counts are in the central tables. The original divisorial-boundary and arbitrary-cover hereditary gates remain open.',
    'The restricted alternating reduction uses actual finite sets, not just their modular representations. Paying the permutation-basis ambiguity gives a count governed by the square-sum of full completed-local orbit sizes. The fixed-formal curve fibre bound then yields n^(A n) covers and polynomial alternating-kernel multiplicities under the O(n log(n+1)) condition. Any orbit factoring through a fixed finitely generated local quotient can be omitted from that sum. In particular the known maximal pronilpotent quotient, explicitly attributed to Suzuki Theorem1.2, allows nilpotent-image orbits of arbitrary size. This is one reduction with its own exact geometric restriction; it does not prove unrestricted alternating multiplicity bounds. Neither proof audits nor dimensional consequences are counted again as separate movement.',
    'Historical individual checkpoint01--17 page images were losslessly re-encoded as WebP to preserve room for the complete continuing record. Every RGB pixel, dimension and metadata item was checked, and the original/current paths and hashes are retained in qa/historical_page_encoding_map.json. The899 images save61653118 bytes; their original bytes remain in immutable checkpoint23. This is storage-only work, not a new visual inspection or mathematical movement.'
]
anchor = "'','## Files and continuation','',"
assert anchor in s
s = s.replace(anchor, ''.join(repr(x) + ',\n' for x in new_report) + anchor, 1)
path.write_text(s)
now = datetime.now(timezone.utc).isoformat()
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Post-checkpoint23 global and restricted-alternating synthesis\n\n'
            'INCOMPLETE. ' + now + '. The global finite-puncture unrestricted-PGL theorem and its stated closures are fully audited and integrated. The selected alternating factorial count and its fixed-local-quotient/nilpotent enlargement are also fully audited and integrated. These are prospective strict reductions for review16, each grouped with its prerequisites and consequences. No requested row changes: general D.1, general D.2(ii), and residual L8 remain open. The formal review is due18:10UTC, before checkpoint24 at the same scheduled time.\n')
print(json.dumps({'utc': now, 'requested_status_changes': [], 'formal_review_performed': False, 'archive_created': False}, indent=2))
