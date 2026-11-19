"""Integrate the independently audited degree-zero weight improvement."""
from pathlib import Path
import csv
import json
root=Path(__file__).resolve().parents[2]
section=root/'sections/part_c.tex'
text=section.read_text()
marker='\\begin{proposition}[The lower-endpoint gate over a trait]'
if '\\label{c:improved-zero-weight}' not in text:
    assert marker in text
    text=text.replace(marker,(root/'part_c/c4_improved_lower_endpoint.tex').read_text()+'\n'+marker)
text=text.replace('since eigenvalues on smooth projective cohomology are algebraic integers.',
 'since eigenvalues on smooth projective cohomology are algebraic integers '
 '\\citep[Expos\\\'e XXI, Theorem~5.2.2 and Corollary~5.5.3, pp.~385--386 and 393--395]{c_katzdeligne1973niveau}.')
section.write_text(text)
bib=root/'part_c/references.bib'
if '@misc{c_yamamura2026weights,' not in bib.read_text():
    bib.write_text(bib.read_text()+'\n'+(root/'part_c/c4_endpoint_sources.bib').read_text())
with (root/'part_c/results.csv').open('a',newline='') as f:
    w=csv.writer(f)
    w.writerow(['c:improved-zero-weight',
      'Degree-zero direct-image stalks at finite-residue points have weights at most0 for j0,1 for j1, and2j-2 for j>=2',
      'Proved for strictly special smooth-projective-family coefficients',
      'sections/part_c.tex, Proposition label c:improved-zero-weight',
      'Rapoport-Zink1982 Satz2.10 and proof2.13; Yamamura2026 Props1.5,1.7-1.8; curve selection and evaluation',
      '12:118-120; C.4',
      'General i0 endpoint now settled for j<=2. Does not assert optimality for j>=3 or a sharper geometric level.'])
    w.writerow(['c:threefold-weight-gate',
      'For a strictly semistable threefold, H3 inertia-invariant weights<=3 iff N:Gr4 to Gr2(-1) is injective iff weight-monodromy holds on H3',
      'Proved equivalence; general vanishing of the indicated kernel unresolved',
      'sections/part_c.tex, Corollary label c:threefold-weight-gate',
      'Two proved extreme monodromy isomorphisms; Poincare duality and strict weight decomposition',
      '12:118-120; C.4',
      'First residual normalized trait case j3; only possible excess weight4 remains.'])
events=[
 ['c:improved-zero-weight','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Opened full Yamamura PDF and RZ original pp40-43; re-proved the extreme H0/H1 monodromy maps, finite-extension descent and curve-selection reduction.'],
 ['c:improved-zero-weight','2026-11-19','GPT-6 Astra (OpenAI), /root/part_b','independent re-proof','Passed curve selection by g-parameter and height theorem, finite descent of geometric data, and equivariant evaluation without falsely descending all l-adic sections.'],
 ['c:improved-zero-weight','2026-11-19','GPT-6 Astra (OpenAI), /root/part_d','independent re-proof','Passed Picard-polarization argument for the next extreme map, strict weight-graded interpretation, and full fragment scope.'],
 ['c:improved-zero-weight','2026-11-19','GPT-6 Astra (OpenAI), /root','independent re-proof','Passed complete source-to-stalk chain; requested explicit product normalization when presenting dimension<j and justification of g extending to parameters, now supplied.'],
 ['c:improved-zero-weight','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','source correction','Rendered and visually checked Yamamura p10: higher-degree hard-Lefschetz twist prints i-d but must be d-i. Our proof uses independently established middle-degree maps only.'],
 ['c:threefold-weight-gate','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','N^3 and N^2 eliminate weights6,5; weight4 kernel is sole obstruction; equal dimensions by Poincare duality identify injectivity with the final monodromy isomorphism.'],
 ['c:threefold-weight-gate','2026-11-19','GPT-6 Astra (OpenAI), /root/part_d','independent re-proof','Passed precise H3 equivalence using strict generalized Frobenius weight decomposition and paired dimensions.'],
 ['c:threefold-weight-gate','2026-11-19','GPT-6 Astra (OpenAI), /root','independent re-proof','Passed the threefold iff and recorded the resulting strictly smaller C4 gate.']]
with (root/'part_c/CHECK_EVENTS.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t').writerows(events)
sources=[
 ['yamamura2026weights','opened full PDF and visually checked p10','https://arxiv.org/pdf/2608.01089v1','Props1.5,1.7,1.8;Theorem1.6 pp9-11;printed HL twist sign corrected'],
 ['rapoportzink1982','opened original full relevant proof','https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/UeberdielokaleZetafunktion.pdf','Satz2.10+(2.11) pp40-41;Satz2.13 proof pp41-43;Picard step p42'],
 ['katzdeligne1973niveau','opened theorem and corollary proofs','https://web.math.princeton.edu/~nmk/old/niveaucoho.pdf','ExposéXXI Theorem5.2.2 pp385-386;Cor5.5.3 pp393-395']]
with (root/'part_c/sources.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t').writerows(sources)
notes=root/'part_c/part_c_notes.md'
intro='''## Lower endpoint narrowed after checkpoint 03 (05:10 UTC)

The degree-zero direct-image weight bound now improves to b(j)=0,1,2j-2 for j=0,j=1,j>=2 at every finite-residue point, with precisely the strictly special smooth-projective-family coefficient scope. The first two extreme monodromy maps are re-proved using rational H0 positivity and polarizations of the Picard images of surface-to-curve restrictions. A complete curve-selection and equivariant-evaluation argument extends the local-field bound to all R0 stalks. B, D and root independently audited the proof. The original Yamamura p10 contains a printed hard-Lefschetz twist sign slip; our independent middle-degree argument avoids it and the correction is recorded.

Thus the lower endpoint is settled for j<=2. The first remaining normalized trait case is H3 of a strictly semistable threefold: only a possible weight4 inertia-invariant remains, and excluding it is proved exactly equivalent to the remaining N:Gr4->Gr2(-1) isomorphism, hence to weight-monodromy on H3. General j>=3 sharpness remains unresolved.

The proposed tautological-parity converse in C1 is now explicitly refuted by the positive pair E times P1. Product stability is proved and the rank3 versus rank4 correspondence-span computation is archived. This is a failed-method clarification, not movement on the unrestricted classification row. A superprojective cancellation route under externally algebraic parity is being audited separately and is not yet a claimed theorem.

'''
s=notes.read_text();notes.write_text(s.replace('# Part C research ledger\n\n','# Part C research ledger\n\n'+intro,1))
output={'main_lines':len(text.splitlines()),'events_added':len(events),'new_labels':['c:improved-zero-weight','c:threefold-weight-gate']}
(root/'code/part_c/integrate_improved_endpoint_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output))
