"""Exact reduced-root checks for two failed C0 norm17 choices.

This verifies finite residual-coordinate packets.  No uniform norm17 or
monodromy conclusion is asserted.  All earlier sources and outputs remain
unchanged; each original three-term Bezout identity is separately retained.
"""
from pathlib import Path
from datetime import datetime, timezone
import sys, json, time, traceback
sys.path.insert(0, '/tmp/research_sa15_flint')
from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx

start=time.perf_counter(); agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','models':[]}
try:
    inputs=[
        ('three_two_two','post_CP29_seventeen_exceptional_coordinates.json',
         'post_CP29_seventeen_zero_exceptional_gcd.json','zero'),
        ('one_four_twos','post_CP30_seventeen_four_unit_coordinates.json',
         'post_CP30_seventeen_four_unit_exceptional_gcd.json','zero_four_units')]
    for name,coordinates_file,gcd_file,model_name in inputs:
        package=json.loads((agent/'outputs'/coordinates_file).read_text())
        data=next(row for row in package['models'] if row['name']==model_name)
        cert=json.loads((agent/'outputs'/gcd_file).read_text())
        row=next(row for row in cert['factors'] if row['gcd_q_degree']>1)
        K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(package['field_modulus']))
        R=fq_default_poly_ctx(K);p=R.gen();zero,one=R.zero(),R.one()
        val=lambda n:K([(n>>i)&1 for i in range(12)])
        enc=lambda c:sum(int(v)<<i for i,v in enumerate(c.to_list()))
        dec=lambda cs:R([val(c) for c in cs])
        serial=lambda f:[enc(c) for c in f.coeffs()]
        factor=dec(row['factor'])
        def trim(a):
            a=list(a)
            while a and a[-1].is_zero():a.pop()
            return a
        def inverse(a):
            r0,r1=factor,a%factor;s0,s1=zero,one
            while not r1.is_zero():
                q,rem=divmod(r0,r1);r0,r1=r1,rem;s0,s1=s1,s0+q*s1
            assert r0.degree()==0
            return s0*(1/r0.coeffs()[0])%factor
        def add(a,b):
            return trim([((a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero))%factor for i in range(max(len(a),len(b)))])
        def scale(a,c):return trim([x*c%factor for x in a])
        def mul(a,b):
            if not a or not b:return []
            result=[zero]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):result[i+j]=(result[i+j]+x*y)%factor
            return trim(result)
        def divide(a,b):
            a=trim(a);q=[zero]*max(0,len(a)-len(b)+1);inv=inverse(b[-1])
            while len(a)>=len(b):
                shift=len(a)-len(b);lead=a[-1]*inv%factor;q[shift]=lead
                a=add(a,[zero]*shift+scale(b,lead))
            return trim(q),a
        def gcd(a,b):
            while b:a,b=b,divide(a,b)[1]
            return scale(a,inverse(a[-1]))
        f=trim([dec(c)%factor for c in row['gcd_q_coefficients']])
        derivative=trim([f[i] if i%2 else zero for i in range(1,len(f))])
        assert gcd(f,derivative)==[one]
        evaluation=zero
        for c in reversed(f):evaluation=(evaluation*p+c)%factor
        assert not evaluation.is_zero()
        pole=dec(data['l2'])
        assert pole.gcd(factor).degree()==0
        qpole=[R([c]) for c in pole.coeffs()]
        assert gcd(f,qpole)==[one]
        for coordinate in ('L','M','nu'):
            co=data['coordinates'][coordinate];n,d=dec(co['numerator']),dec(co['denominator'])
            assert d.gcd(factor).degree()==0
            nc,dc=n.coeffs(),d.coeffs()
            eq=trim([(d*(nc[i] if i<len(nc) else K(0))+n*(dc[i] if i<len(dc) else K(0)))%factor for i in range(max(len(nc),len(dc)))])
            assert not divide(eq,f)[1]
        L=data['coordinates']['L'];Lvalue=dec(L['numerator'])*inverse(dec(L['denominator']))%factor
        out['models'].append({'name':name,'factor':row['factor'],'gcd_q_coefficients':row['gcd_q_coefficients'],
            'number_of_distinct_other_x_values':len(f)-1,'packet_x_cardinality':len(f),
            'gcd_is_squarefree':True,'gcd_avoids_q_equals_p':True,'gcd_avoids_all_poles':True,
            'all_three_coordinate_equations_vanish':True,'L_at_packet_parameter':serial(Lvalue),
            'L_is_nonzero':not Lvalue.is_zero(),'source_coordinates':coordinates_file,'source_gcd_certificate':gcd_file})
    out['status']='PASS_EXACT_REDUCED_COORDINATE_PACKETS'
    out['scope']='The selected C0 maps have respectively five and three distinct nonpole x parameters sharing all three residual Mumford coordinates L,M,nu. L is checked nonzero. This is a retained obstruction to these two nodality attempts, not an obstruction to all multiplier17 maps.'
except Exception:
    out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    target=agent/'outputs/post_CP30_seventeen_C0_packet_obstructions.json'
    assert not target.exists()
    target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
