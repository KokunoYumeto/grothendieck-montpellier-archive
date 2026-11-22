"""Prepare the next scheduled checkpoint; this script never creates an archive."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'code/render_checkpoint.py';s=p.read_text();marker='if number==5: pages.update(range(18,24));'
addition="""if number==23:
    pages={1,3,5,8,25,45,65,85,105,125,145,165,185,205,225,245,265,285,305,325,346,len(doc)}
    aux=(root/'build/RESEARCH_SA12_paper.aux').read_text()
    label_pages={key:int(page) for key,page in re.findall(r'\\\\newlabel\\{([^}]+)\\}\\{\\{[^}]*\\}\\{(\\d+)\\}',aux)}
    first=label_pages['D:normal-subgroup-projective-crowns']
    pages.update(range(max(1,first-1),len(doc)+1))
"""
assert 'if number==23:' not in s and marker in s;p.write_text(s.replace(marker,addition+marker,1))
s=(root/'code/verify_checkpoint22.py').read_text()
s=s.replace('CP22','CP23').replace('checkpoint22','checkpoint23').replace('Checkpoint22','Checkpoint23').replace('CHECKPOINT22','CHECKPOINT23')
s=s.replace('build_pass137','build_pass147').replace('RESEARCH_SA12_checkpoint_21.zip','RESEARCH_SA12_checkpoint_22.zip')
s=s.replace('2026-11-20T16:40:00+00:00','2026-11-20T17:25:00+00:00').replace('16:40UTC','17:25UTC')
s=s.replace('Review14 recorded one strict crown reduction, with the timestamped scope addendum included once; review15 is due17:10UTC.',
 'Review15 recorded two strict main-gate reductions, each counted once; review16 is due18:10UTC.')
s=s.replace('code/output/integrate_post19_post21*.json','code/output/integrate_post19_post22*.json')
s=s.replace('The four-audited normal-subgroup crown refinement is preserved separately from this frozen PDF, with its proof and exact check records; its later assembly is not additional movement.',
 'The normal-subgroup refinement, arbitrary-SNC count and all-dimensional complete-local closure, all classical/exceptional Lie-family recognition, and the auxiliary wild swap example with exact repair are assembled in this PDF. Research files written later retain their separate exact status.')
old='The latest completed hourly comparison is code/output/formal_review14.json and its timestamped scope addendum: one strict crown-gate reduction, consecutive no-movement counter0. It includes the ordinary hereditary projective count and bounded-field projective automorphism crowns; these results cannot be counted again. The next formal review is due17:10UTC. Any subsequent main reduction is tracked separately with its exact proof and audit timestamps.'
new='The latest completed hourly comparison is code/output/formal_review15.json: two strict reductions, consecutive no-movement counter0. The first covers unrestricted-period projective counts for the stated complete local punctures in all dimensions; the second covers one-curve projective crowns with unbounded tame field-image order, including named defining-characteristic Lie-family recognition. Each is counted once. The next formal review is due18:10UTC. Any subsequent main reduction is tracked separately with its exact proof and audit timestamps.'
assert old in s;s=s.replace(old,new)
(root/'code/verify_checkpoint23.py').write_text(s)
s=(root/'code/scheduled_checkpoint22.py').read_text().replace('16:40UTC','17:25UTC').replace('2026,11,20,16,40','2026,11,20,17,25').replace('checkpoint22','checkpoint23').replace("'22'","'23'")
(root/'code/scheduled_checkpoint23.py').write_text(s)
print('Prepared checkpoint23 render, verification and scheduled creation; no archive created.')
