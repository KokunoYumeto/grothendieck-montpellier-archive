#!/usr/bin/env python3
"""Record actual root whole readings, then preserve the checked fragments in main."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
scopes={
 59:'Read the COMPLETE final intended theorem, exact-input declarations and full proof in one untruncated tool output. Checked rigidified Poincare and Rosati identities, split principal level, isotropic kernels and symmetric odd-order lifts, C-deck compatibility, cohomology base change and integral determinant basis, formal isogeny jet surjectivity, basis expansion, exact factorial lower bound and integral valuation group, and every generic IsVtOver versus old CM-type qualification. Reviewed the four internal-reference editorial replacements and URL formatting; all mathematical content is preserved from the already whole-read memo.',
 60:'Read the COMPLETE final memo (03:56 UTC previous context) and COMPLETE intended theorem and proof (current context, untruncated tool output). Checked modulo-p precision and strict error gap at odd p, the exact harmonic factorial identity and product errors, finite residue-class generator choice, denominator clearing by algebraic integers outside the selected prime, CRT and bounded residue representatives, all tensor degrees, global integral nonzero interpolant, fixed-metric sup estimates at all places, linear square powers and remaining source-normalization and selected-family qualifications.'
}
files={59:['theta_translate_span_DP59.md','DP59_integrated_fragment.tex'],60:['linear_height_theta_sections_DP60.md','DP60_integrated_fragment.tex']}
main=root/'DP_MULT.tex';text=main.read_text()
anchor='\\section{Cote 54, Cartier duality, and the crystalline setting}'
assert text.count(anchor)==1
for n in (59,60):
 fragment=(root/'research'/f'DP{n}_integrated_fragment.tex').read_text()
 assert fragment.count('\\begin{proof}')==1 and fragment.count('\\end{proof}')==1
 if f'\\label{{DP{n}}}' not in text:
  text=text.replace(anchor,fragment+'\n\n'+anchor)
 else: assert text.count(fragment)==1
 data={'statement':f'DP{n}','recorded_utc':now,'who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','type':'targeted proof check','scope':scopes[n],'outcome':'PASS complete proof and intended integration preservation; mathematical reading, not Lean or other formal verification.','time_note':'Recorded after the actual complete readings; individual subparagraph reading times were not logged.','files':[{'path':f,'sha256':hashlib.sha256((root/'research'/f).read_bytes()).hexdigest()} for f in files[n]]}
 (root/'research'/f'DP{n}_root_integrated_review_metadata.json').write_text(json.dumps(data,indent=2)+'\n')
main.write_text(text)
print(json.dumps({'recorded_utc':now,'integrated':[59,60],'main_bytes':main.stat().st_size,'fragment_counts':{str(n):text.count((root/'research'/f'DP{n}_integrated_fragment.tex').read_text()) for n in (59,60)}}))
