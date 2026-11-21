"""Exact exploratory ranks for generic binary labels on connected supports."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sys
from test_permanent_transverse_endpoint import jacobian,rank_minor

records=[]
for m in map(int,sys.argv[1:] or [3,4]):
    r=2*m+2
    for mode in ["generic_cycle","generic_cycle_one_chord"]:
        state=20261121
        def next_int():
            global state
            state=(1103515245*state+12345)%(2**31)
            return state%9-4
        pencil=[[[0]*r for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                support=i==j or j==(i+1)%m or (mode.endswith("one_chord") and (i,j)==(0,2))
                if support:
                    pencil[i][j][:2]=[next_int(),next_int()]
                    if pencil[i][j][:2]==[0,0]:pencil[i][j][0]=1
                for k in range(2,r):pencil[i][j][k]=next_int()
        target,J=jacobian(pencil)
        rank,columns,residue=rank_minor(J,1000003)
        record={"m":m,"r":r,"mode":mode,"target_dimension":len(target),
                "rank":rank,"pencil":pencil,"selected_columns":columns,
                "minor_residue":residue,"status":"FULL RANK" if rank==len(target) else "RANK DEFICIENT AT TESTED POINT"}
        records.append(record)
        print({k:v for k,v in record.items() if k not in ["pencil","selected_columns"]},flush=True)
path=Path(__file__).with_name("sparse_connected_binary_base_results.json")
if path.exists():
    older=json.loads(path.read_text())["records"]
    latest={(r["m"],r["mode"]):r for r in older}
    latest.update({(r["m"],r["mode"]):r for r in records})
    records=list(latest.values())
result={"date_utc":datetime.now(timezone.utc).isoformat(),
        "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
        "method":"Generic binary forms on a directed cycle and diagonals, optionally one chord; transverse coefficients from displayed LCG; explicit permutation cofactors and exact modular rank.",
        "prime":1000003,"records":records}
path.write_text(json.dumps(result,indent=2)+"\n")
