#!/usr/bin/env python3
"""T045: c=2k-1, k=K+2 >=2; exact positive residue certificate."""
from two_row_ray_certificate import main

if __name__=='__main__':
    main(point_shift=2,degree_shift=3,statement='T-045',prefix='TWO_ROW_BELOW_RAY')
