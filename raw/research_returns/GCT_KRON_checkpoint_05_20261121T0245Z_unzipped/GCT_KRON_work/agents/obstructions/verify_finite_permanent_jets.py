"""Independently verify finite permanent-jet certificates by permutation sums."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

from test_permanent_transverse_endpoint import jacobian, rank_minor

names = sys.argv[1:] or [
    "per4_9vars_binary_jets_certificate.json",
    "per5_11vars_binary_jets_certificate.json",
]
records = []
for name in names:
    path = Path(__file__).parents[1] / "archive" / name
    witness = json.loads(path.read_text())
    best = witness.get("best", witness)
    target, matrix = jacobian(best["pencil_coefficients"])
    assert target == [tuple(e) for e in best["target_monomials"]]
    assert matrix == best["Jacobian"]
    columns = best["pivot_columns"] if "pivot_columns" in best else best["selected_columns"]
    square = [[row[j] for j in columns] for row in matrix]
    rank, _, residue = rank_minor(square, witness["prime"])
    assert rank == len(target) == len(columns)
    expected = best["selected_minor_mod_prime"] if "selected_minor_mod_prime" in best else best["minor_residue"]
    assert residue == expected != 0
    record = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "source_file": str(path),
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "m": witness["m"], "r": witness["r"],
        "rows": len(target), "columns": len(matrix[0]),
        "entries_compared_exactly": len(target)*len(matrix[0]),
        "prime": witness["prime"], "minor_residue": residue,
        "status": "PASS",
    }
    records.append(record)
    print(json.dumps(record), flush=True)

result = {
    "who_model_effort_run": "/root/saturation_obstructions; GPT-6 Astra Pro; effort not exposed; GCT_KRON_20261120",
    "type": "independent exact computation",
    "method": "Recomputed each permanent cofactor by summing all (m-1)! permutation products; multiplication truncated only above suffixdegree2, which cannot affect retained coefficients. Compared every integer Jacobian entry with the independent subset-DP witness and separately eliminated the selected square minor modulo the displayed prime.",
    "records": records,
}
output = Path(__file__).with_name("finite_permanent_jets_independent_certificate.json")
if output.exists():
    older = json.loads(output.read_text())["records"]
    latest = {record["source_file"]: record for record in older}
    latest.update({record["source_file"]: record for record in records})
    result["records"] = list(latest.values())
output.write_text(json.dumps(result, indent=2) + "\n")
