#!/usr/bin/env python3
"""Exact rational arithmetic for the SH33 contraction gates."""
from fractions import Fraction as F
from pathlib import Path
import json
import sys

cfg=json.loads(Path(sys.argv[1]).read_text())
epsilon=F(cfg['distance_error']);lam=F(cfg['lambda_lower'])
assert 433**2<3*250**2 and 283**2>2*200**2
assert 2*F(433,250)-F(283,200)-2==lam
assert 5+F(283,200)+6*epsilon<F(13,2)
assert 6+F(283,200)+7*epsilon<F(15,2)
seven=3*lam-21*epsilon;eight=4*lam-28*epsilon
seven_charge=F(13,2)*F(cfg['seven_exponent'])
eight_charge=F(15,2)*16*F(cfg['balanced_exponent_per_r_squared'])
assert seven>seven_charge and eight>eight_charge
result={'config':cfg,'seven_defect_lower':str(seven),
        'seven_scale_upper':'13/2','seven_charge_upper':str(seven_charge),
        'seven_margin':str(seven-seven_charge),
        'eight_defect_lower':str(eight),'eight_scale_upper':'15/2',
        'eight_charge_upper_per_t_squared':str(eight_charge),
        'eight_margin_per_t_squared':str(eight-eight_charge),
        'all_comparisons_exact':True}
Path(sys.argv[2]).write_text(json.dumps(result,indent=2));print(json.dumps(result))
