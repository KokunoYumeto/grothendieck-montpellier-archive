#!/usr/bin/env python3
"""Record source-audited scope correction and three-dimensional subgroup theorem."""
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
assert r'\begin{saresult}{C.023}' in (root/'agents/singularities_duality/part_C.tex').read_text()
assert r'\begin{saresult}{A.130}' in (root/'parts/parametric_concordance.tex').read_text()
p=root/'code/update_report.py';s=p.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line=line.replace('A.119–A.129|','A.119–A.130|')
        line+=' A.130 embeds a countable direct sum of Z into the components of every closed orientable three-manifold with infinite fundamental group, detected even after forgetting all TOP boundary restrictions. This subgroup does not determine the whole component group.'
        lines[i]=line
    elif line.startswith('C.2(a) projective CM chain|'):
        lines[i]='C.2(a) projective CM chain|Literal mixed-dimensional claim refuted; complete componentwise repair proved|C.011–C.015,C.019,C.023|All seven conditions, endpoint injection and negative-twist reduction hold for pure CM projective schemes using the canonical module. Without purity, P2 disjoint a point has affine complement but fails the single-global-dimension H0 comparison. C.023 proves the full seven-condition chain with threshold s−m on each clopen pure-dimensional component X_s, requiring only H0 injection when s=m and no condition when s<m. A second projective example proves that the endpoint clause cannot be dropped on components of dimension exactly m.'
s='\n'.join(lines)+'\n'
needle='| RESEARCH_SA20_study/study/STUDY.md:775–780 |'
addition='| RESEARCH_SA20_study/study/STUDY.md:53–54,979–986,1010–1011; supplied PROMPT(20261119-110351).md:109,229 | Projective Cohen–Macaulayness alone does not give the single-global-dimension chain on disconnected mixed-dimensional schemes. Require purity or use threshold s−m separately on each clopen piece; the endpoint is not automatic on components of dimension m. | C.023 |\\n'
assert needle in s
s=s.replace(needle,addition+needle,1)
p.write_text(s)
now=datetime.now(timezone.utc).isoformat()
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### Post-checkpoint10 scope correction and checked subgroup theorem — '+now+'\n\nC.023 is integrated after complete root and lie_theory audits. It refutes the literal mixed-dimensional global-threshold reading of C.2(a), including the supplied study claim, and proves the full componentwise seven-condition replacement. The root independent exact certificate checks53 cases in0.607157170001301s. This repairs an original scope omitted by the previous pure-dimensional statement; it is recorded openly rather than rewriting historical review tables.\n\nA.130 is also integrated: all closed orientable three-manifolds with infinite fundamental group have a countable free abelian subgroup in their PL/definable concordance components. This is a subgroup theorem only and does not count as completion or strict reduction of the full component-computation gate. The higher PL/TOP full-space and PL-to-definable comparison gates remain.\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('SA20-W2/125003;R10\t'+now+'\tGPT-6 Astra, inherited configuration, root\trefuted, with refined statement C.023\tThe supplied pure-global-dimension equivalence fails without purity on mixed-dimensional projective CM schemes; full componentwise repair proved and independently checked. Exact supplied lines in report.\n')
print(now)
