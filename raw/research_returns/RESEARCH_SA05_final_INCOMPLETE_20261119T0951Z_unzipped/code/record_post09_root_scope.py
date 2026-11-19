"""Retain post-checkpoint09 scope refinements and the root transfer attempt."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
path=root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
outcome=('Root independently proved and wrote root_post09_spectral_transfer_attempt.md at09:38–09:39UTC. Split pullback under a smooth projective surface alteration gives characteristic-polynomial divisibility; cancelling the one ample Tate line gives primitive divisibility without requiring primitive pullback. Frobenius powers and nonzero Artin-factor twists also retain old repeated roots. C then read and checked the entire written proof at09:39:44UTC. These three specific transfers cannot supply a missing squarefree spectrum, but arbitrary new projectors or transfers are not excluded. No universal gate change is claimed.')
if not any(r['outcome']==outcome for r in rows):
    rows.append({'statement_id':'c:threefold-simple-spectrum-scope','date':now,
                 'who':'GPT-6 Astra / root / current run',
                 'type':'independent re-proof','outcome':outcome})
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)
path=root/'ITEM_SCOPE_ADDITIONS.json';scopes=json.loads(path.read_text())
adds={
 'B.1':' The separated quotient is in fact canonical and common to every coefficient prime different from p: divisibility maps trivially into any of the proved free quotients. The same formal integral module can nevertheless have a completed eigenvalue at3 and none at any other prime, so the common quotient does not resolve the required comparison.',
 'C.4':' The additional transfer attempt proves that constant-field extensions, smooth projective surface alterations and nonzero Artin-factor twists cannot remove a repeated primitive Frobenius root. This is a limitation of those transfers to the sufficient squarefree case, not a theorem excluding every possible geometric transfer.'}
for key,value in adds.items():
    if value.strip() not in scopes[key]['scope_append']:
        scopes[key]['scope_append']+=value
path.write_text(json.dumps(scopes,indent=2,ensure_ascii=False)+'\n')
entry='''

### Post-checkpoint09 refinements and failed transfers

The separated ordinary Milnor quotient has now been proved independent of
the coefficient prime different from the characteristic. The proof is short:
the ell-divisible kernel maps to zero in every other separated free abelian
quotient, and symmetry identifies the kernels. Root read the complete revised
corollary and the all-prime formal counterexample in the actual written files
at 09:37 UTC; C independently checked them. The formal permutation-submodule
example has an extra four-eigenline after3-adic completion and none after
completion at any other prime. This is not a geometric counterexample.

The source all-model residue audit was independently read by root, including
its code and saved output, at09:32UTC. The family t=s^m has iterated residue m
and gives infinitely many nonzero coordinates in the literal all-model target.
The source-version boundary is retained: only the opened author/arXiv text is
diagnosed, not the uninspected published file. A fixed chosen residue tree
avoids that construction issue; the ordinary regulator proof uses only fixed
finite-support maps. Root did not rerun the finite certificate. C's subsequent
actual timed rerun is separately recorded.

Root also proved the bounded C.4 spectral-transfer obstruction retained in
`root_post09_spectral_transfer_attempt.md`; C checked the entire written
argument. Surface alteration gives divisibility of the primitive Frobenius
characteristic polynomial by cancelling one ample Tate factor from split
degree-two pullback. Constant-field extension and Artin-factor twist retain
old multiplicities as well. These operations therefore do not establish the
new sufficient squarefree hypothesis when it initially fails. This is not
an impossibility result for arbitrary geometric constructions.

The additional conductor/microlocal primary reads are recorded with their
exact limited scopes in Part D's post09 note and canonical source ledger.
Root read that complete note, but did not reopen those three primary papers.
The geometric conductor's actual closed stalk, a generic inertia-invariant
space, and cross-prime support compatibility remain distinct. The BGV local
construction supplies a Clemens–Schmid complex whose required exactness
remains conditional on weight–monodromy. None of these refinements closes an
original open row or supplies a strictly smaller universal gate.
'''
for name in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md']:
    p=root/name;text=p.read_text()
    assert '### Post-checkpoint09 refinements and failed transfers' not in text
    p.write_text(text+entry)
result={'recorded_utc':now,'new_root_event':1,
        'updated_scope_rows':list(adds),'qualifying_movement':False}
(root/'code/record_post09_root_scope_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
