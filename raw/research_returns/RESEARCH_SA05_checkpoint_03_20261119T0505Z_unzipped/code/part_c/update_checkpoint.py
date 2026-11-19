from pathlib import Path
import csv,re,json
ROOT=Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
p=ROOT/'sections/part_c.tex'
s=p.read_text()
marker='\\subsection{C.2: the special bivariant systems}'
addition=r'''\begin{example}[An explicit genus-three failure]
\label{c:fermat-counterexample}
\status{Proved counterexample}
Let $C/\C$ be the plane quartic $X^4+Y^4=Z^4$, and take $o=(0:1:1)$. Its modified diagonal $M_o$ vanishes in every Weil cohomology, but
\[
 M_o\ne0\quad\hbox{in }\CH^2(C^3)_\Q.
\]
Thus the cohomological relation in Proposition~\ref{c:modified-diagonal} fails in rational Chow groups for this completely specified genus-three pointed curve.
\end{example}

\begin{proof}
The three partial derivatives $4X^3,4Y^3,-4Z^3$ have no common projective zero, so $C$ is smooth. Adjunction for a smooth plane quartic gives $g=(4-1)(4-2)/2=3$. The displayed point lies on $C$. Every product of three positive-degree cohomology classes on a curve is zero; Proposition~\ref{c:modified-diagonal} therefore gives the cohomological vanishing.

Put $J=\operatorname{Jac}(C)$ and $i:C\to J$, $x\mapsto[x-o]$. We use the precise nontorsion assertion of \citet[Theorem 4.1, printed p.~104]{c_bloch1984}: the Ceresa cycle $\Sigma=i_*[C]-[-1]_*i_*[C]$ for this Fermat quartic has infinite order modulo algebraic equivalence. We spell out the stronger detected class in its proof, to justify the passage to the modified diagonal. Over $\Q(i)$, Bloch projects its $5$-adic Abel--Jacobi class to the rank-two summand of $H^3(J)(2)$ with Hodge types $(3,0),(0,3)$ before twisting. This class $\beta_5$ is nonzero by his Theorem 3.4 and the proof preceding it. The proof of Theorem 4.1 shows that it is nontorsion: a torsion class would come from invariants of that summand with $\Q_5/\Z_5$ coefficients; Frobenius at $11$ acts there as $-11$, so $-11-1=-12$ is a $5$-adic unit and those invariants vanish. Restriction to any finite extension cannot kill a nontorsion class, because restriction followed by corestriction is multiplication by the extension degree.

For $s:C^3\to J$, $(x,y,z)\mapsto i(x)+i(y)+i(z)$, direct pushforward of the seven terms gives
\[
 s_*M_o=[3]_*i_*[C]-3[2]_*i_*[C]+3i_*[C].
\]
This is also the identity in \citet[Proposition 5.3]{c_grossschoen1995}. Taking its odd part under $[-1]_*$ gives
\[
 \frac{1-[-1]_*}{2}s_*M_o
 =\frac12\bigl([3]_* -3[2]_*+3\bigr)\Sigma.
\]
Abel--Jacobi is functorial for proper pushforward. On $H^3(J)$, multiplication by $m$ acts by $m^3$ under pushforward, since $\dim J=3$ and $[m]_*[m]^*=m^6$. The projected Abel--Jacobi class of this odd part is consequently
\[
 \tfrac12(3^3-3\cdot2^3+3)\beta_5=3\beta_5\ne0.
\]
It follows that $M_o$ is nontorsion over every finite extension of $\Q(i)$. If it were zero in $\CH^2(C^3)_\Q$ over $\C$, the finite set of rational-equivalence data would spread over a finitely generated $\overline\Q$-algebra; specializing to a closed point where the finitely many divisors and rational functions remain defined would give the same rational equivalence over $\overline\Q$, and then over a finite extension. This contradicts the restriction--corestriction argument. Hence the asserted Chow nonvanishing holds over $\C$.

The polynomial smoothness certificate, the point substitution, the genus value, and the coefficient $3^3-3\cdot2^3+3=6$ are recorded by \texttt{check\_explicit\_bad\_reduction.py}. The nontorsion input is the opened theorem and its proof, not a claim that this finite polynomial certificate computes a Chow group.
\end{proof}

'''
if 'c:fermat-counterexample' not in s:s=s.replace(marker,addition+marker)
p.write_text(s)
b=ROOT/'part_c/references.bib'
s=b.read_text().replace('Partly opened: primary introductory page 95 states the nontorsion theorem for the Fermat quartic; exact Theorem 4.1 page retrieval in progress. Do not count its full proof as checked until the source ledger is updated.','Opened: original GDZ digitization and OCR, printed pages 95 and 102--104. Theorem 3.4 and the full proof of Theorem 4.1, p. 104. The page-104 URL is https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0350/00000110?_format=xml; local copies and extracted text retained.')
b.write_text(s)
rows=[
('c:def-pointed','Pointed partition generators and their degrees','Proved','Definition','Poincare algebra','11:55','Definition used throughout C.1.'),
('c:graph-rule','Complete product rule by graph cycle rank','Proved','Theorem','Frobenius coevaluation; Euler class','11:55-57','Checked for 2286 graph pairs in finite models.'),
('c:matrix-presentation','Finite presentation and every graded dimension from exact contraction matrices','Proved','Theorem','Poincare duality; c:graph-rule','11:51-57','Gaussian elimination gives all linear relations; uses full ambient pairing.'),
('c:modified-diagonal','Modified diagonal criterion and failure of generation by M alone','Refuted; corrected theorem proved','Proposition','Poincare duality','11:51-53; R8','P1 with k=2 refutes M-only generation; correct cohomology degree is 4n.'),
('c:pair-ranks','Closed dimensions and relation generators for curves and b1-zero surfaces','Proved','Theorem','Orthogonal/symplectic invariant theory; Yin 2.5; Tavakol 6.1-6.4','11:51-57','Finite numerical ranks checked against hook-length formulas.'),
('c:other-dimensions','Exact coefficient-matrix dimensions for projective spaces and abelian varieties','Proved','Proposition','Exterior algebra; projective-space cohomology','11:51-57','Explicit rank algorithms in every k and degree; no unsupported closed simplification.'),
('c:chow-positive','All tautological cohomology relations lift for distinguished abelian cycles and pointed hyperelliptic curves','Known; application proved','Theorem','OSullivan 6.2.5-6.2.6; Tavakol 6.4; Gross-Schoen 4.8','11:51-57; Lead C1','The K3 all-powers assertion is not included here.'),
('c:k3-gate','Restricted all-powers K3 injectivity is equivalent to the 23rd h2 alternating projector and Kimura finite-dimensionality','Proved equivalence; general vanishing unresolved','Theorem','Yin main theorem; Beauville-Voisin 1 and 3.2','11:51-57; Lead C1','Smallest missing universal determinant occurs on 46 factors; does not finish C.1(c).'),
('c:fermat-counterexample','Fermat quartic with point (0:1:1) has nonzero rational Chow modified diagonal','Proved counterexample','Example','Bloch Theorems 3.4 and 4.1; Gross-Schoen 5.3','11:51-57; Lead C1','Smooth genus three; Bloch 5-adic class yields odd pushforward 3 beta5.'),
('c:bivariant-def','Axioms and adjoint-pair morphisms for special gauged bivariant systems','Proved','Definition','Perfect traces and product-square base change','11:38-48','Unrestricted Cartesian base change excluded explicitly.'),
('c:bivariant-equivalence','Special bivariant systems equivalent to graded Frobenius algebras with adjoint-pair morphisms','Proved','Theorem','c:bivariant-def; tensor contraction','11:38-48','Includes full faithfulness, Weil cohomology example, and associativity.'),
('c:lie-centre','Adjoint invariants equal Lie centre, with component action retained','Proved','Proposition','Characteristic-zero reductive groups','12:59','Pro-reductive inverse-limit version included.'),
('c:serre-centre','Arithmetic Lie-centre dimension is one plus half the maximal CM degree','Proved under stated hypotheses; unconditional for motivated abelian type','Theorem','Andre 0.6.2; Deligne 8.23,8.25; Taniyama Lemmas1-2','12:59; Lead C3','Geometric centre alone is generally infinite-dimensional.'),
('c:finite-field-lie','Elliptic Frobenius torus has algebraic Lie dimension two while analytic dimension is one','Proved counterexample','Example','Explicit point count and split-prime valuations','12:59; R6','Tout valid for commutative band; single Q(0) invalid for algebraic Lie interpretation.'),
('c:level-def','Geometric level convention as in 12:111-115','Proved','Definition','Supplied transcriptions','12:111-115','Not identified with a numerical weight bound or coniveau.'),
('c:level-counterexample','Prompt general min(i,n-1)+j level bound fails for an elliptic structural morphism','Refuted','Proposition','Explicit E/F5 and odd weight','12:118-120; R6','Manuscript box is min(i,n)+j; margin has extra relative-dimension condition.'),
('c:level-special-cases','Sharp smooth-projective constant-coefficient levels and strict normal-crossing local formula','Proved in stated cases','Proposition','Hard Lefschetz; purity; Kummer classes','12:118-120','Universal sharp replacement and margin remain unresolved.'),
('c:vz-positive','Codimension-one good reduction extends under Vasiu-Zink conditions, including e <= p-1','Known; application proved','Theorem','Vasiu-Zink 3 and Corollary4; normal Hom extension; NOS','12:142; Lead C5','Improves sufficient e<p-1 to e<=p-1.'),
('c:explicit-bad-reduction','Explicit quotient abelian surface over W(Fbar2)[[u,v]]/(2-uv) is good in codimension one but has no global abelian model','Proved counterexample','Theorem','Explicit elliptic equations; nonflat R plus m t closure; Hom extension','12:142; Lead C5','All polynomial identities checked over integers without inverting 2.'),
('c:subgroup-versus-object','Finite group objects extend on a punctured regular surface but subgroup embeddings may fail','Proved','Remark','Reflexive extension and Hartogs; explicit closure','12:142; R6','Corrects ambiguity in the finite-subgroup reduction and a dual-arrow typo in Vasiu-Zink Lemma27.'),
('c:ell-independence-cases','Independence for H1, good-reduction generated motives, semistable G-valued abelian type and potentially CM motives','Proved in stated cases','Proposition','SGA7 IX 2.2.5 and 2.2.9; Kisin-Zhou 1.2; Deligne Taniyama Remark3','12:140','Arbitrary bad-reduction tensor summands not claimed.'),
('c:ell-independence-gate','Arbitrary ramified descent and proposed equivalence with a general named conjecture','Unresolved','Remark','Kisin-Zhou Conjecture1.1 and explicit post-Theorem1.2 warning; Commelin5.1','12:140','Common Weil-Deligne conjecture implies independence; converse not established.')]
with (ROOT/'part_c/results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes'])
 for r in rows:w.writerow([r[0],r[1],r[2],'sections/part_c.tex, '+r[3]+' label '+r[0],*r[4:]])
with (ROOT/'part_c/CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 for r in rows:w.writerow([r[0],'2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check',r[2]+': '+r[6]])
 for ident,note in [('c:graph-rule','2286 graph pairs in exact rational Frobenius algebras; check_tautological_output.json'),('c:pair-ranks','Exact computed ranks agree with hook-length formulas in tested cases; check_tautological_output.json'),('c:finite-field-lie','E/F5 has exactly 8 points; polynomial T2+2T+5 verified.'),('c:explicit-bad-reduction','Integer polynomial substitutions, discriminants, inverse formulas, Hopf maps all pass; check_explicit_bad_reduction_output.json'),('c:fermat-counterexample','Smoothness derivatives, point substitution, genus3, and odd push coefficient6 pass; nonvanishing remains literature theorem not computational output.')]:w.writerow([ident,'2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','computation or formal certificate',note])
 for ident,note in [('R8','Re-proved product graph rule and M triple-cup criterion; corrected degree4n and refuted M-only generation.'),('R6','Re-read 12:111-120 and 140-142; prompt n-1 overstrengthens manuscript box; subgroup extension distinction verified.'),('Lead C1','Modified diagonal identification proved; all-K3 extension reduces exactly to finite-dimensionality and is unresolved.'),('Lead C3','Proved under arithmetic Serre-quotient hypotheses and in motivated abelian type; geometric centre alone differs.'),('Lead C5','Verified Vasiu-Zink obstruction and supplied explicit p2 abelian-surface realization.')]:w.writerow([ident,'2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','used and rechecked in this run',note])
report={'rows':len(rows),'outputs':['part_c/results.csv','part_c/CHECK_EVENTS.tsv'],'fermat_appended':'c:fermat-counterexample' in p.read_text()}
(ROOT/'code/part_c/update_checkpoint_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
