import sys,difflib
exec(open('seg_lib.py',encoding='utf-8').read())
F=R/'GCT_POS_final_20261122T0219Z_unzipped'; K=F/'branches/kronecker'
C='GCT_POS_checkpoint_03'
test('K-017 statement, as far as it was printed',K/'ALL_N_ROUTE_AUDIT.tex',9,24,200,C,'AMPLIFIER_FULL_STABILIZERS.tex kronecker/N9_FULL_STABILIZER.tex')
A9=R/'ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/work'
for lab,name,cp,pat in (('P-F1/F2 main section','positivity','01','cat positivity.tex'),
                        ('P-F9/F10','positivity_bounds','01','cat positivity_bounds.tex'),
                        ('P-F11','positivity_modular','01','cat positivity_bounds.tex'),
                        ('P-F12','positivity_ph3','01','cat positivity_bounds.tex')):
    test(lab,A9/(name+'.tex'),1,None,0,'ALPOGE_GCT_checkpoint_'+cp,pat)
test('P-F26 (cp05)',A9/'positivity_finite_lift.tex',1,40,0,'ALPOGE_GCT_checkpoint_05','sed -n 1,40p positivity_finite_lift.tex')
test('PLE-F8 (cp03)',A9/'positivity_actual_plethysm.tex',1,150,0,'ALPOGE_GCT_checkpoint_03','sed -n 1,200p positivity_actual_plethysm.tex')
def show(title,new,old,cap):
    d=[l for l in difflib.unified_diff(old,new,'stored','surviving',n=0,lineterm='')]
    print('#####',title); print('\n'.join(x[:200] for x in d[:cap]))
o=outputs('ALPOGE_GCT_checkpoint_03','cat positivity_cubic_counterexample.tex')[0].rstrip('\n').split('\n')
show('P-F19 cp03 -> cp09',lines(A9/'positivity_cubic_counterexample.tex'),o,60)
o=outputs(C,'sed -n 1,60p SOURCE_AUDIT.md')[0].split('\n')
st=next(i for i,l in enumerate(o) if l.startswith('# Source, attribution'))
show('SOURCE_AUDIT 1-60',cut(lines(F/'SOURCE_AUDIT.md')[:60],120),cut(o[st:st+60],120),70)
