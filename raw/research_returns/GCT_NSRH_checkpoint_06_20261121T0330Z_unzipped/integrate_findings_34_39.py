from pathlib import Path

root = Path(__file__).resolve().parent
p = root / 'GCT_NSRH.tex'
s = p.read_text()

# These two corrections were requested by the full independent F39 review.
f39path = root / 'finding_F39.tex'
f39 = f39path.read_text().replace('equations~(7.1)--(7.2)', 'equations~(7.1)--(7.4)')
f39 = f39.replace('ordinary \\ell-adic', 'ordinary $\\ell$-adic')
f39path.write_text(f39)

if '\\newcommand{\\R}' not in s:
    s = s.replace('\\newcommand{\\A}', '\\newcommand{\\R}{\\mathbb R}\n\\newcommand{\\A}', 1)

dicts = []
def read_split(n):
    f = (root / f'finding_F{n}.tex').read_text()
    if '% Separate paragraph for Part III.' in f:
        body, tail = f.split('% Separate paragraph for Part III.', 1)
        tail = tail.split('% New bibliography keys:', 1)[0]
        dicts.append(tail.strip())
        return body.rstrip() + '\n'
    return f

f35 = read_split(35)
f38 = read_split(38)
f39 = read_split(39)
if '\\label{f:stacktrace}' not in s:
    anchor = '\\subsection{Actual pure classical multiplicity objects via geometric Satake}'
    s = s.replace(anchor, f35 + '\n' + f38 + '\n' + anchor, 1)
if '\\label{f:ncweil}' not in s:
    anchor = '\\subsection{A normalization that cannot be a finite Frobenius trace}'
    s = s.replace(anchor, f39 + '\n' + anchor, 1)
if '\\label{f:binarydimension}' not in s:
    anchor = '\\subsection{Occurrence versus multiplicity}'
    f34 = (root / 'finding_F34.tex').read_text()
    f37 = (root / 'finding_F37.tex').read_text()
    s = s.replace(anchor, f34 + '\n' + f37 + '\n' + anchor, 1)

dicts.append(r'''
\paragraph{\fid{F34}: effective representation classes and growth of graded algebras.}
The actual highest-weight multiplicities are ranks of effective Schur
summands, in the characteristic-zero representation $K_0$ of $\GL_2$.
Their exact positive simplex has dimension $k-2$; purity cannot alter
that growth degree. The polynomial bound fails only for the specified
compact encoding. Locally free Schur operations and their virtual
extensions use the SGA~3 representation and SGA~6 $\lambda$-ring
frameworks. Cote~133, scans~18--21, anchors those operations, not the
computational bound. The dimension and output-length arguments are
proved explicitly in \fid{F34}; they are not archival theorems.

\paragraph{\fid{F37}: effective multiplicity objects with compressed labels.}
The known rectangular identity identifies the marked-tree count with
the rank of the primitive Tate summand constructed in \fid{F31}.
Compression is a bijection on the finite indexing sets for each input,
so it changes neither that effective representation class nor its rank.
It gives a polynomial witness encoding under the listed-row convention;
it does not identify the trees with a canonical cycle basis or make their
recursion into a theta correspondence. Cote~133, scans~19--21, is a
framework anchor for finite-set operations, and cote~16, scans~35,37,39,
for primitive projectors. The exact counting input is PPS, Theorem~4.5;
the new encoding argument is the proof of \fid{F37} itself.
''')
if '\\paragraph{\\fid{F38} in Grothendieck' not in s:
    s = s.replace('\\section{Archival audit and the Fable leads}',
                  '\n\n'.join(dicts) + '\n\n\\section{Archival audit and the Fable leads}', 1)

known = r'''
\paragraph{The attached homogeneous PH1 is already false.}
Kahle--Micha{\l}ek \cite[Theorem~5 and Remark~6, p.~4]{KM}
prove that the fixed-inner-weight stretching function
\[
 \phi(s)=a_{(4s),(3)}^{(7s,5s)}
       =\frac{s+r(s)}3,\qquad
 (r(0),\ldots,r(5))=(3,-1,1,0,2,-2),
\]
with $r$ periodic modulo six, is not the Ehrhart function of a
rational polytope. Its degree is one, but $\phi(1)=0$ and
$-\phi(-1)=1$, contradicting the interior-versus-total inequality
in Ehrhart reciprocity. Their p.~2 explicitly identifies the target
as VI, Hypothesis~1.6.4. By the rectangular identification on their
p.~6, the same function is
\[
 g((4s,4s,4s),(4s,4s,4s),(7s,5s)).
\]
This is a cited prior refutation, not a new finding of this run.
Their pp.~3--4 distinguish the later 2011 formulation allowing
inhomogeneous families $Ax\le sb+c$. The cited theorem does not
exclude every dimension of that later formulation. We therefore
do not leave the old homogeneous assertion as an open gate, or
equate its failure with a refutation of every later positivity
program. Finding~\fid{F34} separately tests the compact dimension
requirement on a family with a genuine positive simplex model.

'''
if '\\paragraph{The attached homogeneous PH1 is already false.}' not in s:
    anchor = 'VI, Hypothesis~1.6.5 (SH),'
    s = s.replace(anchor, known + anchor, 1)

bibs = r'''
\bibitem{KM} T.~Kahle and M.~Micha{\l}ek, \emph{Plethysm and lattice point counting}, Electronic Journal of Combinatorics~25(1) (2018), P1.41; Theorem~5 and Remark~6, p.~4; formulation history, pp.~2--4; rectangular identification, p.~6. \url{https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p41/pdf/}.
\bibitem{PPS} I.~Pak, G.~Panova and J.~P.~Swanson, \emph{A combinatorial interpretation for certain plethysm and Kronecker coefficients}, arXiv:2511.02312v3, uploaded 27 July 2026, title-page date 28 July 2026; Lemma~1.3, p.~2; \S2.2, p.~5; Definition~3.2 and Proposition~3.4, p.~6; Lemma~4.2, p.~9; Definition~4.4 and Theorem~4.5, p.~10. \url{https://arxiv.org/abs/2511.02312v3}.
\bibitem{SunStacks} S.~Sun, \emph{L-series of Artin stacks over finite fields}, Algebra \& Number Theory~6 (2012), 47--122; Theorem~1.1, p.~49; Definition~4.1, p.~84; Theorem~4.2, p.~85; Theorem~4.8 and \S4.8.2, pp.~89--90; Example~7.4, p.~109. \url{https://msp.org/ant/2012/6-1/ant-v6-n1-p03-s.pdf}.
\bibitem{LO2} Y.~Laszlo and M.~Olsson, \emph{The six operations for sheaves on Artin stacks II: Adic coefficients}, Publ. Math. IH\'ES~107 (2008), 169--210; \S9.1, Lemmas~9.1.1--9.1.2, p.~198; Theorem~11.0.14, p.~204. \url{https://numdam.org/item/10.1007/s10240-008-0012-5.pdf}.
\bibitem{TabuadaWeil} G.~Tabuada, \emph{Noncommutative Weil conjecture}, inspected version arXiv:1808.00950v7 (2019); \S1, pp.~2--3, Theorem~1.5; \S5.1, pp.~13--14; \S6.1, pp.~15--16; \S7, equations~(7.1)--(7.4), p.~17. \url{https://arxiv.org/abs/1808.00950v7}.
'''
if '\\bibitem{KM}' not in s:
    s = s.replace('\\bibitem{Run}', bibs + '\n\\bibitem{Run}', 1)

# Update the front matter and current gates, without presenting the run as final.
s = s.replace('Derived lifts and a four-character model give complementary, carefully scoped results in rank one.',
'''An explicit Artin stack realizes that all-extension scalar trace, but its cohomology is unbounded and its actual dual has unbounded spectrum. Reciprocal trace realizations do not give tensor inverses in the usual derived Weil category. The actual collision algebra also fails the smoothness hypothesis of the specified noncommutative Weil framework. Derived lifts and a four-character model give complementary, carefully scoped results in rank one.''')
s = s.replace('The exact known rectangular and no-occurrence theorems are retained.',
'''Primitive Grassmannian motives and compressed marked-tree witnesses give concrete results for two-row rectangular coefficients. The known Kahle--Micha{\\l}ek counterexample already refutes the supplied homogeneous Ehrhart PH1; a separate compact-input growth argument rules out its uniform dimension bound even on a positive simplex family. The exact known rectangular and no-occurrence theorems are retained.''', 1)
s = s.replace('\\item \\gate{P: effective labels and polyhedra.} Produce polynomial-length witnesses and a polynomial-time checking predicate for a \\(\\#P\\) interpretation. PH1 additionally requires its Ehrhart family, dimension/bitlength bounds and separation oracle; SH or the relevant index bound is separate.',
'''\\item \\gate{P: effective labels under a stated encoding.} Specify the input convention before asking for polynomial witnesses. Finding~\\fid{F37} settles the equal-rectangle, two-row-output witness problem with explicitly listed rows. Finding~\\fid{F34} excludes a general \\(\\#P\\) claim under fully compact binary plethysm encoding. The attached homogeneous PH1 is already refuted by the cited Kahle--Micha{\\l}ek theorem; it is not an open requirement to be proved. Any replacement using inhomogeneous polytopes or another counting model needs its own exact formulation, size bounds and algorithm. SH or the appropriate index bound remains separate.''')
s = s.replace('The spectral theorems remove an estimate once the explicit trace and sign hypotheses are supplied. F19--F21 and F27 construct specified coherent or ordinary motivic realizations in the stated cases. They do not complete the general nonstandard realization, designated basis, comparison, complexity or obstruction gates; F26 excludes one precise normalized trace dictionary.',
'''The spectral theorems remove an estimate once the explicit trace and sign hypotheses are supplied. F32 extends the upper-radius argument to a specified countable completion, but bounded visible reciprocal duality then forces finiteness. F19--F21 and F27 construct specified coherent or ordinary motivic realizations. F35 closes the scalar stack-realization question for the actual normalized word trace; its dual does not satisfy the needed second bound. F38 excludes the proposed object-level tensor inverse in the usual derived Weil realization, and F39 excludes the direct nonsmooth collision category from the smooth proper noncommutative Weil framework. These results narrow particular realizations; the designated based operations and path-output comparison remain open.''')
s = s.replace('Neither the encodings nor PH1 follows', 'Neither the encodings nor a replacement for the refuted PH1 follows')
s = s.replace('neither the encodings nor PH1 follows', 'neither the encodings nor a replacement for the refuted PH1 follows')
s = s.replace('\\item \\textbf{Sign-only mechanism.} F01--F04, F17 and F24 are proved and checked; abbreviated versions are refuted by F05 and the F24 countermodels. Application to the designated nonstandard objects remains open at R/S. The specific inherited-positive-category route is refuted by F09, while F27 restores the actual rank-one action in a different cone and F26 excludes a specified normalized trace dictionary.',
'''\\item \\textbf{Sign-only mechanism.} F01--F04, F17, F24 and the admissible countable extension F32 are proved and checked; omitted-hypothesis versions are refuted by the displayed countermodels. F26 excludes the finite normalized all-extension word dictionary. F35 supplies a genuine stack scalar realization with explicit cohomology, while F38 separates its reciprocal traces from actual tensor inverses. The specified main transfer remains open at R/S/E; a scalar mass identity is not a construction of the operators, path output, dual bound or designated basis.''')
s = s.replace('\\item \\textbf{Positivity reached.} No new general canonical-basis, Kronecker/plethysm counting, or closure-multiplicity theorem follows from the available data. The exact known rectangular and two-row results are retained with their locators. General requested positivity remains open at E/L/C/P; multiplicity obstruction construction remains at O.',
'''\\item \\textbf{Positivity reached.} F31 gives actual primitive Tate motives for equal rectangles with two-row output. F37 gives polynomially verifiable compressed witnesses for the known marked-tree rule under the listed-row encoding. F34 proves the separate compact dimension and output-length obstructions. The supplied homogeneous PH1 is refuted by a cited prior theorem, including an equal-rectangle example. General designated canonical-basis positivity and strict orbit-closure multiplicity inequalities remain open at E/L/C/O; replacement effective rules require the revised P gate.''')
s = s.replace('findings A01 and F01--F32', 'findings A01 and F01--F32, F34--F35, F37--F39')
p.write_text(s)
print('Integrated checked F34, F35, F37, F38, F39 and the known PH1 refutation.')
