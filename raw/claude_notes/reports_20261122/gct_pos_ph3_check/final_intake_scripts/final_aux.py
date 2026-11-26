import json,hashlib,pathlib,re,collections
D=pathlib.Path('<local>/Documents')
F=D/'grothendieck_archive_transcription_20261110/research_returns/GCT_POS_final_20261122T0219Z_unzipped'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
print('## main-session hashes against the final')
for l in (D/'reports_20261122/gct_pos_ph3_check/FILES_READ.sha256').read_text().splitlines():
    h,n=l.split(None,1); print(sha(F/'branches'/n.lstrip('*'))==h, n)
print('## nonstandard branch against the preserved cp03 manifest')
M=[p for p in F.glob('_from_earlier_checkpoints/*/_from_earlier_checkpoints/GCT_POS_checkpoint_03*/branches/nonstandard/MANIFEST.json')][0]
old={e['file']:e['sha256'] for e in json.loads(M.read_text())['files']}
N=F/'branches/nonstandard'
now={p.relative_to(N).as_posix():p for p in N.rglob('*') if p.is_file()}
same=[k for k in old if k in now and sha(now[k])==old[k]]
chg=[k for k in old if k in now and sha(now[k])!=old[k]]
gone=[k for k in old if k not in now]
new=sorted(k for k in now if k not in old)
print('listed',len(old),'same',len(same),'changed',chg,'absent',gone)
print('same .tex/.md:',[k for k in same if k.endswith(('.tex','.md'))])
print('not in manifest:',len(new),[k for k in new if k.endswith('.tex')])
out=pathlib.Path('n_branch_diff.tsv')
out.write_text(''.join('%s\t%s\n'%(s,k) for s,L in (('same',same),('changed',chg),('absent',gone),('not in cp03 manifest',new)) for k in sorted(L)))
print('## 1.6.7 in Kronecker-related text')
for rel in ['GCT_POS.tex','IMPLICATIONS.md','README.md','branches/plethysm/modular_pole_transfer.tex','branches/root/grothendieck_dictionary.tex','SOURCE_AUDIT.md','branches/kronecker/HOOK_CHAIN_POLE.tex']:
    for i,l in enumerate((F/rel).read_text(encoding='utf-8').split('\n'),1):
        if re.search(r'1[.]6[.]7|3[.]3[.]4',l): print(rel,i,l[:120])
print('## inclusion in GCT_POS.tex')
t=(F/'GCT_POS.tex').read_text(encoding='utf-8')
names=['AMPLIFIED_LOWER_FIXED_LOCI','SMOOTH_CANCELLATION_COUNTEREXAMPLE','CYCLIC_TRACE_HOOK_IDENTITY','HOOK_CHAIN_POLE','hook_chain_lie','modular_pole_transfer','ODD_LIFT_OBSTRUCTION','CYCLIC_FIXED_COMPONENT_REDUCTION','EXCEPTIONAL_LOCUS_REDUCTION','PRIME_TO_THREE_STABILIZER_REDUCTION','AMPLIFIED_COLLISION_COMPONENTS','FINITE_STABILIZER_REDUCTION','ALL_STABILIZER_SYMMETRY_REDUCTION','AMPLIFIED_COMPONENT_NORMALIZATION','RANK_TWO_COMPONENT_DENSITY','RANK_TWO_CONDUCTOR_REDUCTION','RANK_TWO_DOWNSTAIRS_INERTIA','UNIFORM_RANK_TWO_INERTIA','RANK_THREE_COLLISION_MODULE','RANK_THREE_LOCAL_MOVING_CLASS','cyclic_free_collision_diagnostic','trace_index_obstruction','hook_wave_covariant_gate','tensor_fixed_dimension_gate']
print('not named in GCT_POS.tex:',[n for n in names if n not in t])
print('## run events after cp03 on earlier ids of this part')
for l in (F/'CHECK_EVENTS.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    c=l.split('\t')
    if c[1]>'2026-11-21T22:16' and re.match(r'K-0(0|1)\d|K-020|PNEW-?0(0\d|1[012])\b|R-NEW-?00[123]',c[0]):
        print(c[0],c[1][5:16],c[6][:30],c[7][:130])
