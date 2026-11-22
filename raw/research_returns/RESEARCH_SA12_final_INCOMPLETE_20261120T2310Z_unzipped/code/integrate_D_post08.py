"""Record the fully audited post-checkpoint08 geometric extensions once."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import json

root = Path(__file__).resolve().parents[1]
record_path = root / 'code/output/integrate_D_post08.json'
if record_path.exists():
    raise SystemExit('Refusing to duplicate the post-checkpoint08 integration.')
labels = [
    'D:proper-log-finite-generation', 'D:log-regular-boundary',
    'D:generically-finite-projective-target',
    'D:residual-inseparability-bound', 'D:projective-base-generation',
    'D:projective-image-corollaries',
    'D:finite-formal-cone-cover', 'D:finite-cone-wild-bound',
    'D:negative-curve-finite-wild', 'D:torsion-first-obstruction-cover',
    'D:negative-curve-equality-finite-wild', 'D:wild-genus2-finite-inertia',
    'D:formal-retraction-cone-cover', 'D:formal-retraction-tame',
    'D:finite-cone-mixed-boundary', 'D:finite-cone-fixed-boundary',
    'D:hereditary-base-generation', 'D:iterated-fibration-generation',
    'D:finite-jet-cone-cover', 'D:split-first-neighborhood-finite-wild',
]
paper = (root / 'parts/D/paper_D.tex').read_text()
for label in labels:
    assert '\\label{' + label + '}' in paper, f'Not yet integrated: {label}'
assert 'Proposed for independent audit' not in paper
now = datetime.now(timezone.utc).isoformat()

p = root / 'code/assemble.py'
s = p.read_text()
for item in ['D.1', 'D.2(ii)']:
    old = next(line for line in s.splitlines() if line.startswith("('" + item + "',"))
    old_item, old_state, old_locators = ast.literal_eval(old.rstrip(','))
    state = (
        'Incomplete in general; projective-base and iterated-fibration criteria, '
        'proper log regular pairs, and mixed surface boundaries with finite cone '
        'covers proved; all-genus Schroer and finite-local-image cases retained'
    )
    locators = '; '.join(labels) + '; ' + old_locators
    s = s.replace(old, repr((old_item, state, locators)) + ',', 1)

old = next(line for line in s.splitlines()
           if line.startswith("'D.1/D.2(ii) remain open in full."))
description = (
    'D.1/D.2(ii) remain open in full. The new fixed finite cone-cover argument '
    'controls the full wild inertia image, not only pro-p quotients. A finite '
    'map of smooth exceptional curves, with the stated first and higher '
    'obstruction conditions, extends to a finite locally free formal cone '
    'map. Grothendieck existence algebraizes its finite algebra, formal '
    'functions identifies its normal local Stein ring with a completed '
    'section cone, and the actual radial DVR extension bounds every original '
    'wild image by the fixed field degree. In particular, a sole smooth '
    'exceptional curve of genus g and square -d has finite full wild image '
    'when d>max(0,2g-2). At d=2g-2 for g>=2 the same holds when omega_C '
    'tensor N is torsion, including every Q-Gorenstein germ with arbitrary '
    'Cartier index. A retraction of the entire formal neighborhood gives '
    'tameness for every d>0: a pure Frobenius base change makes the normal '
    'coordinates linear and identifies the actual completed boundary fields '
    'by a purely inseparable extension. A retraction only on O_Y/I^r, with '
    'rd>2g-2, suffices for a finite wild bound. The split first-neighborhood '
    'case has the numerical criterion d>max(0,g-1). These are explicit '
    'hypotheses, not claims about arbitrary negative curves. '
    'The earlier fierce genus-two example is now controlled for full '
    'nonabelian covers: its covering germ T has wild image of order at most4 '
    'and the original germ S at most8. The nonzero original quadratic wild '
    'cover remains a counterexample to universal tameness; neither upper '
    'bound is claimed to be attained. The new sixteen-assertion companion '
    'checks the finite differential, divisor, matrix and degree calculations; '
    'the geometric and full inertia arguments have separate complete proofs. '
    'A mixed finite boundary may contain Q-factorial, log canonical, formally '
    'graded, finite-cone-cover, formally retracted, finite-jet, and the two '
    'explicit genus-two germs. Retained singularities are unrestricted. '
    'For arbitrary fixed boundaries the non-Q-factorial points resolved by '
    'these criteria are required to be isolated in that boundary. Exact '
    'primary-ideal blowups descend the explicit completed one-curve models '
    'without introducing uncontrolled exceptional divisors. A single open '
    'normal subgroup avoids the finitely many finite exceptional wild images '
    'and is a quotient of a projective fixed-boundary tame group. '
    'The generic-fibre reduction also extends from curves to any projective '
    'normal base. One fixed smooth-surjective base open makes all descended '
    'constant-field covers etale there by smooth normalization and fpqc '
    'descent. At each remaining divisor, component multiplicity bounds the '
    'p-part of the ramification index, while one finite pure field extension '
    'bounds the inseparable residue degree. Their product bounds the full '
    'wild image. This includes every vertical boundary and every boundary '
    'whose reduced geometric generic normalization is projective. The exact '
    'base property is stability of fixed-boundary finite generation under '
    'all finite normal covers; it is inherited along towers with projective '
    'reduced geometric generic normalizations, including arbitrary towers of '
    'relative dimension at most one. These towers are global morphisms; '
    'rational pencils on modifications do not automatically qualify. '
    'Every proper fs log regular pair has finitely generated original '
    'fixed-boundary group by the precise Kummer-etale comparison and the '
    'proper relative-tame theorem. Any normal proper variety admitting a '
    'generically finite morphism to a projective image also satisfies every '
    'fixed-boundary assertion, via the Stein projective model and identical '
    'codimension-one DVRs. The remaining normal proper surface consequently '
    'admits no nonconstant morphism to a projective scheme. It must also '
    'avoid the earlier common-neighborhood, local-purity, mixed local, '
    'finite-field, all-genus Schroer and finite-global-local-image criteria; '
    'the latter include klt threefold omitted loci in characteristic>5. '
    'For a sole smooth exceptional curve, the new remaining numerical class '
    'has g>=2 and d<=2g-2; at equality omega_C tensor N is nontorsion, and '
    'therefore the germ is not Q-Gorenstein. Neither a full formal retraction '
    'nor a sufficiently high finite-order retraction may be assumed. '
    'The general case still requires control of new horizontal exceptional '
    'wild inertia or a uniform geometric bound on both finite-module first '
    'cohomology and nonabelian chief-crown multiplicities. Smallness, all-open '
    'pronilpotent generation, and a linear H1 bound alone do not give it.'
)
s = s.replace(old, repr(description) + ',', 1)
p.write_text(s)

entry = f'''

## Post-checkpoint08 proof integration: {now}

Twenty additional numbered statements are included, all with complete written proofs and independent actual-file audits. The requested statuses do not change: general D.1, general D.2(ii), and the dependent residual L8 remain open, and the report remains INCOMPLETE.

### Strict geometric reductions

The fixed finite formal cone-cover construction is stronger than the earlier formal-isomorphism recognition criterion. Its three cohomological conditions produce an actual degree-m finite local map from a completed normal section cone. The proof algebraizes the finite formal algebra over the projective completed resolution (Stacks09ZT), uses formal functions for the Stein ring, and identifies the genuine radial DVR. Intersecting wild inertia with the finite extension group, with purely inseparable factors treated separately, bounds the full wild image by m. Thus d>max(0,2g-2) suffices, replacing the earlier formal-linear numerical threshold d>max(0,4g-4). At equality d=2g-2, a torsion omega_C tensor N suffices. A finite tower of Frobenius, prime-to-p torsion trivialization, and Artin-Schreier torsors kills the degree-zero first obstruction. Every Q-Gorenstein index is allowed in this equality case.

The explicit genus-two source T has N=omega_C inverse, with F squared zero on H1(O_C). A degree4 cone map gives full wild image at most4 over T; composition with the established degree2 map gives at most8 over S. These bounds apply to arbitrary finite monodromy groups. The original nonzero quadratic wild cover still refutes universal tameness, but the two explicit germs are no longer remaining tests for infinite wild image. Root read and reran the sixteen-assertion companion at06:29 UTC: all16 passed in0.04670357100258116seconds. B and D runs and outputs are also retained. There are now22 finite-certificate programs in the consolidated inventory.

A formal retraction gives a stronger conclusion for every d>0. Frobenius along the fixed curve projection leaves only normal-coordinate obstructions, which vanish after qd>2g-2. At the actual completed boundary DVR the resulting extension is k(C)((t)) into k(C')((t)), pure of degree q with t unchanged. Therefore the original wild inertia vanishes. A finite-order retraction on O_Y/I^r, with rd>2g-2, gives instead a degree-q finite cone map after the stated two numerical inequalities. Normal-only corrections run through n=r-1; the first ordinary smooth-target obstruction is at n=r. The r=2 split-first-neighborhood criterion is recognition of the finite-cone construction, not separately counted as movement.

The mixed global surface theorem combines these classes with Q-factorial, lc and formally graded germs. It retains arbitrary singularities in the open and the isolation hypothesis for newly resolved singular points on an arbitrary fixed boundary. The exact image weighted Rees algebra, followed by a degree-one Veronese, identifies the primary blowup ideal of each explicit completed model. This ideal descends because it contains a power of the maximal ideal. No additional exceptional valuation is silently introduced. Every finite exceptional wild image is killed in one open subgroup, giving the projective fixed-boundary quotient argument.

### Higher-dimensional base and recognition results

The generic-fibre theorem now allows any normal projective base. The retained smooth-surjective locus gives one base open independent of the varying finite cover. Smooth normalization and fpqc etale descent give actual etaleness there, including codimension two. At each bad base divisor D, one fixed divisor E above it bounds e_p by its multiplicity, and a fixed pure field extension of kappa(D) bounds the residual inseparability of all descended covers. The product e_p times f_insep is the full wild order. Killing the finitely many resulting wild images reduces to a projective normal base cover. The proof includes nonreduced original geometric generic fibres by finite pure normalization.

The hereditary-base formulation identifies exactly the property used after that finite normalization. Induction proves it for every finite normal cover of every member of a global tower with projective reduced-geometric-generic normalizations; relative dimension at most one is automatic. This formal closure is recorded without an additional independent movement claim. Proper log regular pairs and generically finite morphisms to projective images supply two further precise recognition criteria. No global morphism is inferred merely from a rational pencil.

### Primary-source and literature record

Root and the relevant independent readers read the actual complete proof files. The new source checks include Stacks09ZT (finite-morphism Grothendieck existence),0BG4 (actual completed boundary DVRs),0BUA and09EE/09EB (wild inertia, including inseparable residue),03PK and0A3J (Kummer and Artin-Schreier sequences),04FF (formal etaleness),03GV and02VN (smooth normalization and fpqc descent),0EGH (degree-one Veronese), and33.43.4 in0A22 (projectivity in dimension at most one). All locators were opened with their relevant proofs; earlier duality and square-zero lifting sources were rechecked where used. AHLS2026 Proposition3.1.8, Definition3.2.4 and Theorem3.5.1 were read in the primary LaTeX source, as was Hoshi2006 PropositionA.10 pp57--58 with its exact codimension-one definition and proof. Unique bibliography ownership is preserved.

Before the formal-retraction argument, root searched the phrases "formal neighbourhood Frobenius negative curve", "formal neighborhood section Frobenius line bundle", "local fundamental group retraction curve characteristic", and stronger variants concerning negative normal bundles. The retrieved complex-analytic formal-principle and bundle papers did not provide the positive-characteristic statement used here; they are not cited as proof. Updated full-local-fundamental-group searches returned Suzuki2023 and older local smallness material, without a checked general full-generation theorem. No priority or exhaustive-search claim is made.

The strongest remaining surface gate excludes the classes above and every nonconstant global morphism to a projective scheme. In the sole-smooth-exceptional-curve branch it has g>=2 and d<=2g-2, no applicable full or finite-jet retraction, and at equality nontorsion omega_C tensor N. More complicated exceptional graphs remain. The report preserves the difference between a genuine strict main-gate reduction and a recognition or formal closure of an already included class. This entry is not a formal stopping review and creates no additional checkpoint. Checkpoint09 remains scheduled for06:55 UTC; formal review05 remains scheduled for07:10 UTC.
'''
for name in ['PROGRESS_LEDGER.md', 'report_supplement.md',
             'parts/D/ROOT_POST08_AUDIT_NOTES.md']:
    with (root / name).open('a') as f:
        f.write(entry)
previous = root / 'qa/pdf_verified_checkpoint08.json'
if not previous.exists():
    previous.write_text((root / 'qa/pdf_verified.json').read_text())
record = {
    'utc': now, 'new_statements': len(labels), 'labels': labels,
    'open_requested_rows': ['D.1 general', 'D.2(ii) general', 'L8 residual'],
    'strict_gate_reductions': [
        'fixed finite formal cone covers and full nonabelian wild bounds',
        'negative curves d>2g-2 and torsion equality case',
        'full wild bounds4/8 for the explicit genus-two germs',
        'mixed surface boundaries with these additional local classes',
        'generic-fibre reduction over arbitrary projective normal bases',
    ],
    'recognition_or_formal_closure_not_separately_counted': [
        'log regular and projective-target recognition',
        'split first-neighborhood numerical recognition',
        'hereditary-base and iterated-fibration closure',
    ],
}
record_path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
