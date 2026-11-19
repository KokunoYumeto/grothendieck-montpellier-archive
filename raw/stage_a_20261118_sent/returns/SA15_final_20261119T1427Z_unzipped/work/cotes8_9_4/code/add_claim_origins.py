"""Explicit attribution census, checked against the source passages.

Modern restatement or a new proof does not make a manuscript assertion ours.
"""
import csv
import json
from collections import Counter
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
claims=json.loads((BASE/'claims.json').read_text())
refinements={
 'P894-C077':('The manuscript says T_ℓ for any ℓ. The separation of raw p-adic Tate inertia from finite potentially-good inertia is this run’s explicit correction of that literal reading. The underlying trace question remains Grothendieck’s.', 'cote 9:13–14, lines 478–485'),
 'P894-C078':('The margin asserts Zp-valuedness subject to μp⊂K. Removing that hypothesis by the commuting-Frobenius trace argument is this run’s strengthening. The weaker conditional assertion is explicitly attributed to the manuscript.', 'cote 9:13, lines 474–478'),
 'P894-C082':('The P1 permutation-module calculation and the p=3,d=3 group-order test were supplied in this run as a boundary refinement. They are not an additional assertion by Grothendieck and do not refute the n≥2 question.', 'cote 4:12, lines 1292–1298'),
}
rows=[]
for c in claims:
    if c['id'] in refinements:
        attribution,source=refinements[c['id']]
        c['origin']='present-run refinement; not an additional assertion by Grothendieck'
        c['attribution']=attribution
    else:
        source='; '.join(c['lines'])
        c['origin']='manuscript'
        c['attribution']='The assertion, construction, question or withdrawn statement is on the cited manuscript pages. Its modern restatement, literature assessment and any additional checking proof are this run’s work.'
    if c['id']=='P894-C023':
        c['attribution']='The question of recovering the finite inertia character from mod-p torsion and the negative marginal report belong to the manuscript. The explicit pair of elliptic curves over F(5^(1/8)) is an independent counterexample constructed in this run; it is not identified with Tate’s historical example.'
        c['counterexample_origin']='this run; independently constructed and checked'
    elif c['id']=='P894-C079':
        c['attribution']='Additional manuscript assertion: the potentially constant and potentially multiplicative cases, with the stated μp qualification, occur on cote 9:13. This run supplies the precise modern distinction from the supersingular counterexample.'
    elif c['id']=='P894-C080':
        c['attribution']='Additional manuscript assertions: the coefficient identities and their Frobenius twists are written on cote 9:5. The monomial proof and nontrivial Witt-coefficient computation are checks made in this run.'
    elif c['id']=='P894-C081':
        c['attribution']='Additional manuscript construction: the enveloping extension and its vector term occur in the cote 9:3 discussion. The universal-vector-extension interpretation and precise sheaf-level hypotheses are stated as this run’s reconstruction, supported by the opened literature.'
    elif c['id']=='P894-C071':
        c['attribution']='The equivalence being checked is the manuscript’s live assertion on cote 4:11. The extra preceding-degree stable torsion term and algebraic countermodel are this run’s independent correction; they do not turn the original assertion into a new claim by this run.'
    elif c['id']=='P894-C075':
        c['attribution']='The trace-surjectivity implication is explicitly on cote 4:12, lines 1296–1298. The determinant-one block-matrix proof is supplied in this run; its stronger SL formulation is a checking lemma, not evidence of historical priority.'
    rows.append({'claim_id':c['id'],'origin':c['origin'],'attribution':c['attribution'],'source':source})
(BASE/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
with (BASE/'claim_origins.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['claim_id','origin','attribution','source'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
report={'claims':len(claims),'origins':dict(Counter(c['origin'] for c in claims)),
        'present_run_refinement_ids':list(refinements),
        'manuscript_question_with_new_counterexample':'P894-C023',
        'additional_manuscript_assertions':['P894-C079','P894-C080','P894-C081']}
(BASE/'outputs/claim_origins.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
