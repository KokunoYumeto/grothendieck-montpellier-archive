#!/usr/bin/env python3
"""Exact affine cocycle extension checks for the twisted Sp4 braid chain."""
import importlib.util,contextlib,io,json,pathlib,itertools
path=pathlib.Path(__file__).with_name('affine_cubic_detector.py');spec=importlib.util.spec_from_file_location('cub',path);cub=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(cub)
a,m,n,di=cub.add,cub.mul,cub.N,cub.D
sub=lambda x,y:a(x,n[y])
def eye(d):return [[int(i==j) for j in range(d)] for i in range(d)]
def zero(d):return [[0]*d for _ in range(d)]
def mm(A,B):
 return [[sum9(m(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sum9(xs):
 v=0
 for x in xs:v=a(v,x)
 return v
def ma(A,B):return [[a(x,y) for x,y in zip(ar,br)] for ar,br in zip(A,B)]
def mn(A):return [[n[x] for x in r] for r in A]
def ms(A,c):return [[m(c,x) for x in r] for r in A]
def mp(A,k):
 out=eye(len(A))
 while k:
  if k&1:out=mm(out,A)
  A=mm(A,A);k//=2
 return out
def gauss(rows,rhs,N):
 ar=[list(r)+[b] for r,b in zip(rows,rhs)];pivs=[];row=0
 for col in range(N):
  chosen=next((k for k in range(row,len(ar)) if ar[k][col]),None)
  if chosen is None:continue
  ar[row],ar[chosen]=ar[chosen],ar[row]
  ar[row]=[m(di[ar[row][col]],v) for v in ar[row]]
  for k in range(len(ar)):
   if k!=row and ar[k][col]:
    c=ar[k][col];ar[k]=[sub(x,m(c,y)) for x,y in zip(ar[k],ar[row])]
  pivs.append(col);row+=1
 bad=any(not any(r[:N]) and r[N] for r in ar)
 free=[j for j in range(N) if j not in pivs]
 solution=[0]*N
 if not bad:
  for j,r in zip(pivs,ar):solution[j]=r[N]
 basis=[]
 for f in free:
  v=[0]*N;v[f]=1
  for j,r in zip(pivs,ar):v[j]=n[r[f]]
  basis.append(v)
 return {'rank':row,'augmented_rank':row+int(bad),'consistent':not bad,'solution':solution if not bad else None,'kernel_basis':basis,'free_columns':free}
I=eye(4);J=zero(4)
for j in range(3):J[j][j+1]=1;J[j+1][j]=2
T=[]
for j in range(4):
 M=eye(4)
 for k in range(4):M[j][k]=a(M[j][k],J[j][k])
 T.append(M)
B=[ms(M,6) for M in T] # -i

def system(count):
 rows=[];rhs=[]
 def append(coeff):
  for rr in range(4):rows.append([coeff[g][rr][cc] for g in range(count) for cc in range(4)]);rhs.append(0)
 for g in range(count):
  for h in range(g+1,count):
   coeff=[zero(4) for _ in range(count)]
   if h==g+1:
    coeff[g]=ma(ma(I,mm(B[g],B[h])),mn(B[h]))
    coeff[h]=ma(ma(B[g],mn(I)),mn(mm(B[h],B[g])))
   else:
    coeff[g]=ma(I,mn(B[h]));coeff[h]=ma(B[g],mn(I))
   append(coeff)
 return rows,rhs
result={}
for count in [3,4]:
 rows,rhs=system(count)
 homogeneous=gauss(rows,rhs,4*count)
 for j,left,b in [(0,0,1),(0,1,1),(1,0,3),(1,1,6)]:
  row=[0]*(4*count);row[4*j+left]=1
  if left==0:row[4*j+2]=2
  rows.append(row);rhs.append(b)
 extension=gauss(rows,rhs,4*count)
 result['B'+str(count+1)]={'homogeneous_rank':homogeneous['rank'],'cocycle_dimension':4*count-homogeneous['rank'],'restricted':extension}
 if extension['consistent']:
  zs=[extension['solution'][4*j:4*j+4] for j in range(count)]
  def affine_word(word):
   M=I;v=[[0] for _ in range(4)]
   for j in word:
    v=ma(v,mm(M,[[z] for z in zs[j]]));M=mm(M,B[j])
   return [r[0] for r in v],M
  vC,MC=affine_word(list(range(count))*(count+1))
  result['B'+str(count+1)]['central_full_twist']={'translation':vC,'linear':MC}
  result['B'+str(count+1)]['generators']=list(zip(zs,B[:count]))
print(json.dumps(result,indent=2))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
K1=ma(ma(B[0],mn(I)),mn(mm(B[1],B[0])))
K2=ma(ma(I,mm(B[1],B[2])),mn(B[2]))
stack=K1+K2
for rows in itertools.combinations(range(8),4):
 g=gauss([stack[j] for j in rows],[0]*4,4)
 if g['rank']==4:
  minor={'rows_1_based':[j+1 for j in rows],'matrix':[stack[j] for j in rows]};break
result['B4_inner_certificate']={'K1':K1,'K2':K2,'invertible_minor':minor,'I_minus_A1_rank':gauss(ma(I,mn(B[0])),[0]*4,4)['rank']}
print(json.dumps(result['B4_inner_certificate'],indent=2));pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
