"""Exact tests of the square Hessian map for xI+yC_m restricted to its first-jet kernel."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys
from test_permanent_transverse_endpoint import jacobian, rank_minor

prime=1000003
records=[]
for m in map(int,sys.argv[1:] or [3,4,5]):
    R=2*m-1
    r=R+2
    reference={d:(m-1,(m-1+d)%m) for d in range(m)}
    basis=[(i,(i+d)%m,reference[d]) for d in range(m) for i in range(m-1)]
    for trial in range(3):
        state=20261121+trial
        def nxt():
            global state
            state=(1103515245*state+12345)%(2**31)
            return state%9-4
        A=[[[0]*r for _ in range(m)] for _ in range(m)]
        for i in range(m):
            A[i][i][0]=1
            A[i][(i+1)%m][1]=1
        for k in range(R):
            for i,j,(i0,j0) in basis:
                value=nxt()
                A[i][j][k+2]+=value
                A[i0][j0][k+2]-=value
        target,J=jacobian(A)
        quad=[i for i,e in enumerate(target) if sum(e[2:])==2]
        low=[i for i,e in enumerate(target) if sum(e[2:])<2]
        pairs=[((m*i+j)*r+k+2,(m*i0+j0)*r+k+2)
               for k in range(R) for i,j,(i0,j0) in basis]
        Q=[[J[row][a]-J[row][b] for a,b in pairs] for row in quad]
        low_zero=all(J[row][a]-J[row][b]==0 for row in low for a,b in pairs)
        assert low_zero
        assert len(Q)==len(Q[0])==R*m*(m-1)
        rank,cols,residue=rank_minor(Q,prime)
        record={"m":m,"R":R,"trial":trial,"dimension":len(Q),"rank":rank,
                "first_jet_kernel_exact":low_zero,"pencil":A,
                "selected_columns":cols,"minor_residue":residue,
                "status":"FULL RANK" if rank==len(Q) else "DEFICIENT AT TESTED POINT"}
        records.append(record)
        print({k:v for k,v in record.items() if k not in ["pencil","selected_columns"]},flush=True)
        if rank==len(Q):break
result={"date_utc":datetime.now(timezone.utc).isoformat(),
        "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
        "prime":prime,"method":"Direct permutation-sum cofactors; first-jet kernel uses cyclic-diagonal differences; full square quadratic differential reduced modulo the displayed prime.",
        "records":records}
path=Path(__file__).with_name("cycle_restricted_hessian_results.json")
if path.exists():
    old=json.loads(path.read_text())
    existing={(t["m"],t["trial"]):t for t in old["records"]}
    existing.update({(t["m"],t["trial"]):t for t in records})
    result["records"]=list(existing.values())
path.write_text(json.dumps(result,indent=2)+"\n")

