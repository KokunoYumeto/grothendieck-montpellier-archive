"""Record the bounded, actual source scope of the jury/CNRS route."""
from pathlib import Path
import datetime,json
R=Path('RESEARCH_SA23')
record={'utc_recorded':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'note':'notes/algebra_jury_CNRS_source_search.md',
 'opened':['IMO historical Paris thesis list, complete downloaded text','Sorbonne public archival guide','Persée Schwartz authority metadata','Exact Calames HC12/8 search response','Primary Calames HC12/8 catalogue description, complete','Primary Calames 6 UPFS catalogue description, complete'],
 'not_opened':['Original 1953 thesis','Original Grothendieck jury or CNRS report','Original HC12/8 report folios','Original 6 UPFS papers','Complete scholarly Paris-juries study'],
 'result':'No dated identification of the trace/genus-zero proof or cote1 leaves; narrower public series-level boundary recorded; HC12/8 is Bourbaki Lie/varieties mathematics, not an assessment dossier',
 'raw_web_records':[f'notes/algebra_history_web{i}.json' for i in range(115,127)]}
event='\t'.join(['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters','used and rechecked in this run','New bounded thesis-jury/CNRS route: complete IMO list and Sorbonne guide plus exact primary HC12/8 and 6 UPFS catalogue descriptions read; no original assessment or 1953 thesis opened. AJ16 series-level scope and manual-consultation boundary recorded. HC12/8 Rapports resolved as Bourbaki Lie/varieties mathematics. No manuscript-date witness.','notes/algebra_jury_CNRS_source_search.md;logs/algebra_jury_fetch54.json;logs/algebra_jury_fetch55.json;logs/algebra_jury_record56.json'])
path=R/'notes/algebra_history_CHECK_EVENTS.tsv'
if event not in path.read_text():
 with path.open('a') as f:f.write(event+'\n')
record['event_added']=event
s=json.dumps(record,ensure_ascii=False,indent=2)
(R/'logs/algebra_jury_record56.json').write_text(s+'\n');print(s)
