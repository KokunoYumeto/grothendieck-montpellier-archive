"""Explore connected binary cycle bases for permanent transverse-two jets."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sys
from test_permanent_transverse_endpoint import jacobian,rank_minor

records=[]
for m in map(int,sys.argv[1:] or [3,4,5,6]):
    r=2*m+2
    trials=[]
    for trial in range(3):
        state=20261121+trial
        pencil=[[[0]*r for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                pencil[i][j][0]=int(i==j)
                pencil[i][j][1]=int(j==(i+1)%m)
                for k in range(2,r):
                    state=(1103515245*state+12345)%(2**31)
                    pencil[i][j][k]=state%9-4
        target,J=jacobian(pencil)
        rank,columns,residue=rank_minor(J,1000003)
        trials.append({"trial":trial,"rank":rank})
        print({"m":m,"r":r,"target":len(target),"trial":trial,"rank":rank},flush=True)
        if rank==len(target):break
    records.append({"m":m,"r":r,"target_dimension":len(target),
                    "trials":trials,"last_pencil":pencil,
                    "selected_columns":columns,"minor_residue":residue,
                    "status":"FULL RANK" if rank==len(target) else "RANK DEFICIENT AT TESTED POINTS"})
result={"date_utc":datetime.now(timezone.utc).isoformat(),
        "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
        "method":"Binary pencil xI+yC_m, C_m directed cycle; transverse labels from displayed LCG; explicit permutation-sum cofactors and exact modular rank.",
        "prime":1000003,"records":records}
Path(__file__).with_name("connected_cycle_binary_base_results.json").write_text(json.dumps(result,indent=2)+"\n")
