#!/usr/bin/env python3
"""T048 positive-b branch: s=3,k=K+8,b=B+1."""
from two_row_ray_certificate import main

if __name__=='__main__':
    main(point_shift=8,degree_shift=13,b_shift=1,statement='T-048',
         prefix='TWO_ROW_THREE_DEFECT',correction_kind='three_positive_b')
