#!/usr/bin/env python3
"""Exact numerical repairs of selected GCT_KRON bounds for an independent padding variable.
Python standard library only. The accompanying proof supplies the monotone
infinite tails; this checker verifies the stated finite endpoints and constants.
"""
from math import comb
from pathlib import Path
import argparse,json


def A(m,v):
    t=min(m,v)
    return (m+1)*comb(49+t,49)-49*comb(49+t,50)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output')
    args=parser.parse_args()
    assert 2**189-1<=189**25 and 2**190-1>190**25
    # M008 is independent of the permanent's row cap.
    assert (25+1)*(25+2)<2**25
    # M013 endpoint at the largest external row count m^2+1.
    m=190;jet_size=2*m*comb(m*m+12,12)
    assert jet_size<m**25
    records=[]
    for m in range(190,361):
        value=comb(49+min(360,m),49)+A(m,195)+(m*m-50)*A(m-1,195)
        slack=24*m**25-25*value
        assert slack>0
        records.append([m,value,slack])
    m=190
    square_base=(m+1)*comb(m*m+12,12)
    square_constant=m**25//square_base
    rectangular_base=(2*m+1)*comb(m*m+12,12)
    axis_size=m**25//rectangular_base
    assert square_constant==475465424 and axis_size==238356682
    out=dict(status='PASS',external_support_dimension='m^2+1',
             minimum_m=190,minimum_rows=52,
             M013_m190_size=jet_size,M013_m190_slack=190**25-jet_size,
             A025_finite_checks=len(records),A025_records=records,
             square_constant=square_constant,square_lambda2_threshold=26+square_constant//2,
             rectangular_axis_size=axis_size,rectangular_lambda2_threshold=26+axis_size,
             rectangular_endpoint_slack=m**25-axis_size*rectangular_base,
             rectangular_next_endpoint_failure=(axis_size+1)*rectangular_base-m**25)
    if args.output:Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='A025_records'}),flush=True)

if __name__=='__main__':main()
