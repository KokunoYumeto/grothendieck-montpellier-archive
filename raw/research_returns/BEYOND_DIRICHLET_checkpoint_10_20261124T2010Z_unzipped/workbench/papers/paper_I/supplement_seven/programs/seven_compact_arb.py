#!/usr/bin/env python3
"""Independent tower-coordinate regulator and residue-character verification.

Uses the compact unit witness, not a BNF or expanded degree-21 unit polynomials.
The seven cubic-twist values are the separately checked finite-sum certificate.
"""
import json
from pathlib import Path
from flint import arb, acb, acb_poly, arb_mat, ctx

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "certificates/seven_compact_units.json"
LVALUES = ROOT / "analytic/certificate.json"
OUTPUT = ROOT / "certificates/seven_compact_arb.json"


def horner_ascending(coefficients, value):
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def determinant_mod(matrix, prime):
    matrix = [row[:] for row in matrix]
    answer = 1
    for j in range(len(matrix)):
        pivot = next(i for i in range(j, len(matrix)) if matrix[i][j] % prime)
        if pivot != j:
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            answer = -answer
        value = matrix[j][j] % prime
        answer = answer * value % prime
        inverse = pow(value, -1, prime)
        for i in range(j+1, len(matrix)):
            scalar = matrix[i][j] * inverse % prime
            matrix[i] = [(a-scalar*b) % prime
                         for a, b in zip(matrix[i], matrix[j])]
    return answer % prime


def unit_values(data, alpha, beta, divide):
    values = [divide(horner_ascending(coefficients, beta), denominator)
              for coefficients, denominator in
              zip(data["small_unit_numerators_ascending"],
                  data["small_unit_denominators"])]
    values.append(horner_ascending(data["cubic_unit_numerator_ascending"], alpha))
    for _ in range(6):
        eta = sum(data["orbit_seed_numerators_alpha_first"][3*j+i]
                  * alpha**i * beta**j for j in range(7) for i in range(3))
        values.append(divide(eta, data["orbit_seed_denominator"]))
        beta = divide(horner_ascending(
            data["period_automorphism_numerator_ascending"], beta),
            data["period_automorphism_denominator"])
    return values


def main():
    data = json.loads(DATA.read_text())
    lvalues = json.loads(LVALUES.read_text())
    rows = []
    for prime, root, zeta in data["prime_root_zeta_witnesses"]:
        assert prime % 7 == 1 and pow(zeta, 7, prime) == 1 and zeta != 1
        divide = lambda a, b: a * pow(b, -1, prime) % prime
        alpha = divide(horner_ascending(
            list(reversed(data["cubic_fraction_numerator_descending"])), root),
            horner_ascending(list(reversed(
                data["cubic_fraction_denominator_descending"])), root))
        beta = (alpha-root) % prime
        assert pow(alpha, 3, prime) == 269 % prime
        assert horner_ascending(list(reversed(
            data["period_polynomial_descending"])), beta) % prime == 0
        logs = {pow(zeta, k, prime): k for k in range(7)}
        rows.append([logs[pow(value % prime, (prime-1)//7, prime)]
                     for value in unit_values(data, alpha, beta, divide)])
    assert rows == data["residue_matrix_rows"]
    assert determinant_mod(rows, 7) == 1

    ctx.prec = 2048
    period_polynomial = acb_poly(list(reversed(data["period_polynomial_descending"])))
    betas = period_polynomial.roots(tol=arb(2)**-1950, maxprec=4096)
    assert len(betas) == 7 and all(beta.imag.contains(0) for beta in betas)
    assert all(sum(beta.overlaps(other) for other in betas) == 1 for beta in betas)
    betas = [acb(beta.real) for beta in betas]
    real_alpha = acb((arb(269).log()/3).exp())
    complex_alpha = real_alpha * acb(-arb(1)/2, arb(3).sqrt()/2)
    assert (real_alpha**3).contains(269) and (complex_alpha**3).contains(269)
    real_rows = [[abs(value).log() for value in
                  unit_values(data, real_alpha, beta, lambda a,b: a/b)]
                 for beta in betas]
    complex_rows = [[2*abs(value).log() for value in
                     unit_values(data, complex_alpha, beta, lambda a,b: a/b)]
                    for beta in betas]
    regulator = abs(arb_mat(real_rows[:-1]+complex_rows).det())
    assert regulator > 0 and regulator.rel_accuracy_bits() > 200

    # Independent pairing and the exact Gauss-sum simplification modulo 49.
    logs49 = {pow(3,k,49): k % 7 for k in range(42)}
    z49 = (acb(0,2)*arb.pi()/49).exp()
    z7 = z49**7
    residue = arb(1)
    for j, exponent in ((1,48),(2,19),(3,18)):
        tau = 7*z49**exponent
        finite = sum(z7**(-j*logs49[a])
                     * (2*(arb.pi()*a/49).sin()).log()
                     for a in range(1,49) if a % 7)
        value = -tau*finite/49
        residue *= value.real**2+value.imag**2
    base_epsilon = 270-739*real_alpha+108*real_alpha**2
    base_regulator = abs(abs(base_epsilon).log())
    base_quotient = (arb(lvalues["base_L1"])*arb(217083).sqrt()
                     / (2*arb.pi()*base_regulator))
    assert base_regulator > 0 and base_regulator < 18
    assert base_quotient.contains(7) and abs(base_quotient-7).upper()*72 < 1
    assert pow(444,3,491) == 269 and (270-739*444+108*444**2) % 491 == 88
    assert pow(138,7,491) == 1 and pow(88,70,491) == 223 != 1
    relative_product = arb(lvalues["product_L1_j0_to_j6"])
    quotient = (relative_product*residue*arb(217083**7*7**36).sqrt()
                / (2**13*arb.pi()**7*regulator))
    index_bound = (4*regulator).upper().ceil()
    separation = abs(quotient-7).upper()*index_bound
    assert quotient.contains(7) and separation < 1
    report = {
        "status": "PASS",
        "regulator_method": "tensor embeddings of the cubic and cyclic-seven fields; compact orbit units",
        "precision_bits": ctx.prec,
        "residue_character_determinant_mod7": 1,
        "base_regulator": base_regulator.str(80),
        "base_class_number_divided_by_unit_index": base_quotient.str(65),
        "base_unit_subgroup_7_saturated": True,
        "regulator": regulator.str(80),
        "regulator_accuracy_bits": regulator.rel_accuracy_bits(),
        "cyclic_seven_zeta_residue": residue.str(80),
        "class_number_divided_by_unit_index": quotient.str(65),
        "unit_index_upper_bound": index_bound.str(30),
        "error_times_index_bound": separation.str(20),
        "conclusion": "h/unit_index=7 exactly; 7 does not divide unit_index; Cl(F1){7}=C7",
        "BNF_class_number_used": False,
        "BNF_regulator_used": False,
    }
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
