# ANABELIAN_A1

Sorted 20 Nov 2026 by Claude Opus 5.5 at effort medium (sorting only; no proof judged). The run: GPT-6 Astra (ChatGPT Pro mode). Field: Longue Marche and anabelian.

## The paper's abstract

This manuscript gives an independently audited proof of universal injectivity of point sections for proper hyperbolic curves over finite fields, using the whole arithmetic Galois quotient. Every assertion is assigned an explicit status. The manuscript also records the separate existence, completion, reconstruction, and characteristic-zero questions requested with the proof audit. No priority is claimed.

## What the run set out to do

In its report's words (`ANABELIAN_A1/ANABELIAN_A1_report.md`, opening): the report opens only with 'INCOMPLETE'; the abstract above and the main results below say what it did

## Register at this return

- Return sorted: **cp03**, `longue_marche_pro_pilot_20261104/answers/ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped`.
- Register: `ANABELIAN_A1/ANABELIAN_A1_results.csv`, 121 rows.
- Kinds: proposition 99, refuted 8, open question 7, reduction 5, computation 1, other 1 (kind from the register's type column, the id prefix or a keyword; 'proposition' is the default where the register gives no type).
- Run status (first word): proved 105, refuted 8, open 7, known 1.
- CHECK_EVENTS: none in this return (older prompt).
- Papers: `ANABELIAN_A1/ANABELIAN_A1_paper.tex`
- Bridge flags (RH, Weil, weights, motives): 24 (see `BRIDGE_FLAGS.tsv`).

## Earlier intake

Newest intake or expert note named by the ledger: `pro_intake_20261117/EXPERT_A1_SECOND_READING_PART2_20261117.md` (read up to cp03). Of 121 rows, 108 have their id somewhere in the 8 intake documents that mention this run (an id string match, so short ids such as A.1 overstate it); the other 13 are marked 'no intake' in the reading plan.

## Main results (named in the report's main/conclusion sections or the paper's abstract; most used first)

- `A.1` (proposition; Proved; used by 10): Let $C/k$ be a smooth proper geometrically connected curve of genus at least two over a finite field of characteristic $p$. The map \[ C(k)\longrightarrow \{s:G_k\to\Pi_C\mid \oper
- `B.8` (proposition; Proved; used by 6): For an $F$-stable open normal $H\triangleleft\Delta$, let $S_H$ be the finite set of $a\in J_{D_H}(k)[p^\infty]$ such that, for every normal $K\triangleleft\Delta$ containing $H$, 
- `B.4` (proposition; Proved; used by 5): Fix $(C,P)/\mathbf F_q$ and an odd prime $\ell\ne p$. There is a finite procedure deciding whether B1 has an order-$\ell$ witness over \emph{any} constant extension. For each geome
- `A.23` (proposition; Proved; used by 4): Assume the cuspidal transport construction from equal point sections has been established for a prime set $\Sigma$ containing some $r\ne p$, allowing $p\in\Sigma$. Then $E_C^\Sigma
- `B.49` (refuted; Refuted; used by 4): For every field \(K\) admitting a nontrivial henselian discrete valuation with residue characteristic zero, closed-point-preserving reconstruction of finite-type \(K\)-schemes from
- `B.2` (proposition; Proved; used by 3): Let $a:J_C(L)\twoheadrightarrow A$ be a nontrivial finite abelian quotient of order prime to $p$, and use the Abel map based at $P$ to pull back its constant Lang quotient. Put \[ 
- `B.9` (proposition; Proved; used by 3): Suppose there are a finite extension $L/k$ and compatible pointed étale prime-to-$p$ covers $Z\to Y\to C_L$, both geometrically normal over $C$, such that $Z\to Y$ is nontrivial Ga
- `B.57` (proposition; Proved; used by 3): Let \[ N=\bigcap_{c\geq1}\gamma_{c+1}(I),\qquad K_{p,\mathrm{nil}}=\overline\Q^N =\bigcup_{c\geq1}\overline\Q^{\gamma_{c+1}(I)}. \tag{B.MIX.4} \] For every \(p\geq5\) and every fin
- `A.26` (proposition; Proved; used by 2): For every proper hyperbolic curve $C/k$ over a finite field and every prime $r$, including $r=\operatorname{char}k$, the exceptional image $E_C^{\{r\}}$ is infinite. Here the full 
- `B.28` (proposition; Proved; used by 2): Let $C/K$ be smooth proper of genus $g\ge2$ over a finite field of characteristic $p$. Let $D\to C$ be a geometrically connected \emph{\'etale} cover with constant cyclic deck grou
- `B.35` (proposition; Proved; used by 2): Let $E/\overline{\F}_p$ be an elliptic curve, let $\pi:E\to E/\{\pm1\}\simeq\mathbf P^1$ be its quotient map, and let $S\subset\mathbf P^1(\overline{\F}_p)$ be finite. There exists
- `B.54` (proposition; Proved; used by 2): Let $R$ be a henselian rank-one valuation ring with fraction field $K$ and residue field $\kappa$ of characteristic zero. Let $S\subset\mathbb P^1(K)$ be a finite set containing $0
- ... and 17 more (column `main_in_report` of the TSV).

## Rows the programme rests on (used by three or more rows)

- `A.1` (used by 10; Proved): Let $C/k$ be a smooth proper geometrically connected curve of genus at least two over a finite field of characteristic $p$. The map \[ C(k)\
- `A.4` (used by 7; Proved): Let $C$ be smooth proper geometrically connected of genus at least two over an algebraically closed field of characteristic $p$, and let $\S
- `B.8` (used by 6; Proved): For an $F$-stable open normal $H\triangleleft\Delta$, let $S_H$ be the finite set of $a\in J_{D_H}(k)[p^\infty]$ such that, for every normal
- `A.17` (used by 5; Proved): Let $C/L$ be smooth proper geometrically connected of genus at least two over a finite field, and let $\Sigma$ contain a prime $r\ne\operato
- `B.4` (used by 5; Proved): Fix $(C,P)/\mathbf F_q$ and an odd prime $\ell\ne p$. There is a finite procedure deciding whether B1 has an order-$\ell$ witness over \emph
- `A.2` (used by 4; Proved): Let $1\to L\to H\to B_0\to1$ be an exact sequence of discrete groups, where $L$ is free of finite rank at least two. If conjugation by $H$ a
- `A.3` (used by 4; Proved): Set $F=\Lambda^\Sigma$, $E=\Gamma^\Sigma$, and \[ \begin{split} K_F&=\ker(F\to\Delta),\qquad K_E=\ker(E\to\Delta\times\Delta),\\ F_{\crr}&=F
- `A.13` (used by 4; Proved): Let \(C\) be a smooth proper geometrically connected curve of genus at least two over an algebraically closed field of characteristic \(p>0\
- `A.14` (used by 4; Proved): Let $F$ be profinite, $K\triangleleft F$ closed, $r$ prime, and $N=\ker(K\to K^{(r)})$. For every open $I\le F$ containing $N$, the continuo
- `A.15` (used by 4; Proved): Let $C/k$ be smooth proper geometrically connected of genus at least two, $k$ finite of characteristic $p$, $P\in C(k)$, and $r\ne p$. Every

## Open items (7 open or conjectural rows; 8 refuted)

- `A.28`, `B.5`, `B.12`, `B.24`, `B.32`, `B.52`, `B.67`

## Where everything is

- Sorted rows: `SORTED/ANABELIAN_A1.tsv` (proof_at = file:line of the statement in this return, then the register's own locator).
- Run folder: `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped`.
- Report: `ANABELIAN_A1/ANABELIAN_A1_report.md`; main-result sections: ANABELIAN_A1_report.md lines 41-46, 113-130.
