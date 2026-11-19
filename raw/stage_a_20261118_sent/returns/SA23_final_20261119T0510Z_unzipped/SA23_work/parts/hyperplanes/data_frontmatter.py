"""Editorial front matter and repeated early occurrences, read as source evidence."""
from register_common import I,C,E,L,WHO,DATE
loc='texts/api/ega_v_cote25_combined.tex:43–129'
I.append(dict(id='SA23-607',sources=[],kind='title, date or page count',cote='25',scans=[1,2,3],lines=[loc],his_words='Cette rédaction donne pêle mêle une esquisse détaillée ... réorganisation de fond en comble ... aurai tu une suggestion à faire où le fourrer ?',statement='The opening labels this an état0 of sections hyperplanes et projections coniques, lists sixteen sections, asks for a new plan and placement of additional birational material, and says the linear-system translation is still to be sent. Scan1 is blank apart from its number.',reconstruction='Editorial history only; this does not assert a new mathematical theorem or identify the finished chapter with published EGA IV20.',check='agrees',check_reason='Scans1–6 and their full transcription text were read directly; the placement question and title are retained separately from mathematical claims.'))
E.append(['SA23-607',DATE,WHO,'used and rechecked in this run','Opening plan, état0 designation, blank first leaf and request to place birational material checked against exact source text.'])
I[-1]['scans'] += [134,135]
I[-1]['lines'].append('texts/api/ega_v_cote25_combined.tex:5355–5413')
I[-1]['his_words'] += ' Later letter,29September1965: quels seront les titres des deux morceaux; reconsidérer la question ... joint papar.'
I[-1]['statement'] += ' The dated letter of29September1965 asks for the titles of revised sections20–21, gives a proposed list22–27, and asks Dieudonné to reconsider joint authorship of the former appendix rather than publication under Grothendieck alone.'
E.append(['SA23-607',DATE,WHO,'used and rechecked in this run','The later editorial letter on scans134–135 was reread in the final author-question audit and merged with the chapter-plan subject, retaining its date and joint-authorship request.'])
for n,scans,lo,hi in [(60,[5],194,207),(60,[112],4495,4501)]:
 cid=f'C-SA23-hyp-{n:03}';iid=f'SA23-{500+n}';line=f'texts/api/ega_v_cote25_combined.tex:{lo}–{hi}'
 for obj in I+C:
  if obj['id']in [cid,iid]:
   obj['scans']=sorted(set(obj['scans']+scans));obj['lines'].append(line)
E.append(['C-SA23-hyp-060',DATE,WHO,'targeted proof check','The earlier occurrence on scan5 announces the same relative-divisor parameter construction. Its symmetric-dual convention is assessed with the later explicit construction, without changing the transcription.'])

# The selections below are manually authored and independently source-located.
# This only quotes them; it does not discover claims or make verdicts.
import json
from pathlib import Path
quote_plan=json.loads((Path(__file__).resolve().parents[2]/'integration/hyperplanes_selected_quotes.json').read_text())
for selection in quote_plan['selections']:
 n=selection['claim'];cid=f'C-SA23-hyp-{n:03}';iid=f'SA23-{500+n}'
 passages=[];locations=[]
 for lo,hi in selection['ranges']:
  passages.append('\n'.join(line for line in L[lo-1:hi]if line.strip()and not line.lstrip().startswith(('%','\\clearpage','\\scanpage','\\mspage'))))
  locations.append(f'texts/api/ega_v_cote25_combined.tex:{lo}–{hi}')
 for obj in I+C:
  if obj['id']in [iid,cid,cid+'R']:
   obj['scans']=sorted(set(obj['scans']+selection['scans']));obj['lines']+= [s for s in locations if s not in obj['lines']]
  if obj['id']==cid:
   obj['his_statement']='\n[…]\n'.join(passages);obj['source_quote_ranges']=locations
   if selection.get('scope_note'):obj['source_quote_scope_note']=selection['scope_note']
  if obj['id']==iid:
   obj['his_words']='\n'.join(passages[0].splitlines()[:4]);obj['check_reason']+=' Quote audit: '+selection['reason']
 E.append([cid,DATE,WHO,'used and rechecked in this run','Selected literal source quotation and exact physical-line locators rechecked. '+selection['reason']])
