"""Manually assigned research families, check strengths, repairs and cross-links."""
import pathlib,json,csv,re
out=pathlib.Path(__file__).parent
claims=json.loads((out/'claims.json').read_text())
byid={int(c['id'].split('-')[-1]):c for c in claims}
families=[]
def family(ids,scope,channels,refs,match,limits='No priority or influence claim is inferred merely from similarity.'):
 families.append((ids,scope,channels,refs,match,limits))
family(list(range(601,610)),
 'Ray classes/ideles; unit congruence finite index; Artin target and completions; generalized Jacobian/Picard degree and local symbols.',
 'Web title/topic searches; author course notes; J-STAGE primary Chevalley; Numdam Bourbaki; Serre publisher/bibliography; original local-symbol paper.',
 ['MilneCFT2020','Chevalley1951','Koszul1954','Serre1959','Deligne1991'],
 'CFTV5.3/5.5, ChevalleyI and the generalized Picard construction match the refined scope; sign and completion errors checked independently.',
 'Serre1959 full book unavailable; publisher metadata and contents opened. No exact book page claimed verified.')
family([610,611,613,614,615,630],
 'Ext/cohomology fundamental class; admissibility; constant-Z finite-field cohomology; curve complex and relative Witt Jacobian.',
 'Numdam Serre primary article; arXiv and author PDF extension-sheaf paper; generalized-Jacobian primary exposition; EMS local-Jacobian abstract; backward references.',
 ['Serre1960','RibeiroRosengarten2026','Koszul1954','ContouCarrere2013'],
 'Exact category/degree comparison is only partial; no unnamed complex is identified from a broad title match.',
 'Contou-Carrère full PDF exceeded retrieval limits; only its explicit publisher mathematical abstract supports the stated dimension-one result.')
family([612],
 'Big Witt lambda-series; F,V relations and Cartier note chronology.',
 'IHES primary Cartier note and author bibliography; SGA formal-group references.',
 ['Cartier1967','SGA3VIIB'],'Exact characteristicp formula verified; convention transported explicitly.')
family(list(range(616,623)),
 'Higher adeles/local flags; Matlis Hom and filtered colimits; residue-complex action; Beilinson–Tate operator algebras; simplicial normalization and DG signs.',
 'arXiv title and topic searches; Yekutieli and BGW full primary papers; primary Matlis PDF; EGAIV3 downloaded; backward references to Beilinson/Huber/Yekutieli.',
 ['Yekutieli2003','BGW2016','Matlis1958','EGAIV3'],
 'Exact published action/structural results matched; all-End equality and draft quotient remain stronger. Hom/colimit and sign counterexamples supplied.',
 'Early Beilinson1980 and Huber1991 dates are reported by opened later primary literature; no claim to have independently read those originals.')
family(list(range(623,630)),
 'Local Zariski cohomology; regular-local concentration; local Jacobian pro-representability; henselian pi1; radicial purity.',
 'SGA1/SGA2 full reprints; Stacks primary lemmas; Serre proalgebraic full paper; EMS local-Jacobian abstract; searches for higher local Jacobian.',
 ['SGA1','SGA2','Stacks0BJD','Serre1960','ContouCarrere2013'],
 'Scalar local-cohomology and standard henselian/etale assertions established; unrestricted higher local Jacobian and unspecified Weil topology not identified.')
family([631,632,634],
 'Fppf/fpqc functor continuity, finite-presentation descent, perfection, proposed Weil site and Rj*.',
 'EGAIV3 section8.8 original downloaded; SGA1VIII/IX; Serre1960 full article; SGA3 formal reedition.',
 ['EGAIV3','SGA1','Serre1960','SGA3VIIB'],
 'Published hypotheses separated exactly. Tentative site is not identified as a standard modern site without more data.')
family([633,635,636,637,638,639,640],
 'Local and global finite-coefficient duality; unramified annihilators; finite-flat p examples; Poitou–Tate; abelian Sha finiteness; November2026 status.',
 'Primary TateICM1963 report; Milne author notes; arXiv and recent system1 search; backward Shatz/Poitou/Tate references; Pro43 Artin–Milne/Suzuki primary checks.',
 ['Tate1963','MilneCFT2020'],
 'Tate2.1–2.5 and3.1–3.4 scope compared; finite-flat p assertions require later primary sources, not automatic extension of invertible-order theorem.',
 '2026 search hits on special BSD/Kolyvagin cases were inaccessible or did not settle general Sha. No general finiteness theorem is asserted. Pro43 supplies verified flat-coefficient sources.')
family(list(range(641,647)),
 'Integral/rational l-adic categories; stable lattices; model descent; finite-type field extension invariance of image Lie algebra; closed subgroup germs.',
 'Serre1968 full author-hosted reprint; EGAIV3 8.8.2–3; SGA3VIB10; topic searches on l-adic Lie monodromy.',
 ['Serre1968','EGAIV3','SGA3VIB'],
 'Finite-type extension scope verified; arbitrary infinite extension refuted by cyclotomic representation. Analyticity required for subgroup lemma.')
family([647],
 'Coherent Ext with support as colimit over infinitesimal thickenings; injective torsion submodule.',
 'SGA2VI2.3 directly opened; Stacks08XW statement/proof; original Pro125 comparison.',
 ['SGA2','Stacks08XW'],'Exact published theorem and draft proof agree after retaining coherence, quasi-coherence and noetherian hypotheses.')
family(list(range(648,655))+[680,681],
 'Every nonblank internal Hom and geometric Ext table cell on162–165; height-one restricted Lie; Cartier formal V; unipotent and mixed abelian extensions.',
 'SGA3VIIA7.2/8.1 andVIIB2.2/4.2; Oort publisher; Oort–Oda primary; arXiv Ribeiro–Rosengarten; CWI Hazewinkel–Oort reports; Oort official bibliography; Fanelli–Schröer primary; MilneAG15h; topic searches for Ext alpha_p/Ga and Ga/A.',
 ['SGA3VIIA','SGA3VIIB','Oort1966','OortOda1968','RibeiroRosengarten2026','HazewinkelOort1972a','HazewinkelOort1972b','FanelliSchroer2020','MilneAG2017'],
 'Cell-level findings in hom_ext_cells.tsv. Geometric Ext and internal sheaves kept distinct; difficult mixed cells not settled by opposite-direction formulas.',
 'Oort full book not obtained; exact table comparisons credited only when reproduced in opened primary paper or proved independently. The Sharma1967 backward reference is not marked read.')
family([655,656,657],
 'Primitive torsor extension structure; inverse/symmetry check; universal-homeomorphism invariance; primitive Artin–Schreier classes.',
 'Grothendieck ChevalleyExposé7 primary Numdam PDF; SGA1IX4.10; Ribeiro–RosengartenTheoremA; Serre1959 publisher and backward page reference.',
 ['GrothendieckChevalley1956','SGA1','RibeiroRosengarten2026','Serre1959'],
 'Perfect-field and normalized-rigidity assertions checked. Relative parenthesis on170 remains undeciphered.',
 'Serre p183 original edition not opened; inverse checked independently, not credited to unread page.')
family([658,659,671,672,673],
 'F/V classification; formal/algebraic gluing; completed Dieudonne ring; reasonable modules; local versus uniform nilpotence.',
 'SGA3VIIA/VIIB; Oort–Oda1968 p82; Cartier primary note; Gabriel1962 full downloaded paper; Oort official bibliography.',
 ['SGA3VIIA','SGA3VIIB','OortOda1968','Cartier1967','Gabriel1962'],
 'Finite/precisely completed categories established; unlabelled glued category and unspecified reasonable objects not thereby classified. Formula and quantifier checks explicit.')
family([660,661,662,663,664,665,666],
 'Fundamental theorem of coalgebras, Hopf finite-type approximation, arbitrary-ring projectivity/purity, Cartier character duality, pro-objects versus ordinary limits.',
 'SGA3VIB11.13 andVIIB2.2; MilneAGS VIII; Barr1974 primary; Kihara2016 publisher abstract; arXiv functorial Cartier duality; MathOverflow coalgebra discussion as lead; zbMATH attempt and bibliographies.',
 ['SGA3VIB','SGA3VIIB','MilneAGS2012','Barr1974','Kihara2016','AlvarezSancho2007','EGAIV3'],
 'Field and artinian-flat claims match exact theorems. General free-over-ring suggestion not settled by those sources; artinian-only full faithfulness refuted.',
 'zbMATH direct linked record returned403; no review read. The MathOverflow ring-generalization comment was retracted and is not theorem evidence. Kihara full subscription text not read.')
family([667,668,669,670],
 'Ind length categories; AB5 socle criterion; Gabriel/Krull localization; presumed abelian ind-affine extension category.',
 'Gabriel1962 original PDF downloaded, II§4 and IV/V; SGA3VIIB0.2; Serre1960; categorical topic searches.',
 ['Gabriel1962','SGA3VIIB','Serre1960'],'Ind reconstruction verified; weaker socle criterion independently refuted; undefined category remainsF.')
family(list(range(674,680)),
 'Picard of abelian torsor; Picard–Brauer Tate pairing; complete cohomology; tame symbol reciprocity; strict units; final Albanese-kernel independence.',
 'TateICM1963 primary; Deligne1991 primary Numdam paper; Ribeiro–Rosengarten author manuscript; Serre1959 contents; local-Jacobian source and backward Tate/Serre references.',
 ['Tate1963','Deligne1991','RibeiroRosengarten2026','Serre1959'],
 'Classical normalized pairings established. Arbitrary finite-cover complete cohomology and unqualified final choice independence not located as exact theorems; explicit change factor computed.')

seen=[]
with (out/'research_log.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['claim_id','date_utc','search_scope','channels_and_backward_routes','opened_reference_keys','hypothesis_match','limits'])
 for ids,scope,channels,refs,match,limits in families:
  for n in ids:seen.append(n);w.writerow([byid[n]['id'],'2026-11-19',scope,channels,';'.join(refs),match,limits])
assert len(seen)==len(set(seen))==len(claims) and set(seen)==set(byid)

refinements={
605:'(P+D)/P≅D/(P∩D), with no identification of the intersection itself with that quotient.',
608:'Local reciprocity identifies the profinite completion of K* with Gal(Kab/K), or works at finite norm quotients.',
613:'For discrete trivial Z over Fq, H¹=0 and H²=Q/Z.',
618:'Hom_R(M,−) commutes with filtered colimits when M is finitely presented over R; finite over R_p alone is insufficient.',
620:'Use d(u)=Θu−(−1)^|u|uΘ with Θ²=0 and compatible totalization signs.',
627:'Retain the specified topology and degree restrictions; no all-degree fppf vanishing for every connected linear group.',
645:'Finite-model Lie algebra can be retained under the defined model system; actual image Lie algebra need not survive arbitrary infinite extension.',
665:'Use the pro-object with its topology/continuous maps or the correct pro-Yoneda realization; artinian objects alone are insufficient.',
669:'In a locally noetherian Grothendieck category, finite-socle exhaustion implies local finite length; the AB5-only version is false.',
670:'Define the initial Gabriel radical using locally finite-length objects; identify it with the socle-stage union only under justified finiteness hypotheses.',
673:'Every element of U is killed by some F-power and p-power, with no exponent uniform on the entire union.',
678:'Take U to be strict units of residue1; reciprocity then gives orthogonality to UK*.',
650:'Hom(Ga,V) is the bilinear-character functor with zero geometric field points, not Ga; V=D(Ga).'}
(out/'refinements.json').write_text(json.dumps([{'id':f'RF-SA19-{n:03d}','refutes_or_refines':byid[n]['id'],'statement':s,'authorship':'This run’s explicit repair, not silently substituted into the transcription.'} for n,s in refinements.items()],ensure_ascii=False,indent=2)+'\n')

proofmap={601:'C1',602:'C1',603:'C1',605:'C1',606:'C1',608:'C1',612:'C2',613:'C3',615:'C3',616:'C5',617:'C4 (finite-presentation argument)',618:'C4',620:'C5',621:'C5',623:'C6',624:'C6',627:'C6',642:'C11',644:'C11',645:'C11',646:'C11',647:'C7',648:'C8',649:'C8',650:'C8',651:'C8',652:'C8',655:'C9',656:'C9',657:'C9',660:'C12',662:'C8,C12',663:'C8',664:'C12',665:'C12',666:'C12',669:'C13',670:'C13',672:'C14',673:'C14',677:'C15',678:'C15',679:'C15',680:'C16 in proofs_C16.md',681:'C16 in proofs_C16.md'}
comps={601,606,612,613,616,618,620,621,638,642,650,652,657,665,669,672,677,678,680}
events=[]
who='GPT-6 Astra Pro; effort not exposed; SA19/root/codex43'
for n,c in byid.items():
 events.append([c['id'],'2026-11-19',who,'used and rechecked in this run','Source formulation and exact hypotheses compared with opened literature; scope decision recorded in research_log.tsv. This event does not claim a full re-proof of cited literature.'])
 if n in proofmap:
  events.append([c['id'],'2026-11-19',who,'independent re-proof' if n in {605,608,613,618,620,621,623,624,642,645,646,648,650,652,655,660,662,663,664,665,669,670,672,673,677,678,681} else 'targeted proof check','See '+proofmap[n]+'. The recorded proof is restricted to its stated hypotheses; unresolved relative/category generalizations are not included.'])
 if n in comps:
  events.append([c['id'],'2026-11-19',who,'computation or formal certificate','Exact checks and complete stdout saved. Finite checks are distinguished from unrestricted proofs in proofs.md / proofs_C16.md.'])
 if n in refinements:
  events.append([c['id'],'2026-11-19',who,'refuted, with the refined statement’s id',f'Literal overbroad reading refuted or separated from valid scope; repair RF-SA19-{n:03d}. See the named proof and readings.tsv; ink not adjudicated.'])
for key in sorted({r for c in claims for r in c['refs']}):
 events.append([key,'2026-11-19',who,'carried as background without fault found','Opened source/access level and exact locator recorded in references.bib and research_log.tsv. Metadata-only sources support only metadata; no blanket proof verification claimed.'])
with (out/'CHECK_EVENTS.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)

links=[]
def link(kind,a,b,what,evidence,notes=''):links.append([kind,a,b,what,evidence,notes])
link('folder','43/37–38','43/199–200','Witt-series F,V laws and later Dieudonné normal forms','Both Codex passages read; sameFV=p relation, but one is a series convention and the later one uses semilinear module coefficients. CL612,672.')
link('folder','43/49–51','16/37–39','Indecomposable injectives, Matlis layers and attempted Hom continuity','Both transcriptions read. Cote16 states Matlis structure;43/51 adds a continuity step not implied by finite length over A_p. CL617–618.','MPL_16+47+54+44#9;MPL_16+47+54+44#10')
link('folder','43/71–76','43/102–106','Local Jacobian representing cohomology and realization/duality programme','Both endpoints read, including43/102 local Rosenlicht heading and explicit Ext comparison. Dimension/site differences retained; no automatic general identification. CL626.','MPL_43_094-142#1;MPL_43_094-142#30;MPL_43_094-142#32')
link('folder','43/89–90','43/135–140','Local duality and localization shifts','Both endpoints checked by Codex and Pro workstreams;43/136 has+1 while140 has an unshifted box. CL633 versus ProCL076–083.','MPL_43_094-142#44;MPL_43_094-142#46;MPL_43_094-142#48;MPL_43_094-142#49')
link('folder','43/125','43/161–162','Same coherent Ext-with-support colimit theorem','Both passages directly read. Coherence inserted on161; proof uses injectivity of J-torsion. Duplicate CL647 merged withCL054.','MPL_43_094-142#37')
link('folder','43/143–146','43/204–208','Tate finite/abelian duality and later Picard/local-symbol pairing sketches','Both endpoints read. Finite-module theorem and conditional abelian extension are not conflated with the unfinished geometric independence check. CL635–640,674–679.')
link('folder','43/162–165','43/188–189','Identity of the formal character object V','Both endpoints read;189 defines D(Ga), explaining nonzero values on nonreduced test rings. It also exposes the falseGa answer in one162cell. CL650,662–663.')
link('folder','43/173–184','43/197–202','Continuation of the formal/algebraic Dieudonné category problem','Both endpoints read;183 asks aboutgluing and finite-type modules;199 asks aboutthe action. No unwritten equivalence supplied. CL658–659,671–673.')
link('folder','43/133','54/5–7','F/V Cartier annihilators and reconstruction from A[p]','Both endpoints read.43has the finite-coefficient curve table,54explicitly asks whether its restricted-Lie extension follows from A[p]; modern comparison is Oda, not an extra theorem already on43.','MPL_43_094-142#61;MPL_43_094-142#63;MPL_16+47+54+44#67;MPL_16+47+54+44#69')
link('published work','43/161–162 and43/125','SGA2, ExposéVI, Théorème2.3 (originalp76; reeditionpp59–60)','Coherent Ext with support as a filtered colimit','Both manuscript occurrences and full published statement/proof opened. Hypotheses exactly matched.','MPL_43_094-142#37')
link('published work','43/151–152 and191–192','EGAIV3,8.8.2–8.8.3,pp28–33','Finite-presentation descent of schemes, morphisms and finite diagrams','Original PDF downloaded; theorem and proof locally read. Finite type alone needs noetherian base.')
link('published work','43/185–192','SGA3I,ExposéVIB,Proposition11.13','Affine group scheme over field as limit of algebraic quotients','Exact published proposition opened and matched; transitions faithfully flat; field hypothesis retained.')
link('published work','43/163','SGA3I,ExposéVIIA,7.2 and8.1.1–8.1.2','Restricted-Lie adjunction and height-one classification','Exact published statements opened. Finite-free Lie source and characteristicp conditions retained.')
link('published work','43/188–189','SGA3I,ExposéVIIB,2.2.1–2.2.2','Formal Cartier duality with affine groups','Published proposition opened, including artinian-base/topological-flatness hypotheses; editorial expansion of reedition distinguished.')
link('published work','43/169','SGA1,ExposéIX,4.10','Étale invariance under radicial universal homeomorphism','Exact published corollary and its extension note opened. Does not imply invariance of all flat infinitesimal coefficients.')
link('published work','43/170','Grothendieck,Chevalley seminar1956–1958,Exposé7,pp8–9','Primitive Artin–Schreier polynomial calculation','Both endpoints read. The seemingly unrelated title really contains the cited argument; perfect-field scope retained.')
with (out/'links.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['kind','from','to','what','evidence','note_ids']);w.writerows(links)
print(json.dumps({'claims_searched':len(seen),'research_families':len(families),'events':len(events),'refinements':len(refinements),'links':len(links)}))
