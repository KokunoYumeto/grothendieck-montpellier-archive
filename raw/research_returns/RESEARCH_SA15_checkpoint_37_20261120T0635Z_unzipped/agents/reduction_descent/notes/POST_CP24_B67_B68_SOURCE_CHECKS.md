# B67/B68 source and proof checks

Recorded 2026-11-19, approximately 20:59 UTC. Both results remain candidates
until complete root and companion audits; the finite programs do not prove
the all-prime statements by enumeration.

## Fresh original-source reads in this segment

- **Serre (1961), §3.1, Propositions 1–4, printed pp.126–128.** Read the
  retained original text at sources/serre1961_algebraically_closed.txt,
  including its explicit removal of the algebraically-closed-residue
  restriction in the totally ramified case, the lower filtration,
  Herbrand functions, and Proposition 3's upper quotient formula.
  The original statement refers to Herbrand/Artin for the proof; it is
  not represented here as containing that full proof.
  Original URL: https://www.numdam.org/item/10.24033/bsmf.1562.pdf
- **Colmez, Corps locaux, Propositions 3.7 and 3.13 and Theorem 3.10,
  complete proofs, pp.14–16.** Read the retained original text
  sources/colmez_corps_locaux.txt, including the two norm-polynomial
  divisibilities, the minimum formula, the Herbrand change of variables,
  and the upper quotient conclusion. The argument is applied to the
  totally ramified complete discrete valuation fields already covered
  by Serre's original statement.
  Original URL: https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf
- **Stacks Project, Theorem 10.160.8, Tag 032A, complete proof.**
  Freshly opened and read the original at
  https://stacks.math.columbia.edu/tag/032A .
  Retrieval reference turn493876102view0. The mixed-characteristic
  coefficient-ring construction is used only to choose residue
  representatives fixed by the actual Galois group. No canonical
  Witt embedding is assumed.
- **Tate (1967), Theorem 4, Corollaries 1–2, and Proposition 12,
  complete proofs, pp.181–183.** Freshly opened the original
  https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf
  at turn747083085view0; exact full theorem/proof passage read
  at turn868902042view0 and turn868902042view1.
  This supplies extension of the actual semilinear descent maps
  and inverses; the closure/stabilization proof was read as well.

## Proof dependencies reread

The full current B53 and B55–B59 arguments were reread before writing B67.
The new text explicitly derives
\(A=e p^{r-2}\), \(b_0=(p^2-1)e\), and
\(e_F=(p^2-1)p^2A\), and replaces the old leading coefficient
\(p-1\) by the nonzero residue of \(e\). It does not invoke an
unproved invariance under rescaling. The full-wild argument keeps
the general additive polynomial \(X^{p^2}+sX^p+tX\), with \(t\ne0\).

B68 reuses the already proved universal Newton bounds in B49, the
fixed-coefficient point-field argument of B60/B61, the actual-target
Cartier bound of B64, and the exact lower examples of B63.
The high and low quotient maps, multiplicities, inherited tangent
action, and exact \(p^3\)-to-\(p^2\) quotient are rederived in its
own text. The original Hopkins–Gross and published Bondarko sources
were previously audited; no new fresh read of those whole original
papers is claimed in this segment.

## Exact finite supplements

- code/verify_irreducible_arbitrary_index.py: PASS at
  20:57:06.817466 UTC, author runtime 2.847146783999051 seconds.
  Covers 150 varying prime-to-\(p\) ramification indices and the
  exact coefficient, ramification, and additive-plane checks stated
  in its output. No formal group or extension is instantiated.
- code/verify_initial_tame_sector.py: PASS at
  20:57:28.665501 UTC, author runtime 2.3066381700045895 seconds.
  Covers all 60 stated \(t\)-sectors at six primes, with independently
  computed Newton polygons and quotient root counts.

Both exact sources, outputs, pre-certificate proof versions and
candidate SHA records are retained. No failed numerical execution
occurred in these two supplements. Two exploratory local file
lookups used incorrect filenames and returned file-not-found;
the actual files were then located with rg --files and read.
No inference was made from those failed lookups.
The first attempt to write this source-log note failed during JavaScript
parsing because Markdown backticks were unescaped; no command or
filesystem mutation executed in that failed call. The parse error was
"SyntaxError: missing ) after argument list"; this corrected note
records that nonmathematical tool failure explicitly.
