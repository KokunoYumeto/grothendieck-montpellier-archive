"""Record the actually read new B49 scope remark after its path/layout repair."""
from pathlib import Path
import csv,datetime,json,re
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/checkpoint17_scope_check.json';assert not dest.exists()
text=(w/'agents/reduction_descent/B_tame_minimal_height_two.tex').read_text()
block=re.search(r'\\begin\{remark\}\[Scope and exact arithmetic check\](.*?)\\end\{remark\}',text,re.S)[1]
assert '\\label{rem:B-RD49-scope}' in block
assert (w/'code/reduction_descent/verify_tame_height_two_gate.py').exists()
assert all(x in block for x in ['136220','6984','1320','1.3878417579981033','0.6928875380035606','0.7361230790047557'])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['rem:B-RD49-scope',now,
       'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
       'targeted proof check',
       'PASS: entire scope remark actually read, including nontrivial finite norms, absence of elliptic replacement, open least-index interval, actual original-source fetch limits, exact coefficient/cancellation/degree/determinant counts and all three real runtimes. The referenced program path is corrected to its literal code/reduction_descent export. No finite check is presented as an existence theorem. This new remark now has a stable explicit label; its provisional auto label was never delivered in a checkpoint.'])
out={'status':'PASS','actual_utc':now,'statement_id':'rem:B-RD49-scope',
     'provisional_undelivered_id':'auto:B:473c6604547d',
     'reason':'Stable explicit identifier and correct literal program path; no mathematical change.'}
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
