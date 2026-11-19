#!/usr/bin/env python3
"""Explicit subject assignments made after the root's primary-source review."""
from pathlib import Path
import json,csv,datetime
P=Path(__file__).resolve().parents[1]/'parts/cote63'
# These are manually selected relevant retrieval batches, not keyword-generated verdicts.
families={
 'TATE':([1,2,3,4,8,10,23,24,25,33,51], 'Tate author text and published Antwerp pages; publisher/bibliographic and zbMATH-targeted search. Local reduction and algorithm statements matched directly.'),
 'DELIGNE':([1,2,3,8,10,24,25,27,33,54], 'Deligne1968 IHES catalog, actual 1975 page images, EGA III-2 full PDF, author bibliographies. The automorphism functor and infinitesimal same-j caveats are kept explicit.'),
 'MODFORMS':([1,2,3,4,9,18,24,25,55], 'Deligne1975 Sections6–7 and Katz1973 Sections1–2; Serre–Tate1981. Integral forms, mod-p forms, Hasse sections and canonical lift are different statements.'),
 'ATKINPART':([1,2,3,4,5,6,7,11,17,18,35,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54], 'arXiv author proof, current 2026 publication metadata, exact Atkin–O’Brien1967 original, Atkin11-adic original, Numdam Serre bibliography, zbMATH and MathOverflow targeted queries; backward references followed for the17-progression.'),
 'ATKINJ':([1,2,3,4,6,7,9,11,14,15,17,18,21,22,23,26,28,29,30,35,39,43,44,45,46,47,48,49,50,51,52,53,54,55], 'Original author expositions, published Atkin–O’Brien PDF, Serre collected paper, Katz exact3.13 statements, Guerzhoy2006/2010 full proofs, Maier2009 exact tables; zbMATH/arXiv/MO/Numdam and publisher/backward bibliographies. Sharp depth versus eventual convergence was checked separately.'),
 'SGA':([11,12,14,21,22,31,32,34], 'SGA4 digitized original: XII5.1 and XVI1.2; SGA7II XXI5.2.2; Deligne1974 original Numdam PDF. Proper and smooth base change and purity have separately matched hypotheses.'),
 'CM':([11,12,13,20,24,27,36,37,51,52], 'Original Stark records attempted; author historical article Stark2007 read; DLMF modular conventions. Class-number-one fields, nonmaximal orders and finite numerical corroboration are distinguished.'),
 'HODGE':([5,6,7,8,9,11,12,13,14,15,16,19,20,21,24,27,36,49,51,54,55,56], 'Katz1976 exact Hodge-line and converse question; arXiv/MO/zbMATH searches; author papers on almost holomorphic singular moduli. Independent supplement follows Bertrand1978, Waldschmidt2004 and Spence2018 and rejects a generated deRham/Betti conflation.'),
 'LOCAL':([5,14,15,16,17,18,20,21,23,24,27,36], 'Katz Serre–Tate deformation theorem, Deligne small-characteristic equations, Artebani–Dolgachev Hesse pencil, Hua2026 exact tangent computation, Kummer hypotheses. No group-scheme assertion is inferred from point counts alone.'),
 'REUSED':([2,17,21,22,23,24,27,31,32,34,36,37,38,39,40,41,42,54], 'Published SGA6X7.14 question identified against the draft; Fulton1975 Sections4.1–4.4 read; Lurie Banach proof; Deuring publisher and SerreBourbaki bibliography. Unavailable correspondence is not assigned a mathematical fate.')
}
req=json.load(open(P/'search_requests.json'));existing={a['id'] for a in req}
claims=json.load(open(P/'claims.json'));records=[]
for c in claims:
    ids,scope=families[c['search_family']]
    records.append({'claim_id':c['id'],'family':c['search_family'],'search_ids':';'.join('S63-'+str(x).zfill(3) for x in ids if 'S63-'+str(x).zfill(3) in existing),'searched_scope':scope,'exact_result':c['fate'],'refs':';'.join(c['refs']),'date':'2026-11-19'})
with (P/'claim_search_coverage.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(records[0]),delimiter='\t');w.writeheader();w.writerows(records)
with (P/'search_log.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['search_id','date','request','returned_urls','response_sha256','retention_note'])
    for a in req:w.writerow([a['id'],a['recorded_date'],json.dumps(a['request'],ensure_ascii=False) if a['request'] is not None else a['request_scope'],';'.join(a['source_urls']),a['response_sha256'],'Third-party response bodies excluded; the claim map records the assessed mathematical scope.'])
print(json.dumps({'claims_with_searched_fate':len(records),'families':len(families),'retrieval_batches':len(req)}))
