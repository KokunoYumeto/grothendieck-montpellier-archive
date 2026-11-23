"""Exact rational certificate and independent numerical identities for ALP-LIFT-02.

The theorem is proved symbolically in lift_accounting.md. The rational certificate
uses only fractions, a positive atanh series, and an explicit integral tail bound.
The mpmath values are labelled numerical cross-checks, not proof certificates.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import mpmath as mp


def log1p_bounds(x, terms=6):
    assert x >= 0
    t = x / (2 + x)
    lower = 2 * sum((t ** (2*k+1) / (2*k+1) for k in range(terms)), F(0))
    rem = 2 * t ** (2*terms+1) / ((2*terms+1) * (1-t*t))
    return lower, lower + rem


def exact_certificate(N=100):
    low, high = F(0), F(0)
    for n in range(N):
        x = F(14*n+7, (7*n+2)*(7*n+4)**3)
        a,b = log1p_bounds(x)
        low += a
        high += b
    # The nth logarithm is a third finite difference of log at step one.
    # It lies between 2/(7*n+5)^3 and 2/(7*n+2)^3.
    # Integral comparison for the decreasing tails supplies these bounds.
    low += F(1, 7*(7*N+5)**2)
    high += F(1, 7*(7*N-5)**2)
    claim_low, claim_high = F(5568702,100000000), F(5568705,100000000)
    assert claim_low < low < high < claim_high
    return {
        "N": N,
        "atanh_terms": 6,
        "certified_decimal_lower": "0.05568702",
        "certified_decimal_upper": "0.05568705",
        "rational_lower_floor_times_1e12": (low.numerator*10**12)//low.denominator,
        "rational_upper_ceil_times_1e12": (high.numerator*10**12+high.denominator-1)//high.denominator,
        "exact_fraction_bit_lengths": {"lower_numerator":low.numerator.bit_length(),"lower_denominator":low.denominator.bit_length(),"upper_numerator":high.numerator.bit_length(),"upper_denominator":high.denominator.bit_length()},
        "assertions_passed": True,
    }


def numerical_crosscheck():
    mp.mp.dps = 80
    x = {a:mp.loggamma(mp.mpf(a)/7) for a in range(1,7)}
    delta = x[2]+3*x[4]-3*x[3]-x[5]
    z3 = -mp.log(7)+x[1]+x[2]-x[3]+x[4]-x[5]-x[6]
    z1r = -mp.log(7)+x[1]+x[2]/4+5*x[3]/4-5*x[4]/4-x[5]/4-x[6]
    hind = -mp.mpf(3)/2*z3-mp.mpf(3)/4*mp.log(7)
    hj = -mp.mpf(4)/3*z1r-mp.mpf(1)/6*z3-mp.mpf(3)/4*mp.log(7)
    hw = mp.log(7)-mp.mpf(3)/2*mp.log(mp.pi)+mp.mpf(3)/14*mp.log(2)-sum(
        mp.loggamma(mp.mpf(2*j-1)/14)-mp.loggamma(mp.mpf(j+3)/7)
        for j in range(1,4))
    hodge = []
    for i in range(1,4):
        a=mp.mpf(i)/7
        v=2*mp.pi/7*mp.gamma(a)*mp.gamma(mp.mpf(1)/2-a)/(mp.gamma(1-a)*mp.gamma(mp.mpf(1)/2+a))
        hodge.append(mp.nstr(v,65))
    assert abs(hj-hind-delta)<mp.mpf('1e-70')
    assert abs(hw+mp.mpf(3)/2*mp.log(mp.pi)-hj)<mp.mpf('1e-70')
    # Exact rational type autocorrelations and their character expansions.
    phi={0,1,2}
    psi={0,2,4}
    pairchar=[2,1,-1,-2,-1,1]
    quad=[1,-1,1,-1,1,-1]
    corr=[]
    for k in range(6):
        a=F(sum((j-k)%6 in phi for j in phi),6)
        b=F(sum((j-k)%6 in psi for j in psi),6)
        assert a == F(1,4)+F(pairchar[k],9)+F(quad[k],36)
        assert b == F(1,4)+F(quad[k],4)
        corr.append({"k":k,"A_phi":str(a),"A_ind":str(b)})
    return {
        "precision_decimal_digits":80,
        "delta":mp.nstr(delta,65),
        "h_J_Yang_metric":mp.nstr(hj,65),
        "h_ind_Yang_metric":mp.nstr(hind,65),
        "h_J_Wilms_metric":mp.nstr(hw,65),
        "hodge_norm_squared":hodge,
        "type_autocorrelation_exact":corr,
        "numerical_checks_passed":True,
    }


if __name__ == '__main__':
    result={"rational_certificate":exact_certificate(),"numerical_crosscheck":numerical_crosscheck()}
    dst=Path(__file__).with_name('colmez_height_certificate.json')
    dst.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"file":str(dst),"certified_interval":[result['rational_certificate']['certified_decimal_lower'],result['rational_certificate']['certified_decimal_upper']],"delta":result['numerical_crosscheck']['delta'],"checks":"passed"},indent=2))
