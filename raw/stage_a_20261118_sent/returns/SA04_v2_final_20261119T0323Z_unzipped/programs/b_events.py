from pathlib import Path
import json,csv,re
R=Path(__file__).resolve().parents[1];O=R/'parts/b'
I=json.loads((O/'items.json').read_text());C=json.loads((O/'claims.json').read_text())
events=[]
who='GPT-6 Astra Pro; effort inherited, not separately exposed; run SA04/notes_93_b'
def ev(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for x in I:
 ev(x['id'],'used and rechecked in this run','Textual comparison only, not a proof: every assigned source entry was read against the cited Pro passage and its Codex counterpart where supplied. '+x['check_reason'])
for x in C:
 ev(x['id'],'used and rechecked in this run','Textual comparison only: checked the statement, doubt/correction status, and source locators. Literature searches are recorded in search_log.tsv; a source statement match is not an independent proof.')
no_full_proof={203,204,211,216,217,220,221}
for x in C:
 n=int(x['id'].split('-')[-1])
 if n not in no_full_proof:
  ev(x['id'],'independent re-proof','The precise qualified mathematical statement/counterexample was independently derived in proof_checks.md. Where the record combines a classical cited general theorem with a small-characteristic counterexample, this event covers only the explicitly written derivation, not the cited theorem’s entire proof. '+x['computation'])
for n in [204,217]:
 ev('C-SA04-'+str(n),'carried as background without fault found','Classical C3 chain-rule extension or integral Hasse cocycle input is carried with the explicit scope in the record; no second complete proof of notes_93_a C-SA04-122 is credited here.')
for n in [210,213,214,215,218,219,223,225,226,227,231,235,241,242,246,247,250,252]:
 ev('C-SA04-'+str(n),'computation or formal certificate','Exact symbolic/matrix arithmetic, not proof-assistant certification: programs/b_computations.py rerun successfully; outputs/b_computations.json and b_computations_stdout.json retained. The specific identity or counterexample is named in the claim computation field.')
# These are intentional item-register targets, not abbreviated claim IDs.
# Each item contains the concrete correction or qualified surviving statement.
refinements=[
 (201,202,'An unused coherent direct summand disproves the unrestricted target-isomorphism assertion. Target generation is a necessary repair to specify, not a sufficient classification theorem proved here.'),
 (208,209,'For the stated horizontal-frame convention, D_g-D_f=-dlog(g/f), and D_dg-D_df=-dlog(dg/df). The positive cocycle corresponds to the opposite convention.'),
 (210,211,'The logarithmic ratio is (dg/g)/(df/f)=(dg/df)(f/g); its square is the later inversion-invariant expression.'),
 (214,215,'In c_n(g)-c_m(f), the second-input logarithmic derivative is f-prime/f, not g-prime/g.'),
 (227,228,'The quadratic-input coefficient is f-f-double-prime/f+(5/4)(f-prime/f)^2 relative to c_t, with the linear f term required by the preceding definition.'),
 (232,242,'The canonical equivariant identification with the relative-jet pushforward is obstructed in characteristic2; after inverting2 the scalar splitting is supplied by trace/2. An arbitrary local rank-four isomorphism is a weaker assertion.'),
 (235,244,'Over fields of characteristic not2 the adjoint projective/Lie automorphism comparison holds. In characteristic2, AutLie(pgl2)=GL(W) semidirect W has dimension6 and is larger than PGL2.'),
 (242,250,'The Killing-pairing identification g/Omega with L-dual holds with2 invertible; the characteristic2 nonsplit elliptic extension gives the stated counterexample without that hypothesis.'),
 (246,255,'Every derivation is inner with2 invertible, as the author later requires. In characteristic2, D(e)=f and D(h)=D(f)=0 is outer.')]
assert all('SA04-'+str(it) in {x['id'] for x in I} for _,it,_ in refinements)
for n,it,refinement in refinements:
 ev('C-SA04-'+str(n),"refuted, with the refined statement's id",'Refuted only in the literal or unrestricted formulation specified, with hypotheses/counterexample in proof_checks.md. Refined statement: SA04-'+str(it)+' (item register; this is not a claim ID). '+refinement+' Witness ambiguities remain reading questions; this does not identify the ink or authorize a diplomatic correction.')
for n in [231,232,233,234,235]:
 ev('SA04-'+str(n),'independent re-proof','Earlier-run idea, not manuscript claim: independently proved in proof_checks.md §3. No historical novelty is asserted; the prior proof files named in the notes were not available.')
for n in [231,232,233,235]:
 ev('SA04-'+str(n),'computation or formal certificate','Exact finite-field/Hasse diagnostics in b_computations.py, with saved output. Finite enumeration does not prove the arbitrary-ring statement.')
scopes={
'BDeligne1970':'I§1.3,Proposition1.7;I§2.3–2.6,Theorem2.17;I§5.2–5.12. Opened exact statements and indicated arguments; selective proof comparison, not full-book proof verification. Seminar1969 versus publication1970 checked.',
'BDumas2009':'§3.1–3.2,pp8–11; Schwarzian formula,cocycle,vanishing criterion and ODE description read. Used as classical framework, not proof of integral universality.',
'BBDOpers2005':'§1.2,§2.7,§3.1–3.3; smooth complex curve marked P1/oper and torsor statements read. Text-written1993/arXiv2005 distinction checked.',
'BHoshi2024':'§3Theorem3.5/Corollary3.6;§6Remark6.4.2; exact target and characteristic restrictions compared, not the whole paper independently proved.',
'BHoshi2020':'Titlepage/introduction datedApril2020; metadata/circulation check only.',
'BWakabayashi2021':'Introduction and§1.7,p10; odd prime,algebraicallyclosed andlocNoeth hypotheses read. No characteristic2 theorem inferred.',
'BGrothendieckBrauerI':'§5.1–5.3,§7.1–7.5,§8.1–8.5 opened and compared; Brauer obstruction distinguished from globallysplit presentation. TalkMay1965/publication1966 checked.',
'BAlberca2015':'§7pp15–16: ring derivation calculation beforeLemma12,Corollary4,Lemma13. Exactfield/ring scopes checked. These are not proofs about characteristic2pgl2.',
'BStacks058Q':'Proposition10.83.3 statement/proof read for finiteprojectivefaithfullyflatdescent.',
'BStacks0B5B':'Lemma53.5.2 statement/proof read; conditional genus≥2 consequence independentlyderived.',
'BStacks01OA':'§27.21 quotient convention read; noBrauer–Severi globalsplittinginferred.',
'BStacks0A2J':'Azumaya definition andLemma59.62.1 statement/proof read; endomorphismalgebraline-twist ambiguity.',
'BStacks09CN':'Lemma10.133.6 statement/proof read; firstprincipalparts only.',
'BIhara1974Metadata':'Institutionalauthorbibliographyitem13checked. FullpaperURLfailed; no theoremorproofverification.',
'BEGAIV4Metadata':'Numdam1967metadataopened; fullPDFtoo large andZbl403. NoexactEGA16.3proofverification.',
'BSGA3Metadata':'SMFpublishermetadataopened; seminar1962–64,original1970,recomposed2011. NooriginalSGA3theoremverification.',
'BGrothendieckBibliography':'CSG65andEGA/SGAmetadataread asdiscoverybibliography only.'}
for k,v in scopes.items():ev(k,'used and rechecked in this run','Primary-source or metadata comparison, not blanket proof certification: '+v)
with (O/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'check_events':len(events)}))
