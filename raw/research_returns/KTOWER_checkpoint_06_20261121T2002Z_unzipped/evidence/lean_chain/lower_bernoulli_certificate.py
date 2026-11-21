"""Independent exact Bernoulli seeds, using only the standard library.

The three known small residual moduli are verified against the lower-weight
Eisenstein special values. Further degrees give discovery targets only;
they are not asserted to exhaust the full compact Hecke comparison.
"""
from fractions import Fraction
from math import comb,gcd,isqrt
from pathlib import Path
import json

KNOWN={26:697446897311,28:323026426255399,30:236017358500033404991}


def bernoulli_through(n):
    values=[Fraction(1)]
    for m in range(1,n+1):
        values.append(-sum((comb(m+1,j)*values[j] for j in range(m)),Fraction(0))/(m+1))
    return values


def normalized_chi3(n,B):
    return sum((Fraction(comb(n,j))*B[j]*(1-2**(n-j))*Fraction(3)**(j-1)
                for j in range(n+1)),Fraction(0))/n


def primes_through(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if a[p]:a[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if a[p]]


def main():
    degrees=(26,28,30,32,34,36);B=bernoulli_through(2*max(degrees)+1)
    primes=primes_through(100000);rows=[]
    for e in degrees:
        entry={'e':e,'scope':'exact special values; no full U3 support exhaustion assertion'}
        for label,n in [('lower',e+1),('higher',2*e+1)]:
            value=normalized_chi3(n,B);remaining=abs(value.numerator);removed={}
            for p in primes:
                exponent=0
                while remaining%p==0:remaining//=p;exponent+=1
                if exponent:removed[p]=exponent
            row={'index':n,'normalized_numerator':value.numerator,
                 'normalized_denominator':value.denominator,
                 'removed_primes_through100000':removed,'remaining_numerator':remaining}
            if label=='lower' and e in KNOWN:
                m=KNOWN[e]
                assert value.numerator%m==0
                assert gcd(m,value.denominator)==gcd(m,6)==gcd(m,1-2**e)==1
                row.update({'known_residual_modulus':m,'divides_numerator':True,
                            'denominator_gcd':1,'gcd_with6':1,
                            'gcd_with_inert_CM_test':1})
            entry[label]=row
        rows.append(entry)
        print('e',e,'lower remaining',entry['lower']['remaining_numerator'],
              'higher remaining',entry['higher']['remaining_numerator'],flush=True)
    out={'status':'PASS exact Fraction Bernoulli seeds',
         'method':'Bernoulli recurrence and full conductor-three Bernoulli-polynomial sum',
         'primality_assumed_for_moduli':False,'degrees':rows}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
