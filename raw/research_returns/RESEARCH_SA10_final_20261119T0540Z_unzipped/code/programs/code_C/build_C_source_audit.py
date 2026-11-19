#!/usr/bin/env python3
"""Record the exact inherited statements actually used, with their audit outcome.
This only writes source-audit metadata and check-event additions, never TeX.
"""
from pathlib import Path
import csv, re, json
W=Path(__file__).resolve().parents[1]
R=W.parent/'sources/RESEARCH_SA10_study/study/readings'
records={}
for p in R.glob('150_*_CHECK_EVENTS.tsv'):
 with p.open(newline='') as f:
  for line,row in enumerate(csv.DictReader(f,delimiter='\t'),2):
   records[row['id']]=(p,line,row.get('result',''),row.get('where',''))
for p in R.glob('150_*_CORRECTIONS.tsv'):
 with p.open(newline='') as f:
  rd=csv.DictReader(f,delimiter='\t')
  for line,row in enumerate(rd,2):
   vals=list(row.values());ident=vals[0]
   records[ident]=(p,line,' | '.join(vals[4:6]),vals[2])
checks=[]
def add(ids,status,new,detail):
 for ident in ids.split():
  p,line,old,where=records[ident]
  checks.append(dict(prior_id=ident,source_path=str(p.relative_to(W.parent)),source_line=line,manuscript_locator=where,current_status=status,new_statements=new,correction_or_confirmation=detail,prior_claim=old))
add('SA10-R150b-11','Used part re-proved','C1.03;C2.05','The cone quotient and collar-absorption reconstruction used here are proved by explicit quotient maps. No broader untyped category of all continuous maps is inferred.')
add('SA10-R150b-21','Qualified and completed','C3.01;C3.04','The local cubical product is correct. It is a manifold with the specified corners exactly when its transverse open-face base is a manifold in the chosen category; the Cantor product refutes an unconditional manifold conclusion.')
add('SA10-R150c-14 SA10-R150c-16','Used and re-proved','C1.03;C3.04','For the actual finite recursive data, retained old and new boundary collars are part of /036(22). Their product compatibility gives the induction and topological reconstruction without source fibrancy. Original /036 visually checked.')
add('SA10-R150c-19','Confirmed with incidence qualification','C1.04;C3.02-C3.04','A global stratum orbit-poset can forget local branches and self-incidences. The moduli statement uses fixed incidence chains and full automorphism groupoids; manifoldness of the coarse space is a separate issue.')
add('SA10-R150c-20 SA10-R150c-21','Confirmed under typed fibrancy','C1.01-C1.02;C1.04','Nonfinal flag deletions are the collared face embeddings. Initial-segment maps are composites of base changes of the assumed source fibrations; weak mapping-cone data do not imply those fibrations.')
add('SA10-R150c-23 SA10-K150c-15','Confirmed by explicit example','C1.04','For Mbar_0,4 use three point objects, a sphere with three open discs removed, and three boundary circles. The cylinders fill the three discs and recover S2. Literal open strata or boundary-circle point objects are different conventions.')
add('SA10-R150c-30','Confirmed with exact finite certificate','C3.02','The interval of flags with fixed final vertex is Boolean. Exhaustive naturally-labelled posets of sizes0..5 give4135 flags and10603 tested intervals; the subset proof covers every finite size.')
add('SA10-R150c-31 SA10-R150c-32 SA10-K150c-14','Confirmed and strengthened','C1.02;C1.B1-C1.B3','Strict Segal reconstruction is valid with only identity arrows over identical grades. Hurewicz source fibrations make the pullbacks homotopy pullbacks. Raw Reedy fibrancy is not automatic; geometric Exit identification requires the separate collage proof.')
add('SA10-R150c-37 SA10-R150c-41 SA10-K150c-12','Confirmed original slip; construction completed','C1.03','Original /043 genuinely writes p=long d-prime. The selected-prefix count is p=cardinality(d). The full colimit needs three transition families, including initial-prefix identifications; the two-point counterexample and cell-quotient program verify their necessity.')
add('SA10-R150e-16 SA10-R150e-17 SA10-K150e-02','Confirmed with textual qualification','C2.01-C2.02','The twist counterexample is valid for bare a)-c), and a compact smooth enhancement verifies the other geometric clauses. However /065 already calls its hexagon commutative: if that is included as an axiom, pi-control is written. The invalid inference is that commutativity follows from the bare subset identities.')
add('SA10-R150e-34 SA10-K150e-01','Confirmed typed correction','C2.01-C2.02','The inverse image must be s_jk^{-1}(Sigma_ij) inside Sigma_jk. The written b_ij^{-1} has the wrong ambient space.')
add('SA10-R150d-23 SA10-K150d-08 SA10-R150e-21 SA10-K150e-08','Confirmed and strengthened','C5.04-C5.05','TOP face-manifold deduction is false, now with compact F times square and every source proper Hurewicz. PL/smooth collar cancellation and the full boundary formula hold in those categories.')
add('SA10-R150d-25 SA10-K150d-09 SA10-R150e-14 SA10-K150e-07','TOP part confirmed; unconditional PL/smooth extension refuted','C5.03;C5.05-C5.06','TOP fails even for a genuine locally trivial bundle. Proper PL and smooth maps that are Hurewicz fibrations can also have a nonmanifold fibre, by the boundary-spin/Ferry construction. Positive PL-bundle and full smooth-source-system statements are proved with their exact regularity assumptions.')
add('SA10-R150e-10 SA10-K150e-09','Bare independence confirmed; fibrant/local-trivial conflation corrected','C5.02;C5.05;C5.08','The bare other axioms do not imply collar transversality. Local product triviality of the full face diagram suffices. Merely smooth proper Hurewicz sources do not suffice: the compact u-to-u-squared example is a homeomorphism on each source component but has zero normal derivative.')
add('SA10-K150e-05','Source reading used; alternative treated explicitly','C5.08','The source letter is consistent with /062 p1 and /065-066. If the doubtful alternative b is read literally, product-collar transversality of a nonempty target boundary embedding to itself is impossible, rather than an automatic condition; the strict-arrow case then becomes empty.')
add('SA10-R150e-23 SA10-K150e-11','Confirmed for path components; connected scope qualified','C5.01;C5.07-C5.08','Path lifting gives the pullback surjection on path components. The unrestricted statement for connected components is false; the collared pseudoarc-ray counter satisfies the stated TOP hypotheses. Locally path-connected cases and the open proper-source alternative are proved.')
add('SA10-R150e-26 SA10-K150e-12 SA10-R150f-02 SA10-K150f-13','Unrestricted TOP conclusion refuted; stronger corrections proved','C5.01;C5.07-C5.08','Finite connected dimension alone is insufficient: a compact finite-dimensional connected ray compactification has a strict internal arrow with proper Hurewicz source and collared target. For ordered spaces with open path-connected components no dimension assumption is needed. General-category manifold and PL proofs use local sections and invariance of domain, without assuming local triviality.')
add('SA10-R150e-27 SA10-R150e-28 SA10-R150e-29 SA10-K150e-17 SA10-R150e-30','Conditional proof confirmed; unrestricted scope refuted','C5.01;C5.07-C5.08','Once no strict arrow remains inside a component, the component partial order, redundant monomorphism condition, and incomparable incoming-face disjointness follow. C5.01 proves that premise for the stated path-connected scope; C5.07 refutes it for arbitrary connected TOP components.')
add('SA10-R150e-32 SA10-R150e-33','Used and re-proved with completion qualification','C1.02-C1.04;C1.B1-C1.B3','The two-stratum realization is the mapping-cylinder gluing. Complete-Segal/Exit comparison is now proved under proper recursive conical collars. Mapping spaces are homotopy fibres of (s,b); a geometric outgoing link retains its variable target and is not automatically the mapping space to one fixed point in a noncontractible target stratum.')
add('SA10-R150f-13 SA10-R150f-16 SA10-R150f-19 SA10-R150f-29','Strengthened; Mather control not necessary for these pro comparisons','C4.01','For finite metric HSS, one fixed Quinn nearly strict stratum-preserving deformation and cofinal shrinking prove (51),(56),(57),(69) as compatible pro-homotopy equivalences. Independent retractions at separate levels would not suffice. Domination remains required.')
add('SA10-R150f-30','Confirmed failure without domination','C4.01-C4.02','For a reversed incident pair, V_J^L is empty while the overlapping tube germ is nonempty; the domination condition is retained. Strict-holink language separately requires disjoint bands; overlap uses the all-paths relative model.')
add('SA10-R150f-28 SA10-R150f-33 SA10-R150f-34','Confirmed with actual sheaf cover and finite scope','C4.03','Choose upper-band neighbourhoods inside the open upper union, so the covering equality is stagewise exact. The finite flag-poset/flabby double complex proves (73); no homotopy invariance of arbitrary coefficient sheaves is used.')
add('SA10-R150f-35 SA10-K150f-14','Confirmed against original scans','C4.06','Str_inf is cote147. Original147/173-177, including(286)-(294), were opened visually. The quotient puncture removes every coordinate hyperplane, not only the zero section.')
add('SA10-R150f-36','Confirmed with a repaired cofinality argument','C4.05','Actual compatible proper conical tubes give cofinal triangular variable-radius regions, not fixed rectangles over the deepest face. Their natural projection and the inward-face homotopy yield V_d equivalent to Sigma_d. HSS alone need not provide an actual deployed collar model.')
fields=['prior_id','source_path','source_line','manuscript_locator','current_status','new_statements','correction_or_confirmation','prior_claim']
with (W/'C_inherited_audit.tsv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(checks)
text=['# Audit of inherited cote 150 claims','', 'This records actual checks made in this run, not inherited authority. Source paths and line numbers refer to the supplied, once-unpacked study. Exact primary-source locators and opened status are in C_source_manifest.tsv. The TeX contribution is frozen; this file changes only the research record.','', '## Main corrections','',
'- Bare a)-c) do not imply pi-control; the original hexagon is nevertheless explicitly called commutative. One radius level records less than a whole radial control germ.',
'- The raw topological nerve needs a complete-Segal interpretation and, where necessary, Reedy/Rezk replacement. The Exit comparison is a separate coherent collage theorem. Moduli require whole incidence-chain groupoids, including ineffective stabilizers.',
'- The literal finite recursive section8 data already retain transverse old/new collars, so the cutting gives precylindricity. Manifoldness is a further local criterion. Ordinary coarse moduli can fail it in the interior.',
'- Proper Hurewicz fibrancy is weaker than PL bundle or smooth regular source data. The PL and smooth mixed-manifold assertions are false for raw fibrancy. The proper smooth u-to-u-squared source also refutes automatic smooth collar transversality.',
'- Finite-dimensional connected TOP components do not suffice for the component-order conclusion. The full collared ray/pseudoarc counterexample satisfies the geometric hypotheses. Open path-connected components, or open proper sources, give corrected statements.',
'- Finite metric HSS suffice for the pro-neighbourhood comparisons; full Mather radial control is not necessary there. For V_d versus an actual face, cofinal radii must vary recursively, producing horn regions. Arbitrary sheaf cohomology uses an exact cover, not a homotopy replacement.','',
'## Exact inherited-ID table','', '| Prior ID | Supplied source and line | Current result | New proof |','|---|---|---|---|']
for r in checks:
 text.append(f"| {r['prior_id']} | {r['source_path']}:{r['source_line']} | {r['current_status']} | {r['new_statements']} |")
text += ['', '## Detailed dispositions','']
for r in checks:
 text += [f"### {r['prior_id']}",'',r['correction_or_confirmation'],'']
text += ['## Scope boundary','', 'No divisibility or dense-order assumption from the separate SA21 material is imported. Nonfaithful gradings retain component incidences; ineffective orbifold actions retain their full stabilizers. Empty labels, disconnected strata, rank-zero normal quotients, and empty diagrams are treated explicitly. The finite manuscript scope is not silently extended to arbitrary non-locally-finite families.','']
(W/'C_source_corrections.md').write_text('\n'.join(text))
p=W/'CHECK_EVENTS_C.tsv'
with p.open(newline='') as f:events=list(csv.DictReader(f,delimiter='\t'))
for e in events:
 if e['statement_id'].startswith('RECHECK-SA10-'):
  e['statement_id']=e['statement_id'].removeprefix('RECHECK-')
seen={(e['statement_id'],e['type']) for e in events}
for r in checks:
 ident=r['prior_id']
 event_key=(ident,'used and rechecked in this run')
 if event_key not in seen:
  events.append(dict(statement_id=ident,date='2026-11-19',who='GPT-6 Astra (OpenAI); effort not separately exposed; ChatGPT Pro; /root/cote150',type='used and rechecked in this run',outcome=r['current_status']+'. '+r['correction_or_confirmation']+' Source '+r['source_path']+':'+str(r['source_line'])+'; proof '+r['new_statements']))
  seen.add(event_key)
with p.open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');wr.writeheader();wr.writerows(events)
out={'inherited_records_checked':len(checks),'check_events_total':len(events),'outputs':['C_inherited_audit.tsv','C_source_corrections.md','CHECK_EVENTS_C.tsv']}
(W/'code_C/build_C_source_audit.out').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
