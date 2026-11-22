#!/usr/bin/env python3
"""Exact integer certificates for PNEW-M11--12 from K009 + PNEW013."""
import json
from pathlib import Path


def maximum(n):
    lhs = 4**(n-1)*n**(3*n)
    rhs = (3*n-2)**(3*n-2)
    assert lhs <= rhs
    exponent = 0
    while 9*lhs <= rhs:
        lhs *= 9
        exponent += 1
    assert lhs <= rhs < 9*lhs
    return exponent


def main():
    exponents = {n: maximum(n) for n in range(2,501)}
    selected = {n: exponents[n] for n in (2,3,4,5,6,9,16,26,58,100,500)}
    assert selected == {2:0,3:0,4:1,5:1,6:2,9:4,16:10,26:18,58:45,100:81,500:427}
    data = dict(status='PASS', checked_n=[2,500],
        checked_dimensions=len(exponents), selected_upper_bounds=selected,
        all_upper_bounds=exponents,
        scope='Exact finite arithmetic for the all-n proved K009/PNEW013 corollary; actual exponent not identified.')
    target=Path(__file__).resolve().parents[1]/'certificates'/'modular_lift_range.json'
    target.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='all_upper_bounds'},indent=2))


if __name__=='__main__':
    main()
