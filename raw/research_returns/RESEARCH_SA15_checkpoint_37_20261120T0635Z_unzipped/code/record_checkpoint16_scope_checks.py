"""Record actual checks of the three new automatically labelled scope remarks."""
from pathlib import Path
import csv,datetime,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/checkpoint16_scope_checks.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
events=[
 ('auto:A_monodromy:feea204b71c7','PASS: full scope remark read. Its geometric degree/bundle/one-loss assertions are the previously fully audited sheaf lemmas; the all-even proof now discharges irreducibility independently. The retained pencil factorizations remain exploratory, with no uniform geometric implication attributed to them and no new root rerun claimed.'),
 ('auto:B:a2534788021e','PASS: full scope remark read after root independently rederived B45 and reran the entire exact certificate. Counts192000 and24576, actual author runtime, and the retained a3 crossing correction agree with the checked code/output. The infinite graph/Cartier proof is separate. No finite decision procedure for all16-congruences is claimed.'),
 ('auto:B:e906eee05992','PASS: full scope remark read after the entire B44 proof and certificate were independently checked. Its phrase leaving the all-supersingular16 comparison open refers to the preceding reduction alone; the later B48 theorem now resolves that remaining comparison. The exact24-automorphism, quaternion, formal-valuation and determinant checks have the stated limited scope and runtime. The actual B43 eight-torsion ambiguity persists.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,outcome in events:
        writer.writerow([sid,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort','targeted proof check',outcome])
out={'status':'PASS','actual_utc':now,'statements':[x[0] for x in events],
     'scope':'All three full passages actually read; no new computational audit of unused pencil experiments.'}
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
