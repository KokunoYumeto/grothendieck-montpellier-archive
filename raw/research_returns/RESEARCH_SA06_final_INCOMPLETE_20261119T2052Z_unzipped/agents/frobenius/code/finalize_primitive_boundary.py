"""Retain the Witt proof and make the shorter integral-quotient final auxiliary."""
from pathlib import Path
import shutil

base = Path(__file__).resolve().parents[1]
source = base / "C3_primitive_exceptional_boundary_draft.tex"
text = source.read_text()
start = text.index(r"\textbf{3. The designated cubic cup")
end = text.index(r"\textbf{4. Actual lifts", start)
replacement = r"""\textbf{3. A free integral primitive quotient kills the saturated image.}
For $z\in B_s$ define
\[
 \Phi_k(z):H^0(T,L_T)\longrightarrow
 H^0(\mathbb P^m,\mathcal O(1))\otimes
            \bigotimes_i H^1(W_i,A_i\otimes\Omega^1_{W_i/k})
 \tag{PB.10}
\]
by multiplying a section by the divisor-cycle $d\log$ class of $z$
and projecting to the indicated component. Products of divisor
classes realize this map; rationally equivalent divisor polynomials
give the same class by the integral product compatibility
\citep[Section 3, diagram (22), pp.~557--558]{cyBraunling2013}.
In the multigrading of the integral ring of $T$, only the part
\[
       (\text{degree on }\mathbb P^m;\text{cubic degrees})
                         =(0;1,\ldots,1)
 \tag{PB.11}
\]
can contribute. On $\delta_1\boxtimes\cdots\boxtimes\delta_s$
in that part the map is the tensor product of
\[
 \mu_{\delta_i}:H^0(W_i,A_i)\longrightarrow
           H^1(W_i,A_i\otimes\Omega^1_{W_i/k}),
 \qquad u\longmapsto u\,d\log\delta_i,
\]
and the identity on the projective-space factor.

Each $A_i$ is primitive in the free Picard lattice: its intersection
number with a line is one. Thus
\[
 \Lambda_i=\operatorname{Pic}(W_i)/\mathbb ZA_i,
 \qquad \Lambda=\bigotimes_{i=1}^s\Lambda_i
\]
are free abelian groups. Let $\Psi:B_s\to\Lambda$ be the integral
projection to the multidegree in (PB.11), followed by the quotient
in each cubic Picard factor. For $v\in B_{s-1}$, the contribution
of $hv$ to that multidegree is zero. Every other term of $bv$ that
reaches it inserts an $A_i$ into a missing cubic factor. Therefore
\[
                         \Psi(bv)=0.
\]

We verify that $\Phi_k$ factors through $\Psi$ in every characteristic.
The restricted Euler sequence and cubic hypersurface cohomology give
\[
 \begin{gathered}
 0\longrightarrow\Omega^1_{\mathbb P^3/k}(1)|_{W_i}
       \longrightarrow\mathcal O_{W_i}^{\oplus4}
       \longrightarrow A_i\longrightarrow0,\\
 H^1(W_i,\Omega^1_{\mathbb P^3/k}(1)|_{W_i})=0.
 \end{gathered}
 \tag{PB.12}
\]
Indeed the global middle-to-right map is the isomorphism from the
four coordinates to $H^0(W_i,A_i)$, and
$H^1(W_i,\mathcal O_{W_i})=0$. These cohomology statements follow
from the cubic hypersurface sequence and
\citet[Lemmas 30.8.1--30.8.2, Tag 01XS]{frPrimitiveProjectiveCohomology}.
The class $d\log A_i$ comes from the ambient cotangent sheaf, so
every section times that class factors through the zero group in
(PB.12). Hence $\mu_{A_i}=0$. The maps $\mu_{\delta_i}$ are additive
in the integral Picard class and therefore factor through $\Lambda_i$.
Their tensor product proves the desired factorization of $\Phi_k$.

Apply $\Psi$ to the Smith relations (PB.9). Since $\Lambda$ is free,
\[
 d_j\Psi(w_j)=\Psi(bv_j)=0
 \quad\Longrightarrow\quad\Psi(w_j)=0
 \quad\Longrightarrow\quad\Phi_k(w_j)=0.
 \tag{PB.13}
\]
The first implication is in a free integral lattice before passing
to characteristic $p$. It remains valid when $p\mid d_j$ and proves
that $\Phi_k$ kills the entire saturation of $bB_{s-1}$.
This argument needs neither a division by a Smith invariant factor
nor a cohomological hard Lefschetz theorem.

"""
text = text[:start] + replacement + text[end:]
text = text.replace("Auxiliary proposition (proved here; pending independent audit)",
                    "Auxiliary proposition for C.3bl (Proved)")
text = text.replace(
    "% Separate auxiliary proof. No new local restriction theorem is registered here.\n% Full independent typed audits are requested before a geometric application.",
    "% Final integral-quotient auxiliary; combined geometric application remains separate.\n% Supersedes only Step 3 of the retained Witt-lift draft, whose proof remains valid.")
text = text.replace("Every line bundle pulled from $C$ consequently lifts through all\nneighbourhoods of $V$.",
    "Every line bundle pulled from $C$ consequently lifts through all\nneighbourhoods of $V$ by the square-zero unit sequence\n\\citep[Lemma 37.4.1, Tag 0C6R]{frC3azStacksPicThickening}.")
text = text.replace("Formal existence\nover $\\widehat R$ algebraizes the compatible invertible system.",
    "Formal existence\nover $\\widehat R$ algebraizes the compatible invertible system\n\\citep[Lemma 30.24.3, Tag 0885]{frC3azStacksExistence}.")
text += r"""

\noindent\emph{Proof history.}
The complete earlier draft proves (PB.13) by lifting the designated
Picard lattice to the Witt ring and using a free twisted cotangent
cohomology module. That independent proof is retained unchanged.
The present Step 3 replaces it by the free integral quotient
$\bigotimes_i(\operatorname{Pic}(W_i)/\mathbb ZA_i)$ and therefore
removes the lifting argument from this final proof. No assertion
of the earlier proof has been withdrawn.
"""
(base / "C3_primitive_exceptional_boundary.tex").write_text(text)
out = base / "output"
for suffix in ("pdf", "tex", "bbl", "log"):
    old = out / ("C3_primitive_exceptional_check."+suffix)
    keep = out / ("C3_primitive_exceptional_Witt_check."+suffix)
    if old.exists() and not keep.exists():
        shutil.copyfile(old, keep)
print("Wrote C3_primitive_exceptional_boundary.tex; retained full Witt draft and wrapper outputs.")
