"""Exact discovery producer using native matrix algebra and cached monomials.

All full neighbor evaluations, rational matrix identities and two extra
points are retained. Arithmetic use requires a separate full-model replay.
The original model and other running producers are left unchanged.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys, time
from flint import fmpq_mat, fmpz_mat, fmpz_poly
import flint
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'compute_higher_incremental.py'
spec=importlib.util.spec_from_file_location('native_basis_model',SOURCE)
basis=importlib.util.module_from_spec(spec);spec.loader.exec_module(basis)
model=basis.model
OUT=HERE/'fast_native';OUT.mkdir(exist_ok=True)

def matrix_json(a):
    return [[str(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]

def orbit_evaluations(k, expanded, z, w):
    pairs=sorted({pair for orbit in expanded for mon in orbit for pair in mon})
    values=[]
    for i in range(3):
        zp=[(1,0)];wp=[(1,0)]
        for _ in range(k):
            zp.append(model.emul(zp[-1],z[i]));wp.append(model.emul(wp[-1],w[i]))
        values.append({(a,b):model.emul(zp[a],wp[b]) for a,b in pairs})
    output=[]
    for orbit in expanded:
        a=b=0
        for mon in orbit:
            v=model.emul(model.emul(values[0][mon[0]],values[1][mon[1]]),values[2][mon[2]])
            a+=v[0];b+=v[1]
        output.append((a,b))
    return output

def transformed(k,expanded,H,point,neighbors):
    z,w=point;tot0=[0]*len(expanded);tot1=[0]*len(expanded)
    for neighbor in neighbors:
        zz=[];ww=[]
        for column in neighbor['columns']:
            zz.append(tuple(sum(model.econj(column[i])[j]*z[i] for i in range(3)) for j in range(2)))
            ww.append(tuple(sum(column[i][j]*w[i] for i in range(3)) for j in range(2)))
        values=orbit_evaluations(k,expanded,zz,ww)
        for i,(a,b) in enumerate(values):tot0[i]+=a;tot1[i]+=b
    v0=fmpz_mat([tot0])*H;v1=fmpz_mat([tot1])*H
    return [int(v0[0,j]) for j in range(H.ncols())],[int(v1[0,j]) for j in range(H.ncols())]

def calculate(k,primes):
    start=time.monotonic()
    source,target,expanded,lap,Hs,signs=basis.harmonic_data(k)
    points,evs=basis.choose_points(k,expanded,Hs)
    H=fmpz_mat([[int(x) for x in row] for row in Hs.tolist()])
    ev=fmpq_mat([[int(x) for x in row] for row in evs.tolist()])
    data={'status':'EXPLORATORY exact full model; independent replay pending',
      'k':k,'e':k+1,'highest_weight':[k,0,-k],'source_orbits':source,
      'target_orbits':target,'laplacian':model.matrix_json(lap),
      'harmonic_basis_columns':matrix_json(H),'swap_signs':signs,
      'evaluation_points':points,'evaluation_matrix':matrix_json(ev),
      'evaluation_determinant':str(ev.det()),'results':[],
      'neighbors_sha256':hashlib.sha256(model.NEIGHBORS.read_bytes()).hexdigest()}
    records=json.loads(model.NEIGHBORS.read_text())['results']
    for record in records:
        p=record['p']
        if p not in primes:continue
        rows0=[];rows1=[]
        for i,point in enumerate(points):
            v0,v1=transformed(k,expanded,H,point,record['neighbors'])
            rows0.append(v0);rows1.append(v1)
            if (i+1)%25==0:print('neighbor rows',k,p,i+1,len(points),'seconds',round(time.monotonic()-start,2),flush=True)
        B0=fmpq_mat(rows0);B1=fmpq_mat(rows1)
        M0=ev.solve(B0);M1=ev.solve(B1)
        assert ev*M0==B0 and ev*M1==B1
        n=len(points);rr=[]
        for i in range(n):
            row=[]
            for j in range(n):
                a,b=M0[i,j],M1[i,j]
                assert signs[i]*signs[j]*a==a-b
                assert signs[i]*signs[j]*b==-b
                if signs[i]==signs[j]:assert b==0;row.append(a)
                else:assert b==2*a;row.append(-3*a if signs[i]==1 else a)
            rr.append(row)
        rational=fmpq_mat(rr);polyq=rational.charpoly()
        assert all(c.denominator==1 for c in polyq.coeffs())
        poly=fmpz_poly([int(c) for c in polyq.coeffs()])
        extras=[((1,2,4),(3,-1,2)),((2,-3,1),(1,4,-2))]
        for point in extras:
            b0,b1=transformed(k,expanded,H,point,record['neighbors'])
            v=fmpq_mat(fmpz_mat([model.eval_orbits_integer(expanded,k,*point)])*H)
            assert v*M0==fmpq_mat([b0]) and v*M1==fmpq_mat([b1])
        content,factors=poly.factor();assert content==1
        product=fmpz_poly([1])
        for factor,m in factors:product*=factor**m
        assert product==poly
        comparison=1+p**(k+1)+p**(2*(k+1))
        row={'p':p,'dimension':n,'cosets':len(record['neighbors']),
          'scaled_operator':'p^k times negative minuscule T; same spectrum as positive by swap',
          'transformed_evaluations_0':matrix_json(B0),
          'transformed_evaluations_omega':matrix_json(B1),
          'operator_0':matrix_json(M0),'operator_omega':matrix_json(M1),
          'rational_real_form_operator':matrix_json(rational),
          'charpoly':str(poly),'charpoly_coefficients':[int(c) for c in reversed(poly.coeffs())],
          'charpoly_factors':[{'polynomial':str(f),'multiplicity':int(m),
                'coefficients':[int(c) for c in reversed(f.coeffs())]} for f,m in factors],
          'comparison_point':comparison,'comparison_value':int(poly(comparison)),
          'two_extra_evaluation_checks':True,'conjugation_similarity_checked':True}
        data['results'].append(row)
        (OUT/f'harmonic_k{k}_exact_exploration.json').write_text(json.dumps(data,indent=2)+'\n')
        print('completed prime',k,p,'degrees',[f.degree() for f,m in factors],
              'seconds',round(time.monotonic()-start,2),flush=True)
    data['elapsed_seconds']=time.monotonic()-start
    data['producer_implementation']={'native_backend':'python-flint '+flint.__version__,
       'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'basis_driver_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
       'original_model_sha256':hashlib.sha256(basis.SOURCE.read_bytes()).hexdigest(),
       'scope':'discovery; separate exact full replay required'}
    (OUT/f'harmonic_k{k}_exact_exploration.json').write_text(json.dumps(data,indent=2)+'\n')
    print('FULL_TIMING',k,data['elapsed_seconds'],flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('k',type=int)
    parser.add_argument('--primes',type=int,nargs='+',default=[7,13]);args=parser.parse_args()
    calculate(args.k,args.primes)
