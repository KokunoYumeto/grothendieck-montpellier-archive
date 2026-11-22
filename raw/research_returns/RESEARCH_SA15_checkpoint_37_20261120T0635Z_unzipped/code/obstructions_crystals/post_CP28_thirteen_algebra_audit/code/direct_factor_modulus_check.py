"""Independent binary-only identities for the exploratory norm-thirteen data."""
from pathlib import Path
from datetime import datetime, timezone
import json
from post_CP27_binary_coefficient_ring import cmul, factor_power

agent = Path(__file__).resolve().parents[1]
raw = json.loads((agent / "outputs/post_CP28_thirteen_parameter_probe.json").read_text())
checks = []
for row in raw["stages"]:
    if "factorization" in row:
        value = 1
        for factor in row["factorization"]:
            value = cmul(value, factor_power(int(factor["factor_hex"], 16), factor["exponent"]))
        assert value == int(row["polynomial_hex"], 16)
        checks.append(row["stage"])
D = (1 << 12) | (1 << 9) | (1 << 6) | (1 << 3) | 1
H = (1 << 4) | (1 << 1)
mu_one = factor_power(D, 5) ^ factor_power(H, 12)
assert mu_one == int(raw["stages"][-1]["gcd_hex"], 16)
result = {
    "status": "PASS_BINARY_FACTOR_PRODUCTS_AND_MODULUS_ONE_IDENTITY",
    "actual_utc": datetime.now(timezone.utc).isoformat(),
    "factor_products": checks,
    "gcd_is_exactly_D12_power5_plus_H4_power12": True,
    "degree": mu_one.bit_length() - 1,
    "scope": "Exact algebra supplement only; no exceptional-fibre or norm-thirteen theorem.",
}
dest = agent / "outputs/direct_factor_modulus_check_retained.json"
dest.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
