"""Serialize individually read and manually adjudicated project endpoints.

The register's statuses are reported, never independently endorsed. Numbered
source headings are navigation only. No matching or mathematical verdict is
inferred from a keyword, status label, or heading by this program.
"""
from pathlib import Path
import csv, json, collections, hashlib, datetime, re

P=Path(__file__).parent
B=Path('/workspace/scratch/4017236f14bf')
NAV=json.loads((P/'context_navigation.json').read_text())
SOURCE='sources/notes/pro/MPL_156-1+156-2_notes.md'
N69='prior_context/extracted/notes/RESULTS_STATE.md'
D69='prior_context/extracted/DOSSIER_STATEMENTS_WITH_STATUS.md'
N138='prior_context_138/extracted/notes/RESULTS_STATE.md'
PREFIX='MPL_156-1+156-2#'
ROWS=[]

def add(key,target,nums,status,loc,statement,recorded,relation,limit='',extra=None):
    nums=sorted(set(nums)); occurrences=[]
    for n in nums:
        if n==117:
            for line in (extra or {}).get(117,[]):
                occurrences.append({'note_id':PREFIX+str(n),'line':line})
        elif n==118:
            for line in (extra or {}).get(118,[]):
                occurrences.append({'note_id':PREFIX+str(n),'line':line})
        elif n in [115,121]:
            for line in (extra or {}).get(n,[]):
                occurrences.append({'note_id':PREFIX+str(n),'line':line})
        else:
            hits=[r for r in NAV if r['note_id']==PREFIX+str(n)]
            assert len(hits)==1,(key,n)
            occurrences.append({'note_id':PREFIX+str(n),'line':hits[0]['line']})
    ROWS.append({'id':'PL-SA21-'+key,'target':target,
      'note_ids':[PREFIX+str(n) for n in nums],
      'source_occurrences':occurrences,'match_status':status,
      'checked_target_locator':loc,'what_target_actually_says':statement,
      'recorded_status':recorded,'relation_to_sa21':relation,
      'limits':limit or 'This is verification of the cited project endpoint only; its mathematical claim has not been independently proved or reclassified in this audit.'})

MISS='missing_target'
BOUNDED='No exact target in the two recovered contexts, including all 106 textual files searched. Other occurrences of an unqualified short ID belong to different runs. The original package-48 register and the named source return are unavailable; absence here is not absence from the project.'
def missing(key,target,nums,reported,relation,loc='search_manifest.json; candidate_summary.tsv',extra=None):
    add(key,target,nums,MISS,loc,'The named target is not present in the recovered selections.',reported,relation,BOUNDED,extra)

missing('WG2-B15','WG2 B15 (§1.2)',[1,7,8,16,19,22,25,30,33,35,36,37,38,39,40,41,52,55,60,65,66,68,69,70,85,87,95,96,99,101,103,104,117,118],
 'Unchecked planning entry, according to the SA21 notes.',
 'Proposed finite-cutting/pro-object/workshop bridge. Notes #38/#41 name the WG2 analogy generically in the body and B15 in search metadata; they are retained as qualified occurrences.',
 N69+':513–515; '+N138+':440–449; both README files:1–31',
 {117:[1000,1008,1016,1040],118:[1134]})
missing('WG2-3.1-2','WG2 §3.1 #2',[1,8,22,37,39,99,117],
 'Unchecked planning entry, according to the SA21 notes.',
 'The proposed categorical/refinement bridge is not supplied by the local filtering axioms.',
 N69+':513–515; '+N138+':440–449',{117:[1008]})
add('README48','Original package-48 README, “The guess”',[16,66,85,87,96,99,101,103,104,107,113,114,115,117,118,121],
 'different_context_version','prior_context/extracted/README.md:1,17–38; prior_context_138/extracted/README.md:1,13–38',
 'The recovered READMEs concern package 69 (Pursuing Stacks) and package 102 (arithmetic of maps). Neither contains the cited SA21 finite-cutting/pro-object/workshop guess.',
 'Original proposal reported by SA21 notes as an unchecked title-based guess.',
 'Retain the historical lead as a report of the SA21 notes; do not replace it by either recovered README.',
 'The SA21 notes identify their original context at lines1192–1196: README dated12November with14November addition, package48 RESULTS_STATE built14November18:02UTC. Those exact two files remain missing.',
 {115:[939,941],117:[1000,1008,1016,1040,1116],118:[1134],121:[1192,1196]})
add('STATE48','Original package-48 RESULTS_STATE (14November18:02UTC)',[115,121],
 'different_context_version',N69+':1–8; '+N138+':1–8',
 'The recovered registers are package-specific selections built17November03:18 and03:20UTC. They share run summaries but have different selected entries.',
 'Mixed earlier-run claims, first-pass notes, intake readings and unchecked plans.',
 'Each surviving named endpoint is checked below; register-level status never certifies a missing individual result.',
 'An apparent ordinal mismatch is explained by counting ## as well as ### headings: the selected SA21 §122 is current note#116 plus six ## headings. It is not evidence by itself of changed note content.',
 {115:[939,941],121:[1194,1196]})
missing('R121-08','MPL_121_049-073+153+155 R121-08',[2,3,18,21,64,75],
 'First-pass lead at121/050–052, compared with147/179–180,185–190, as reported by SA21 notes.',
 'Incidence data versus stratified attachment data; no identification with interval networks.',
 N69+':503,552 (bibliography/source filename only)')
add('STRATA-A4','STRATA A.4',[4,5,9,23,31,38,45,64,65,69,105,106],
 'exact_id_excerpt',N69+':454',
 'Finite minimum-vertex realizations have contractible strata, opposite-poset exits and the stated ordinary constructible-sheaf category. Anchor: Lead1 finite geometric clause.',
 'Proved (return’s claim).',
 'Confirms the finite-poset comparison reported by the SA21 notes. It does not extract a poset from a réseau or prove the manuscript’s interval axioms.',
 'The selected row abbreviates the coefficient/sheaf statement. BISITE G.10 supplies a fuller related finite dictionary; A.12 for every small poset is not present.')
add('BISITE-G10','BISITE G.10',[4,9,31,45,105],
 'exact_return_row',D69+':223; '+N69+':461',
 'For finite P, label |NP| by its least positive-coordinate vertex and give P downset opens. The return claims continuity, contractible conical strata, exit∞ category P^op, and P-constructible sheaves equivalent to Fun(P^op,C), for spaces, compactly assembled coefficients and stable presentable coefficients; inverse image from the finite Alexandrov space identifies that subcategory.',
 'Proved (return’s claim; DOSSIER header5 explicitly denies a full-effort review of these rows).',
 'A comparison model for a given finite poset. No theorem identifies all SA21 figures or ateliers with this special realization.')
missing('STRATA-A12','STRATA A.12',[5,23,69,105,106],
 'Proved for every small poset, as reported by SA21 notes.',
 'The infinite-poset assertion must not be inferred from the recovered finite A.4/G.10 rows.')
missing('MPL150-N18','MPL_150_044-084 N18',[6,13,20,51,53,57,59,61,62,63,66,71,72,83,84,91,94,95,100,110,112],
 'First-pass lead at150/077,081–084, as reported by SA21 notes.',
 'Retention of attachment maps and pieces in reconstruction; the SA21 finite-cut chain keeps its gluing homeomorphisms.',
 N69+':509,554 (bibliography/source filename only)')
add('STRATA-0.1','STRATA 0.1',[10],
 'exact_id_excerpt',N69+':476',
 'Presheaf variance uses downset opens and minimum-vertex stratification; geometric exits have the opposite variance. Anchors I ms1–9; XII ms59–63.',
 'Proved (return’s claim).',
 'Confirms the notes’ warning that the convention belongs to a different sheaf comparison and cannot determine the orientation of an SA21 biorder.')
missing('MPL150-Q1b','MPL_150_001-043 Q1b',[11,24,26,46,47,49,56,58,59,78,80,81,90,117],
 'First-pass conical-neighborhood lead at150/012–015,022–023, compared with147/140–142.',
 'Related conic germs; no identification with SA21’s contraction-and-cone regular immersion.',
 N69+':505,553 (bibliography/source filename only)',{117:[1024]})
add('INTAKE-13.2','INTAKE 20261114 §13.2',[11],
 'exact_id_excerpt',N69+':491',
 'The intake locates uncertain “tubulure”/“ombre” only at149/133, absent from150/001–043 and147/138–190; it starts a list of neighboring definitions at150/012–015,022 before the excerpt ends.',
 'Intake reading, Claude Fable5.2 effort high; not a referee verdict.',
 'Confirms the narrow terminology lead. It does not make those notions identical to a regular immersion in SA21.',
 'The excerpt ends with an ellipsis; no omitted list, conclusion or proof is reconstructed.')
missing('MPL150-Q4b','MPL_150_001-043 Q4b',[12,48,67,97],
 'First-pass compact Hauptvermutung lead at150/037–039.',
 'Different compact-tame comparison; does not settle the finite-polyhedron endpoint classification in SA21.',N69+':505,553')
missing('MPL151-Q4-02','MPL_151_032-075 Q4-02',[12,67,87,97,98],
 'First-pass compact-polyhedral-object comparison at151/044–045,059–061.',
 'The hypothesis is separately specified; it does not rule out the Cantor examples for the literal SA21 definitions.')
missing('MPL148-R29','MPL_148_029-072 R29',[13,15,17,43,44,60,89,94,101,102,117],
 'First-pass marked-circle cutting lead at148/058–059,061.',
 'A different cutting/erasure problem; no same counterexample or common-refinement theorem is verified.',extra={117:[1032]})
missing('MPL150-N39','MPL_150_044-084 N39',[14,50,74,79,80,86,88,93,108,113],
 'First-pass component versus normal-link/prospace lead at150/072,077; comparisons147/180,149/134.',
 'SA21 rives retain a Boolean germ invariant, which cannot be identified with full link information from the missing entry.',N69+':509,554')
missing('EXIT-P4e','EXIT_ONE_TYPE P4e',[14,54,75,77,83,84,88,93,96,100,112,113],
 'Proved, return’s claim, at149/133 as reported by SA21 notes.',
 'Information-loss caution for coarse maquettes; no precise P4e hypotheses or proof are present.',N69+':177–178,450,462,531,557 (other exact EXIT rows and run-level summary only)')
missing('MPL148-R34','MPL_148_029-072 R34',[15,44,89,117],
 'First-pass cutting/erasure lead at148/055,061,064.',
 'Terminological and geometric comparison with maille/birive, not identity of constructions.',extra={117:[1032]})
missing('MPL150-Q9','MPL_150_044-084 Q9',[26,48],
 'First-pass lead on unspecified tame axioms at150/073–076.',
 'SA21’s “modérée” qualification requires its own hypotheses; the missing lead cannot fill them.',N69+':509,554')
missing('BISITE-D11','BISITE D.11',[27,28,29,38],
 'Proved, return’s claim, on finite-poset properness with lifting conditions, as reported by SA21 notes.',
 'Does not justify arbitrary restriction of a réseau; the supplied DOSSIER contains other BISITE parts, not this exact D.11.')
missing('RESIDUE-H1','RESIDUE H.1',[27,28,29],
 'Proved, return’s claim, on finite-poset properness/lifting conditions, as reported by SA21 notes.',
 'A comparison about different hypotheses; no exact H.1 row survives in either context.')
add('PATHS-E10','PATHS E.10',[32],
 'exact_return_row',D69+':104',
 'Components of the marked subcategory alone do not specify a stratification whose exit paths compute general localization mapping spaces.',
 'Refuted (return’s claim), meaning the proposed sufficiency assertion was refuted.',
 'Confirms the notes’ scope distinction: connected components of an SA21 model do not furnish exit-path mapping data.')
missing('MPL150-N35','MPL_150_044-084 N35',[34],
 'First-pass lead at150/077, compared with147/180.',
 'Methodological comparison to orientation transport, with no exact orientation theorem supplied.',N69+':509,554')
add('STRATA-C8','STRATA C.8',[34,61,63,91],
 'indirect_id_mention',N69+':510',
 'A selected cross-reference in MPL_150_085-099+151_001-031 §106 names STRATA C.1,C.3,C.5,C.6,C.8 and mentions spans, face maps, bands and neighborhoods for coherent gluing. It does not give C.8’s theorem.',
 'The SA21 notes report C.8 as Proved; the recovered occurrence is only a first-pass cross-reference.',
 'Retain a lead about gluing coherence; no exact enhanced-coefficient pullback theorem can be read from this occurrence.',
 'Exact ID occurs but exact statement/hypotheses are missing. Do not substitute PATHS C.8 or RESIDUE C.8, which are different rows.')
missing('RESIDUE-H2','RESIDUE H.2',[42,111],
 'Refuted, return’s claim, for an unmodified extension from posets to categories with nonidentity idempotents.',
 'The missing obstruction cannot be replaced by the unrelated POLES H.2 row in the recovered register.')
missing('MPL150-Q2','MPL_150_044-084 Q2',[45,92,103,109,114],
 'First-pass realization/postponement lead at150/073–084, especially074,076–077,084.',
 'A broader reconstruction program with geometric choices; it supplies no verified SA21 realization functor.',N69+':509,554')
add('EXIT-P1a1','EXIT_ONE_TYPE P1a1',[47,74,79,81,86,88,90,108],
 'indirect_id_mention',N69+':490,494',
 'INTAKE §13.3 calls P1a1 the claim that normal-link homotopy fibres give every exit mapping space. The expert excerpt stresses at150/039 that fibrancy of each map is too weak and requires the whole stratified family over a fixed stratum to be locally trivial.',
 'P1a1 is reported by SA21 notes as Proved (return’s claim); recovered documents are an intake and an expert reading, not the exact result row.',
 'Confirms that the earlier discussion distinguishes link data and a whole-family hypothesis; it does not verify the full P1a1 theorem or its quantifiers.',
 'Both excerpts are truncated. The run-level “0 wrong” review at531 is not a substitute for opening the missing P1a1 return/proof.')
add('MPL147-69','MPL_147_138-190 §69 = note151-33',[53,62],
 'exact_source_note','prior_context_138/extracted/MPL_147_138-190_notes.md:286–288',
 'The earlier run proposes organizing relative construction pieces at147/161–163 by exit-path data retaining directed specialization and homotopies. It compares the mixed recollement topos with its galoisian reflection and leaves identification of germ flags with exit paths and verification of conical/tame hypotheses as tasks.',
 'Own idea of the first-pass run; confidence medium; not a proved reconstruction theorem.',
 'Matches the SA21 notes’ building-piece/attachment comparison and its limited status.',
 'Register §69 counts both ## and ### headings: this is the65th ### plus four ## headings, verified mechanically. The original147 scans/transcription are not in this recovered archive; only the earlier note endpoint is checked.')
missing('MPL151-Q4-03','MPL_151_032-075 Q4-03',[73],
 'First-pass isotopy/homeomorphism comparison at151/044–045,059–061.',
 'Different from the author-withdrawn endpoint-inclusion equivalence in SA21.')
missing('RESIDUE-A7','RESIDUE A.7',[77],
 'Proved, return’s claim; finite-fibre sphere obstruction, no manuscript anchor reported.',
 'Could constrain coarse finite models, but the exact hypotheses and statement are not in the recovered return selection.')
missing('MPL148-R39','MPL_148_029-072 R39',[76,117],
 'First-pass withdrawn/unpursued cancelled-skeleton lead at148/067.',
 'Separate cancelled gluing proposal; no identification with SA21’s cancelled duplicate.',extra={117:[1040]})
missing('INTAKE-13.6','INTAKE 20261114 §13.6',[57,78,82,91,109],
 'Intake reading, not referee verdict, on cote150 reconstruction/attachments.',
 'Neighboring §13.2–13.4 excerpts do not supply §13.6.',N69+':488–495')
missing('MPL121-Q4.2','MPL_121_001-048 Q4.2',[106],
 'First-pass compact-polyhedral comparison at121/030–035.',
 'Distinct from Clader’s inverse-sequence output; the precise comparison remains unavailable.',N69+':508,551')
add('DER-XVI-87-96','Les Dérivateurs XVI ms87–96 (via recovered companion)',[107],
 'reproduced_manuscript_passage','prior_context/extracted/companion/chunks/DER_XVI.tex:2641–2653,2706–2770; commentary2655–2674,2772–2818; '+N69+':470',
 'The reproduced text asks for a finer fundamental localizer retaining simple homotopy, proposes finite maquettes/posets and elementary moves, distinguishes topological from categorical homotopy, and gives the subdivided triangular-circle obstruction. Page94 is explicitly missing. The companion comments separately on minimality and finite-poset simple homotopy.',
 'Manuscript conjectural program, retraction/qualification and example as reproduced by an earlier AI companion; its commentary is that run’s claim.',
 'The proposed thematic bridge is real at the level of finite combinatorial models and elementary moves. No matching definition of an SA21 network/cutting move is supplied.',
 'This audit verifies the recovered companion endpoint, not the original XVI ink or all commentary proofs. No new proof of Cisinski, Barmak–Minian or Whitehead theory is claimed.')
missing('MPL121-Q4.3','MPL_121_001-048 Q4.3',[110],
 'First-pass isotopy-refinement lead, referring to147/181–184.',
 'The cutting-specific coherence question remains different from the missing earlier comparison.',N69+':508,551')
missing('STRATA-B1','STRATA B.1',[111],
 'Proved, return’s claim, for an EI criterion, as reported by SA21 notes.',
 'The recovered STRATA B.2 at477 is a related coefficient/topos dictionary; it is not B.1 and cannot verify its criterion.',N69+':477 (different B.2 row)')
add('PATHS-D13','PATHS D.13',[111],
 'exact_return_row',D69+':79',
 'A relative-poset localization of an ordinary category need not rectify: a finite circle P presents BZ, and an explicit countable signed-face orbit poset Q presents BC2 but fails rectification at the finite category BC2.',
 'Refuted (return’s claim), for the proposed rectification assertion.',
 'Confirms the notes’ warning that general-category/rectification extensions require separate data; it is not a statement about SA21’s cutting category.')
missing('MPL148-R16','MPL_148_029-072 R16',[114],
 'First-pass realization/avatars lead at148/043.',
 'A distinct realization program, with no exact target in the recovered files.')
missing('MPL148-T01','MPL_148_029-072 T01',[117],
 'First-pass documentary lead at cover scans148/040,066.',
 'Only a precedent for keeping local foliation and cover records separate; no mathematical claim.',extra={117:[984,992,1048,1086,1116]})

# The nine explicit open targets of source note#118.
add('LM4-C12','LM4 C.12',[118],
 'exact_id_excerpt',N138+':353; '+N69+':211–212',
 'The return neither constructs an infinite operator group with nontrivial kernel in the exact level-zero comparison nor proves universal injectivity. It begins identifying the hyperbolic-surface kernel as pi1 of a centralizer; the excerpt stops. Anchors §23,folios140–141,scans279–281.',
 'Open (return’s claim).',
 'Confirms the target and its unresolved status. SA21’s branch/rive constructions supply no such operator-group comparison.',
 'The selected entry is truncated; no complete theorem or kernel formula with all ambient conventions is reconstructed.',{118:[1124]})
missing('RESIDUE-E6','RESIDUE E.6',[118],
 'Open, according to SA21 note#118; anchors VII ms65–67,PATHS B.8/C.9–C.10.',
 'The full all-endpoint and ind-stage comparison is not checked by SA21 endpoint gluing. PATHS B.8,C.9,C.10 are separately recovered below; they do not replace RESIDUE E.6.',extra={118:[1125]})
add('EXIT-P3c','EXIT_ONE_TYPE P3c-general',[118],
 'exact_run_summary',N69+':177–178,531; '+N138+':175–176',
 'The run summary names P3c-general as its remaining Open row and starts the assertion about good normal-crossings completions with algebraic markings for arbitrary smooth algebraic threefolds. The statement is cut off after “strat…”.',
 'Open in the run summary; final13November; full result row unavailable.',
 'Supports note#118’s unchanged-open boundary only; it does not verify the omitted exact formulation.',
 'Exact run and ID are present, but the full result row and hypotheses are not. No missing words are supplied.',{118:[1126]})
add('PATHS-C10','PATHS C.10',[118],
 'exact_return_row',D69+':66',
 'Literal pointed and pointed-ind-category refinements of stabilized full paths remain unresolved in the stated generality; anchors IX044,049,052,072.',
 'Open (return’s claim).',
 'Confirms the unchanged-open target; finite chains of ficelles do not supply this refinement theorem.',extra={118:[1125,1127]})
add('RESIDUE-C8','RESIDUE C.8',[118],
 'exact_return_row',D69+':259',
 'The least number of objects of a finite category with pullbacks admitting conditions(a),(b) but not(c) is undetermined. C.3 gives an upper bound of five; the exclusion classification for smaller categories and an enumeration through six objects are not supplied.',
 'Open (return’s claim).',
 'Confirms the finite-category minimum problem, distinct from SA21’s F1–F6 labels.',
 'Conditions(a)–(c) belong to the earlier return. This audit does not reconstruct them from the minimum-problem row or perform a new enumeration.',{118:[1128]})
add('RESIDUE-F6','RESIDUE F.6',[118],
 'exact_return_row',D69+':277; '+N69+':424',
 'The return leaves open whether every totally W_Z-aspherical presheaf is totally W_infinity-aspherical, equivalently the specified TOTASPH F.27 composition question. The general-action argument does not transfer because presheaf totality tests only actions pulled back from the base; the requested bounded monoid/presheaf search was not performed.',
 'Open (return’s claim).',
 'Confirms the unchanged target. Boolean sections near a closed subset in SA21 do not test this total-asphericity condition.',extra={118:[1129]})
add('RESIDUE-I7','RESIDUE I.7',[118],
 'exact_return_row',D69+':285; '+N69+':428',
 'No proof or counterexample is supplied for the reversible accessible-localizer classification. A natural assignment D↦D′ on all Der1–4 derivators with W_D′=W_D^lc, the alternative finite-poset obstruction, weakest sufficient enhancement and general iteration remain unresolved. I.9 handles specified enhanced spectra and D(F_p) cases only.',
 'Open (return’s claim).',
 'Confirms the exact bare-derivator/general classification boundary; SA21 contains no such construction.',extra={118:[1130]})
add('RESIDUE-J2','RESIDUE J.2',[118],
 'exact_return_row',D69+':289',
 'The ordinary-base proof does not establish recognition for a walking noninvertible/invertible2-cell, one-object generating2-cell examples or general strict2-categories. Nonidentity2-cells in lax triangles defeat the strict comma identity; no sufficiently coherent relative strictification/straightening theorem is supplied.',
 'Open (return’s claim).',
 'Confirms that ordinary pushouts of ficelles do not settle the strict higher-base recognition problem.',extra={118:[1131]})
add('RESIDUE-J3','RESIDUE J.3',[118],
 'exact_return_row',D69+':290',
 'Universal pullback-preserving classes, complete boundary-piece tests and the proposed lax-comma Der4 base-change theorem are not established. Absolute model structures and Theorem A do not imply them; the full four-variance table still needs recognition and lax-comma compatibility.',
 'Open (return’s claim).',
 'Confirms the unchanged target; the SA21 cutting lemma does not provide this higher-categorical base-change criterion.',extra={118:[1132]})

# Secondary run/ID references explicitly named inside source paragraphs.
add('PATHS-B8','PATHS B.8 (secondary anchor of RESIDUE E.6)',[118],
 'exact_return_row',D69+':50',
 'Whether the full/weak-vertical comparison J is always a weak equivalence, including wide, two-out-of-three, saturated, HCF, model and Brown variants beyond the specified B.4 cases, remains open.',
 'Open (return’s claim).',
 'Checks the secondary anchor of note#118; does not recover the missing RESIDUE E.6 statement.',extra={118:[1125]})
add('PATHS-C9','PATHS C.9 (secondary anchor of RESIDUE E.6)',[118],
 'exact_return_row',D69+':65',
 'The general additive relative-category proposal is not proved from the manuscript’s unspecified additional axioms or merely from finite-sum closure of a saturated weak class; anchors IX061,065,070.',
 'Open (return’s claim).',
 'Checks the secondary anchor; does not reconstruct the stronger all-endpoint/ind-stage RESIDUE E.6 comparison.',extra={118:[1125]})
add('TOTASPH-F27','TOTASPH F.27 (secondary anchor of RESIDUE F.6)',[118],
 'exact_id_excerpt',N69+':418,286–288',
 'The arguments do not decide whether every W_infinity-dwyerienne sieve is discretely flat or whether such sieves are composition-closed; the excerpt says these are equivalent to a one-point couniversal recognition question and the F.26 presheaf implication.',
 'Open (return’s claim).',
 'Confirms the composition-question anchor and its scope; no link from the SA21 sheaf calculation resolves it.',
 'The selected row is truncated; its references to F.26 remain pointers rather than a checked full equivalence proof.',{118:[1129]})
missing('GALOIS-A8','GALOIS A.8 (secondary comparison for STRATA C.8)',[61,63],
 'Comparison ID reported in the SA21 context paragraphs; exact status not supplied there.',
 'Named among gluing/descent comparisons. No exact A.8 row in either recovered selection.')
add('GALOIS-B3','GALOIS B.3 (secondary comparison for STRATA C.8)',[61,63],
 'exact_id_excerpt',N69+':453',
 'The entry is headed Relative Theorem A for an arbitrary derivator and assumes Der1–4 in presheaf variance on all U-small categories, with functors A→B→S. The excerpt ends before its comparison conclusion.',
 'Proved (return’s claim).',
 'Checks the exact ID as a relative-descent lead; the truncated entry supplies no complete theorem to apply to SA21.',
 'Do not infer or reproduce the missing quantified comparison statement from the title alone.')
missing('GALOIS-B5','GALOIS B.5 (secondary comparison for STRATA C.8)',[61,63],
 'Comparison ID reported in the SA21 context paragraphs; exact status not supplied there.',
 'Named among gluing/descent comparisons. No exact B.5 row in either recovered selection.')

assert len(ROWS)==54,len(ROWS)
assert len({r['id'] for r in ROWS})==len(ROWS)
for row in ROWS:
    assert row['source_occurrences'],row['id']
    assert {o['note_id'] for o in row['source_occurrences']}==set(row['note_ids'])

(P/'project_targets.json').write_text(json.dumps(ROWS,ensure_ascii=False,indent=2)+'\n')
def write_tsv(path,fields,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
flat=[];links=[];events=[]
for r in ROWS:
    loc='; '.join(f"{o['note_id']}:{o['line']}" for o in r['source_occurrences'])
    flat.append({'target_id':r['id'],'target':r['target'],'note_ids':';'.join(r['note_ids']),
      'note_locators':SOURCE+' '+loc,'match_status':r['match_status'],
      'checked_register_locator':r['checked_target_locator'],'actual_statement':r['what_target_actually_says'],
      'recorded_status':r['recorded_status'],'relation':r['relation_to_sa21'],'limits':r['limits']})
    links.append({'kind':'our projects','from':SOURCE+' '+loc,
      'to':r['target']+' — '+r['checked_target_locator'],
      'what':r['relation_to_sa21'],
      'evidence':r['match_status']+'. '+r['what_target_actually_says']+' Status: '+r['recorded_status']+' '+r['limits'],
      'note_ids':';'.join(r['note_ids'])})
    events.append({'statement_id':r['id'],'date':'2026-11-19',
      'who':'GPT-6 Astra Pro; /root/cotes_156_8_9; project endpoint audit',
      'type':'used and rechecked in this run',
      'outcome':'Textual endpoint/identity/status check only: '+r['match_status']+'. '+r['checked_target_locator']+'. '+r['limits']})
write_tsv(P/'project_links.tsv',list(flat[0]),flat)
write_tsv(P/'links.tsv',['kind','from','to','what','evidence','note_ids'],links)
write_tsv(P/'check_events.tsv',list(events[0]),events)
exact={'exact_return_row','exact_id_excerpt','exact_run_summary','exact_source_note','reproduced_manuscript_passage'}
write_tsv(P/'located_links.tsv',['kind','from','to','what','evidence','note_ids'],
          [l for l,r in zip(links,ROWS) if r['match_status'] in exact])
write_tsv(P/'unresolved_leads.tsv',list(flat[0]),
          [r for r in flat if r['match_status'] not in exact])
coverage=[]
for n in NAV:
    matches=[r['id'] for r in ROWS if any(o['note_id']==n['note_id'] and o['line']==n['line'] for o in r['source_occurrences'])]
    coverage.append({'note_id':n['note_id'],'line':n['line'],'read':'full Context paragraph read',
                     'target_ids':';'.join(matches)})
assert all(r['target_ids'] for r in coverage),[r for r in coverage if not r['target_ids']]
write_tsv(P/'context_coverage.tsv',list(coverage[0]),coverage)
print(json.dumps({'targets':len(ROWS),'statuses':dict(collections.Counter(r['match_status'] for r in ROWS)),
 'context_paragraphs_read':len(coverage),'source_notes':len({i for r in ROWS for i in r['note_ids']}),
 'located_endpoints':sum(r['match_status'] in exact for r in ROWS),'unresolved_or_indirect':sum(r['match_status'] not in exact for r in ROWS)},indent=2))
