#!/usr/bin/env python3
"""Search audit: exact issued queries and concise checked outcomes; no article copies."""
from pathlib import Path
import json
P=Path(__file__).parent
R={r['key']:r for r in json.loads((P/'reference_checks.json').read_text())}
rows=[]
def q(query,ids,keys,outcome,engine='web search, system1'):
    rows.append(dict(date='2026-11-19',query=query,engine=engine,claim_ids=[f'C-SA23-bt-{n:03d}' for n in ids],opened_sources=[dict(key=k,url=R[k]['url'],locator=R[k]['locator'],verification_extent=R[k]['checked']) for k in keys],match_outcome=outcome,limits='Opened locators establish only the scope stated in claims.json. No-hit results are not evidence of novelty; first-circulation dates remain unavailable unless explicitly distinguished in the record.'))
q('Grothendieck "canonical connection" "torsor" "de Rham" square zero',list(range(22,32))+[88],['bt_GrothCrystals1968','bt_GrothWorks','bt_Stacks03AJ','bt_Stacks01UP','bt_Stacks08J7','bt_Stacks0FKL'],
  'Exact match in Crystals §3.4 pp.326–329: square-zero isomorphism torsor, additive Hom relation, extension of Z, degrees−1,0, derived morphism and transitivity. The published construction corrects the mathematical formulation but does not adjudicate manuscript ink. §3.5 limits higher positive-characteristic conclusions.')
q('Katz Oda differentiation de Rham cohomology parameters periods Stein holomorphic',list(range(3,15)),['bt_KatzOda1968','bt_GrothCrystals1968'],
  'Exact connection and analytic comparison found. Grothendieck §1.2 distinguishes Stein global forms from hypercohomology; Katz–Oda §2 Theorem1 and §4 give algebraic/analytic compatibility. Neither source supports horizontal-endpoint vanishing or simultaneous horizontality of intersecting sections.')
q('Grothendieck EGA "16.8" "différentiels" parties principales formellement exacte',[1,2]+list(range(15,22))+[87,88],['bt_EGAIV4','bt_GrothCrystals1968'],
  'EGA IV4 pp.39–41 directly verifies principal-parts representability and base-linearity. Crystals §§6.2–6.5 gives formalization/Poincaré. No exact definition matching the sheet’s all-P finite-order “formally exact” premise was recovered. The initial quotient on221 lacks preceding definitions.')
q('Serre "Sur les groupes de Galois attachés" "groupes p-divisibles"',list(range(32,55))+[89],['bt_Serre1967','bt_SerreBibliography','bt_Lubin1967'],
  'The supplied text is the published1967 article, pp.118–131, dated December1966. Full attached proof sequence read and checked as recorded. The provisionally admitted Lemma3 is proved on the following page; the general centralizer proof is separately omitted. Official Lubin metadata corrects1961 to1967 without changing transcription.')
q('Sen ramification p-adic Lie extensions 1972 bounded filtrations e n c',[54,55],['bt_Sen1972','bt_Gross1979','bt_FontaineOuyang'],
  'Exact bounded-shift statement and hypotheses in Fontaine–Ouyang A.4.1/A.85 pp.197–200; Sen1972 metadata verified. Mixed characteristic and totally ramified reduction retained; no equal-characteristic theorem inferred.')
q('Serre Hodge Tate modules neutral component algebraic envelope Sen 1973 weight zero',[38,39,40,41,42,43,53,56,57,58,59,60,61,65,67,68,69],['bt_Sen1973','bt_Serre1979','bt_Sahu2019','bt_SerreCourses1968'],
  'Serre1979 §1.1 has algebraically closed residue field; Theorems1–2 and Corollary3 state algebraicity, neutral-envelope generation and weight-zero finite image. Finite inertia components are not removed. Exact Sen centralizer attribution found in Sahu with its explicit application hypotheses. Classification/realization are separated at p.185.')
q('de Jong Homomorphisms Barsotti Tate positive characteristic 1998 full faithfulness erratum',[62],['bt_deJong1998','bt_deJongICM1998','bt_deJongErratum1999'],
  'Author’s ICM Theorem2 p.261 is an exact generic-fibre Hom extension theorem over integrally closed Noetherian integral domains. The entire1999 erratum was opened; only Lemma2.1(iii) and semistability definition corrected, with no other changes.1995submission,1998publication and1999erratum dates separated from2018digitization.')
q('Liu Barsotti Tate crystalline Hodge Tate weights 0 1 Tate curve noncrystalline',[47,65,66,70,71],['bt_Liu2013','bt_Gunton2021','bt_FontaineOuyang'],
  'Liu Theorem2.2.1 gives all-prime BT/crystalline-lattice equivalence under finite totally ramified K/K0. Gunton’s Tate curve gives exact noncrystalline two-weight boundary. Fontaine–Ouyang Theorem2.13 and§6.5TheoremA verify tensor/dual period construction in admissible categories, not arbitrary HT objects.')
q('Ziegler graded filtered fiber functors theorem 4.14 torsor 4.15 characteristic zero',list(range(67,74)),['bt_Ziegler2015','bt_Milne2017'],
  'Grading/cocharacter equivalence and filtered splitting torsor found at precise theorem numbers. Global splitting requires affine/pro-smooth hypotheses; no canonical splitting asserted. First arXiv2011, journal online2013, issue2015 separately verified.')
q('Katz Serre Tate local moduli theorem 1.2.1 2.1 canonical lift',[63,64],['bt_Katz1981','bt_Messing1972','bt_Serre1979'],
  'Exact deformation equivalence over p-nilpotent R and nilpotent I, and ordinary formal-torus parameters read in Katz. Messing1972 chapterV metadata and Serre1979erratum attribution checked; full Messing proof not read.')
q('nonabelian cohomology restriction neutral fibre twisting injectivity cocycles',list(range(74,82)),['bt_Milne2017','bt_SerreGalois1997'],
  'Milne§3k and§23.52 give cocycles, torsors and twisted fibres. SourceΓ remains unspecified. Independent normalization/stabilizer proofs and exact A5 counterexample distinguish neutral kernel from injectivity. Serre1964 chronology verified by publisher foreword and official bibliography.')
q('Weil restriction multiplicative group points tensor product Neron model valuation uniformizer',[59,82,83,84],['bt_JordanRibetScholl2024','bt_Serre1979'],
  'Primary modern exposition§1.1/Proposition1.4 confirms functor of points, Néron generic/special fibres and valuation sequence. It does not identify the handwritten modelÑ or ambiguous point arguments.')
q('Katz Nilpotent connections monodromy theorem 10.0 global nilpotence smooth proper 1970',[85],['bt_Katz1970'],
  'Theorem10.0 read with arithmetic smooth-proper and locally free cohomology hypotheses. It gives nilpotent p-curvature; no absent manuscript arithmetic model or zero p-curvature conclusion inferred.')
q('Bertram Neeb Projective completions Jordan pairs 3-graded Lie algebra 2003',[61,86],['bt_BertramNeeb2003','bt_Springer1973','bt_Serre1979'],
  'Exact three-grading/Jordan-pair formula in§3.1, extra unital structure in§5. Springer§11 identity verified through Serre1979; publisher reprint distinct from1973edition. Journal publisher retrieval returned403, so arXiv2003metadata remains the cited verified version.')
q('site:mathoverflow.net Grothendieck Gauss Manin connection history Cartan',list(range(3,15)),['bt_GrothCrystals1968','bt_KatzOda1968'],
  'No MathOverflow answer was used to settle an exact claim. Followed primary Grothendieck and Katz–Oda sources instead; forum search is logged as coverage, not as novelty evidence.')
q('site:zbmath.org Grothendieck crystals de Rham cohomology 1968',list(range(1,32))+[87,88],['bt_GrothCrystals1968','bt_GrothWorks'],
  'No usable exact zbMATH review retrieved. Direct zbMATH0258.12009 retrieval returned403. Exact primary published construction and official works catalogue verified independently.')
# Additional exact searches retained from the earlier part of this run.
q('Serre "n1 = 1" "Hodge" commutant',[60],['bt_SerreCourses1968','bt_Serre1979'],
  'No exact standalone theorem hit sufficient to replace the source’s hypotheses. The printed course assertion and expanded representation classification were read; no independent full proof of this compressed corollary claimed.')
q('"one-dimensional formal groups" "centralizer" "Sen"',[53],['bt_Sahu2019','bt_Sen1973'],
  'Sahu§3 explicitly attributes the centralizer result to SenTheorem3 and states its application hypotheses. Original Sen proof not obtained/read.')
q('"Serre Tate" "canonical lift" Katz theorem 2.1 pdf',[64],['bt_Katz1981'],
  'Primary author-hosted PDF found and exact ordinary formal-torus/canonical-identity parameter theorem read.')
q('Milne "nonabelian" "twisting" "cohomology" torsors',[73,75,76,77,78,79,80,81],['bt_Milne2017'],
  'Correct iAG2017 algebraic-groups PDF opened; initial AG.pdf link was an algebraic-geometry book and was rejected as an unrelated lead. Twisting and torsor locators verified.')
q('Grothendieck "Crystals and the de Rham cohomology" 1966 pdf',list(range(1,32))+[87,88],['bt_GrothCrystals1968','bt_GrothWorks'],
  'Primary lecture scan opened; §§1.2,3.2–3.5,6.2–6.5 and Appendix read.1966talks/1968publication distinction established; archival leaf date not inferred.')
q('SGA7 expose IX "Tate" "fidèle"',[48,62,65],['bt_Serre1967','bt_deJongICM1998','bt_Liu2013'],
  'Opened current transcription https://grothendiecksga.com/read/sga7/fr/9-5.html §5.8. It concerns Tate/good reduction but was not an exact verified original-source match for the desired generic Hom theorem. Therefore not promoted to a bibliography proof reference.')
q('Katz "Serre-Tate local moduli" 1981 pdf',[63,64],['bt_Katz1981'],
  'Author-hosted full PDF opened; theorem hypotheses, publication identity and ordinary parameters checked.')
q('Serre Cohomologie galoisienne 1964 Lecture Notes 5 Springer',list(range(75,82)),['bt_SerreGalois1997','bt_SerreBibliography'],
  'Publisher foreword and official author bibliography confirm original1964book from1962–63course. Exact current cocycle mathematics checked in Milne and independently, not misrepresented as a full reading of Serre’s book.','web search, system2')
q('site:mathoverflow.net "Hodge-Tate" "crystalline" "two"',[65,66,70,71],['bt_Gunton2021','bt_Liu2013'],
  'No forum result used as theorem authority; primary Tate-curve and BT-essential-image sources supply exact hypotheses.','web search, system2')
q('site:zbmath.org "On the differentiation of de Rham"',list(range(3,15)),['bt_KatzOda1968'],
  'No usable exact review retrieved; primary article opened and read.','web search, system2')
q('site:zbmath.org "Sur les groupes de Galois attachés"',list(range(32,55))+[89],['bt_Serre1967','bt_SerreBibliography'],
  'No usable exact review retrieved; attached primary offprint, publisher entry and author bibliography used.','web search, system2')
with (P/'search_log.jsonl').open('w') as f:
    for a in rows:f.write(json.dumps(a,ensure_ascii=False)+'\n')
with (P/'external_read_log.tsv').open('w') as f:
    f.write('key\tdate\turl\tlocator\textent\n')
    for a in R.values():f.write('\t'.join([a['key'],'2026-11-19',a['url'],a['locator'],a['checked']]).replace('\n',' ')+'\n')
covered={s for a in rows for s in a['claim_ids']};expected={a['id'] for a in json.loads((P/'claims.json').read_text())}
assert expected<=covered,expected-covered
print(len(rows),'search records; all',len(expected),'claims mapped to searched fates')
