"""Record the separate reverse-order check of the new formal argument."""
from pathlib import Path
from datetime import datetime,timezone
import csv
root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
with (root/'research/SECOND_CHECKS.md').open('a') as f:
 f.write(r'''

## H035.39 — second derivation of the stronger countable-base theorem

Rechecked in reverse dependency order, from the desired composite comparison.
If W=G(M) is finite over the completion C, the outer completion axiom applies
to W. What remains is a pro-isomorphism, not just an equality of inverse
limits: an arbitrary additive F need not preserve an equality of limits.
For the natural W/I^nW→G(M/I^nM), each kernel and cokernel is finite over
C and killed by I^n. At a prime q over I, C_q completed is A_p completed:
the identity modulo p^r follows from exact completion and I^r⊂p^r.
Flat base change for G is valid over C without any finite-output assumption.
The two nested limits of G(M_B/(I^n+m^r)M_B) commute; fixing r makes the
n-system eventually constant. Thus the comparison has zero completed-local
error limits. Matlis duality, exact filtered colimits and exact duality give
exact limits of finite B-modules. This does not assume finite length or ML.

To detect pro-zero, fix a target index before choosing a prime. The descending
supports of the images stabilize; at a generic point of a nonempty stable
support the images have finite length and hence stabilize nontrivially. Flat
completion and exact inverse limits then give a nonzero local limit, a
contradiction. The order of these choices is essential: vanishing at each
prime alone would not give a uniform index without the support argument.

It remains to check that countability supplies W finite without presupposing
the comparison just proved. Use only the given I-completion equality for G.
Any finite C-submodule L of W has closed image after every completed maximal
localization: the maximal-completion axiom identifies the target limit, and
exactness of inverse limits lifts every compatible family in its finite
coordinate images to L_B. The map from W is continuous because its rth
coordinate kills I^rM. Faithfully flat descent at all maximal ideals proves
L closed globally; it does not require W/L finite. All maximal ideals of C
contain I. Finite presentation makes each evaluation image from N finite
over C. Countability is used precisely to enumerate the finite presentation
matrices of N, not to claim the completion or M is countable. Finitarity gives
the union of the finite sums of these images. Baire gives an open one, and
its quotient is finite because it is a quotient of a submodule of one V_n.

Boundary checks: I=0 gives a constant system; I=A gives the zero completion.
The nonartinian example K_n=(x^n,y^n) does not contradict this argument because
it lacks the completed-local comparison at the generic point (x). The earlier
weighted-torsion candidate explicitly fails that same axiom. The countable
proof makes no claim for an uncountable union of closed finite submodules.
No circular use of finite completed output, generic base change or a presumed
Mittag–Leffler property remains in this derivation. The broad arbitrary-base
assertion stays open; the sufficient finite-output gate is strictly smaller.
''')
who='GPT-6 Astra Pro; effort not exposed; OBJ_H035 single-stream run'
with (root/'CHECK_EVENTS.tsv').open('a') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['H035.39',stamp,who,'targeted proof check — separate reverse-order derivation','Full countable-base composition proved; arbitrary-base problem reduced to finite completed output; no nonartinian ML assumption','PROOFS.tex H035.39 arguments (A)–(D); research/SECOND_CHECKS.md stronger countable-base theorem'])
 w.writerow(['Stacks08Z9',stamp,who,'used and rechecked in this run','Proposition 47.7.8 reopened: complete noetherian local finite-module biduality; derived exactness of inverse limits','PROOFS.tex H035.39(A); https://stacks.math.columbia.edu/tag/08Z9'])
 w.writerow(['Stacks00MB',stamp,who,'used and rechecked in this run','Lemma 10.97.2 reopened: flatness and finite-module exactness of completion justify the completed localization identity','PROOFS.tex H035.39(C); https://stacks.math.columbia.edu/tag/00MB'])
 w.writerow(['Stacks0GNI',stamp,who,'used and rechecked in this run','Lemmas 56.2.1–5: finite-presentation restriction and finitary extension; not a composition theorem for the archival class','research/SEARCH_AUDIT.md; references.bib'])
 w.writerow(['HartshorneSpaceCurves',stamp,who,'used and rechecked in this run','Section 2 pp.88–89: finite Hom-presentation coherent class and its abelian closure; distinct from the larger archival class','research/SEARCH_AUDIT.md; references.bib'])
 w.writerow(['GrothendieckCollectedIndex',stamp,who,'carried as background without fault found','Bibliographical index opened; no exact matching theorem inferred from index metadata','research/SEARCH_AUDIT.md; references.bib'])

ledger=root/'PROGRESS_LEDGER.md'
s=ledger.read_text()
a=s.index('Only completion compatibility remains')
b=s.index('## Current statement rows')
s=s[:a]+f'''All noncompletion axioms are stable in the explicit affine reconstruction.
Full closure is now proved for countable A, Dedekind domains and artinian
rings. A separate proof shows that finite output on a finite completed
module implies the necessary pro-comparison, even for a nonartinian
principal tower. The remaining sufficient gate is finite generation of
G(M) over arbitrary local or principal completions for uncountable A.
Every finite evaluation image is closed; the countable-cover Baire step
does not handle the remaining uncountable cover. H035.40 separately records
the undefined general two-scheme programme and its proved proper examples.

Start: 2026-11-19T02:54:34Z. One stream; no delegated workers.
Current ledger update: {stamp}.
Mandatory three-hour review due 05:54:34 UTC, then hourly.
The results attachment was opened only after the full entry was frozen;
it has zero result rows. See research/RESULTS_AUDIT.md.

'''+s[b:]
with (root/'STATEMENTS.tsv').open() as f: row=next(r for r in csv.DictReader(f,delimiter='\t') if r['id']=='H035.39')
lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('| H035.39 |'):lines[i]='| H035.39 | '+row['status']+' | '+row['statement']+' See PROOFS.tex and research/SECOND_CHECKS.md. |'
s='\n'.join(lines)+'\n'
s=s.replace('## Mandatory progress reviews',f'- {stamp}: H035.39 strictly reduced to arbitrary-base completed-output finite generation; full countable-base composition proved and checked a second time. Nonartinian pro-continuity is no longer an outstanding gate.\n\n## Mandatory progress reviews')
ledger.write_text(s)
with (root/'progress.log').open('a') as f:f.write('H035.39 separate reverse-order check completed '+stamp+'\n')
print('Recorded second derivation, six source/proof events, current ledger, and empty-results status.')
