import sys,re
exec(open('seg_lib.py',encoding='utf-8').read())
p=R/'ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/work/positivity.tex'
ls=lines(p)
for key in ('P-F1:','P-F2:'):
    a=next(i+1 for i,l in enumerate(ls) if 'begin{proposition}' in l and key in l)
    b=next(i+1 for i,l in enumerate(ls) if i+1>a and 'end{proof}' in l)
    test(key+' statement and proof',p,a,b,0,'ALPOGE_GCT_checkpoint_01','cat positivity.tex')
