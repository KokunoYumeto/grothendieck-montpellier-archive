#!/usr/bin/env python3
"""Record the audited universal B2(c) criterion and correct current A1 scope."""
from pathlib import Path
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[1]
assert r'\begin{saresult}{B.082}{Proved}' in (root/'agents/tensor_and_finite/part_B.tex').read_text()
p=root/'code/update_report.py'
lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line=line.replace('The remaining closed unstable cases are','The remaining closed unstable component cases are')
        line += ' Separately, the unrestricted unstable higher PL/TOP concordance homotopy type for arbitrary manifolds remains to be computed: E(K) is a component presentation, the Whitehead-spectrum model is stable, and the sphere homotopy-fibre formula does not evaluate all higher groups.'
        lines[i]=line
    elif line.startswith('B.2(c) specified inclusion criterion|'):
        lines[i]='B.2(c) specified inclusion criterion|Proved in full arbitrary-ring generality|B.008,B.009,B.013–B.082|B.082 gives an explicit necessary-and-sufficient coefficient-syzygy criterion for every unital inclusion of commutative rings. Form the determinant-colon coefficient ring C and its polynomial-value module E; test epicness by finite matrix certificates, the two kernel groups K1 and K2 by Tor through degree two and explicit transgressions, and the two coefficient arrays by delta0. The proof identifies the entire tensor kernel and cokernel and therefore proves existence and uniqueness. It includes all non-Noetherian and nonflat cases, recovers B.080 when C is flat, and checks the nonflat forest and flat cusp examples directly. The many earlier structural classifications remain useful applications. No uniformly terminating algorithm for arbitrary infinite rings or automatic higher plethory coherence is asserted.'
    elif line.startswith('C.2(a) projective CM chain|'):
        lines[i]=line.replace('|Proved|','|Proved for pure dimension; literal mixed-dimension scope under audit|').replace('Gorenstein is not imposed silently.','Gorenstein is not imposed silently. A projective Cohen–Macaulay scheme may have disconnected components of different dimensions; the literal scope and componentwise endpoint repair are being checked separately and are not yet promoted.')
p.write_text('\n'.join(lines)+'\n')
p=root/'notes/root_B082_universal_audit.md'
s=p.read_text().replace('18:22 UTC','18:20–18:22 UTC')
s+='\n## Final consistency calculations checked\n\nWe also read the added sign comparison and both explicit examples in full. For the nonflat forest, the Tor rows split by monic-basis index pairs; their exact sequences give K1=K2=0 and T1=(S/R)^16 without assuming the positive Tor groups of S vanish. The two identities for Q=X^4+X^2 give precisely zero low-low coefficient obstruction. For the flat cusp, E contains K/V as a split summand. The two long exact sequences identify Tor2(K/V,K/V) with the kernel of V⊗V→K⊗V; the displayed β⊗1−1⊗β is detected nontrivially after residue reduction. Its split image is the previously established Ω tensor kernel. These are algebraic consistency calculations, not additional finite program certificates.\n'
p.write_text(s)
now=datetime.now(timezone.utc).isoformat()
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### Post-review05 original-row closure — '+now+'\n\nOriginal B.2(c) is now closed by B.082 for arbitrary unital inclusions of commutative rings. Root and lie_theory completed independent checks of the finite matrix criterion, total-complex signs, explicit transgressions, cokernel calculation and full two-layer kernel filtration. Root also checked the final flat/nonflat consistency examples. The theorem is a universal arithmetic and syzygy criterion, with all tests defined from coefficient data before Ω tensor powers; it does not require flatness or finiteness. This is completion of the original inclusion question, not another special case. It is eligible for review06 and was not counted at review05. Detailed audit: notes/root_B082_universal_audit.md.\n\nScope correction retained for the main A.1(b): beyond the remaining low-dimensional component cases and PL-to-definable higher comparison, the full unrestricted unstable higher PL/TOP homotopy type remains uncomputed. E(K), stable Whitehead models and the special sphere homotopy-fibre model are distinguished explicitly. Correcting this scope wording is not itself qualifying movement.\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('B.082\t'+now+'\tGPT-6 Astra (OpenAI, ChatGPT Pro mode), root\ttargeted proof check\tPASS: complete universal matrix/Tor/transgression criterion and both consistency examples; original B2(c) closed; see root_B082_universal_audit.md.\n')
print(now)
