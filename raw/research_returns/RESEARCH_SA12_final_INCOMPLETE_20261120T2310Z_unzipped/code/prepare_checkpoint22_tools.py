"""Prepare scheduled checkpoint22 checks without creating an archive."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
renderer=root/'code/render_checkpoint.py'
s=renderer.read_text()
marker='if number==5: pages.update(range(18,24));'
addition="""if number==22:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\\\newlabel\\{([^}]+)\\}\\{\\{[^}]*\\}\\{(\\d+)\\}',aux)}
    first=label_pages['D:SNC-tree-Brauer-geometry']
    pages.update(range(max(1,first-1),len(doc)+1))
"""
assert 'if number==22:' not in s and marker in s
renderer.write_text(s.replace(marker,addition+marker,1))

s=(root/'code/verify_checkpoint21.py').read_text()
s=s.replace('CP21','CP22').replace('checkpoint21','checkpoint22').replace('Checkpoint21','Checkpoint22').replace('CHECKPOINT21','CHECKPOINT22')
s=s.replace('build_pass134','build_pass137')
s=s.replace('RESEARCH_SA12_checkpoint_20.zip','RESEARCH_SA12_checkpoint_21.zip')
s=s.replace('2026-11-20T15:55:00+00:00','2026-11-20T16:40:00+00:00').replace('15:55UTC','16:40UTC')
s=s.replace('Review13 recorded one strict one-curve projective-count reduction; review14 is due16:10UTC.',
            'Review14 recorded one strict crown reduction, with the timestamped scope addendum included once; review15 is due17:10UTC.')
s=s.replace('Newly assembled post19 units and their exact source hashes are recorded in code/output/integrate_post19*.json.',
            'Newly assembled units and their exact source hashes are recorded in code/output/integrate_post19_post21*.json.')
old='The latest completed hourly comparison is code/output/formal_review13.json: one strict main-gate reduction, consecutive no-movement counter0. Since that review, the restricted field-permutation crown result has been proved, including its tame radial extension; these together constitute one further strict reduction to be assessed at review14,16:10UTC.'
new='The latest completed hourly comparison is code/output/formal_review14.json and its timestamped scope addendum: one strict crown-gate reduction, consecutive no-movement counter0. It includes the ordinary hereditary projective count and bounded-field projective automorphism crowns; these results cannot be counted again. The next formal review is due17:10UTC. Any subsequent main reduction is tracked separately with its exact proof and audit timestamps.'
assert old in s
s=s.replace(old,new)
(root/'code/verify_checkpoint22.py').write_text(s)
s=(root/'code/scheduled_checkpoint21.py').read_text().replace('15:55UTC','16:40UTC').replace('2026,11,20,15,55','2026,11,20,16,40').replace('checkpoint21','checkpoint22').replace("'21'","'22'")
(root/'code/scheduled_checkpoint22.py').write_text(s)
print('Prepared checkpoint22 renderer, verifier and scheduled creator; no archive created.')
