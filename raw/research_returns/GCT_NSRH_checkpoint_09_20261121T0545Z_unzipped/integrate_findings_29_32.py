from pathlib import Path

root=Path(__file__).resolve().parent
p=root/'GCT_NSRH.tex'
s=p.read_text()
f32=(root/'finding_F32.tex').read_text()
f29=(root/'finding_F29.tex').read_text()
f30=(root/'finding_F30.tex').read_text()
f31=(root/'finding_F31.tex').read_text()
f30body,f30dict=f30.split('In the language of schemes,',1)
f31body,f31dict=f31.split('% Separate paragraph for Part III',1)
f31dict=f31dict.split('% New bibliography keys requested',1)[0]
f31dict=f31dict[f31dict.index('\\paragraph'):]
if '\\label{f:countable}' not in s:
 s=s.replace('\\subsection{What the hypotheses mean geometrically}',f32+'\n\\subsection{What the hypotheses mean geometrically}',1)
if '\\label{f:tower}' not in s:
 s=s.replace('\\section{Two further geometric routes and their limits}',f30body+'\n\\section{Two further geometric routes and their limits}',1)
if '\\label{f:sphericity}' not in s:
 s=s.replace('\\subsection{Occurrence versus multiplicity}',f29+'\n'+f31body+'\n\\subsection{Occurrence versus multiplicity}',1)
dictionary=r'''
\paragraph{\fid{F29}: flag schemes and orbit dimensions.}
The action is that of the split group scheme $SL_n\times SL_n$ on
the partial flag scheme of its tensor product representation,
base-changed to $\C$. These flag schemes are iterated relative
Grassmannians, hence instances of the locally free Quot framework
in FGA, Expos\'e~221, \S3, Theorems~3.1--3.2. Their filtered
frame bundles give the Borel torsors used in the proof; the group
actions belong to SGA~3, I, \S4. The complete dimension and
stabilizer calculation proves only the absence of an open orbit for
this action. Cote~90, scan~17, anchors equivariant affine-module
language, not an attribution of this orbit theorem to the archive.

\paragraph{\fid{F30}: vector bundles and coherent commutants under specialization.}
'''+ 'In the language of schemes,'+f30dict+r'''
The framework is the affine module/sheaf equivalence of EGA~I,
\S9.5, and equivariant modules in SGA~3, I, 4.7.2--3; cote~90,
scan~17, is the audited archive anchor. Every needed idempotent
image, scalar commutant and special-fiber calculation is proved
in \fid{F30}; no general base-change theorem is asserted without
its hypotheses.

'''+f31dict+r'''
\paragraph{\fid{F32}: completed Tate classes and the limits of visible duality.}
For a countable direct sum of Tate pieces whose Euler trace has a
convergent nonnegative absolute moment, the theorem specifies exactly
the discrete completion being used. It is not an element of ordinary
finite $K_0$ merely by notation. Tensor multiplication is legitimate
because the absolute-moment estimate proves convergence and finite
grouping at each nonzero root. The formal binomial expansion of
$(1+\mathbb L^{-1})^{-4}$ in the actual trace has such a realization
at the level of convergent Euler spectra; its inverse Tate degrees
are unbounded. Dualization sends them to unbounded positive degrees,
outside this bounded-spectrum class. Thus an effective or signed
completed class still needs a specified duality and trace functor.
The finite trace framework is SGA~4\,$\frac12$, \emph{Rapport},
3.2, and SGA~5, III, 4.7. Cote~1, scans~77--78, records the
audited generic Fredholm trace/determinant vocabulary; neither it
nor finite $K_0$ supplies this countable extension. Its convergence
and reciprocal-finiteness proof is given in \fid{F32} itself.
'''
if '\\paragraph{\\fid{F32}: completed' not in s:
 s=s.replace('\\section{Archival audit and the Fable leads}',dictionary+'\n\\section{Archival audit and the Fable leads}',1)
s=s.replace('The coherent bundle above is not yet the original GCT tensor module, and the scheme model does not identify VIII\'s basis or formal quantum grading with Frobenius weights. These remain the precise comparison tasks.', 'The coherent bundle above models the algebra; \\fid{F21} below supplies the actual right tensor module. Neither construction identifies VIII\'s based left/right structure or formal quantum grading with Frobenius weights. Those remain precise comparison tasks.')
s=s.replace('$\\Spec A\\times_{\\Spec A^s}\\Spec A$; passing to its normalization\nseparates the character points and yields the other positive cone.', '$\\Spec A\\times_{\\Spec A^s}\\Spec A$. Separately, the coefficient\nHecke algebra $H=R[c]/(c^2-\\delta c)$ normalizes to $R^2$\n(and its tensor square to $R^4$); this separates its character\npoints and yields the other positive cone.')
s=s.replace('Change of rank-one positive model&F16 gives positive Tate structure data for the abstract algebra.&Restore the original tensor action; the sign-tensor-sign test shows it currently fails.', 'Change of rank-one positive model&F16 loses the actual action; F27 restores it in a localized four-character mixed Tate cone.&Identify the designated basis and operations; the repaired object is not pure of one weight.')
bibs=r'''
\bibitem{BlasiakRep} J.~Blasiak, \emph{Representation theory of the nonstandard Hecke algebra}, arXiv:1201.2209v2 (2012); Theorem~5.1, p.~14; Proposition~5.2, pp.~14--15; Definition~6.1 and Remark~6.2, p.~23. PDF equation~(25) has a different number in the converted HTML. \url{https://arxiv.org/abs/1201.2209v2}.
\bibitem{PPBounds} I.~Pak and G.~Panova, \emph{Bounds on certain classes of Kronecker and $q$-binomial coefficients}, author manuscript dated 13 October 2016; Lemma~1.3, p.~2. \url{https://www.math.ucla.edu/~pak/papers/QBC23.pdf}.
\bibitem{Brosnan} P.~Brosnan, \emph{On motivic decompositions arising from the method of Bia\l ynicki--Birula}, Invent. Math.~161 (2005), 91--111; inspected author PDF \S2, pp.~3--4, Theorems~3.3 and~3.5, pp.~5--6. \url{https://math.umd.edu/~pbrosnan/Papers/bb.pdf}.
'''
if '\\bibitem{BlasiakRep}' not in s:s=s.replace('\\bibitem{Run}',bibs+'\n\\bibitem{Run}',1)
s=s.replace('findings A01 and F01--F28','findings A01 and F01--F32')
p.write_text(s)
print('Integrated F29–F32 and their separate Grothendieck translations.')
