"""Explicit scientific refinements after exact-source follow-up, 19 Nov 2026.

Run after root_items.py, root_claims.py, root_problems.py and root_sources.py.
Every change below is a manually reasoned decision; no classification is inferred
from a heading, keyword, or source-title match.
"""
from pathlib import Path
import json,csv
B=Path(__file__).resolve().parents[1]; O=B/'parts/root'
claims=json.loads((O/'claims.json').read_text()); cs={c['id']:c for c in claims}
items=json.loads((O/'items.json').read_text()); its={i['id']:i for i in items}
ps=json.loads((O/'problems.json').read_text()); pmap={p['id']:p for p in ps}
events=list(csv.DictReader((O/'claim_events.tsv').open(),delimiter='\t'))
WHO='GPT-6 Astra Pro / inherited effort (not numerically exposed) / SA18 root'
def change(cid,**kw):
    c=cs[cid];c.update(kw)
    if 'fate' in kw:c['present_status']='As of 2026-11-19: '+kw['fate']
    return c
def event(sid,kind,outcome,who=WHO):
    events.append(dict(statement_id=sid,date='2026-11-19',who=who,type=kind,outcome=outcome))

change('CL-SA18-11065',status_on_pages='stated without proof',fate='SGA3 XII Remark 1.6 explicitly states the smooth affine DVR family with generic fibre Gm and special fibre Ga. The source asserts that an example is easy to construct; it does not supply our formula. The reconstruction Spec Z_(3)[x,(1+3x)^−1], with law x+y+3xy, verifies the existence assertion and the variation of reductive rank.')
change('CL-SA18-11093',refs=['R-SGA3XII','R-SGA3XIV'],fate='The deferred result is proved in SGA3 XIV: Corollary 1.4 gives a maximal torus, containing any prescribed torus, for a smooth finite-type group over an artinian base. For a smooth finitely presented group with connected reductive geometric fibres, Corollary 3.20 gives Zariski-local maximal tori, and Remark 3.21(c) puts any given torus inside one Zariski-locally. The distinct prescribed-special-fibre lifting question in 3.21(b) is not needed for these assertions.',confidence='high')
change('CL-SA18-11020',fate='The reused typescript matches Mumford–Fogarty GIT, second edition, Chapter 3 Corollary 3.2 and the preceding Proposition 3.1. Restriction of the equivariant chart gives the corollary. The first GIT edition is dated 1965 by the author bibliography; the exact original typescript date and first-edition wording were not established. This is not a Grothendieck-authored theorem by physical proximity.')
change('CL-SA18-11021',fate='The omitted inverse checks hold on the specified determinant/unit-coordinate chart. The general tree-normalization argument in R3 supplies the inverse and the PGL product decomposition, with an exact n=2 certificate. The same construction is read in GIT Chapter 3 Proposition 3.1 and Corollary 3.2.')
change('CL-SA18-11023',fate='GIT Chapter 3 Definition 3.7, Proposition 3.4 and Theorem 3.8 identify the selected stable-configuration locus: its quotient is a locally trivial PGL torsor and the descended product bundle is ample. The earlier prestable quotient may be nonseparated and is a different locus. The reused pages belong to Mumford’s text.',confidence='high')
change('CL-SA18-11024',fate='Consecutive differences give the exact simplicial-cone isomorphism. For a nonzero sorted zero-sum vector at least one coefficient is positive. The general proof and exact rational tests validate the elementary calculation; the opened GIT Chapter 3 text supplies its published context.')
change('CL-SA18-11102',status_on_pages='stated without proof',**{'class':'C'},fate='The source states the abstract Lemma B and marks its analytic-polyhedron application to be clarified; it gives no proof on this leaf. Siu Theorem 1 establishes the exact analytic noetherianity criterion, and the semianalytic Stein-compact convention in Buchweitz–Flenner supplies a positive setting. These sources do not prove the full abstract ringed-space implication. The remaining step is to derive a neighborhood on which all later terms of an ascending coherent-submodule chain agree from hypothesis (v); stalkwise stabilization alone does not supply that uniform neighborhood.',confidence='medium')
pmap['MP-SA18-11036'].update(state_of_art='Siu1969 Theorem1 characterizes noetherian Stein-compact function rings by finiteness of connected components of analytic intersections. Buchweitz–Flenner explicitly uses semianalytic Stein compacta. No opened source was found proving the full abstract Lemma B as stated. Its unresolved proof obligation is uniform neighborhood stabilization from hypothesis(v), beyond pointwise noetherian stalks.',plausible_today='Use Siu’s exact analytic-intersection criterion for Stein compacta, or the verified semianalytic specialization. Treat the manuscript’s abstract unique-continuation criterion as a separate statement requiring a proof of uniform stabilization.',worth='Worth a short, sharply bounded proof audit of hypothesis(v); do not reopen the already established analytic criterion.')
change('CL-SA18-11110a',**{'class':'E'},origin='Literal Grothendieck lattice; product diagnosis is this run’s elementary calculation',fate='The elementary integral change of lattice basis makes the transcribed torus a product of elliptic curves. This is a standard lattice fact, not an attributed later discovery. The source’s intended nonprojectivity conclusion is false for this literal lattice; it remains a high-weight scan alarm.',fate_date='Classical lattice algebra; exact source-sheet date unknown; literal diagnosis checked2026-11-19')
change('CL-SA18-11110b',refs=['R-OortZarhin1996','R-RosenShnidman2017','R-MilneAV'],origin='Grothendieck’s existence goal; alternate explicit lattice is this run’s reconstruction',fate='The existence of nonalgebraic extensions of elliptic curves is established in the exact extension classification of Oort–Zarhin1996 Lemma3.2 and the algebraizability criteria following it. Rosen–Shnidman2017 Proposition2.3 gives the CM-period matrix and identifies algebraic extensions with torsion classes. Taking both periods i and a real irrational extension coordinate k produces precisely our alternative lattice. This does not correct the manuscript’s generators without scans.',fate_date='Oort–Zarhin communicated1995-11-27, published1996-12-16; references back to Shafarevich1974, whose passage was not opened. Rosen–Shnidman circulated2016-08-03 and published2017-05-01. No earliest-discovery claim.')
pmap['MP-SA18-11039'].update(state_of_art='Oort–Zarhin1996 Lemma3.2 and its following equivalent conditions classify extensions and detect algebraizability by torsion. Rosen–Shnidman2017 Proposition2.3 makes the same criterion explicit for CM periods; its matrix with periods i and irrational real coordinate k matches our alternative. MilneAV Proposition12.1 gives the independent complement obstruction. The literal manuscript lattice still splits.',refs=['R-OortZarhin1996','R-RosenShnidman2017','R-MilneAV'])

# Exact volume and theorem concordance, including incomplete source fragments.
locs={
 'CL-SA18-11104a':'EGA IV.2, Proposition 5.2.1 and Corollary 5.2.2',
 'CL-SA18-11104b':'EGA IV.2, Corollary 4.1.4',
 'CL-SA18-11104c':'EGA IV.2, Corollary 4.1.5',
 'CL-SA18-11104d':'EGA IV.2, Corollary 5.2.3',
 'CL-SA18-11105a':'EGA IV.2, Theorem 4.1.2(i)',
 'CL-SA18-11105b':'EGA IV.2, Theorem 4.1.2(i,ii)',
 'CL-SA18-11105c':'EGA IV.2, Remark 5.4.3',
 'CL-SA18-11106a':'EGA IV.2, Proposition 3.1.7(iii)',
 'CL-SA18-11106b':'EGA IV.2, Corollary 3.1.9',
 'CL-SA18-11106c':'EGA IV.2, Proposition 3.1.8 with finite prime avoidance in the affine coherent case',
 'CL-SA18-11106d':'EGA IV.2, Proposition 3.2.1'}
for cid,loc in locs.items():
    c=cs[cid]
    change(cid,refs=['R-EGAIV2']+(['R-Stacks07NB'] if cid.startswith('CL-SA18-11104') else []),fate=loc+' is the exact opened published comparison. '+c['fate'],fate_date='EGA IV.2 received 1963-12-15; published 1965. The manuscript sheets are undated; no earlier circulation date is inferred.')
change('CL-SA18-11103c',refs=['R-EGAIV2','R-Stacks00ON'],fate='EGA IV.2 Corollary 6.1.2 proves the exact flat local dimension formula; Stacks Lemma 10.112.7 supplies the going-down proof. Flatness is explicitly requested in the source margin.',fate_date='EGA IV.2 publication 1965; no first-circulation date for this particular result established')
change('CL-SA18-11103f',statement='If f is a global function on a locally noetherian scheme and its image in the residue field of every generic point is nonzero, every irreducible component of V(f) has codimension one. Equivalently, on an affine chart f belongs to no minimal prime.')
change('CL-SA18-11105c',fate='The manuscript’s actual example is Spec K→Spec B for a DVR B, a finite-type map because K=B[1/π], with source dimension0 and image-closure dimension1. EGA IV.2 Remark5.4.3 uses the same DVR mechanism and adds Spec of the residue field, obtaining a bijective local immersion from a zero-dimensional source. These are related formulations, not literally identical examples.')

i=its['SA18-11106']
c=dict(id='CL-SA18-11106e',items=[i['id']],cote=55,scans=[9],lines=[{'file':'SA18_texts/codex/K55-01_transcription.tex','start':249,'end':251}],his_statement='Ass F = union_i Ass F_i (the antecedent is absent from the supplied leaf).',statement='The surviving formula does not specify how F and F_i are related. The immediately corresponding published statement is: if quasi-coherent subsheaves F_i have union F, then Ass F is the union of Ass F_i. This missing hypothesis is identified from EGA, not restored to his words.',status_on_pages='stated without proof',computation={'method':'Conceptual union-of-submodules argument; no finite numerical calculation is asserted.'},**{'class':'A'},fate='EGA IV.2 Proposition 3.1.7(ii) prints the exact union formula just before the direct-sum formula matching the next source line. That order identifies the likely lost antecedent; its actual wording is unavailable on this leaf.',fate_date='EGA IV.2 publication 1965; selected source fragment undated',present_status='As of 2026-11-19: the published union-of-submodules theorem is established; the missing manuscript antecedent remains a documentary gap.',refs=['R-EGAIV2'],confidence='medium',research_searches=['RS-DIMENSION'],origin='Grothendieck manuscript; published comparator is explicitly separate')
claims.append(c);cs[c['id']]=c
event(c['id'],'used and rechecked in this run','Read the isolated manuscript formula and both adjacent published clauses of EGA IV.2 3.1.7. Preserved the missing antecedent rather than inventing source text.')
change('CL-SA18-11111',**{'class':'A'},refs=['R-EGAIV2'],statement='The source begins a definition of a reduced quasi-coherent module of finite type and breaks off after the associated-cycle clause. The later EGA definition requires no embedded associated points and length one at generic points of the support; the absent second clause is not claimed to survive on this leaf.',fate='EGA IV.2 Definition 3.2.2 and Proposition 3.2.3 identify the intended reduced-module notion and give its characterization as a torsion-free rank-one module on its reduced support. The exact selected manuscript definition remains incomplete.',fate_date='EGA IV.2 publication 1965; selected leaf undated',confidence='medium')
its['SA18-11111']['statement']=cs['CL-SA18-11111']['statement']
its['SA18-11111']['reconstruction']='The later published definition is identified from the opened EGA IV.2 3.2.2–3.2.3. Its absent generic-length condition is not inserted into the manuscript transcription.'

pmap['MP-SA18-11030'].update(plausible_today='For a smooth finite-type group over an artinian base, every torus lies in a maximal torus. For a reductive group over an arbitrary base, any torus lies in a maximal torus Zariski-locally. Thus the local-base/reductive alternative in the draft is covered; no unrestricted nonreductive arbitrary-base assertion is made.',state_of_art='Opened SGA3 XIV Corollary 1.4 proves the artinian case; Corollary 3.20 and Remark 3.21(c) prove Zariski-local existence and containment for smooth finitely presented groups with connected reductive geometric fibres. The separate lifting of a prescribed special-fibre torus in Remark 3.21(b) is a different question.',refs=['R-SGA3XII','R-SGA3XIV'])
pmap['MP-SA18-11037'].update(state_of_art='EGA 0IV Proposition 16.3.9 gives the upper bound using parameters; EGA IV.2 Corollary 6.1.2 gives equality under flatness. The opened Stacks Lemma 10.112.7 supplies the going-down proof. R10 independently repairs the false generator phrase.',refs=['R-EGAIV1','R-EGAIV2','R-Stacks00ON'])
pmap['MP-SA18-11038'].update(state_of_art='EGA IV.2 4.1.2,4.1.4–4.1.5 and5.2.1–5.2.3 prove the exact finite-type dimension, product, extension and pointwise formulas. Remark5.4.3 uses the same DVR mechanism and adds the residue-field point to make the morphism bijective. Stacks07NB supplies a second opened formulation.',refs=['R-EGAIV2','R-Stacks07NB'])

# Computation fields name only programs that really compute that claim.
for c in claims:
    co=c['computation']
    if 'certificate_keys' not in co:
        co.pop('code',None);co.pop('output',None)
        if 'proof_record' in co:co['scope']='The cited proof record is a conceptual mathematical argument; no finite calculation is represented as proving it.'
    else:
        co['code']='scripts/root_certificates.py';co['output']='outputs/root_certificates.json'
    if 'proof_record' in co:
        co['proof_record']=co['proof_record'].split(';')[0]
    if c['id']=='CL-SA18-11102':
        co.clear();co.update(method='No computation is asserted. The abstract uniform-stabilization step has not been independently proved; analytic special cases are identified in the opened sources.')
for cid,key in [('CL-SA18-11021','GIT_chart_inverse'),('CL-SA18-11100','coherent_elimination'),('CL-SA18-11107d','continuous_image_dimension')]:
    cs[cid]['computation'].update(code='scripts/root_extra_certificates.py',output='outputs/root_extra_certificates.json',certificate_keys=[key],scope='Exact symbolic/model identities supplement the general proof in research/root_proofs.md; finite instances alone do not establish the general claim.')
    event(cid,'computation or formal certificate','Executed scripts/root_extra_certificates.py; exact output group '+key+'.')

# Distinguish full re-proofs, targeted checks, reference reading, and refutations.
for cid,section in [('CL-SA18-11008','R1'),('CL-SA18-11014','R2'),('CL-SA18-11015','R2'),('CL-SA18-11021','R3'),('CL-SA18-11024','R3'),('CL-SA18-11037','R4'),('CL-SA18-11042','R5'),('CL-SA18-11065','R7'),('CL-SA18-11097','R9'),('CL-SA18-11100','R11'),('CL-SA18-11110b','R10')]:
    event(cid,'independent re-proof','Independent argument for the precisely qualified assertion is written in research/root_proofs.md '+section+'. This event does not claim that the full cited literature theorem was reproved.')
repairs={11009:'the corrected generating-family formulation in the same claim',11012:'the nonempty-block count in the same claim',11025:'the nonzero-functional criterion in the same claim',11033:'the order-dividing-two character in the same claim',11034:'the reduced-cohomology comparison in the same claim',11038:'the corrected Gysin degree table in the same claim',11047:'the signed primitive square in the same claim',11064:'the maximal-T version in the same claim',11096:'CL-SA18-11097',11103:'CL-SA18-11103b',11109:'the componentwise equicodimensional repair in CL-SA18-11109a',11110:'CL-SA18-11110b'}
for c in claims:
    if c['status_on_pages']=='false as stated':
        n=int(c['items'][0].split('-')[-1])
        event(c['id'],'refuted','The exact literal assertion fails for the counterexample or type/degree obstruction in this claim. Refined statement: '+repairs.get(n,c['id']+' (corrected interpretation explicitly stated in the record)')+'. Reading alarms remain undecided on the ink.')
for cid in ['CL-SA18-11064','CL-SA18-11096','CL-SA18-11100','CL-SA18-11109a','CL-SA18-11110a','CL-SA18-11110b']:
    event(cid,'targeted proof check','Agent16 independently reviewed the complete counterexample/repair argument and checked its hypotheses. Agent46 also checked the coherent-product elimination proof where applicable.','GPT-6 Astra Pro / inherited effort / SA18 agent16 independent review')
for r in json.loads((O/'references.json').read_text()):
    scope=r['verification_scope']
    typ='carried as background without fault found' if r['note']=='unverified' or ('bibliograph' in scope.lower() and 'only' in scope.lower()) else 'used and rechecked in this run'
    event(r['key'],typ,r['note']+': '+scope+' Exact locator: '+r['locator']+'. Opening metadata alone is not a theorem-proof check.')

# Report the final checked scope in the date-level event register. Earlier draft
# classifications remain reproducible in root_claims.py, but are not endorsed by
# the consolidated check record after exact-source follow-up.
for e in events:
    if e['type']=='used and rechecked in this run' and e['statement_id'] in cs:
        c=cs[e['statement_id']]
        e['outcome']='Read the source passage and checked the exact scope against the recorded searches and opened comparators. Final page status: '+c['status_on_pages']+'. '+c['fate']

(O/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2))
(O/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
(O/'problems.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2))
with (O/'claim_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'claims':len(claims),'problems':len(ps),'events':len(events),'new_exact_comparators':['EGA IV.2 3.1.7(ii)','EGA IV.2 3.2.2','SGA3 XIV1.4,3.20,3.21(c)']},indent=2))
