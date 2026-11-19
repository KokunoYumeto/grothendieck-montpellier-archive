"""Serialize the independent, manually read full root doubts audit.

The decisions below were made after reading all 1,545 doubts lines and the
specified transcription passages. This program validates and serializes them;
it does not generate mathematical verdicts from keyword searches.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path('/workspace/scratch/26604d0a9a98')
AUDIT = ROOT / 'work/global_audit'
OUT = AUDIT / 'outputs'
OUT.mkdir(exist_ok=True)
DOUBTS = 'sources/SA15_notes/pro/MPL_7_061-072+8_001-078_doubts.md'
TEX = 'sources/SA15_texts/pro/MPL_7_061-072+8_001-078_transcription.tex'
LOC = 'SA15_texts/pro/MPL_7_061-072+8_001-078_transcription.tex:'
SCHEMA = ['cote', 'scan', 'line', 'reading', 'alternative', 'evidence', 'weight', 'confidence']
NOW = datetime.now(timezone.utc).isoformat(timespec='seconds')

rows = [
    {
        'cote': '8', 'scan': '002', 'line': LOC + '248–263',
        'reading': 'First triangle: ℓ•^G[−1], with tentative marginal P; second triangle: ℓ•^G[1]^(p)=P^(p).',
        'alternative': 'Check both shift signs, the marginal identification P, and whether a rotation or a changed convention is intended; do not choose a sign from consistency alone.',
        'evidence': 'If the same P is intended, [−1] and [1] differ by two degrees. The intervening two-term models and the arrows labelled degree 1 make this consequential for the triangle. Doubts:133–151,1255–1257. Existing 8/002 row at line274 concerns Frobenius/base notation and does not record this shift discrepancy.',
        'weight': 'High: changes cohomological degrees and the identification of a factor of the triangle.',
        'confidence': 'High mathematical alarm conditional on the same P; ink and shift convention undecided',
    },
    {
        'cote': '8', 'scan': '012', 'line': LOC + '681–687',
        'reading': 'Stack-descent margin deletes H₀(ℓ), H₀(ℓ̌′[1])≃0 and inserts uncertain H₁(ℓ•)—H₁(ℓ′•), followed by a diagram and local-freeness wording.',
        'alternative': 'Recheck the degree, dual, shift, relation sign, cancellation boundaries, and the objects required to be locally free; no single repaired criterion is supported by the supplied text.',
        'evidence': 'The margin qualifies the question whether the enriched categories are stacks. Replacing a deleted vanishing condition by an asserted equality between differently indexed homology objects would change the hypotheses. The following t*,ω diagram does not resolve the overwritten criterion. Doubts:244–250,1295–1297. P78-C021/P78-P007 already preserve the unfinished stack question.',
        'weight': 'High: determines the hypotheses of a proposed descent criterion.',
        'confidence': 'High importance; reconstruction and ink undecided',
    },
    {
        'cote': '8', 'scan': '014', 'line': LOC + '754–756;770–782',
        'reading': 'Upper-left object M^p|M in the square with lower-left M^(p), upper-right t′ and lower-right t′^(p).',
        'alternative': 'M is the type-compatible candidate if the upward arrow is the F_M:M^(p)→M specified immediately before; verify the ink and the arrow identification.',
        'evidence': 'Line756 explicitly factors F_M:M^(p)→M through t′^(p). The large diagram on lines779–782 again places M between ω and t′. An extra upper Frobenius twist would change this factorization. Doubts:263–268,1303–1305. The existing 8/013 row ends at line743 and treats a separate Frobenius-descent issue.',
        'weight': 'High: changes the source/target of Frobenius and the reconstructed exact diagram.',
        'confidence': 'High for the mathematical type check; ink undecided',
    },
    {
        'cote': '8', 'scan': '018', 'line': LOC + '904–923',
        'reading': 'Left vertical arrow in the compatibility square labelled φ*(ω)|φ*(v).',
        'alternative': 'φ*(v) is type-compatible, if v is the preceding morphism of triangles; preserve the alternative v|σ for the name of that morphism.',
        'evidence': 'The endpoints are φ*(T(ω)) and φ*(T(ω′)). Lines905–912 define u and v, and line919 says φ*(v) is determined by u as T(u). Thus φ*(ω) is an object where a morphism is needed. Doubts:304–307,1319–1321. No existing reading row records this compatibility-arrow issue.',
        'weight': 'High: changes the definition of morphisms in the proposed enriched category.',
        'confidence': 'High mathematical type check; ink undecided',
    },
    {
        'cote': '8', 'scan': '034', 'line': LOC + '1446–1454',
        'reading': 'The full A-action λ↦λ_M is by W-autom|endom commuting with F_M.',
        'alternative': 'W-endomorphisms for λ∈A; W-automorphisms only after restricting to λ∈A×.',
        'evidence': 'An action of the whole ring A sends 0 to the zero endomorphism. Also π_M=F_M^f cannot be an automorphism of the nonzero integral finite free W-module: p=uπ^e would then act invertibly, whereas p is not a unit in W. Inverting p changes the category. Doubts:522,1371–1373. P78-C036 already treats the integral A-linear Dieudonné modules, but the reading register lacked this distinction.',
        'weight': 'High: distinguishes integral module data from an action of units or an isocrystal.',
        'confidence': 'High mathematical type check; ink undecided',
    },
    {
        'cote': '8', 'scan': '056', 'line': LOC + '2009–2013',
        'reading': 'Tate-twisted semilinear action x↦τ(x|g)g(x).',
        'alternative': 'τ(g)g(x) is the type-compatible candidate.',
        'evidence': 'τ is the Tate character of the Galois group π, whereas x is a scalar in C. The boxed equation immediately below reads g(x₁)=τ(g)⁻¹χ_π(g)x₁ and supplies an internal check. Doubts:759,767,1461. The existing 8/056 row at2016;2020 concerns A× normalization and inertia quantifiers, not this argument of τ.',
        'weight': 'High: determines the Galois action and the period eigen-equation.',
        'confidence': 'High mathematical type check; ink undecided',
    },
]

source_spans = [
    (DOUBTS, 1, 220, '11017d', 'complete direct textual read'),
    (DOUBTS, 221, 460, 'a65aca', 'complete direct textual read'),
    (DOUBTS, 461, 700, 'fe7229', 'complete direct textual read'),
    (DOUBTS, 701, 940, '69b5f8', 'complete direct textual read'),
    (DOUBTS, 941, 1180, '110996', 'complete direct textual read'),
    (DOUBTS, 1181, 1400, '698387', 'complete direct textual read'),
    (DOUBTS, 1401, 1545, 'af80cb', 'complete direct textual read'),
    ('work/root_review/readings_c7.json', 1, 32, 'previous full read; b8b33d repeated', 'all three existing rows read'),
    ('work/root_review/readings_c8.json', 1, 372, 'previous full read; b8b33d repeated', 'all 37 existing rows read'),
    (TEX, 1, 220, '1fc3c2', 'complete passage read: cote7/061–072'),
    (TEX, 620, 930, 'd3bd42', 'complete passage read: cote8/010–018 and start019'),
    (TEX, 235, 325, '6c0fc3', 'complete selected passage read'),
    (TEX, 1170, 1275, '6c0fc3', 'complete selected passage read'),
    (TEX, 1427, 1466, '6c0fc3', 'complete selected passage read'),
    (TEX, 1678, 1704, '6c0fc3', 'complete selected passage read'),
    (TEX, 1785, 1811, '6c0fc3', 'visible selected passage; surrounding output truncation is not counted'),
    (TEX, 1994, 2030, '6c0fc3', 'complete selected passage read'),
    (TEX, 2206, 2245, '6c0fc3', 'complete selected passage read'),
    (TEX, 2620, 2690, '6c0fc3', 'complete selected passage read'),
    (TEX, 230, 282, '6e3043', 'final direct recheck of shift alarm'),
    (TEX, 674, 690, '6e3043', 'final direct recheck of overwritten stack criterion'),
    (TEX, 746, 782, '6e3043', 'final direct recheck of Frobenius diagram'),
    (TEX, 900, 925, '6e3043', 'final direct recheck of morphism compatibility square'),
    (TEX, 1440, 1458, '6e3043', 'final direct recheck of integral A-action'),
    (TEX, 1995, 2018, '6e3043', 'final direct recheck of Tate-character argument'),
]

def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

inputs = {p: {'sha256': sha(p), 'lines': len((ROOT/p).read_text().splitlines())}
          for p in [DOUBTS,TEX,'work/root_review/readings_c7.json','work/root_review/readings_c8.json']}
assert inputs[DOUBTS]['lines'] == 1545
existing = []
for name in ['readings_c7.json','readings_c8.json']:
    existing += json.loads((ROOT/'work/root_review'/name).read_text())
assert len(existing) == 40
assert len(rows) == 6
assert all(list(r) == SCHEMA for r in rows)
assert len({(r['cote'],r['scan'],r['line'],r['reading']) for r in rows}) == len(rows)
assert all(r not in existing for r in rows)
covered = set()
for p,a,b,_,_ in source_spans:
    assert 1 <= a <= b <= len((ROOT/p).read_text().splitlines()), (p,a,b)
    if p == DOUBTS:
        covered.update(range(a,b+1))
assert covered == set(range(1,1546))

target = ROOT/'work/root_review/additional_readings.tsv'
if target.exists():
    with target.open(newline='') as f:
        old = list(csv.DictReader(f,delimiter='\t'))
    assert old == rows, 'Refuse to overwrite independently added rows.'
else:
    with target.open('w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

with (AUDIT/'root_doubts_source_read_log.tsv').open('w',newline='') as f:
    fields = ['run_id','recorded_at_utc','reader','source','line_start','line_end','read_kind','tool_output','source_sha256','qualification']
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    for p,a,b,tool,kind in source_spans:
        writer.writerow(dict(zip(fields, ['SA15-20261119/root-doubts-independent',NOW,'GPT-6 Astra Pro; effort not exposed',p,a,b,kind,tool,sha(p),'Textual evidence only; inherited reports of scan inspection are not a scan inspection in this run.'])))

report = {
    'run_id': 'SA15-20261119/root-doubts-independent',
    'recorded_at_utc': NOW,
    'reader': 'GPT-6 Astra Pro',
    'effort': 'not exposed',
    'inputs': inputs,
    'doubts_lines_read': 1545,
    'doubts_coverage_complete': True,
    'existing_readings_compared': 40,
    'additional_high_impact_readings': 6,
    'additions': [{'cote':r['cote'],'scan':r['scan'],'line':r['line']} for r in rows],
    'new_claim_or_problem': None,
    'claim_problem_coverage': {
        'shift and proposed triangles': ['P78-I014','P78-I015','P78-C013','P78-C014'],
        'stack hypotheses and enriched morphisms': ['P78-C019','P78-C021','P78-P007'],
        'BT1 Frobenius diagram': ['P78-C022','P78-P007'],
        'integral A-linear action': ['P78-C036'],
        'Tate character and periods': ['P78-C045','P78-C046','P78-C047','P78-P015'],
    },
    'other_substantive_alarms_reviewed': [
        {'location':'7/062–065','decision':'No additional row','reason':'Formal-smooth abbreviation is internally expanded on line61; existing claims preserve formal smoothness. This audit does not replace it by finite-type smoothness.'},
        {'location':'8/016','decision':'No additional row','reason':'The uncertain p-faite|p-finie qualifier occurs beside an explicit perfect-complex/amplitude condition. Without scans no further mathematical distinction can be supported beyond preserving the uncertainty.'},
        {'location':'8/042','decision':'No additional reading row','reason':'The two invariant lattices are written separately; the mathematical common-lattice issue is already treated by P78-C038 and its proof. No additional ink ambiguity has been established.'},
        {'location':'8/061','decision':'No additional row','reason':'T_p|V_p in the rational/isogeny setting requires convention awareness, already supplied by the explicitly Q_p-linear target; no new independent proposition is extracted.'},
        {'location':'8/071','decision':'No duplicate row','reason':'Existing reading at2552–2583 already records the group-form, prime/exponent and comparison-torsor ambiguities.'},
        {'location':'8/073','decision':'No duplicate row or new claim','reason':'The unfinished comparison map is already registered; canceled coefficient sketches are not promoted to established claims.'},
    ],
    'preservation': {
        'original_inputs_modified': False,
        'existing_root_readings_modified': False,
        'claims_or_problems_modified': False,
        'ink_decisions': 0,
        'new_literature_searches': 0,
        'scan_images_opened_in_this_audit': 0,
        'warning': 'The supplied doubts include earlier visual-audit reports. Those reports were read as historical textual evidence, not represented as a new visual inspection.'
    },
    'validation': {'schema_exact':True,'no_exact_duplicate_reading':True,'full_doubts_line_union':True},
}
(OUT/'root_doubts_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

markdown = '''# Independent full root-package doubts audit

The entire supplied `MPL_7_061-072+8_001-078_doubts.md` was read: **all 1,545 lines**, including both the inherited doubts and the complete later visual-audit reports. The accompanying source-read log records the seven consecutive reads and the manuscript passages checked. All **40 existing root reading rows** were compared: three for cote 7 and 37 for cote 8. The audit adds **six high-impact mathematics-dependent rows**, using the exact required eight-column schema, in `work/root_review/additional_readings.tsv`.

## Added reading alarms

| Cote/scan | Exact transcription lines | Mathematical reason |
|---|---|---|
| 8/002 | 248–263 | The two apparent identifications of P use [−1] and [1]. They cannot be treated as the same shifted complex without checking the marginal P, rotation and convention. |
| 8/012 | 681–687 | Overwritten homology indices, a dual/shift and local-freeness wording qualify the proposed stack criterion. No exact replacement hypothesis can be read securely from the supplied text. |
| 8/014 | 754–756;770–782 | The uncertain M^p|M must be checked against the explicitly written Frobenius map M^(p)→M and its factorization through t′^(p). |
| 8/018 | 904–923 | The compatibility square requires a morphism φ*(v); φ*(ω) would name an object. This affects the proposed category's morphisms. |
| 8/034 | 1446–1454 | A full ring action of A is by endomorphisms. Only units act by automorphisms on the integral W-module. Zero and the uniformizer rule out the blanket automorphism reading. |
| 8/056 | 2009–2013 | The Tate character takes a Galois element g as its argument, not the scalar x. The adjacent boxed period equation supplies an internal check. |

These are reading alarms, **not transcription corrections**. No scans are supplied; the actual ink remains undecided. Mathematical compatibility does not establish what the author wrote. In particular, the stack margin remains an uncertain, overwritten proposal rather than a reconstructed theorem.

## Claim and problem completeness

No additional distinct claim or problem is established by these doubts. The enriched-category questions are already recorded in P78-C019, P78-C021 and P78-P007; the BT1 diagram is part of P78-C022; the integral A-module calculation is P78-C036; and the period action is already within P78-C045–047 and P78-P015. The extra rows sharpen the source conditions attached to these records. They do not justify a second copy of a proposition.

The other material alarms are already represented in the root register or mathematical audit: the site change on 7/062, the Frobenius-descent problem on 8/013, relative Ext degrees, the triangular-matrix convention, the gauge sign, ramification and rank factors, invariant-lattice construction, jet dimensions and variance, tensor bases, period normalization and inertia quantifiers, comparison-torsor forms, the unfinished comparison map, and the purity twist. The separate lattice assertions on 8/042 require the existing common-lattice argument; they do not expose a new ink ambiguity. The ambiguous qualifier next to the explicitly perfect complex on 8/016 was preserved without inventing an additional hypothesis. The canceled comparison sketch on 8/073 was not promoted to a new assertion.

## Evidence and limits

The older visual-audit entries are part of the supplied textual evidence. Their reports that particular scans or crops were inspected are **not** a scan inspection performed in the current run. No new literature search was needed for this narrow audit: all six additions follow from the actual neighboring formulas and the already registered mathematical questions. No original input, existing reading row, claim or problem was edited. The audit program validates the exact schema, absence of identical existing rows, source hashes, and complete line coverage of the doubts file; it does not manufacture mathematical verdicts.
'''
(AUDIT/'root_doubts_audit.md').write_text(markdown)

assert sha('work/root_review/readings_c7.json') == inputs['work/root_review/readings_c7.json']['sha256']
assert sha('work/root_review/readings_c8.json') == inputs['work/root_review/readings_c8.json']['sha256']
print(json.dumps({'doubts_lines_read':1545,'existing_readings':40,'additional_readings':6,'new_claims':0,'new_problems':0,'schema':SCHEMA,'output':str(target),'validation':'passed'},ensure_ascii=False,indent=2))
