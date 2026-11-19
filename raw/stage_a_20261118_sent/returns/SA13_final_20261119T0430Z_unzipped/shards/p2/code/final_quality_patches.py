"""Manual final scope corrections and Codex-only item authorship.

Run after the core author/refine builders. No verdict row is created or changed.
The groups below are editorial decisions, not automated topic clustering.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, csv

OUT = Path(__file__).resolve().parents[1]
claims = json.loads((OUT / 'claims.json').read_text())
items = json.loads((OUT / 'items.json').read_text())
cm = {int(x['id'].split('-')[-1]): x for x in claims}

completion_statement = ('Let R⊂Rbar be regular local domains of the same dimension with the same residue '
                        'field and mRbar=mbar. Their completions are canonically isomorphic; every idealI '
                        'ofR contracts from IRbar toI, principality of IRbar descends toI, and Frac(R)∩Rbar=R.')
completion_fate = ('The entire Lemma2 is recovered by the exact printed continuation33:173→137→135. '
                   'The common-completion, ideal-contraction and principality statements are independently '
                   'checked; neither ring is asserted complete. The original article/edition remains '
                   'unidentified, separately from the now recovered mathematical statement. '
                   'Stacks10.97.3 supplies the opened faithful-flatness input.')
completion_proof = ('The regular associated graded rings are polynomial rings in the same minimal '
                    'generators over the common residue field, so R/m^q≅Rbar/mbar^q for everyq. Passing '
                    'to limits gives equal completions. Faithful flatness of each local completion gives '
                    'ideal contraction; minimal-generator counts give descent of principality. '
                    'If z/t∈Frac(R)∩Rbar then z∈tRbar∩R=tR.')
cm[157]['modern_statement'] = cm[157]['statement'] = completion_statement
for key in ('literature_fate', 'fate', 'present_status'):
    cm[157][key] = completion_fate
cm[157]['reconstruction'] = completion_proof
cm[157]['class'] = cm[157]['classification'] = 'E'
cm[157]['confidence'] = 'high'
cm[157]['references'] = ['Abhyankar1956:unidentified exact source lead only', 'Stacks00MC:Lemma10.97.3']
cm[157]['refs'] = ['Abhyankar1956', 'Stacks00MC']
continuations = [
    dict(file='pro/MPL_33_098-146_transcription.tex', cote=33, scan=137, start=957, end=983),
    dict(file='pro/MPL_33_098-146_transcription.tex', cote=33, scan=135, start=908, end=910),
]
for loc in continuations:
    if loc not in cm[157]['lines']:
        cm[157]['lines'].append(loc)
    scan = f"{loc['cote']}:{loc['scan']:03d}"
    if scan not in cm[157]['scans']:
        cm[157]['scans'].append(scan)

fix198 = ('For H¹ monodromy, reduce through normal open restriction and a generic transverse curve '
          'to a smooth projective curve after a generic-parameter field extension with a suitable '
          'dominating valuation, and subsequent finite extensions as needed, using the boundary '
          'localization sequence. The required open-image condition on inertia is the separate issue C-SA13-227.')
cm[198]['modern_statement'] = cm[198]['statement'] = fix198
fate198 = ('The proposition is left blank at34:51, but K34-04§5 supplies the same reduction. '
           'SGA7I3.5 and Illusie1994§1–3 establish the resulting local monodromy theorem; exact manuscript '
           'formulation remains unfinished. The Grassmannian/function-field extension is generally '
           'transcendental, not merely finite; the valuation/inertia comparison is retained as C-SA13-227.')
for k in ('literature_fate', 'fate', 'present_status'):
    cm[198][k] = fate198
fates = {
    203: ('The manuscript invokes Grothendieck1966 Proposition4.4 and extends its argument. The1966 paper '
          'title/publication and citation are verified, but the exact Proposition4.4 text was not available '
          'through the opened publisher page. The primary comparison is therefore partial: geometric '
          'semisimplicity is verified, while the exact radicial constant-part descent and the scope of '
          'this adaptation still require proposition-level collation. ClassC records that specific incomplete '
          'identification; it is not a declaration that the correctly formulated modern abelian-scheme theorem is open.'),
    204: ('The page calls this an adaptation of Grothendieck1966Prop4.4 using Mordell–Weil/trace descent. '
          'Verified geometric semisimplicity removes nontrivial unipotent geometric monodromy, but the '
          'constant/radicial descent additionally needs the abelian-scheme theorem whose exact Proposition4.4 '
          'text was not collated. ClassC marks this precise source-identification gap, not a newly open modern conjecture.'),
}
for n, fate in fates.items():
    cm[n]['classification'] = cm[n]['class'] = 'C'
    cm[n]['confidence'] = 'medium'
    for k in ('literature_fate', 'fate', 'present_status'):
        cm[n][k] = fate

# id, title, kind, claim numbers, concise modern object, reconstruction limits
groups = [
    (213, 'Congruence kernels and the prime-to-ell inertia reduction', 'other', list(range(168,172)),
     'For finitely generated Z_ell modules, the congruence kernel is pro-ell; prime-to-ell image is finite. A compact rational representation has a stable lattice, and its inertia action factors through an open ell-primary tame quotient after finite extension.',
     'The lattice, finite-image and quotient statements remain separate claims; the source inverse-image typo does not change the construction.'),
    (214, 'Quasi-unipotent representations and the restricted algebraic envelope', 'other', list(range(172,180)),
     'For characteristic-zero ell-adic representations of a profinite group, relate quasi-unipotence to the identity component of the algebraic image and construct the fixed-open-subgroup vector extension for representations with commutative unipotent identity component.',
     'This is a restricted envelope, distinct from the all-representation analytic/algebraic envelopes on183–196. Splittings exist only with their stated hypotheses and are not generally unique.'),
    (215, 'Finite coinvariants, solvable image and the radical-isogeny error', 'self-flagged step', list(range(180,184)),
     'The finite-coinvariant criterion forces the identity component of a virtually solvable inertia image to be unipotent. The attempted extension to an arbitrary connected image uses a false radical-to-abelianization isogeny. The residue cyclotomic condition then gives arithmetic quasi-unipotence and the essentially abelian finite-image consequence.',
     'Keep the proved solvable criterion, the refuted radical inference and the arithmetic applications distinct; a semidirect-product counterexample does not refute the solvable theorem.'),
    (216, 'The general geometric local-monodromy conjecture', 'conjecture', [184],
     'For finite-type separated schemes over a henselian discretely valued field and ell distinct from residue characteristic, the source proposes quasi-unipotence on every degree of ordinary and compact-support geometric cohomology.',
     'The conjectural occurrence and its promised two proof routes are preserved separately from later conditional proofs and the established general theorem.'),
    (217, 'Degreewise inertia traces, Weil weights and rational forms', 'conjecture', list(range(185,189)),
     'The source asks for degreewise integral ell-independent inertia traces, compatibility for Weil elements, stated eigenvalue weights, and a common rational local-monodromy representation.',
     'These have different quantifiers and current fates. Nonnegative trace is already false, and a rational form is stronger than equality of characteristic polynomials.'),
    (218, 'Regular trait approximation and the spreading proof', 'self-flagged step', list(range(189,193)),
     'In equal characteristic zero, resolve finite-type approximations of the trait and its parameter divisor; use normal-crossing Abhyankar/Kummer inertia and proper cohomological constructibility to spread the representation. The nonproper extension needs an additional direct-image/base-change premise.',
     'No resolution result in positive or mixed characteristic is inferred. The normal-crossing group is the prime-to-p quotient, and a common adic lisse open is not an arbitrary infinite intersection.'),
    (219, 'Descent and the generic-curve reduction for H1', 'self-flagged step', [193,194,195,196,197,198,223,227,228],
     'Use duality, localization and proper or finite descent to reduce monodromy; for H1 use a generic complete-intersection curve over a parameter function field, a suitable dominating valuation and the boundary sequence, then the smooth-curve nilpotence bound.',
     'The generic-parameter extension is generally transcendental. The valuation must give the required open inertia image. Preserve the draft bounds2/3 and the stronger published general bound2 as different occurrences.'),
    (220, 'Finite geometric abelian coinvariants and the curve proof', 'unproved claim', [199,200,201,202,217,218,219,220,221,222,224,225,226],
     'For normal geometrically connected schemes of finite type over finitely generated fields, the geometric pro-ell abelian coinvariants are finite and vanish for almost all ell. The proof uses normal-open surjectivity, radicial invariance, a generic curve, the open-curve twist and finite-field Jacobians.',
     'Keep invariants versus coinvariants distinct, and retain the actual normality, field and finite-generation assumptions. Exposé-number similarity does not identify the final published redaction.'),
    (221, 'The constant-part adaptation for abelian schemes', 'self-flagged step', [203,204,205],
     'For an abelian scheme over a normal geometrically integral base over a separably closed field, the source deduces potential trivial geometric Tate action from virtually solvable image and asks for the radicial constant-part adaptation; full level structure removes finite twisting in characteristic zero.',
     'Geometric semisimplicity and level rigidity are checked; the exact Grothendieck1966 Proposition4.4 adaptation remains a source-collation gap, not a declaration of a new open theorem.'),
    (222, 'Potential isotriviality, CM and arithmetic image criteria', 'self-flagged step', [206,207,208,211,212,216],
     'The source relates potentially solvable Tate action to CM and potential good reduction, and proposes Frobenius-density and cross-prime arguments. Its attempt to replace an arbitrary finite cover by a constant-field extension is false.',
     'The explicit quadratic twist needs a function-field extension. The nilpotent-image Frobenius argument and the general solvable-image CM theorem remain distinct claims.'),
    (223, 'Geometric semisimplicity and the motivic extension', 'conjecture', [209,210,229],
     'Extend the geometric solvable-monodromy conclusions from abelian schemes to higher cohomology and motives; distinguish the geometric semisimplicity theorem for smooth proper families from arithmetic semisimplicity.',
     'The smooth-proper geometric result is established. The broad motivic programme is not exhausted by that theorem or by later special arithmetic cases.'),
    (224, 'Potential good reduction and the coefficient-prime distinction', 'self-flagged step', [213,214,215],
     'For abelian varieties over henselian discretely valued fields, compare potential good reduction with inertia semisimplicity. The ell≠p criterion is established; the written extension to ell=p has a false converse, witnessed by an ordinary good-reduction Serre–Tate lift.',
     'Keep rational p-adic inertia semisimplicity, finite inertia image and Barsotti–Tate good reduction separate. The q=1+5 lift over W(F5bar) supplies the checked counterexample; the sufficiency direction is separately recorded.'),
    (225, 'The cancelled nonabelian solvable-coinvariant proposal', 'withdrawn in the same text', [230],
     'The cancelled remark proposes an open-commutator analogue for a solvable pro-ell geometric quotient stable under the arithmetic group.',
     'The action used in the commutator and the ambient group of openness are ambiguous. Do not turn the withdrawn sentence into a precise surviving conjecture.'),
]
assert set(n for g in groups for n in g[3]) == set(range(168,231))
assert sum(len(g[3]) for g in groups) == 63
new_ids = {f'SA13-{g[0]}' for g in groups}
# New IDs were checked against every current source shard before allocation.
for directory in OUT.parent.iterdir():
    f = directory / 'items.json'
    if directory != OUT and f.exists():
        assert not new_ids.intersection(x['id'] for x in json.loads(f.read_text()))
items = [x for x in items if x['id'] not in new_ids]
for number, title, kind, numbers, statement, reconstruction in groups:
    selected = [cm[n] for n in numbers]
    locations = list({json.dumps(loc, sort_keys=True): loc for c in selected for loc in c['lines']}.values())
    locations.sort(key=lambda z: (z['file'], z['start'], z['end']))
    item_id = f'SA13-{number}'
    items.append({
        'id': item_id, 'title': title,
        'sources': sorted({z['file'].replace('_transcription.tex', '') for z in locations}),
        'kind': kind, 'cote': sorted({z['cote'] for z in locations}),
        'scans': list(dict.fromkeys(f"{z['cote']}:{z['scan']:03d}" for z in locations)),
        'lines': locations, 'his_words': selected[0]['his_statement'],
        'statement': statement, 'reconstruction': reconstruction, 'check': 'agrees',
        'check_reason': 'Codex-only source item added after full transcription/notes review. It creates no Pro NOTES_INDEX verdict. Distinct mathematical hypotheses, revisions and fates remain in the linked atomic claims.',
        'claims': [c['id'] for c in selected],
    })
    for c in selected:
        c['items'] = list(dict.fromkeys(c['items'] + [item_id]))
# Unindexed EVT subsidiary claims attach to the exact existing source object.
# Where no dedicated mathematical item exists, SA207 is explicitly provenance
# only; this is not a forced theorem merge with a nearby editorial request.
evt_links = {231:[174],232:[207],233:[207],234:[207],235:[207],236:[207],
             237:[180],238:[182,193],239:[182],240:[207],241:[203]}
for number, targets in evt_links.items():
    cm[number]['items'] = [f'SA13-{target}' for target in targets]
    if 207 in targets:
        cm[number]['item_relation'] = {'SA13-207': 'Exact reused EVT folio/source-family provenance; the subsidiary mathematical assertion is distinct from the inventory item and is not merged with another theorem.'}
(OUT / 'items.json').write_text(json.dumps(items, ensure_ascii=False, indent=2) + '\n')
(OUT / 'claims.json').write_text(json.dumps(claims, ensure_ascii=False, indent=2) + '\n')

problems = json.loads((OUT / 'problems.json').read_text())
p51 = next(p for p in problems if p['id'] == 'MP-SA13-51')
p51.update(
    as_he_states='Verify the delegated local-algebra lemmas and the quadratic-transform chain assertions, retaining the distinct source-identification obligations.',
    plausible_today=completion_statement + ' The quadratic-sequence claim still needs its own valuation and absent-lemma hypotheses.',
    why_open='The common-completion mathematical statement is now recovered and independently proved. What remains unresolved is the exact printed source and the separate C158 dependencies[A6]/[A7] and Lemmas9–10; no universal termination claim follows.',
    worth='High source-identification value: recover the original reference and quadratic-sequence dependencies; the common-completion proof itself need not be redone.',
)
for row in p51['state_of_art']:
    if row['claim_id'] == 'C-SA13-157':
        row.update(result=completion_fate + ' ' + completion_proof,
                   locators=['Supplied printed continuation33:173→137→135; cross_package_merge_audit.md', 'Stacks00MC:Lemma10.97.3'],
                   canonical_claim_id='C-SA13-064')
for loc in continuations:
    occurrence = dict(loc, claim_id='C-SA13-157')
    if occurrence not in p51['occurrences']:
        p51['occurrences'].append(occurrence)
if 'Stacks00MC' not in p51['refs']:
    p51['refs'].append('Stacks00MC')
(OUT / 'problems.json').write_text(json.dumps(problems, ensure_ascii=False, indent=2) + '\n')

reference = '''@misc{Stacks00MC,
  title = {The Stacks Project, tag 00MC},
  url = {https://stacks.math.columbia.edu/tag/00MC},
  year = {2026},
  author = {The Stacks Project Authors},
  note = {verified},
  annote = {Opened exact primary project statement and its relevant hypotheses: Lemma10.97.3 faithful flatness of completion. Access year; no first-publication priority claim.},
  urldate = {2026-11-19},
}
'''
bib = OUT / 'references.bib'
if '@misc{Stacks00MC,' not in bib.read_text():
    with bib.open('a') as handle:
        handle.write('\n' + reference)
search_path = OUT / 'search_log.tsv'
with search_path.open() as handle:
    reader = csv.DictReader(handle, delimiter='\t'); search_fields = reader.fieldnames; searches = list(reader)
for row in searches:
    if row['search_id'] == 'P2-S05' and 'https://stacks.math.columbia.edu/tag/00MC' not in row['opened_sources']:
        row['queries_or_openings'] += '; direct opening of Stacks00MC for the recovered common-completion proof'
        row['opened_sources'] += ' | https://stacks.math.columbia.edu/tag/00MC'
        row['exact_locators'] += '; Lemma10.97.3, noetherian local completion faithfully flat'
        row['outcome'] += '; Final cross-package continuation recovers full Lemma2 hypotheses and proof; exact printed source remains unidentified. Primary faithful-flatness statement opened2026-11-19.'
with search_path.open('w') as handle:
    writer = csv.DictWriter(handle, fieldnames=search_fields, delimiter='\t'); writer.writeheader(); writer.writerows(searches)

events_path = OUT / 'check_events.tsv'
with events_path.open() as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    events = list(reader)
who = 'GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p2'
additions = [
    ('C-SA13-198', 'Final scope audit: a generic-parameter function-field extension need not be finite; source §5.3/5.4 and C227 require a suitable valuation/inertia comparison. Statement corrected without changing the manuscript.'),
    ('C-SA13-203', 'Final publication-scope audit: exact1966 Proposition4.4 was not collated. ClassC/medium confidence preserves the verified geometric-semisimplicity ingredient and the precise radicial constant-part identification gap; no new mathematical openness is asserted.'),
    ('C-SA13-204', 'Final publication-scope audit: unipotent geometric monodromy is killed by the verified semisimplicity result, but the constant/radicial descent requires the separately uncollated Proposition4.4 adaptation. ClassC is explicitly limited to this source gap.'),
    ('MP-SA13-51', 'Final cross-package update: exact printed continuation173→137→135 supplies the same-dimensional two-ring hypotheses. The common-completion lemma is recovered and independently proved; source identity and the separate quadratic-sequence dependencies remain unresolved.'),
    ('Stacks00MC', 'Direct primary opening2026-11-19: Lemma10.97.3 gives faithful flatness of the completion of a noetherian local ring. Only this standard input is attributed to the source; the two-ring associated-graded argument is independently reconstructed.'),
]
for ident, outcome in additions:
    if not any(e['statement_id'] == ident and e['outcome'] == outcome for e in events):
        events.append(dict(statement_id=ident, date='2026-11-19', who=who,
                           type='used and rechecked in this run', outcome=outcome))
completion_event = 'Recovered full Lemma2 across173→137→135: equal-dimensional regular associated graded rings give all finite quotient isomorphisms, hence common completion; faithful flatness gives ideal contraction and generator descent, and the principal-ideal case gives the fraction-field intersection. This proves the recovered statement without identifying the original printed source.'
if not any(e['statement_id'] == 'C-SA13-157' and e['outcome'] == completion_event for e in events):
    events.append(dict(statement_id='C-SA13-157', date='2026-11-19', who=who,
                       type='independent re-proof', outcome=completion_event))
for number, title, kind, numbers, statement, reconstruction in groups:
    ident = f'SA13-{number}'
    outcome = ('Codex-only source-summary comparison: the cited passages were read in full during the '
               'K34-01–04 review and reread for relevant final scope corrections. This item groups the '
               'listed source object while retaining each atomic claim and its hypotheses, page status '
               'and fate. This is a source/background check, not an independent proof event. Claims: ' +
               ', '.join(f'C-SA13-{n}' for n in numbers) + '.')
    if not any(e['statement_id'] == ident and e['outcome'] == outcome for e in events):
        events.append(dict(statement_id=ident, date='2026-11-19', who=who,
                           type='carried as background without fault found', outcome=outcome))
with events_path.open('w') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t')
    writer.writeheader(); writer.writerows(events)

result = {'new_codex_items': sorted(new_ids, key=lambda x: int(x.split('-')[-1])),
          'items': len(items), 'claims': len(claims), 'codex_claims_linked': 63,
          'empty_claim_items': [c['id'] for c in claims if not c['items']],
          'verdict_rows_added_or_changed': 0,
          'corrected_fields': {'C-SA13-157 / MP-SA13-51': 'Recovered common-completion statement and proof, source identification separately open',
                               'C-SA13-198': 'field-extension scope',
                               'C-SA13-203': 'classC; exact-proposition gap',
                               'C-SA13-204': 'classC; exact-proposition gap'}}
(OUT / 'outputs/final_quality_patches.json').write_text(json.dumps(result, indent=2) + '\n')
with (OUT / 'progress.log').open('a') as handle:
    handle.write(datetime.now(timezone.utc).isoformat() + ' Final quality patches: C198 generic-parameter extension; C203/C204 exact-proposition gap; thirteen Codex-only items213–225 link all63 supplementary claims without new Pro verdicts.\n')
print(json.dumps(result, indent=2))
