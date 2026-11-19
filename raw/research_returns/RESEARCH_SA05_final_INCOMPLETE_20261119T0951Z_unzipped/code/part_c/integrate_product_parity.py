"""Integrate the audited product lemma and the failed parity converse."""
from pathlib import Path
import csv
import json
root=Path(__file__).resolve().parents[2]
section=root/'sections/part_c.tex'
text=section.read_text()
marker='\\begin{theorem}[The narrow K3 ring already detects finite-dimensionality]'
if '\\label{c:product-parity}' not in text:
    assert marker in text
    text=text.replace(marker,(root/'part_c/c1_product_parity.tex').read_text()+'\n'+marker)
section.write_text(text)
with (root/'part_c/results.csv').open('a',newline='') as f:
    csv.writer(f).writerow(['c:product-parity',
      'Narrow all-powers cycle injectivity is stable under products; it does not force tautological parity',
      'Proved product theorem; refuted proposed converse',
      'sections/part_c.tex, Proposition label c:product-parity',
      'Factor cases; rational Betti Kunneth; graph normalization; exact rank certificate',
      '11:51-57; C.1(c)',
      'E times P1 is a positive pair with parity outside span(Delta,o1,o2), although graph([-1]E times id) realizes parity algebraically. This is a failed-method clarification, not a resolution of the general classification.'])
events=[
 ['c:product-parity','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Product external generators and rational Kunneth prove injectivity; normalized endomorphisms of E times P1 act by a common scalar on H1,H2,H3, which cannot equal parity.'],
 ['c:product-parity','2026-11-19','GPT-6 Astra (OpenAI), /root/part_d','independent re-proof','Product stability and explicit odd-derivation parity obstruction independently verified; full audit saved in part_d/c1_product_parity_audit.md.'],
 ['c:product-parity','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','computation or formal certificate','check_parity_span.py gives rank3 for the tautological correspondence span and rank4 after adjoining parity, with exact Fraction arithmetic; output archived.']]
with (root/'part_c/CHECK_EVENTS.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t').writerows(events)
output={'label':'c:product-parity','main_lines':len(text.splitlines()),'events_added':len(events)}
(root/'code/part_c/integrate_product_parity_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output))
