"""Preserve final exact research reads; no manuscript promotion or movement."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
def sha(path): return hashlib.sha256((root/path).read_bytes()).hexdigest()
snc='parts/D/post29_research/note_weighted_SNC_final_minus_one_D.tex'
initial='parts/D/post29_research/weighted_SNC_exact_initial_1bd307cc.source.txt'
assert sha(snc)=='192867e75d054b802f48bd84f8596be09c14039bd6b54843a0a28885e8534204'
assert sha(initial)=='1bd307cc1fbb8f9984e4568283bcb4eb8c500ab799fd4d80cef69d705ab44d43'
old=(root/initial).read_bytes()
token=bytes.fromhex('7b0d6d206e65777d')
assert old.count(token)==2 and old.count(b'+sum_{j\\ne i}')==1
repaired=old.replace(token,b'\\mathrm{new}').replace(b'+sum_{j\\ne i}',b'+\\sum_{j\\ne i}')
assert repaired==(root/snc).read_bytes()
now=datetime.now(timezone.utc).isoformat()
audit={
    'utc':now,'actor':'root','path':snc,'sha256':sha(snc),
    'verdict':'PASS in stated numerical scope; unpromoted research note',
    'actual_read_scope':'Entire initial actual file and entire final corrected file read. Complete source/author scope record read. Complete existing degree-linear core and weighted-chain compression proofs freshly reread.',
    'exact_typography_reconstruction':dict(initial_path=initial,initial_sha256=sha(initial),two_CR_rm_tokens_repaired=True,one_sum_backslash_repaired=True,exact_bytes_verified=True),
    'independent_checks':[
        'The strict-transform ideal sequence gives the delta drop n(n-1)/2. Adjunction contributes n(n-1) on the normalized branch, yielding v_E(f_i)-a_E=2delta_i at the final transverse point in every characteristic.',
        'The q=2(m-a)-a recurrence is positive during the singular stage; the first smooth free or satellite case and each subsequent fixed-parent corner step keep q nonnegative. Hence the intrinsic final multiplicity is at most6delta_i.',
        'After intrinsic resolution, any further necessary centre on that branch contains another strict branch. The centres are free along it and are charged to intersection drops. Distinct final new(-1) curves can be assigned distinct analytic branches.',
        'Restriction of every other branch equation at the final transverse point gives v_E(f_j)=I_ij. Summing the resulting weights gives the displayed6delta+2pair-intersection bound.',
        'Only original bad points are charged. Negative definiteness excludes triple noncore intersections and noncore pair multiplicity at least2. Self-nodes are charged as two analytic branches when strict global normal crossings requires their separation.',
        'The weighted GC/WC and rowwise Schur inputs pay all core and core-adjacent terms. Canonical intersection invariance plus the bounded final negative-canonical mass controls the refined positive-canonical core. New zero-Z(-1) curves remain explicit core vertices.',
        'The resulting numerical estimate does not control products of adjacent cycle coefficients, replace extra blowup curves by ADE blocks, or supply a small order-module atlas.'
    ],
    'fresh_primary':[
        dict(apa='The Stacks Project Authors. (2026). Lemma54.3.1 (Tag0AGQ). The Stacks Project.',url='https://stacks.math.columbia.edu/tag/0AGQ',ref='turn178266262view0',scope='Complete statement and written proof read.'),
        dict(apa='The Stacks Project Authors. (2026). Lemma54.3.2 (Tag0AGR). The Stacks Project.',url='https://stacks.math.columbia.edu/tag/0AGR',ref='turn178266262view1',scope='Complete statement and written proof read.'),
        dict(apa='The Stacks Project Authors. (2026). Lemma54.3.4 (Tag0AGS). The Stacks Project.',url='https://stacks.math.columbia.edu/tag/0AGS',ref='turn178266262view2',scope='Complete statement and written proof read; its explicitly omitted graded-map verification and recursive inputs remain Known.')
    ],
    'reused_known_inputs':['Cartier adjunction','Canonical point-blowup formula','Previously audited fixed-base different and geometric budgets'],
    'movement':False,'promoted':False
}
audit_path='parts/D/post29_research/audit_weighted_SNC_root.json'
assert not (root/audit_path).exists()
(root/audit_path).write_text(json.dumps(audit,indent=2)+'\n')
items=[
    ('parts/B/post29_research/note_order_head_generation_diagnostic_B.tex','55453517ab943597f49949144e2f444fafdf855d304f471a8586ff8f7781a7b2','Entire actual note read. Conditional head-kernel duality, the all-simple-quotient generation condition, incidence codimension and the exact h2,A1 diagonal-head obstruction checked.'),
    ('parts/B/post29_research/note_P1_order_generator_count_B.tex','f7b9eb1f31468e04a2b4934555c0e7d771a7cfd9bc108f55ef65100e51f6ffc2','Entire actual note read. Root proposed the example independently; local Morita rank one, global first-column image, determinant lower bound and explicit d+1 band-matrix construction checked. The failure of s+1 occurs for d>=2, a nonminimal period-one anchor.'),
    ('parts/C/post29_research/note_two_end_pair_coefficient_gerbe_C.tex','dcd5612fff2f621d3afd696e2c2efa2d658688924a11a74684d46afc3721b3f1','Entire actual note and all four exact audit records read. Root source/proof scope is in the dedicated audit. All four passes are local; the note remains unpromoted.'),
    (snc,sha(snc),'Entire initial and final actual note read; exact byte repair verified. Detailed numerical and source audit is recorded separately.'),
    ('parts/C/post17_research/D_uniform_generation_cycle_charts.tex',sha('parts/C/post17_research/D_uniform_generation_cycle_charts.tex'),'Entire existing theorem, cycle-chart proposition and complete proofs freshly reread. The full ordinary evaluation premise and all-subcycle point-ideal argument remain essential; no new source reopening for recursive inputs.'),
    ('parts/C/D_exceptional_graph_core.tex',sha('parts/C/D_exceptional_graph_core.tex'),'Entire current original core proposition and proof freshly reread, including weighted GC.4 and the rowwise Schur attachment calculation.'),
    ('parts/C/D_weighted_exceptional_chain_compression.tex',sha('parts/C/D_weighted_exceptional_chain_compression.tex'),'Entire current weighted compression proposition and proof freshly reread, including WC.1 and anti-nef attachment budgets.')
]
files=[]
for p,d,s in items:
    assert sha(p)==d,p
    files.append(dict(path=p,sha256=d,complete_actual_file_read=True,scope=s))
pair_audits=[
    'parts/C/post29_research/audit_two_end_pair_author_C.json',
    'parts/C/post29_research/audit_two_end_pair_root.json',
    'parts/B/post29_research/audit_C_two_end_pair_coefficient_gerbe_B.json',
    'parts/D/post29_research/audit_C_two_end_pair_coefficient_gerbe_D.json'
]
for p in pair_audits:
    a=json.loads((root/p).read_text())
    assert a['sha256']==items[2][1] and a['verdict'].startswith('PASS')
record={
    'utc':now,'actor':'root','kind':'Last complete actual-file and exact source reads before review21',
    'files':files,
    'two_end_exact_audit_records':[dict(path=p,sha256=sha(p)) for p in pair_audits],
    'weighted_SNC_root_audit':dict(path=audit_path,sha256=sha(audit_path)),
    'unproved_minimal_period_diagnostic_route':{
        'status':'Unproved exploratory route; no example claimed',
        'idea':'Extend the nonminimal overorder diagnostic to a period2 class on a reducible positive-genus exceptional fibre with an unramified component supporting a stable rank2 restriction.',
        'missing':['Actual surface construction and contraction','Global class and prescribed rank2 anchor construction/algebraization','Required positive-pole End-layer vanishing and canonical scalar-image verification','Complete elementary-modification comparison in that actual minimal-period example'],
        'limitation':'Even such an example would not by itself rule out a suitably optimized anchor or disprove the requested representation count.'
    },
    'manuscript_promotions':[], 'requested_status_changes':[], 'strict_main_gate_reductions':[], 'movement':False,
    'remaining':'Uniform all-coefficient global object presentation, core/gerbe/order compatibility, all thick overlap layers and the other strongest main gates remain unproved.'
}
out=root/'code/output/root_review21_last_research_scope.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'root_scope':str(out.relative_to(root)),'files':len(files),'SNC_audit':audit_path,'movement':False}))
