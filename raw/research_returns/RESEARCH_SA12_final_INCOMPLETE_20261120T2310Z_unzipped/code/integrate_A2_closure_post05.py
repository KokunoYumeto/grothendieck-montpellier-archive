"""Integrate the audited persistent arithmetic counterexample to A.2 once."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
record = root / 'code/output/integrate_A2_closure_post05.json'
if record.exists():
    raise SystemExit('Already integrated; refusing to repeat the dated event.')

p = root / 'parts/A/paper_A.tex'
s = p.read_text()
anchor = r'\input{parts/A/topological_models_A2_post05.tex}'
assert anchor in s
s = s.replace(anchor, anchor + '\n' + r'\input{parts/A/quadratic_tower_A2_post05.tex}'
              + '\n' + r'\input{parts/A/quadratic_tower_consequences_A2_post05.tex}')
p.write_text(s)

p = root / 'parts/A/quadratic_tower_A2_post05.tex'
s = p.read_text().replace('[The elementary two-group calculation]',
                         '[Proved; the elementary two-group calculation]')
s = s.replace('[A quadratic step preserving ideal classes modulo two]',
              '[Proved; a quadratic step preserving ideal classes modulo two]')
s = s.replace('[Counterexample to A.2]',
              '[Refuted; A.2 even for an excellent Dedekind domain]')
p.write_text(s)

p = root / 'parts/A/arithmetic_tower_A2_post04.tex'
s = p.read_text()
s = s[:s.index(r'\paragraph{Unresolved construction.}')] + r'''
\paragraph{The non-Galois construction is completed below.}
Lemma~\ref{A:A2-quadratic-step} combines unramified inertness at
any prescribed finite set of primes with injectivity of ideal
extension modulo two and growth of its dimension. The resulting
non-Galois tower in Theorem~\ref{A:A2-persistent-arithmetic-counterexample}
satisfies both the noetherianity and class-persistence requirements.
The virtually procyclic restriction above explains why the full
integral closure in an arbitrary Galois tower was an inadequate route.
'''
p.write_text(s)

p = root / 'parts/A/iwasawa_A2_post02.tex'
s = p.read_text().replace('an exact arithmetic instance of the remaining gate',
                         'an exact cyclotomic arithmetic criterion')
s = s.replace('The general A.2 row therefore remains unresolved.', r'''
This leaves that particular cyclotomic instance undecided. The
unrestricted assertion A.2 is refuted independently by the non-Galois
tower in Theorem~\ref{A:A2-persistent-arithmetic-counterexample}; no
claim about the cyclotomic $\mu$-conjecture is inferred from it.''')
p.write_text(s)

p = root / 'parts/A/milnor_A2_post03.tex'
s = p.read_text().replace(r'''quotient. We have not proved that one finite deletion makes these
cokernels vanish on all finite normalizations. In particular, this
does not supply the missing uniform deletion for the excellent
Nagata--Gabber affine counterexample.''', r'''quotient. One finite deletion does not always make these cokernels
vanish: Theorem~\ref{A:A2-persistent-arithmetic-counterexample} gives
an excellent arithmetic counterexample already in generic dimension
one. The Nagata--Gabber example has a different outcome: its
eventual equality follows from the principal-completion theorem
proved below.''')
p.write_text(s)

p = root / 'parts/A/topological_models_A2_post05.tex'
s = p.read_text().replace(r'''remaining unrestricted-model problem is still recorded in
Section~\ref{A:unresolved}.''', r'''scope of these positive results is recorded in
Section~\ref{A:unresolved}. The unrestricted A.2 assertion is refuted
by the separate arithmetic construction below.''')
p.write_text(s)

p = root / 'parts/A/unresolved_A.tex'
old = p.read_text()
external = old[old.index(r'\begin{remark}[External modern reading consulted]'):
               old.index(r'\subsection{A.6 and A.7:')]
p.write_text(r'''\section{Part A: disposition and scope}
\label{A:unresolved}
Every requested Part A assertion is now decided in its stated
scope. The counterexamples and their proved replacements remain
separate from further classification questions about special fields.

\subsection{A.2 is refuted with persistent failure on every open}
Theorem~\ref{A:A2-persistent-arithmetic-counterexample} constructs
an excellent regular Dedekind domain $R$ with $2$ invertible and
$\cd_2(\Frac R)=1$, but $\cd_2(U)=2$ for every nonempty affine
open $U$. Its Picard group modulo two is infinite dimensional
after every finite deletion. The quadratic-step construction
preserves old classes modulo two by an explicit diagonal transfer,
while controlling splitting and ramification at every old prime.
Thus both the quasi-excellent and unrestricted readings of A.2
are refuted. Corollary~\ref{A:A2-sharp-curve-consequences} also
gives persistent dimension-one refutations of A.1 and both A.6
claims, with no orderable residue fields.

The general lower witness after shrinking remains valid by
Proposition~\ref{A:spread}. On curves, the exact replacement is
the simultaneous Milnor-residue criterion of
Theorems~\ref{A:Dedekind-Milnor-criterion} and
\ref{A:curve-normalization}, with the sharp upper bound one
greater than the generic dimension. This covers nonnormal and
nonexcellent curves. In generic dimension one the criterion is
divisibility modulo $p$ of the Picard groups of all finite
separable normalizations after one localization.

The positive results proved during the investigation retain their
full statements: all semilocal curves; schemes essentially of
finite type over a field; every noetherian model of an arithmetic
field of maximal cohomological dimension
$\operatorname{trdeg}_{\Q}K+2$; all models of the specified
strictly local surface fields; and semilocal or topologically
normal models of quasi-excellent strictly local fraction fields.
The Nagata--Gabber example satisfies eventual equality after its
specified parameter localization.

The cyclotomic comparison in
Theorems~\ref{A:Iwasawa-equivalence} and
\ref{A:canonical-Iwasawa} is still an exact equivalence for that
particular family. The non-Galois counterexample neither proves
nor refutes the full cyclotomic $\mu$-conjecture. Settling each
cyclotomic instance is not required to refute the universal A.2
assertion, and is not counted as remaining requested work.

\subsection{The other Part A questions}
Theorem~\ref{A:wild-affine-counterexample} supplies the excellent
regular complete two-dimensional counterexample to A.5, and
Theorem~\ref{A:wild-affine-upper} proves its uniform replacement.
The affine A.7 assertions hold over quasi-excellent bases and
fail without that hypothesis; their nonaffine versions as posed
fail without separatedness. The fraction-field and local lower
bounds in A.8 and A.9 hold in their precisely stated scopes,
with the real and characteristic exceptions explicitly decided.
The outcome table lists all individual variants and proof locators.

''' + external)

p = root / 'code/assemble.py'
s = p.read_text()
s = '\n'.join(line for line in s.splitlines()
              if not line.startswith("a.append(dict(zip(cols,['A:unresolved'")) + '\n'
s = re.sub(r"\('A\.2',.*?\),\n", "('A.2','Refuted even excellent regular Dedekind: generic cd2=1, every nonempty affine open has cd2=2; exact curve replacement proved','A:A2-persistent-arithmetic-counterexample; A:A2-quadratic-step; A:A2-sharp-curve-consequences; A:spread; A:Dedekind-Milnor-criterion; A:curve-normalization'),\n", s, count=1)
s = s.replace("('A.1','Refuted, even excellent regular with no real residues','A:nagata-global-consequences; A:realcone')", "('A.1','Refuted, even excellent regular with no real residues; failure persists on every nonempty affine open','A:A2-sharp-curve-consequences; A:nagata-global-consequences; A:realcone')")
s = s.replace("('A.6(i)','Refuted even excellent regular affine','A:nagata-global-consequences')", "('A.6(i)','Refuted even excellent regular affine, persistently with n=1 and cd=2','A:A2-sharp-curve-consequences; A:nagata-global-consequences')")
s = s.replace("('A.6(ii)','Refuted even excellent regular affine','A:nagata-global-consequences')", "('A.6(ii)','Refuted even excellent regular affine, persistently with n=1 and affine-open supremum=2','A:A2-sharp-curve-consequences; A:nagata-global-consequences')")
s = s.replace("('L2','Proposed A.6 conclusion refuted even excellent regular','A:nagata-global-consequences')", "('L2','Eventual equality and proposed A.6 conclusion refuted even excellent regular; generic lower persistence proved','A:A2-persistent-arithmetic-counterexample; A:A2-sharp-curve-consequences; A:spread')")
oldline = next(line for line in s.splitlines() if line.startswith("'A.2: the lower half"))
s = s.replace(oldline, "'A.2 is refuted by an explicit recursively constructed excellent Dedekind domain. Its fraction field is algebraic over Q with cd2=1, while every nonempty affine open has cd2=2 and infinite-dimensional Pic/2. A principal-ray-prime quadratic step gives an unramified, 2-split V-by-V class-field quotient over the next field; diagonal Artin transfer makes every extension map on S-ideal classes modulo two injective and doubles the rank. Eventual inertness at every rational prime gives finite splitting, bounded ramification, and Noetherianity; local degree growth kills the Brauer group over every finite extension of the limit field. The full proof received independent actual-file audits, and the seed and finite group calculations passed111784 exact assertions. The sharp curve bound and exact simultaneous-residue criterion are the proved replacements. No Part A gate remains requested open work.',")
s = s.replace('includes an infinite local group.', 'includes an infinite global image of a local group.')
p.write_text(s)

p = root / 'code/program_inventory.py'
s = p.read_text().replace('certs=[', "certs=[\n('parts/C/code/check_quadratic_tower.py','111784 exact assertions; ranks1,2,3 regular-module quotient, transfer, inertia and Frobenius; Q(sqrt(-35)) norm/Minkowski seed','parts/C/output/quadratic_tower_certificate.json','elapsed_seconds'),", 1)
p.write_text(s)

p = root / 'code/render_checkpoint.py'
s = p.read_text().replace("'first direct image'", "'first direct image','two-group calculation','quadratic step','counterexample to eventual','invariant abelian','upper-cone stabilization','topological normalization','finite global images','semilinear action','finite constant extensions'")
s = s.replace("if number==5:", "if number==6:\n    pages.update(range(21,34))\n    pages.update(range(65,82))\nif number==5:")
p.write_text(s)

p = root / 'report_supplement.md'
s = p.read_text().replace('The lower half holds in general. Eventual equality is now proved essentially of finite type over every field. The general case remains under active investigation.', 'The general lower half holds. A.2 is refuted by the excellent arithmetic Dedekind construction A:A2-persistent-arithmetic-counterexample, with cd2=1 generically and cd2=2 on every nonempty affine open. The exact curve criterion and the stated positive cases remain proved.')
s = s.replace('## Research decisions since checkpoint 01', '## Historical research decisions since checkpoint 01\n\nThe following checkpoint entries retain the state at their stated stage. The current outcome table and the latest closure entries supersede earlier unresolved statuses and scheduling statements.', 1)
s += f'''\n\n## A.2 closure at {now}\n\nThe quadratic-step lemma and its infinite tower refute A.2 even for excellent regular Dedekind domains. The construction starts from Q(sqrt(-35)), whose class group remains C2 after inverting2. At each step the explicit regular-module quotient supplies a wreath Galois group; complement inertia makes the upper extension unramified and2-split, and diagonal transfer preserves every old class modulo2. All old primes are simultaneously made unramified inert. The limit ring is Noetherian by its discrete local valuations and finite character. Its fraction field and every finite extension have vanishing2-torsion Brauer group, giving generic cohomological dimension1. Infinite Pic/2 survives every finite deletion, so each nonempty affine open has cohomological dimension2. Root and B independently audited the written proof and its seed; the finite certificate passed111784 assertions. The same construction gives the A.6 pointwise value n=1 against affine-open dimension2. All Part A requests are decided; the remaining requested rows are D.1, D.2(ii), and their L8 dependency.\n'''
p.write_text(s)

p = root / 'PROGRESS_LEDGER.md'
with p.open('a') as f:
    f.write(f'''\n\n## A.2 closed after review02: {now}\n\nThe universal A.2 assertion is now **refuted**, even for an excellent regular Dedekind domain of characteristic zero with2 invertible. The limit fraction field has cd2=1; every nonempty affine open has cd2=2 and infinite-dimensional Pic/2. A controlled quadratic-step lemma combines mod2 class-extension injectivity and rank doubling with unramified inertness at every prescribed old prime. The full ray-class/Kummer/transfer construction, Noetherian limit, arbitrary-finite-extension Brauer argument, and all-coefficient conclusion passed independent actual-file audits. The exact finite program passed111784 assertions, including the Q(sqrt(-35)) seed. No positive Iwasawa mu assertion is used. The previously proved sharp curve upper bound, generic lower persistence, exact Milnor-residue criterion, and positive field/model classes are retained as replacements.\n\nThis closes the A.2 requested row in both the quasi-excellent and unrestricted scope. A.1/A.6 gain the sharper persistent dimension-one counterexample. All Part A, B and C requests are decided. Only D.1, D.2(ii), and the dependent part of L8 remain. This is a dated status change, not an additional formal review. The next formal review is still05:10 UTC and checkpoint06 is due04:40 UTC.\n''')

with (root / 'parts/A/CHECK_EVENTS_A.tsv').open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['A:A2-wreath-calculation;A:A2-quadratic-step;A:A2-persistent-arithmetic-counterexample', now[:10], 'GPT-6 Astra; /root', 'independent actual-file proof, source and certificate audit', 'Read the complete final A fragment and finite certificate code/output. Independently derived principal ray-prime existence, regular-module quotient and all local Frobenius cases, diagonal transfer, Noetherian finite character, finite-extension local-degree inequality, arbitrary-coefficient cd1 and persistent Pic/2. Opened Milne CFT exact ray/transfer/ABHN locators, Milne ANT Theorem4.3 p70, and Stacks07QS.111784 finite assertions pass. Final integration at '+now+'. No mathematical gap found; no priority claim.'])
    w.writerow(['A:A2-sharp-curve-consequences', now[:10], 'GPT-6 Astra; /root', 'proof from the fully audited construction', 'Every closed residue field is an eventually quadratic union of finite fields, hence cd2=0; generic cd2=1 and local dimension1 give A.6 n=1, while every affine open has cd2=2. Exact curve replacement references retained.'])

record.write_text(json.dumps({'utc': now, 'status': 'A.2 refuted; A/B/C complete', 'remaining': ['D.1', 'D.2(ii)', 'L8 residual'], 'certificate_assertions': 111784}, indent=2)+'\n')
print(record.read_text())
