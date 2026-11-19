"""Assemble the task register, source audit, program inventory and corrections.

Pass --final only after the mathematical and PDF audits are complete.
This script changes no mathematical result or evidence classification.
"""
import argparse
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

parser=argparse.ArgumentParser()
parser.add_argument('--final',action='store_true')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
aux=(root/'logs/RESEARCH_SA21_paper.aux').read_text()
locators={m[0]:(m[1],m[2]) for m in re.findall(r'\\newlabel\{(SA21-[^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux)}
def refs(*ids):
 return '; '.join(f"{locators[i][0]} (p. {locators[i][1]}; {i})" for i in ids)
def esc(s):
 return str(s).replace('|','\\|').replace('\r','').replace('\n','<br>')
def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+'\n'.join('| '+' | '.join(esc(v) for v in row)+' |' for row in rows)+'\n'

tasks=[
('A.1','Proved exact classifications; refuted universal OML and L2',('SA21-A03','SA21-A04','SA21-A06','SA21-A11','SA21-A26','SA21-A27'),'Arbitrary-poset neighbourhood criteria; arbitrary-L Boolean interval classification; finite-L conditional-lattice classification; scan113 reconstructed.'),
('A.2','Proved exact class; refuted the unrestricted equivalence',('SA21-A13','SA21-A17','SA21-A18'),'Lieus give the exact orthoset reduction. Actual figures are weaker than all abstract orthogonal pairs. O6 and a spatial C5 give the requested failures.'),
('A.3','Proved exact class',('SA21-A14','SA21-A14a'),'Neighbourhood inclusion must force equality. For M(L), every lieu support is atomic iff L is an antichain or has no isolated points.'),
('A.4','Proved exact replacement; refuted the original general assertion and L3',('SA21-A15','SA21-A16','SA21-A24'),'Two-neighbourhood test gives the lattice identities; incidence-coverage gives clause(d). Old hypotheses imply coverage but do not imply the lattice test.'),
('A.5','Proved existence',('SA21-A20',),'A two-stratum normalized faithful external support function is not fully faithful.'),
('B.1','Proved the qualified bridges; refuted the listed false implications',('SA21-B-mag-equivalence','SA21-B-local-equivalence','SA21-B-Sigma-counter','SA21-B-deployment-unique','SA21-B-Atstar','SA21-B-L6-status'),'Chronological axiom atlas, definition branches, positive implications, explicit nonimplication models, and all four requested open implications.'),
('B.2','Proved the corrected connectedness statements; refuted C4',('SA21-B-incidence-components','SA21-B-figure-components','SA21-B-refinement-components','SA21-BM-cell-connected'),'Global incidence components, components within each figure, and global refinement components are distinct and fully classified as stated.'),
('B.3','Refuted literal L1; proved exact representable subclass',('SA21-BM-r12','SA21-BM-event-iff','SA21-BM-domain','SA21-BM-refinement'),'Local distributivity/bounded-join primality is necessary and sufficient for binary-conflict prime events with finite causes; refinement remains extra structure.'),
('B.4','Proved the precisely specified o-minimal model; refuted stronger readings',('SA21-BM-cell-definition','SA21-BM-cell-axioms','SA21-BM-cell-support','SA21-BM-cell-moderation'),'Closed-support generalized cells with finite frontier decompositions give a faithful model and finite common subdivisions over arbitrary o-minimal real closed fields.'),
('C.1','Refuted L4; proved the all-dimensional replacement',('SA21-C01','SA21-C03','SA21-C06','SA21-C07','SA21-C08'),'Corrected sign/orbit conventions, finite principal ideals, spherical lower intervals and coherent orientations characterize regular CW data; global link connectedness is not necessary.'),
('C.2','Proved exact simplicial criterion; refuted the manuscript shortcut',('SA21-C09','SA21-C10','SA21-C11','SA21-C12'),'Boolean principal ideals plus global meets/vertex-set injectivity give simplicial complexes; positional figures and order-complex flags are separated.'),
('L1','Refuted; corrected equivalence proved',('SA21-BM-r12','SA21-BM-event-iff','SA21-BM-domain'),'Literal contrées are broader. The representable subclass is locally distributive; higher-arity consistency is also broader than binary conflict.'),
('L2','Refuted; exact replacement proved',('SA21-A03','SA21-A07','SA21-A08'),'Sumner finite-graph normality characterizes the clique support law and is weaker than double-polar orthomodularity.'),
('L3','Refuted; exact Boolean and faithfulness criteria proved',('SA21-A04','SA21-A15'),'Nondisjoint twins and a genuine dense-chain-plus-isolated-point interval model prevent the proposed inference. Separation is essential.'),
('L4','Refuted in both directions; exact CW characterization proved',('SA21-C06','SA21-C07','SA21-C08'),'The torus-with-top model satisfies the local proposals but has nonspherical boundary; two triangles sharing one vertex refute global-link necessity.'),
('L5','Proved under the specified cell-model hypotheses; stronger assertions refuted',('SA21-BM-cell-axioms','SA21-BM-cell-support','SA21-BM-cell-moderation','SA21-BM-cell-limits'),'The axiom truth table and exact triangulation construction state which clauses hold and which fail.'),
('L6','Refuted; exact automatic package proved',('SA21-B-optional-implications','SA21-B-L6-countermodels','SA21-B-L6-status'),'Strong Mag does not imply every optional local, support, absolute-compatibility or subdivision-extension condition.'),
('L7','Refuted as an unqualified morphism identification; corrected object-and-arrow theorem proved',('SA21-A21','SA21-A22','SA21-A23'),'Radical removal yields orthosets; saturated correspondences are complete join maps with the stated dagger, not ordinary orthogonality-preserving functions.'),
]
lines=[]
if not args.final:
 lines.append('INCOMPLETE\n\nThe mathematical classifications and counterexamples are complete; final source-register and PDF audit assembly remains in progress.\n')
lines.append(table(['Item','Outcome','Printed statements','Exact scope'],[(a,b,refs(*c),d) for a,b,c,d in tasks]))
lines.append('''
# RESEARCH_SA21 — final research and verification report

**AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).** We claim no human authorship and no priority. The reasoning-effort setting was not exposed in this run; the check-event records say so rather than guessing it. The supplied study and leads retain their stated AI provenance and are treated as claims to recheck.

The table above covers all eleven numbered Part items and all seven Leads. “Refuted” is followed in the paper by a complete counterexample and the exact replacement proved here. Definitions, conventions and hypotheses remain explicit: we do not extend a finite theorem to infinite objects by enumeration. The following subtask register makes the subsidiary requests individually visible.
''')
subtasks=[
('A.1 comparability disjoncteur',('SA21-A03','SA21-A04','SA21-A25'),'Exact arbitrary-poset tests, strict cograph sufficiency, and refutation of the proposed Sumner equivalence.'),
('A.1 interval magasin',('SA21-A05a','SA21-A06','SA21-A09','SA21-A10','SA21-A26','SA21-A27'),'Strong axioms for every L; finite supp1; infinite-figure counterexample; complete split-poset comparison; exact finite conditional-lattice class.'),
('A.1 ten-element manuscript example',('SA21-A11',),'Complete set model, fourteen Hasse edges, all operations, complement and explicit orthomodular failure.'),
('A.2 supp1 versus spatial law',('SA21-A16','SA21-A17'),'Actual figures and universal abstract-support figures are kept distinct; only the universal pair version is exactly OML.'),
('A.2 margin “Oui!”',('SA21-A18',),'Four-point path orthoset and five-cycle spatial realization supply complete finite failures.'),
('A.4 all four clauses of scan94',('SA21-A16','SA21-A24'),'The lattice criterion includes relative complements and arbitrary nonempty meets; ambient empty-meet preservation has a separate top condition; clause(d) has an incidence-coverage condition.'),
('B.1 At9Σ + At10 ⇒ At12',('SA21-B-Sigma-gate','SA21-B-Sigma-counter'),'False, even with additional stated axioms; exact missing condition is membership of the common refined deployment in Σ.'),
('B.1 uniqueness in At14bis',('SA21-B-extension-unique','SA21-B-deployment-unique','SA21-BM-14bis-reading'),'An actual object is not uniquely forced; the abstract deployment is unique up to its specified isomorphism. Literal all-target and corrected exterior-target clauses differ.'),
('B.1 Théorème-Scholie converse',('SA21-B-Atstar','SA21-B-Atstar-literal'),'The prime core and canonical-subfigure membership give both directions. The shortened ambient membership-free list does not.'),
('B.1 optional axioms / L6',('SA21-B-optional-list','SA21-B-optional-implications','SA21-B-L6-status'),'Source-resolved list, proved implications, and explicit finite or infinite separating models.'),
('B.3 domain dictionary',('SA21-BM-domain','SA21-BM-refinement'),'All configurations form the ideal completion of finite ones; events are complete primes; support polarity is translated; subdivision/refinement require the retained extra relation.'),
('B.4 definition and axioms',('SA21-BM-cell-definition','SA21-BM-cell-calculus','SA21-BM-cell-axioms'),'Arbitrary definable X over an o-minimal expansion of a real closed field; closed-support generalized-cell families with finite frontier decompositions.'),
('B.4 faithful and modérée',('SA21-BM-cell-support','SA21-BM-cell-extension','SA21-BM-cell-moderation'),'All point strata are lieux, supports are the full powerset of X, and compatible triangulation gives finite common subdivisions.'),
('C.1 connected boundaries',('SA21-C03','SA21-C04','SA21-C05'),'Boundary comparability/Alexandrov/order-complex connectedness, low-dimensional exceptions, infinite boundary paths, and the necessary edge non-repetition condition.'),
('C.1 every dimension',('SA21-C06','SA21-C07','SA21-C08'),'Complete obstruction certificates and regular-CW construction using spherical lower intervals, finite closures and coherent signed incidence.'),
('C.2 simplices and flags',('SA21-C09','SA21-C10','SA21-C11','SA21-C12'),'Exact simplicial characterization, square counterexample, flags versus interval figures, and the precise weak-homotopy comparison.'),
]
lines.append(table(['Subsidiary task','Printed statements','Resolution'],[(a,refs(*b),c) for a,b,c in subtasks]))
lines.append('''
## Main classifications and the scope of the proofs

For an irreflexive symmetric orthogonality relation, write N(A) for its common orthogonal neighbourhood and cl(A)=N²(A). The support lattice consists of the closed sets. Its exact orthomodularity condition is that every maximal orthogonal subset of every closed set generates that closed set. Specializing to comparability gives the explicit maximal-chain/neighbourhood criterion of the paper, including arbitrary infinite orders. Booleanity has the exact point-neighbourhood test stated separately. These are criteria in the original order relation, with both directions proved, rather than an appeal to an undefined “repair” of induced fences.

For the interval magasin M(L), the general criterion is applied to the explicitly defined positional order. In addition, the paper proves two structural classifications: for **finite** L, orthomodularity holds exactly when every upper-bounded pair has a join and every lower-bounded pair has a meet; for **arbitrary** L, Booleanity holds exactly when the nonisolated elements of L form a chain. The split-poset comparison with proper quotients is proved for every L. The finite conditional-lattice theorem uses the opened bounded-lattice theorem only after an explicit bounding-and-transfer argument. An unrestricted unbounded assertion in the opened 2022 arXiv version is separately refuted; we do not attribute that error to an unopened revised journal text.

The four-point crown gives an eight-stratum interval magasin with twenty supports that is not orthomodular. Every one of its actual finite figures nevertheless satisfies the figure support law. This separates global orthomodularity from Boolean calculus inside a figure and separates Sumner's normality condition from the Dacey orthomodularity condition. A countable example prevents silently extending the finite-flag proof to arbitrary infinite figures.

The atom question is answered by an exact neighbourhood-inclusion condition, distinct from point separation. In the interval model, lieux are minima for full refinement, not minima for the interior relation alone. They are precisely the point symbols. Every lieu support is an atom exactly when L is an antichain or has no isolated points. Connected orders therefore satisfy the atom assertion, including the one-point case, but connectedness is not the maximal class.

For the support theorem of scan156-7/94, the two-neighbourhood condition characterizes relative complementation and the associated complete Boolean calculus. Its fourth clause, recovery of the support of an incidence-closed subfigure, additionally requires the displayed incidence-coverage equation outside the older hypotheses. Under those older hypotheses the coverage condition follows, but the lattice condition can still fail. The old eight-stratum example is rechecked with all hypotheses and both advertised failures.

The chronological axiom atlas distinguishes literal complete join-irreducibility from bounded-join primality. The original156-6 formula(1.20) already assumes the latter; the full representation theorem there is consequently valid. The156-4 equality-based reading and the independent156-8 atlas list admit the counterexamples. The precise convention inherited in156-7 is stated. This qualification was found in the final original-scan audit and is reflected in the corrected source and event registers.

Literal finite contrées need not be event-configuration domains. The exact representable subclass is locally distributive, equivalently has the needed bounded-join primality. Binary conflict, rather than unrestricted finite consistency, is essential. The ideal-completion and support translations are proved, and refinement is explicitly retained as additional data. For geometry, closed-support generalized cells and finite frontier decompositions give the specified faithful o-minimal atelier. The axiom table states the failures of C4 and the overly strong polyhedral/simplicial and extension readings; compatible triangulation proves moderation for arbitrary definable X over the stated field.

For maquettes, literal oriented inequality conflicts with single-argument reversal invariance, and a second sign ambiguity has genuinely different mathematical consequences. Each reading is treated. Signed diamonds and connected boundaries do not force regular cells: the torus with a formal top cell gives a finite all-axiom counterexample. Conversely, global link connectedness is not necessary for a regular CW complex. The corrected all-dimensional theorem requires finite principal ideals, spherical lower intervals, unique immediate oriented lifts and coherent signs. The simplicial refinement requires Boolean principal ideals and the global meet/vertex-set condition. No low-dimensional classification is substituted for the all-dimensional result.

## Reading and source-access record

We unpacked the supplied ZIP once. We read the study and relevant per-cote reading/correction/check records, then rechecked the claims used against the indicated transcription passages and original scans when the mathematical step depended on a doubtful glyph. The exact file-and-line record below is part of the evidence. Source access is distinguished from source authority: a failed retrieval or a metadata page never counts as an opened theorem.
''')
source=root/'parts/bmodels/FINAL_SOURCE_AUDIT.md'
lines.append(source.read_text() if source.exists() else '\nFinal consolidated source-access audit is being assembled; the per-part source records and bibliography remain available.\n')
lines.append('''
## Literature searches and priority

We searched the exact title “Vers une géométrie des formes” and combinations of Grothendieck, cote156, orthomodular, Dacey graphs, orthogonality spaces associated with posets, regular CW posets and prime event structures. The official notice for Jean Malgoire's3October2002 seminar demonstrates prior mathematical attention to these pages. The search did not establish a published proof of the particular classifications and corrections assembled here; it does not prove that no such publication exists. Michel Hua's project landing page was opened as a contemporary resource; no uncredited theorem proof is taken from it. We make no priority claim for statements not located in these searches. All27 bibliography entries explicitly describe their actual access status.

## Computations and reproducibility
''')
lines.append((root/'parts/maquettes/PROGRAM_INVENTORY.md').read_text())
lines.append('''
### Final operational assembly

`code/build_root_corrections.py` creates the root correction table from verified locators. `code/audit_metadata.py` checks exact agreement between included numbered statements, CSV rows, printed labels, event coverage, effort disclosure and citation keys; it also reads the final build log. `code/build_final_report.py` assembles this report without modifying mathematical claims. `code/build_final_package.py` creates the final ZIP and a SHA256 manifest. These operations have no mathematical enumeration scope and no aggregate run time is asserted. `README.md` gives the build and certificate commands. The report and final audit JSON identify the retained runs, rather than treating repeated executions as additional cases.

## Complete correction and qualification register

The following table includes corrections to the supplied study, readings, transcriptions, prompt claims and leads, as well as source confirmations that prevent a false correction. Paths are relative to the unpacked attachment unless they name the prompt itself. “Scan” means the PDF scan index; the archive's pencil page is one smaller. Alternative readings are stated explicitly, and changing a mathematical hypothesis is not disguised as a transcription correction. Repeated conclusions at distinct source locators are retained so that every affected supplied record can be found.
''')
corrections=[]
for file in sorted((root/'parts').glob('*/CORRECTIONS.tsv')):
 with file.open(newline='') as handle:
  corrections.extend(csv.DictReader(handle,delimiter='\t'))
prompt=(root.parent/'upload/PROMPT(20261119-110210).md').read_text().splitlines()
for row in corrections:
 if row['id']=='SA21-C-K09':
  matches=[str(i) for i,line in enumerate(prompt,1) if line.startswith('- **L4.') or line.startswith('- **C.1.')]
  row['line_or_locator']=','.join(matches)+'; L4 and C.1'
headers=['id','file','line_or_locator','kind','correction','evidence']
assert len({r['id'] for r in corrections})==len(corrections)
with (root/'RESEARCH_SA21_corrections.tsv').open('w',newline='') as file:
 writer=csv.DictWriter(file,fieldnames=headers,delimiter='\t');writer.writeheader();writer.writerows(corrections)
lines.append(f'\nThere are **{len(corrections)}** locator-specific correction/qualification records.\n\n')
lines.append(table(['ID','Attached file and line','Kind','Correction or qualification','Evidence'],[(r['id'],r['file']+': '+r['line_or_locator'],r['kind'],r['correction'],r['evidence']) for r in corrections]))
lines.append('\n## Verification and typesetting\n')
qa=root/'parts/maquettes/FINAL_PDF_QA.md'
lines.append(qa.read_text() if qa.exists() else '\nPDF visual verification is in progress. No unchecked PDF is included as a deliverable.\n')
audit=root/'code/outputs/final_metadata_audit.json'
if audit.exists():
 data=json.loads(audit.read_text())
 lines.append(f"\nThe final metadata audit matches {data['numbered_statements']} numbered statements to {data['result_rows']} CSV rows, covers every statement in {data['check_events']} check events, and checks {data['bib_entries_with_access_markers']} bibliography entries. The final log has {len(data['overfull_boxes'])} overfull boxes in total, {data['overfull_boxes_above_2pt']} above2pt, and {len(data['build_errors_or_undefined_references'])} recorded build-error/undefined-reference categories. Rerun requested: {data['rerun_requested']}. The independent visual record is above; a clean log alone is not presented as visual QA.\n")
lines.append('''
## Progress reviews, checkpoints and final scope

Work began on19November2026 at12:02:40 Europe/Berlin (11:02:40UTC). Checkpoints follow the requested45-minute schedule; prior checkpoints are retained separately and are not nested inside this ZIP. `PROGRESS_LEDGER.md` records the changing proof gates and the actual audit state. The three-hour review becomes due at15:02:40 Europe/Berlin; no formal no-movement review is claimed before that deadline. The final package preserves the written mathematical work, source-access notes, correction/check registers, scripts and outputs from the checkpoints, with current deliverables replacing their earlier working versions. Historical notes and failed build/retrieval logs remain historical records; the current paper and this report determine the final status.

All Parts, Leads and subsidiary tasks in the outcome registers have a proved exact statement or a complete refutation with its proved replacement. Source-access limitations are disclosed separately; no result relies on an unavailable theorem being silently assumed. The manuscript's broader informal aspirations are not additional theorems claimed here. The arbitrary-poset criteria are complete answers in neighbourhood form; the stronger finite conditional-lattice description is not asserted as an unproved classification of infinite posets.
''')
lines.append('\nReport assembled: '+datetime.now(ZoneInfo('Europe/Berlin')).isoformat(timespec='seconds')+'.\n')
if args.final:
 assert source.exists() and qa.exists() and audit.exists(), 'Final audit dependencies are missing.'
 data=json.loads(audit.read_text())
 assert not data['build_errors_or_undefined_references'] and not data['rerun_requested'] and not data['overfull_boxes_above_2pt']
(root/'RESEARCH_SA21_report.md').write_text('\n'.join(lines))
print(json.dumps({'final':args.final,'task_rows':len(tasks),'subtask_rows':len(subtasks),'correction_rows':len(corrections),'report_bytes':(root/'RESEARCH_SA21_report.md').stat().st_size}))
