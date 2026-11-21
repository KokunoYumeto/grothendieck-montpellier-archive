"""Complete frozen replay with native integer products in Faddeev recursion.

The independent orbit, harmonic-kernel, identifying-point, all-neighbor,
matrix-similarity and extra-point checks are unchanged. Characteristic
polynomials use explicit Faddeev recursion, not the producer's charpoly
routine. Every integer trace division and the final zero matrix is checked.
"""
from pathlib import Path
import hashlib,json,sys
import flint
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
DRIVER=HERE/'replay_integral_faddeev.py'
driver=DRIVER.read_text()
cut=driver.rindex("exec(compile(source,str(SOURCE),'exec')")
ns={'__file__':str(DRIVER),'__name__':'native_replay_setup'}
exec(compile(driver[:cut],str(DRIVER),'exec'),ns)
source=ns['source'];old=ns['new_faddeev']
new='''def characteristic_polynomial(a):
    from math import lcm
    from flint import fmpz_mat
    n=len(a)
    denominator=lcm(*(x.denominator for row in a for x in row))
    integral=[[x.numerator*(denominator//x.denominator) for x in row]
              for row in a]
    assert all(F(integral[i][j],denominator)==a[i][j]
               for i in range(n) for j in range(n))
    aa=fmpz_mat(integral)
    b=fmpz_mat(identity(n))
    coefficients=[F(1)]
    for k in range(1,n+1):
        b=aa*b
        quotient,remainder=divmod(sum(int(b[i,i]) for i in range(n)),k)
        assert remainder==0
        c=-quotient
        coefficients.append(F(c,denominator**k))
        for i in range(n):b[i,i]+=c
    assert b==fmpz_mat(n,n)
    return coefficients
'''
assert source.count(old)==1
source=source.replace(old,new)
run={'__name__':'__main__','__file__':str(ns['SOURCE'])}
exec(compile(source,str(ns['SOURCE']),'exec'),run)
report_path=run['args'].report
report=json.loads(report_path.read_text())
report['replay_implementation']={
 'wrapper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'frozen_verifier_sha256':hashlib.sha256(ns['SOURCE'].read_bytes()).hexdigest(),
 'integral_driver_sha256':hashlib.sha256(DRIVER.read_bytes()).hexdigest(),
 'native_backend':'python-flint '+flint.__version__,
 'native_operation':'integer matrix multiplication only inside explicit Faddeev recursion',
 'other_full_checks_unchanged':True,
}
report_path.write_text(json.dumps(report,indent=2)+'\n')
