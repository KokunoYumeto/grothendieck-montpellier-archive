"""Serialize the final editorial ranking of already authored prospective tasks.

The order and normalized scores below are editorial judgments. The program
neither invents new directions nor develops any of their proposed mathematics.
"""
from pathlib import Path
import re, csv, json
OUT=Path(__file__).resolve().parents[1]
original=(OUT/'editorial/root_direction_seeds.md').read_text()
root_chunks=re.split(r'^## (\d+)\. ',original,flags=re.M)
blocks={}
for i in range(1,len(root_chunks),2):
    blocks['R'+root_chunks[i]]=root_chunks[i+1].split('## Prerequisites for external-project comparisons')[0].strip()
b=(OUT/'parts/b2/directions.md').read_text()
b_chunks=re.split(r'^## DIR-B2-(\d+)\. ',b,flags=re.M)
b_scores=[(5,4),(5,4),(4,4),(4,5),(4,4),(5,4),(4,5),(4,4)]
for i in range(1,len(b_chunks),2):
    n=int(b_chunks[i]);block=b_chunks[i+1].strip();score,reach=b_scores[n-1]
    block=re.sub(r'\*\*Interest:.*?\*\*',f'**Interest {score}; one-run reach {reach}.**',block,count=1)
    blocks['B'+str(n)]=block
c=(OUT/'parts/c2/directions.md').read_text()
c_chunks=re.split(r'^## (\d+)\. ',c,flags=re.M)
c_scores=[(5,4),(5,3),(4,2),(4,3),(4,4),(4,5),(4,5),(3,5)]
for i in range(1,len(c_chunks),2):
    n=int(c_chunks[i]);block=c_chunks[i+1].split('## Source-recovery priority')[0].strip();score,reach=c_scores[n-1]
    block=re.sub(r'\*\*Interest:.*?\*\*',f'**Interest {score}; one-run reach {reach}.**',block,count=1)
    blocks['C'+str(n)]=block
order='R1 R2 B1 R3 C1 R5 B2 C2 R4 B6 R6 R7 R8 R9 C5 B7 C6 C3 C4 R10 R11 B3 R12 R13 R14 B4 R15 R16 R17 R18 R19 C7 B5 B8 C8 R20'.split()
assert set(order)==set(blocks) and len(order)==len(set(order))
aliases={}
for filename in ['ITEM_MERGES.json','CLAIM_MERGES.json','PROBLEM_MERGES.json']:
    aliases.update({x['from']:x['to'] for x in json.loads((OUT/filename).read_text())})
def canonical(x):
    while x in aliases:x=aliases[x]
    return x
pat=re.compile(r'(?<![A-Za-z0-9-])(?:MP-SA03-\d+|CL-SA03-\d+|SA03-\d+)(?!\d)')
intro=root_chunks[0].strip()+'''\n\nThe ranking consolidates 20 cross-folder tasks and 16 further tasks from the\ncomplete Codex-only blocks. The two numeric scores use one scale throughout:\n5 is high interest or high reach, 1 is low. They are editorial assessments,\nnot estimates of a conjecture's probability. The local direction files preserve\ntheir original rankings; `DIRECTION_CONCORDANCE.tsv` maps them to this list.\n'''
parts=[intro]
rows=[]
for rank,key in enumerate(order,1):
    block=pat.sub(lambda m:canonical(m.group()),blocks[key])
    # Avoid self-alias prose after canonical replacement.
    block=block.replace('SA03-682, canonically merged into SA03-682','SA03-682')
    block=block.replace('CL-SA03-1201 and CL-SA03-667, the latter merged into CL-SA03-667','CL-SA03-1201 and CL-SA03-667')
    block=block.replace('MP-SA03-107, merged into MP-SA03-107','MP-SA03-107')
    block=block.replace('SA03-640, merged with SA03-640','SA03-640')
    parts.append(f'## {rank}. '+block)
    source={'R':'editorial/root_direction_seeds.md','B':'parts/b2/directions.md','C':'parts/c2/directions.md'}[key[0]]
    rows.append(dict(rank=rank,source_file=source,source_direction=key,title=block.splitlines()[0]))
parts.append('## Prerequisites for external-project comparisons\n\n'+original.split('## Prerequisites for external-project comparisons\n\n',1)[1].strip())
(OUT/'SA03_directions.md').write_text('\n\n'.join(parts)+'\n')
with (OUT/'DIRECTION_CONCORDANCE.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['rank','source_file','source_direction','title'],delimiter='\t');w.writeheader();w.writerows(rows)
print('Final ranked directions:',len(rows))
