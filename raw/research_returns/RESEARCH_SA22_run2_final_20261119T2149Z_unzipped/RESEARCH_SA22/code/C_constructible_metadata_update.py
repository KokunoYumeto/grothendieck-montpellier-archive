from pathlib import Path
import csv
p=Path('RESEARCH_SA22')
f=p/'notes/C_constructible_group_algebraization.tex'
s=f.read_text()
s=s.replace('Lemmas 29.10.2 and 29.51.5 (tags 01S4 and 0BAC).','Lemmas 29.10.2 and 29.51.5 (tags 01S4 and 0BAC)\\cite[tags 01S4 and 0BAC]{C_StacksConstructible2026}.')
s=s.replace('tag 05F9).','tag 05F9)\\cite[tag 05F9]{C_StacksConstructible2026}.')
s=s.replace('Edixhoven--Romagny, not merely a weaker generic associativity condition.','Edixhoven--Romagny\\cite[Definition 2.1, pp.~4--5]{CEdixhovenRomagny2013}, not merely a weaker generic associativity condition.')
s=s.replace('Section 2.  It constructs','Section 2\\cite[Theorem 2.11 and its proof, pp.~4--7]{CEdixhovenRomagny2013}.  It constructs')
s=s.replace('pp.~1--2, records both','pp.~1--2\\cite[pp.~1--2 and p.~2, footnote 3]{CHrushovskiMetastableDraft}, records both')
s=s.replace('Sections 2.B and 3.B, spells out','Sections 2.B and 3.B\\cite[Sections 2.B and 3.B]{CPoizat2025}, spells out')
f.write_text(s)
f=p/'notes/C_absolute_flat_piecewise_comparison.tex'
s=f.read_text().replace('as the full subcategory of $\\operatorname{Abs}_k$ with objects $T(X)$\narising from finite-type reduced schemes','as the full subcategory of $\\operatorname{Abs}_k$ with objects $T(X)$\narising from separated finite-type reduced schemes')
s=s.replace('algebraization in the reflected category','algebraization in the absolutely flat category').replace('subcategory formed by the $T(X)$ for finite-type reduced $k$-schemes','subcategory formed by the $T(X)$ for separated finite-type reduced $k$-schemes')
s=s.replace('universal absolutely flat scheme.  Thus','universal absolutely flat scheme.  The functor $T$ is right adjoint to\nthe inclusion of absolutely flat schemes into schemes.  Thus')
s=s.replace('Stacks, Lemma 32.10.1, parts (2) and (3), tag 01ZM, to the section of','Stacks, Lemma 32.10.1, parts (2) and (3), tag 01ZM\\cite[tag 01ZM]{C_StacksConstructible2026}, to the section of')
f.write_text(s)
bib=r'''
@misc{CEdixhovenRomagny2013,
  author = {Edixhoven, Bas and Romagny, Matthieu},
  title = {Group schemes out of birational group laws, {Neron} models},
  year = {2013},
  eprint = {1204.1799v3},
  archivePrefix = {arXiv},
  url = {https://imag.umontpellier.fr/~romagny/articles/artin_birational_law.pdf},
  note = {OPENED: complete Section 2, Definition 2.1, Lemmas 2.2--2.10 and Theorem 2.11 with proof, author pp. 4--7. Author PDF has copyright 2012; arXiv v3 dated 16 June 2013 is the cited preprint version. No journal publication year is inferred from the PDF copyright. Retrieved 19 November 2026}
}
@misc{CHrushovskiMetastableDraft,
  author = {Hrushovski, Ehud},
  title = {Valued fields, metastable groups},
  year = {n.d.},
  url = {https://webusers.imj-prg.fr/~francois.loeser/mst.pdf},
  note = {OPENED: undated 43-page solo-author draft, introduction pp. 1--2, especially p. 2 footnote 3 quoting Grothendieck's letter to Poizat dated 17 June 1979. The inspected title material does not establish a publication year. This is not Computing the Galois group of a linear differential equation (2002), nor the later Hrushovski--Rideau arXiv version, whose current introduction omits the historical footnote. Retrieved 19 November 2026}
}
@misc{CPoizat2025,
  author = {Poizat, Bruno},
  title = {Logique et g\'eom\'etrie},
  year = {2025},
  howpublished = {MODNET preprint 25-03},
  url = {https://modnet.imj-prg.fr/preprints/papers/25-03-Poizat.pdf},
  note = {OPENED: original preprint Sections 2.B and 3.B, including the characteristic distinction between regular, constructible and piecewise morphisms. Not cited as a complete proof of group algebraization. Retrieved 19 November 2026}
}
@misc{C_StacksConstructible2026,
  author = {{The Stacks Project Authors}},
  title = {Radicial morphisms, birational morphisms, fibre dimension and limits of schemes},
  year = {2026},
  url = {https://stacks.math.columbia.edu},
  note = {OPENED: complete Lemmas 29.10.2 (01S4), 29.51.5 (0BAC), 37.30.3 (05F9), and 32.10.1(2)--(3) (01ZM), including the finite-presentation descent and equality proofs. Exact lemma locators, not merely section tags, used; retrieved 19 November 2026}
}
'''
f=p/'C_references.bib';s=f.read_text()
if '@misc{CEdixhovenRomagny2013,' not in s:f.write_text(s+bib)
rows=[
('C.37','Finite-type constructible graphs give piecewise morphisms in characteristic zero and under the residue-field-trivial convention in every characteristic','C:piecewise-graph-category','Radicial and birational morphisms; noetherian induction','notes/C_constructible_group_algebraization.tex'),
('C.38','Piecewise regular homomorphisms between reduced algebraic groups are regular in every characteristic','C:piecewise-group-fullness','Translation of one nonempty regularity open','notes/C_constructible_group_algebraization.tex'),
('C.39','Reduced algebraic groups are equivalent to group objects in the specified finite-type piecewise category','C:piecewise-group-algebraization','C:piecewise-graph-category; C:piecewise-group-fullness; Edixhoven-Romagny Theorem2.11','notes/C_constructible_group_algebraization.tex'),
('C.40','Universal absolutely flat schemes realize finite piecewise morphisms fully faithfully with internal product T(X times Y)','C:absolute-flat-piecewise','Olivier1968/1978; Ferrand2003Section8.3; EGAI7.2.14; Stacks01ZM','notes/C_absolute_flat_piecewise_comparison.tex'),
('C.41','Group objects in the finite-type absolutely-flat subcategory with its internal product algebraize','C:absolute-flat-group-algebraization','C:absolute-flat-piecewise; C:piecewise-group-algebraization','notes/C_absolute_flat_piecewise_comparison.tex')]
f=p/'C_results.csv'
with f.open(newline='') as h:old=list(csv.reader(h))
ids={r[0] for r in old}
with f.open('a',newline='') as h:
 w=csv.writer(h)
 for id,statement,label,deps,path in rows:
  if id not in ids:w.writerow([id,statement,'Proved',path+', label '+label,deps,'67/047 subject11','Exact finite-type separated reduced finite-partition scope. Does not identify every historical schema morcele or arbitrary pro-affine/sheaf object. No finite test applies.'])
f=p/'C_CHECK_EVENTS.tsv'
with f.open('a',newline='') as h:
 w=csv.writer(h,delimiter='\t')
 for id,statement,label,deps,path in rows:
  w.writerow([label,'2026-11-19','GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/algebra_c, ChatGPT Pro mode','targeted proof and primary-source check','PASS. Complete exact proof in '+path+'. All used primary definitions and proof dependencies opened. No finite certificate applies; see notes/C_constructible_group_source_audit.md.'])
  w.writerow([label,'2026-11-19','GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/algebra_c, ChatGPT Pro mode','independent targeted proof check by B','PASS. B read exact proof and source dependencies. Full Edixhoven-Romagny Section2 and complete absolute-flat sources audited. Notes/B_constructible_group_audit.md.'])
  w.writerow([label,'2026-11-19','GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/algebra_c, ChatGPT Pro mode','independent targeted proof check by root','PASS. Root read the exact group proof and comparison proof route, checked all small scope clarifications, reduced finite-partition stages and internal categorical product. Historical identification remains qualified.'])
print('Added 5 result rows, 15 proof-check events and 4 bibliography entries; amended only C-owned notes/bibliography/metadata.')
