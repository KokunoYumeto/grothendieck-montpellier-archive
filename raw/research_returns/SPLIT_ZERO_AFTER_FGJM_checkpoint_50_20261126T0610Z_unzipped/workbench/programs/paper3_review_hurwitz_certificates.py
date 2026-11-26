#!/usr/bin/env python3
"""Independent exact-rational audit of stored Hurwitz path geometry.

This checks coverage, endpoint identity, strict disk containment, initial
separation and the analytic domain. It does not reimplement Euler--Maclaurin.
The optional --replay flag reruns the producer's interval calculation on the
worst reported slab of each path; this is targeted replay, not independence.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]


def centre(r):
    return Q(r['centre_real']), Q(r['centre_imag'])


def squared_distance(a, b):
    x, y = centre(a)
    u, v = centre(b)
    return (x-u)**2+(y-v)**2


def main(replay=False):
    rows=[]
    initials=[]
    producer=None
    if replay:
        spec=importlib.util.spec_from_file_location(
            'producer', ROOT/'programs/paper2_interval_zeros.py')
        producer=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(producer)
    for branch in range(1,6):
        p=ROOT/f'checks/paper2_path_{branch}_interval_certificate.json'
        d=json.loads(p.read_text())
        slabs, endpoints=d['slabs'],d['endpoints']
        assert len(endpoints)==len(slabs)+1
        assert endpoints[0]==d['initial']
        initials.append(d['initial'])
        last=Q(0)
        for i,s in enumerate(slabs):
            left,right=Q(s['t_left']),Q(s['t_right'])
            mid,h=Q(s['parameter_mid']),Q(s['parameter_half_width'])
            radius=Q(s['radius'])
            assert left==last and left<right<=1
            assert mid-h==1+left and mid+h==1+right
            assert s['endpoint_index']==i+1 and s['passed']
            assert s['overlap_inclusion']
            x,y=centre(s)
            # The entire complex rectangle avoids the Hurwitz pole s=1.
            assert abs(y)>radius
            assert x-radius+2*d['M']>1
            assert d['N']+mid-h>1
            for ep,param in zip(endpoints[i:i+2],(1+left,1+right)):
                assert Q(ep['parameter_mid'])==param
                assert Q(ep['parameter_half_width'])==0 and ep['passed']
                er=Q(ep['radius'])
                assert radius>er
                # Squared comparison proves Euclidean containment without
                # square roots or floating-point arithmetic.
                assert squared_distance(ep,s)<(radius-er)**2
            last=right
        assert last==1
        worst=max(slabs,key=lambda s:Q(s['ratio_upper']))
        rec={'branch':branch,'slabs':len(slabs),
             'coverage':'exact rational partition of [0,1]',
             'endpoint_containment':'all exact rational squared comparisons pass',
             'domain':'A>1; Re(s)+2M>1; all rectangles avoid s=1',
             'maximum_reported_ratio':worst['ratio_upper'],
             'worst_slab_left':worst['t_left'],
             'worst_slab_right':worst['t_right']}
        if producer:
            z=producer.mp.mpc(worst['centre_real'],worst['centre_imag'])
            ok,r=producer.rout(z,Q(worst['parameter_mid']),
                               Q(worst['parameter_half_width']),
                               producer.mp.mpf(worst['radius']))
            assert ok
            rec['producer_interval_replay']='passed; targeted replay, not independent enclosure'
            rec['replayed_ratio_display']=r['ratio_upper']
        rows.append(rec)
    for i,a in enumerate(initials):
        for b in initials[i+1:]:
            assert squared_distance(a,b)>(Q(a['radius'])+Q(b['radius']))**2
    result={'checker':'GPT-6 Astra Pro; effort not exposed; no human check',
            'method':'independent exact-rational geometry audit plus optional targeted producer replay',
            'initial_discs_pairwise_disjoint':True,'paths':rows,
            'limitation':'Saved decimal bound strings are rounded display summaries; the producer interval comparisons provide the analytic certificate.'}
    target=ROOT/'checks/paper3_hurwitz_geometry_audit.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--replay',action='store_true')
    main(ap.parse_args().replay)
