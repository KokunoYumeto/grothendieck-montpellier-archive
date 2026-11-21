#!/usr/bin/env python3
"""T046: c=2k-2,k=K+5; exact pair-line correction and positive count."""
from two_row_ray_certificate import main

if __name__=='__main__':
    main(point_shift=5,degree_shift=8,statement='T-046',prefix='TWO_ROW_LINE_CORRECTION',with_pair_correction=True)
