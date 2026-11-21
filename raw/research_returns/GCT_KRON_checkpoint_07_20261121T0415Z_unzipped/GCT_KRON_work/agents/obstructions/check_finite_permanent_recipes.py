"""Verify the compact A031 recipes and the independent positive K bounds."""
from pathlib import Path
from datetime import datetime, timezone
import json

omitted = {
    3: {47,55,63} | set(range(67,72)),
    4: {77,118,129,139} | set(range(149,160)),
    5: {118,179,238,251,263,275} | set(range(282,300)),
    6: {167,251,334,419,433,447,461,474} | set(range(477,504)),
}
expected_b = {3:1,4:7,5:63,6:594}
records = []
for m in range(3,7):
    r = 2*m+2
    source = Path(__file__).parents[1]/"archive"/f"per{m}_{r}vars_lcg_certificate.json"
    data = json.loads(source.read_text())
    u = 20261121
    coefficients = []
    for c in range(m*m*r):
        u = (1103515245*u+12345) % (2**31)
        coefficients.append(u % 9 - 4)
    assert coefficients == [v for row in data["pencil_coefficients"] for entry in row for v in entry]
    assert set(range(m*m*r))-set(data["selected_columns"]) == omitted[m]
    k = 2*m*m-4*m-1
    coefficients_series = [0]*(k+1)
    coefficients_series[0] = 1
    for part in range(2,m+1):
        for degree in range(part,k+1):
            coefficients_series[degree] += coefficients_series[degree-part]
    b = coefficients_series[k]
    assert b == expected_b[m]
    r0 = 2*m+1
    eta = [r0*(m-2)+2]+[2]*(r0-1)
    beta = [k*(m-1),k]+[0]*(r0-2)
    lam = [2*m*m*(m-2)+1,2*m*m-4*m+1]+[2]*(2*m-1)
    assert [a+b for a,b in zip(eta,beta)] == lam
    assert sum(lam) == 2*m*m*(m-1)
    records.append({"m":m,"r":r,"all_source_coefficients":len(coefficients),
                    "omitted_count":len(omitted[m]),"binary_degree":k,
                    "determinant_multiplicity_lower_bound":b,
                    "weight_sum_checked":True,"status":"PASS"})
result = {
    "date_utc":datetime.now(timezone.utc).isoformat(),
    "who_model_effort_run":"/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
    "method":"Fresh LCG recurrence from the proof; exact omitted-column sets; positive coin-change product coefficients and highest-weight additions.",
    "records":records,"status":"PASS",
}
Path(__file__).with_name("finite_permanent_recipe_certificate.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
