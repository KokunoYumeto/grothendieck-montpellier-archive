"""Independent finite seed check by cycle-index plethysm and character recursion.

The root calculation counts GL4 monomial weights. This certificate instead
expands h_k[h_4] in symmetric-group cycle types and evaluates the rectangular
Specht character by the Murnaghan--Nakayama implementation independently
developed in work/rectangular/verify_rectangular.py. It never imports or calls
the root weight-counting algorithm.
"""
from fractions import Fraction
from pathlib import Path
import csv
import importlib.util
import time

OUT = Path(__file__).resolve().parent
MODULE = OUT.parent / 'rectangular' / 'verify_rectangular.py'
spec = importlib.util.spec_from_file_location('rectangular_characters', MODULE)
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)


def run():
    records = []
    for k in (4, 6, 7):
        t0 = time.perf_counter()
        expansion = rc.power_sum_plethysm(k, 4)
        rectangle = (k,) * 4
        terms = [(cyc, coeff, rc.character(rectangle, cyc))
                 for cyc, coeff in sorted(expansion.items())]
        value = sum((coeff * char for _, coeff, char in terms), Fraction())
        assert value == 1, (k, value)
        detail = OUT / f'QUARTIC_SEED_k{k}_CLASS_SUM.tsv'
        with detail.open('w', newline='') as f:
            wr = csv.writer(f, delimiter='\t')
            wr.writerow(['cycle_type', 'plethysm_coefficient', 'Specht_character',
                         'contribution'])
            for cyc, coeff, char in terms:
                wr.writerow([','.join(map(str, cyc)), str(coeff), char,
                             str(coeff * char)])
        sec = time.perf_counter() - t0
        records.append([k, 4, str(rectangle), len(terms), str(value),
                        'h_k[h_4] cycle-index; Murnaghan-Nakayama', f'{sec:.3f}'])
        print(f'k={k}: {len(terms)} cycle types; multiplicity={value}; {sec:.3f}s',
              flush=True)
    with (OUT / 'QUARTIC_SEEDS_INDEPENDENT_CHECK.tsv').open('w', newline='') as f:
        wr = csv.writer(f, delimiter='\t')
        wr.writerow(['outer_k', 'inner_degree', 'rectangle', 'cycle_types',
                     'multiplicity', 'method', 'seconds'])
        wr.writerows(records)


if __name__ == '__main__':
    run()
