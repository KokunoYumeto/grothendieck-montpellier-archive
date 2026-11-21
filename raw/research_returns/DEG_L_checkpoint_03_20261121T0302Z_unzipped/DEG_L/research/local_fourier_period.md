# A local Fourier normalization control

The local shell results LN1–LN6 are incorporated into B14a and B17. The following separate control is included with its original identifier; it concerns a model Fourier functional, not a geometric Weil period.

## LN7. A model period can be small while the integral test vector has bounded norm

Let $\eta|_{\mathcal O^\times}$ be primitive of conductor $m\ge1$, and let $\psi:F\to\mathbb C^\times$ be an additive character trivial on $\mathcal O$ but nontrivial on $\varpi^{-1}\mathcal O$. For the cyclotomic-integral-valued test vector (LN5.1), define the Fourier functional

\[
 \ell_m(\phi)=\int_{F^3}\phi(x)\psi(\varpi^{-m}x_1)\,dx.
\]

Then

\[
 |\ell_m(\phi_\eta)|=q^{-m/2},
 \qquad \|\phi_\eta\|^2=Z_\eta(\phi_\eta,\phi_\eta)=1-q^{-1}.
 \tag{LN7.1}
\]

**Proof.** Set $R=\mathcal O/\varpi^m\mathcal O$ and $\Psi(a)=\psi(\varpi^{-m}a)$, a primitive additive character of $R$. For $a\in R$, put

\[
 S(a)=\sum_{x\in R^\times}\eta(x)^{-1}\Psi(ax).
\]

For a unit $a$, substitution $y=ax$ gives $S(a)=\eta(a)S(1)$. If $m\ge2$, primitiveness provides $h\in1+\varpi^{m-1}\mathcal O$ with $\eta(h)\ne1$. For nonunit $a$, the substitution $x\mapsto hx$ does not change $\Psi(ax)$, so $S(a)=0$. For $m=1$, the only nonunit is zero and the nontrivial character sum is zero. Orthogonality of additive characters on the finite ring gives

\[
 \sum_{a\in R}|S(a)|^2
 =q^m\sum_{x\in R}|\mathbf1_{R^\times}(x)\eta(x)^{-1}|^2
 =q^m|R^\times|.
\]

There are $|R^\times|$ unit arguments, all with magnitude $|S(1)|$, so $|S(1)|^2=q^m$. Haar integration over unit residue classes gives $\ell_m(\phi_\eta)=q^{-m}S(1)$, proving (LN7.1). QED.

This is a model Fourier period, not the selected geometric Weil period. It proves a narrower point: integral values of the Schwartz input and a uniform Rallis norm do not imply a uniform lower bound for a Haar-averaged arithmetic functional. In this example forcing the displayed period to have absolute value one costs $q^{m/2}$ in input norm. No such growth is asserted for the actual construction.

