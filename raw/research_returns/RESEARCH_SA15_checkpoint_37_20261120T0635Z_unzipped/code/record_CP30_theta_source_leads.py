"""Record actual theta-source retrievals after the CP30 paper freeze."""
from pathlib import Path
import datetime,json
w=Path(__file__).resolve().parents[1]
path=w/'notes/late_source_census.json';rows=json.loads(path.read_text())
new=[
 {'key':'Pareschi2021ThetaTorsionLead','author':'Pareschi, G.', 'year':'2021',
  'title':'Torsion points on theta divisors and semihomogeneous vector bundles. arXiv:2007.12252v3,22October2021.',
  'access':'Original11-page arXiv PDF opened and the complete printed text read; cited external dependencies not all audited',
  'locators_and_limits':'Read the full introduction and TheoremsA--C; Section2 including Proposition2.1 and proof; full TheoremA proof in Section3; Theorem4.1 and its reduction to Pareschi--Popa7.30; full TheoremB proof pp6--7; all of Section5, including the separate genus2 proof pp9--10, and references. The paper works over complex abelian varieties. Mukai, Oprea and Pareschi--Popa dependencies are not newly read; no characteristic2 extension of those theorems is claimed. The root proposed a separate direct delta-bound proof for a smooth theta curve, with no Seshadri-constant import and no Cartier identification.',
  'url':'https://arxiv.org/pdf/2007.12252'},
 {'key':'AuffarthEtAl2017ThetaTorsionLead','author':'Auffarth, R.; Pareschi, G.; Pirola, G. P.; Salvati Manni, R. (arXiv metadata includes appendix authorship)',
  'year':'2017','title':'Torsion points on theta divisors. arXiv:1512.09296v4,28June2017; main paper Proc.Amer.Math.Soc.145,89--99.',
  'access':'Original15-page arXiv PDF opened; introduction and initial Section2 setup read',
  'locators_and_limits':'Read printedpp1--2, including Theorem1.1 and Proposition1.2 statements, and Section2 theta-group/isogeny setup through the Lemma2.1 statement onp4. The full main proof and appendix were not read. The source works over complex abelian varieties and is not imported into characteristic2. The main PDF title page lists Auffarth, Pirola and Salvati Manni; the arXiv metadata also lists Pareschi for the appended result. The author-site Torsion_again.pdf request timed out; arXiv original succeeded.',
  'url':'https://arxiv.org/pdf/1512.09296'},
 {'key':'MarcucciPirola2016ThetaErratumLead','author':'Marcucci, V. O., and Pirola, G. P.',
  'year':'2016','title':'Erratum: Points order2 on theta divisors. Rend.Lincei Mat.Appl.27,249--250. DOI10.4171/RLM/733.',
  'access':'Entire original two-page publisher erratum opened and read',
  'locators_and_limits':'Read the complete Proposition1 and proof pp249--250. It proves that a complex theta divisor cannot contain a translate of a maximal isotropic2-torsion subgroup, using irreducibility of the theta representation. It does not assert a subgroup avoiding the theta divisor, and is not a characteristic2 result. The original2012 paper and the cited Kempf book proof were not newly read; no result is imported.',
  'url':'https://ems.press/content/serial-article-files/39856?nt=1'},
 {'key':'Pieper2024ThetaNullvaluesLead','author':'Pieper, A.','year':'2024',
  'title':'Theta nullvalues of supersingular Abelian varieties. arXiv:2208.12492v2,4February2024.',
  'access':'Original37-page arXiv PDF opened; complete introduction printedpp2--4 read',
  'locators_and_limits':'The introduction explicitly fixes p>2 onprintedp2 and uses level4 theta structures. It describes invariant rational functions on a superspecial product and their descent through connected subgroup quotients. No main theorem or algorithm proof in Sections4--6 was read or imported. In particular this is not a verified recipe for the present characteristic2 Cartier calculation.',
  'url':'https://arxiv.org/pdf/2208.12492'}]
known={r['key'] for r in rows};assert not(known&{r['key'] for r in new})
snap=w/'notes/theta_sources30_census_before.json';assert not snap.exists();snap.write_text(path.read_text())
rows.extend(new);path.write_text(json.dumps(rows,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with(w/'notes/ROOT_SEARCH_LOG_30.md').open('a') as f:
 f.write('''
## Torsion avoidance and semihomogeneous theta bounds

Exact engine2 queries: `abelian surface theta divisor maximal isotropic subgroup disjoint odd torsion` and `theta divisor torsion points maximal isotropic subgroup nonvanishing theta constants`. The original author-site Torsion_again.pdf request returned TimeoutError. The EMS two-page erratum and the arXiv1512.09296 original were successfully opened. A subsequent engine1 verification used `"Theta nullvalues of supersingular Abelian varieties" Pieper arxiv` and `"Torsion points on theta divisors" 2n n general bound`, locating the original Pieper and Pareschi preprints. These originals were opened; other hits were metadata only and supply no theorem.

The exact scopes and bibliographic data are recorded in the four new late-source census rows. The Pareschi11-page original was read completely, including its TheoremA/B proofs and genus2 TheoremC argument; the external semihomogeneous-bundle and multiplication dependencies were not newly audited. The source's field is complex. The genus2 proof suggested a direct alternative using the normalization and local delta invariant of[ell]Theta; the root's separate candidate proves its own branch-count bound in the stated characteristic and claims no extension of Pareschi's bundle theory. Its link to the actual Cartier tensor is unproved.

Retrieval provenance: search turn317902890search20--23; timeout turn246763466view0; complete erratum turn246763466view1; arXiv metadata turn246763466view2; original torsion paper turn608871158view0; Pareschi original turn964236038view0 and subsequent complete text reads turn911512914view1--3, turn811879239view0, turn709303443view0; Pieper original introduction turn964236038view1. These identifiers record retrieval, not an assertion that every dependency was read.
''')
with(w/'notes/checkpoint30_changes.md').open('a') as f:
 f.write('\n### Separate theta-source leads after the paper freeze\n\n'
  'Four original-source comparison records were added to the late source census after the '
  'numbered-paper freeze: Pareschi2021, Auffarth and collaborators2017, the Marcucci--Pirola2016 '
  'erratum, and Pieper2024. Their exact scopes and failed retrieval are retained in '
  'notes/ROOT_SEARCH_LOG_30.md. The first two theta-bound sources work over the complex numbers, '
  'and Pieper explicitly fixes p>2. No theorem from them is imported into the frozen paper. '
  'The separate root theta-avoidance candidate uses a direct local delta proof and finite '
  'symplectic incidence count; its Cartesian/Cartier coefficient bridge and any nodal-image '
  'conclusion remain unproved. It is not a numbered theorem or main-gate advance in checkpoint30.\n')
dest=w/'outputs/CP30_theta_source_leads.json';assert not dest.exists()
dest.write_text(json.dumps({'status':'RECORDED','actual_utc':now,'sources':new,
 'frozen_paper_changed':False,'scope':'Exact read scopes only; no theorem import.'},indent=2)+'\n')
print('Recorded four actual primary-source read scopes at',now)
