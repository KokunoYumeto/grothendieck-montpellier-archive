"""Explicit permanent residue tensor for the binary base t*J+diag(a_i).

This is a conditional arbitrary-size reduction, not an arbitrary-size rank
certificate.  Direct cases test the displayed uniform two-channel embedding.
"""
from itertools import combinations
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import importlib.util
import json
import time


def rank_tool():
    source = Path(__file__).parents[1]/"obstructions/test_permanent_transverse_endpoint.py"
    spec = importlib.util.spec_from_file_location("permanent_endpoint", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.rank_minor


def kernel_basis(a, prime):
    edges = [(i, j) for i in range(len(a)) for j in range(len(a)) if i != j]
    basis = [{(i, j): 1,
              (i, i): a[i]*pow(a[j]-a[i], -1, prime) % prime,
              (j, j): a[j]*pow(a[i]-a[j], -1, prime) % prime}
             for i, j in edges]
    return edges, basis


def residue_matrix(a, root, prime):
    edges, basis = kernel_basis(a, prime)

    def raw(e, f):
        i, j = e
        k, l = f
        if i == k or j == l:
            return 0
        union = {i, j, k, l}
        if root not in union:
            return 0
        value = pow(-a[root], len(union)-2, prime)
        for vertex in union-{root}:
            value = value*pow(a[vertex]-a[root], -1, prime) % prime
        return value

    matrix = [[sum(c*d*raw(e, f) for e, c in u.items() for f, d in v.items()) % prime
               for v in basis] for u in basis]
    return matrix


def two_channel_embedding(m, coefficient=2, prime=1000003):
    # Coordinates u_0,...,u_(m-1), v_0,...,v_(m-2); v_(m-1)=0.
    r = 2*m-1
    edges, _ = kernel_basis(list(range(1, m+1)), prime)
    rows = []
    for i, j in edges:
        row = [0]*r
        if i < j:
            row[i] = 1
            row[j] = coefficient
        else:
            if j < m-1:
                row[m+j] = 1
            if i < m-1:
                row[m+i] = coefficient
        rows.append(row)
    return rows


def quadratic_jacobian(matrices, embedding, prime):
    n, r = len(embedding), len(embedding[0])
    jacobian = []
    # The last residue is minus the sum of the first m-1.
    for matrix in matrices[:-1]:
        product = [[sum(matrix[u][v]*embedding[v][c] for v in range(n)) % prime
                    for c in range(r)] for u in range(n)]
        for c in range(r):
            for d in range(c, r):
                row = [0]*(n*r)
                for u in range(n):
                    row[u*r+c] += product[u][d]
                    row[u*r+d] += product[u][c]
                jacobian.append([v % prime for v in row])
    return jacobian


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[3, 4, 5, 6])
    parser.add_argument("--zero-last", action="store_true")
    parser.add_argument("--save", type=str)
    args = parser.parse_args()
    prime, rank_minor = 1000003, rank_tool()
    results = []
    for m in args.sizes:
        start = time.time()
        a = list(range(1, m+1))
        if args.zero_last:
            a[-1] = 0
        matrices = [residue_matrix(a, i, prime) for i in range(m)]
        assert all(sum(matrix[u][v] for matrix in matrices) % prime == 0
                   for u in range(m*(m-1)) for v in range(m*(m-1)))
        embedding = two_channel_embedding(m, prime=prime)
        jacobian = quadratic_jacobian(matrices, embedding, prime)
        rank, pivots, residue = rank_minor(jacobian, prime)
        result = {"m": m, "a": a, "transverse_dimension": 2*m-1,
                  "tensor_quadratic_ranks": [rank_minor(matrix, prime)[0] for matrix in matrices],
                  "square_dimension": len(jacobian), "rank": rank,
                  "selected_minor_mod_prime": residue, "seconds": time.time()-start}
        results.append(result)
        print(json.dumps(result), flush=True)
    if args.save:
        source = Path(__file__)
        certificate = {
            "date_utc": datetime.now(timezone.utc).isoformat(),
            "reviewer": "/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed",
            "run": "GCT_KRON_20261120", "prime": prime,
            "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "scope": "Finite tests of the exact conditional residue reduction; no general-size nonvanishing conclusion.",
            "results": results,
        }
        Path(args.save).write_text(json.dumps(certificate, indent=2)+"\n")


if __name__ == "__main__":
    main()
