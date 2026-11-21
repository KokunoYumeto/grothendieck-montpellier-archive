"""Independent polynomial-resultant verification for A20; no producer imports."""
from pathlib import Path
import json
import sympy as s

def main():
    t = s.symbols('t')
    p = t**4+t**3+2*t+4
    quotient, remainder = s.div(t**20-1, p, domain=s.GF(3))
    expected = t**16-t**15+t**14+t**12+t**11+t**10-t**6+t**5-t**4-t**2-t-1
    assert remainder == 0 and s.Poly(quotient-expected,t,modulus=3).is_zero
    assert s.gcd(s.Poly(p,t,modulus=3),s.Poly(s.diff(p,t),t,modulus=3)).degree() == 0
    resultant = int(s.resultant(p,t**20-1,t))
    assert resultant == 1099812538656
    assert resultant % (3**4) == 0 and resultant % (3**5) != 0
    result = dict(status='PASS',method='SymPy polynomial resultant and finite-field polynomial division',
                  imports_producer=False,exponent=20,resultant=resultant,valuation_at_3=4,
                  quotient=str(quotient),squarefree_mod3=True)
    Path(__file__).with_name('three_primary_independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
