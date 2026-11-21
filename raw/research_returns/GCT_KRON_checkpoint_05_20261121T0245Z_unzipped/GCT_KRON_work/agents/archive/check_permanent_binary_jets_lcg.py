#!/usr/bin/env python3
"""Mathematically specified LCG witnesses for A031."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from check_permanent_binary_jets import echelon_mod_prime, jacobian


def pencil(m, r, seed):
    u = seed
    coefficients = []
    for _ in range(m * m * r):
        u = (1103515245 * u + 12345) % (2**31)
        coefficients.append(u % 9 - 4)
    return [
        [coefficients[(m * i + j) * r:(m * i + j + 1) * r] for j in range(m)]
        for i in range(m)
    ]


def main():
    results = []
    for m in [3, 4, 5, 6]:
        r = 2 * m + 2
        for seed in [20261121, 20261122, 20261123]:
            A = pencil(m, r, seed)
            monomials, matrix = jacobian(A)
            rank, selected, residue = echelon_mod_prime(matrix, 1000003)
            print(m, r, seed, rank, len(monomials), residue, flush=True)
            if rank != len(monomials):
                continue
            omitted = [i for i in range(m * m * r) if i not in set(selected)]
            result = {
                "m": m, "r": r, "seed": seed, "prime": 1000003,
                "lcg_multiplier": 1103515245, "lcg_increment": 12345,
                "lcg_modulus": 2**31, "coefficient_rule": "(u_t mod9)-4 for t=1..m²r",
                "coefficient_order": "i,j,k lexicographic, flattened ((m*i+j)*r+k), zero-based",
                "pencil_coefficients": A, "target_monomials": monomials,
                "Jacobian": matrix, "rank": rank, "selected_columns": selected,
                "omitted_columns": omitted, "minor_residue": residue,
                "date_utc": datetime.now(timezone.utc).isoformat(),
                "model": "GPT-6 Astra Pro", "effort": "not exposed",
                "run": "GCT_KRON_20261120", "who": "/root/archive_finish",
                "method": "Subset-DP permanent cofactors; exact integer coefficient Jacobian; exact modular selected minor",
                "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "status": "FULL RANK",
            }
            path = Path(__file__).with_name(f"per{m}_{r}vars_lcg_certificate.json")
            path.write_text(json.dumps(result, indent=2) + "\n")
            results.append({k: result[k] for k in ["m", "r", "seed", "rank", "minor_residue", "omitted_columns"]})
            print("OMITTED", omitted, flush=True)
            break
        else:
            raise RuntimeError(f"No full-rank LCG witness for m={m}")
    Path(__file__).with_name("permanent_lcg_witness_summary.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()
