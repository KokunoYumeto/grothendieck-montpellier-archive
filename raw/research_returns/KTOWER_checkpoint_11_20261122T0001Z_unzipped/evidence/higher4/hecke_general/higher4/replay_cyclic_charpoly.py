"""Complete frozen Hecke replay with exact cyclic-vector charpoly certificates.

All frozen finite-model checks remain enabled. Only the characteristic
polynomial algorithm is replaced, and the replacement explicitly receives
and certifies the claimed coefficients. A missing cyclic witness fails.
"""
from pathlib import Path
import hashlib
import json
import sys
import flint
from cyclic_charpoly_certificate import certify_characteristic_polynomial

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
DRIVER = HERE/'replay_integral_faddeev.py'
driver = DRIVER.read_text()
cut = driver.rindex("exec(compile(source,str(SOURCE),'exec')")
ns = {'__file__': str(DRIVER), '__name__': 'cyclic_replay_setup'}
exec(compile(driver[:cut], str(DRIVER), 'exec'), ns)
source = ns['source']
old = ns['new_faddeev']
new = '''_cyclic_certificates = []

def characteristic_polynomial(a, claimed, e, p):
    coefficients, certificate = certify_characteristic_polynomial(a, claimed)
    certificate.update({'e':e, 'p':p})
    _cyclic_certificates.append(certificate)
    return coefficients
'''
assert source.count(old) == 1
source = source.replace(old, new)
old_call = '        poly = characteristic_polynomial(rational)\n'
new_call = "        poly = characteristic_polynomial(rational, record['charpoly_coefficients'], e, p)\n"
assert source.count(old_call) == 1
source = source.replace(old_call, new_call)
run = {'__name__': '__main__', '__file__': str(ns['SOURCE']),
       'certify_characteristic_polynomial': certify_characteristic_polynomial}
exec(compile(source, str(ns['SOURCE']), 'exec'), run)
report_path = run['args'].report
report = json.loads(report_path.read_text())
report['cyclic_characteristic_polynomial_certificates'] = run['_cyclic_certificates']
report['replay_implementation'] = {
    'wrapper_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'certificate_module_sha256': hashlib.sha256((HERE/'cyclic_charpoly_certificate.py').read_bytes()).hexdigest(),
    'frozen_verifier_sha256': hashlib.sha256(ns['SOURCE'].read_bytes()).hexdigest(),
    'integral_driver_sha256': hashlib.sha256(DRIVER.read_bytes()).hexdigest(),
    'native_backend': 'python-flint '+flint.__version__,
    'native_operations': 'integer matrix-vector multiplication and prime-field Krylov rank',
    'other_full_checks_unchanged': True,
}
report_path.write_text(json.dumps(report, indent=2)+'\n')
