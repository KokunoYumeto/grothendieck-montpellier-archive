"""Integrate the fully checked F58 fragment once; guarded against reruns."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib
r=Path(__file__).resolve().parent
p=r/'GCT_NSRH.tex'; s=p.read_text(); f=r/'finding_F58.tex'
assert hashlib.sha256(f.read_bytes()).hexdigest()=='b099ca23f05312a58498b00ab68ff3d49548837b4db3a52fdeafd2ad39a6c870'
body,dictionary=f.read_text().split('% Separate paragraph for Part III.',1)
needle=r'\subsection{A normalization that cannot be a finite Frobenius trace}'
assert s.count(needle)==1 and r'\label{f:cellpositivityspecialization}' not in s
s=s.replace(needle,body.rstrip()+'\n\n'+needle)
needle=r'\section{Archival audit and the Fable leads}\label{sec:archive}'
s=s.replace(needle,dictionary.strip()+'\n\n'+needle)
s=s.replace('findings A01 and F01--F57,','findings A01 and F01--F58,')
old='Compatible graded kernels for larger whole modules or for the two-row quotient, a source-prescribed higher categorical presentation and designated simple/global labels remain.'
new='F58 also excludes strict effective generator kernels on a two-row rank-four basis retaining the source cell/quasi-cell refinement: positive Laurent entries cannot lose the required connecting edge at the positive specialization. Arbitrary positive bases without that cell comparison remain outside the obstruction. A signed or derived action comparison, a source-prescribed higher categorical presentation and designated simple/global labels remain.'
assert old in s; s=s.replace(old,new); p.write_text(s)
q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:
    rd=csv.DictReader(f,delimiter='\t'); fields=rd.fieldnames; rows=list(rd)
for x in rows:
    if x['id']=='Q3-GCT':
        x['finding_ids']+=',F58'
        x['current_gate']+=' F58 excludes strict effective named-generator kernels even in the rank-four two-row case when the source cell/quasi-cell refinement is retained. A signed/derived action or a distinct positive canonical operator comparison is now required for that route.'
        x['next_step']='Construct a signed/derived actual-action comparison retaining designated cells and independent local bounds, or specify different effective canonical operators; strict effective P or Q kernels in the source cellular basis cannot supply the extension.'
    if x['id']=='Q3-GRADED-COEFFICIENT-KERNELS':
        x['finding_ids']='F56,F57,F58'
        x['current_gate']+=' F58 also excludes a strict effective two-row extension preserving the source cell/quasi-cell refinement; arbitrary positive bases without that comparison and derived/signed alternatives remain.'
        x['next_step']='Construct the required signed/derived extension or identify different effective canonical operators; compare the global/local lattices and source cells explicitly.'
    if x['id']=='Q6': x['current_gate']=x['current_gate'].replace('F01–F57','F01–F58')
row=['Q3-CELL-POSITIVITY','F58; IV §2.4 pp18–19 eq17; Thm13.4 pp74–75; Conj19.1(ii)–(iii) pp130–131; Example19.3 pp133–135 Fig21','Can strict Laurent positivity of the named generators retain the required generic cells and specialized quasi-cells?','REFUTED_ALREADY_FOR_THE_TWO_ROW_RANK_FOUR_SOURCE_CELL','F58','Nonnegative Laurent entries have unchanged support, coordinate invariant subspaces and all-algebra cell preorder at every positive specialization. The actual6Dcell must split into3Dsubmodule/3Dquotient atv1, so no source-compatible strict positive P-basis or Q-basis exists. Arbitrary positive bases with non-coordinate special summands and signed/factored positivity are not refuted.','Zero-reflecting positive evaluation; graph reachability; coordinate subquotients; exact source filtration; positive2D irreducible-to-reducible counterexample','Use signed/derived coefficient objects or a different effective operator basis while proving the required source cell/global comparison.']
rows.append(dict(zip(fields,row))); assert len({x['id'] for x in rows})==len(rows)
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t'); w.writeheader(); w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
events=[('F58-COMPLETE','/root','targeted proof check','Read/reconstructed entire report, source audit, complete final fragment and independent review. Positive support, all-algebra preorder, cellular quotients, actual6Dsource application, regular-local basis and2Dlimitation example all PASS. Primary Figure21 previously visually inspected; exact textual source premises are checked by both source agents.','agent_cell_specialization_positivity.md SHA256 223bd6571a53270b82ae5d108b8cb4065c55a599eab32cb65cc4e5bbe3a66c37; finding_F58.tex SHA256 b099ca23f05312a58498b00ab68ff3d49548837b4db3a52fdeafd2ad39a6c870'),('F58-FRESH','/root/gct_statements','independent re-proof','Actual reviewer independently reconstructed whole report and whole final fragment, and checked exact source cell definitions/filtration; PASS.','REVIEW_CELL_SPECIALIZATION_GCT.md SHA256 9b32a91d22539e3050e29a09e6267808726d8830d7c1bccb88a8fc15bdf265dc'),('F57-FINAL-ELL-REVIEW','/root/rectangular_and_theta','targeted proof check','Actual reviewer matched final ell-not-dividing-q convention after whole-fragment review; PASS.','REVIEW_RANK4_NEGATIVE_TRACE_THETA.md SHA256 3a304487baee5862898c9c78c3d8de9ace92181637842468ffb9b02ecc0fb6a9'),('SYNTHESIS-SNAPSHOT07','/root/grothendieck_dictionary','targeted proof check','Actual reviewer read entire abstract, PartIV and all new PartIII/bar dictionaries of snapshot throughF56; PASS after recommended rank-three whole-tensor and split-K0/state-bar precision changes, both integrated. Not a fresh whole-paper proof review.','agent_dictionary_snapshot7_review.md SHA256 7a989e49ed1881b7f54bf3721f09cde22fc7bf5a7d66c3bbedd824b9fede1a5f')]
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,who,typ,out,loc in events: w.writerow([sid,now,who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121',typ,out,loc])
with (r/'LEDGER.md').open('a') as f:
    f.write(f'\n## {now} — F58 cell-compatible strict positivity gate closed\n\nIntegrated the full proof and separate dictionary after root and independent whole-report/fragment checks. Even the actual two-row rank-four module cannot have strict positive Laurent named-generator matrices in a basis retaining the required cell/quasi-cell refinement. The graph/preorder cannot change under positive evaluation; the prescribed6Dcell must refine into3+3. This is stronger than the previous displayed-basis rescaling obstruction and distinct from F57, while leaving arbitrary positive bases and signed/factored positivity untouched. The actual cell-compatible extension must now permit cancellation or use different effective operators.\n')
with (r/'IMPLICATIONS.md').open('a') as f:
    f.write('\n## F58: required two-row cells force cancellation\n\nStrict nonnegative Laurent entries preserve their zero pattern at every positive parameter. Consequently the actual all-algebra cell preorder and coordinate cellular subquotients cannot change. IV’s rank-four two-row construction requires one6Dgeneric cell to specialize into3Dcellular submodule and3Dquotient. Therefore its source-compatible basis cannot have strictly nonnegative Laurent matrices for every named P_i, or for every Q_i. This is an obstruction to an additional strict positivity requirement, not a contradiction to IV’s signed/factored conjecture or its constructed basis.\n\nIn the source graph the exact disappearing edge is c0=(v−v^-1)^2, a nonzero rank-zero virtual character. The effective representation cone has no nonzero class of augmentation zero; representation K0 does. The precise framework anchors are SGA3 I4.7.2–3/cote90 scan17, SGA6 V2–3/cote133 scan18, and EGA I1.3.7/1.3.8/1.4.1. This forces a signed/derived action comparison or different effective operators in any continuation that retains the designated cells. It does not rule out an arbitrary positive basis with non-coordinate specialized summands.\n')
readme=r/'README.md'; txt=readme.read_text().replace('integrates F01–F57','integrates F01–F58')
txt+='\nF58 closes the stricter two-row cell-compatible positive-matrix route: the prescribed cell refinement atv1 forces a nonzero coefficient to vanish, impossible for a nonnegative Laurent polynomial. Signed/factored or derived actions remain distinct possibilities. The current PDF is the checkpoint06 build throughF57 until the next rebuild.\n'
readme.write_text(txt)
print('F58 integrated; questions',len(rows),'main',hashlib.sha256(p.read_bytes()).hexdigest())
