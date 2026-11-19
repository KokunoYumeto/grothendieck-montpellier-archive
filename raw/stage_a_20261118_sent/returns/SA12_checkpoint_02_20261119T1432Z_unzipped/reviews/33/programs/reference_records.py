"""Bibliography records from actually opened pages, with access scope explicit."""
import json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
R=[]
def add(key,title,author,year,url,scope,calls,verified=True,extra=None):
 R.append(dict(key=key,title=title,author=author,year=str(year),url=url,note='verified' if verified else 'unverified',scope=scope,search_calls=calls,extra=extra or {}))
add('SA12_SGA4III','Théorie des topos et cohomologie étale des schémas, Tome3 (SGA4, Exposés IX–XIX)','Artin, Michael and Grothendieck, Alexander and Verdier, Jean-Louis',1973,'https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf','Full primary re-edition opened. Targeted statements/proof passages read in XVI1.6,2.1–2.2,3.8–3.10,4.1; XVII5; XVIII2.9–2.10,3.2.5–3.2.6; XIX introduction. Not a proof audit of all423 PDF pages. Seminar1963–1964. Deligne attribution for XVII–XVIII separately checked against IAS bibliography.',[7,10,11,13,14,16,29,30,31,32],True,{'series':'Lecture Notes in Mathematics','volume':'305','publisher':'Springer'})
add('SA12_Riou2014','Classes de Chern, morphismes de Gysin, pureté absolue','Riou, Joël',2014,'https://www.numdam.org/book-part/AST_2014__363-364__301_0/','Official publication metadata opened; author full text at https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/16-classes-de-Chern/gysin.pdf opened and §2.3,2.5.13,3.1.1,3.1.3–3.1.4 read. PDF dated2016-11-14; original exposition301–349 in2014. Seminar talks2006-06-16 and2007-04-13.',[3,7,14,29],True,{'journal':'Astérisque','volume':'363–364','pages':'301–349'})
add('SA12_ILO2012','Travaux de Gabber sur l’uniformisation locale et la cohomologie étale des schémas quasi-excellents. Séminaire à l’École polytechnique2006–2008','Illusie, Luc and Laszlo, Yves and Orgogozo, Fabrice',2012,'https://arxiv.org/abs/1207.3648','Abstract and full PDF opened; XIII1.1.1 finiteness and XV1.1.2 affine theorem statements inspected. arXiv submitted2012-07-16; collection published as Astérisque363–364 in2014. Editors listed as authors for this collection citation.',[22,23],True,{'eprint':'1207.3648','archivePrefix':'arXiv'})
add('SA12_Fujiwara2002','A proof of the absolute purity conjecture (after Gabber)','Fujiwara, Kazuhiro',2002,'https://doi.org/10.2969/aspm/03610153','Real paper corroborated by Riou’s primary bibliography. DOI opening failed; this paper’s theorem/proof was not opened. Do not conflate it with the distinct Fujiwara intersection-theory exposition encountered in search.',[2,3,14],False,{'journal':'Advanced Studies in Pure Mathematics','volume':'36','pages':'153–183','doi':'10.2969/aspm/03610153'})
add('SA12_Milne2013','Lectures on Étale Cohomology, Version2.21','Milne, James S.',2013,'https://www.jmilne.org/math/CourseNotes/LEC.pdf','Author’s full PDF opened. Version dated2013-03-22; targeted results15.1,20.2,21.1–21.5 read for bounds, proper smooth local constancy and comparison/Riemann existence.',[10,13,28],True)
add('SA12_Hansen2017','Artin vanishing in rigid analytic geometry','Hansen, David',2017,'https://arxiv.org/abs/1708.07276','arXiv abstract and v1 PDF opened. Theorem1.7, Conjecture1.8, proof §3 and bibliography read. First submitted2017-08-24. Later2020 journal revision has title Vanishing and comparison theorems in rigid analytic geometry; its results are not substituted for the opened version.',[6,15,16],True,{'eprint':'1708.07276','archivePrefix':'arXiv'})
add('SA12_Huber1996','Étale Cohomology of Rigid Analytic Varieties and Adic Spaces','Huber, Roland',1996,'https://link.springer.com/book/10.1007/978-3-663-09991-8','Publisher metadata and table of contents opened; full book theorem text not inspected. Corollary3.2.3 and proper comparison3.7.2 are locators reported by the opened Hansen primary paper, not independently checked in the book.',[31],True,{'series':'Aspects of Mathematics','volume':'30','publisher':'Vieweg','doi':'10.1007/978-3-663-09991-8'})
add('SA12_Hartshorne1967','Local Cohomology: A seminar given by A. Grothendieck, Harvard University, Fall1961','Hartshorne, Robin',1967,'https://link.springer.com/book/10.1007/BFb0073971','Publisher metadata and contents opened, including source seminar date1961 and publication1967. §§1–2 are bibliographic matches to the manuscript margin; the exact circulated1961 notes and their text were not collated.',[29],True,{'series':'Lecture Notes in Mathematics','volume':'41','publisher':'Springer','doi':'10.1007/BFb0073971'})
add('SA12_EGAIV4','Éléments de géométrie algébrique IV: Étude locale des schémas et des morphismes de schémas, quatrième partie','Grothendieck, Alexander',1967,'https://www.numdam.org/item/PMIHES_1967__32__5_0/','Official publication page opened, with title, volume and pagination. The large PDF failed to open. §19.6 heading is consistent with the attached leaf and a secondary navigation table, but missing conditionsb,c were not recovered or verified. Collaboration with Jean Dieudonné is part of the EGA attribution.',[3,6,18,19],True,{'journal':'Publications Mathématiques de l’IHÉS','volume':'32','pages':'5–361','doi':'10.1007/BF02732123'})
add('SA12_Bourbaki1968','Groupes et algèbres de Lie, Chapitres4,5 et6','Bourbaki, Nicolas',1968,'https://link.springer.com/book/10.1007/978-3-540-34491-9','Publisher book/chapter metadata and Bourbaki’s official bibliography https://www.bourbaki.fr/Ouvrages.html opened. First edition1968; opened publisher record is2007 reprint. ChapterVI pagination142–233 verified, but tables/plates were not opened in full. No identification of typescript n°391 is claimed.',[3,8,24],True,{'publisher':'Hermann; later Springer reprint','doi':'10.1007/978-3-540-34491-9'})
add('SA12_Bourbaki1972','Groupes et algèbres de Lie, Chapitres2 et3','Bourbaki, Nicolas',1972,'https://link.springer.com/book/10.1007/978-3-540-33978-6','Publisher metadata/contents and official bibliography opened. Original edition1972, later Springer reprint2006; ChapterIII pages95–285. Exact Tribu n°62 draft and its notation were not identified.',[3,25],True,{'publisher':'Hermann; later Springer reprint','doi':'10.1007/978-3-540-33978-6'})
add('SA12_Coxeter1934','Discrete Groups Generated by Reflections','Coxeter, H. S. M.',1934,'https://sites.math.washington.edu/~billey/classes/reflection.groups/references/Coxeter.1934.pdf','Primary article PDF opened, with receipt date1933-06-16, publicationJuly1934, classification §9 and table/diagram locators. Targeted excerpts read; not a full independent proof of the classification.',[24,26],True,{'journal':'Annals of Mathematics','volume':'35','number':'3','pages':'588–621'})
add('SA12_SGA3XXI','Données radicielles, ExposéXXI, SGA3','Demazure, Michel',1970,'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp21-13oct24.pdf','Primary-text re-edition dated2024 opened. Definitions, classification framework and §7.5.1 on irreducible scaling inspected. Original SGA3 seminar1962–1964 and publication1970 are distinguished from this modern re-edition; no date for the reused manuscript leaf inferred.',[13,15,16],True)
add('SA12_KleisliWu1964','On Injective Sheaves','Kleisli, Heinrich and Wu, Charles T.',1964,'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008439500052309','Primary article PDF opened, particularly final remarkp422 on right-perfect categories/enough small objects and reference5 to Gray’s Columbia mimeograph. Received1963-06-01; published1964. The source identification remains a lead, not a proved attribution of the attached English fragment.',[10,14,17],True,{'journal':'Canadian Mathematical Bulletin','volume':'7','number':'3','pages':'415–423','doi':'10.4153/CMB-1964-040-4'})
add('SA12_Gray1965','Sheaves with values in a category','Gray, John W.',1965,'https://doi.org/10.1016/0040-9383(65)90066-2','Real publication corroborated in bibliographic/search results and the earlier mimeograph citation in Kleisli–Wu. DOI/publisher full opening failed. Neither this article nor its missing ChapterI definitions were inspected; unverified accordingly.',[15,17,18,20,21],False,{'journal':'Topology','volume':'3','pages':'1–18','doi':'10.1016/0040-9383(65)90066-2'})
add('SA12_Wehler2017','Lie Algebras and Lie Groups, Draft Release0.51','Wehler, Joachim',2017,'https://www.math.lmu.de/~wehler/LieAlgebrasLieGroupsScript.pdf','Author’s144-page PDF opened; date2017-08-02 and introductory scope verified. Theorem3.5 formal-group Lie bracket was identified by search excerpt, but subsequent find operations failed; its entire proof was not read. This is a comparison source, not a claimed identification of Tribu62.',[25,26,28],True)
stacks=[
 ('095T','Theorem59.91.11, Proper base change',[4]),
 ('0EYU','Theorem59.89.2, Smooth base change',[4]),
 ('095U','Proper cohomological-dimension bound',[4]),
 ('03SH','Section59.66, Méthode de la trace',[4]),
 ('03QP','Finite morphisms and higher direct-image vanishing',[4]),
 ('03RW','Constructible sheaves',[4]),
 ('06YV','Section21.18, Derived pullback',[5]),
 ('0GL0','Theorem63.14.5, Constructibility of direct images with compact support',[5]),
 ('0G2A','Lemma63.10.2, Cohomological bound for compact support',[5]),
 ('0F7J','Lemma63.9.2, Composition of compact-support direct images',[5]),
 ('01DI','Injectives in the category of sheaves of modules',[13]),
 ('061M','Quasi-regular sequences',[22]),
 ('067M','Regular, Koszul-regular, H1-regular and quasi-regular implications',[22]),
 ('03QQ','Section59.59, Cohomology of a point',[26]),
 ('03Q9','Theorem59.53.1, Stalks of higher direct images',[26]),
 ('04HX','Lemma59.33.1, Étale stalk and strict henselization',[26]),
 ('0B6E','Section21.36, Global derived Hom',[27]),
 ('09XP','Section59.79, Cohomology with support in a closed subscheme',[27]),
 ('0AZR','Section43.14, Tor formula and localization',[29]),
 ('05NU','Lemma19.2.6, Baer’s criterion',[31]),
 ('072X','Section21.14, Leray and relative Leray spectral sequences',[35,36]),
]
for tag,title,calls in stacks:
 add('SA12_Stacks'+tag,title,'The Stacks Project Authors',2026,'https://stacks.math.columbia.edu/tag/'+tag,'Actual tagged page opened and the relevant statement/hypotheses inspected on19November2026. Dynamic reference; this access date is not the theorem’s first publication date. Proof audit is limited to the events recorded separately.',calls,True)
for r in R:
 if r['key']=='SA12_SGA3XXI':
  r['search_calls'] += [33,34]
  r['scope'] += ' Original1970 publication and chapter pages85–155 independently verified on Springer https://link.springer.com/book/10.1007/BFb0059027 in call34.'
 if r['key']=='SA12_Coxeter1934':
  r['search_calls'] += [33]
  r['scope'] += ' Theorem9 and Lemmas9.1–9.2 at printed601–602 read in call33.'
 if r['key']=='SA12_Wehler2017':
  r['search_calls'] += [33,34]
  r['scope'] += ' Further find/open attempts in calls33–34 also returned502; no additional proof reading claimed.'
(O/'REFERENCE_ACCESS.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
def esc(s): return str(s).replace('&',r'\&').replace('_',r'\_')
with (O/'references.bib').open('w') as f:
 for r in R:
  f.write('@misc{'+r['key']+',\n')
  for k,v in dict(author=r['author'],title=r['title'],year=r['year'],url=r['url'],note=r['note'],annote=r['scope'],**r['extra']).items():
   f.write('  '+k+' = {'+(str(v) if k in ['url','doi'] else esc(v))+'},\n')
  f.write('}\n\n')
print(f'Wrote {len(R)} references: {sum(r["note"]=="verified" for r in R)} opened, {sum(r["note"]=="unverified" for r in R)} unverified; access scope retained.')
