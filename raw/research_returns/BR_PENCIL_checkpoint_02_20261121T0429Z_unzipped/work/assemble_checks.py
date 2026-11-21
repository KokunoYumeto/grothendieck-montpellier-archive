from pathlib import Path
import shutil
root=Path(__file__).resolve().parent.parent
out=root/'deliverable/checks';out.mkdir(parents=True,exist_ok=True)
files={
'pencil':['verify_global_bounds.py','global_j345_certificate.json','check_pencils.py','pencil_certificate.json','check_finite_differences.py','finite_difference_certificate.json'],
'sdp_orbits':['check_permanent_apolar_certificate.py','permanent_apolar_certificate.json','check_certificates.py','certificate.json'],
'fields_literature':['verify_five_by_two.py'],
'root':['five_by_two_extra.json']}
for directory,names in files.items():
 for name in names:shutil.copyfile(root/'work'/directory/name,out/name)
