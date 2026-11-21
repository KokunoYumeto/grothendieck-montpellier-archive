"""G028 strict square-kernel targets: independent JT and full MN checks."""
from pathlib import Path
from fractions import Fraction
import json
import check_gap2_seeds_independent as jt
from verify_rectangular import power_sum_plethysm

HERE=Path(__file__).resolve().parent
cases=(((12,7,3,2,1),2),((12,5,4,3,1),1),
       ((10,8,4,2,1),3),((9,7,6,3),2))
p_expansion=power_sum_plethysm(5,5)
rows=[]
for lam,expected in cases:
    traces=[jt.trace(lam,5,cycle) for cycle in jt.CLASSES]
    value=sum(Fraction(v,jt.z(cycle)) for cycle,v in zip(jt.CLASSES,traces))
    mn=sum(coefficient*jt.character(lam,cycle) for cycle,coefficient in p_expansion.items())
    assert value==mn==expected
    rows.append(dict(partition=lam+(0,)*(5-len(lam)),traces=traces,
                     target=int(value),kernel_from_CIM=1,image=int(value)-1))
    print(lam,"JT/MN target",int(value),"image",int(value)-1,flush=True)
receipt=dict(statement="G028 four strict square-kernel target checks",status="PASS",
             power_sum_cycle_terms=len(p_expansion),rows=rows,
             method="literal JT balanced traces and independent full h5[h5] power-sum/Murnaghan-Nakayama expansion")
(HERE/"STRICT_CANONICAL_TARGET_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")

