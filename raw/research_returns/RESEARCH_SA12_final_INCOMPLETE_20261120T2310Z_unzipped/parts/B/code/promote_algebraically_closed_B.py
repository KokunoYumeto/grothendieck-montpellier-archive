from pathlib import Path
import csv
base=Path(__file__).resolve().parents[1]
p=base/'paper_B.tex'
s=p.read_text()
a=s.index('\\subsubsection*{Statement B.2c')
b=s.index('\\subsection{B.3:',a)
new=r'''\subsubsection*{Statement B.2c (Proved with the indicated scope: tangent stabilization)}
Choose a geometrically normal proper model whose $h^1(\mathcal O)$
is maximal among the bounded dimensions of B.2.  Every geometrically
normal proper model dominating it has the same first cohomology,
via pullback.  If $k$ is perfect, the normal-model category is
filtered, and this is eventual constancy of its tangent system.
Over an arbitrary field, every proper birational morphism from a
geometrically normal model to a smooth proper model induces an
isomorphism on $\operatorname{Pic}^{\tau}$.
\begin{proof}
Pullback on $H^1$ is injective by Leray and $f_*\mathcal O=\mathcal O$.
Maximal dimension therefore makes it an isomorphism.  Over a perfect
field, normalization of a graph is geometrically normal and gives a
common dominating model.  For the last assertion, base change to an
algebraic closure and apply B.1 to each geometric component, then
use faithfully flat descent of an isomorphism.

A tangent bound alone does not imply a group-scheme stabilization
bound: the proper finite groups $\alpha_{p^r}$ form a strictly
increasing system with constant tangent dimension one.  The following
statements supply the additional geometric control over an
algebraically closed field.  Over an imperfect field, a normalized
graph need not be geometrically normal; we do not silently use that
false cofinality assertion.
\end{proof}

'''
c=(base/'B2_completion_candidate.tex').read_text()
c=c[c.index('\\subsubsection*{Candidate B.2d'):]
for x,title in [('d','simultaneous embedding into one Jacobian'),('e','finite quotients of a smooth model'),('f','descent through a purely inseparable extension'),('g','full stabilization over an algebraically closed field')]:
 c=c.replace('\\subsubsection*{Candidate B.2'+x+': '+title+'}','\\subsubsection*{Statement B.2'+x+' (Proved): '+title+'}')
c=c.replace('Let $k$ be algebraically closed, let $Y$ be a smooth projective integral','Let $k$ be algebraically closed of characteristic $p>0$, and let $Y$ be a smooth projective integral')
c=c.replace('Choose $e$ with $(K\')^{p^e}\\subset K$, and put $q=p^e$.', 'In transcendence degrees zero and one, the unique normal proper model\nproves the assertion.  We may therefore assume transcendence degree at\nleast two.  Choose $e$ with $(K\')^{p^e}\\subset K$, and put $q=p^e$.')
c=c.replace('its kernel is a quotient\nof $\\ker(h_W)$.  Thus it is finite of order at most $nN$.',r'''its kernel is a quotient
of $\ker(h_W)$.  For clarity, if $h_W(x)$ belongs to $B_T$, then
fppf locally it equals $h_T(y)$ for some $y\in P_T$, because a
homomorphism onto its scheme-theoretic group image is faithfully flat.
Thus $x-y\in\ker h_W$, and the kernel is exactly
$\ker(h_W)/(\ker(h_W)\cap P_T)$.  Quotients by closed normal
subgroups exist as group schemes in this finite-type commutative
setting.  Hence $P_W/P_T$ is finite of order at most $nN$.''')
s=s[:a]+new+c+'\n'+s[b:]
p.write_text(s)
r=base/'references_B.bib'
with r.open('a') as f:f.write(r'''
@article{deJong1997,
  author = {de Jong, A. Johan},
  title = {Families of curves and alterations},
  journal = {Annales de l'Institut Fourier},
  volume = {47},
  number = {2},
  pages = {599--621},
  year = {1997},
  doi = {10.5802/aif.1575},
  url = {https://www.numdam.org/item/10.5802/aif.1575.pdf},
  note = {Opened: Situation 5.3 p.613, Theorem 5.13 and Corollary 5.15 pp.619--620, and projectivity in Theorem 5.9 and Proposition 5.11. The invariant field is allowed a finite purely inseparable extension; no separable Galois regular alteration is assumed. Accessed 2026-11-20}
}
''')
f=base/'results_B.csv'
with f.open(newline='') as x:rows=list(csv.DictReader(x))
for row in rows:
 if row['id']=='B.2c':
  row['statement']='Maximal h1 stabilizes under further geometric-normal dominations; over perfect fields this is the tangent direct system; smooth-target birational Pic isomorphism descends to arbitrary fields'
  row['status']='Proved under stated hypotheses'
  row['notes']='The original draft cofinal-graph argument over imperfect fields was removed; geometric normality need not survive normalized graphs.'
 if row['id']=='B.2-U':
  row['statement']='Full Pic^tau stabilization over arbitrary imperfect fields with geometrically normal models'
  row['depends_on']='B.2d-B.2g prove algebraically closed case; geometric-normal model category need not be filtered over imperfect fields'
  row['notes']='Only the imperfect-ground-field descent/cofinality issue remains; infinitesimal heights are controlled in the algebraically closed case.'
for x,st,dep in [('d','Simultaneous closed immersions of all modification Pic^tau groups into one fixed generic-curve Jacobian','B.2a; B.2b; Kummer; logarithmic differentials'),('e','Full Pic^tau stabilization for invariant fields of finite group actions on smooth projective varieties','B.1; finite-character kernel bound; invariant divisor norm; Kleiman Theorem6.3'),('f','Full Pic^tau stabilization descends through a finite purely inseparable function-field extension over algebraically closed k','B.2d; Frobenius factorization; fixed Jacobian torsion bounds'),('g','Full Pic^tau system is essentially constant over algebraically closed k','B.2e; B.2f; deJong1997 Corollary5.15')]:
 rows.append(dict(id='B.2'+x,statement=st,status='Proved',where_proved='paper_B.tex Statement B.2'+x,depends_on=dep,manuscript_pages='29/075',notes='All finite group schemes and infinitesimal kernels are included; not merely a tangent-space assertion.'))
with f.open('w',newline='') as x:
 w=csv.DictWriter(x,fieldnames=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writeheader();w.writerows(rows)
(base/'unresolved_B.tex').write_text(r'''% Only unchecked scope remains here.
\section{Unresolved gate attached to Part B}
\subsection*{B.2-U: the imperfect-ground-field formulation}
The uniform $h^1$ bound is proved for every ground field in B.2.
The full scheme-theoretic Picard stabilization is proved over an
algebraically closed ground field in B.2g; the finite-height issue is
resolved by B.2d--f, not assumed from tangent boundedness.

The remaining assertion is full essential constancy over an arbitrary
imperfect field when the index category is restricted to geometrically
normal models.  A normalized graph of geometrically normal models need
not remain geometrically normal, so an argument saying only that
normal graphs give a cofinal subsystem is insufficient in that scope.
We are checking descent and the precise categorical formulation.
This concern does not affect the arbitrary-field cohomological bound:
its graphs are formed only after passage to an algebraic closure.

The literal N.B. on scan075 lists separate dimension, torsion-order,
and tangent bounds.  The chain $\alpha_{p^r}$ shows why tangent
boundedness alone is not a formal substitute for full stabilization.
It is not a geometric counterexample.  Our earlier failed alteration
argument, which had not controlled infinitesimal images or kernels,
is superseded over algebraically closed fields by the fixed-Jacobian
argument and finite Galois/purely inseparable descent.
''')
with (base/'CHECK_EVENTS_B.tsv').open('a') as f:
 for x,out in [('B.2d','Root independently audited Lie-zero kernel, descent of prime-torsion points, Kummer covers, and dlog detection; no gap found.'),('B.2e','Checked character-kernel construction universally, decomposition-group ramification divisibility, semilocal divisor norm, numerical triviality, and exact quotient length bound.'),('B.2f','Root independently audited q-power descent and Jacobian[q] bound; intermediate model is finite normalization of Frobenius twist, ensuring normality, projectivity and exact function field.'),('B.2g','Opened deJong1997 Situation5.3, Theorem5.13, Corollary5.15 and projectivity construction; combined with B.2e and B.2f.'),('B.2c','Corrected prior imperfect-field cofinality overclaim: maximal tangent dimension still controls further dominations, but normalized graphs need not be geometrically normal.')]:
  f.write(x+'\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b with root audit where stated\ttargeted proof check\t'+out+'\n')
print('Promoted B.2d-g; corrected B.2c scope; reduced B.2-U to imperfect ground field; updated bibliography, results and check events.')
