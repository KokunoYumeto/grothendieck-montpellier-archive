"""Manually assessed cross-links; missing project targets remain reported leads."""
import csv,json
from pathlib import Path
B=Path(__file__).resolve().parents[1]
E={int(e['entry_id'].rsplit('#',1)[1]):e for e in json.loads((B/'entries_source.json').read_text())}
I=json.loads((B/'items.json').read_text());byentry={int(s.rsplit('#',1)[1]):i for i in I for s in i['sources']}
rows=[]
def add(kind,ns,to,what,evidence,frm=None):
 if frm is None:
  unique=[]
  for n in ns:
   x=byentry[n]
   loc=f"{x['id']}: cote 138, scans {x['scans']}, {x['lines']}"
   if loc not in unique:unique.append(loc)
  frm='; '.join(unique)
 rows.append(dict(kind=kind,**{'from':frm},to=to,what=what,evidence=evidence,note_ids='; '.join(E[n]['entry_id'] for n in ns)))

add('folder',[1,2,4,5,6,7],
 'SA09_texts/pro/MPL_138_046-089_transcription.tex, cote 138, scan 89, lines 1664–1724, especially 1673; continuation SA09_texts/pro/MPL_138_090-133_transcription.tex, scan 90, lines 2–49',
 'The named-peripheral profinite group and the bound nu>=2 continue directly across the package boundary. The rank bound needed for the inner injection is already present.',
 'Both original combined transcription passages read. The note claiming a missing lower bound is corrected; no additional hypothesis is inserted into the source.')

context=[
('C1',[10,12,13,17,21],'LM_140-2_text.tex, cote 140-2, scans 71–72, lines 2075–2104','Tate-module peripheral maps, conjugacy and tangential choices.'),
('C2',[13,14,15,16,17,18],'LM_140-2_text.tex, cote 140-2, scans 84–85, lines 2398–2437','Common cyclotomic exponent for all peripheral maps.'),
('C3',[1,3,13,15],'LM_140-2_text.tex, cote 140-2, scans 89–92, lines 2580–2685','Orientation module, product relation and injection exceptions.'),
('C4',[1,12,13,14,16,18,19],'LM_140-2_text.tex, cote 140-2, scans 99–100, lines 2888–2947; scans 110–111, lines 3305–3357','Outer actions and the common sign/cyclotomic character.'),
('C5',[3],'LM_140-2_text.tex, cote 140-2, scans 257–259, lines 8260–8325','Low-puncture spaces, groups and rigidifications must be distinguished.'),
('C6',[2,4,7],'LM_140-2_text.tex, cote 140-2, §26, scans 318–320, lines 9473–9540','Centrelessness and discrete completion versus its image.'),
('C7',[5,6,7],'LM_140-2_text.tex, cote 140-2, §26, scans 322–327, lines 9594–9775','Self-normalizer retraction and normality of the geometric strict subgroup.'),
('C8',[5,6,7],'LM_140-2_text.tex, cote 140-2, scans 368–370, lines 10946–10994','Marking dependence and normalizers in the full profinite ambient group.'),
('C9',[9,10,11,18,20],'LM_140-2_text.tex, cote 140-2, scans 331 and 374–377, lines 9863–9883 and 11121–11159','Embedding versus isomorphism torsors, commutant twists and quotient torsors.'),
('C10',[20],'LM_140-2_text.tex, cote 140-2, scans 540–541, lines 15650–15665','Primitive roots and the maximal cyclotomic subextension.'),
('C11',[8],'LM_140-4_text.tex, cote 140-4, scans 185–187, lines 9099–9144; scans 193–195, lines 9222–9255','Finite cone-order presentation and a conditional multiplicity/finite-cover comparison.'),
('C12',[13,16,19],'LM_140-4_text.tex, cote 140-4, scan 96, lines 5613–5644','Cyclotomic character as one component of a richer arithmetic map.')]
for key,ns,target,what in context:
 add('our projects',ns,target,what,'Reported context link '+key+' in MPL_138_090-133_notes.md, context table lines 176–187 and the cited entries, checked on the source side. The exact target files are absent from this attachment. Their line numbers and result claims are retained as reported leads, not independently checked target evidence.')

extra=[
([28],'LM_140-2_text.tex, scan 547, line 15778; LM_140-3_text.tex, scans 180–181, lines 7891–7898; LM_140-3_notes.md, note C3','C2-gerbes, quadratic twists and the Legendre/special elliptic curve comparison.'),
([29],'LM_140-2_text.tex, scans 547–548, lines 15787–15795','An automorphism group versus its effective quotient.'),
([39],'LM_140-2_text.tex, §36, scan 506','Coefficient conjugation passed to the cartographic quotient.'),
([42],'LM_140-2_text.tex, scans 475–479, §§35–36','Later curve/three-point-cover statements do not supply a missing converse in the present pages.'),
([48],'LM_140-2_text.tex, scans 402–403','Boundary and gluing compatibility is stronger than isolated covering naturality.'),
([64],'LM_140-2_text.tex, scans 573–574, lines 16920–16930','Galois action on spherical regular maps, compared with the small sextic orbit.'),
([82,83,84,101,103,104,105],'LM_140-2_text.tex, §23, scans 279–283, especially scan 281','Lifting, centralizers and topology of an identity component; no definition of the present invariant-rigidification space is thereby recovered.')]
for ns,target,what in extra:
 add('our projects',ns,target,what,'The complete cited note entries and their 138 transcription passages were read. Named target files were not supplied; this is a reported lead. The public partial LM PDF is a separate edition and its §§13bis–24 are largely blank, so a heading there cannot verify this exact target.')

add('folder',[21,34,48],'MPL_147_003-047_notes.md, N075, cote 147, scans 003 and 035–047',
 'The notes connect cartographic naturality with a later boundary/gluing question, itself citing LM scans 402–403.',
 'Source entries read; target cote-147 file absent. Both-side content verification is unavailable, explicitly retained as a reported cross-folder lead, not a checked mathematical implication.')

register=[
('EXIT_TOWER E.24','Open, the return’s claim','Finite maps and arithmetic examples do not compute the full arithmetic image.'),
('LM1 D.7','Open, the return’s claim','Geometric completion versus ambient arithmetic/peripheral groups.'),
('LM4 C.12','Open, the return’s claim','A different infinite hyperbolic centralizer question; finite disc rigidity does not settle it.'),
('LM4 D.12','Open, the return’s claim','Complex conjugation is one specified involution, not a classification of profinite torsion.'),
('LM4 D.32','Proved, refereed 14 November 2026 as claimed by the supplied register','Three-cusp rank and finite pure loop groups; no substitution for ambient-group equality.'),
('LM4_SUCCESSOR B.38','Open, the return’s claim','Congruence kernels, including K5; no such kernel computed here.'),
('LM4_SUCCESSOR B.12','Open, the return’s claim','Corrected orbifold target Out_partial(C3 coproduct C3), not settled by the weighted presentation.'),
('LM6 F.35','Proved, the return’s claim','Identifications and forgetful maps; not re-proved here.'),
('LM6 B.27','Open, the return’s claim','Cyclotomic inertia does not answer the centralizer question.'),
('LM7_PUSH E.3','Open, the return’s claim','A small Kummer example does not decide a CM-image problem.'),
('EXIT_TOWER E.49','Explicitly unrefereed claim','Not used to declare LM7_PUSH E.3 settled.'),
('LM2 C.d1','Unreviewed return claim in LM2_CONGRUENCE_ROWS.md','Bridge B5 and congruence rows have a different scope from these finite maps.'),
('LM2 C.r1','Unreviewed return claims C.r1–C.r3 in LM2_CONGRUENCE_ROWS.md','All three row claims retained without status promotion.'),
('WG H1','Unchecked war-game hunch','Peripheral character versus a centralizer assertion.'),
('WG H5','Unchecked war-game hunch','Finite Nielsen classes and generators do not determine unproved arithmetic consequences.'),
('138-operations-belyi-extending','Hua candidate finding / research lead','Rational postcomposition has precise field and index hypotheses.'),
('138-operations-subset-criterion','Hua candidate finding / research lead','Condition on the graph itself is not the repaired complementary-face condition.')]
for token,status,what in register:
 ns=[n for n,e in E.items() if token in e['text']]
 if token=='LM2 C.r1' and not ns:ns=[47]
 add('our projects',ns,'RESULTS_STATE.md / '+token,what,
     'Reported status: '+status+'. The source register summary at notes lines 148–168 and linked source notes were read. The named run/report is absent, so neither its result nor review status is independently verified or changed.')

hua=[
([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41],'§13.I–III, reported lines 1508–1610','Precartes, pinning, raw moduli and finite arithmetic action.'),
([54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70],'§13, “Un arbre de degré 6”, reported lines 1649–1688','Sextic calculations, the corrected discriminant roots and Kummer-field comparison.'),
([71,72,73,74,75],'§14, reported lines 1693–1713','Small spherical-map catalogue and degree bounds.'),
([81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,111,116,117,118,119,120,121,122,123,124,125,126,127],'§15, reported modernization','Operations, rigidification and holomorphic uniqueness; the orange counterexample was already credited to this earlier context.')]
for ns,target,what in hua:
 add('our projects',ns,'Michel Hua, modernization of cote 138, '+target,what,
     'Earlier-run/context attribution preserved. The exact context edition and its line numbering were not supplied. This consolidation independently checks the mathematics but does not claim to have verified those exact target lines. A contemporaneous public AI-assisted edition, if used by the root dossier, is a separate source and not independent corroboration of the notes.')

published=[
([9,10,11,12,13,14,15,16,17,18,19,20,21],'SGA1, Exposé XII, Theorem 5.1; Exposé XIII, §§2.9–2.12; https://arxiv.org/pdf/math/0206203','Comparison, local inertia and the common character.','Both archive passages and exact SGA passages opened; outer actions, basepoint choices and local injectivity hypotheses retained.'),
([28,30,34,37,38,39,40,41],'SGA1, Exposé XIII, Corollary 2.9, construction 2.10 and Lemma 2.11; https://arxiv.org/pdf/math/0206203','Finite prime-to-characteristic cover data and specialization support the finite geometric-class scheme.','Both sides checked. This does not represent the raw rational isomorphism-class presheaf; the quadratic-twist counterexample remains.'),
([1,3,5,6,7],'Grothendieck, Esquisse d’un programme, §2, printed pp.9–10; https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf','Genus-zero tower action, braid language and recognition of the arithmetic image.','Public Esquisse passage and source 138 passages opened. The absent API transcription E1/E2 scan and line references are not treated as the same checked file.'),
([34,35,36,37,38,39,40,41,42,43,44,45,93,127],'Grothendieck, Esquisse d’un programme, §3, printed pp.15–18; same public PDF','Finite cartographic/cover dictionary and later retrospective discussion of the Belyi converse.','Both public passage and source 138 passages opened. The present range explicitly has a Galois action, but does not assert the all-curves converse or global faithfulness.'),
([88,116,127],'Grothendieck, Esquisse d’un programme, §§3–4, printed pp.15–20; same public PDF','Conjugation/hemisphere comparison and the finite/infinite cartographic programme.','Both sides read in the public edition. The definition and topology of the 138 rigidification space remain missing; no exact infinite rigidity theorem is imported.'),
([42,44,45],'Belyi, 1980, Theorem 4, p.255 and corollary, p.256; https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1682&what=fullteng','Later three-point-cover theorem and arithmetic injection, with receipt 2 August 1978 and Russian/English publication 1979/1980.','The source absence claim is checked against the whole late transcription. The later exact theorem was opened; it is not retroactively inserted into the manuscript.'),
([54,56,59,60,61,63,64,65],'Bétréma–Zvonkin, 1993, §4.3, pp.607–608; https://www.labri.fr/perso/zvonkin/Research/vraie-forme.pdf','Exact sextic and cubic family, three-tree arithmetic S3 orbit, backward link to spring-1992 catalogue.','Both sides checked; exact polynomial and orbit matched, not merely broad subject. Independent programs recalculate dependencies.'),
([122,123,124,125,126],'Wood, 2006, §3.1 Proposition 2, §§3.2–3.3, Proposition 4; https://arxiv.org/pdf/math/0304489','Belyi-extending maps and Galois-compatible operations; one specific separation example.','Both sides checked. Q-definition and branch-set hypotheses retained; no universal orbit-separation theorem or strict-cleanness claim follows.'),
([99,100,120,121,122,123],'Ellenberg, author manuscript 2000 / publication 2002, §3, pp.4–6; https://people.math.wisc.edu/~ellenberg/BraidDessin.pdf','Earlier cleaning 4f(1-f) and rational branch-preserving postcomposition.','Both sides checked by backward search. The square (2f-1)^2 has different white-fibre indices and does not universally clean.'),
([101,102,103,104],'Constantin–Kolev, 1994, Proposition 3.2 and Theorem 3.1; https://arxiv.org/pdf/math/0303256','The finite-order disc boundary theorem needed in the isotopy-kernel argument.','Exact theorem/proof opened and its finite-cellular reduction checked; contractibility of unspecified rigidifications is not proved by it.'),
([71,76,77],'Adrianov et al., preprint 2007 / journal 2009, §§5.4, 6.1–6.2; https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2007/157.pdf','Oriented automorphism groups of the digon and planar bouquets.','Exact catalogue entries opened and compared with the permutation certificates. Their oriented clean-map convention differs from the full signed symmetry and folded-edge conventions here.'),
([106,116,127],'Morvan, 2017, Definition 8 and Proposition 8, §11, pp.31–32; https://arxiv.org/pdf/1706.09158','Canonical realization of fully colored dessins and colored graph automorphisms.','Both sides checked. White vertices are retained in the modern theorem and are additional data relative to unmarked edge midpoints.'),
([116],'Cañas et al., 2022, §§1, 2.1–2.3 and Theorem 2; https://link.springer.com/article/10.1007/s13398-022-01285-7','Modern infinite dessins and tame countable group actions.','Exact hypotheses read: locally finite coverings and finite-sided disc faces. This does not answer the unrestricted infinite question as phrased in 138.'),
([30],'Fulton, 1969, Hurwitz schemes and irreducibility of moduli of algebraic curves, publisher record; https://annals.math.princeton.edu/1969/91-3/p06','Bibliographic lead cited in the earlier context for moduli.','Publisher metadata and DOI landing page opened, confirming Annals 90(3),542–575 despite the unusual URL. Full mathematical theorem not inspected; no support for the raw pinned functor is attributed to it.')]
for ns,target,what,evidence in published:add('published work',ns,target,what,evidence)

main=[rows[0]]+[r for r in rows if r['kind']=='published work']
leads=[r for r in rows if r not in main]
for name,data in [('links.tsv',main),('project_leads.tsv',leads),('verified_project_links.tsv',[])]:
 with (B/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(data)
print(len(main),'links with both endpoints read;',len(leads),'reported leads; 0 verified project-file comparisons')
