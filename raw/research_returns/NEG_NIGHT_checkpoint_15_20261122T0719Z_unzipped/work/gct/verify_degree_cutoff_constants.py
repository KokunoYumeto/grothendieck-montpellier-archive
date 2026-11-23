"""Check only the concrete inputs to NN-G029,not its polyhedral proof/search."""
from pathlib import Path
import json
j=json.loads(Path('work/gct/dimension_certificate_3352.json').read_text())
K=max(abs(int(e)) for r in j['constants'] for e in r['trace_q'])
N0=sum(abs(v) for r in j['constants'] for v in r['trace_q'].values())
N=sum(v for r in j['constants'] for v in r['dimension_q'].values())
C=j['total_cancelling_pairs'];anchors={1}|{int(e) for r in j['constants'] for e in r['trace_q'] if int(e)>0};n=N//2+len(anchors);B=n*(K+1)*4**(n-1)
assert (K,N0,N,C,n)==(5,4443,11147,3352,5578)
assert N==N0+2*C and B<2**11170
out={'trace_degree':K,'trace_absolute_mass_including_unit':N0,
     'positive_trace_anchors':sorted(anchors),'anchor_count':len(anchors),'incumbent_cost':C,'incumbent_total_mass':N,'max_exponent_variables_with_anchors':n,
     'exact_bound_expression':str(n*(K+1))+' * 4^'+str(n-1),'strict_power_two_bound':11170,
     'bound_bit_length':B.bit_length(),
     'scope':'Numerical input check only;full elementary integer-polyhedron proof is NN-G029;no exhaustive search performed.'}
Path('work/gct/degree_cutoff_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
