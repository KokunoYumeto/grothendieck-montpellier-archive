"""Explicit source audit: correct one locator/content mismatch and complete-proof statuses."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'scripts/build_claims.py';s=p.read_text()
block='''# Final manual source alignment audit, after rereading the complete printed proofs.
for c in C:
    n=int(c['id'].split('-')[-1])
    if n==527:
        c.update(items=['SA14-493'],scans=[50],lines=['MPL_60_036-070_transcription.tex:273–275'],his_statement='N_p=M_p pour presque tout p∈P',statement='Let M be a finite torsion-free module over a Noetherian normal domain and let x_1,...,x_m be generically linearly independent elements. Their images in M⊗κ(p) are linearly independent for all but finitely many height-one primes p.',fate='Independently proved by extending the vectors to a generic basis and comparing the resulting free lattice N with M at height one. Stacks0AVB supplies the same height-one lattice framework. The distinct tensor determinant identity is already recorded in C-SA14-554.',present_status='As of 2026-11-19: established. The first assertion of the lemma is cut at its beginning, but its complete proof explicitly identifies the finite-exception statement; this reconstruction is labelled.',page_status_detail='The statement begins before the supplied fragment; the full argument for this first assertion is present at line275. This replaces an incorrectly anchored duplicate tensor-class specialization found during the final locator audit.',computation='No numerical computation is used. The generic-basis and finite-support argument is written in proof_notes.md §12.',attribution='reused printed proof, with the cut statement explicitly reconstructed')
    if n in [522,525,526,527,529,531,532,533,534,535,536,537]:
        c['status_on_pages']='proved there'
    if n==531:c.update(scans=[54,56],lines=['MPL_60_036-070_transcription.tex:411,486–489'])
    if n==532:c.update(scans=[54,56],lines=['MPL_60_036-070_transcription.tex:413–419,470–475'])
    if n==533:c.update(scans=[56],lines=['MPL_60_036-070_transcription.tex:468–485'])
    if n==534:c.update(scans=[52,54,56],lines=['MPL_60_036-070_transcription.tex:336,421–426,477–485'])
    if n==535:c.update(scans=[56,58],lines=['MPL_60_036-070_transcription.tex:462–466,528–534'])
'''
if '# Final manual source alignment audit' not in s:s=s.replace('def save():\n',block+'def save():\n');p.write_text(s)
p=R/'proof_notes.md';s=p.read_text()
anchor='A finite torsion-free module over a Noetherian normal domain embeds in its generic vector space.'
replacement=anchor+' For the finite-exception assertion C-SA14-527, extend the specified generically independent vectors to a generic basis contained in M. The free lattice N they generate has torsion quotient M/N. A nonzero annihilator of this finite quotient lies in only finitely many height-one primes, so N_p=M_p outside that finite set. The images of the chosen basis are then independent in M⊗κ(p), as asserted. This is the first assertion whose proof is complete on scan50; it is distinct from the tensor-class formula of C-SA14-554.'
assert anchor in s;s=s.replace(anchor,replacement);p.write_text(s)
p=R/'synthesis.md';s=p.read_text().replace('87 proof sketched;54 stated without proof;13 false as stated','12 proved there;75 proof sketched;54 stated without proof;13 false as stated');p.write_text(s)
print('Claim527 aligned to the finite-exception proof; complete printed proofs distinguished from sketches.')
