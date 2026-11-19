"""Write explicitly reviewed links; do not infer a link from shared keywords."""
from pathlib import Path
import csv,json
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[1]
items={i['id']:i for i in json.loads((B/'items.json').read_text())}
L=[];P=[]
A='MPL_64_078-115_transcription.tex';Z='MPL_64_116-157_transcription.tex'
E='MPL_64_002-039_transcription.tex';F='MPL_64_040-077_transcription.tex'
def link(kind,fr,to,what,evidence,ids):
    ns=sorted(set(s for n in ids for s in items['SA16-'+str(n)]['sources']))
    x=dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=';'.join(ns));L.append(x);return x
def folder(fr,to,what,ids):
    return link('folder',fr,to,what,'Both supplied transcript endpoints read directly in this run; this is a passage comparison, not an inherited proof certificate.',ids)
def pub(fr,to,what,ids,scope):
    return link('published work',fr,to,what,'Manuscript endpoint and the indicated published passage both opened. '+scope,ids)
def project(ids,target,what,run_names,notes_locator,reported_status='No change to reported external status'):
    fr='; '.join(items['SA16-'+str(n)]['lines'] for n in ids)
    x=link('our projects',fr,target,what,
        'Current manuscript passage and supplied note report checked. '+notes_locator+'. Original external endpoint absent from this topic archive; its mathematical assertions are not verified here.',ids)
    P.append(dict(x,run_names=run_names,reference_availability='Supplied note report available; original target unavailable',
        checked_here='Current passage and exact note-level attribution; any independent local computation is separately identified in the item and check events.',
        not_checked='Original project passage, its complete hypotheses, proofs, certificate files and current project status.',reported_status=reported_status))

folder(E+':260–365 (cote64 scans8–9)',A+':6–31 (scan78)',
       'The earlier combinatorial square and its orientation data underlie the standard square Q0 and its four rotations. The late passage specifies side endpoints rather than the polynomial example introduced by an earlier run.',[501,502,552])
folder(F+':816–862 (scans75–76)',A+':6–31,65–83 (scans78,80)',
       'The promise to specify Q0 is fulfilled at78 by sides s_i=v_i−u_i and s_i′=i s_i; the scalar twist is then used at80. The explicit s⁴=−4 model remains a separate reconstructed example.',[501,502,503,552])
folder(E+':945–1132 (scans26–28)',A+':382–391 (scan93); '+Z+':76–125 (scans117–118)',
       'The rank-two Z/4 module, its three fibres and sum-zero torsor P_M are the combinatorial predecessor of choosing halves of the three nonzero two-torsion points with zero sum. This identifies the datum, not the unfinished pinning scale.',[538,552])
folder(F+':638–732 (scans66–69)',A+':382–391 (scan93); '+Z+':76–125,222–289 (scans117–121)',
       'The relative-level-four construction recurs as the same requested canonical map to Legendre pinning. The later coordinate conditions still postpone the tensor-square normalization.',[516,538])
folder(F+':744–811 (scans71–74)',A+':395–464 (scans94–95)',
       'The earlier tangent-norm/Kummer category assertion leads into the later description by a square root of the quotient tangent line. The elementary μ2-torsor equivalence alone does not prove the full elliptic-category identification.',[513])
folder(F+':348–418 (scans54–57)',A+':108–124,1332–1353 (scans81–82,115)',
       'The four-pointed line and its Klein action recur as the elliptic quotient by negation and the three descended nonzero-two-torsion translations. The quotient coordinate changes must be specified.',[520,537,554])
folder(F+':545–631 (scans63–65)',A+':1332–1353 (scan115); '+Z+':4–49 (scan116)',
       'Earlier f_2^t is descended multiplication by two. The later σ_i is descended translation by a two-torsion point. Their branch permutations connect them, while the maps have different degrees and must not be identified.',[537,554])
folder(F+':228–343 (scans48–53)',A+':65,162–175 (scans80,84–85)',
       'The characteristic-five bare-octahedron exception and the characteristic-three collision of equianharmonic fixed parameters are different phenomena. The full cote supplies the previously unavailable early endpoint; pairing structure matters in the former.',[512,553])
folder(A+':382–391,593–706 (scans93,98–100)',Z+':76–125,222–289,419–484 (scans117–121,125–126)',
       'The announced level-four map and equation73 continue as equations83b/83c. The loose cyclic-difference calculation determines a line; it does not settle the explicitly deferred square scale.',[516,538])
folder(A+':1100–1178 (scans110–111)',Z+':59–117 (scans117–118)',
       'The determinant proposition is cited in the half-division calculation. Distinctness was inserted in the original proposition and is satisfied later because the three doubles are different.',[534])
folder(A+':1332–1353 (scan115)',Z+':4–49,101–117 (scans116,118)',
       'The Möbius involution continues across the package boundary. Its fixed-point radical supplies a direct check of the later sign-defective expansion.',[537,561])
folder(Z+':522–930 (scans131–141)',Z+':934–1214 (scans143–149)',
       'The first complex-structure draft is replaced by a holomorphic period-family construction. The author’s orientation withdrawal and the antiholomorphic first formula must remain visible in the comparison.',[562,563,564,565,568])
folder(Z+':911 (scan140)',Z+':1231–1259 (scan150)',
       'The first outer-action formulation contains the false rank-one abelianization parenthesis. The second repeats the orientation-preserving outer-action statement without that parenthesis; it does not explicitly retract it.',[569,570])
folder(Z+':1432–1482 (scan155)',Z+':1527–1575,1595–1615 (scans156–157)',
       'The local quadratic-order test feeds the global normalization problem and the final tangent-cone scratch calculation. Normality, generic étaleness and ordinary-node type are separate assertions.',[580,581,582,583,584,585,586,587,588])
folder('MPL_62_002-050_transcription.tex:1083–1127,1232–1256 (cote62 scans42–44,50)',A+':41–58,124–154,269–305 (cote64 scans79,82–83,90–91)',
       'A projective line with étale trisection and a disjoint section gives the same three-label/anharmonic geometry underlying J,t and the S3 pinning action. Cote62’s normalized invariant must not be silently replaced by the standard j coordinate.',[506,507,513,520])
folder('K63-02_transcription.tex:205–229,247–272,293–318 (cote63 scans96–100)',A+':162–175 (cote64 scans84–85); '+Z+':1432–1482,1595–1615 (scans155,157)',
       'Both folders ask about exceptional elliptic behaviour in residue characteristics two or three and tangent multiplicities. Cote63’s distinct/equal tangent retraction is not settled by cote64’s one-dimensional quadratic-order test; deformation base and divisor must first be identified.',[512,582,565])

pub(A+':65–83,395–464 (scans80,94–95)',
    'SGA1 VIII, Theorem1.1, Remark1.12 and §2 opening; https://arxiv.org/pdf/math/0206203 (recomposition pp153–158)',
    'Faithfully flat descent for lines and tensor structures supplies the exact published background for contracted-product twists and square-root torsors.',[503,513],
    'Statement and its tensor-compatible extension read; no claim to have audited the full general descent proof.')
pub(A+':175–193 (scans85–86); '+Z+':934–970 (scans143–144)',
    'GrothCartanI §2, Definition2.3 and Lemma2.4; https://www.numdam.org/item/SHC_1960-1961__13_1_A4_0.pdf',
    'The Jacobi/Torelli terminology and level-structure framework predate these pages. The published general theorem assumes genus≥2, so it is not itself a genus-one rigidification proof.',[518,562],
    'Hypothesis and terminological scope checked directly.')
pub(Z+':522–544,934–1010 (scans131,143–145)',
    'GrothCartanX introduction17-01; https://www.numdam.org/item/SHC_1960-1961__13_2_A4_0.pdf',
    'The published 1961 introduction explicitly describes the genus-one lattice-family model later reconstructed in these sheets.',[555,562],
    'The earlier text leaves the genus-one construction to the reader; no full proof transfer is claimed.')
pub(Z+':1488–1550 (scan156)',
    'EGAIV2 Theorem5.8.6, printedp108; https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf',
    'R1 plus S2 upgrades the asserted height-one normality to global normality of the quadratic hypersurface, removing the proposed finite exceptional nonnormal set.',[583,585],
    'Entire theorem and proof read; the hypersurface application is independently proved in proof_notes.md.')
pub(Z+':934–1010,1231–1259 (scans143–145,150)',
    'SGA1 XII, Theorem5.1; https://arxiv.org/pdf/math/0206203 (recompositionp251; originalp333)',
    'The published Riemann existence theorem is the finite-cover comparison relevant to moving from complex analytic geometry to finite étale covers. It does not by itself determine any arithmetic outer image.',[575,576,577],
    'Statement and beginning of proof opened; only the stated comparison is used.')

# External project links remain in their own table as well as the prescribed combined schema.
project([507,539],'LM_140-2_text.tex scans527–529; LM_140-2_notes.md LM_P053 S06–S09',
    'Compare the reported normal complement H=ker(εβκ) and its order-twelve quotient with the verified fibre product D3′. The proposed λ(1−λ) twist requires a family, branch-order and monodromy comparison.',
    'La Longue Marche; B5; LM_P053','MPL_64_078-115_notes.md entries B5-03a/b',
    'Normal-complement statement carried only as the supplied note report; its original proof and S06 outer-map qualification remain unverified here.')
project([538,576],'LM_140-2_text.tex scans517–519,527–528,533,570; LM_140-2_notes.md R22,R24,R28–R29; LM_140-3_text.tex §38 scan20 and §39 scans28–30',
    'The finite level-two/four data and reduction of an integral Torelli frame supply geometric input for B5. They do not identify every projective kernel or prove GT₀ preservation.',
    'B5; LM2 C.d1; LM_P053; LM_P061','MPL_64_078-115_notes.md B5-02; MPL_64_116-157_notes.md L01,B04,B05')
project([537,575],'MPL_149_091-136_notes.md RN099-03,RN101-01,RN101-04,RN103-05 (scans099–103); LM_140-2_text.tex §37 scan517',
    'The analytic q chart and its elementary unipotent monodromy are present. Extension over q=0, a Tate arithmetic model, residue action and an inertia splitting remain separate requirements.',
    'B5; EXIT_TOWER E.24; cote149 research notes','MPL_64_078-115_notes.md B5-01; MPL_64_116-157_notes.md B01,B03')
project([537,566],'LM_140-3_text.tex §39 scans024–026, especially025; LM_140-3_notes.md LM_P06110–13 and own noteE',
    'The determinant-minus-one matrix τ∞ converting action conventions differs from the reported arithmetic inertia source T∞. The finite character does not restore an outer action’s lost full unit multiplier.',
    'LM2 C.r2; B5; LM_P061','MPL_64_078-115_notes.md B5-01b; MPL_64_116-157_notes.md B02',
    'The reported multiplier qualification is preserved; no unseen assertion is repaired or reversed.')
project([540],'LM2_CONGRUENCE_ROWS.md C.d1,C.r1,C.r2,C.r3; LM_140-3_text.tex scans022–026 and176–178',
    'Finite χ4, a geometric modular action and an arithmetic outer congruence action have different domains and targets. None of the current formulas yields the full arithmetic image or all projective kernels.',
    'LM2 C.d1; LM2 C.r1–C.r3','MPL_64_078-115_notes.md B5-03c; MPL_64_116-157_notes.md B06',
    'C.d1 reported known/unreviewed; C.r1 and C.r3 reported proved/unreviewed; C.r2 reported refuted/unreviewed. These are quotations of the register status, not current validation.')
project([541],'notes/RESULTS_STATE.md LM4 D.12 and reported D.29 qualification',
    'Finite geometric stabilizers and descended two-torsion translations do not classify arbitrary profinite torsion or establish geometric realizability of a peripheral system.',
    'LM4 D.12; LM4 D.29','MPL_64_078-115_notes.md B5-04',
    'D.12 remains open as reported; the reported D.29 qualification is neither re-proved nor overturned.')
project([542,538],'notes/RESULTS_STATE.md EXIT_TOWER E.24; cote143 §9 scans29–33 as reported',
    'Arithmetic orientation data do not specify the missing arithmetic outer target, index or boundary-inertia tests. The truncated target is not reconstructed from analogy.',
    'EXIT_TOWER E.24','MPL_64_078-115_notes.md B5-05; MPL_64_116-157_notes.md B04',
    'Open in the supplied report; no status change.')
project([543,538],'notes/RESULTS_STATE.md LM4_SUCCESSOR B.38 (B.5)',
    'The current pages name levels two and four and postpone a normalization. They do not calculate K5,K7,K11 or a compatible all-level family.',
    'LM4_SUCCESSOR B.38','MPL_64_078-115_notes.md B5-06; MPL_64_116-157_notes.md L01,L04,B04',
    'The relevant higher-kernel rows remain open as reported.')
project([515,556],'notes/RESULTS_STATE.md LM6 A.22; LM7_PUSH E.3; LM_140-3_notes.md scan009 special-j lead',
    'Choosing a primitive fourth root throughout a family is not a CM restriction. Finite special stabilizers and the unnamed exceptional parameter do not compute the external CM coset or image.',
    'LM6 A.22; LM7_PUSH E.3','MPL_64_078-115_notes.md R14,RC12g; MPL_64_116-157_notes.md T12,T14,H06',
    'Open in the supplied report; no status change.')
project([544,545,546,578,579],'README.md S20; SECTIONS_STATE.md §11b lines218–226 and §21 lines370–379; cotes93 and159',
    'Fibre derivations, tangent frames and period local systems are distinct from a specified base connection. Independent Picard–Fuchs, Hasse and p-curvature calculations give comparison tests, with no historical identification of the absent connection text.',
    'S20; Les Dérivateurs; MPL_93 P09','MPL_64_078-115_notes.md RC01,RC13a/b; MPL_64_116-157_notes.md S01–S06',
    'S20 remains an unchecked planning hypothesis in the report, not confirmed or refuted by this fragment.')
project([547],'MPL_93_002-046 P09; notes/RESULTS_STATE.md P09 row',
    'The supplied note gives only the future-comparison title. Branch, orientation and tangent-square data are possible inputs, but no unseen test list is inferred.',
    'MPL_93_002-046 P09','MPL_64_078-115_notes.md RC02a')
project([548],'MPL_93_002-046 E14',
    'The visible distinction between a coarse parameter and a stack with stabilizers warns against equating the two in deformation theory. No absent deformation equation is identified.',
    'MPL_93_002-046 E14','MPL_64_078-115_notes.md RC02b')
project([549],'MPL_93_002-046 E16',
    'The reported phrase about smallest orders supplies no quantifiers. It cannot be identified with pole order or an exceptional stabilizer from the current pages.',
    'MPL_93_002-046 E16','MPL_64_078-115_notes.md RC02c')
project([550],'MPL_93_002-046 C29',
    'A tangent-square line is a possible comparison object for the reported first-order datum, but actual deformation spaces and the map on the other side are missing.',
    'MPL_93_002-046 C29','MPL_64_078-115_notes.md RC02d')
project([551],'MPL_93_002-046 C35',
    'The visible determinant correction is not the reported withdrawal of cote93 Problem1. Nothing here reopens that absent objection.',
    'MPL_93_002-046 C35','MPL_64_078-115_notes.md RC02e',
    'Withdrawn in the supplied report; no status change.')
project([537],'MPL_142_094-122_notes.md B01, cote142 scan108; MPL_147_003-047_notes.md AppendixB',
    'The explicit Möbius involution gives a geometric comparison lead for the reported Klein/four-point material. The other manuscripts and their proof claims are absent.',
    'Cote142 B01; cote147 AppendixB; LM4 D.12','MPL_64_078-115_notes.md ALG08')
project([564,565,566],'LM_140-3_notes.md R30–R34, scans19–20; LM_140-3_text.tex §38',
    'Orientation, conjugation and right/left framing formulas need the same declared basis conventions before any family identification. The current first draft is corrected by its own later draft.',
    'LM_P061; B5','MPL_64_116-157_notes.md T03–T05')
project([567],'LM_140-2_text.tex scans261–263',
    'The exact action on lattice translations supplies a discrete formula for the reported universal-family group extension. It does not prove an arithmetic-image assertion.',
    'La Longue Marche; EXIT_TOWER E.24','MPL_64_116-157_notes.md T06')
project([577],'LM_140-2_notes.md second-pass own noteD on scan320; LM_140-3_text.tex scan24 equation7; notes/RESULTS_STATE.md EXIT_TOWER D.19 and LM6 C.17',
    'The full nonabelian procongruence action and the homological congruence completion are different. The modern Bux–Ershov–Rapinchuk theorem answers the precise low-genus literature comparison, without validating the absent broader register statement.',
    'EXIT_TOWER D.19; LM6 C.17; LM2 C.d1','MPL_64_116-157_notes.md B07',
    'Broader genus and cutting-factor claims remain carried context, with no inferred contradiction.')
project([552,553,554,513,516,555,556,590],
    'context/hua_project/64.modern.tex; reported sections I–VI, lines233–2118; 64-legendre-pinning-moduli finding',
    'The earlier modernization supplied antecedent and continuation leads. Available cote64 endpoints are now read directly; the original modernization file and its Lean certificates are not supplied. The separately opened public November2026 preprint is not silently treated as that earlier version.',
    'Hua modernization project; 64-legendre-pinning-moduli; B5; S20',
    'MPL_64_078-115_notes.md RC12a–g; MPL_64_116-157_notes.md editorial cover discrepancy',
    'Earlier finding reported as candidate conjecture/new-to-us intake; no inherited proof certificate.')
project([558],
    'Earlier records/research_connections.md; research/connections_hua.md; root_context_queries.json; CHECK_EVENTS.tsv; scripts and wrappers listed in MPL_64_078-115_notes.md final record',
    'The prior run’s tests, source hashes and wrappers were not supplied. Their checks are not inherited; this run’s executable identities, proofs and check events are newly recorded.',
    'MPL_64_078-115 prior Pro research run',
    'MPL_64_078-115_notes.md entry63, physical lines464–487',
    'Documentary provenance only; no mathematical verification inherited.')

cols=['kind','from','to','what','evidence','note_ids']
with (B/'links.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader();w.writerows(L)
pc=cols+['run_names','reference_availability','checked_here','not_checked','reported_status']
with (B/'our_project_links.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=pc,delimiter='\t');w.writeheader();w.writerows(P)
with (B/'progress.log').open('a') as f:
    f.write(datetime.now(timezone.utc).isoformat()+'\tSTAGE5\t'+str(len(L))+' checked-attribution links, including '+str(len(P))+' external-project leads with unavailable original endpoints explicitly identified.\n')
print('Links',len(L),'folder',sum(x['kind']=='folder' for x in L),'published work',sum(x['kind']=='published work' for x in L),'our projects',len(P))
print('No absent original project endpoint was treated as read or proved.')
