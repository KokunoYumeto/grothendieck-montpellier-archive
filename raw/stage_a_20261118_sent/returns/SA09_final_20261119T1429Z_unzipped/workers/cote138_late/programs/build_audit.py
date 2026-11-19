"""Serialize manually assessed search scopes and check events; no semantic classification."""
import csv, json, re
from pathlib import Path

B=Path(__file__).resolve().parents[1]
C=json.loads((B/'claims.json').read_text())
I=json.loads((B/'items.json').read_text())
groups=json.loads((B/'claim_search_groups.json').read_text())
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; effort inherited from parent and not separately exposed; run /root/cote138_late'

# These assignments were made after reading the claims, searches and opened passages.
S={
'G01':(['web_search_02.json','web_search_03.json','web_primary_04.json','web_primary_05.json'], 'Named punctures, ordinary punctures rather than parametrized boundary, extended versus oriented pure group, and the central C2 sphere-braid quotient.'),
'G02':(['web_search_02.json','web_search_03.json','web_primary_01.json','web_primary_04.json','web_primary_05.json','web_primary_10.json'], 'Injection of the full profinite completion into the congruence closure for genus zero, including the inner/point-pushing passage; not merely injectivity of the discrete group.'),
'G03':(['web_search_02.json','web_search_03.json','web_primary_11.json','web_primary_14.json','web_primary_17.json','web_primary_18.json'], 'Normality in the exact pure peripheral ambient group, versus normality in its common-character kernel; all ranks nu>=2 and compatible puncture forgetting. Current tower/GT results have additional hypotheses.'),
'G04':(['web_remaining_08.json','web_remaining_13.json','web_primary_10.json'], 'Sphere-orbifold cone relations with finite positive orders; infinity means a missing relation, not a literal infinite exponent.'),
'G05':(['web_remaining_08.json','web_remaining_10.json','web_primary_08.json','web_primary_09.json','web_primary_10.json'], 'Contracted products, embedding torsors, canonical outer versus chosen actual actions, same cyclotomic exponent at every rational puncture, and orbit sizes versus the bare inertia orbit set.'),
'G06':(['web_search_05.json','web_search_06.json','web_remaining_10.json','web_primary_12.json','web_primary_14.json'], 'The literal fibre-cardinality morphism law, all genera, pinning cells rather than flags, raw automorphisms versus their effective action, and isomorphism classes rather than labelings.'),
'G07':(['web_remaining_09.json','web_primary_08.json','web_primary_12.json'], 'Common dartdegree of all three fibre partitions; folded edges count one. An isolated 6N does not specify a monodromy order.'),
'G08':(['web_search_05.json','web_primary_14.json','web_remaining_08.json','web_remaining_10.json','web_primary_05.json','web_primary_06.json','web_primary_10.json'], 'Raw rational isomorphism-class presheaf versus finite geometric Galois-set scheme; tame specialization at primes p>degree; label pinning must eliminate actual descent obstructions.'),
'G09':(['web_search_05.json','web_search_06.json','web_primary_01.json','web_primary_08.json','web_primary_09.json','web_primary_10.json','web_primary_12.json','web_primary_14.json','web_primary_15.json'], 'Finite geometric classes, faithful transitive monodromy with core-free stabilizer, fixed branch target, continuity and relabeling commutation; no full faithfulness conclusion from a small orbit.'),
'G10':(['web_remaining_09.json','web_primary_14.json','web_primary_08.json','web_primary_13.json','web_primary_15.json','web_primary_17.json'], 'Exact normalized rational functions and passports in degrees 1-3; folded white points allowed; cubic-star pinned classes and cyclotomic action.'),
'G11':(['web_search_04.json','web_search_07.json','web_primary_06.json','web_primary_07.json','web_primary_12.json','web_primary_13.json','web_primary_14.json','web_primary_15.json','web_primary_16.json','web_primary_17.json','web_primary_18.json','web_primary_19.json','web_remaining_14.json'], 'The exact sextic z^3(z-1)^2(z-c), cubic 25c^3-12c^2-24c-16, discriminant collision, nondegeneracy, arithmetic S3 versus geometric S6, with backward reference tracing to 1992/1993.'),
'G12':(['web_search_04.json','web_primary_13.json','web_primary_15.json','web_primary_17.json'], 'Coprime numerator and denominator with distinct disjoint root supports, degree numerator greater than denominator, and residual critical polynomial after cancellation.'),
'G13':(['web_remaining_09.json','web_remaining_11.json','web_remaining_12.json','web_remaining_13.json','web_remaining_14.json','web_primary_08.json','web_primary_12.json','web_primary_14.json'], 'Finite connected genus-zero permutation maps with folded edges and degree at most six; full versus oriented symmetry; exact passport/drawing identification and D4 convention remain conditions.'),
'G14':(['web_search_06.json','web_remaining_01.json','web_remaining_10.json','web_primary_01.json','web_primary_02.json','web_primary_13.json','web_primary_14.json'], 'Functorial isotopy quotient, descent as a hypothesis, variance of compatible global sections, completed denominator, and universal subset operations versus rational postcomposition.'),
'G15':(['web_search_06.json','web_primary_13.json','web_remaining_01.json','web_primary_08.json','web_primary_09.json','web_primary_10.json'], 'Finite graph and union graphness; every connected finite cover branched in {0,1,infinity}; at most one branch value in each complementary face, not in the graph itself.'),
'G16':(['web_search_06.json','web_primary_14.json','web_remaining_01.json','web_remaining_09.json','web_primary_01.json','web_primary_02.json','web_primary_06.json','web_primary_10.json'], 'Composition order, exact multiplicative local indices, strict clean index two versus folded-edge index at most two, exceptional old white endpoint, and rationality for arithmetic equivariance.'),
'G17':(['web_search_02.json','web_search_03.json','web_search_07.json','web_primary_11.json','web_remaining_01.json','web_remaining_02.json','web_remaining_03.json','web_primary_01.json','web_primary_02.json'], 'Finite-order map-isotopy kernel for finite cellular maps; invariant rigidification and contractibility only after specifying the space and topology. A colored-dessin realization theorem does not supply these missing definitions.'),
'G18':(['web_search_06.json','web_remaining_01.json','web_remaining_02.json','web_remaining_03.json','web_remaining_04.json','web_primary_12.json','web_primary_14.json','web_remaining_14.json'], 'Literal equality of functions on a fixed Riemann surface and same unmarked map, versus isomorphism of fully colored Belyi pairs; all orange orders and cell versus flag isotopy.'),
'G19':(['web_search_06.json','web_remaining_01.json','web_remaining_02.json','web_remaining_03.json','web_remaining_04.json','web_remaining_05.json','web_remaining_06.json','web_remaining_07.json','web_primary_15.json'], 'Finite face boundary prime ends and finite-sided discs, marked centres/midpoints, and the unrestricted infinite-map question versus locally finite tame infinite dessins.'),
'G20':(['web_search_06.json','web_remaining_01.json','web_primary_01.json','web_primary_02.json','web_primary_06.json','web_primary_10.json'], 'Six separate holomorphic operation conditions; no assertion that all are equivalent. Universal strict-clean postcomposition compared against Wood Proposition 2, which only preserves the Belyi property.'),
'G21':(['web_search_04.json','web_search_05.json','web_search_06.json','web_primary_13.json','web_primary_14.json','web_primary_16.json','web_primary_17.json','web_primary_18.json','web_primary_19.json'], 'Finite orbit computations and specified operation invariants, not classification of every Galois orbit or every natural operation.'),
'G22':(['web_remaining_09.json','web_primary_13.json','web_primary_17.json'], 'Unidentified isolated phi(n) notation; critical points with values zero or one, not zero alone. No notation supplied from a title match.')}

L={
'SGA1':'Exposé XII, Theorem 5.1; Exposé XIII, Corollary 2.9, construction 2.10, Lemma 2.11, Corollary 2.12; Exposé V carried as Galois-category background.',
'Belyi1980':'Theorem 4, p.255, and corollary, p.256; official receipt date 2 August 1978.',
'McReynolds2012':'Theorem 1.1, p.926, and introduction historical attribution; proof source opened, earlier original papers not independently opened.',
'Kent2014':'Author manuscript dated 14 February 2014, §4, Theorem 7, closure and Birman exact sequence.',
'LochakCurves':'Author manuscript p.31, pure sphere braid group modulo central C2; date not established.',
'Collas2026':'Version 2, 5 November 2026, §§2.2 and 3; §4.2, Definition 4.3 and Theorem 4.5. COF/RGC and tower compatibility retained.',
'Oesterle2003':'Bourbaki exposé 907, §§1.1–1.4, 2.3–2.5 and Theorem 2; outer action, local inertia and comparison.',
'Stacks03QR':'Tag 03QR, Lemma 58.2.2, statement and proof: étale schemes over a field and continuous Galois sets.',
'Stacks03SF':'Tag 03SF, §58.7: finite Galois covers and normal open subgroups.',
'GuillotDessins':'Opened author PDF: Theorems 1.14, 1.21, 1.23; Proposition 1.24; Theorem 2.8 and Example 2.9. Publisher chronology checked separately.',
'Zvonkin2004':'§§2.1–2.2, pp.60–64, permutation and surface dictionary; §3.2, Example 3, pp.71–72, exact sextic example.',
'BPZ1992':'Author-hosted catalogue introduction, six-edge page and procedure page; exact (3,2,1)|(2,2,1,1)|(6) row has three conjugates. Formula images not rendered.',
'BetremaZvonkin1993':'§3.1, Proposition 1; §3.3 derivative algorithm; §4.3, pp.607–608, exact sextic, cubic and S3 orbit. Introduction reports spring 1992 catalogue.',
'LandoZvonkin2004':'§2.2.2.3, pp.92–94, full-book text mirror plus publisher metadata; exact sextic and parasitic collision factor. Hardcover release 1 December 2003, copyright 2004.',
'Jones2013':'Example 7.7, p.12: exact cubic, three oriented trees, S6 monodromy and S3 arithmetic orbit; first arXiv circulation 20 September 2013.',
'GirondoGonzalezDiez2011':'Publisher metadata opened; Example 4.58 reported by Jones but its text was not opened. Bibliographic lead only.',
'Ellenberg2002':'Author PDF dated 8 September 2000, §3, pp.4–6: cleaning and rational branch-preserving postcomposition; published 2002.',
'Wood2006':'Definition and Proposition 2, §3.1; combinatorial construction §§3.2–3.3; Proposition 4 (specific degree-ten separation). First arXiv 30 April 2003; publication 30 September 2006.',
'ConstantinKolev1994':'Theorem 3.1 and Proposition 3.2 with proof, pp.2–3 of arXiv version: periodic disc homeomorphism fixing boundary. Original 1994; deposit 2003.',
'Esquisse1984':'§§2–4, especially printed pp.9–10 and 15–20: arithmetic image, finite dictionary, regular covers, finite/infinite cartography. Circulation 1984, publication 1997.',
'Morvan2017':'Definition 6, §9.1, p.24; Definition 8 and Proposition 8, §11, pp.31–32: fully colored finite dessins. First circulation 28 June 2017, v2 22 September 2017.',
'CanasEtAl2022':'§§1, 2.1–2.3 and Theorem 2: finite vertex degrees, finite-sided disc faces, locally finite branched covers and tame countable group actions; 1 August 2022.',
'AdrianovEtAl2007':'§5.4, Figure 6, p.11 (oriented V4 digon); §§6.1–6.2, Figures 8–9, p.13 (oriented C3 and C2 bouquets). First arXiv 14 October 2007; journal 2009.',
'Fulton1969':'Publisher record and DOI landing page only: Annals of Mathematics 90(3),542–575. Full theorem not inspected; bibliographic lead only.'}

def query_strings(files):
 out=[]
 for name in files:
  d=json.loads((B/'outputs'/name).read_text())
  args=d.get('args',{})
  for engine in ['system1_search_query','system2_search_query']:
   for q in args.get(engine,[]) or []:
    text=f"{engine}: {q['q']}"
    if text not in out:out.append(text)
 return ' || '.join(out) or 'Opened exact primary passages listed in the raw result files; no invented query.'

with (B/'search_log.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['claim_id','date_utc','search_group','query_log_files','queries','exact_scope','opened_results','outcome','limitations'],delimiter='\t');w.writeheader()
 for c in C:
  g=groups[c['id']];files,scope=S[g]
  w.writerow(dict(claim_id=c['id'],date_utc=DATE,search_group=g,query_log_files='; '.join('outputs/'+x for x in files),queries=query_strings(files),exact_scope=scope+' Exact claim: '+c['statement'],opened_results=' || '.join(r+': '+L[r] for r in c['refs']),outcome=c['fate'],limitations='A negative search is bounded by the logged queries and opened results, not proof of universal absence. The matched scope above is part of the conclusion. '+('Metadata-only Girondo reference is not mathematical support. ' if 'GirondoGonzalezDiez2011' in c['refs'] else '')+('Undefined notation or topology remains unidentified; no ink decision.' if c['class']=='F' else '')))

# Actual proof/computation work, manually classified by claim.
computations=set(list(range(18,20))+list(range(28,47))+[48,49,50,51,52,53,65,66,72,77,78,81])
reproofs={1,2,4,6,7,8,10,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,36,47,54,55,58,59,60,61,62,63,66,67,68,69,70,71,72,73,76,82}
refutations={4,6,13,15,16,17,19,20,22,25,31,41,43,66,67,69,70,72,76,81}
proof_section={**{n:1 for n in [1,2,3,7]},**{n:2 for n in [4,5,6]},**{n:3 for n in range(8,15)},**{n:4 for n in [15,16,17,18,19,22,23,24,25,48,51]},**{n:5 for n in [20,21,26,27]},**{n:6 for n in range(28,48)},**{n:7 for n in [49,50,52,53,77,78]},**{n:8 for n in range(54,62)},**{n:9 for n in [62,65,66,76,82]},**{n:10 for n in [63,64]},**{n:11 for n in range(67,75)},75:12,79:12,80:7,81:6}
events=[]
def event(s,t,o):events.append(dict(statement_id=s,date=DATE,**{'who(model,effort,run)':WHO},type=t,outcome=o))
for i in I:
 event(i['id'],'used and rechecked in this run','Full source entry/entries read and compared with their original transcription passages; source-fidelity judgment '+i['check']+': '+i['check_reason']+' This event is a textual comparison, not a mathematical proof check. Source entries: '+', '.join(i['sources']))
for c in C:
 n=int(c['id'].rsplit('-',1)[1]);loc=f"proofs.md §{proof_section[n]}"
 event(c['id'],'used and rechecked in this run','Full cited source passage read; status distinguished from uncertain transcription and earlier-run ideas. Literature fate searched with exact-scope comparison: search_log.tsv, '+groups[c['id']]+'. '+c['status_on_pages'])
 if n in computations:event(c['id'],'computation or formal certificate',c['computation']+' Output files and executable programs retained; '+loc+'. This certifies the stated algebra/permutations, not an uncertain drawing or ink reading.')
 if n in reproofs:event(c['id'],'independent re-proof',loc+' supplies the stated proof or conditional reconstruction with hypotheses. '+('The proof reconstructs only the specified conditional statement, not the damaged original fragment. ' if c['class']=='F' else '')+c['present_status'])
 if n in refutations:event(c['id'],'refuted, with refined statement id','Literal assertion or proposed affirmative answer is refuted under the explicit hypotheses in '+loc+'. Refined statement id: '+c['id']+' (its statement field contains the corrected formulation or counterexample). No transcription was changed.')
 if n==3:event(c['id'],'carried as background without fault found','McReynolds Theorem 1.1 and Kent Theorem 7 were opened and their hypotheses checked; the full congruence theorem was not independently re-proved here.')
 if n==21:event(c['id'],'targeted proof check','Checked the use of SGA1 XIII 2.9–2.11: group order divides degree factorial, so p>degree makes it invertible. Only finite geometric-class variation is concluded, not the raw functor.')
 if n in [56,57,64,74,75,80]:event(c['id'],'carried as background without fault found','The nearby established framework is used only with the limits recorded in the statement and fate fields. The incomplete or undefined manuscript assertion is not certified.')
for r in L:
 if r in ['GirondoGonzalezDiez2011','Fulton1969']:
  event(r,'carried as background without fault found','Publisher record opened and publication metadata checked. The exact mathematical passage was not opened and is not used as independently verified mathematical evidence. '+L[r])
 else:
  event(r,'used and rechecked in this run','Primary result/edition opened and compared with the relevant claim hypotheses: '+L[r]+' Reading and scope checking only unless a separate proof event follows.')
 if r in ['Stacks03QR','Stacks03SF','ConstantinKolev1994']:
  event(r,'targeted proof check','Read the indicated proof/argument and checked its use in the dossier. '+L[r]+' No claim of a new proof of the entire reference.')
with (B/'CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who(model,effort,run)','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

with (B/'search_coverage.md').open('w') as f:
 f.write('# Search coverage and limits\n\nEvery one of the 82 late-package claims has its own row in `search_log.tsv`. Claims with the same precise dependency share searches, but each row retains its own formulation, matched results and bounded outcome. Raw requests and responses are retained in `outputs/web_*.json`; some early result-only captures have no saved request object and are never assigned invented query strings.\n\n')
 f.write('## Channels actually used\n\nSearches used both available web engines, arXiv full texts and records, Numdam, primary author pages, SGA 1, Grothendieck’s Esquisse, publisher records, bibliographies and backward references. MathOverflow was searched and opened for context, not substituted for primary theorem evidence. zbMATH Open was searched by site queries and direct title-query URL; direct access failed and did not supply an exact usable mathematical result. EGA/SGA and finite-étale-moduli searches led to the opened SGA 1 and Stacks results; no EGA theorem with the literal raw pinned-functor hypotheses was identified, and unverified modern translation hits were not used.\n\n')
 f.write('## Access limitations\n\nAsada’s original article and the Diaz–Donagi–Harbater original were not successfully opened. Their historical priority is explicitly reported from McReynolds’s primary reproof. Girondo–González-Diez Example 4.58 was not opened; only its publisher record was checked. The 1992 catalogue’s formula GIFs could not be rendered; the exact 1993 PDF calculation was opened instead. The Lando–Zvonkin exact book section was read in a full-text mirror, with publisher record and author errata checked. No missing project context file is treated as an opened result.\n\n')
 f.write('## Backward chronology\n\nThe exact sextic first appeared in the located material in the spring-1992 catalogue (as dated by the authors in 1993), then in Bétréma–Zvonkin (1993), §4.3, pp.607–608. The 2003/2004 book and Jones’s 2013 example are later confirmations, not assigned priority. Ellenberg’s source circulated in 2000 and was published in 2002; Wood’s circulated in 2003 and was published in 2006. Guillot’s first arXiv circulation was 2013, its journal volume is 2014, and its actual release was 2015. The Adrianov et al. catalogue circulated in 2007 and appeared in a journal in 2009.\n\n')
 f.write('## Meaning of a negative outcome\n\n“No exact result located” refers only to these searches. It does not establish that a theorem is unknown worldwide, and is never alone used to assign class D. Class F is reserved for an unidentified object, formula or topology; class C distinguishes a refuted broad statement from the narrower established framework or proposed repair.\n')
print(f'{len(C)} per-claim search rows; {len(events)} check-event rows; {len(L)} reference keys')
