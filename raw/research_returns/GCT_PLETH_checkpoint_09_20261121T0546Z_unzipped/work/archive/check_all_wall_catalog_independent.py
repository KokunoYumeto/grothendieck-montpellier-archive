"""G031 printed catalog, TSV/index and support evaluator against audited graph data."""
from pathlib import Path
import csv,json,re,sys,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent/'root'
j=json.loads((ROOT/'ALL_WALL_SUPPORT_GRAPH.json').read_text())
labels=('5','41','32','311','221','2111','11111')
nodes={tuple(row['gaps']):row for f in j['faces'] for row in f['nodes']}
report=(ROOT/'all_five_row_support_report.md').read_text()
printed={}
for gaps,axes,zero in re.findall(r'^\| \((\d+,\d+,\d+,\d+)\) \| ([^|]+) \| ([^|]+) \|$',report,re.M):
    g=tuple(map(int,gaps.split(',')));assert g not in printed
    actualaxes=[] if axes.strip()=='—' else [int(x)-1 for x in axes.strip().split(',')]
    zeros=[v.strip() for v in zero.split(',')]
    row=nodes[g]
    assert actualaxes==row['stable_axes']
    assert zeros==[label for label,v in zip(labels,row['multiplicities']) if not v]
    printed[g]=(actualaxes,zeros)
assert len(printed)==344 and set(printed)==set(nodes)
with (ROOT/'ALL_WALL_SUPPORT_NODES.tsv').open(newline='') as f:tsv=list(csv.DictReader(f,delimiter='\t'))
assert len(tsv)==344
for row in tsv:
    g=tuple(map(int,row['gaps'].split(',')));actual=nodes[g]
    assert tuple(map(int,row['multiplicities'].split(',')))==tuple(actual['multiplicities'])
    assert tuple(map(int,row['traces'].split(',')))==tuple(actual['traces'])
    assert tuple(int(v)-1 for v in row['stable_axes'].split(',') if v)==tuple(actual['stable_axes'])
idx=json.loads((ROOT/'FIVE_ROW_SUPPORT_INDEX.json').read_text())['nodes']
assert len(idx)==344 and {tuple(r['gaps']) for r in idx}==set(nodes)
for row in idx:
    actual=nodes[tuple(row['gaps'])]
    assert row['multiplicities']==actual['multiplicities'] and row['stable_axes']==actual['stable_axes']
known={}
for face in j['faces']:
    for key in ('initial_seeds','nodes','edges','ray_edges'):
        for row in face[key]:
            for field in ('gaps','target','raw_target'):
                if field not in row:continue
                g=tuple(row[field]);v=tuple(row['multiplicities'])
                assert g not in known or known[g]==v
                known[g]=v
sys.path.insert(0,str(ROOT));import five_row_support as evaluator
entries=exact=0
for g,vector in known.items():
    for d in (0,1):
        lam=tuple(sum(g[i:])+d for i in range(5));wanted=vector[::-1] if d else vector
        got=evaluator.classify(lam)
        assert got['support']==[v>0 for v in wanted]
        entries+=7
        if 'exact_multiplicities' in got:
            assert tuple(got['exact_multiplicities'])==wanted;exact+=7
special=0
for d in range(4):
    value=evaluator.classify((d,)*5)
    wanted=(1,0,0,0,0,0,0) if d%2==0 else (0,0,0,0,0,0,1)
    assert tuple(value['exact_multiplicities'])==wanted;special+=7
for lam in ((5,1,1,1,1,1),(2,2,2,2,1,1)):
    assert evaluator.classify(lam)['exact_multiplicities']==[0]*7;special+=7
isolated=sum(not row['stable_axes'] for row in nodes.values())
raybases=sum(len(row['stable_axes']) for row in nodes.values())
assert (isolated,raybases)==(158,196)
receipt=dict(statement='G031 full printed catalog and support evaluator',status='PASS',
 printed_catalog_rows=344,tsv_rows=344,index_rows=344,
 known_gap_vectors=len(known),support_entries_both_determinant_parities=entries,
 exact_returned_entries=exact,determinant_and_excess_length_entries=special,
 isolated_points=isolated,stable_ray_bases=raybases,
 report_sha256=hashlib.sha256(report.encode()).hexdigest(),
 note='Finite character values independently reconstructed by check_all_wall_support_independent.py; this check verifies every published row and executable lookup against those audited data.')
(HERE/'ALL_WALL_CATALOG_INDEPENDENT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
