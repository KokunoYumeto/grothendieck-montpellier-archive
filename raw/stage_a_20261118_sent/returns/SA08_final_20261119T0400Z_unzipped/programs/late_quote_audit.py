"""Manual literal-source quotation audit of late claims and indexed items.

All selections below follow close reading. The code checks copying and records
locators; it neither assigns verdicts nor infers mathematics from cue words.
"""
from pathlib import Path
import csv
import json

B=Path('/workspace/scratch/7feb9690b71f/SA08_work')
P=B/'work/late'
WHO='GPT-6 Astra Pro; effort not exposed by runtime; SA08/late'
FILES={'D':'pro/MPL_136_235-281_transcription.tex',
       'E':'pro/MPL_136_282-327_transcription.tex'}
specs=[]
def Q(n, packet, passages, voice='authorial working text'):
    specs.append((f'SA08-C{n}',packet,passages,voice))

Q(201,'D',[(18,18,None),(30,30,None)])
Q(202,'D',[(22,22,None)])
Q(203,'D',[(43,43,None),(46,46,None)])
Q(204,'D',[(92,92,None),(115,115,None)])
Q(205,'D',[(164,164,None),(168,170,None)])
Q(206,'D',[(202,202,None),(205,205,None)])
Q(207,'D',[(210,211,None)])
Q(208,'D',[(229,229,None)])
Q(209,'D',[(446,446,None),(467,467,None)],'cancelled working block, D378–469')
Q(210,'D',[(688,689,None),(693,695,None)],'cancelled working block, D656–720')
Q(211,'D',[(795,795,None),(835,836,None)],'cancelled working block, D792–847')
Q(212,'D',[(285,285,None),(357,357,None),(474,474,None),(634,634,None)])
Q(213,'D',[(374,374,r"mais en général pas à gauche, sans doute --- on ne s'attend pas qu'il ait encore un adj. à g.")])
Q(214,'D',[(741,744,None)])
Q(215,'D',[(773,775,None),(1802,1802,None)])
Q(216,'D',[(901,907,None),(914,915,None)])
Q(217,'D',[(850,853,None)])
Q(218,'D',[(924,927,None),(957,958,None)])
Q(219,'D',[(1053,1057,None)])
Q(220,'D',[(1161,1163,None)])
Q(221,'D',[(1249,1250,None),(1253,1253,None),(1257,1258,None)])
Q(222,'D',[(1329,1329,None),(1333,1333,None)])
Q(223,'D',[(1362,1363,None)])
Q(224,'D',[(1453,1454,None),(1496,1496,None)])
Q(225,'D',[(1567,1569,None)])
Q(226,'D',[(1571,1571,None)])
Q(227,'D',[(1613,1614,None),(1618,1620,None)])
Q(228,'D',[(1624,1624,None)])
Q(229,'D',[(1663,1664,None)])
Q(230,'D',[(1700,1702,None)])
Q(231,'D',[(1732,1733,None),(1772,1773,None)])
Q(232,'D',[(1840,1842,None)])
Q(233,'D',[(1882,1882,None)],'cancelled working block, D1864–1909')
Q(234,'D',[(1869,1869,None),(1872,1872,None)],'cancelled working block, D1864–1909')
Q(235,'E',[(87,87,None),(102,102,None)])
Q(236,'E',[(165,165,None)])
Q(237,'E',[(582,585,None),(589,589,None)])
Q(238,'E',[(640,640,None),(651,652,None)])
Q(239,'E',[(693,693,None),(704,707,None)])

Q(265,'D',[(243,243,r'le foncteur $G\longmapsto G^{\mathrm{an}}$'),
          (243,243,r'est pleinement fidèle, comme il serait facile à établir grâce aux résultats du type GAGA relatifs [10].')],
  'authored reused SGA7 donor text')
Q(266,'D',[(184,184,r"Plus délicate sans doute est la question de savoir si, pour un espace analytique $X$ propre sur $S$, tel que le complété formel $\widehat X$ le long de $X_s$ soit algébrisable, $X$ est algébrisable sur $S$ au voisinage de $s$.")],
  'authored reused SGA7 donor text')
Q(267,'D',[(128,128,None),(136,136,None)],'authored reused SGA7 donor text')
Q(268,'D',[(56,56,None),(78,78,r"où $B'_K$ s'identifie d'ailleurs au schéma abélien dual de $B_K$ (8.2).")],
  'authored reused SGA7 donor text')
Q(269,'D',[(1086,1090,None)],'authored reused SGA7 donor text')
Q(270,'D',[(1285,1288,None)],'authored reused SGA7 donor text')
Q(271,'D',[(1369,1369,None)],'authored reused SGA7 donor text')
Q(272,'D',[(1375,1375,None)],'authored reused SGA7 donor text')
Q(273,'D',[(1424,1424,r"J'ignore si de tels \(M_n\) existent nécessairement (et en doute fort).")],
  'authored reused SGA7 donor text')
Q(274,'D',[(1577,1577,r"Il peut être intéressant d'observer que cette fonction à valeurs entières sur \(I\) peut se réconstituer également par la connaissance de \(T_\ell(A_K)\) pour \(\ell=p\) - du moins (pour le moment) en inégales caractéristiques.")],
  'authored reused SGA7 donor text')
Q(275,'E',[(620,620,r"(sous réserve, lorsque $\ell=p$, de disposer du théorème de Tate [33, th.4], i.e. pour l'instant qu'on soit alors dans le cas d'inégales caractéristiques)")],
  'authored reused SGA7 donor text')
Q(276,'D',[(1635,1637,None)],'authored reused SGA7 donor text')
Q(277,'D',[(1711,1711,r'que nous laissons au soin du lecteur à expliciter.'),(1723,1725,None)],
  'authored reused SGA7 donor text')
Q(278,'D',[(1822,1822,r"\uline{Alors il existe une extension finie galoisienne} \(K'\) \uline{de} \(K,\) \uline{telle que le schéma abélien} \(A_{K'}=A_K\otimes_K K'\) \uline{ait réduction semi-stable} (3.4) \uline{sur le normalisé} \(S'\) \uline{de} \(S\) \uline{dans} \(K'.\)")],
  'authored reused SGA7 donor text')
Q(279,'E',[(135,135,None),(139,141,None)],'authored reused SGA7 donor text')
Q(280,'E',[(724,724,r"Pour simplifier, nous allons admettre que $P$ \uline{est représentable par un schéma en groupes sur} $S$")],
  'authored reused SGA7 donor text')
Q(281,'E',[(527,530,None),(536,536,None)],'reused analysis exercise')
Q(282,'E',[(541,541,r'Montrer que si la série $c_n$ est divergente, alors $u_nc_n$ est convergente si et seulement si on a'),(542,542,None)],
  'reused analysis exercise')
Q(283,'E',[(478,482,None)],'reused analysis exercise')
Q(284,'D',[(1571,1571,None)],'manuscript compatibility phrase; gcd deduction is from the earlier run and Cartan')
Q(288,'D',[(1185,1187,None),(1190,1192,None)],'authored reused SGA7 donor text')

overrides={}
audit=[]
events=[]
def extract(sid,packet,passages,voice):
    fn=FILES[packet]
    lines=(B/'sources/texts'/fn).read_text().splitlines()
    fragments=[]; locators=[]
    for a,b,selection in passages:
        source='\n'.join(lines[a-1:b])
        fragment=source.strip() if selection is None else selection
        assert fragment in source,(sid,a,b,fragment)
        fragments.append(fragment)
        locators.append({'file':fn,'lines':str(a) if a==b else f'{a}–{b}'})
    quote=' … '.join(fragments)
    if voice.startswith('cancelled'):
        quote='Cancelled passage: “'+quote+'”'
    rec={'his_statement':quote,'quotation_lines':locators,'quotation_scope':voice}
    audit.append({'id':sid,'voice':voice,'literal_fragments':fragments,'quotation_lines':locators})
    events.append(dict(statement_id=sid,date='2026-11-19',who=WHO,
      type='used and rechecked in this run',
      outcome='Manually selected a short literal quotation after reading the actual passage. Exact copying and line locators checked; no diplomatic reading changed. '+voice+'. This source-fidelity event is not an independent mathematical proof.',
      refined_statement_id='',evidence='; '.join(f"{x['file']}:{x['lines']}" for x in locators)))
    return rec

for sid,packet,passages,voice in specs:
    overrides[sid]=extract(sid,packet,passages,voice)

# The middle colleague selects these manually from the full source passages.
# Their copied excerpts are independently checked before final application.
mid=P.parent/'middle/late_quote_candidates.json'
if mid.exists():
    incoming=json.loads(mid.read_text())
    assert not set(incoming)&set(overrides)
    for sid,rec in incoming.items():
        parts=rec['his_statement'].split(' … ')
        assert len(parts)==len(rec['quotation_lines']),sid
        for fragment,loc in zip(parts,rec['quotation_lines']):
            a,*rest=loc['lines'].replace('–','-').split('-')
            b=rest[0] if rest else a
            lines=(B/'sources/texts'/loc['file']).read_text().splitlines()
            assert fragment in '\n'.join(lines[int(a)-1:int(b)]),sid
        overrides[sid]={**rec,'quotation_scope':'authorial working text; manually selected by middle, independently source-checked by late'}
        audit.append({'id':sid,'voice':'authorial working text',
                      'literal_fragments':parts,'quotation_lines':rec['quotation_lines']})
        events.append(dict(statement_id=sid,date='2026-11-19',who=WHO,
          type='used and rechecked in this run',
          outcome='Independently read the actual passage and reviewed the middle colleague’s manually selected literal quotation. Exact locators and uncertainty marks checked. Source fidelity only, not another mathematical proof.',
          refined_statement_id='',
          evidence='; '.join(f"{x['file']}:{x['lines']}" for x in rec['quotation_lines'])))

# These three are explicitly the consolidation's refinements, never attributed
# to the manuscript as independent assertions.
for n,parent,label in [
 (285,255,"This run's flat-hypothesis reconstruction; related source question"),
 (286,230,"This run's completed coefficient-presentation proof; related source relations"),
 (287,216,"This run's replacement quotient; related source definition")]:
    sid=f'SA08-C{n}'; original=overrides.get(f'SA08-C{parent}')
    if original:
        overrides[sid]={
          'his_statement':label+': “'+original['his_statement']+'”',
          'quotation_lines':original['quotation_lines'],
          'quotation_scope':'No separate authorial assertion. The quoted related source does not assert this reconstruction.'}
        audit.append({'id':sid,'voice':overrides[sid]['quotation_scope'],
          'literal_fragments':next(x['literal_fragments'] for x in audit if x['id']==f'SA08-C{parent}'),
          'quotation_lines':original['quotation_lines']})
        events.append(dict(statement_id=sid,date='2026-11-19',who=WHO,
          type='used and rechecked in this run',
          outcome='Confirmed that this row is a reconstruction by the consolidation, not a verbatim manuscript claim. A related literal source passage is supplied only as provenance.',
          refined_statement_id='',evidence=f'Related source quotation: SA08-C{parent}'))

claims=json.loads((P/'claims.json').read_text())
for c in claims:
    if c['id'] in overrides:
        c.update(overrides[c['id']])
    if c['id']=='SA08-C284':
        c['scans']=[273]
        c['lines']='D1571; earlier-note MPL_136_235-281#74, not #75'
        c['status_on_pages']='Only compatibility with multiplication is stated here; the binomial-factor/gcd recovery deduction is the earlier run’s comparison with Cartan.'
        c['origin']='Manuscript phrase about compatibility; earlier-run deduction in note#74; exact published Cartan antecedent identified. The binomial equations on275 are the module-rigidity calculation, not a displayed weighted-product formula.'
    if c['id']=='SA08-C283':
        c['scans']=[292]
        c['lines']='E478–486'
(P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')

# Item-to-claim links below are manual semantic selections, not keyword matches.
# Other items have their own short source anchors.
item_claim={
403:201,405:205,406:206,407:203,408:209,410:210,411:211,
415:212,416:213,417:214,420:215,421:216,422:217,
423:216,425:218,426:219,427:220,428:221,431:222,432:223,
437:225,438:226,439:227,440:228,441:229,
442:230,443:231,444:232,446:233,447:234,459:266,460:265,
461:269,462:270,463:272,464:273,465:274,466:276,467:277,
468:278,471:284,473:289,474:248,475:241,476:289,477:245,
478:290,479:251,482:244,483:237,484:239,486:261,487:264,
488:252,489:255,490:235,491:246,498:262,499:262,500:264,
502:263,503:260,508:280,523:288}
item_quotes={}
for n,cnum in item_claim.items():
    source=overrides.get(f'SA08-C{cnum}')
    if not source:
        continue
    sid=f'SA08-{n}'
    item_quotes[sid]={'his_words':source['his_statement'],
                     'quotation_lines':source['quotation_lines'],
                     'quotation_scope':source['quotation_scope']}
    original=next(x for x in audit if x['id']==f'SA08-C{cnum}')
    audit.append({**original,'id':sid})
    events.append(dict(statement_id=sid,date='2026-11-19',who=WHO,
      type='used and rechecked in this run',
      outcome='Reviewed this item against the actual passage and replaced its paraphrased quotation field with the manually selected literal source excerpt. Mathematical verdict unchanged. Voice and diplomatic markers remain explicit.',
      refined_statement_id='',evidence=f"Same literal passage as SA08-C{cnum}; "+'; '.join(f"{x['file']}:{x['lines']}" for x in source['quotation_lines'])))
def I(n,packet,passages,voice='authorial working text'):
    sid=f'SA08-{n}'
    q=extract(sid,packet,passages,voice)
    item_quotes[sid]={'his_words':q['his_statement'],
                     'quotation_lines':q['quotation_lines'],
                     'quotation_scope':voice}
I(402,'D',[(875,875,None)],'printed donor notice, not Grothendieck’s mathematical text')
I(404,'D',[(85,88,None)],'cancelled unfiltered comparison')
I(412,'D',[(1620,1620,None)])
I(413,'E',[(761,761,"objet d'un topos")])
I(414,'D',[(64,64,None)],'authored reused SGA7 donor heading')
I(418,'D',[(1745,1745,None)])
I(419,'D',[(1802,1802,None)],'related authorial recurrence; its constancy proof is the earlier run’s argument')
I(424,'D',[(893,897,None)])
I(433,'D',[(1453,1454,None)])
I(434,'D',[(1462,1462,None),(1466,1467,None)],'cancelled working block, D1457–1468')
I(435,'D',[(1494,1494,None),(1496,1496,None)])
I(436,'D',[(1517,1517,None)],'cancelled working block, D1500–1519')
I(453,'D',[(115,115,None)])
I(472,'E',[(748,748,None),(761,761,r"objets $\tfrac12$ simpliciaux")])
I(480,'E',[(1559,1559,None),(1608,1610,None)])
I(481,'E',[(1655,1655,r"attention, dans cette formule \unsure{apparaît la confusion en attendant} de la situation")])
I(497,'E',[(1881,1881,None)])
I(509,'E',[(519,519,None),(536,536,None)],'reused analysis exercise')
I(510,'E',[(1780,1780,None)],'cancelled working block, E1767–1819')
I(511,'E',[(733,735,None)],'authorial cover wording, doubtful title word retained')
I(515,'E',[(753,754,None)])
I(516,'E',[(801,801,None),(809,809,None)])
I(517,'E',[(645,646,None)])
I(518,'E',[(1556,1556,None)])
I(519,'E',[(1683,1683,None)])
I(520,'E',[(1897,1897,None),(1946,1946,None)])
items=json.loads((P/'items.json').read_text())
for item in items:
    if item['id'] in item_quotes:
        item.update(item_quotes[item['id']])
(P/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
(P/'item_quote_overrides.json').write_text(json.dumps(item_quotes,ensure_ascii=False,indent=2)+'\n')

# Propagate corrected source fields to every occurrence, without rebuilding the
# problem dossiers and losing their separately checked state-of-art refinements.
by_id={c['id']:c for c in claims}
problems=json.loads((P/'problems.json').read_text())
for problem in problems:
    for occurrence in problem['occurrences']:
        c=by_id[occurrence['claim']]
        occurrence.update(cote=c['cote'],scans=c['scans'],lines=c['lines'],
                          his_statement=c['his_statement'])
        for key in ['quotation_lines','quotation_scope']:
            if key in c:
                occurrence[key]=c[key]
    if problem['id']=='MP-SA08-68':
        problem['as_he_states']='At scan273 the manuscript asks for compatibility with multiplication. The earlier run’s note#74 proposes recovering the ordinary product from compatible weighted factors; that deduction is not a displayed formula in the module-rigidity calculation on275.'
(P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

(P/'quote_overrides.json').write_text(json.dumps(overrides,ensure_ascii=False,indent=2)+'\n')
(P/'quotation_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
with (P/'quotation_CHECK_EVENTS.tsv').open('w') as f:
    w=csv.DictWriter(f,list(events[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(events)
print(json.dumps({'literal_claim_records':len(overrides),
                  'expected_final_records':len(claims),
                  'literal_item_records':len(item_quotes),
                  'source_fidelity_events':len(events)},indent=2))
