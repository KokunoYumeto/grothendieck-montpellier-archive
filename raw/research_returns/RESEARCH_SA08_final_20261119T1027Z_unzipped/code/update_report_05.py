"""Refresh the fifth-checkpoint report after explicit PDF approval."""
from pathlib import Path
import json, runpy

root = Path(__file__).resolve().parents[1]
runpy.run_path(str(root/'code/update_report_04.py'), run_name='__main__')
path = root/'RESEARCH_SA08_report.md'
text = path.read_text()
text = text.replace('0.031828 seconds. The possible next relation-obstruction group',
                    '0.032493 seconds in the final run with unimodular certificates. The possible next relation-obstruction group')

marker = 'Source download, source inspection, OCR, registry consolidation, and packaging scripts are also retained.'
begin = 'Additional mathematical computations completed before checkpoint 05:'
extra = '''Additional mathematical computations completed before checkpoint 05:

- B_check_fermat_pushout.py: three exact symbolic cases, primes 3, 5 and 7; 0.937367 seconds. The certificate checks the polynomial factorization, differential identities, closedness syzygy, weights, formal curve equation, the nonzero leading coefficient at infinity and logarithmic residue minus one. These supplement the all-odd-prime C19 proof.
- D_bar_closure_check.py: 2,144 exact checks, including all rank-one bar differential and contraction matrices through arity eight, low-arity signed shuffles, Leibniz identities, odd squares and divided squares; 0.048110 seconds. D029 supplies the integral proof for arbitrary free parameters and every arity.
- C_signed_shuffle_checks.py: 4,956 exact unitriangular columns, with every parity choice on two letters through length eight and three letters through length five, together with integral divided-power coefficients and odd-square checks; 0.083071 seconds. The general signed Lyndon argument and relative K-flatness proof are in C24.

'''
counter = root/'logs/D_lifting_counterexample.json'
if counter.exists():
    data = json.loads(counter.read_text())
    elapsed = next((data[k] for k in ('elapsed_seconds','runtime_seconds','seconds') if k in data), None)
    extra += ('- D_lifting_counterexample.py: 10 exact checks of the square-zero lifting counterexample over Z, F2 and F3; '
              + (f'{elapsed:.6f} seconds. ' if elapsed is not None else '')
              + 'The complete receipt lists the coefficient rings, chain-map identities, unique degreewise lift and nonzero chain defect. D031 gives the all-nonzero-ring proof and the corrected lifting hypotheses.\n\n')
if begin in text:
    a=text.index(begin); b=text.index(marker,a); text=text[:a]+extra+text[b:]
else:
    text=text.replace(marker,extra+marker)

source_marker = '## Computation record'
source = '''The additional bar-repair source checks distinguish exact usable results from failed leads. Richter's normalized divided-power construction is opened at Theorem7.5 and Section8; D029 gives the positive-cochain regrading and integral contraction explicitly. Melançon–Reutenauer's Section4, printed pp589–590, supplies the unsigned triangularity; C24 proves the signed extension instead of assuming it. Caradot–Lin arXiv:2511.22614v4 was read at Section2.1, Proposition3.10 and Theorem3.15: D031 gives a complete counterexample to Proposition3.10's unrestricted lifting assertion, with a finite certificate and correct sufficient replacement hypotheses. The distinct theorem is not refuted. Searches of tame-model and shuffle literature, including unsuccessful attempts to inspect a particular Hazewinkel chapter paragraph, are recorded with their exact scope in notes/A_source_searches.md. No priority is claimed.

'''
if source not in text:text=text.replace(source_marker,source+source_marker)

gate_start=text.index('C.3: special universally flasque theories')
gate_end=text.index('\n\nL7:',gate_start)
gate='''C.3: special universally flasque theories have contractible nerve; strict common-source equalization is false over every nonzero base. C16–C17 prove common sources and terminal localization for every coefficient ring with finitely many noninvertible rational primes, including the flat-term category and optional q≤w support. The smallest remaining coefficient ring is Z. The two remaining assertions are an admissible common source for every pair and terminal localization at all morphisms. Neither is inferred from primewise existence.

The excluded constructions remain explicit. Ordinary tensor products have prime-power Tor in unbounded weights (C11). Independently marked free PD disks over Z fail except for the ordinary weight-one disk (D022–D023). Projection-preserving arithmetic gluing with unbounded first flasque weights is impossible (C12). Standard tails are not an initial comparison family (C13). Free linear-disk replacements and free resolutions of coefficient tails have the distinct obstructions in C14–C15. C19 now shows that arbitrary ordinary common-target pushouts can create unbounded degree-one cohomology even rationally. These are counterexamples to the specified methods, not to global uniqueness itself.

The positive results now separate the issues more sharply. D027–D028 identify the nonfree differential-image problem with explicit marked-line intersections, prove the first-row eventual bound, and exhibit a finite integral H3 class; no higher eventual bound is extrapolated from computations. C18 constructs delayed nonlinear p-local closures, but does not construct compatible maps from the delayed coefficient tails. C21 constructs one global common partial model with free terms, uniform horizontal bounds, correct H0, and a vertical comparison through degree d after inverting floor((d+1)/2)!. It is not asserted to be admissible integrally.

C20 computes a nonzero possible relation-obstruction group. C22 proves that the actual second quadratic map nevertheless has a simultaneous strict simplicial repair. C23 proves the corresponding fixed-arity repair for any one odd disk under explicit finite-range flatness and acyclicity hypotheses. The distinction between a possible group and an actual class is retained throughout.

D029 supplies an integral functorial bar closure in positive cochain degrees, with an explicit contraction and all arities. D030 extends a prescribed original disk map through bar arity two without adding a new degree-one parameter. C24 proves the relative vertical base-change property for a split free parameter inclusion: the larger bar closure is semifree and K-flat over the smaller, so the ordinary pushout is a universal vertical quasi-isomorphism. This relative algebraic property is proved; it is not substituted for a target-map extension theorem.

The remaining construction tasks are compatible higher and mixed-arity maps with prescribed earlier boundary data, control of coefficient-tail delays and uniform horizontal bounds, and an actual global comparison/descent argument. These auxiliary advances do not by themselves change the requested C.3 row or prove a strictly smaller global coefficient-ring gate. The next formal review remains responsible for applying the user's movement criterion to the actual remaining assertions.'''
text=text[:gate_start]+gate+text[gate_end:]

qa_start=text.index('## Typesetting status')
qa_end=text.index('## Proved obstructions, approaches and remaining gates',qa_start)
qa=text[qa_start:qa_end]
addition=('The subsequent build29 introduced one 46.7365 pt overflow in the quadratic-certificate paragraph; the paragraph was rewritten and its location added to the inspection set. A twelve-column exact matrix also required increasing the documented matrix-column limit; the failed build and repaired build are retained. ')
qa=qa.replace('The approved current LuaLaTeX build has ', addition+'The approved current LuaLaTeX build has ')
text=text[:qa_start]+qa+text[qa_end:]
path.write_text(text)
print(json.dumps({'report':path.name,'checkpoint_update':5,'remaining_requested_rows':['C.3','L7']},indent=2))
