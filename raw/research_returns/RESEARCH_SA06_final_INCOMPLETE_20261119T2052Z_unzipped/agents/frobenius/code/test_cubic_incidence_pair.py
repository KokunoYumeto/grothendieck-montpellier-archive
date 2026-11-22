import sympy as s,time,json
p=5;y,z,u=s.symbols('y z u'); outs=[]
for zp in (0,2):
 for fp in (0,1):
  t0,t1=(s.Integer(1),u) if fp==0 else (u,s.Integer(1))
  if zp==0:
   zz=[s.Integer(1),y,z]
   ww=[(y*y-z)*t0+y*z*t1,-y*t0-z*t1,t0,t1]
  else:
   zz=[y,z,s.Integer(1)]
   ww=[t0,t1,-y*t0-z*t1,y*z*t0+(z*z-y)*t1]
  F=sum(v**4 for v in zz);G=s.expand(sum(v**3 for v in ww))
  jac=s.Matrix([[s.diff(P,v) for v in (y,z,u)] for P in (F,G)])
  pol=[F,G]+[s.expand(jac[:,[i,j]].det()) for i in range(3) for j in range(i+1,3)]
  st=time.perf_counter();gb=s.groebner(pol,y,z,u,modulus=p,order='grevlex'); elapsed=time.perf_counter()-st
  out={'z_chart':zp,'fibre_chart':fp,'unit':list(gb)==[1],'seconds':elapsed,'basis':[str(a) for a in gb]};outs.append(out);print(json.dumps(out),flush=True)
print(json.dumps(outs),flush=True)
