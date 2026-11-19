"""Manually reasoned records; source reading and judgments are not generated from headings."""
import csv, json, pathlib
BASE=pathlib.Path(__file__).resolve().parent
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner groupes'
F1='sources/texts/codex/K161-1-01_transcription.tex'
items=[]; claims=[]; problems=[]; readings=[]; events=[]; searches=[]; links=[]; bibliography=[]

def source_file(part):
    return F1 if part=='1' else f'sources/texts/codex/K161-2-{int(part):02d}_transcription.tex'

def unit(n,part,title,scans,lines,words):
    i=f'SA23-{n}'; f=source_file(part); cote='161-1' if part=='1' else '161-2'
    items.append(dict(id=i,sources=[],kind='other',cote=[cote],scans=scans,lines=[f'{f}:{lines}'],his_words=words,statement=title,reconstruction='Additional archival unit from a fully read Codex transcription; its companion note is a lead and receives no Stage 1 verdict row.',check='agrees',check_reason='The actual source passage was read in full; mathematical corrections and withdrawn formulations are distinguished in the linked claims.'))
    return i

def addclaim(n,item_no,part,scans,lines,his,today,status,proof,fate,refs,cls='B',confidence='high',event='independent re-proof'):
    cid=claim(n,f'SA23-{item_no}',scans,lines,his,today,status,proof,fate,refs,cls,confidence,event)
    claims[-1]['cote']=['161-1' if part=='1' else '161-2']
    claims[-1]['lines']=[f'{source_file(part)}:{lines}']
    return cid

def occurrence(part,scans,lines,status='live question'):
    return dict(cote='161-1' if part=='1' else '161-2',scans=scans,file=source_file(part),lines=lines,drafting_status=status)

def addproblem(n,title,occurrences,as_he,plausible,state,refs,worth='Useful for a precise commentary; the stated mathematical issue is settled or narrowed by the linked claims.'):
    problems.append(dict(id=f'MP-SA23-groupes-{n:02d}',title=title,occurrences=occurrences,as_he_states=as_he,plausible_today=plausible,state_of_art=state,why_open='No historical reason is stated. Cancellations, answers and changes of formulation are recorded at their actual occurrences; none is interpreted as evidence of a failed research program.',worth=worth,refs=refs))

def search(query,nums,opened,limits='',engine='web search, followed by opening the exact primary source'):
    searches.append(dict(date=DATE,query=query,engine=engine,claims=[f'C-SA23-groupes-{n:03d}' for n in nums],opened=opened,limits=limits))

def checked_ref(key,outcome,kind='targeted proof check'):
    events.append([key,DATE,WHO,kind,outcome])

def item(n,title,scans,lines,words):
    i=f'SA23-{n}'
    items.append(dict(id=i,sources=[],kind='other',cote=['161-1'],scans=scans,lines=[f'{F1}:{lines}'],his_words=words,statement=title,reconstruction='Additional archival unit from fully read Codex transcription; not an indexed Stage 1 note entry.',check='agrees',check_reason='Read directly in the transcription and companion Codex note; no indexed-entry verdict row is added.'))
    return i

I1=item(901,'Adjunction fixed parts and reflective localization',[4,5,6,7,8],'1–281','Ceci n’est pas nécessaire ...')
I2=item(902,'Finite families, symmetric monoidal coherence, and invertible-object signs',[10,11,12,13],'284–466','catégorie symétrique unitaire')
I3=item(903,'Exactness of extension from a small category',[14,16],'469–575','ne sera jamais exact à droite')
I4=item(904,'Tannakian grading and semilinear conjugation',[17],'579–636','Int ρ(σ)')
I5=item(905,'Dense subcategories and left Kan extension',[18,19,20],'639–727','cofinal')

def claim(n,item_id,scans,lines,his,today,status,proof,fate,refs,cls='B',confidence='high',event='independent re-proof'):
    cid=f'C-SA23-groupes-{n:03d}'
    claims.append(dict(id=cid,items=[item_id],cote=['161-1'],scans=scans,lines=[f'{F1}:{lines}'],his_statement=his,statement=today,status_on_pages=status,computation=dict(code=None,output=None,proof_or_check=proof,limit='Analytic reasoning; no claim of machine formalization.'),**{'class':cls},fate=fate,fate_date='Matched source/version dates in references.bib. Undated sheets do not establish priority. Present status dated 19 November 2026.',present_status='As of 19 November 2026: '+proof,refs=refs,confidence=confidence))
    events.append([cid,DATE,WHO,event,proof])
    return cid

c1=claim(1,I1,[4],'5–59','Full faithfulness on E′ is sufficient from invertibility of the unit, and necessary if RL(E′) remains in the full subcategory.','For L⊣R and full E′⊂E with RL(E′) in its essential closure, L|E′ is fully faithful iff η_Y is invertible for every Y∈E′; the dual counit statement holds.','proved there','The adjunction comparison is Hom(X,η_Y). Bijectivity for X,Y∈E′ and closure of RL(Y) let Yoneda in E′ detect invertibility. The converse needs no closure.','RiehlContextOnline Lemma 4.5.11 gives the global criterion; the full-subcategory version is re-proved here with its closure condition.',['RiehlContextOnline'])
c2=claim(2,I1,[4],'5–59','Trouver un exemple ... E′ réduit à un seul objet.','The closure condition cannot be omitted, even for a one-object E′.','open on the pages','Take E the poset 0<1, F the terminal category, L unique and R selecting 1. For E′={0}, L|E′ is fully faithful, but η_0:0→1 is not invertible. All adjunction hom-sets are singletons.','The standard unit criterion in RiehlContextOnline Lemma 4.5.11 isolates the missing global hypothesis; this exact two-object counterexample is supplied in this run.',['RiehlContextOnline'])
c3=claim(3,I1,[4],'27–36','Faithful / monomorphism parenthetical, followed by necessity under closure.','If the claimed necessity means η_Y monic in all of E, faithfulness of L|E′ and RL(E′)⊂E′ do not suffice. They give only E′-relative monicity.','false as stated, if the parenthesis is ambient','E has objects Z,Y,T, distinct f,g:Z→Y, unique h:Y→T and k:Z→T with hf=hg=k, and identities. T is terminal. Let L:E→1, R(*)=T, E′={Y,T}. The restricted L is faithful on each hom-set and RL(E′)⊂E′, but η_Y=h is not monic because f≠g.','RiehlContextOnline Lemma 4.5.11 is a statement for the whole adjoint functor; it does not assert this false restricted criterion. The relative correction and finite witness are present reconstruction.',['RiehlContextOnline'],'C',event='refuted, with refined statement RF-SA23-groupes-003')
c4=claim(4,I1,[5,6],'61–210','Les objets où η ou ε est un isomorphisme se correspondent; questions de réflexion et coréflexion.','The full subcategories E0={η_X invertible}, F0={ε_Y invertible} correspond by L,R. If η_R is invertible (equivalently ε_L), E0 is reflective in E and F0 coreflective in F.','proof sketched with open steps','Triangle identities restrict L,R to inverse equivalences. If η_R is invertible then μ=RεL is its inverse and monad identities give Tη=ηT. Transposing this equality gives Lη·ε_L=id; the other triangle gives ε_L·Lη=id. Thus ε_L is invertible. Unit/counit give reflector RL and coreflector LR.','RiehlContextOnline Exercise 5.1.iii and Proposition 5.3.3 match idempotent monads and their reflective fixed objects; the adjunction equivalence and dual statement are checked directly.',['RiehlContextOnline'])
c5=claim(5,I1,[7],'214–231','Examples with a category reduced to one object.','Adjunction with the terminal category selects an initial object on the left and a terminal object on the right.','proved there','The required Hom(-,-) sets are singletons exactly by the defining initial/terminal universal properties. Singleton inclusions are fully faithful.','RiehlContextOnline Chapter 4 supplies the adjunction framework; the complete elementary argument is given here.',['RiehlContextOnline'])
c6=claim(6,I1,[7,8],'233–281','Representability after a localization; existence of a right adjoint after composition.','For a reflector a:E→E1 with fully faithful right adjoint j, a presheaf ψ on E1 whose pullback along a is representable is representable. If βa has a right adjoint R then β has right adjoint aR.','open on the pages','A representing ξ is local because Hom(-,ξ) inverts every arrow inverted by a, in particular the units. Applied to η_ξ this supplies a retraction; naturality and the invertibility after a give the other inverse identity. Hence ξ≅j(aξ); Yoneda and the counit descend the representing isomorphism. Apply this objectwise to Hom(βa(-),Y) to obtain aR. Full faithfulness of β is unnecessary.','RiehlContextOnline Definition 4.5.12 and Proposition 5.3.3 identify the local objects. The descent and adjoint-composition assertion are independently proved here, not attributed as verbatim statements in that source.',['RiehlContextOnline'])

def problem(n,title,scans,lines,as_he,plausible,state,refs):
    problems.append(dict(id=f'MP-SA23-groupes-{n:02d}',title=title,occurrences=[dict(cote='161-1',scan=s,file=F1,lines=lines,drafting_status='live question, answered in this run') for s in scans],as_he_states=as_he,plausible_today=plausible,state_of_art=state,why_open='The pages give no historical reason for leaving this step open; none is inferred.',worth='Useful for a precise commentary and proof repair; the stated issue is settled by the argument recorded here.',refs=refs))

problem(1,'One-object failure of the restricted unit criterion',[4],'5–59','Find an example with E′ reduced to one object.','The closure condition on RL(E′) is necessary for the stated implication.',c2+' gives a two-element poset counterexample; '+c1+' proves the valid criterion.',['RiehlContextOnline'])
problem(2,'Idempotent adjunction fixed parts',[5,6],'61–210','The dotted-arrow identity and the reflection/coreflection properties are queried.','η_R invertible iff ε_L invertible; the fixed subcategories are reflective/coreflective.',c4+' gives the triangle-identity proof; RiehlContextOnline Proposition 5.3.3 identifies the idempotent-monad fixed category.',['RiehlContextOnline'])
problem(3,'Representability descending through a reflector',[7,8],'233–281','Does representability after pullback imply representability, and does a right adjoint descend?','Yes for a reflector with fully faithful right adjoint; βa⊣R implies β⊣aR.',c6+' proves locality of the representing object and the adjoint formula.',['RiehlContextOnline'])

readings.extend([
['161-1','6','188','Im u ⊂ E0','Im u ⊂ F0','u:E→F has image in F; the surrounding fixed-counit discussion concerns F0.','high','high'],
['161-1','7','238','α has a right adjoint','possibly α′ has right adjoint α','The reflector already has the full inclusion as right adjoint; a reflective inclusion need not itself be coreflective.','high','medium'],
['161-1','8','265','ξ lies in E1 / αξ','ξ1∈E1 and ξ≅αξ1∈E','The representing object before descent belongs to E.','high','high'],
['161-1','8','276','Hom_E1 with arguments in E','Hom_E','The arguments before applying the reflector lie in E.','high','high'],
])

searches.append(dict(date=DATE,query='Emily Riehl Category Theory in Context reflective subcategory idempotent monad unit fully faithful adjunction',engine='system2; followed by official author-site lookup and full PDF download',claims=[c1,c2,c3,c4,c5,c6],opened=[dict(url='https://emilyriehl.github.io/files/context.pdf',locators='Lemma 4.5.11 pp161–162; Exercise 5.1.iii p189; Proposition 5.3.3 p199',match='Exact global adjunction and idempotent-monad results; restricted counterexamples and localization descent are independent proofs.')],limits='Current author PDF is a second-edition revision of the 2016 book; no manuscript priority inferred. Earlier author URL returned404.'))

def write():
    for name,data in [('items.json',items),('claims.json',claims),('problems.json',problems)]:
        (BASE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    def tsv(name,header,rows):
        with (BASE/name).open('w',newline='') as f:
            w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
    tsv('entries.tsv',['entry_id','item_id','verdict','reason'],[])
    tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)
    tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)
    tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)
    (BASE/'search_log.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in searches))
    (BASE/'references.bib').write_text('''@misc{RiehlContextOnline,
  author={Emily Riehl},
  title={Category Theory in Context: current author second-edition PDF},
  url={https://emilyriehl.github.io/files/context.pdf},
  howpublished={Author-hosted revision; first edition published in 2016; this PDF is undated},
  urldate={2026-11-19},
  note={verified}
}
'''+''.join(bibliography))

if __name__=='__main__':
    for p in sorted(BASE.glob('records_*.py')):
        exec(compile(p.read_text(),str(p),'exec'),globals())
    write()
    print(json.dumps({'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'indexed_entry_rows':0}))
