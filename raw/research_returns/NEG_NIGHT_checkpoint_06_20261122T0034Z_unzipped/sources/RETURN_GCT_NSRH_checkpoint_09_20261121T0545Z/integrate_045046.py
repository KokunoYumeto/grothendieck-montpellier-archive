"""One-time integration of checked fragments and verified primary locators."""
from pathlib import Path
import hashlib

root=Path(__file__).resolve().parent
p=root/'GCT_NSRH.tex'
t=p.read_text()
f45=root/'finding_F45.tex'
s45=f45.read_text()
s45=s45.replace('The data are smooth projective schemes, rational algebraic',
'''The trace-formula framework is SGA~5, III, 4.7; the data
are smooth projective schemes, rational algebraic''')
f45.write_text(s45)
f46=root/'finding_F46.tex'
s46=f46.read_text()
s46=s46.replace('All displayed fractions belong to $S_0$.',
                  'The parameters $z_1,z_2$ and $\\Delta$ belong to $S_0$.')
s46=s46.replace('For an arbitrary real algebraic parameter, the analogous\nall-conjugate claim would require total reality.',
'''For a general real algebraic parameter, total reality is a
sufficient additional hypothesis for the analogous all-conjugate
assertion; it is not asserted to be necessary.''')
s46 += r'''
The affine module/sheaf dictionary is EGA~I, Theorem~1.3.7,
p.~86, Corollary~1.3.8, p.~87, and Theorem~1.4.1,
pp.~90--92. Perfect complexes use SGA~6, I, Definition~4.7,
pp.~121--122, and Example~4.8, p.~122. The equivariant-module
framework is SGA~3, I, 4.7.2--3, with cote~90, scan~17,
as the audited archive anchor. The eigenvalue and complex-weight
conventions are BBD~5.1.2 and~5.1.8. These locators supply
the framework; the displayed resolutions and matrix-unit
arguments prove this particular comparison.
'''
f46.write_text(s46)
marker='% Separate paragraph for Part III.'
b45,d45=s45.split(marker,1)
b46,d46=s46.split(marker,1)
assert '\\label{f:projectiveword}' not in t
assert '\\label{f:cayleyweil}' not in t
pos=t.index('\\begin{finding}[\\fid{F47}')
pos=t.rfind('\\subsection',0,pos)
t=t[:pos]+b45+'\n'+b46+'\n'+t[pos:]
pos=t.index('\\paragraph{\\fid{F47} in Grothendieck')
t=t[:pos]+d45+'\n'+d46+'\n'+t[pos:]
t=t.replace('F01--F44, F47, with agent','F01--F47, with agent')
t=t.replace('EGA~I framework is \\S\\S1.3--1.4.',
'''EGA~I framework is Theorem~1.3.7, p.~86, Corollary~1.3.8,
p.~87, and Theorem~1.4.1, pp.~90--92.''')
t=t.replace("historical EGA~I framework of \\S\\S1.3--1.4;",
'''historical EGA~I framework of Theorem~1.3.7, p.~86,
Corollary~1.3.8, p.~87, and Theorem~1.4.1, pp.~90--92;''')
t=t.replace("within EGA~I's \\S\\S1.3--1.4 framework;",
'''within EGA~I's Theorem~1.3.7, p.~86, Corollary~1.3.8,
p.~87, and Theorem~1.4.1, pp.~90--92;''')
t=t.replace('Perfect complexes use SGA~6, I, 4.7 (original-source access\nqualified below), with the precise bounded-projective criterion',
'''Perfect complexes use SGA~6, I, Definition~4.7, pp.~121--122,
and Example~4.8, p.~122, with the modern bounded-projective criterion''')
t=t.replace('SGA~6, I, 4.7, supplies the\nhistorical perfect-complex framework,',
'''SGA~6, I, Definition~4.7, pp.~121--122, and
Example~4.8, p.~122, supply the historical perfect-complex framework,''')
old=r'''The original EGA~I scan has not yet been visually checked for
\S\S1.3--1.4; the actual module equivalence used above was
read in Stacks Lemma~26.7.5, tag~01IB. EGA~I, \S9.5, is
reserved for scheme-theoretic images, not that equivalence.
The original SGA~6 scan could not be visually retrieved here;
Expos\'e~V, \S\S2--3, is carried as background for the
$\lambda/\gamma$ formalism. Its perfect-complex locator is
instead I, 4.7, independently corroborated in the primary
Thomason paper \cite[\S3.1, pp.~8--9]{ThomasonPerfect}; this
is a locator check, not a fresh reading of SGA~6's proof.'''
new=r'''The original EGA~I affine-module statements and their proof
contexts were read, and printed pp.~86, 87 and~90 were visually
checked: Theorem~1.3.7, Corollary~1.3.8 and Theorem~1.4.1
(the last proof continues through p.~92). Stacks Lemma~26.7.5,
tag~01IB, supplies a separately read modern formulation.
EGA~I, \S9.5, is reserved for scheme-theoretic images.
The original SGA~6, I, Definition~4.7, pp.~121--122, and
Example~4.8, p.~122, were visually read from the facsimile;
the primary Thomason locator check
\cite[\S3.1, pp.~8--9]{ThomasonPerfect} is retained as
corroboration. Expos\'e~V, \S\S2--3, remains background for
the $\lambda/\gamma$ formalism, not a fresh original-source
proof check.'''
assert old in t
t=t.replace(old,new)
t=t.replace(r'\S\S1.3--1.4 (affine module/sheaf framework, original scan not freshly verified)',
            r'Theorem~1.3.7, p.~86, Corollary~1.3.8, p.~87, and Theorem~1.4.1, pp.~90--92 (affine module/sheaf framework; original scan and proof contexts checked)')
t=t.replace(r"Expos\'e~I, 4.7 (perfect complexes), and Expos\'e~V by P.~Berthelot, \S\S2--3 ($\lambda/\gamma$ operations). Original scan not visually verified in this run; used as background, not a claimed fresh source-proof check.",
            r"Expos\'e~I by L.~Illusie, Definition~4.7, pp.~121--122, and Example~4.8, p.~122 (perfect complexes; original facsimile visually checked); Expos\'e~V by P.~Berthelot, \S\S2--3 ($\lambda/\gamma$ operations; carried as background). Facsimile pages: \url{https://wstein.org/sga/sga/6/6t_121.jpeg} and \url{https://wstein.org/sga/sga/6/6t_122.jpeg}.")
bib=r'''\bibitem{WeilI} P.~Deligne, \emph{La conjecture de Weil. I},
Publ. Math. IH\'ES~43 (1974), 273--307; Theorem~(1.6), p.~276,
and its derivation from Theorem~(1.7), pp.~276--277.
\url{https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf}.

'''
assert r'\bibitem{WeilI}' not in t
t=t.replace(r'\bibitem{Run}',bib+r'\bibitem{Run}')
abstract='''
For the actual rank-three tensor lattice, a checked joint basis
makes both ordinary left and nonstandard right generators positive
and retains its bar. Every whole-word trace has an explicit
projective motive and hard Lefschetz, but a retained isotypic
projector obstructs the stronger positive representation-kernel
model. A relative smooth order retains the entire collision family.
A separate Cayley construction gives exact pure Weil End/Hom
objects, both actions, and perfect coherent objects on a projective
line, with explicit crossed extensions. Its chosen Frobenius fails
the extension-parameter rule and a smooth-projective integrality
test. Positive adjoint realizations of the full collision algebra
must kill its radical. These precise constructions and boundaries
leave the actual path-sign and designated-basis comparisons open.
'''
t=t.replace('\\end{abstract}',abstract+'\n\\end{abstract}',1)
summary=''' F43 supplies the actual positive joint action, full regular
commutant and tensor bar in rank three. F44 gives the relative
smooth corner and a precise Frobenius tradeoff. F45 supplies
projective word-dependent motives and hard Lefschetz, while proving
an obstruction when a specified commutant projector is retained.
F46 realizes the actual algebra, both actions and collision
extensions by pure Weil End/Hom data and coherent projective-line
objects; its chosen Frobenius fails the specified extension law
and constant-coefficient integrality comparison. F47 proves the
positive-adjoint radical obstruction. Existence of every finite
pure rank-three coefficient realization is therefore no longer
the gate; the required path-sign, arithmetic grading and
designated basis compatibility remain. '''
t=t.replace('Replacing all seven by the single phrase',summary+'Replacing all seven by the single phrase')
p.write_text(t)
for f in (f45,f46,p):
 print(f.name,hashlib.sha256(f.read_bytes()).hexdigest())
