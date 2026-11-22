"""One exact two-sign discriminator; no bounded-census or uniform assertion."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

from explicit_two_unit_certificate import (
    bernoulli_numbers, direct_teichmuller_residue, jacobi,
    normalized_bernoulli, rational_residue,
)


def main():
    p = 43
    values = bernoulli_numbers(23)
    rows = []
    for sign in (1, -1):
        m = p + 4 * sign
        f = p * m
        chi = [jacobi(a, m) for a in range(m)]
        chi_real = [jacobi(a, f) for a in range(f)]
        assert sum(chi_real) == 0
        assert sum(a * chi_real[a] for a in range(f)) == 0
        beta2 = Fraction(sum(a * a * chi_real[a] for a in range(f)), 2 * f)
        beta23 = normalized_bernoulli(23, chi, values)
        beta3 = normalized_bernoulli(3, chi, values)
        beta1 = normalized_bernoulli(1, chi, values)
        teich = direct_teichmuller_residue(p, chi, 22)
        assert teich == rational_residue(beta2, p)
        assert teich == rational_residue(beta23, p)
        rows.append({
            "sign": sign, "D": -m, "real_discriminant": f,
            "h_imag": str(-beta1), "beta2_real_exact": str(beta2),
            "beta23_imag_exact": str(beta23), "beta3_imag_exact": str(beta3),
            "first_residue": teich, "third_residue": rational_residue(beta3, p),
        })
    assert rows[1]["beta2_real_exact"] == "2752"
    assert rows[1]["first_residue"] == 0
    assert rows[0]["first_residue"] != 0
    report = {
        "finding_id": "KT-RD-BETA2-NONIMPLICATION", "p": p,
        "scope": "Exact discriminator of automatic beta2 nonvanishing from the explicit Richaud-Degert norm-one unit; the two-choice family is not disproved. No range claim and no main arithmetic movement.",
        "rows": rows,
        "normalizations": "beta_j=B_(j,chi)/j; real character is primitive Kronecker character of p*|D|.",
        "method": "Independent exact Bernoulli-polynomial values and direct conductor-p|D| Teichmuller sum, using already reviewed helper functions.",
        "helper_sha256": sha256(Path(__file__).with_name("explicit_two_unit_certificate.py").read_bytes()).hexdigest(),
        "status": "PASS",
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
