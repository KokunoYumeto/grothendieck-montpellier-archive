"""Literal author quotations for root C901–920, selected by direct close reading.

The agent read K136-01 through line744 and K136-02 through line481 before
selecting these ranges. This extraction only preserves the selected text and
checks its provenance; it does not infer any mathematical verdict.
"""
from pathlib import Path
import json,csv,datetime,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'work/middle'
A='codex/K136-01_transcription.tex';B='codex/K136-02_transcription.tex'
selections={
901:[(A,21,21),(A,44,45)],
902:[(A,73,77)],
903:[(A,81,81),(A,85,85),(A,90,91)],
904:[(A,126,126),(A,136,136)],
905:[(A,270,270),(A,338,338),(A,369,369)],
906:[(A,317,317),(A,349,351)],
907:[(A,401,404),(A,429,430)],
908:[(A,479,486),(A,676,678)],
909:[(A,521,522),(A,554,554)],
910:[(A,533,533)],
911:[(A,567,571),(A,586,587)],
912:[(B,28,30)],
913:[(B,40,44)],
914:[(B,72,73),(B,93,98)],
915:[(B,114,116),(B,133,133)],
916:[(B,156,156),(B,225,228)],
917:[(B,251,252),(B,302,302)],
918:[(B,318,318),(B,341,343),(B,348,349),(B,364,364)],
919:[(B,418,418),(B,425,432)],
920:[(B,464,464),(B,471,473)],
}
texts={f:(ROOT/'sources/texts'/f).read_text().splitlines() for f in(A,B)}
quotes={};rows=[]
for n,parts in selections.items():
    snippets=[];locators=[]
    for f,a,z in parts:
        ls=texts[f];chunk='\n'.join(ls[a-1:z]).strip();assert chunk
        scan=next(int(re.search(r'\\scanpage\{(\d+)\}',x).group(1)) for x in reversed(ls[:a]) if '\\scanpage{'in x)
        assert not any('\\scanpage{'in x for x in ls[a:z])
        snippets.append(chunk);locators.append({'file':f,'lines':str(a)if a==z else f'{a}–{z}'})
        rows.append({'claim_id':f'SA08-C{n}','file':f,'scan':scan,'lines':str(a)if a==z else f'{a}–{z}','literal_excerpt':chunk,'audit':'Exact source fragment; cancellations and unsure alternatives preserved. Direct reading/source collation, not a mathematical proof.'})
    quotes[f'SA08-C{n}']={'his_statement':' … '.join(snippets),'quotation_lines':locators}
(OUT/'root_quote_candidates.json').write_text(json.dumps(quotes,ensure_ascii=False,indent=2)+'\n')
with(OUT/'root_quote_candidates_audit.tsv').open('w')as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
events=[{'statement_id':k,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed by runtime; SA08/middle','type':'carried as background without fault found','outcome':'Literal quotation selected after direct reading of the complete relevant Codex leaf and adjoining continuation; exact ranges are in root_quote_candidates.json. This event checks attribution and text, not the mathematical claim.'}for k in quotes]
with(OUT/'root_quote_candidates_events.tsv').open('w')as f:
    w=csv.DictWriter(f,fieldnames=list(events[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
print('Selected and exact-range validated',len(quotes),'claims in',len(rows),'literal fragments.')
print('Range: SA08-C901..920. Sources: K136-01:1–744 and K136-02:1–481 directly read.')
print('Quotation file:',OUT/'root_quote_candidates.json')
