"""Record the observed completed-agent state after the actual stopping review."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
path=root/'code/output/formal_review21.json'
review=json.loads(path.read_text())
assert review['stopping_condition_met'] and review['consecutive_no_movement_reviews']==2
assert not review['movement']
record=dict(utc=datetime.now(timezone.utc).isoformat(),formal_review_number=21,
            formal_review_actual_utc=review['actual_utc'],
            formal_review_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            all_research_agents_stopped=True,
            observed_agent_states={name:'completed' for name in ['/root/part_b','/root/part_c','/root/part_d']},
            observation='After review21, root issued an interrupt for each research agent and then called collaboration.list_agents. All three were observed completed, with no active research turn.',
            root_research_state='Stopped at the formal stopping review. Only final scope, packaging, archive verification and delivery continue.',
            reason='Formal reviews20 and21 both recorded no requested-row status change and no strictly smaller strongest main gate.',
            next_research_review=None,next_scheduled_checkpoint=None)
out=root/'code/output/research_stopped.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'record':str(out.relative_to(root)),'review':21,'all_research_agents_stopped':True,'utc':record['utc']}))
