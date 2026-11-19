"""Apply the approved, manually assessed 81-record problem-origin audit.

Run last, after both parts' source/literature serializers. This overlay is
idempotent: original records are preserved in provenance/pre_origin_audit and
in source_records. No verdict or mathematical judgment is inferred by code.
"""
from pathlib import Path
import collections, copy, csv, json, re, sys

HERE=Path(__file__).resolve().parent
PARTS=HERE.parent
WORK=PARTS.parent
AUDIT=json.loads((WORK/'integration/ega_problem_origin_review.json').read_text())
DATE='2026-11-19'

# For retained mathematical questions: manually rewritten documentary reason
# and one-sentence assessment of the value of further work.
WHY_WORTH={
'ega':{
2:("The question marks remain attached to two applications; the surviving annotations do not resolve their precise scope or identify the annotating hand independently of the offprint.","Worth a bounded hypothesis and scan comparison of these two applications; the separate Cartier reconstruction check is editorial context."),
4:("The source explicitly doubts the lemma without injectivity and inserts a containing base ring in the correction; no later reason for omission is documented.","Worth preserving the exact missing-injectivity diagnosis and comparing the corrected formulation with the printed statement."),
5:("The source expressly says that general infinitesimal Cohen-lift existence is not known there, while proving existence under a separable-residue restriction; no reason for a later abandonment is documented.","Worth a carefully delimited comparison of the source's general topological existence problem with the established complete-local factorization theorem."),
6:("The source labels the matter an open question, considers characteristic-dependent answers, and records pessimistic or negative marginal reactions.","Worth preserving the now-checked adic/discrete distinction; a new task should address an exact residual formulation rather than repeat the counterexamples."),
7:("The draft asks openness and localization stability, then sketches reductions using good rings and resolution without supplying a general final theorem.","Worth comparing the intended good-ring hypotheses with the precise modern openness conditions."),
8:("The page marks the general flat-locus question unknown and proposes a generic-flatness reduction; it gives no documentary explanation of later omission.","The unrestricted assertion is false, so further value lies in the counterexample and exact missing finiteness assumptions."),
9:("The coefficient-choice step is explicitly introduced as remaining to prove and ends in an unfinished selection and ellipsis.","The finite-support completion is now supplied; further work should concern a precise stronger statement or historical identification."),
17:("The source expressly seeks a characterization, but its category, order and locality conventions remain exploratory.","Worth first fixing one category and order condition before attempting a scheme-theoretic classification theorem."),
18:("The author explicitly leaves algebraic closure of k in A unverified for example(i), whose surviving formulas do not determine a unique repair.","Worth checking the original ink before completing the constant-field argument; the verified second example is a separate editorial check."),
19:("The only authorial query is cancelled and partly unreadable; the supplied transcription does not determine its exact df/delta-f formula.","Worth recovering the formula from the scan, but no new conjecture should be manufactured from the uncertain reading."),
20:("Lê explicitly says that associated primes and depth are outside his knowledge and that he does not know whether the definitional errata obstruct the demonstrations.","Worth a proof-by-proof erratum concordance addressing Lê's stated uncertainty, with the corrected meromorphic definitions fixed first."),
22:("The source expressly hopes to remove local noetherianity and replace finite by integral; the stronger statement is not proved on the surviving leaf.","Worth fixing the exact epimorphism and unramified-section quantifiers before applying modern integral étale descent."),
23:("The draft questions whether the old nonnoetherian definition is reasonable and calls for a §16 revision, recording a correction process rather than a finished definition.","Worth retaining the source-to-SGA6 comparison; the cited Koszul formulation settles the identified definition issue."),
24:("The finite-presentation kernel question is explicit, and separation objections carry marginal doubts; the surviving letters record changes of position rather than a reason for abandonment.","Worth preserving the exact counterexamples and the distinction between A-submodules and B-submodules."),
25:("The Koszul-resolution condition bears an explicit(?) in the equivalence list; the following argument addresses it, so this is a source doubt with a supplied resolution, not a still-open theorem.","Worth a short concordance of the questioned condition and its proof, keeping it separate from the already-published removal of separation."),
29:("Deligne explicitly says he cannot give the simpler N=A, M=B pro-Tor vanishing proof, although his more elaborate comparison argument precedes it.","Worth presenting the completed pro-zero argument with transition indices; inverse-limit vanishing alone does not answer the requested step."),
31:("A marginal question mark follows the proposed weakening of EGA0.19.4.6; the hand is not independently identified and the source gives no resolution of that particular doubt.","Worth one exact proof audit of the proposed formal-projectivity weakening, rather than treating the confirmed unrelated errata as its proof."),
36:("The source adds avec réserve and tentatively requires submersiveness stable under étale base change for the extension beyond separated objects.","Worth a precise nonseparated étale test after fixing the comparison functor and the intended topology."),
39:("The S_k transfer arrow is explicitly marked with a question and immediately followed by a change-of-ring depth warning; the exact module notation remains incomplete.","Worth recovering the module operation and hypotheses before asserting a general preservation theorem."),
42:("The source explicitly says that independence from the chosen sections should be verified; the necessary preceding compatibility is separately a reader diagnosis.","The triangular proof now answers the stated check under explicit augmented compatibility, and is worth including in the commentary."),
44:("Question introduces the three implications; their differing outcomes are established in this run rather than documented as a historical reason for omission.","The finite counterexample and two corrected tensor-product implications complete the bounded mathematical task."),
45:("The excellent-functor/morphism margin and detached-pieces relation sketch remain question-marked programme fragments without a definite theorem formulation.","Worth preserving as historical mathematical programme fragments; a new theorem requires a separately justified formulation."),
46:("The margin asks about a common treatment and Cas Greenberg? but does not supply the exact seminar-edition target or all hypotheses.","Worth an exact SGAD/Greenberg concordance before claiming that a general restriction-of-scalars theorem settles the intended case."),
47:("The plan explicitly lists missing Picard topics and marks the pencil study with(?), allocating work to later chapters without documenting a mathematical obstruction.","Worth a focused comparison of the proposed pencil approach with the intended Picard chapter, not an unrestricted new Picard conjecture."),
48:("The item belongs to Problèmes-types à résoudre, but the structures and base category are not specified.","Worth pursuing only after identifying the corresponding structures and descent problem."),
49:("The explicit problem list records only partial results for the nonprojective Hilbert/Picard case.","Worth comparing the intended category of representing objects with the exact later algebraic-space theorems."),
50:("The problem is annotated OK par Raynaud; the leaf does not supply the proof date or a precise citation.","Worth checking the original attribution and date while keeping the existence question marked resolved in the identified scope."),
51:("The problem-list phrase supplies neither a quotient category nor hypotheses replacing flatness.","Worth selecting one precise equivalence relation and quotient functor before further work."),
52:("The listed problem uses sans point fixe without defining it and associates the issue with Mumford.","Worth a terminology comparison with the intended Mumford source before replacing that phrase by scheme-theoretic freeness."),
53:("The explicit programme asks for very general moduli without boundedness, rigidity or a specified moduli functor.","Worth mapping to separate precisely formulated moduli problems; its present wording is too broad for one proof task."),
54:("The listed classification problem distinguishes affine commutative and noncommutative structural groups but leaves broad relative-base and representability choices open.","Worth choosing one fixed relative curve and structural group before comparing the exact established moduli-stack theorem."),
55:("The finite-group special case is explicit; the marginal rédiger/vérifier/vérifié ambiguity prevents deciding its recorded progress from this transcription.","Worth resolving that ink and the group-scheme hypotheses before deciding whether any mathematical step remained."),
56:("The source explicitly marks the relative P1/GL_n problem possibly ill posed.","Worth using a family with changing splitting type to clarify the intended classification functor."),
57:("The formal-moduli question is literal and carries a circled affirmative answer, without a proof on this leaf.","Worth an exact comparison with the formally smooth unpolarized abelian-deformation theorem, not treating the answer as still unknown."),
58:("The nonprojective theorem-of-the-square item is part of the explicit problem list; no reason for its later omission is supplied.","Worth matching the exact nonprojective hypotheses to a numbered proof before asserting a complete historical identification."),
59:("The mathematical programme is crossed out and contains a theta-divisor question; the cancellation does not document why it was dropped or whether it was solved.","Worth preserving the cancelled programme and its existing overlaps, without turning its notation choices into mathematical problems."),
},
'analysis_curves':{
2:("The author explicitly postpones spelling out the duals of2.6 and2.7; the existence caveats are hypotheses, not a separate general existence conjecture.","Worth writing the exact dual statements with their product and finite-presentation assumptions."),
4:("The margins expressly request the surjectivity-only case and more general localization procedures; no later reason for dropping either request is documented.","Worth fixing one general localization procedure and distinguishing local lifting from surjectivity on every open."),
6:("The margin reads preuve/prouver for the absolute-value distribution comparison; the ambiguity concerns the wording of the request, not the displayed comparison.","Worth supplying the short normalized minimax proof under explicit trace and one-sided-cutoff conventions."),
8:("The finite-rank identity carries the inserted instruction vérifier d'après cas décomposable, while its extension by continuity is asserted.","The rank-one multilinear computation answers the requested check and is worth retaining with its1/n! normalization."),
9:("The page explicitly leaves the sense of continuity à préciser; later source arguments do not retroactively define that phrase on the earlier leaf.","Worth a statement-and-proof concordance distinguishing finite Riesz clusters from a whole-list topology with tail control."),
10:("The theorem is announced, but its reduction to the positive case is expressly deferred in future tense on this leaf; later analytic arguments give the fate of that proof programme.","Worth explaining the analytic genus-zero mechanism and why an unsupported positive-case reduction alone does not establish the nonnormal trace formula."),
11:("The strongest-possible language is explicitly tentative and does not specify an exact completeness or extremality problem.","Worth one formulation comparison with complete Horn-type feasibility, without turning the tentative phrase into an invented sharp theorem."),
12:("The page explicitly asks to find the general scalar functions and then an n-argument version; no documentary reason for later abandonment is known.","Worth a scoped multivariable formulation task, since the normalized one-variable trace-subadditivity problem is already settled."),
13:("An actual marginal? accompanies formula(39) after symmetry is deleted; the source does not explain the later history of that doubt.","The exact2x2 counterexample resolves the unsymmetric variant, so further value is in ink collation and a corrected statement."),
14:("A marginal? follows the total-and-strongly-closed step in the reflexivity equivalence; the surrounding duality statements have arguments.","Worth a concise finite-truncation and polar-duality explanation of that exact step."),
18:("The source explicitly asks for the Schatten-norm generalization and finite-dimensional reduction, and questions the r>=1 trace extension; later leaves contain the broader proof programme.","Worth a proof-dependency comparison under exact trace assumptions; the established Hölder theorem itself is not left open."),
19:("The source asks both the finite-p convergence extension and uniform convexity, which are mathematically distinct; it supplies no historical reason for omission.","Worth explaining the all-p Kadec–Klee result separately from uniform convexity for1<p<infinity."),
20:("The source expressly asks monotonicity in the power parameter and precise inequalities; the false unrestricted range is diagnosed by the present-run certificate, not withdrawn in the manuscript.","Worth stating the exact surviving parameter range and investigating a sharply formulated residual boundary using the saved rational counterexample."),
21:("The margin explicitly requests individual eigenvalue majorants with an uncertain fractional index or an analogue; no later disposition is recorded there.","The finite cyclic and compact-block examples answer the unrestricted request and make a useful explanatory companion."),
}}

# Narrowed modern formulations/fates. Broader former discussions remain in the
# preserved source record and, where useful, a separately named editorial task.
SCOPE_FATES={
('ega',2):('Keep the source formal-series and Hopf applications with their stated characteristic and finiteness assumptions; an unrestricted group/Hopf formulation is not supported.','Stacks0BF6 supplies the finite-type characteristic-zero group theorem. It does not independently identify the exact formal-series margin. The Cartier connectedness counterexample is recorded separately as an editorial check.'),
('ega',4):('Use the corrected finite inclusion of domains and the actual separability/formal-fibre hypotheses.','The completed finite-module inclusion argument supports the corrected formulation. A finite quotient is not interchangeable with a finite inclusion; the margin alone does not refute the separate localization-stability statement.'),
('ega',18):('Check algebraic closure of k in the ring of source example(i), once its incompatible surviving formulas have been read on the scan.','No unique formula for example(i) is imposed. The exact later match Stacks038S concerns the separately verified example(ii), not a proof of this unresolved reading-dependent step.'),
('ega',19):('No stronger formula is asserted: the cancelled df/delta-f question is not uniquely legible.','The surrounding equalizer and formal-diagonal assertions have the saved counterexamples and standard repairs, but these do not identify the cancelled question itself. Its remaining issue is textual identification, not a proven open modern conjecture.'),
('ega',20):('Test each affected proof after replacing the meromorphic-function definitions by a restriction-stable nonzerodivisor sheaf; locally noetherian stalk identifications require their explicit hypotheses.','Original EGAIV20.1.3–4,20.1.8 and21.2.9 were compared with Lê’s correction. Stacks01X1 supplies the restriction-stable definition and0EMG the locally noetherian identifications. These resolve the checked definitions and local identifications, not an unperformed audit of every downstream proof mentioned in the letter.'),
('ega',22):('Precisely specify integral scheme epimorphism, the unramified section category and the allowed surjective test before stating the hoped-for extension.','Rydh’s subtrusive effective descent of étale morphisms and SGA4VIII9.4 are verified neighboring results. They do not by themselves establish all the source quantifiers for unramified sections.'),
('ega',25):('For a proper ideal of a noetherian local ring with a minimal finite generating sequence, positive Koszul acyclicity is equivalent to regularity in the stated local criterion.','The source itself follows the questioned condition by a local/Koszul argument. The standard regular-sequence/Koszul framework is checked in SGA6VII and the cited EGA material; the independent removal-of-separation theorem is retained separately as ED25-context.'),
('ega',29):('In the exact noetherian relative finite-module setup of the letter, prove pro-vanishing of positive Tor for the indicated powers of an ideal, with the transition maps explicit.','Stacks0911 provides the Artin–Rees pro-Tor mechanism and Stacks09Q9 the flat noetherian factorization ingredient. The relative argument is reconstructed in proof_notes.md; this is not an assertion that the whole letter formulation is literally Stacks0911.'),
('ega',31):('Audit the proposed replacement or removal of formal-projectivity assumptions in EGA0.19.4.6 using the specified extension-class/Hochschild argument.','The original EGA passage is located, but this exact weakening is not independently certified by the confirmed locality, sign or completion errata. Those other corrections are preserved as ED31-context; they do not settle the question mark at19.4.6.'),
('ega',36):('For arbitrary possibly nonseparated étale objects, retain the precise topological hypotheses on the base-change-stable submersive comparison.','Rydh supplies effective descent under a verified universally subtrusive hypothesis. This is a bounded comparison, not a proof that every candidate submersiveness formulation on the page is sufficient.'),
('ega',39):('Recover the precise restriction/change-of-ring operation on M before proposing an S_k preservation implication.','The adjacent source warning distinguishes depth over B from depth over A. The opened normality/S2 sources and cusp example check the surrounding normalization argument but do not establish a uniquely formulated version of the question-marked module transfer.'),
('ega',42):('For nonnegative grading with compatible augmentation and the stated vanishing of the augmented composition on A_+, prove that(b-double-prime) is independent of the chosen sections.','The triangular degree-induction proof is supplied in proof_notes.md. The missing compatibility counterexample belongs to the contextual editorial task and is not substituted for the explicitly asked section-independence step.'),
('ega',45):('No unique modern theorem is assigned to excellent functor/morphism or the detached-pieces equivalence-relation sketch.','The opened FGA/SGA material gives programme context only. Its existence does not define the ambiguous mathematical fragments; chapter order and terminology are preserved separately as editorial work.'),
('ega',46):('State the elementary representability functor and the exact Greenberg construction before asserting a common theorem.','Stacks05Y8 Proposition97.11.5 proves finite locally free restriction of scalars in its algebraic-space setting. The source’s SGAD edition/paragraph target and intended Greenberg comparison remain bounded identification issues.'),
('ega',59):('Retain the cancelled Hilbert/Picard construction programme, particularly the theta-divisor question, without treating cancellation as a mathematical negation.','The opened Hilbert/Picard literature identifies the families of results and overlaps with the live problem list, but does not explain why this particular programme was cancelled.'),
('analysis_curves',2):('For the exact contravariant setting, spell out the natural Hom comparison and the left-exactness criterion; the all-module extension needs the stated products.','SGA2IV1.1/1.3 and Stacks0F5S provide the exact finite/torsion representation framework. The requested dualization is reconstructed with its product assumptions rather than identified with an unrestricted representability theorem.'),
('analysis_curves',6):('Under the specified faithful normal semifinite trace framework and the normalized one-sided distribution conventions, establish the written comparison for |1+A| and1+|A|.','Grothendieck Bourbaki113§4 and Fack–Kosaki2.2/2.5 supply the minimax/distribution framework. The independent minimax argument settles the comparison in that scope; the original fragment’s ambient b and cutoffs remain readings to check.'),
('analysis_curves',8):('For decomposable finite-rank operators, compute the mixed exterior trace coefficient with the source’s averaged antisymmetrizer normalization, then extend by multilinearity and continuity.','Grothendieck1956I§§1–2 gives the matching construction. The saved rank-one1/n! coefficient and exact antisymmetrizer checks complete the explicitly requested finite-rank calculation.'),
('analysis_curves',9):('Use finite nonzero Riesz clusters together with an explicitly stated summable matching topology and uniform tails.','Grothendieck1955IIpp20–21,Remark4 was visually checked and supplies the identified p<=1 published assertion. Grothendieck1956pp361–364 gives the cluster mechanism; the broader all-p matching proof in this dossier is explicitly present reconstruction.'),
('analysis_curves',10):('Prove the Hilbert trace-class trace/eigenvalue formula through a valid analytic genus-zero argument, not by merely asserting a reduction to positive operators.','Reinov2012 gives the exact Hilbert trace formula and the1955/1959 historical comparison. The checked Hadamard/minimal-type route explains the missing nonnormal mechanism; the source’s announced positive-case reduction alone is incomplete.'),
('analysis_curves',11):('Choose a precise sharpness or completeness question before comparing these particular determinant bounds with complete singular-value feasibility.','Fulton2000Theorem15 supplies the complete Horn-index-set description in the finite complex setting. The source bounds are valid, but its tentative strongest-possible phrase does not uniquely assert that formulation.'),
('analysis_curves',13):('With equal total products, monotonicity may be dropped in the symmetric log-convex comparison; symmetry must be retained for the asserted universal inequality.','The exact2x2 counterexample refutes formula(39) without symmetry. The published symmetric log-majorization framework supports the repaired statement, and the question is thereby answered in its literal scope.'),
('analysis_curves',14):('For the minimal/maximal sequence spaces associated with a symmetric gauge and its polar, justify the reflexivity equivalence through the dual identifications and the closed, weakly dense coordinate subspace.','Antezana–Larotonda–Varela§§2,5.1 supports the modern framework. The finite-truncation/polar proof is supplied here and resolves the particular total/closed step; unrelated summary slips remain editorial checks.'),
('analysis_curves',18):('Keep the exact Schatten gauge assumptions, finite-dimensional approximation, and faithful normal semifinite trace hypotheses in the requested extensions.','Grothendieck113§5 and Fack–Kosaki4.2/4.9 establish the identified Hilbert and semifinite Hölder scopes. The independent analytic/dyadic proof records the reduction and endpoint conditions; the broader trace setting is not imported for an arbitrary C*-trace.'),
}

# Genuine partial editorial splits. Their IDs do not redirect the surviving MP;
# source_problem_id records origin. No duplicate task is created where an
# existing whole ED record or another MP already preserves the excluded context.
PARTIALS={
'ega':{
2:('Cartier reconstruction checklist', [34], 'Check the asserted Cartier/hyperalgebra reconstruction checklist and its connectedness condition.', 'The real function Hopf algebra on C3 refutes the weakened checklist; Cartier’s exhaustive connected filtration and the precise enveloping theorem are the relevant comparison.', 'Worth a concise hypothesis table explaining the saved counterexample.'),
18:('Verification of the second inseparable-curve example',[42],'Preserve the independent regularity, constant-field and geometric-singularity checks of example(ii), distinct from the author’s unfinished example(i).','Example(ii) is supplied as an assertion with argument; our exact local-ring calculation and Stacks038S match are verification, not an authorial question.','Worth placing the verified example beside the unresolved ink of example(i).'),
19:('Verification of the surrounding formal-diagonal assertions',[43],'Check the asserted flat equalizer and formal-diagonal statements surrounding the cancelled question.','Faithful flatness and connected infinitesimal hypotheses matter; the saved Z-to-Q and separable-extension examples refute the unrestricted assertions.','Worth preserving these minimal counterexamples without using them to guess the cancelled formula.'),
20:('Lê’s definition and local-trivialization errata concordance',[46],'Collate the exact meromorphic-denominator and local-trivialization corrections with the printed EGA passages.','The definitions and their comparisons are source assertions/corrections; the separate retained MP asks about the effect on proofs.','Worth a line-by-line source concordance with explicit noetherian hypotheses.'),
22:('Verification of the asserted finite unramified descent case',[48],'Verify the finite-case descent assertion before considering its explicitly hoped-for integral extension.','The finite case is an assertion on the leaf, not a question; the epimorphism and surjective-test quantifiers need reader verification.','Worth a proof-focused check of those exact quantifiers.'),
25:('Published removal of separation in EGAIV19.5.5',[52],'Collate Deligne’s asserted b-implies-c proof without separation with EGAIV19.5.5 and its attribution footnote.','The final1967 publication expressly credits Deligne and reproduces the proof; this is a completed historical identification, not the questioned Koszul condition.','Worth preserving the exact manuscript-to-publication concordance.'),
31:('Confirmed numbered EGA corrections and proof comparisons',[61],'Preserve the locality, differential-sign, integral-closure and completion-formula checks outside the narrow19.4.6 question.','These are distinct asserted corrections, including the repaired III4.3.6 proof and the printed old/new sign-label issue.','Worth a critical apparatus that keeps each correction and its exact source separate.'),
39:('Normalization and codimension-one verification',[74,75],'Check the asserted normalization/S2/codimension-one mechanism and the definition of the exceptional set.','The cusp counterexample and required codimension-one agreement concern surrounding assertions, not a precise answer to the incomplete S_k transfer query.','Worth preserving the quantifier correction alongside the known S2 mechanism.'),
42:('Missing augmented compatibility in the graded splitting',[78],'Verify the source’s asserted graded splitting and the necessity of the augmented-composition hypothesis.','The polynomial counterexample is a present-run check of the source assertion; the author’s explicit question is section independence.','Worth making the missing compatibility visible before presenting the independence proof.'),
45:('EGA V chapter order and covering terminology',[83],'Preserve the interversion, paragraph-placement and covering-terminology instructions as editorial planning tasks.','These choices are explicit in the plan but are not mathematical questions with a literature theorem as answer.','Worth retaining the plan’s cancellation and ordering history without assigning mathematical openness.'),
59:('Notation query adjacent to the cancelled programme',[83],'Preserve the question about suitability of the Hom notation separately from the cancelled Hilbert/Picard programme.','A notation choice is editorial; it does not create an additional mathematical problem.','Worth checking the intended notation and recording the original question mark.'),
},
'analysis_curves':{
2:('Existence conventions in the representation constructions',[4,5,7],'Verify finite presentations, coproduct/product preservation and exact-colimit assumptions in the surrounding representation constructions.','The source’s existence caveats state assumptions; the retained MP is the explicit request to spell out dual statements.','Worth an exact hypothesis table for the finite, all-module and torsion versions.'),
6:('Trace minimax cutoff and atomic conventions',[22,23,24],'Verify the unit-ball normalization, one-sided cutoff and atomic-trace cases of the asserted minimax formulas.','The supplied minimax proof and atomic conventions are separate from the marginal request for the absolute-value comparison.','Worth a convention table against Bourbaki113 and Fack–Kosaki.'),
8:('Exterior normalization and introductory notation',[31,32,35],'Preserve the antisymmetrizer normalization correction and the instruction to add a preamble as editorial checks.','The requested finite-rank identity is retained as a mathematical step; broad normalization/preamble work is not itself an open authorial theorem.','Worth retaining the exact n=2,3,4 certificates and the inclusion/quotient factor table.'),
11:('Index and exponent collation in the singular-value bounds',[38,39,40],'Collate the asserted sum inequalities and their indices independently of the tentative optimality comment.','Reader-discovered display repairs do not become questions merely because the later sentence conjectures optimality.','Worth preserving the literal displays and exact finite checks in the commentary.'),
13:('Other asserted convexity variants and reciprocal signs',[45,47],'Verify the asserted convexity variants outside the actual question-marked formula(39).','The exact2x2 counterexamples diagnose false assertions, not additional authorial questions.','Worth placing each counterexample beside its separate corrected symmetric statement.'),
14:('Polar signs, duality variance and ideal inclusions',[51,52,54,55,56],'Preserve checks of polar signs, source/target variance, inclusion directions and minimal/maximal completions outside the narrow reflexivity doubt.','The full arguments and short summaries differ; these are reader checks of assertions with saved counterexamples.','Worth a single notation and duality table.'),
18:('Known-results attribution and analytic proof dependencies',[69,71,72,73,74,75],'Preserve the request to identify known portions and the detailed proof-dependency comparison as editorial work.','Bibliographic attribution is distinct from the explicit mathematical generalization and reduction questions.','Worth retaining exact source locators and the independent dyadic route that removes circularity.'),
}}

CONTEXT_LINKS={
('ega',4):['MP-SA23-ega-02'],
('ega',29):['ED-SA23-ega-27','ED-SA23-ega-30'],
('ega',46):['ED-SA23-ega-15'],
}

def load(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def unique(xs):return list(dict.fromkeys(xs))

def write_tsv(p,fields,rows):
    with p.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

def direction_markdown(ds,title,editorial=False):
    text=[f'# {title}\n', ('These reader/editorial directions are preserved outside Stage6. Their earlier ratings are historical judgments, not an authorial-problem ranking.\n' if editorial else 'These Stage6 directions retain actual authorial question or deferred-step provenance. Editorial dependencies are listed separately. Ratings are manual1–5 judgments.\n')]
    for d in ds:
        text += [f"## {d.get('rank',d.get('original_rank',''))}. {d['title']}\n",
                 f"ID: {d['id']}. Interest: {d['interest']}/5. Feasible progress in one run: {d['feasible_progress_in_one_run']}/5.\n",
                 'Items: '+', '.join(d['items'])+'. Claims: '+', '.join(d['claims'])+'.\n',
                 'Authorial problems: '+(', '.join(d.get('problems',[])) or 'none')+'. Editorial tasks: '+(', '.join(d.get('editorial_tasks',[])) or 'none')+'.\n',
                 'Known: '+d['known']+'\n','Residual: '+d['residual']+'\n','First step: '+d['first_step']+'\n']
    return '\n'.join(text)

application=[]
all_aliases={}
for owner in ['ega','analysis_curves']:
    part=PARTS/owner
    baseline=load(part/'provenance/pre_origin_audit/problems.json')
    by_original={p['id']:p for p in baseline}
    claim_map={c['id']:c for c in load(part/'claims.json')}
    # Four inherited cote26 line ranges missed the very clauses they named.
    # The problem-origin reread fixes locators only; old locators stay visible.
    if owner=='ega':
        locator_repairs={91:'317–318',94:'337–338',95:'342–343',96:'347'}
        for number,loc in locator_repairs.items():
            c=claim_map[f'C-SA23-ega-{number:03}']
            c.setdefault('locator_before_origin_audit',{'source':c['source'],'scans':c['scans'],'lines':c['lines']})
            c['lines']=loc
        dump(part/'claims.json',list(claim_map.values()))
        its=load(part/'items.json')
        for it in its:
            linked=[claim_map[c] for c in it.get('claims',[]) if c in claim_map and int(c.rsplit('-',1)[1]) in locator_repairs]
            if linked:
                it.setdefault('locator_before_origin_audit',{'lines':it['lines']})
                it['lines']=[c['source']+':'+c['lines'] for c in linked]
        dump(part/'items.json',its)
    rows=[r for r in AUDIT['rows'] if r['owner']==owner]
    assert set(by_original)=={r['original_id'] for r in rows}
    problems=[];editorial=[];partial_map={}
    for row in rows:
        old=by_original[row['original_id']]
        n=int(old['id'].rsplit('-',1)[1])
        rec=copy.deepcopy(old)
        rec['source_records']=[copy.deepcopy(old)]
        rec['origin_audit']='integration/ega_problem_origin_review.json'
        rec['origin_audit_date']=DATE
        rec['source_cue']=row['rationale']
        rec['source_cue_locations']=[{k:v for k,v in ev.items() if k!='literal_transcription'} for ev in row['source_evidence']]
        rec['source_cue_literal']=[ev['literal_transcription'] for ev in row['source_evidence']]
        rec['title']=row['proposed_title']
        rec['origin_class']=row['origin_class']
        rec['date']=DATE
        rec['count_as_authorial_mathematical_problem']=row['count_as_authorial_mathematical_problem']
        if row['action']=='reclassify_to_editorial':
            rec['id']=row['proposed_id'];rec['original_id']=old['id']
            rec['record_type']='editorial task';rec['origin']='present-run editorial or verification task'
            rec['as_he_states']=row['proposed_scope']
            rec['source_statement_not_question']=old['as_he_states']
            rec['why_open']='Not an authorial open question. '+row['rationale']
            # Existing worth judgments were individually reviewed in the origin
            # audit; they describe the value of this reader task, not source openness.
            rec['worth']=old['worth']
            editorial.append(rec);all_aliases[old['id']]=[rec['id']]
        else:
            rec['record_type']='authorial mathematical problem'
            rec['origin']='authorial mathematical question, deferred step or unfinished programme'
            rec['as_he_states']=row['proposed_scope']
            rec['claims']=row['retained_question_claims']
            rec['asserted_context_claims']=row['asserted_context_claims_not_authorial_questions']
            rec['why_open'],rec['worth']=WHY_WORTH[owner][n]
            if (owner,n) in SCOPE_FATES:
                rec['plausible_today'],rec['state_of_art']=SCOPE_FATES[owner,n]
            rec['refs']=unique([r for c in rec['claims'] for r in claim_map[c]['refs']])
            # Preserve documentary absence separately, without repeatedly
            # appending a generic disclaimer to why_open on rebuild.
            rec['historical_explanation_limit']='No reason for later omission or abandonment is inferred beyond the explicitly quoted source cue.'
            rec['related_context_records']=CONTEXT_LINKS.get((owner,n),[])
            if n in PARTIALS[owner]:
                title,ns,scope,reason,worth=PARTIALS[owner][n]
                ed=copy.deepcopy(old)
                ed['id']=f'ED-SA23-{owner}-{n:02}-context'
                ed['source_problem_id']=old['id']
                ed['record_type']='editorial task';ed['origin']='present-run editorial or verification task'
                ed['origin_class']='editorial context separated from a retained authorial question'
                ed['title']=title;ed['as_he_states']=scope
                ed['claims']=[f'C-SA23-{owner}-{k:03}' for k in ns]
                ed['source_cue']=reason;ed['why_open']='Not an additional authorial mathematical question. '+reason
                ed['worth']=worth;ed['refs']=unique([r for c in ed['claims'] for r in claim_map[c]['refs']])
                ed['source_records']=[copy.deepcopy(old)]
                ed['origin_audit']=rec['origin_audit'];ed['origin_audit_date']=DATE
                ed['count_as_authorial_mathematical_problem']=False
                ed['scope_limit']='The broader original state-of-the-art and occurrence record are preserved as context; this task does not redirect or replace the surviving MP.'
                editorial.append(ed);partial_map[old['id']]=ed['id']
                rec['editorial_tasks']=[ed['id']]
            problems.append(rec)
        application.append({'original_id':old['id'],'action':row['action'],'target_id':rec['id'],'source_record_preserved':True})

    # Retain additional, separately justified source records created after the
    # 81-record review. Currently this is the bounded Deligne request only.
    existing=load(part/'problems.json')
    for p in existing:
        if p['id'] not in by_original:
            assert owner=='ega' and p['id']=='MP-SA23-ega-60',p['id']
            problems.append(p)
    assert len({p['id'] for p in problems})==len(problems)
    assert len({p['id'] for p in editorial})==len(editorial)
    dump(part/'problems.json',problems);dump(part/'editorial_tasks.json',editorial)
    dump(part/'problem_origin_applied.json',{'audit':str((WORK/'integration/ega_problem_origin_review.json').relative_to(WORK)),
        'approved_by_parent':True,'date':DATE,'retained_authorial_problems':len(problems),
        'whole_editorial_redirects':sum('original_id' in e for e in editorial),
        'partial_editorial_contexts':sum('source_problem_id' in e for e in editorial),
        'rows':[r for r in application if r['original_id'].startswith('MP-SA23-'+owner+'-')]})

    original_directions=load(part/'provenance/pre_origin_audit/directions.json')
    pids={p['id'] for p in problems};edids={e['id'] for e in editorial}
    ranked=[];ed_directions=[]
    for d0 in original_directions:
        d=copy.deepcopy(d0);d['source_records']=[copy.deepcopy(d0)]
        d['original_rank']=d0['rank']
        d['problems']=[p for p in d0['problems'] if p in pids]
        eddeps=[all_aliases[p][0] for p in d0['problems'] if p in all_aliases]
        eddeps += [partial_map[p] for p in d0['problems'] if p in partial_map]
        for p in d['problems']:
            eddeps += [x for x in CONTEXT_LINKS.get((owner,int(p.rsplit('-',1)[1])),[]) if x.startswith('ED-')]
        d['editorial_tasks']=unique(eddeps)
        assert set(d['editorial_tasks'])<=edids,(d['id'],set(d['editorial_tasks'])-edids)
        if d['problems']:
            d['rank']=len(ranked)+1;d['record_type']='Stage6 direction with authorial problem provenance'
            d['provenance_note']='Only problems lists authorial questions. Editorial dependencies are separately listed; the full earlier direction is preserved in source_records.'
            ranked.append(d)
        else:
            d.pop('rank',None);d['record_type']='editorial direction outside Stage6'
            d['stage6_eligible']=False
            d['provenance_note']='No confirmed authorial mathematical question remains among this direction’s dependencies. It is preserved as reader/editorial work and excluded from Stage6 counts/ranking.'
            ed_directions.append(d)
    dump(part/'directions.json',ranked);dump(part/'editorial_directions.json',ed_directions)
    (part/'directions.md').write_text(direction_markdown(ranked,'Ranked directions — '+owner))
    (part/'editorial_directions.md').write_text(direction_markdown(ed_directions,'Editorial directions — '+owner,True))

    # Narrative IDs are first expanded while the original ID set is still
    # available, then redirected. This avoids compact ranges spanning removed
    # MP records and leaves narrowed references manually adjusted below.
    sys.path.insert(0,str(WORK/'integration'))
    from id_rewrite_helper import rewrite_ids
    text=(part/'provenance/pre_origin_audit/section.md').read_text()
    if owner=='analysis_curves':
        # Existing owner shorthand is explicit; expansion is syntactic only.
        text=re.sub(r'\bMP(\d{2})(?!\d)',lambda m:'MP-SA23-analysis_curves-'+m[1],text)
    text=rewrite_ids(text,all_aliases,set(by_original),kinds=('problem',))
    if owner=='ega':
        text=text.replace('97 claims and 59 problems','98 claims and 37 authorial mathematical problems, with 34 separately preserved editorial tasks')
        text=text.replace('Claims001–013 and problems01–04 retain these distinctions.','Claims001–013 retain these distinctions; MP-SA23-ega-02 and MP-SA23-ega-04 are the actual marginal questions, while ED-SA23-ega-01 and ED-SA23-ega-03 preserve the separate reader checks.')
        text=text.replace('[C-SA23-ega-052; MP-SA23-ega-25; EGAIV4]','[C-SA23-ega-052; ED-SA23-ega-25-context; EGAIV4]')
        text=text.replace('[C-SA23-ega-061; MP-SA23-ega-31; EGAIII; EGAIV1; EGAIV4]','[C-SA23-ega-061; ED-SA23-ega-31-context; EGAIII; EGAIV1; EGAIV4]')
        text=text.replace('**82 entries,69 indexed subject items plus20 additional Codex subjects,97 claims,59 problems,48 reading alarms,35 links and12 ranked directions**','**82 entries,69 indexed subject items plus21 additional Codex subjects,98 claims,37 authorial mathematical problems,34 editorial tasks,48 reading alarms,37 links and7 Stage6 directions**')
        text=text.replace('Claim classes are A14, B24, C28, D0, E25 and F6.','Claim classes are A14, B25, C28, D0, E25 and F6. The added classB record concerns Deligne’s later theorem; both letter and theorem retain his authorship, and classA remains Grothendieck’s own later published work.')
        text=text.replace('The links comprise8 archive links,20 publication links and7 separately quarantined earlier-project leads.','The links comprise8 archive links,22 publication links and7 separately quarantined earlier-project leads.')
        insertion='''\n## A distinct deferred hard Lefschetz proof\n\nIn his letter of17 October1966, Deligne says he will not attempt the “théorème de Lefschetz vache” that year and hopes Grothendieck can find someone to prove it. The line gives no coefficients or base hypotheses. SGA7XVIII5.2.2, printedpp281–282, uses exactly that name for the cup-product isomorphisms and still conjectures the smooth case; the exposé is by N.Katz, based on Grothendieck’s notes. Deligne’s *Weil II*, Theorem4.1.1, printedpp217–218, proves the smooth projective ample-class statement over an algebraically closed field with rational l-adic coefficients, l different from the characteristic. This identifies a precise standard interpretation and its later resolution without pretending that every hypothesis is written in the1966 sentence. It is distinct from the parafactorial margins. No new computation is claimed: the source supplies no proof or calculation to redo. [SA23-1321; C-SA23-ega-098; MP-SA23-ega-60; EGA_KatzSGA7XVIII1973; EGA_DeligneWeilII1980.]\n'''
        text=text.replace('## 4. Descent',insertion+'\n## 4. Descent')
    else:
        text=text.replace('**20 subjects,85 claims,22 problems,38 reading alarms and9 ranked directions**','**20 subjects,85 claims,14 authorial mathematical problems,15 editorial tasks,38 reading alarms and8 Stage6 directions**')
        text=text.replace('## Questions that have definite answers','## Questions and asserted formulas with definite answers')
        text=text.replace('[C031–035; MP-SA23-analysis_curves-08;','[C031–035; MP-SA23-analysis_curves-08; ED-SA23-analysis_curves-08-context;')
        text=text.replace('[C051–057; MP-SA23-analysis_curves-14;','[C051–057; MP-SA23-analysis_curves-14; ED-SA23-analysis_curves-14-context;')
    text+='\n## Provenance of the problem index\n\nOnly explicit authorial questions, deferred mathematical steps and unfinished programmes are counted in Stage3. Asserted or proved results that needed present-run checking are preserved in editorial_tasks.json, with exact MP-to-ED redirects for whole reclassifications. Mixed records retain a narrower MP and separately named editorial context using source_problem_id. The approved row-by-row decisions and literal source cues are in integration/ega_problem_origin_review.json. '+str(len(ed_directions))+' directions with only editorial dependencies are preserved in editorial_directions.json and editorial_directions.md outside Stage6; their useful research proposals have not been discarded or given invented MP links.\n'
    (part/'section.md').write_text(text)

    coverage=(part/'provenance/pre_origin_audit/coverage.md').read_text()
    if owner=='ega':
        coverage=coverage.replace('Stage3:59 problems MP-SA23-ega-01–59, with supported formulation, separately modern scope, state of the art and bounded remaining issue.','Stage3:37 authorial mathematical problems after the complete origin audit and the separately recovered Deligne request;34 editorial tasks preserve23 whole redirects and11 partial context splits.')
        coverage=coverage.replace('Stage6:12 ranked directions,','Stage6:7 ranked directions,')
        coverage=coverage.replace('97 claims','98 claims').replace('20 additional','21 additional').replace('35 links','37 links').replace('Bibliography:85 records.','Bibliography:87 records.')
        coverage=coverage.replace('SA23-1301–1320 (89 total subject records)','SA23-1301–1321 (90 total subject records)')
        coverage=coverage.replace('C-SA23-ega-001–097','C-SA23-ega-001–098').replace('Classes A14,B24','Classes A14,B25')
        coverage=coverage.replace('8 across archive places,20 to published work','8 across archive places,22 to published work')
        coverage=coverage.replace('Twenty additional Codex subjects supply exact direction provenance','The original twenty additional Codex subjects supply direction provenance; SA23-1321 separately records the recovered Deligne proof request')
        coverage=coverage.replace('All182 core/analysis claims','All183 core/analysis claims')
    else:
        coverage=coverage.replace('**22 merged open/editorial questions**','**14 authorial mathematical problems plus15 editorial tasks**')
        coverage=coverage.replace('9 ranked directions','8 Stage6 directions')
    coverage+='\n## Approved problem-origin audit\n\nThe audit covers every original problem record:59 core and22 analysis/curves records. The initial records and directions are preserved under provenance/pre_origin_audit; the approved audit has exact literal cues. Whole reclassifications use original_id; partial editorial contexts use source_problem_id. Why-open and worth fields have been manually reviewed, and no missing historical reason is inferred. This part has '+str(len(problems))+' retained authorial problems, '+str(len(editorial))+' editorial tasks, '+str(len(ranked))+' Stage6 directions and '+str(len(ed_directions))+' editorial directions outside Stage6. Run apply_problem_origin_audit.py last after a full rebuild.\n'
    (part/'coverage.md').write_text(coverage)

    events_path=part/'check_events.tsv'
    events=list(csv.DictReader(events_path.open(),delimiter='\t'));fields=list(events[0])
    tag='Approved problem-origin audit:'
    events=[e for e in events if not e['outcome'].startswith(tag)]
    for rec in problems+editorial:
        if rec['id']=='MP-SA23-ega-60':continue
        events.append({'statement_id':rec['id'],'date':DATE,'who':'GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega',
            'type':'source provenance audit','outcome':tag+' '+rec['source_cue']+' No source transcription altered.'})
    write_tsv(events_path,fields,events)

out={'date':DATE,'approved_audit':'integration/ega_problem_origin_review.json','rows':application,
     'whole_editorial_aliases':all_aliases,
     'editorial_direction_paths':['parts/ega/editorial_directions.json','parts/analysis_curves/editorial_directions.json'],
     'owner_counts':{o:{k:len(load(PARTS/o/(k+'.json'))) for k in ['problems','editorial_tasks','directions','editorial_directions']} for o in ['ega','analysis_curves']},
     'rebuild_overlay':'parts/ega/apply_problem_origin_audit.py',
     'validation':{'original_81_covered_once':len(application)==81 and len({r['original_id'] for r in application})==81,
                   'whole_redirects_only_have_original_id':True,'partial_splits_only_have_source_problem_id':True}}
dump(WORK/'integration/ega_problem_origin_application.json',out)
print(json.dumps({'counts':out['owner_counts'],'whole_redirects':len(all_aliases),'validation':out['validation']},indent=2))
