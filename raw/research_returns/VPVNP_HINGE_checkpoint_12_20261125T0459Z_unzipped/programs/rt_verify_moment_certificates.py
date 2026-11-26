"""Independent semantic and rational audit including the geometric second moment.

Uses only the root author's exhaustive folded-cube enumerator.  It imports
neither a certificate generator nor an optimizer. Each new forbidden pair
is checked directly against the stated integer rectangular rank inequality.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json,sys
from rt_verify_two_minimum_certificates import geometry

W=Path(__file__).resolve().parents[1]

def verify_rectangular_violation(P,Q,ka,kb,witness):
    """Check the raw integer consequence, independently of row generation."""
    family,a,b=witness
    r,s=2**ka,2**kb
    if family=='singh':
        labels={(4,3):3,(15,11):5,(67,49):7}
        assert (a,b) in labels and Q>=labels[a,b]
        assert b*(r+s)<a*P
    else:
        assert a in(0,1)
        if a:r,s=s,r
        if family=='three':assert Q>=2 and b==2 and r+3*s<2*P
        else:assert family=='square' and 1<=b<=Q and r+b*b*s<b*P

def check(path):
    a=json.loads(path.read_text());D,m=a['D'],a['m'];n=D*m
    two='marked_distance' in a;h=a['marked_distance'] if two else 0
    lo=a['low_value'];other=a['other_low_value'] if two else None
    assert 0<=lo<=(m-2)*D-1
    if two:
        assert lo<=other<(m-1)*D
        assert 2**lo+2**other>=2**(m*(D-h))
    else:assert a['global_min'] and a['minimum_both']
    orbits,weights,triples,marks=geometry(D,h);O=len(orbits);M=2**(D-1)
    assert weights==a['weights']
    if two:
        assert [list(x) for x in orbits]==a['orbits']
        assert marks==a['marked_orbits']
    else:assert a['layers']==O
    totals={};rhs=Fraction(0);kinds={}
    def ix(term,o,t):
        assert term in(0,1) and 0<=o<O and 1<=t<=n
        return (term*O+o)*n+t-1
    for e in a['certificate']:
        c=Fraction(e['numerator'],e['denominator']);assert c>=0
        kind,*v=e['label'];b=0;kinds[kind]=kinds.get(kind,0)+1
        if kind=='monotone':
            term,o,t=v;terms=[(ix(term,o,t+1),1),(ix(term,o,t),-1)]
        elif kind=='budget':
            term,=v;terms=[(ix(term,o,t),weights[o]) for o in range(O) for t in range(1,n+1)]
            b=(m-1)*D*M-1
        elif kind=='quadratic_budget':
            term,=v
            terms=[(ix(term,o,t),weights[o]*(2*t-1)) for o in range(O) for t in range(1,n+1)]
            b=D*D*(m-1)*(m-1)*M-1
        elif kind=='mixed':
            o,p,d,orientation=v;assert(o,p,d)in triples and orientation in(0,1)
            L=m*(D-d);terms=[(ix(0,o,L-1+orientation),-1),(ix(1,p,L-orientation),-1)];b=-1
        elif kind=='strict_mixed':
            o,p,d=v;assert(o,p,d)in triples and d>=1
            assert 2**(m*d)>m*(D-d)+1
            L=m*(D-d);terms=[(ix(0,o,L),-1),(ix(1,p,L),-1)];b=-1
        elif kind=='rectangular_forbidden':
            o,p,d,ka,kb,*witness=v
            assert(o,p,d)in triples and d>=1
            assert 0<=ka<n and 0<=kb<n
            P,Q=2**(m*(D-d)),2**(m*d)
            verify_rectangular_violation(P,Q,ka,kb,witness)
            terms=[(ix(0,o,ka+1),-1),(ix(1,p,kb+1),-1)];b=-1
        elif kind=='lipschitz':
            term,o,p,t=v;assert(o,p,1)in triples and t>2*m
            terms=[(ix(term,o,t),1),(ix(term,p,t-2*m),-1)]
        elif kind=='low_cut':
            assert not two and not v;terms=[(ix(0,0,(m-2)*D),1)]
        elif kind=='exact_low_upper':
            value,=v;assert not two and value==lo;terms=[(ix(0,0,lo+1),1)]
        elif kind in('exact_low_lower','other_global_lower'):
            o,value=v;assert not two and value==lo and lo>0
            term=int(kind=='other_global_lower');terms=[(ix(term,o,lo),-1)];b=-1
        elif kind in('minimum_upper','minimum_lower'):
            term,o,value=v;assert two and value==(lo,other)[term]
            if kind=='minimum_upper':
                assert o==marks[term];terms=[(ix(term,o,value+1),1)]
            else:
                assert value>0;terms=[(ix(term,o,value),-1)];b=-1
        elif kind in('lower','upper'):
            j,=v;assert 0<=j<2*O*n;terms=[(j,1 if kind=='upper' else-1)];b=int(kind=='upper')
        else:raise AssertionError(e['label'])
        for j,z in terms:totals[j]=totals.get(j,Fraction(0))+c*z
        rhs+=c*b
    assert all(z==0 for z in totals.values()) and rhs<0
    return dict(path=str(path.relative_to(W)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                dimension=D,width=m,low=lo,other=other,distance=h,rows=len(a['certificate']),
                kinds=kinds,exact_rhs=str(rhs),status='PASS')

def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());all_checks=[];coverage=[]
    radial=json.loads((W/cfg['radial_manifest']).read_text())
    for D in cfg['dimensions']:
        m=cfg.get('width',6);radial_lows=set();remaining_lows=set();covered=set();pruned=set()
        for c in radial['cases']:
            if c['dimension']!=D:continue
            if c['certificate']:
                result=check(W/c['output']);assert result['dimension']==D and result['width']==m
                assert result['low']==c['low_value'];radial_lows.add(result['low']);all_checks.append(result)
            else:remaining_lows.add(c['low_value'])
        assert radial_lows.isdisjoint(remaining_lows)
        assert radial_lows|remaining_lows==set(range((m-2)*D))
        for rel in cfg['two_minimum_manifests']:
            manifest=json.loads((W/rel).read_text());mc=manifest['config']
            if mc['dimension']!=D:continue
            assert mc['width']==m and set(mc['first_minima'])==remaining_lows
            universe={(t,y,h) for t in remaining_lows for y in range(t,(m-1)*D) for h in range(D//2+1)}
            found={(p['first'],p['second'],p['distance'])for p in manifest['pruned']}
            assert found<=universe and len(found)==len(manifest['pruned'])
            for entry in manifest['pruned']:
                t,y,h=entry['first'],entry['second'],entry['distance']
                P,Q=2**(m*(D-h)),2**(m*h)
                if entry['reason']=='mixed-cut rank sum bound':
                    assert 2**t+2**y<P
                elif entry['reason']=='strict rectangular sum bound':
                    assert h>=1 and Q>m*(D-h)+1 and 2**t+2**y<P+1
                else:
                    assert entry['reason']=='rectangular inequality' and h>=1
                    verify_rectangular_violation(P,Q,t,y,entry['witness'])
            pruned|=found
            for stem in manifest['cases']:
                result=check(W/'outputs'/(stem+'.json'));case=(result['low'],result['other'],result['distance'])
                assert result['dimension']==D and result['width']==m and case not in covered
                covered.add(case);all_checks.append(result)
            assert covered==universe-found
        if remaining_lows:assert covered or pruned
        coverage.append(dict(dimension=D,width=m,radial_certificates=len(radial_lows),
                             remaining_first_minima=sorted(remaining_lows),
                             two_minimum_certificates=len(covered),pruned_branches=len(pruned),
                             complete=True,status='PASS'))
    output=dict(status='PASS',coverage=coverage,certificates=all_checks,
                solver_used=False,generator_imported=False,
                geometry='Independent exhaustive folded-cube enumeration')
    Path(sys.argv[2]).write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output['coverage'],indent=2))

if __name__=='__main__':main()
