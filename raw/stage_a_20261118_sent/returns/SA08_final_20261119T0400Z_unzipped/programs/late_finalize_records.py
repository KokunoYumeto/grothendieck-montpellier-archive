"""Apply manually reviewed final corrections; this is not a verdict generator.

Run after the late_build_* serializers. The literal adjustments below record
source-access updates and the final source-to-publication chronology convention.
"""
from pathlib import Path
import csv,json
P=Path('/workspace/scratch/7feb9690b71f/SA08_work/work/late')
items=json.loads((P/'items.json').read_text()); I={x['id']:x for x in items}
claims=json.loads((P/'claims.json').read_text()); C={x['id']:x for x in claims}

C['SA08-C204']['fate']="""Cartan1976 Theorem3 p267 requires flat cycles; §6 p268 weakens extendability to splitting and records multiplicativity requirements; §7 gives the weighted range. Garvin1998 was read in full: Theorems4.1–4.2 pp175–176 apply to arbitrary simplicial sets in the STRICT range p<q; Proposition3.2 and Remark3.3 pp174–175 give q-extendability and its failure at q+1. The phrase up to q in4.3 does not enlarge the explicit4.2 range. This does not independently settle the boundary i=p in the manuscript's arbitrary completed filtered setting. Miller's finite-complex scope is reported in Garvin's introduction; exact original verification is separately handled in the parent dossier."""
C['SA08-C204']['present_status']="""As of 2026-11-19: The integral weighted construction has exact published developments. Garvin's strict p<q theorem does not by itself prove this manuscript's inclusive i<=p boundary or arbitrary completed-coefficient assertion. This does not produce an ordinary strictly commutative integral cochain model in all degrees."""
C['SA08-C205'].update(statement='For t=0 the source identifies the graded piece with Gamma_k^p(Psi_*), then uses an uncertain Pi_*/K_* name and claims nonflasqueness for every p. Under the standard simplex quotient Psi this is not an ordinary K(k,p): normalized Gamma²(Psi) is k --2→ k in degrees2→1.',status_on_pages='asserted with a doubtful object name; ordinary Eilenberg–Mac Lane and all-p nonflasqueness readings fail in the standard model',fate='Breen–Mikhailov–Touzé2016 Proposition3.5 and Corollary3.6p270 identify the derived nonlinear framework and the rational odd-shift exterior result. This agrees with the direct quadratic calculation: overZ, H1=Z/2; overQ the weight2 complex is acyclic. Cartan’s weighted comparison does not validate the stronger ordinary-K reading of this degenerate object.',present_status='As of2026-11-19: Retain Gamma^p(Psi) and the uncertain Pi/K notation separately. The ordinary K(k,p) interpretation is refuted in weight2, and the all-p nonflasqueness assertion fails overQ under the standard convention. Weight1 remains nontrivial, so the degenerate unfiltered construction is still not generally acyclic.',refs=['late_BMT2016','late_Richter2009'],searches=['L01','L11'],proof_check='proofs.md §15 and programs/late_quadratic_normalization.py derive all quadratic faces and the normalized boundary. This is an explicit mathematical alarm, not an ink emendation.',computation='programs/late_quadratic_normalization.py; logs/late_quadratic_normalization.json; exact integral matrix and general support argument.',confidence='high')
C['SA08-C205']['class']='C'
I['SA08-405'].update(statement='The t=0 degeneration is identified with Gamma^p(Psi); the next Pi_*/K_* name is doubtful. The claimed nonflasqueness for every weight needs qualification: in the standard model Gamma²(Psi) is acyclic overQ, although weight1 is nontrivial.',reconstruction='The note wisely does not settle the doubtful name. This run corrects its own earlier overinterpretation as ordinary K(k,p), using the exact quadratic normalization and BMT2016.',check_reason='The source explicitly warns against dropping the graded-free hypothesis, which supports the note. Its intermediate all-weight homotopy/nonflasqueness wording needs the new quadratic alarm; no manuscript ink is changed.')

# The A classification here follows the donor-draft-to-print history. It never
# suggests that a 1972 publication followed the live 1975–1976 PD work.
for n in [267,268,269,270,271,272,274,276,277,278,279]:
 c=C[f'SA08-C{n}']; c['class']='A'
 c['fate_date']='Donor text from SGA7 seminar1967–1969, published SGA7I1972; this publication precedes the live1975–1976 PD compilation.'
 c['chronology_note']='A denotes the exact authored SGA7IX donor-text-to-publication match, not a later development of the de Rham manuscript.'
for n in [270,274,275]:
 if 'late_LevinTate' not in C[f'SA08-C{n}']['refs']:
  C[f'SA08-C{n}']['refs'].append('late_LevinTate')

I['SA08-489']['statement']="""The general convolution-PD and uniqueness questions are unfinished. Finite projective coalgebras admit the base-change construction; the construction extends to flat coalgebras by symmetric tensors. The unrestricted nonflat existence assertion has an explicit counterexample. The uniqueness counterexample covers only positive-index composition and fixed-object binomial product identities; q=0 composition and full additive naturality exclude that example."""
I['SA08-489']['reconstruction']="""The finite-projective and nonflat analyses extend earlier-run work; the flat proof is this run's reconstruction of a sufficient-hypothesis answer. The restricted uniqueness example is not a refutation of every possible quantifier reading. Literal Hom(A,M) ring targets and Hom(A,Gamma+M) inclusion remain reading questions."""
I['SA08-489']['check_reason']="""The notes preserve the open question, but the uniqueness conclusion needs the exact positive-index and fixed-object restriction. The finite-projective construction is correct, and the flat extension is proved in proofs.md §11. No manuscript quantifier is silently supplied."""

for n in [281,282,283]:
 C[f'SA08-C{n}']['fate']="""The primary Gressman lecture page was found through an indexed Dirichlet-test excerpt, but full-page access failed with403 and remains unverified. No theorem-read claim is based on that excerpt. This is elementary classical analysis; the exact statement and its limits are independently re-proved in proofs.md §13. The search trail and failed access are retained in L20."""

# A substantive assertion present in the transcription but not isolated by the
# source notes: add an item without inventing a source-entry id.
if 'SA08-523' not in I:
 x=dict(id='SA08-523',sources=[],kind='unproved claim',cote='136',scans=[262],lines='D1186-1204',his_words='Proposition 7.5. Soit S un trait complet',statement="""For a complete trait S and an abelian variety A_K with semistable reduction, the formal abelian quotient of the identity component of its Néron model algebraizes to a functorial abelian scheme A^ab over S. Divisorial correspondences induce unique correspondences on the abelian parts whose reductions pull back to the original biextensions.""",reconstruction='A full-transcription claim omitted as a separate heading in the notes; the exact published Proposition7.5 supplies the statement and hypotheses.',check='agrees',check_reason='Read the actual live donor statement D1186–1204 and the original SGA7IXp412/PDF417. No manuscript scan was available; the publication match is exact.')
 items.append(x); I[x['id']]=x
if 'SA08-C288' not in C:
 x=dict(id='SA08-C288',items=['SA08-523'],cote='136',scans=[262],lines='D1186-1204',his_statement='Proposition7.5: partie abélienne, dépendant fonctoriellement; correspondance divisorielle unique.',statement=I['SA08-523']['statement'],status_on_pages='published proposition reproduced; surrounding proof summarized on this leaf',computation='No numerical computation; exact source and hypotheses checked.',**{'class':'A'},fate='Exact match to Grothendieck, SGA7I ExposéIX Proposition7.5, publishedp412, originalPDF417. The preceding paragraph gives perfect duality over the specified dense open and extends the orthogonality formulas. This is a donor-text theorem, not a new claim of the PD exposition.',fate_date='SGA7 seminar1967–1969; publication1972; reused before/within live1975–1976 compilation.',present_status='As of2026-11-19: Established under the complete-trait and semistable-reduction hypotheses of Proposition7.5. No arbitrary-base generalization is inferred.',refs=['late_SGA7IX'],confidence='high',searches=['L16'],proof_check='Exact statement compared in the transcription and original published page; not an independent proof of Proposition7.5.',origin='Grothendieck donor transcription; claim identified from full-text reading',chronology_note='A records the donor-text-to-own-publication match; the publication predates the live PD work.')
 claims.append(x);C[x['id']]=x

for n in [222,286]:
 if 'Parent SA08/root' not in C[f'SA08-C{n}']['proof_check']:
  C[f'SA08-C{n}']['proof_check']+=' Parent SA08/root and SA08/early independently reviewed the exact-L argument on2026-11-19; see separate targeted-proof-check events. This verifies an existing manuscript assertion and earlier-run repair, not a claim of novelty.'

# Two explicit authorial warnings deserve claim rows even though they are not
# named theorems. Their existing note items already have adjudicated entries.
for x in [
 dict(id='SA08-C289',items=['SA08-476','SA08-473'],cote='136',scans=[306],lines='E955–973',his_statement='ce ne sont pas des invariants du type d’homotopie de X_*; catégories de fractions.',statement='Raw representable invariants of simplicial sets need not preserve homotopy equivalences. Adding operations and localizing the arrows induced by equivalences is a separate construction; the page does not assert a complete reconstruction theorem.',status_on_pages='explicit warning and proposed programme',computation='No numerical computation; explicit representable counterexample in proofs.md §14.',**{'class':'E'},fate='Dold–Kan and the ordinary Yoneda theorem give the exact elementary warning. Later Mandell2006, Ekedahl2002, Horel2024 and Toën2020 obtain distinct structured homotopy comparisons with explicit connectivity, nilpotence, finite-type and fullness restrictions. None proves that every unspecified category of fractions in this paragraph reconstructs homotopy types.',fate_date='Warning is standard background at the time; named later comparisons first circulated2001/2003/2019/2022 and were published2002/2006/2020/2024 respectively.',present_status='As of2026-11-19: Correct warning. If M=DK(Z[1]), maps from point to M are0, while maps from Delta1 to M form Z, though both source spaces are contractible. The localized structured target must still be specified.',refs=['late_Stacks019G','late_Kelly1982','late_Mandell2006','late_Ekedahl2002','late_Horel2024','late_Toen2020'],confidence='high',searches=['L10','L11','L12'],proof_check='proofs.md §14 independent representable example; exact later primary theorem envelopes checked, not identified with the manuscript category.',origin='Grothendieck transcription'),
 dict(id='SA08-C290',items=['SA08-478'],cote='136',scans=[311,312],lines='E1220–1238',his_statement='cette structure ... n’est pas reconstructible par la seule connaissance de C_.',statement='The bare additive chain invariant does not supply cup multiplication or the coherent diagonal operations of the original simplicial set. In particular chain-homotopy type alone cannot recover the integral cohomology ring.',status_on_pages='explicit structural warning',computation='No numerical computation; cohomology-ring comparison in proofs.md §14.',**{'class':'E'},fate='The loss of products under additive forgetting is standard. Richter2009 and Schwede–Shipley2003 specify monoidal comparison data; Mandell2006 requires integral E-infinity cochains, while Richter–Sagave2020 uses commutative diagram dgas. These do not identify a bare chain complex with those enriched inputs.',fate_date='Standard warning at the time; cited precise later structures published2003,2006,2009,2020, with first-circulation dates recorded in the bibliography.',present_status='As of2026-11-19: Correct at the homotopy-invariant level. CP² and S²∨S⁴ have chain-homotopy-equivalent free integral chain complexes but different cup squares. This example does not assert a canonical strict isomorphism of their original normalized simplicial chain functors.',refs=['late_Richter2009','late_SchwedeShipley2003','late_Mandell2006','late_RichterSagave2020'],confidence='high',searches=['L11','L12'],proof_check='proofs.md §14 independent ring/chain comparison; canonical strict isomorphism not claimed.',origin='Grothendieck transcription')]:
 if x['id'] not in C:claims.append(x);C[x['id']]=x

# Preserve the source-entry verdicts while updating the scope of the uniqueness
# reasoning for every merged source that points at the corrected item.
with (P/'entries.tsv').open() as f:
 r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; entries=list(r)
for e in entries:
 if e['item_id']=='SA08-489':
  e['verdict']='corrected'
  e['reason']=I['SA08-489']['check_reason']
 if e['item_id']=='SA08-405':
  e['reason']='Kept as a warning against dropping the graded-free hypothesis, with the doubtful object name left unresolved as the note requires. The manuscript’s all-weight nonflasqueness assertion is not certified: the quadratic normalization is acyclic over Q. This run retracts its own earlier ordinary-K interpretation, not the note’s cautious handling of the ink.'
with (P/'entries.tsv').open('w') as f:
 w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(entries)
for fn,rows in [('items.json',items),('claims.json',claims)]:
 (P/fn).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

refs=json.loads((P/'reference_verification.json').read_text())
new_refs=[
 dict(key='late_BMT2016',type='article',author='Breen, Lawrence and Mikhailov, Roman and Touzé, Antoine',title='Derived functors of the divided power functors',year='2016',journal='Geometry & Topology',volume='20',number='1',pages='257--352',doi='10.2140/gt.2016.20.257',url='https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf',note='verified',eprint='1312.5676',verification_scope='Published primary PDF opened; Proposition3.5 and Corollary3.6p270 read, including projective/field and rational odd-shift hypotheses. arXiv metadata first19Dec2013, revision21Feb2014; published29Feb2016. Author bibliography also opened. Used to distinguish Gamma²(Psi) from an ordinary Eilenberg–Mac Lane object, with independent exact matrix proof.'),
 dict(key='late_Touze2026',type='misc',author='Touzé, Antoine',title='The universal property of strict polynomial functors',year='2026',url='https://arxiv.org/pdf/2607.00631',eprint='2607.00631',note='verified',verification_scope='Primary preprint introductionpp1–5 and its theorem statements read: Proposition1,Example2,Lemma3,Definition4,Theorems5,9,Remark11. Ground field; exact strong symmetric tensor functors and tensor-abelian targets with prescribed admissibility. First arXiv1Jul2026, PDF datedJune2026. No separate publication or full-proof check claimed; bounded contemporary comparison only.')]
for r in new_refs:
 if r['key'] not in {s['key'] for s in refs}:refs.append(r)
for n in [249,250,259]:
 c=C[f'SA08-C{n}']
 if 'late_Touze2026' not in c['refs']:
  c['refs'].append('late_Touze2026')
  c['fate']+=' Contemporary bounded comparison: Touzé2026 Lemma3 and Theorem5 give uniqueness/existence of exact strong tensor functors from strict polynomial functors over a field to admissible tensor abelian categories (in particular those modeled on vector spaces). Theorem9 supplies closure properties. Those hypotheses do not identify this manuscript’s arbitrary-ring operation category or its lax convolution functor.'
for r in refs:
 if r['key']=='late_LevinTate':
  r['year']='n.d.'
  r['verification_scope']='Author seminar notes opened; Theorem1.2p3 and its reduction read. Integrally closed Noetherian domain, fraction field characteristic0. No independently checked first-circulation or publication date is asserted.'
 if r['key']=='late_Stacks09PF':
  r['verification_scope']='Definition23.6.5 and the warning immediately after it, retrieved lines74–75, explicitly distinguish differential compatibility from boundary descent. Lemma23.6.6 gives a sufficient descent case. No reliance on the coefficient-free iteration formula printed in Example23.6.3.'
(P/'reference_verification.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
out=[]
for r in refs:
 fields={k:v for k,v in r.items() if k not in ['key','type']}
 out.append('@'+r['type']+'{'+r['key']+',\n'+',\n'.join('  '+k+' = {'+str(v).replace('\n',' ')+'}' for k,v in fields.items())+'\n}\n')
(P/'references.bib').write_text('\n'.join(out))
# Re-save after the contemporary comparison additions above.
(P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
problems=json.loads((P/'problems.json').read_text())
for p in problems:
 if p['id']=='MP-SA08-60' and 'degenerate Gamma²(Psi)' not in p['state_of_art']:
  p['state_of_art']+=' The degenerate Gamma²(Psi) calculation is k --2→ k, so the doubtful Pi/K object and all-weight nonflasqueness cannot be used as an ordinary K(k,2) statement; BMT2016p270 gives the derived nonlinear context.'
  p['refs'].append('late_BMT2016')
 if p['id'] in ['MP-SA08-75','MP-SA08-78'] and 'Touzé2026' not in p['state_of_art']:
  p['state_of_art']+=' Touzé2026Lemma3/Th5/Th9 is a precise new comparison for exact strong tensor functors over a field and admissible tensor abelian categories. It does not settle the unspecified integral/lax target of these leaves.'
  p['refs'].append('late_Touze2026')
 p['refs']=list(dict.fromkeys(p['refs']))
(P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
with (P/'readings.tsv').open() as f:
 rr=csv.DictReader(f,delimiter='\t');rfields=rr.fieldnames;readings=list(rr)
if not any('quadratic normalization' in r.get('evidence','') for r in readings):
 readings.append(dict(zip(rfields,['136','239','sources/texts/pro/MPL_136_235-281_transcription.tex:162–170','Gamma^p(Psi_*) then unsure Pi_*|K_*(k,p); nonflasque for every p','Preserve the uncertain name; do not substitute ordinary Eilenberg–Mac Lane K(k,p); check the all-p and coefficient hypotheses.','Exact quadratic normalization gives k --2→ k in degrees2→1. OverZ this has H1=Z/2; overQ it is acyclic. BMT2016Prop3.5/Cor3.6p270 gives the corresponding derived context. No ink decision.','essential','high mathematical alarm; ink undecided'])))
with (P/'readings.tsv').open('w') as f:
 w=csv.DictWriter(f,rfields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(readings)
print(json.dumps({'items':len(items),'entries':len(entries),'claims':len(claims),'references':len(refs),'added_full_text_claim':'SA08-C288'},indent=2))

# Finalization must retain the later manually selected literal quotations and
# their corrected provenance in every problem occurrence.
import runpy
runpy.run_path(str(P.parent.parent/'programs/late_quote_audit.py'),run_name='__main__')
