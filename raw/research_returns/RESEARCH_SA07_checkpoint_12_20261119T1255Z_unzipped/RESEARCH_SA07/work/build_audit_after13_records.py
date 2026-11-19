"""Exact A5 one-cover lift and independent affine-completion audit records."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/f6dbb6638732')
DATE='2026-11-19'
WHO='GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
events=[]
def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def event(statement,kind,outcome,agent='period_triangle'):
    events.append(dict(statement_id=statement,date=DATE,
      who=WHO.replace('agent period_triangle','agent '+agent),
      type=kind,outcome=outcome))

code='output/RESEARCH_SA07/code/build_A5_boundary_nilpotent.py'
matrix='output/RESEARCH_SA07/code/build_A5_boundary_nilpotent.json'
output='output/RESEARCH_SA07/code/build_A5_boundary_nilpotent.output.txt'
source='work/sources_audit_next/BleherChinburgLubotzky2004_08860v3.pdf'
assert sha(code)=='6d9624c231ef1bdc21ebfb3dc37fb97b68c3c1448d49684a5caffb862d58ed07'
assert sha(matrix)=='ba0e10ed1fc1eb306fafdfbb2e77fe3ed38f17f5ba0f5593188f59203872b111'
for suffix in ('.py','.json','.output.txt'):
    assert (ROOT/'work'/('build_A5_boundary_nilpotent'+suffix)).read_bytes()==(
      ROOT/'output/RESEARCH_SA07/code'/('build_A5_boundary_nilpotent'+suffix)).read_bytes()
own_internal=re.search(r'ACTUAL_WALL_SECONDS ([0-9.]+)',
                      (ROOT/output).read_text()).group(1)
independent=json.loads((ROOT/'work/code_generation_audit/A5_independent.meta.json').read_text())
assert independent['exit_code']==0
assert independent['program_sha256']==sha(code)
assert independent['json_sha256']==sha(matrix)

event('E.2.29','independent re-proof',
 'Constructed the actual A5 cover with X=(123),Y=(12345),z=(xy)^-1, inertia orders3,5,5, genus9 and44 cusps. The Cayley graph supplies an integral61-cycle basis and the actual43-dimensional saturated boundary lattice. A specified unimodular boundary minor and two finite group averages give integral N=ST/10 with N^2=0 and H-equivariance. The actual cusp b and proper quotient functional q have qB=0,qNb=19440. Thus gamma=I+60N has integral inverse and q gamma b=1166400, proving failure of the fixed proper quotient square. The BFS section gives all3600 cocycle values and the literal correction eta=N sum_k c(h,k), with delta eta=(gamma-I)c. The resulting specified extension automorphism lifts by BCL Cor2.4 and fixes the A5 quotient. Exact naturality and a determinant-minus-one exponent minor make every such lift IA.')
event('E.2.29','targeted proof check',
 'Typed the actual chain, boundary, finite-cover, completed relation-module and extension maps. The commutator quotient of R is the closed commutator quotient; finite index supplies the full induced profinite topology on K. The extension multiplication fixes the plus sign in gamma_tilde(m,h)=(gamma m+eta(h),h), and Neta=0 gives the stated inverse. The exact obstruction concerns this one affine integral lattice and its fixed proper quotient. It does not assert an all-cover transporter for E2.22 or E2.28. A Galois lift fixing this quotient would preserve actual cusp inertia and hence Phat, contradicting the computed nonzero proper image.')
event('E.2.29','computation or formal certificate',
 'The self-contained construction starts only from the two literal permutations, enumerates the60 group elements and120 edges, builds the61-cycle basis and44 actual cusp chains, computes the unimodular43-minor and full61x61 N, and checks N^2=0, H-equivariance, EN=0, NE=60N, integral gamma inverse, qB=0 and qNb=19440. It checks all3600 cochain identities and the exact exponent map AN=0, the minor[[2,1],[-1,-1]] and both identity-monodromy words. Internal program time '+own_internal+'seconds; code SHA256 '+sha(code)+'; matrix SHA256 '+sha(matrix)+'; retained output SHA256 '+sha(output)+'. The actual profinite lift is supplied by the written application of BCL, not computed generator words.')
event('E.2.29','independent re-proof',
 'Generation read the complete proof and final code including the IA strengthening, reopened BCLv3pp4-5, and independently checked the decisive matrices using arbitrary-precision SymPy objects. It verified nilpotence, EN=0,NE=60N,qB=0,qNb=19440,Neta=0, the exact exponent map and both actual A5 word values. The isolated run reproduced the full JSON byte for byte: exit0, external1.779917296seconds, internal0.956303676seconds. Its audit is work/generation_A5_boundary_lift_audit.md; output/meta are work/code_generation_audit/A5_independent.output.txt and A5_independent.meta.json.',agent='period_generation')
event('E.2.29','independent re-proof',
 'Root read the full A5 work proof and independently verified the actual cocycle correction sign, inverse, quotient identity and IA naturality. Root reopened BCL original v3 and read Theorem2.1,Corollary2.4,Lemma2.5 and the full proof on printedpp4-5. The production-ready text is work/E2_29_integrated_text.tex; parent retains its integration review, production append/build and the registered computation run.',agent='root')
event('E.2.28','independent re-proof',
 'Independently read all AF1-AF8 of work/agent_affine_integral_automorphism_completion.md. Verified the actual embedded quotient completions, every original-lattice intersection, the finite-group cocycle averaging sign and normalizer Gamma_N*Z_N by Smith normal form. Proved transition surjectivity despite Z_M->Z_N having image [N:M]Z_N: lift an integral invariant residue through Gamma_M and the divisible remainder through Z_M. This gives compatible actual conjugators and one h in G without compactness of nonclosed solution sets. AF7 passes: generator images in H imply an integral lattice endomorphism whose completed determinant is a unit at every prime, hence determinant+-1; the finite quotient then forces equality of Gamma_N. AF8 retains the intrinsic off-diagonal boundary-extension class and the discrete-representative/Galois obligations. Full exact audit:work/triangle_affine_integral_completion_audit.md.')
event('E.2.22','targeted proof check',
 'E2.29 supplies the explicit map showing that a quotient-fixing generic profinite lift preserving one affine integral lattice need not descend through that cover boundary lattice to proper integral homology. It is therefore not used as the all-cover proper transporter required in E2.22. E2.28 characterizes the actual all-affine-lattice condition, with its exact boundary-extension map retained. No main-gate resolution or historical assertion-status change is inferred.')

source_note=('Opened original arXiv2004.08860v3, version10June2021 and paper date25May2021,19pages. '
 'Theorem2.1 printedp4 is the exact surjection from quotient-fixing continuous free-profinite automorphisms '
 'to H-module automorphisms fixing the specified extension class. Gaschutz Lemma2.3,Corollary2.4, '
 'extension Lemma2.5 and proof on p5 lift the specified extension automorphism. Theorem5.1 pp12-13 and '
 'Example5.3 p13 concern the shared constituent obstructing descent; the latter has the actual A5 '
 'monodromy used here. The new certificate constructs integral maps and an IA lift at that cover. '
 'Root and generation independently reopened the primary theorem/proof. No unstated redundant-presentation '
 'hypothesis or Galois image assertion is imported.')
sources=[dict(source_key='AuditBleherChinburgLubotzky2021v3',
 url='https://arxiv.org/pdf/2004.08860v3',
 status='OPENED ORIGINAL V3; EXACT LIFTING MAP AND A5 EXAMPLE CHECKED',
 locator_and_access=source_note,dependent_statement_ids='E.2.29',
 record_file='work/audit_after13_references.bib',date=DATE,who=WHO,
 local_path=source,sha256=sha(source))]
event('SRC.AuditBleherChinburgLubotzky2021v3','used and rechecked in this run',source_note)

for path,rows,delim in [
 ('work/audit_after13_CHECK_EVENTS.tsv',events,'\t'),
 ('work/audit_after13_source_checks.csv',sources,',')]:
    with (ROOT/path).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=delim)
        writer.writeheader();writer.writerows(rows)

record=dict(statement_id='E.2.29',code=code,output=output,matrix_artifact=matrix,
 code_sha256=sha(code),output_sha256=sha(output),matrix_sha256=sha(matrix),
 exit_code=0,local_internal_seconds=own_internal,
 independent_external_seconds='1.779917296',
 independent_internal_seconds='0.956303676',
 registered_run_status='Parent owns registered run; this record preserves the frozen local and independent runs.',
 inputs='A5 permutations(123),(12345); BFS X-before-Y;61 non-tree cycles;44 cusp chains;first43 boundary columns and listed43 rows;standard seed index1;finite averages;all3600 section-cocycle pairs;IA cycle indices1,6.',
 arithmetic='Integer and rational matrices; explicit bounds on potentially large NumPy products; independent arbitrary-precision decisive matrix recheck.',
 scope='Actual integral nilpotent, boundary failure, explicit extension correction and IA certificate at one specified cover. Profinite lift uses the opened BCL theorem; no all-cover or Galois transporter is computed.',
 independent_audit='work/generation_A5_boundary_lift_audit.md')
(ROOT/'work/audit_after13_computation_records.json').write_text(json.dumps([record],indent=2)+'\n')
claims=list(csv.DictReader((ROOT/'work/audit_claims.csv').open()))
validation=dict(generated_utc=datetime.now(timezone.utc).isoformat(),
 assertion_count=len(claims),source_entry_count=len({r['note_id'] for r in claims}),
 status_counts=dict(Counter(r['status'] for r in claims)),
 changed_statuses=[],updated_claim_ids=[],
 canonical_new_result_ids=['E.2.29'],canonical_independently_audited_result_ids=['E.2.28'],
 addendum_event_count=len(events),source_record_count=len(sources),
 new_bibliography_keys=['AuditBleherChinburgLubotzky2021v3'],
 code_sha256=sha(code),matrix_sha256=sha(matrix),
 main_gate_movement='None claimed; explicit one-cover obstruction and exact all-affine characterization scopes retained.',
 tex_ready='work/E2_29_integrated_text.tex')
(ROOT/'work/audit_after13_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
(ROOT/'work/audit_after13_findings.md').write_text(
 '# E.2.29 and E.2.28 audit addendum\n\n'
 'E.2.29 is production-ready in work/E2_29_integrated_text.tex. The actual A5 cover has genus9,44 cusps, '
 'and affine/peripheral/proper ranks61/43/18. An explicit integral H-equivariant N has N-squared zero and sends an actual '
 'boundary class to a proper class detected by19440. Gamma=I+60N has integral inverse and a specified extension '
 'correction; BCL Cor2.4 lifts that extension automorphism. Its base action is IA by the actual exponent map '
 'and determinant-minus-one minor. The nonzero proper quotient value1166400 proves the one-cover descent failure.\n\n'
 'The final frozen code, output and complete matrix JSON are copied into output/RESEARCH_SA07/code. '
 'The parent owns the registered production run. Independent generation audit and byte-identical reconstruction passed.\n\n'
 'The independent AF1-AF8 proof check of E.2.28 is saved at work/triangle_affine_integral_completion_audit.md. '
 'In particular the local-conjugator transition maps and AF7 generator-image characterization pass. '
 'The proper-to-affine boundary-extension condition and discrete-representative/Galois gates remain explicitly scoped. '
 'No historical inventory status or main-gate movement is changed by this addendum.\n')
print(json.dumps(validation,indent=2))
