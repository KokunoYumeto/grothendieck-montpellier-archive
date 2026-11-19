#!/usr/bin/env python3
"""Concise search and exact-match audit; handwritten mappings, mechanical serialization."""
import json,re,csv
from pathlib import Path
P=Path(__file__).parent
groups=json.loads((P/'claim_groups.json').read_text())
claims=json.loads((P/'claims.json').read_text())
ref={x['key']:x for x in json.loads((P/'reference_checks.json').read_text())}
# Each mapping identifies the actual topical searches/primary openings used for
# these already-read statements. A reference hit alone never determines a fate.
M={
 'incidence':([1,2,9,10,13],'Projective quotient conventions and universal-section first jets; direct affine-chart proof.'),
 'generic':([1,2,3,6],'Generic incidence, Samuel/Seidenberg, Stacks primary-field lemma; ordinary and geometric irreducibility distinguished.'),
 'local_properties':([1,9,22],'EGA associated-prime, flat-depth and dimension statements read in original PDF; generic-section application checked independently.'),
 'smooth_bertini':([1,9,13],'Stacks smooth Bertini and original EGA local differential hypotheses; the global nowhere-zero auxiliary lemma is explicitly refuted.'),
 'connectedness':([1,2,38,39,44,45,46,47,49],'Connectedness queries, then MO→Martinelli/Naranjo/Pirola primary paper and EGAIII1 4.3.7–8. No exact all-m relative C_m theorem located.'),
 'spreading':([9,22],'Benoist proper-flat family theorem and original EGAIV3 9.7.7,12.2.1–4; precise openness restrictions retained.'),
 'relative_divisors':([10,13,14,22],'Relative Cartier criterion and EGAIV3 11.3.7–8; cancellation/restoration is a source event, not a literature theorem.'),
 'seidenberg':([1,2,5,6,42,43],'Samuel primary exposition fully read; AMS original retrieval failed, not treated as proof access.'),
 'quasisections':([4,10,22,27],'EGAIV4 17.16 quasi-finite scope compared with the draft finite strengthening; projectivity gap retained.'),
 'exceptional_depth':([3,9,36,38,39,40],'Benoist exact bounds and depth obstruction; Poonen–Slavov and higher-slice literature. Full sheaf-valued componentwise iff not matched.'),
 'duality':([3,4,5,7,8,24,25],'Original SGA7II XVII conormal/differential proof and Fermat inseparability example; later quadratic definitions checked.'),
 'poonenslavov':([3,9,38],'Poonen–Slavov exact Th1.5,Example1.7,Th1.8; independent blow-up total-transform computation.'),
 'surface_irreducibility':([3,9,38,39],'Benoist dimension-two bound and SGA7 nodes; full finite-exceptional-set iff not claimed settled.'),
 'fixed_base':([1,2,9,13],'Stacks fixed-subscheme smoothness and codimension-two base-locus irreducibility; independent fixed-divisor counterexample.'),
 'veronese':([3,4,5,7,8],'SGA7II XVII2.5.1 and XII1.1–2; ordinary quadratic point distinguished from separable conormal map.'),
 'lefschetz_heading':([3,4,38,44],'SGA/Lefschetz/fundamental-group searches locate related precise results but cannot identify the incomplete literal heading.'),
 'pencils':([3,4,5,22],'Original SGA7II XVII2.5 and blow-up universal property; Rees identity independently checked.'),
 'grassmann':([10,13,14],'Stacks quotient charts and projective convention; infinite-rank and nonsplit-sequence conclusions checked separately.'),
 'higher_sections':([9,13,38,39,40,41],'Flag iteration plus Kmentt–Shute Theorem1.2 full proof; Remark1.5 expressly leaves arbitrary-morphism extension expected.'),
 'schubert':([3,4,13,38,39,40],'Determinantal/Grassmannian framework and Lefschetz pencil comparison; exact rank count and conic counterexample.'),
 'artin':([4,23,24,26,27,28,29,30,31,32,33],'Original ArtinXI and Schmidt–Stix Lemma6.3 full proofs; perfect/infinite/rational/nonrational hypotheses separately matched.'),
 'artin_finite':([4,5,6,7,8,23,24,25,26,27,28,29,30,31,32,33,42],'PSV2009 Appendix full proof; Panin2025 Th5.3 full proof; Panin2019 metadata and indexed statement only. Relative or unspecified disconnected variants not inferred.'),
 'artin_relative':([4,17,18,19,20,21,23,24,27],'Guo–Panin Def1.1/Th1.3 compared explicitly: smooth projective over regular local base, weak rather than geometrically connected fibers.'),
 'projection':([3,9,13,22,34,35],'Noether normalization/Grassmannian geometry and miracle flatness; generic-fiber loophole tested by the same explicit blow-up, not a new literature identification.'),
 'axiomatic':([1,3,9,36,37,38,39,43],'Jouanolou, Cumino/Greco/Manaresi and Spreafico title/backward searches; restricted/inaccessible full texts recorded. Local incidence proof checked; no exact global-axiom theorem certified.'),
 'picard':([9,13,14,42,44,45],'Projective-space Picard/UFD proof, proper cohomology/base change, original EGAIII1 announcement and deformation step.'),
 'divisors':([9,10,13,14,22,42,44,45],'Original EGAIII2 7.7.6 and base change, universal quotient and relative Cartier locus. Corepresentability is distinguished from the full divisor-functor statement.'),
 'linear_systems':([9,10,13,14,42,44,45],'Relative Cartier criterion, quotient Grassmannian and cohomology base change; nonzero/nonnilpotent/associated-point conditions checked.'),
 'hartogs':([14,15,16,22,34,35],'Stacks0E9I full proof and original EGAIV2 5.10,6.3 plus IV3 11.3.7–8; fixed-divisor ambiguity tested independently.'),
 'faithfulness':([9,13,14,42,43,44,46,47,48,49,50],'Linear-system and Hilbert-tangent search, followed to Grothendieck’s original1961 5.3–5.5; arbitrary-functor strengthening kept separate.'),
 'brauer':([42,43,44,46,47,48],'PGL/Brauer–Severi query followed to Reineke–Schröer §2 primary general-scheme preliminary discussion; descent proof also given.'),
 'linear_system_questions':([9,13,14,42,44,45,46],'Projective quotient/divisor theory and primary tangent/parameter sources; no exact full imperfect-field extension located.'),
 'limits':([22],'Original EGAIV3 finite-presentation limit framework; elementary finite-data proof of the cancelled step.'),
 'hodge':([14,17,18,19,20,21],'Deligne–Illusie primary introduction read. No canonical interpretation of the manuscript H_n is selected from a related theorem.'),
 'ordinary':([3,4,5,6,7,8,16],'Original SGA7II XII1.1–2 and XVII§§1–3, ConradC.1; ordinary smooth quadric versus polar nondegeneracy.'),
 'hessian':([3,4,5,6,7,8,15,16,38,39,43],'SGA7 conormal/Hessian comparison and Conrad invariant quadratic form; determinant character recomputed symbolically.'),
 'ramification':([3,4,5,7,8,38,39,43],'SGA7II XVII3.3 proof compared with source diagram; conormal fiber-injectivity shortcut refuted by a node.'),
 'elementary':([3,4,5,6,7,8,15,16,38,39,43],'SGA7 ordinary local form and Conrad quadratic smoothness; higher-degree and augmented-ring claims retain their precise residual scope.'),
 'hilbert':([5,6,8,15,16],'Quadratic associated-graded local form in original SGA7 and Conrad; polynomial Hilbert series independently recomputed, graded versus cumulative rank separated.'),
 'intrinsic':([3,4,5,6,15,16,38,39,43],'Intrinsic Hessian/cotangent/critical-locus searches plus original SGA7 and EGA conormal setting. No exact arbitrary-base second-order factorization matched; split-kernel base-change argument repaired.'),
 'duality_correction':([3,4,5,7,8,24,25],'SGA7 Fermat example and Gauss-map searches; conjectural degree2 phrase depends on original versus higher-Veronese embedding.'),
 'transversality':([15,16,36,37,38,39,43],'Intrinsic Hessian and axiomatic transversality searches, with EGA/SGA local comparison; no exact complete pair statement identified.'),
 'quadratic':([5,6,7,8,15,16,27],'SGA7II XII1.1–2 exact characteristic-two distinction; Conrad AppendixC full relevant passages.'),
 'halfdisc':([5,6,7,8,15,16,17,18,27,51,52],'ConradC.1.4 and Dolgachev–Duncan Prop2.2/Remarks2.3–4; universal polynomial and odd-plus-odd factor recomputed.'),
 'quadratic_forms':([5,6,8,15,16,19,20,21],'ConradC.1.4,C.2.1 and SGA7XII1.2; explicit fppf normal-form/descent proof.'),
 'orthogonal':([5,6,8,15,16,19,20,21],'ConradC.1.5 full characteristic-two orthogonal-group treatment; even Dickson component versus odd mu2 quotient.'),
 'finite_trivialization':([15,16,17,18,19,20,21,41],'SGA3XXIV original and corrected4.2.3 read with proof; split reductive/semilocal finite étale theorem applied only after the correct finite component torsor.'),
 'halfdisc_history':([5,6,8,15,16,17,18,27,51,52],'Backward citation from Dolgachev–Duncan to unpublished Grothendieck17.16 and Kneser2002; publisher metadata opened. Independent discovery is documented, exact relative priority is not.'),
 'veronese_fixed_space':([53,54,55],'Recovered literal question on scan81, independently checked against a singular pencil on the Veronese plane. Stacks33.47.1/3 full proof reread; Wutz2016 Theorem1.2 and local jet obstruction Lemmas2.3–2.4 read. Finite-field asymptotic hypotheses are not substituted for an arbitrary degree≥2 claim. Backward Altman–Kleiman publisher opening failed and is not used as an opened exact theorem.'),
 'general_divisor_scheme':([56,57,58,59,60,61],'Recovered deleted future-chapter promise on scan112. Exact own-publication match found in Grothendieck Bourbaki232 Proposition4.1; its noetherian context and preceding open-Hilbert argument read, printed152 visually inspected. The linked1962 erratum was obtained through the alternate primary /item/ PDF route and read. No relative chronology of the cancelled leaf and1962 exposé is inferred.')
}
assert set(M)==set(groups),(set(groups)-set(M),set(M)-set(groups))
log=[];batchids=set()
for f in sorted(P.glob('search_[0-9]*.json')):
 raw=json.loads(f.read_text());n=int(f.stem.split('_')[1]);res=raw.get('result',raw.get('value',raw))
 args=raw.get('args',raw.get('queries'))
 meta=[]
 for v in res.get('content',[]):
  for block in v.get('text','').split('--------------------------------------------------------------------------------'):
   m=re.search(r'^\s*(.*?)\s*\((https?://[^\n]+)\)\s*\n【([^】]+)】',block,re.M)
   if m:meta.append({'title':m.group(1),'url':m.group(2),'retrieval_ref':m.group(3),'failed':any(s in block for s in ['Failed to fetch','not accessible','403 Forbidden'])})
 bid=f'hyp-search-{n:03}';batchids.add(bid)
 log.append(dict(id=bid,date='2026-11-19',requests=args if args is not None else 'Original request payload not retained; returned primary/discovery metadata below preserves the actual retrieved sources. No query is invented.',purpose=raw.get('purpose',''),result_metadata=meta,claim_ids=[c for g,(ns,_) in M.items()if n in ns for c in groups[g]],warning='Search result discovery is not exact-claim verification. Unofficial SGA translations, AI readers and unrelated hits were not used as mathematical evidence.'))
for g,(ns,scope)in M.items():
 log.append(dict(id='hyp-group-'+g,date='2026-11-19',claim_ids=groups[g],search_batches=[f'hyp-search-{n:03}'for n in ns],source_comparison=scope))
for c in claims:
 g=next(g for g,cs in groups.items()if c['id']in cs);ns,scope=M[g]
 log.append(dict(id='hyp-fate-'+c['id'],date='2026-11-19',claim_ids=[c['id']],group=g,search_batches=[f'hyp-search-{n:03}'for n in ns],refs=[{'key':k,'note':ref[k]['note'],'exact_check':ref[k]['annote']}for k in c['refs']],exact_match=c['fate'],limits=c['present_status'],assessment_basis=scope))
log.append(dict(id='hyp-coverage-and-limits',date='2026-11-19',named_resources={'zbMATH Open':'Direct0511.14025 query and domain searches attempted, retrieval failed; failure not evidence of novelty.','arXiv':'Primary version histories opened for Benoist,Poonen/Slavov,PSV,Schmidt/Stix,Guo/Panin,Dolgachev/Duncan,Kmentt/Shute and connectedness paper; Panin2017 endpoint failed.','MathOverflow':'Searches and connectedness question opened; followed backward to primary paper. No MO assertion alone serves as a mathematical certificate.','Numdam':'Samuel,Benoist,EGAIII/IV and Grothendieck Hilbert221 primary PDFs/records.','EGA/SGA':'Original published PDFs, exact passages, and corrected SGA3 original/typed comparison.','collected works and author bibliographies':'CSG published-works catalogue, Conrad author page/PDF, Polo SGA3 bibliography; later papers followed backward to original exposés.'},missing_raw_batches='Earlier openings numbered11–12 in working conversation were not preserved as raw response files. Their exact checks are documented in reference records and local retrieval/read outputs; no nonexistent raw file is cited.',source_read_scope='EGA/SGA PDFs were read only at specified passages. All7304 manuscript transcription lines were read. No manuscript images were opened.',date_limit='Status checked19November2026; unsuccessful searches justify only not identified in this search, not a universal claim of nondevelopment.'))
with(P/'search_log.jsonl').open('w')as f:
 for row in log:f.write(json.dumps(row,ensure_ascii=False)+'\n')
assert all(f'hyp-search-{n:03}'in batchids for ns,_ in M.values()for n in ns)
with(P/'fate_check_events.tsv').open('w')as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 for c in claims:w.writerow([c['id'],'2026-11-19','GPT-6 Astra Pro; effort not independently exposed; SA23-20261119/root','used and rechecked in this run','Exact fate/hypothesis comparison recorded in search_log.jsonl, hyp-fate-'+c['id']+'. '+c['fate']])
print(json.dumps({'raw_query_batches':len(batchids),'manual_topic_mappings':len(M),'claims_with_searched_fate':len(claims),'audit_rows':len(log)}))
