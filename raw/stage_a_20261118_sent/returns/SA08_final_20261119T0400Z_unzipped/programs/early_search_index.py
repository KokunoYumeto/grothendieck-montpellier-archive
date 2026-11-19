"""Index saved raw searches and claim/search links; makes no claim adjudications."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];O=R/'work/early'
out=['# Early-package literature search log','',
 'Audit date: 19 November 2026. Every substantive web call is saved in logs/early_search_*.json, including failed routes and irrelevant results. The exact queries and opens below are mechanically indexed from those records; the mathematical outcomes were written after reading the sources.', '',
 '## Outcomes and limits','',
 '- Cartan/Miller: title and bibliography searches led to Cartan’s full original §§1–7, Garvín et al.1998, and the exact Cenkl–Porter1982/1984 sources. Cartan is the exact weighted match. Miller metadata and its prepublication existence are verified, but the early analysis does not claim an independently checked full Miller proof.',
 '- Shadows: French ombres and English divided-power/tail/fully-faithful/localization/Ext searches, including zbMATH, arXiv and MathOverflow targeting, located Nagpal–Snowden. Its complete-noetherian/finitely-presented scope and D/(x) counterexample target differ from the induced-target manuscript claim. Absence of an exact all-module source is not evidence of novelty.',
 '- Integral models: author/arXiv/journal sources for Mandell, Ekedahl and Horel were opened. Their nilpotent finite-type hypotheses, E∞/numerical/binomial targets, and faithfulness/fullness conclusions are retained separately. No equivalence with the manuscript PD category was found.',
 '- Arithmetic and negative maps: original Lucas pp51–52 supplies the digit congruence; the infinite-height MathOverflow presentation was checked directly. Exact saved proofs, rather than search results, settle the stated binomial-family and negative-map refinements.',
 '- Coefficients/topoi: searches on local-coefficient de Rham models, category cohomology, flasque PD algebras and Grothendieck’s later accounts led to official Stacks pages, Cartan’s hypotheses, and actual Pursuing Stacks passages. No source licenses the literal arbitrary-presheaf tensor resolution; it is refuted here.',
 '- Donors: Sullivan’s author bibliography and exact original PDF identify the English minimal-model leaves. SGA7 original scans identify the reused French typescripts. Exact original pages, not later AI translations surfaced by search, control the donor collation.',
 '- Earlier analytic history: primary de Rham metadata, Cartan’s Stein exposé, Grothendieck1966 and DGMS1975 were opened. References not independently proved are explicitly carried as background. EGA IV theorem references were followed through the original SGA argument, not represented as full independent EGA proof checks.',
 '- Access limitations: several Garvín, journal, zbMATH and EGA PDF routes failed. Successful alternate downloads and their paths are preserved. A failure to retrieve a source is never a negative mathematical result.', '',
 '## Exact saved calls','']
index=[]
for p in sorted((R/'logs').glob('early_search_*.json')):
 if p.name=='early_search_index_output.json':continue
 try:d=json.loads(p.read_text())
 except Exception as e:
  index.append({'file':p.name,'parse_error':repr(e)});continue
 q=d.get('queries',d.get('query',d.get('request',{})))
 index.append({'file':p.name,'queries':q,'purpose':d.get('purpose','')})
 out+=['### '+p.name,'']
 if d.get('purpose'):out += [d['purpose'],'']
 if q:out+=['```json',json.dumps(q,ensure_ascii=False,indent=2),'```','']
 else:out+=['The raw result preserves the opened source, command and source reference; see the named JSON record.','']
out += ['## Claim-to-search audit','', '| Claim | Saved raw search logs |','|---|---|']
for c in json.loads((O/'claims.json').read_text()):out.append('| '+c['id']+' | '+'; '.join(sorted(set(c['search_logs'])))+' |')
(O/'search_log.md').write_text('\n'.join(out)+'\n')
(O/'search_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'raw_search_calls':len(index),'claims_indexed':len(json.loads((O/'claims.json').read_text()))},indent=2))
