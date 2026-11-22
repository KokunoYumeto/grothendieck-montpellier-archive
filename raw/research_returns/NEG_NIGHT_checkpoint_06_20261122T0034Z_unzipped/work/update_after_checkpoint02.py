"""Record the reviewed gate changes after checkpoint02, without making a checkpoint."""
import argparse
import csv
import json
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--utc',required=True)
args=parser.parse_args()
root=Path(__file__).resolve().parent.parent
path=root/'work/main_gates.json'
rows=json.loads(path.read_text())
g={r['id']:r for r in rows}

r=g['Q-MAIN03']
r['state']='rank-one coherent Frobenius parity hardness proved even in a smooth generic pencil; polynomial uniform NP isolation remains open'
r['finding_ids']+=';NN-C023;NN-C024'
r['current_gate']='A polynomial deterministic odd/unique restriction family remains missing. The geometric gate is now a single Frobenius entry in an explicitly based coherent line: deterministic computation for the smooth generic pencil gives P=parity-P; a polynomial algorithm on the smooth finite-field promise gives parity-P in BPP and NP=RP by verified search.'
r['approaches_tried']+=' Constructed a degree-r form in r variables whose rank-one top coherent Frobenius entry is parity-SAT. A Fermat pencil supplies generic smoothness and a randomized finite-field smooth specialization with controlled field bitlength; purity does not compute the entry.'
r['next_step']='Seek deterministic polynomial-cost good specialization, or a restricted witness family with efficient hashed parity; retain the precise succinct input and promise model.'

r=g['Q-MAIN07']
r['finding_ids']+=';NN-S014'
r['approaches_tried']+=' Sharpened the required final-output supported-zero probability to Omega(log n/n²), and constructed a uniform randomized test selector for uniform circuit families.'

r=g['Q-MAIN08']
r['finding_ids']+=';NN-C023;NN-C024'
r['approaches_tried']+=' Genuine smooth projective finite Weil objects can still encode parity-counting in a rank-one coherent Frobenius entry; object existence and purity are separate from effective evaluation and from a canonical GCT realization.'

r=g['Q-MAIN10']
r['finding_ids']+=';NN-A021'
r['state']='effective fixed-order and fixed-unitary-rank negative-time intervals proved; quantitative rates and global collision law remain open'
r['approaches_tried']+=' Certified a terminating rational fixed-order interval by compact interval arithmetic and effective sector bounds. Proved the corresponding all-degree positive character interval for every fixed U(d), with finite failure rank tending to infinity.'
r['next_step']='Seek a quantitative angular rate uniform in all zero indices; distinguish this from a collision height-time law.'

r=g['Q-MAIN11']
r['finding_ids']+=';NN-A021'
r['state']='exact fixed-rank unitary character boundary proved; GCT realization and quantitative detecting-rank rate remain open'
r['current_gate']='The least failing U(d) rank equals the least negative-minor order for the translated coefficients of E_t(z−1) near zero, and diverges as t approaches0 from below. A quantitative rate requires uniform angular control. These positive real representation weights do not supply integral nonstandard canonical-basis constants.'
r['approaches_tried']+=' Proved positivity for every polynomial irreducible at fixed rank and all degrees, the exact PF_d dictionary, and an effective rank-dependent interval.'
r['next_step']='Quantify the detecting rank; keep the shifted generating function distinct from the original heat coefficients and any integral GCT realization.'

r=g['Q-MAIN12']
r['finding_ids']+=';NN-S014'
r['approaches_tried']+=' A refined KKL/Talagrand threshold and explicit uniform empirical test selection strengthen the generator cancellation probability to Omega(log n/n²), including uniform randomized security for uniform circuits.'

r=g['Q-DIMOPT']
r['state']='minimum7064 proved for arbitrary monic quadratic cells, degW<=2 and positive rational constant ratios; global optimum open'
r['finding_ids']='NN-G011;NN-G019;NN-G021;NN-G022'
r['current_gate']='Unequal monic quadratic cells require at least7958 pairs even for arbitrary-degree W. Any improvement below7064 with monic quadratic cells and constant positive rational ratios must therefore use a common cell and higher-degree W; other remaining routes change the cell degree/leading coefficient, ratios, or table shape.'
r['approaches_tried']+=' Removed unnecessary auxiliary positivity, allowed rational ratios and proved exact7064 optimum with eight minimizers. The independent table verifier passes132 positions and1000 triples. An algebraic shared-root/parity argument excludes all unequal quadratic improvements without any bound on W degree.'
r['next_step']='Analyze common quadratic cells with arbitrary-degree W; a mass bound alone is not a degree bound.'

path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
stamp=args.utc.replace('-','').replace(':','').replace(' ','T',1).replace(' UTC','Z')
(root/'work/gate_history'/f'{stamp}.json').write_text(json.dumps({'date_utc':args.utc,'kind':'interim state; not the scheduled movement review','gates':rows},ensure_ascii=False,indent=2)+'\n')

p=root/'deliverables/LEDGER.md'
s=p.read_text()
s=s.replace('checkpoint02 is due at21:34:37 UTC','checkpoint02 was due at21:34:37 UTC, created at21:37:52 UTC and saved at21:38:08 UTC (about three minutes late); checkpoint03 is due at22:19:37 UTC')
s=s.replace('8. **Dimension-ring optimality:**7276 is proved minimal in the stated integral-ratio subclass (NN-G019). A new7064 construction and larger rational-ratio optimum theorem are written as NN-G021, awaiting root review at this ledger update. No global optimum is claimed.','8. **Dimension-ring optimality:**7064 is proved minimal for arbitrary monic quadratic cells, degreeW at most2, positive rational constant ratios and signed auxiliary parameters (NN-G021–022). Unequal cells cost at least7958 even for arbitrary-degree W. Common cells with higher-degree W and more general table classes remain open.')
s=s.replace('Root read all GCT findings and analytic findings in full; the GCT track read all eleven root findings in full. Root read the complexity proofs; newly added sections and the rational-weight height clarification are tracked separately until read.','The review map identifies every complete reading. Root has read the complexity, GCT and analytic findings through C024, G022 and A021; the GCT track has read root findings through S014. Newly added statements remain separate until their entire proof has been read.')
s=s.replace('the first successful build was131 pages. Visual layout checks and final cross-reference passes remain separate from proof checks.','the current checked checkpoint draft is145 pages. All page text bounds passed, and sample pages1 and105 were visually inspected without clipping. New material requires a new build and layout check; these are separate from proof checks.')
s+='\n## Dated update: '+args.utc+'\n\nThis is an interim update, not the three-hour movement review. New completed proof reviews establish:\n\n- NN-C023 encodes parity-SAT in a single explicitly based coherent Frobenius entry. NN-C024 preserves that entry in a smooth generic pencil and a randomized smooth finite-field promise reduction. The algorithmic gate survives genuine finite Weil objects and purity.\n- NN-G021 lowers the composing dimension-ring score to7064 and proves optimality in a larger rational-ratio class. NN-G022 excludes unequal monic quadratic cells from any improvement, even for arbitrary-degree W.\n- NN-A021 proves all-degree character positivity at each fixed U(d) on a certified negative-time interval, identifies it exactly with PF_d of the translated coefficients, and proves finite failure ranks diverge.\n- NN-S014 strengthens the required final-output cancellation probability to Omega(log n/n²) and supplies a uniform polynomial-time randomized distinguisher when this condition fails.\n\nThe source record now includes fresh root checks of Katz2.3.7.12–2.3.7.17, SGA1 II4.10(iii)/4.12, Deligne Weil I1.6, Etingof5.22.1/5.23.2, and Faraut2007 Sections4.1–4.2. Complete input proofs are not inferred from those locator checks.\n'
p.write_text(s)

p=root/'deliverables/IMPLICATIONS.md';s=p.read_text()
s=s.replace('At rank three, a verified dimension ring has7276 cancelling pairs, and NN-G019 proves that number minimal in its precisely stated integral-ratio subclass. A7064 improvement and an expanded rational-ratio optimum proof are drafted as NN-G021 and await the separate review recorded in the register.','At rank three, a verified dimension ring now has7064 cancelling pairs. NN-G021 proves the exact optimum in its rational-ratio, signed-auxiliary class, and NN-G022 enlarges the class to unequal monic quadratics by proving they require at least7958 pairs, even for arbitrary-degree W.')
s+='\n## Smooth cohomology and finite-rank characters\n\nNN-C023–024 sharpen the effectiveness obstruction beyond unknown cohomology rank or singularities. A compact degree-r equation in r variables has an explicitly based one-dimensional top coherent cohomology group whose Frobenius entry is parity-SAT. A smooth generic pencil keeps this invariant; a polynomial-bit finite field and a randomized specialization give a smooth projective example with probability greater than three quarters. Thus a polynomial smooth-input Frobenius or point-parity procedure would put parity-P in BPP and, after checked-witness search, give NP=RP. The generic symbolic zero test instead gives a deterministic parity-P collapse. The distinctions between these two conclusions are part of the theorem. SGA1 II4.10–4.12 supplies the smoothness criterion, Katz2.3.7.17 the rank-one formula, SGA7 II XXII3.1–3.2 the trace and zeta congruences, and Deligne Weil I1.6 the purity of good fibers.\n\nNN-A021 resolves the finite-rank character question. Every fixed U(d) sees positive character weights in all polynomial representation degrees for some negative-time interval. Each negative time nevertheless fails at some finite rank. The exact PF_d criterion applies to the Taylor coefficients of E_t(z−1), so the representation boundary is not confused with an unshifted coefficient test. This remains an analytic probability measure on irreducibles, not an integral vector-bundle multiplicity or a canonical GCT basis.\n\nNN-S014 makes the cancellation obstruction apply to ordinary uniform randomized security for uniform split-circuit families. Its sampling procedure chooses a coordinate or two-coordinate test with polynomial cost and proves a necessary final-output zero-fiber size Omega(2^n log n/n²). The finite-scheme rank interpretation is EGA IV4 18.2.1–18.2.2; no purity claim enters that probability bound.\n'
p.write_text(s)
print(json.dumps({'date_utc':args.utc,'gate_history':f'work/gate_history/{stamp}.json','scheduled_movement_review':False}))
