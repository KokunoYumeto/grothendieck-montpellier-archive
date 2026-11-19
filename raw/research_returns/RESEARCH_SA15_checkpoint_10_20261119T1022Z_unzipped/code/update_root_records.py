import csv,json,pathlib,re
root=pathlib.Path(__file__).resolve().parents[1]
rows=json.loads((root/'notes/root_results.json').read_text())
columns=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
with (root/'RESEARCH_SA15_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader()
    for row in rows: writer.writerow({k:row[k] for k in columns})
events=root/'CHECK_EVENTS.tsv'
old=events.read_text() if events.exists() else 'statement_id\tdate\twho\ttype\toutcome\n'
who='GPT-6 Astra (OpenAI); /root; effort not exposed; RESEARCH_SA15 2026-11-19'
for row in rows:
    key=row['id']+'\t2026-11-19\t'+who
    if key not in old:
        kind='used and rechecked in this run' if row['id'] in ['A-R1','A-R2'] else 'targeted proof check'
        if row['id']=='A6-COMPUTATION': kind='computation or formal certificate'
        if row['id']=='A6-COUNTEREXAMPLE': kind='refuted, with refined statement A6-SMALL-RANGE'
        old+=key+'\t'+kind+'\t'+row['status']+': '+row['statement']+'. '+row['notes']+'\n'
events.write_text(old)
print(f'Wrote {len(rows)} root result rows; retained all existing check events.')
