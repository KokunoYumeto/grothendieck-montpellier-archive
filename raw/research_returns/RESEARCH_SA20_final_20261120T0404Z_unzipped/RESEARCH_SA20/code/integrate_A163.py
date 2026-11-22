#!/usr/bin/env python3
"""Promote the fully audited relative aspherical-four comparison theorem."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
record_path = root/'logs/integrate_A163.json'
assert not record_path.exists(), 'This promotion is recorded once'
source = root/'agents/singularities_duality/logs/pending_aspherical_four_relative_comparison.tex'
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash == '0b3f3f3cbe0039b134492c190771d1d0288e3994efd77c05c8bf9507dfc22a36'
for rel in ['agents/higher_comparison/logs/aspherical_four_relative_comparison_independent_audit.md',
            'agents/higher_comparison/logs/A163_four_torus_checker_independent_audit.md']:
    assert (root/rel).is_file()
shutil.copy2(root/'RESEARCH_SA20_paper.pdf', '/tmp/RESEARCH_SA20_build33c_before34.pdf')
shutil.copy2(root/'logs/pdf_qa.json', root/'logs/pdf_qa_before_build34.json')

text = source.read_text()
text = text[text.index('Let $B$'):text.index('\\textbf{Source/provenance and scope.}')]
text = text.replace('\\textbf{Candidate theorem.}\\quad\n', '')
text = text.replace('AC.', 'A.163.')
text = text.replace('\\begin{proof}', '\\end{saresult}\n\n\\begin{proof}', 1)
text = text.replace("Definition18.2, printed pp.197--198, explicitly treats compact",
                    "Definition~18.2, printed pp.~197--198 \\cite{Ranicki1992TopologicalManifolds}, explicitly treats compact")
text = text.replace('relative-version paragraph on p.198,\nProposition18.3 and Theorem18.5, pp.198--201,',
                    'relative-version paragraph on p.~198,\nProposition~18.3 and Theorem~18.5, pp.~198--201,')
text = text.replace('Example24.16, printed p.278, gives',
                    'Example~24.16, printed p.~278 \\cite{Ranicki1992TopologicalManifolds}, gives')
text = text.replace('Annals of Mathematics175(2012),\n631--689, TheoremB and Proposition0.3, printed pp.633--635.',
                    'Annals of Mathematics~175 (2012),\n631--689, Theorem~B and Proposition~0.3, printed pp.~633--635\n\\cite{BartelsLuck2012Borel}.')
text = text.replace('TheoremB', 'Theorem~B').replace('Proposition0.3', 'Proposition~0.3')
text = text.replace('0.15173493099791813 seconds. The program certifies',
                    '0.15173493099791813 seconds. An independent rerun also passed\nall 24,473 checks in 0.16903232899858267 seconds; its complete output\nand code audit are retained with the authored records. The program certifies')
prefix = ('% AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 20 November 2026.\n'
          '% Full literal root and independent proof/source/code audits recorded separately.\n'
          '\\Needspace{10\\baselineskip}\n'
          '\\subsection{A.163. Relative comparison over aspherical four-manifolds}\n\n'
          '\\begin{saresult}{A.163}{Proved under stated hypotheses}{Assembly, the relative cylinder comparison, and the four-torus}\n\n')
suffix = ('\n\\paragraph{Scope and proof provenance.}\n'
          'We use the full opened originals at the precise printed locators cited\n'
          'above. This is our argument from those inputs and the previously\n'
          'audited A.135--A.136, rather than a theorem quoted verbatim from a\n'
          'source. We make no assertion that the assembly hypotheses hold for\n'
          'every aspherical four-manifold, that either exact sequence splits,\n'
          'or that the general free-top comparison is evaluated. The latter\n'
          'still contains the ordinary four-dimensional automorphism comparison\n'
          'and the remaining part of $\\beta_B$.\n')
target = root/'agents/singularities_duality/part_aspherical_four_relative_comparison.tex'
target.write_text(prefix+text.rstrip()+'\n'+suffix)

bib = root/'notes/root_references.bib'
assert 'BartelsLuck2012Borel' not in bib.read_text()
bib.write_text(bib.read_text()+'''\n\n@article{BartelsLuck2012Borel,
 author={Bartels, Arthur and L{\\"u}ck, Wolfgang},
 title={The {Borel} Conjecture for Hyperbolic and {CAT(0)}-Groups},
 journal={Annals of Mathematics},
 volume={175}, number={2}, year={2012}, pages={631--689},
 doi={10.4007/annals.2012.175.2.5},
 url={https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p05-p.pdf},
 note={Published original opened and read by root and independent agents; Theorem B and Proposition 0.3, pp. 633--635. Algebraic assembly and decoration conversion only; no four-dimensional geometric Borel theorem inferred.}
}\n''')
part = root/'parts/new_concordance_results.tex'
old = '\\input{agents/higher_comparison/part_RP3_equivariant_germs}\n'
new = '\\input{agents/singularities_duality/part_aspherical_four_relative_comparison}\n'
assert part.read_text().count(old) == 1
part.write_text(part.read_text().replace(old, old+new, 1))

audit = f'''# Root audit of A.163

Completed at {stamp}. Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), root.

**PASS under every stated hypothesis.** We read the complete core proof before the latest context compaction and reread its full middle at 03:21 UTC. We read the final common-collar, four-torus, and Bartels--Lück additions after a fresh 03:20:56 UTC clock. The final candidate SHA256 is `{source_hash}`. The promoted source differs only by the theorem wrapper, numbering, exact citations, typographic spacing, independent-run information, and removal of retrieval identifiers from the manuscript.

1. The mapping cylinder retains all three boundary labels. Its map is a relative homotopy equivalence with the actual relative TOP normal invariant in dimension 5+r, always at least six. Injective assembly forces that invariant to vanish. The universal PL reduction obstruction, with the same boundary labels, is the suspension of the relative difference class. No stable bundle lift is silently converted into an isotopy.
2. For r at least two the boundary preimage is connected in the universal cover and the cover is contractible. The equivariant relative-cell argument therefore proves precisely the required relative homotopy. For r=1 we retain the central evaluation class and remove it only under the stated PL-loop realization hypothesis.
3. The parameterized microbundle formula is a germ homeomorphism at every interpolation time, fixes the zero section over the trace base homeomorphism, and respects all boundary collars. It identifies the actual trace obstruction with the connecting maps in the comparison sequence.
4. The A.135 long exact sequence gives the stated component kernel, fundamental-group exact sequence, and higher isomorphisms. The pullback action on relative cohomology is trivial because both boundary restrictions are fixed. The component-kernel identification is an isomorphism of groups. Surjectivity on components uses the actual five-dimensional relative classification and orbit path lifting.
5. The four-torus translation loops are jointly PL and realize every central class. We reopened the full original Ranicki author PDF and read Definition 18.2 and its relative paragraph on pp. 197--198, Proposition 18.3/Theorem 18.5 on pp. 198--201, and Example 24.16 on p. 278. We checked the one-connective versus zero-connective assembly degrees 6--8.
6. We reopened the full published Bartels--Lück original and read Theorem B, Proposition 0.3 and the decoration-conversion proof on pp. 633--635. Finite aspherical B is torsion-free by the finite cohomological-dimension argument. The cofiber between the one-connective and full spectra has no positive homotopy groups, so finite base dimension four makes the homology comparison an isomorphism for j at least six. No four-dimensional Borel assertion is used.
7. We authored and executed the exact finite T4 checker after checking its staircase construction. It verifies 24,473 assertions, all passing, with f-vector (81,1215,4050,4860,1944), binary boundary ranks (80,1131,2913,1943) and Betti numbers (1,4,6,4,1). The product construction establishes the PL type independently of those numerical invariants. The independent agent read and reran the complete checker and restored our original log byte for byte.

The full independent mathematical audit and its Bartels--Lück addendum are in `agents/higher_comparison/logs/aspherical_four_relative_comparison_independent_audit.md`; the independent construction and code audit is in `agents/higher_comparison/logs/A163_four_torus_checker_independent_audit.md`. The proof does not compute the free-top fibre, all of beta_B, or the endpoint condition. We do not count this additional class of relative comparisons as qualifying movement on the remaining general gate.
'''
(root/'notes/root_A163_audit.md').write_text(audit)

results = root/'notes/root_results.csv'
with results.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
assert not any(r['id']=='A.163' for r in rows)
rows.append(dict(zip(fields,[
    'A.163', 'Relative PL-TOP comparison over aspherical real PL four-manifolds under stated assembly and central-loop hypotheses; explicit four-torus and hyperbolic/CAT(0) scope.',
    'Proved under stated hypotheses', str(target.relative_to(root)),
    'A.135; A.136; Ranicki1992 Definition18.2 Proposition18.3 Theorem18.5 pp197-201 Example24.16 p278; BartelsLuck2012 TheoremB Proposition0.3 pp633-635',
    'A.1(b)',
    'Full root and independent proof/source audits PASS; root and independent finite T4 runs each pass24473 checks. Fully boundary-fixed comparison only; ordinary-loop beta contribution vanishes under extra central realization. General free-top beta, endpoint and component-image gates remain. No qualifying movement credit.'
])))
with results.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader(); writer.writerows(rows)
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root; inherited configuration'
with (root/'notes/root_checks.tsv').open('a') as f:
    for kind, outcome in [
      ('targeted full literal proof and original-source check', 'PASS: complete A.163 proof and final extensions read; actual relative normal invariant, trace identification, assembly degrees, group structure, central realization and published decoration conversion checked. notes/root_A163_audit.md; no general free-top closure or qualifying movement.'),
      ('computation or formal certificate', 'PASS: 24473 exact finite T4 checks in0.15173493099791813seconds; independent rerun24473PASS in0.16903232899858267seconds. Complete vertices/facets and algebra outputs retained. Finite model only, not computational proof of assembly or isotopy.')]:
        f.write('\t'.join(['A.163',stamp,who,kind,outcome])+'\n')

report=root/'code/update_report.py'
text=report.read_text().replace('A.119–A.162|','A.119–A.163|',1)
needle='A.139–A.141 compute stated sphere and realization cases only.'
assert text.count(needle)==1
text=text.replace(needle, needle+' A.163 computes the fully boundary-fixed cylinder comparison for aspherical four-manifolds under precise assembly and central-loop hypotheses, including T4 and the stated hyperbolic/CAT(0) scope; it also kills the ordinary-loop contribution under those hypotheses. The general free-top beta and endpoint gates remain, so this additional class receives no qualifying-movement credit.',1)
report.write_text(text)

record={'utc':stamp,'candidate_sha256':source_hash,
        'promoted_source':str(target.relative_to(root)),
        'promoted_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'qualifying_movement':False,
        'open_original_rows':['A.1(b)','A.5','C.2(b)'],
        'independent_checks':24473,'root_checks':24473}
record_path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
