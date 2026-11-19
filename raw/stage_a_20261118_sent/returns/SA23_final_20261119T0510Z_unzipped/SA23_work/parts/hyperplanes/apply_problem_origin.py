"""Apply individually read, manually decided question-provenance corrections.

The saved audit contains literal witnesses; no keyword inference assigns decisions.
"""
import copy, json
from pathlib import Path

P = Path(__file__).parent
AUDIT = P.parents[1] / 'integration/hyperplanes_problem_origin_audit.json'

# Independently authored changes to the surrounding explanatory fields.  These
# prevent a narrower question field leaving an invented request in the title.
NARROW = {
 7: ('The marginal avoidance variant of multisections',
     'The marginal extension is brief and not separately established there; even the word fini is uncertain in the supplied transcription.',
     'A bounded avoidance comparison is useful after preserving the uncertain size condition; the later projection exercise is separate.', [16,17]),
 10: ('The conormal comparison and its scheme-level formulation',
      'The mechanical comparison is identified as an exercise; the later passage expressly asks for the scheme-level refinement of the ramification identity.',
      'Useful for a precise diagram and ideal comparison, with the narrower sign questions separately indexed under MP-SA23-hyp-54.', [21,81]),
 12: ('A collected and strengthened general-pencil statement',
      'The request concerns a more precise collected statement and convenient placement after the blow-up description; the source has already supplied the constituent arguments.',
      'The published pencil theorem resolves the mathematics; an exact statement concordance is worthwhile.', [23,32,33]),
 14: ('A replacement for the rejected word réglée',
      'The smooth quadric shows the proposed terminology conflicts with customary usage, and the author explicitly requests a better word.',
      'Preserve the terminology correction; no new mathematical theorem is required.', [23]),
 19: ('The ordinary-singularity argument after the separability withdrawal',
      'After rejecting the universal separability clause, the author says the remaining assertion seems correct and proposes the ordinary-quadratic-point construction as its proof.',
      'Compare the proposed construction with the exact published Veronese-pencil theorem; do not reopen the false universal separability assertion.', [29,78]),
 21: ('An unfinished collected theorem and tentative fundamental-group clause',
      'The collected theorem stops before a precise fundamental-group conclusion; its pi1 reading is itself uncertain.',
      'Only source concordance is ready; a stronger theorem would be an invention without further evidence.', [31]),
 29: ('Writing the general independent-hyperplane induction once',
      'The fixed-point lemma is proved later in the passage. The explicit outstanding request is to write its recurring generic-hyperplane induction in a reusable general form.',
      'A short exposition task is useful; the field-case theorem itself is established in the opened sources.', [43]),
 35: ('Fiber dimension and flatness of a generic conical projection',
      'The source explicitly asks the dimension and flatness question before stating its proposed answer, and separately requests the Cohen–Macaulay module variant.',
      'Useful for correcting the answered question’s quantifiers: generic fiber dimension does not control every fiber.', [48,50]),
 44: ('Rewriting the extension criterion and extracting its corollary',
      'The proof is completed, then the author explicitly asks for a single necessary-and-sufficient formulation and a preceding corollary.',
      'This is a precise exposition task; retain the depth and finite-presentation hypotheses already checked.', [65,66,67]),
 47: ('The deferred functorial infinitesimal criterion',
      'The general monomorphism criterion and tangent-deviation formalism are deferred to later sections; the source explains why their use is not circular.',
      'A bounded dependency concordance is useful, while a general arbitrary-functor theorem needs separately stated hypotheses.', [72]),
 48: ('The promised descent of twisted linear-system parameters',
      'The source defers faithfully flat descent and explicitly announces twisted projective parameters for the next treatment.',
      'Established descent theory supplies the framework; compare the actual promised scope without inventing an ordinary-projective-bundle conclusion.', [73]),
 49: ('The optional proof exercise for Proposition 4.4a',
      'The author expressly withholds the easy exercise proof unless the collaborator requests it.',
      'Useful as a short established-result annotation, not a claim that the theorem remains open.', [74]),
 50: ('The geometric formulation of the 4.4b/c exercise',
      'The author asks for the condition on the section space after algebraic closure and records its geometric-integrality simplification.',
      'A precise scalar-extension formulation is worthwhile; the statement that examples are easy is not an additional request to construct them.', [74,75]),
 53: ('Elementary terminology and the proposed ultra-singular subscheme',
      'The author requests the collaborator’s opinion about terminology and arbitrary multiplicity, and proposes the corrected-discriminant subscheme at least in a remark.',
      'Useful for tracing the corrected singularity notions and the exact proposed scheme construction.', [78,79]),
 55: ('The deleted multiplication-lemma exercise and degree-n variant',
      'The explicit delegation is deleted and followed by a field-reduction proof; the later higher-degree formulation is still an express instruction.',
      'Retain this historically answered exercise and the degree extension; the binomial-index repair is this run’s verification.', [85,86,87]),
 56: ('Choosing augmented-algebra generality and terminology',
      'The author leaves the choice of beginning with several generators to the collaborator and asks whether regular or quasi-regular is the correct term.',
      'This is a bounded terminology and organization task; the asserted presentation criterion stays in the claim map.', [85,94]),
 57: ('The explicitly unverified higher-corank ramification identity',
      'The source says it has not checked the identity in detail and asks for an equality of closed subschemes; the adjacent dimension bound is asserted separately.',
      'Worth isolating the scheme-equality calculation; correcting the separate false height bound is an editorial check.', [89]),
 60: ('The promised blow-up proof of an isolated elementary singularity',
      'A later section is explicitly promised for the isolation proof; Cohen–Macaulayness has already been deduced, and normality/reducedness are stated consequences.',
      'A short standard blow-up proof and exact dimension convention complete the useful annotation.', [84,94]),
 65: ('The proposed general homogeneous-space lemma',
      'The uncertain margin asks for a lemma to be extracted from the supplied orbit-flatness proof, not for a new proof of the entire torsor equivalence.',
      'A short extraction of the generic-flatness/transitivity lemma is useful, conditional on the marginal reading.', [102]),
}

PLAUSIBLE = {
 14:'Use dual-defective for the appropriate duality condition; the source has already rejected its own use of réglée.',
 19:'For a smooth projective variety with an immersion, retain the ordinary-quadratic-singularity conclusion for degree-at-least-two Veronese pencils with the exact SGA7 hypotheses; do not restore universal separable duality in odd dimension and characteristic two.',
 21:'No unique fundamental-group theorem is recoverable from the unfinished, uncertain clause. The surrounding smooth, proper, geometrically integral and unramified assumptions are context, not an unstated conclusion.',
 29:'State the iterated generic-hyperplane argument with independent parameters and retain the dimension, smoothness and boundary-transversality conditions at each induction step; this repackages the supplied argument.',
 44:'Under the source’s finite-presentation, flatness and fiber-depth hypotheses, express invertible extension by the condition that j_*L be invertible, and state the relative Cartier-divisor corollary separately.',
 47:'Use a precisely stated finite-presentation infinitesimal criterion for the relevant functors, with the normal-bundle tangent space for Cartier divisors. Pointwise geometric-fiber injectivity alone is insufficient for arbitrary functors.',
 48:'Use effective faithfully flat descent for the divisor family and a Brauer–Severi parameter space with its descended polarization data. An ordinary projective bundle requires the corresponding twisting obstruction to vanish.',
 53:'Distinguish smooth projective tangent forms from nonsingular polar forms, especially in characteristic two. A proposed ultra-singular closed subscheme must use the corrected discriminant and its line-bundle convention, not only a set-theoretic terminology change.',
 56:'State the regular-immersion/associated-graded hypotheses and distinguish regular from quasi-regular conventions; no mathematical existence question follows merely from choosing the order of exposition.',
 57:'On the stated split rank stratum, compare the explicit second-order degeneracy ideal with the Fitting ideal defining ramification of V¹→Y. The adjacent false arbitrary-matrix codimension lower bound is excluded from this requested identity.',
 60:'For the noetherian elementary local hypersurface with smooth projectivized tangent cone, prove isolation by the promised blow-up argument and retain intrinsic dimension at least two for normality and at least one for reducedness.',
 65:'For an equivariant morphism of finite-type schemes over an algebraically closed field, a reduced target with a transitive algebraic-group action allows the generic flat locus to be translated across the target; retain finite-presentation and surjectivity hypotheses for faithful flatness. This is the precise general form suggested by the supplied proof, conditional on reading the margin that way.',
}

def apply(records):
    audit = json.loads(AUDIT.read_text())
    decisions = {a['original_id']:a for a in audit['decisions']}
    assert len(decisions) == 68
    kept, editorial = [], []
    for original in records:
        q = copy.deepcopy(original)
        a = decisions.get(q['id'])
        if a is None:
            assert q['id'] in ['MP-SA23-hyp-69','MP-SA23-hyp-70']
            q['source_question_found'] = True
            q['provenance_audit'] = 'Individually recovered and source-read after the 68-record audit; see data_late_audit.py and the cited exact passage.'
            kept.append(q)
            continue
        q['pre_origin_audit_record'] = copy.deepcopy(original)
        q['problem_origin'] = a['origin']
        q['source_question_found'] = a['source_question_found']
        q['source_question_confidence'] = a['confidence']
        q['source_cues'] = a['source_cues']
        q['provenance_audit_reason'] = a['reason']
        q['provenance_audit_path'] = 'integration/hyperplanes_problem_origin_audit.json'
        if 'recommended_as_he_states' in a:
            q['as_he_states'] = a['recommended_as_he_states']
        for cue in a['source_cues']:
            lo,hi = cue['physical_lines']
            q['occurrences'].append(dict(source=cue['source'],cote=cue['cote'],scans=cue['scans'],lines=[f'{cue["source"]}:{lo}–{hi}'],role='literal authorial cue or assertion used in provenance audit'))
        if a['decision'] == 'reclassify_to_editorial_task':
            q['original_id'] = q['id']
            q['id'] = a['proposed_id']
            q['title'] = 'Editorial verification: '+q['title']
            q['task'] = q['as_he_states']
            q['editorial_formulation'] = q['as_he_states']
            q['as_he_states'] = 'Source basis, not an authorial question: '+a['reason']
            q['why_open'] = 'No corresponding authorial question is established. '+a['reason']
            q['reclassification_reason'] = a['reason']
            editorial.append(q)
        else:
            n = int(q['id'].rsplit('-',1)[1])
            if n in NARROW:
                title,why,worth,nums=NARROW[n]
                q.update(title=title,why_open=why,worth=worth)
                q['claims']=[f'C-SA23-hyp-{i:03}' for i in nums]
                q['context_claims']=[i for i in original.get('claims',[]) if i not in q['claims']]
                q['state_of_art']='For the narrowed source question, with the following claim comparisons also documenting its asserted context: '+q['state_of_art']
                if n in PLAUSIBLE:q['plausible_today']=PLAUSIBLE[n]
            if n in [10,54]:
                q['overlap_scope']='The scheme-level identity clause of MP-SA23-hyp-10 overlaps the conormal/sign exercise in MP-SA23-hyp-54; the former also has a distinct early incidence comparison. These are cross-referenced components, not two independent discoveries.'
            if n in [55,59]:
                q['overlap_scope']='The degree-n Hilbert clause is shared by MP-SA23-hyp-55 and MP-SA23-hyp-59; the latter additionally proposes the presentation criterion and geometric definitions.'
            if n == 68:
                q['problem_kind']='authorial editorial and authorship questions, not a mathematical research problem'
                q['count_as_authorial_mathematical_problem']=False
            kept.append(q)
    assert len(kept)==49 and len(editorial)==21
    (P/'editorial_tasks.json').write_text(json.dumps(editorial,ensure_ascii=False,indent=2)+'\n')
    (P/'problem_origin_audit.json').write_text(json.dumps(dict(audit_source=str(AUDIT),applied=True,authorial_records=49,authorial_editorial_records=1,editorial_tasks=21,decisions=audit['decisions']),ensure_ascii=False,indent=2)+'\n')
    return kept, editorial
