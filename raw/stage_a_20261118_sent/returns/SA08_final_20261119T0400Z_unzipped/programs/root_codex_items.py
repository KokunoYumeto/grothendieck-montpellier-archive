"""Manually selected Codex leads, without NOTES_INDEX verdict rows.

The Codex note tables and all three transcriptions were read in full. These
additional items make the distinct continuation questions addressable, including
research directions whose source has no Pro-index entry. No synthetic entry ID
is assigned: sources=[] explicitly records that distinction.
"""
from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[1];D=R/'work/root'
cs={c['id']:c for c in json.loads((D/'claims.json').read_text())}
qp=D/'quote_overrides.json';q=json.loads(qp.read_text()) if qp.exists() else {}
# id, exact claim group, kind, substantive reading assessment
groups=[
 (901,[901],'self-flagged step','The cancelled half-class equation and the surviving alternatives are both present; the note correctly leaves the normalization undecided.'),
 (902,[907],'self-flagged step','The numerical calculation and a questioned object-level decomposition are distinct. The uncertain exponent must not be resolved from ranks alone.'),
 (903,[909,910,911,912,913],'self-flagged step','The cochain-test diagrams, nonlinearity note, bidual issue and limit comparison are genuinely questioned; the unrestricted reconstructions need the stated hypotheses.'),
 (904,[914,915],'self-flagged step','The torsor comparison carries an explicit homotopy-equivalence question. The circle computation is an example, not a proof of the general comparison.'),
 (905,[918,919,920],'self-flagged step','The half-differential-algebra definition is followed by an explicit question about extending its product. The Hom ambiguity alone supplies no existence proof.'),
 (906,[924,926,927],'self-flagged step','The equivariant multiplication diagram is questioned. The later insertion that X varies changes the natural-Hom claim but does not supply Dold’s separate-variable hypothesis.'),
 (907,[925,928],'reading question','The operation sign exponent is genuinely blank; other sign alarms depend on an explicitly stated chain convention. No exponent is filled in.'),
 (908,[935],'self-flagged step','The question mark follows the complete Adem identity. The additional term is false under the usual right-to-left composition convention.'),
 (909,[947,948],'unproved claim','The connectivity estimate is written, but the smash/tensor notation is not sufficiently typed. The ordinary-space interpretation has a counterexample below the stated bound.'),
 (910,[952,953,954,955,956,957],'self-flagged step','The additive-group Ext calculation contains two lemmas and a proof explicitly restricted to P0. The unfinished product/spectral-sequence step is not supplied by the later group calculation alone.'),
 (911,[949,950,951],'unproved claim','The change-of-coefficients and power-operation formulas require finiteness and semilinearity qualifications. The Witt extension lives in abelian sheaves, not in Fp-module sheaves.'),
 (912,[939,943,944,945,946],'self-flagged step','The notes correctly record unspecified Cartan hypotheses and a small-range qualification; neither may be dropped when restating the symmetry and low-degree formulas.'),
 (913,[940,941,942],'other','The K2 and coniveau review is present on scan370. Stable rank and regularity hypotheses are essential in a modern precise restatement.'),
]
items=[];mapping={};events=[]
for n,nums,kind,why in groups:
 ident=f'SA08-{n}';claim_ids=[f'SA08-C{i}' for i in nums];rows=[cs[i] for i in claim_ids]
 first=rows[0];quote=q.get(first['id'],{}).get('his_statement',first['his_statement'])
 lines=[]
 for c in rows:
  for x in c['lines']:
   if x not in lines:lines.append(x)
 scans=sorted({s for c in rows for s in c['scans']})
 statement='\n\n'.join('['+c['id']+'] '+c['statement'] for c in rows)
 items.append(dict(id=ident,sources=[],kind=kind,cote=136,scans=scans,lines=lines,his_words=quote,statement=statement,
  reconstruction='Direct Codex-continuation lead, checked against the full supplied transcription and the Codex notes table. It has no NOTES_INDEX entry and creates no verdict row. The modern formulations and counterexamples are this run’s explicitly scoped checks; the manuscript reading is unchanged.',check='agrees',check_reason=why))
 for c in claim_ids:mapping.setdefault(c,[]).append(ident)
 events.append([ident,'2026-11-19','GPT-6 Astra Pro; effort not exposed by runtime; SA08/root','used and rechecked in this run','Codex lead and full transcription passage compared; '+why+' Individual mathematical check scopes are in the linked claims.'])

metadata=[
 (914,'K136-01',[328,336,342],'Gribouillis','The supplied first Codex segment has fifteen scan markers328–342. Scan336 is a title-only sheet; the pencil archive numbers run329–343. No written composition date or total is supplied.'),
 (915,'K136-02',[348,349,350,351,353,357,358,359,360,361],'Theorem D: (Generalized de Rham)','The second segment has fifteen supplied scan markers between343 and361, omitting344,347,354,356. English typescripts, half-differential-algebra examples and successive EZ headings are interleaved; no written total or composition date is supplied.'),
 (916,'K136-03',[362,363,364,365,366,367,368,369,370,371,372,373,374,375,376],'Calcul des Ext^i(G_a,G_a)','The third segment has fifteen scan markers362–376. Internal numbering1–5 andI–II belongs to two sequences. The printed1954 and1966 references are bibliographical dates, not composition dates; pencil foliation differs from scan numbering.'),
]
for n,folder,scans,quote,statement in metadata:
 ident=f'SA08-{n}'
 items.append(dict(id=ident,sources=[],kind='title, date or page count',cote=136,scans=scans,lines=[{'file':'codex/'+folder+'_transcription.tex','lines':'whole segment; title, heading and foliation comments'}],his_words=quote,statement=statement,reconstruction='Direct Codex metadata lead from codex/'+folder+'_notes.md, checked against the transcription. No NOTES_INDEX verdict row is created; scan count is an inventory count, not a manuscript assertion.',check='agrees',check_reason='The headings, nonconsecutive scan markers and foliation comments were read; no catalogue chronology is inferred from a bibliographical date.'))
 events.append([ident,'2026-11-19','GPT-6 Astra Pro; effort not exposed by runtime; SA08/root','used and rechecked in this run','Codex notes metadata and supplied transcription headings/scan markers compared; no independent scan inspection claimed.'])
(D/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
(D/'claim_item_links.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
with (D/'item_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print(json.dumps({'codex_items':len(items),'indexed_verdict_rows_created':0,'linked_claims':len(mapping),'exact_quotation_audit_loaded':qp.exists()}))
