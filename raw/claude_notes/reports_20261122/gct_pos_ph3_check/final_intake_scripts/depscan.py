# static transitive import scan; imports nothing from the scanned folder
import ast,sys,pathlib
root=pathlib.Path(sys.argv[1]); dirs=[root,root.parent/'theta'/'outer5'/'variable_wall']
todo=[sys.argv[2]]; seen={}
risky={'open','write_text','write_bytes','eval','exec','compile','__import__','system','popen','unlink','rmtree','rename','urlopen','Popen','run'}
while todo:
    m=todo.pop()
    if m in seen: continue
    ps=[d/(m+'.py') for d in dirs if (d/(m+'.py')).exists()]
    if not ps: continue
    t=ast.parse(ps[0].read_text(encoding='utf-8')); hits=set(); seen[m]=hits
    for x in ast.walk(t):
        if isinstance(x,ast.Import): todo+=[a.name for a in x.names]
        if isinstance(x,ast.ImportFrom) and x.module: todo.append(x.module)
        if isinstance(x,ast.Call):
            f=x.func; name=getattr(f,'id',getattr(f,'attr',''))
            if name in risky and not (name=='compile' and getattr(getattr(f,'value',None),'id','')=='re'): hits.add((name,x.lineno))
for m,h in sorted(seen.items()): print(m,sorted(h))
