from pathlib import Path
from unittest.mock import patch
from datetime import datetime, timezone
import contextlib, hashlib, io, json, runpy, sys, re
sys.dont_write_bytecode=True
R=Path.cwd(); sys.path.insert(0,str(R/'code'))
import normalize_check_events
old_open=Path.open; suppressed=[]
def ro_open(self,mode='r',*a,**kw):
    if any(x in mode for x in 'wax+'):
        suppressed.append(str(self.relative_to(R)))
        return io.BytesIO() if 'b' in mode else io.StringIO()
    return old_open(self,mode,*a,**kw)
def ro_write(self,*a,**kw):
    suppressed.append(str(self.relative_to(R))); return len(a[0]) if a else 0
with patch.object(Path,'open',ro_open), patch.object(Path,'write_text',ro_write), patch.object(normalize_check_events.EventNormalizer,'save',lambda self:None), contextlib.redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(R/'code/build_registers.py'))
now=data['TASKS']; ledger=(R/'PROGRESS_LEDGER.md').read_text()
part=re.split(r'^## Scheduled mathematical review 15[^\n]*\n',ledger,flags=re.M)[1]
part=re.split(r'^## Scheduled mathematical review ',part,flags=re.M)[0]
prior=[]
for line in part.splitlines():
    if re.match(r'^\| (?:[A-F]\.\d+|Lead [A-F]\d+) \|',line):
        vals=tuple(x.strip() for x in line.strip().strip('|').split('|'))
        assert len(vals)==4; prior.append(vals)
old={x[0]:x for x in prior}
assert len(now)==len(prior)==41 and set(old)=={x[0] for x in now}
assert all(x[1]==old[x[0]][1] for x in now)
assert [x[0] for x in now if x!=old[x[0]]]==['C.3']
c3=next(x for x in now if x[0]=='C.3'); assert c3[3].startswith(old['C.3'][3])
stamp=datetime.now(timezone.utc).isoformat()
lines=[
'# Independent administrative comparison of all 41 main and Lead rows',
'',
'**PASS: no qualifying main-gate movement since review 15; no status promotion or gate deletion.**',
'',
f'Reviewer: GPT-6 Astra Pro (OpenAI), `/root/cycles_continuation`. Completed {stamp}. This is an administrative comparison, not a new review of every historical proof and not the scheduled review 16 itself. Root explicitly authorized this receipt during the mathematical source freeze; no mathematical, TeX, bibliography, master, bundle, builder or root register file was edited.',
'',
'## Comparison method and complete coverage',
'',
'Executed the current `code/build_registers.py` through `runpy.run_path` with every write-mode `Path.open`, every `Path.write_text`, and `EventNormalizer.save` intercepted in memory. Compared its computed `TASKS` against the actual 41-row table preserved under scheduled review 15 in `PROGRESS_LEDGER.md`. The review-15 receipt records 2026-11-19T19:50:17.127434+00:00, movement NO, dry streak 1. The comparison checked the complete item set, each status, each statement range and each full scope string. It did not merely compare displayed headings.',
'',
'Exactly 41 current rows and 41 historical rows were present. All 41 statuses are identical. Forty complete four-field rows are identical. C.3 alone changes its statement range from `C.3a–bu;C.1f` to `C.3a–bw;C.1f`; its entire review-15 scope is preserved verbatim, followed only by the C.3bv and C.3bw auxiliary paragraphs.',
'',
'| Rows checked | Count | Result |',
'|---|---:|---|',
'| A.1–A.8 | 8 | Every field identical |',
'| B.1–B.4 | 4 | Every field identical |',
'| C.1, C.2, C.4, C.5 | 4 | Every field identical |',
'| C.3 | 1 | Status identical; bv/bw statement range and auxiliary scope appended only |',
'| D.1–D.4 | 4 | Every field identical |',
'| E.1–E.6 | 6 | Every field identical |',
'| F.1–F.2 | 2 | Every field identical; delivery statuses have not been substituted for mathematical completion |',
'| Lead A1–A4 | 4 | Every field identical |',
'| Lead B1–B2 | 2 | Every field identical |',
'| Lead C1, Lead D1 | 2 | Every field identical |',
'| Lead E1–E4 | 4 | Every field identical |',
'',
'## New-work scope check',
'',
'- **C.3bv:** the whole K1 family lifts on the original fixed local base times a proper curve. The row expressly retains normality/characteristic-p and the supplied modification scope, distinguishes the extra endpoint hypothesis, and denies a symbolic nonlocal-base lift or a change to UK.7.',
'- **C.3bw:** the integral surface gamma bound and polynomial fixed-product lift are auxiliary. The row expressly leaves the actual supported boundary-node obstruction unproved and the main quotient unchanged.',
'- **HD:** the final full note at SHA `812b2461b6a3cc14a70750faf81c4bdcebc4ae7a7dbe9f0c833c1922f1a3814a` was reread. Relative to the previously fully audited argument, its final changes correct the Weil-restriction source attribution and synchronize completed audit status. It proves the exceptional symbolic endpoint relation, retains the FK source qualification, and explicitly does not lift the whole symbolic family to the regular target. No HD assertion changes a main row.',
'- **SR:** the supported repair is conditional on vanishing of the actual support-Mayer–Vietoris node vector; that hypothesis is explicitly unproved for HK/VE. The conditional mechanism is not a proof that all node classes vanish.',
'- **SC and UP:** the fixed-section tensor criterion and universal Picard reformulation describe a method-specific condition. Neither identifies every actual supported node, forces the criterion from component Albanese-kernel membership, nor supplies a counterexample to UK.7. UP final hash `b120bfe9d13dc962b707d963bf3b0af607c562af53fefd3b038baaa24de12c5a` includes only a CH^1 notation correction after its initially logged save.',
'- **BT:** the final supersingular-threefold note was checked for its header and complete BT.9–BT.11 scope. Constant and elliptic-complement exclusions do not settle arbitrary nonconstant Jacobian factors. BT.11 explicitly leaves the surface-complement extension unpromoted with source/classification dependencies unfinished. The C.4 and Lead C1 rows are fully unchanged. This administrative scope check is not an independent full proof audit of BT.',
'',
'C.3bt was already qualifying movement at review 14 and is not counted again. Its exact residual surface gate remains `T_E / (phi(J_K intersect S00) + phi(Q intersect S00))`. Historical bm–bs scope paragraphs are cumulative; bt explicitly supersedes their component-kernel obstruction in the surface branch. The separate higher-dimensional bp compatibility remains outside that removal. No broad vanishing, quotient exactness beyond the proved UK.7 presentation, or node-cancellation theorem has been silently added.',
'',
'All other gates named in review 15 are retained: C.1/C.2 standard-conjecture/positivity/image questions; global and rational-top C.3 questions and the remaining higher characteristic-p restriction ranges; general C.4 integral splitting cases; D.4/E.2 motivic gates; and the A.8/Lead A3 and E.5/Lead E3 historical interpretation gaps. The two new registered auxiliaries do not qualify as main movement. If no later qualifying theorem is certified before the scheduled review, the current evidence supports another NO; this receipt does not itself advance the scheduled clock or record that review.',
'',
'## Input fingerprints',
'',
'| Input | SHA-256 |',
'|---|---|'
]
for rel in ['code/build_registers.py','logs/scheduled_review_15.json','notes/REVIEW_15_ASSESSMENT.md','PROGRESS_LEDGER.md','agents/frobenius/C3_symbolic_higher_kernel_descent_RESEARCH.md','agents/frobenius/C3_surface_supported_repair_RESEARCH.md','agents/cycles/notes/SL_section_choice_tensor_criterion_2024.md','agents/cycles/notes/SC_universal_Picard_reformulation_2041.md','agents/real_weil/C4_SUPERSINGULAR_BT1_LIFTING_RESEARCH.md']:
    lines.append('| `'+rel+'` | `'+hashlib.sha256((R/rel).read_bytes()).hexdigest()+'` |')
lines += ['', 'Intercepted root output paths: `RESEARCH_SA06_results.csv`, `CHECK_EVENTS.tsv`, and `RESEARCH_SA06_report.md`; normalization saves were suppressed. No root output was written by this check.', '']
p=R/'agents/cycles/MAIN_ROWS_REVIEW15_COMPARISON_2045.md'
p.write_text('\n'.join(lines))
print(json.dumps({'saved':str(p.relative_to(R)),'utc':stamp,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'all_states_unchanged':True,'full_rows_identical':40,'auxiliary_append_only':'C.3','qualifying_main_movement':'NO','suppressed_root_writes':suppressed},indent=2))
