p=5;N=24;qs=[]
types={1:'A',5:'A',9:'B',21:'B',13:'C',17:'C'}
for c,t in types.items():
 for B in range(1,p*(p-1)):
  if (B-c)%(p+1):continue
  r=((c-B)//(p+1))%(p-1)
  qs.append((t,c,B,r, p*N-(p+1)*B))
print('All possible Newton/tame records',qs)
print('Wild comparable distinct types, at least one divisible B:')
for i,x in enumerate(qs):
 for y in qs[i+1:]:
  if x[0]==y[0] or x[3]!=y[3] or (x[2]%p and y[2]%p):continue
  if x[2]%p==0 and y[2]%p and y[4]>=x[4]:continue
  if y[2]%p==0 and x[2]%p and x[4]>=y[4]:continue
  print(x,y)
print('Tame residual pairs:')
for i,x in enumerate(qs):
 for y in qs[i+1:]:
  if x[0]==y[0] or x[2]%p or y[2]%p:continue
  if sorted([x[3],(1-x[3])%4])==sorted([y[3],(1-y[3])%4]):print(x,y)
