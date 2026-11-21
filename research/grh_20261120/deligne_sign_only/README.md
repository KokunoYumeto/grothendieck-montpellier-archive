# A sign-only proof of Deligne's purity theorem (Alpöge's footnote 3, worked out)

**Status (21 Nov 2026):** AI-produced and unrefereed. No human has checked it. Please check it, and tell us if this
route is already known.
- It has had two independent AI checks, and both found no gap.
- A first literature search found no proof along this route.
- The write-up for Hexagon is `deligne_sign_only.pdf`, with its TeX beside it. It is a draft, not yet deposited.

**Who did what:**
- The proof is Part I of `HODGE_SIGN.pdf`, from a research run of GPT-6 Astra (ChatGPT Pro mode) on 21 Nov 2026,
  00:14-00:56 UTC (our prompt 32, HODGE_SIGN).
- First check: Claude Opus 5.5 at effort high, a targeted proof check of every step (`INTAKE_HODGE_SIGN_20261121.md`).
- Second check: Claude Fable 5.2 at effort max. It was not shown the first check, and it re-proved every step
  (`CHECK_a3ccbc11_20261121.md`). It made one correction: the weak-Lefschetz input should come from Katz's Appendix A.5
  (Deligne's proof, weight-free), applied to the graph of the path form, and not from the printed proof of his
  Corollary 3.4.1, which runs through the Fourier transform. The write-up adopts this.
- This page: Claude (Claude Opus 5.5 at effort max). No human wrote or checked any of it.
- The idea is L. Alpöge's: footnote 3 of his note on RH, https://alpo.ge/remark.pdf (20 Nov 2026).

## What is proved

**Theorem** (Deligne: Weil I, Théorème 1.6; Weil II, Théorème 3.3.1 over a point). Let $X/\mathbf F_q$ be separated of
finite type, and let $\mathcal F$ be a constructible $\overline{\mathbf Q}_\ell$-sheaf whose local Frobenius eigenvalues
at each closed point $x$ have absolute value at most $|\kappa(x)|^{w/2}$. Then every Frobenius eigenvalue on
$H^i_c(X,\mathcal F)$ has absolute value at most $q^{(w+i)/2}$. If $X$ is smooth and proper, and $\mathcal F$ is lisse
and pointwise pure of weight $w$, then $H^i(X,\mathcal F)$ is pure of weight $w+i$.

These are Deligne's theorems of 1974 and 1980. What would be new is the proof. It uses:
- the trace formula, Künneth, affine Artin vanishing and Poincaré duality;
- Katz's generic weak Lefschetz theorem (whose proof uses generic base change and Artin vanishing, and no weights);
- Noether normalization;
- Parseval for a bilinear character sum;
- tensor powers.

It uses no monodromy, no Lefschetz pencils, no Rankin-Selberg squaring and no theory of weights.

## Why this is not a consequence of GRH

There are two Riemann hypotheses here.
- **Over $\mathbf Q$ and number fields**: the zeros of $\zeta$ and of Dirichlet and Hecke L-functions. Alpöge's note
  (20 Nov 2026) proves RH and GRH for Dirichlet L-functions, with a Lean formalization.
- **Over finite fields**: the absolute values of Frobenius on étale cohomology. Weil proved it for curves, and Deligne
  in general.

Neither implies the other. Alpöge remarks that his sign mechanism also works over finite fields. Carried out, it gives
a short new proof of the finite-field theorem. That also tests his method in a case where the answer is known.

## The proof in five steps

1. **Effective power sums** (HS-01). Let $\lambda_j$ be distinct and nonzero, and $c_j$ positive integers. If
   $|\sum_j c_j\lambda_j^n| \le C e^{o(n)}B^n$ for all $n$, then every $|\lambda_j|\le B$. Each $\lambda_j$ gives a pole
   of the generating function at $1/\lambda_j$, and positive multiplicities cannot cancel.

2. **The remainder is effective** (SG-08). Let $U$ be smooth affine of dimension $d$, $\mathcal F$ lisse,
   $X=U^k$ ($D=kd$), and $\mathcal F_k=\mathcal F^{\boxtimes k}$. Let $Y\subset X$ be a smooth affine hypersurface such
   that $H^a(X,\mathcal F_k^\vee)\to H^a(Y,\mathcal F_k^\vee)$ is an isomorphism for $a<D-1$ and injective for
   $a=D-1$. Write $M_n$ for the trace sum of $\mathcal F$ over $U(\mathbf F_{q^n})$, $N_n$ for that of $\mathcal F_k$
   over $Y(\mathbf F_{q^n})$, and $R_n=q^nN_n-M_n^k$. Then

   $$(-1)^{D-1}R_n=\operatorname{Tr}\bigl(F^n,\,H^d_c(U,\mathcal F)^{\otimes k}\bigr)+\operatorname{Tr}(F^n,K_k),\qquad K_k=\ker\bigl(H^{D-1}_c(Y)(-1)\to H^{D+1}_c(X)\bigr).$$

   $K_k$ is an actual module, so the right side is an effective power sum. The proof:
   - Artin vanishing and duality kill the low degrees.
   - The Gysin isomorphisms cancel all higher degrees in pairs.
   - Surjectivity at the border leaves the kernel.
   - Künneth gives $H^D_c(X)=H^d_c(U)^{\otimes k}$.

3. **The choice of $Y$** (SG-09). Take a finite Noether normalization $\pi:U\to\mathbf A^d$; its fibres have at most
   $B$ points. Take coordinates $z$ embedding $U$, and a nondegenerate bilinear form $b$ on $\mathbf A^d$. Let $Y$ be
   $$f+\textstyle\sum_i g_i+c=0,\qquad f(u_1,\dots,u_k)=\sum_{i<k}b(\pi u_i,\pi u_{i+1}),$$
   with $g_i$ generic linear combinations of the coordinates of $u_i$. Katz's Corollary 3.4.1 (generic weak Lefschetz,
   with $f$ fixed) gives the restriction property of step 2 for generic coefficients, and Bertini gives smoothness.

4. **Parseval** (HS-03). Group the points by $x_i=\pi u_i\in\mathbf F_Q^d$. Then $R$ is a sum over $h\ne0$ of path sums
   $\sum_x\prod_i t_i(x_i)\,\psi\bigl(h\sum_i b(x_i,x_{i+1})\bigr)$, with weights $|t_i|\le BCQ^{w/2}$. The matrices
   $\psi(h\,b(x,y))$ are $Q^{d/2}$ times unitary, so
   $$|R|\le (BC)^k\,Q^{k(w+d)/2+d/2+1}.$$
   This is square-root size for $U^k$, up to a factor $Q^{d/2+1}$ that does not grow with $k$.

5. **Tensor powers** (HS-02, SG-09-SG-11).
   - Steps 1, 2 and 4 give $|\alpha|^k\le q^{k(w+d)/2+d/2+1}$ for every eigenvalue $\alpha$ on $H^d_c(U,\mathcal F)$.
     Take $k$th roots and let $k\to\infty$: $|\alpha|\le q^{(w+d)/2}$.
   - Higher degrees follow from generic hyperplane sections and induction on the dimension, and a general $X$ by
     stratification (SG-11).
   - Purity for smooth proper $X$ follows by Poincaré duality (SG-10).

## Where to look hardest
- Katz, ACT, Appendix A.3-A.5 (and Corollary 3.4.1). Check that A.5, applied to the graph of the path form, gives the
  restriction property used in step 2, and that its proof uses no purity.
- The remainder identity of step 2.
- The Parseval bound when the weights depend on $h$ and $i$.

## Files
- `HODGE_SIGN.pdf` and `HODGE_SIGN.tex`: the run's paper. Section 1 of Part I is this proof; the rest of the paper is
  about Grothendieck's cotes 16, 34 and 44.
- `CHECK_EVENTS.tsv`, `LEDGER.md`, `VERIFICATION.md`: the run's own records.
- `INTAKE_HODGE_SIGN_20261121.md` and `INTAKE_HODGE_SIGN_20261121_CHECK_EVENTS.tsv`: our check.
- The whole raw return, with the prompt as sent:
  [`raw/research_returns/HODGE_SIGN_final_20261121T0057Z_unzipped/`](../../../raw/research_returns/HODGE_SIGN_final_20261121T0057Z_unzipped/).

## References
- P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974); *II*, Publ. Math. IHÉS 52 (1980).
- N. Katz, *Affine cohomological transforms, perversity, and monodromy*, J. Amer. Math. Soc. 6 (1993), Cor. 3.4.1 and
  App. A.5.
- SGA 4, XIV, Théorème 3.1 (affine vanishing); SGA 4½, *Théorèmes de finitude* (generic base change).
- L. Alpöge, note on RH, https://alpo.ge/remark.pdf, footnote 3.

Corrections are welcome as a GitHub issue. This page and the run's text are AI-written and dedicated to the public
domain under CC0 1.0.
