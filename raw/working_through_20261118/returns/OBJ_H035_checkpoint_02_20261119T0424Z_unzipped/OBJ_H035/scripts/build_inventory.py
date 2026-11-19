"""Maintain the statement inventory; working statuses are deliberately conservative."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
rows=[
(1,'002.1–15','Construction de faisceaux de modules','Cover programme: reconstruct coherent modules and apply to prorepresentation and invariants','Programme; precise affine realization supplied by Theorem 12'),
(2,'003.2–7','F : Mod A → (Ens)','Restriction to A-algebras and canonical module structure on a left exact set-valued functor','Canonical A-linearity is our explicit reconstruction'),
(3,'003.8–13','Lemme 1','Faithfully flat descent of module representability, including finite and finitely presented versions','Noetherianity unnecessary'),
(4,'003.14–004.13','Lemme 2','Representability from completion, punctured principal open, left exactness and filtered colimits','Finite modules over the completed ring are literal test objects'),
(5,'004.14–005.12','Proposition 3','Noetherian induction using generic representation on every quotient','Exclude the zero quotient in the nonnilpotent-element clause'),
(6,'005.15–006.10','Proposition 4','Local representability from left exactness, filtered colimits, completion and finite length values','Matlis duality supplies the omitted argument'),
(7,'006.11–007.2','Lemme 5','Local finite representability under conditions (i)–(iv)','Separated from the strict prorepresentation assertion'),
(8,'006.22–007.27','F est strictement proreprésentable','Strict prorepresentation by finite modules with generic representation on integral quotients','The displayed f in A/p must be nonzero; literal zero is vacuous'),
(9,'008.1–7','la fonction … est constructible','Generic representation on integral quotients implies constructible fibre rank','Noetherian stratification'),
(10,'008.8–26','En sens inverse','Claimed converse from constructible rank and generic normality','False without an extra finite-value hypothesis; repaired by Theorem 12(iv)'),
(11,'009.1–3','Lemme 6','Generic local freeness of gr_J(O_S) and gr_J(F) over S_red','The scheme is locally noetherian; this is not generic Cohen–Macaulayness'),
(12,'009.4–19','Tor','Generic vanishing of all positive Tor for regular-sequence quotients and a coherent module','Undefined M in the proof is the coefficient module'),
(13,'009.20–010.19','Corollaire 7','Generic base change for Hom under arbitrary local regular-sequence quotients','Correct the coefficient and use all positive Tor vanishing'),
(14,'010.5–11','K','The displayed two-term Hom complex','The scan writes P where the coefficient must be Q'),
(15,'010.12–18','Tor','Claimed sufficient two-term cohomology base-change criterion','Z^1 is insufficient; B^1 or a Tor_2 hypothesis is required'),
(16,'011.1–3','module de différentielles pour un C.M.','Characterization by indecomposable injective parameter quotients','Ink says différentielles; canonical-module interpretation is ours'),
(17,'011.4–9','Lemme 8','Canonical module descends modulo a regular sequence','Modern interpretation of faisceau fondamental'),
(18,'011.10–14','Corollaire 9','Parameter quotient of a canonical module is an indecomposable injective','Over the artinian local parameter quotient'),
(19,'011.15–22;013.1–7','Corollaire 10','Dense open with coherent generic canonical module and parameter-duality tests','Locally embeddable in a regular scheme'),
(20,'011.17m','excellent','Excellent replacement for the regular-embedding hypothesis','Generic canonical module, not a global dualizing complex'),
(21,'011.17m','EGA IV 6.11.8','Claimed extension under the CMU condition of EGA IV','False: CMU does not ensure generic Gorenstein or canonical modules'),
(22,'012.5–8','valeur absolue','Definition on the inserted typescript','Off H035; f(0)=0 is missing literally'),
(23,'012.13–20','PROPOSITION 1','Valuative absolute values and the bound on integer multiples of 1','Normalize f(0)=0; prove the binomial criterion'),
(24,'012.21–23','COROLLAIRE 1','Every absolute value in positive characteristic is valuative','Only nonzero elements of the prime field are roots of unity'),
(25,'012.24–25','équivalentes','Equivalence by taking a real power','The exponent must be strictly positive'),
(26,'012.26–30','PROPOSITION 2','Classification of absolute values of Q','Include the trivial absolute value; complete the interrupted proof'),
(27,'013.1–7','c)','Parameter-quotient Hom tests detect surjections between finite modules','All parameter systems are essential; surjectivity can be removed'),
(28,'013.8–20','Corollaire 11','Cancelled finite-module isomorphism criterion using Omega','Retain cancellation and separate rewritten definitions'),
(29,'015.7–016.9','Corollaire 11','Stationarity of a prorepresenting system under finite-value and parameter-base-change tests','Strictness and finite terms dropped in the rewrite; required for the explicit stage assertion'),
(30,'016.10–017.22','Théorème 12','Finite-module representability criterion (i)–(vi)','Main question; repair dependencies without changing its hypotheses'),
(31,'017.23–26','Remarque 13','Generically regular integral quotients replace regular embedding and make (v) redundant','Use (vi) with Omega=B and generic freeness'),
(32,'018.1–25','Théorème 14','Proper Hom representability for finitely presented F,G with G flat over the base','Arbitrary base change; Hall C,D and Example 3.10'),
(33,'018.5m;024.17–21','passage à la limite','Quasi-coherent first-argument extension of Hom representability','Filtered union of finitely presented modules, then colimit of representing modules'),
(34,'019.1–9','En fait','Higher Ext and cohomology functors satisfy the non-left-exact axioms','Underived coefficient tensor product must be retained'),
(35,'019.10–020.9','Lemme 15','Generic regular-quotient base change for finitely many sheaf Ext degrees','Finite-type morphism and coherent coefficients over a noetherian base'),
(36,'019.21–020.8','les K','Bounded-complex Tor criterion for cohomology base change','All positive Tor for terms and cohomology; explicit double-complex proof'),
(37,'020.10–23','Lemme 16','Generic relative Tor vanishing for a coherent module','Ink changes R to F; generic freeness must apply to gr R as well as gr O_X'),
(38,'021.1–21','Lemme 17','Generic regular-quotient base change for proper cohomology','Literal quantifier s in S is false; corrected s in U'),
(39,'022.1–8','foncteur constructible','Definition and proposed composition theorem for constructible functors','Exact affine composition class remains under investigation; do not substitute a smaller class'),
(40,'022.4–8','Ext … Tor … R^q f_*','Proposed two-scheme constructible-functor theory and examples','Unqualified direct image fails finite values without properness'),
(41,'022.10–023.8','Théorème 19','Affine restriction of scalars along a proper flat finitely presented morphism','Represent algebra maps by linear maps plus closed equations'),
(42,'022.13–15;023.1–8','de prés. finie (resp de type fini)','Finite-presentation and finite-type refinements of Theorem 19','Separate the two finiteness assertions'),
(43,'023.9–17','Corollaire 20','Restriction of scalars preserves closed immersions between affine X-schemes','Reduce by universal section to the closed-subscheme condition'),
(44,'023.18–24.6','premier cas','Linear-cone case and embedding into a cone','Coherent need not be locally free; formula needs f_*'),
(45,'024.7–16','Murre, th. 3','Closed subscheme parameterizing bases on which Y=X','Murre exp.294 Theorem 3, printed page 255, hypotheses matched'),
(46,'024.17–21','Remarque 21','Restriction of a quasi-coherent linear cone is a linear cone','General quasi-coherent coefficient, no finiteness claim'),
]
fields=['id','tag','locator','his_words','date','statement','reconstruction','status','proof_or_reference','later','check_events','confidence']
with (root/'STATEMENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t'); w.writeheader()
 for n,loc,words,claim,rec in rows:
  w.writerow(dict(id=f'H035.{n}',tag='H035' if n not in range(22,27) else 'off-object:absolute-values',locator='94/'+loc,his_words=words,date='Undated; catalogue: [à partir de 1965]; no exact page date',statement=claim,reconstruction=rec,status='open — proof drafted, second check pending' if n<=15 else 'open — working argument recorded',proof_or_reference=f'PROOFS.tex §H035.{n}' if n<=15 else 'research/WORKING_ARGUMENTS.md',later='',check_events='',confidence='Provisional; not a completion certificate'))
ledger=root/'PROGRESS_LEDGER.md'
with ledger.open('a') as f:
 f.write('\n## Statement inventory at 2026-11-19T03:37Z\n\n')
 f.write('All 46 statement rows are now enumerated. Working arguments are not final checks. The first 15 proof sections are drafted. No item is marked settled until its independent check or exact reference match is recorded. The main gate is the proof of Theorem 12 using repaired 5 bis and strict Corollary 11. The separate composition programme H035.39 retains a genuine completion-compatibility obstruction. The results archive remains closed.\n\n')
 for n,loc,words,claim,rec in rows:
  f.write(f'- H035.{n}: open. {claim}. Gate: {rec}.\n')
print(f'Wrote {len(rows)} provisional statement rows and the matching ledger inventory.')
