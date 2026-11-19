"""Reconcile the earlier question with the now-read IX95–97 correction.

Authored assessment, not an automatic proof checker. Only this part is edited.
The original early source statement and occurrences remain intact.
"""
from pathlib import Path
import json

P=Path(__file__).parent
f=P/'curated_zzz_completion.py'
s=f.read_text()
start=s.index("Pstate('9-08',")
end=s.index('\n\n# Add only observed',start)
new="""Pstate('9-08','The unrestricted closure formula fails by C-SA21-9-030R; the author’s nonsurjective injection refutes the stronger complement formula only. The author subsequently repairs the criterion in Proposition4, IX95–97: for any correspondence alpha:E→P(F), pretranspose existence, commutation with double-polar closure on every subset, closed orthogonality fibers, and preservation of arbitrary joins PLUS alpha*(cl_E{x})=cl_F(alpha(x)) for every x are equivalent. The inserted generator condition is at J156-9-12:253–257 and is explicitly acknowledged as an afterthought at351–355; the complete argument at242–355 has now been checked directly. See C-SA21-9-038/054 and MP-SA21-9-10 for the continuation. Paseka–Vetterlein2025 Definition3.1, Lemmas3.5–3.7 and Theorem6.7 supply a later comparison for adjointable single-valued maps, not an automatic identification of the full atelier-morphism theory. This is an internally answered question after correction, not a still-unread continuation.',
 'Worth comparing the corrected correspondence criterion with later adjointability, while retaining the independent distinction between closure commutation, preservation of joins and preservation of complement.', ['PasekaVetterlein2025','Birkhoff1948'],
 'The early proof is crossed out on IX63–64; the stronger formula fails on IX65. Proposition4 on IX95–97 supplies the missing generator hypothesis and completes the corrected equivalence.')"""
s=s[:start]+new+s[end:]
old_marker="p['state_of_art']=p['state_of_art'].replace("
start=s.index(old_marker) if old_marker in s else s.index("p['plausible_today']='For disjoncteurs E,F")
end=s.index("\nL('folder','156-9 scans63–65",start)
s=s[:start]+"""p['plausible_today']='For disjoncteurs E,F and alpha:E→P(F), write c_E,c_F for double-polar closure, alpha_bar(A)=union_{x in A}alpha(x), and f(S)=c_F(alpha_bar(S)) on closed S. Then alpha has a pretranspose iff c_F alpha_bar c_E=c_F alpha_bar on every subset iff each orthogonality fiber {x:alpha(x) orthogonal y} is c_E-closed iff f preserves all joins, including the empty join, and f(c_E{x})=c_F(alpha(x)) for every x. The extra generator equality cannot be dropped; this criterion does not imply complement preservation.'
"""+s[end:]
s=s.replace('Earlier failed formulas read here; later endpoint checked and reported by cotes_156_3_5. Its full corrected Proposition4 belongs to that reader’s claim record.', 'Both endpoints now read directly: IX95 conditions and IX96–97 proof at J156-9-12:242–355, including the inserted generator equality and the author’s explicit acknowledgment. The full corrected proposition is C-SA21-9-054; early and late versions remain distinct records.')
f.write_text(s)
f=P/'narrative.md';s=f.read_text()
s=s.replace('IX09–13 and IX14–18 are assigned to the other two readers; their continuations must be merged before making claims about the author\'s final answer in chapter IX.', 'IX09–13 and IX14–18 are assigned to the other two readers; their completed continuations are cross-referenced here. The late corrected Proposition4 at IX95–97 and the support question at IX124 have additionally been checked directly at the exact endpoints.')
f.write_text(s)
print(json.dumps({'updated':['curated_zzz_completion.py','narrative.md'],'problem':'MP-SA21-9-08','late_source':'J156-9-12_transcription.tex:242–355','preserved':'original early statement and early failure; later corrected theorem separately identified'},ensure_ascii=False,indent=2))
