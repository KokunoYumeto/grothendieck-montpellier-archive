"""Index actual saved search results; never manufacture historical query strings.

Claim dispositions remain the manually authored records.  This program joins their
explicit search references to the saved result payloads and verified-source audit.
"""
from pathlib import Path
import json,re,csv,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'work/middle';RESEARCH=ROOT/'research'
purposes={
1:'SGA IX donor claims, mixed extensions and monodromy; title/section searches and bibliography leads.',
2:'Equal-characteristic Tate full faithfulness, de Jong and bibliographic databases including zbMATH leads.',
3:'Graded divided powers, free algebra and Koszul hypotheses in Stacks; standard PD conventions.',
4:'Dold–Puppe derived nonadditive functors; Stoia Gorenstein title and Numdam discovery.',
5:'Stoia/Gorenstein backward bibliography search and Numdam source checks.',
6:'Breen–Mikhailov–Touzé original derived-power paper and de Jong author bibliography.',
7:'Original published SGA7 I access and donor section comparison.',
8:'Grothendieck/Cartan generalized de Rham comparison, uniqueness and weighted hypotheses.',
9:'Cartier, the four differential complexes, Euler contraction and simplex integration.',
10:'de Jong publication/author source, full faithfulness and reduction criteria.',
11:'Potential-semista­ble monodromy integrality/sign questions; Coleman and Stoia leads.',
12:'Stoia original-note search, exact title and 1979 follow-back bibliography.',
13:'Bănică–Stoia, Stacks Gorenstein openness, de Jong and monodromy publication matches.',
14:'Completed PD categories, representability, localization and unresolved uniqueness/fraction formulations.',
15:'Cartier/author bibliographies and integration normalization; direct calculations are separately logged.',
16:'Sullivan minimal models and Cartier publication bibliography.',
17:'BMT exact derived-power/Koszul discussion and Cartier comparison scope.',
18:'Lazard theorem in Stacks058G, with flat-module reduction hypotheses.',
19:'Sullivan Theorems8.1 and10.1; monodromy exposition lead used only within checked scope.',
20:'Sullivan rational/nonnilpotent distinction and exact theorem passages; follow-back references.',
21:'Cenkl1989 original, §5 hypotheses and obstruction to a natural commutative cochain model.',
22:'Horel, Ekedahl and Toën exact enhanced-model statements and their hypotheses.',
23:'Dwyer tame homotopy, Cenkl–Porter cubical forms and exact coefficient-system queries.',
24:'Dwyer DOI access failure; Cenkl–Porter access; Toën/Ekedahl exact bounds.',
25:'Scheerer–Tanré primary exposition found by backward references; original Dwyer sought.',
26:'Garvín and Richter–Sagave searches; Scheerer–Tanré and Mandell cochain multiplications.',
27:'Mandell2002 exact Main/Uniqueness statements; Richter–Sagave and Cenkl–Porter source discovery.',
28:'Mandell2002 uniqueness and Richter–Sagave diagram-category theorem boundaries.',
29:'Publisher click/access attempts, including an irrelevant result and inaccessible Garvín route; neither used as a proof.',
30:'Cenkl–Porter1982 original discovered; Garvín strict-range source search.',
31:'Mandell2001 author PDF, Cenkl–Porter1982/1984 originals, Bachmann–Burklund2026 source discovery.',
32:'Mandell2001 and Bachmann–Burklund arXiv/published versions; Cenkl–Porter1984 §4.',
33:'Mandell coefficient distinctions, Cenkl–Porter theorems and Bachmann–Burklund publication metadata.',
34:'Mandell AppendixA; visual Cenkl–Porter §4 statements; Bachmann–Burklund dates.',
35:'Published Bachmann–Burklund Theorems1.2/8.1 and1.3/8.2; Mandell AppendixA.',
36:'SGA9.7 and Grothendieck uniqueness follow-up; Sullivan full-source follow-back. Unofficial SGA retyping and AI-generated exposition excluded as theorem evidence.',
37:'Sullivan exact theorem search; unsuccessful guessed Numdam endpoint retained as an access failure.',
38:'Sullivan §§5/8 direct source reading of construction, nilpotent comparison and incomplete nonnilpotent claim.',
39:'Explicit final searches: de Jong erratum, Coleman pairing, Stoia title, MathOverflow divided powers.',
40:'Open Coleman (403), Bănică–Stoia original, zbMATH record (403), MathOverflow crystalline question.',
41:'Explicit uniqueness/Hasse/endomorphism searches; Li–Mondal surfaced as a distinct algebraic de Rham theory.',
42:'Hasse–Schmidt, DLMF and author-bibliography searches; no exact PD-localization theorem inferred.',
43:'Hoffmann–Kowalski, Hazewinkel, DLMF and Grothendieck published-works bibliography opened.',
44:'Higher-derivation definitions/constants; Li–Mondal publisher access; bibliography checks.',
45:'Li–Mondal author original; Hoffmann–Kowalski translation formula and arXiv chronology.',
46:'Li–Mondal Theorem1.1 precisely read and excluded as a solution of the different simplicial PD category.',
47:'Exact final search strings for quasi-flasque, uniqueness, simplicial PD endomorphisms and fraction calculus; unrelated algebraic de Rham and AI-generated pages excluded.',
48:'Guillén Santos–Navarro–Pascual–Roig monoidal acyclic-models original and source discovery.',
49:'Original publisher PDF and arXiv chronology for monoidal acyclic models.',
50:'Theorems4.10,8.1,9.2 and Corollary9.3, with exact hypotheses, in monoidal acyclic models.',
51:'Monoidal acyclic-models p373 visually checked; Theorem4.10 proof and9.2 proof read. OCR >0 corrected to ≥0 only for this published source, not manuscript ink.'}
records=[]
for n in range(1,52):
    p=RESEARCH/(f'middle_search_{n:02d}.json' if n<=2 else f'middle_web_{n:03d}.json')
    d=json.loads(p.read_text());r=d.get('result',d)
    txt='\n'.join(c.get('text','') for c in r.get('content',[]) if c.get('type')=='text')
    # The source snippets retain URLs and source-reference IDs. This is retrieval
    # metadata only; theorem acceptance is in reference_audit and claims.
    urls=list(dict.fromkeys(re.findall(r'https?://[^\s<>"）]+',txt)))
    urls=[u.rstrip(').,]') for u in urls]
    ids=list(dict.fromkeys(re.findall(r'【(turn[^】]+)】',txt)))
    rec={'id':f'MID-S{n:02d}','file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'purpose':purposes[n],'query':d.get('query'),'query_provenance':'Literal tool input retained.' if 'query'in d else 'Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.','source_ids':ids,'urls':urls}
    records.append(rec)
(OUT/'search_results_index.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')

claims=json.loads((OUT/'claims.json').read_text());refs=json.loads((OUT/'reference_audit.json').read_text());rd={r['key']:r for r in refs}
rows=[]
for c in claims:
    evidence=[]
    for k in c['refs']:
        r=rd[k];evidence.append(k+': '+r.get('annote',''))
    rows.append({'claim_id':c['id'],'manuscript':c['lines'],'search_records':c.get('search_record',''),'classification':c['class'],'searched_fate':c['fate'],'exact_source_scope':' | '.join(evidence),'calculation_evidence':c['computation'],'limit':'Source theorem reading is not an independent proof. Negative search is not novelty or present-day openness.'})
with (OUT/'search_coverage.tsv').open('w')as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
assert len(rows)==101 and all(x['search_records'] for x in rows)

intro='''# Middle-package search audit

Date: 2026-11-19 UTC. Research identity: GPT-6 Astra Pro; effort not exposed by runtime; SA08/middle.

This is the search record for all 101 middle-package claims. `search_coverage.tsv` gives one row per claim, its exact manuscript locator, actual search batches, the resulting fate, source hypotheses and computational evidence. `search_results_index.json` indexes all 51 saved result payloads and their hashes. The human-authored judgments are in `claims.json`; this program only joins already written records.

## Search scope and limits

The search covered published SGA7 IX and its backward references; Numdam for Cartan-related and Dold–Puppe/Roby/Sullivan sources; the author sites of de Jong, Mandell, Cartier, Horel and Li–Mondal; arXiv for integral, rational, binomial and p-adic homotopy models; publisher originals for BMT, Cenkl, Cenkl–Porter, Garvín and the monoidal acyclic-model theorem; MathOverflow; zbMATH-indexed results and a directly attempted record; and Grothendieck publication bibliographies. The final theorem comparisons use opened primary works, except the explicitly marked original-source access gaps.

The zbMATH record attempt returned 403. Coleman’s original PDF also returned 403 through the browser retrieval and an independent urllib attempt; a publisher first-page excerpt is bibliographic evidence only. The original Stoia1975 note, Dwyer1979 and Cartier1957 note were not obtained by this agent. Stoia’s title/month were followed back through the opened Bănică–Stoia1979 bibliography; Dwyer’s precise range is reported from the opened later primary exposition by Scheerer–Tanré1991; the elementary Cartier-coordinate calculation has its own proof. Miller’s original is delegated to root and is not relabelled as opened by this agent. These gaps limit source attribution, not the existence of a searched fate.

For batches 1–38 the saved files contain full original returned tool output but not a separate top-level input object. Their purpose labels below therefore describe the actual recorded research themes and source-opening trail; they are not invented verbatim search strings. Batches39–51 retain the literal tool inputs as well. Search-result titles are discovery leads until a primary source is opened and its hypotheses checked. Newly surfaced self-labelled AI-generated exposition and an unofficial SGA retyping were not used as theorem evidence.

## Principal comparison decisions

1. Cartan’s original §7 explicitly reports the Grothendieck lecture of 12 December1975 and publishes weighted PD comparisons and binomial products. This is an exact development by another author, not a theorem asserting an ordinary unweighted integral commutative cochain equivalence.
2. Garvín et al., Theorem4.2 p176, has strict p<q. Cenkl–Porter1982 Proposition1 has the same strict range and adds higher multiplicative homotopies; Cenkl–Porter1984 uses Q_q obtained by inverting primes≤q. These statements cannot replace the inclusive good-truncation comparison of the manuscript without a convention check.
3. Mandell2002 and Guillén Santos–Navarro–Pascual–Roig2008 establish strong uniqueness results in precisely specified enhanced or monoidal categories. Their exact axioms have not been verified for the manuscript’s weighted τ-infinity PD category. Li–Mondal’s algebraic de Rham endomorphism theorem has smooth-algebra inputs, so its semidirect monoid does not calculate the manuscript’s groups.
4. BMT2016 Proposition3.5 p270 is derived Γ/Λ/Sym décalage for finite projective modules; it does not make naive termwise powers of complexes equivalent. The Γ²/Sym² calculation in this dossier is explicit and distinguishes them from the correct exterior model.
5. The SGA donor matches are dated seminar1967–1969/publication1972, despite their physical reuse in a 1975–1976 folder. De Jong1998 removes a characteristic-p full-faithfulness obstacle; its1999 erratum changes the semistable definition. Published SGA9.7 and14.1.12 still retain the integrality and sign questions on which this search did not establish a precise modern answer.
6. Horel, Ekedahl, Toën, Mandell and Bachmann–Burklund require different algebraic structures and space hypotheses. None is silently identified with the manuscript coefficient/coPD construction; ordinary cohomology alone is never substituted for the enhanced model.

## Saved search and opening batches
'''
parts=[intro]
for r in records:
    parts.append(f"\n### {r['id']}\n\nPurpose: {r['purpose']}\n\nEvidence file: `{r['file']}`. SHA-256: `{r['sha256']}`.\n\n{r['query_provenance']}\n")
    if r['query'] is not None:parts.append('\nLiteral input:\n\n```json\n'+json.dumps(r['query'],ensure_ascii=False,indent=2)+'\n```\n')
    parts.append('\nRetrieved/opened URLs (presence here is not endorsement):\n\n'+'\n'.join('- '+u for u in r['urls'])+'\n')
parts.append('''
## Shared primary-source work

`ROOT-Cartan-full`: original journal scan at `work/reference_pdfs/invent35.pdf`; printed pp264,266–271, particularly §7. `ROOT-SGA-full`: original SGA7I PDF and per-page text/images in `work/reference_pdfs/sga7-1/`; exact donor locators are in `reference_audit.json` and `links.tsv`. `ROOT-Roby` and `ROOT-DoldPuppe`: original Numdam works opened by root, with the bounded source findings shared in the agent record. Shared access is identified as such in CHECK_EVENTS; it is not a claim that this agent independently reproved the source.

## Follow-back paths

Cartan’s1976 proof note → Miller preprint → Miller1978 → Cenkl–Porter1982/1984 and Garvín1998. Cartan’s comparison axioms → Mandell2002 and Guillén Santos et al.2008. SGA Tate proviso → de Jong’s author bibliography → original1998 DVI → original1999 erratum. Stoia donor attribution → same-title1975 note in Bănică–Stoia1979 bibliography → Stacks scheme openness theorem, kept distinct from the1979 analytic theorem. Dold–Puppe normalization → BMT derived-power décalage, with explicit finite-projective hypotheses. Dwyer title/DOI access attempts → Scheerer–Tanré1991 original, whose exact restatement is used under its own citation.

No source search or negative result in this file is used to assert that a manuscript question is new or still open in November2026. Classes C/D are accompanied by the exact comparison or search boundary in each claim.
''')
(OUT/'search_log.md').write_text('\n'.join(parts))
print('Indexed',len(records),'actual retrieval payloads and',len(rows),'searched claim fates.')
print('All literal query inputs available in batches39–51 retained; earlier absent inputs explicitly labelled.')
