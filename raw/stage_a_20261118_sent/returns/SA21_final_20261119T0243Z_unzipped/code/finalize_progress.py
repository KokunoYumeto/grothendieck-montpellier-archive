"""Record the actual completion milestone after the final coverage gate passes."""
from pathlib import Path
import json,datetime
R=Path(__file__).resolve().parents[1]
v=json.loads((R/'audit/final_validation.json').read_text())
assert v['validation']=='PASS','Do not record completion before final validation.'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
counts=v['counts']
milestones=[
 ('STAGE1_COMPLETE','122 source entries read with passages;97 consolidated items; all verdicts and corrections accounted for.'),
 ('STAGE2_COMPLETE',f"{counts['claims']} claim records, each with read source status, an executed literature-search assignment and a scoped check event. Computation certificates and proof qualifications saved."),
 ('STAGE3_COMPLETE',f"{counts['problems']} merged problem records with read-source state of art and separate source/current formulations."),
 ('STAGE4_COMPLETE',f"{counts['readings']} mathematical reading alarms; no scan or ink decision claimed."),
 ('STAGE5_COMPLETE','All supplied cross-references evaluated. Verified endpoints, unresolved missing/ambiguous targets and54 other-project leads kept in separate explicit tables.'),
 ('STAGE6_COMPLETE',f"{counts['directions']} ranked next tasks, each with existing item, claim and problem origins; no direction developed as a new project."),
 ('END','All final content assembled and coverage gate passed; final archive packaging and persistent delivery follow. No original inputs, full publications or earlier checkpoint archives are bundled.')]
with (R/'progress.log').open('a') as f:
 for tag,message in milestones:f.write(now+'\t'+tag+'\t'+message+'\n')
print(json.dumps({'utc':now,'recorded_milestones':[x[0] for x in milestones],'counts':counts},indent=2))
