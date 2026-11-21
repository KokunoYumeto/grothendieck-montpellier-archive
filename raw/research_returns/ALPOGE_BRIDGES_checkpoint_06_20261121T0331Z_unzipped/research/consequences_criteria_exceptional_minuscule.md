# CC-APG09–11: short extremal-weight orbits obstruct opposition in types $E_6,E_7$

All groups in this section are over $\mathbf C$. An ordered pair $(T_0,T_1)$ is in principal apposition in the sense fixed in CC-APG01: a principal element $c\in T_0$ of order the Coxeter number $h$ normalizes $T_1$ and acts on it as a Coxeter element. The group $G$ is adjoint. Representations below are taken on its simply connected cover $\widetilde G$; highest lines and Borel subgroups descend through the central isogeny. No assertion that the representations descend linearly to $G$ is used.

## CC-APG09: the short-orbit criterion

#### Statement.

Choose a positive system for $T_0$ in which $$c=\rho^\vee(\zeta),\qquad \zeta=e^{2\pi i/h};
        \qquad \alpha_j(c)=\zeta\quad\hbox{for every simple root}.$$ Let $V=L(\lambda)$ be the irreducible representation of $\widetilde G$ with a fundamental highest weight $\lambda=\omega_i$. Transport the root labels to $T_1$ by an inner conjugacy. Suppose the Coxeter action $C$ on the extremal weight orbit $W\lambda$ has an element $\mu$ with $$C^d\mu=\mu,\qquad 0<d<h.$$ Then some $B_0\supset T_0$ and $B_1\supset T_1$ are not opposite. The hypothesis concerns only the extremal orbit; it makes no assumption about other weights or the dimension of $V$.

#### Proof.

Existence of $V$, uniqueness of its highest line, and Weyl invariance of weight multiplicities are the standard highest-weight theorems: Milne (2017), Lemma 22.15, pp. 466–467, Proposition 22.17, p. 467, and Theorems 22.18–22.20, pp. 467–468. In particular, every extremal weight space $V_\nu$, $\nu\in W\lambda$, is one-dimensional and is the highest line for a Borel containing the corresponding torus.

Choose any lift $\widetilde c$ of $c$ to $\widetilde T_0$. It normalizes $\widetilde T_1$. The line $V_\mu$ for $T_1$ is preserved by $\widetilde c^d$, because $C^d\mu=\mu$. Thus there is $b\in\mathbf C^\times$ such that $\widetilde c^d u=bu$ for $0\ne u\in V_\mu$. Choose $B_1\supset T_1$ for which this is the highest line.

For $T_0$, the two extremal weights $$\nu_0=\lambda,\qquad
               \nu_1=s_i\lambda=\lambda-\alpha_i$$ give eigenvalues of $\widetilde c^d$ whose ratio is $\alpha_i(c)^d=\zeta^d\ne1$. Hence at least one of them, say $\nu$, has eigenvalue $a=\nu(\widetilde c^d)\ne b$. Let $f$ be a nonzero element of the one-dimensional dual weight space $V^*_{-\nu}$. Equivalently, $f$ is supported on $V_\nu$ and annihilates all other $T_0$-weight spaces. Consequently $$f(\widetilde c^d u)=a f(u)=b f(u),
                  \qquad\hbox{so}\qquad f(u)=0.$$ The weights $-W\lambda$ form the extremal orbit of $V^*$. Therefore the line of $f$ is the highest line of $V^*$ for some $B_0\supset T_0$.

If $B_0,B_1$ were opposite, their highest lines in $V^*,V$ would have nonzero natural evaluation. Indeed, conjugate the pair to a standard pair $B_+,B_-$. If the highest weight of $V$ for $B_+$ is $\eta$, its highest line for $B_-$ is $V_{w_0\eta}$, and the highest line of $V^*$ for $B_+$ is $V^*_{-w_0\eta}$. These one-dimensional dual spaces pair nondegenerately. This contradicts $f(u)=0$. Thus $B_0,B_1$ are not opposite. $\square$

#### Construction with the specified coordinates.

For each application, start with $T_1$ and its explicitly labeled base, and choose a representative $c\in N_G(T_1)$ of the specified product $C=s_1\cdots s_r$. The converse principal-class statement in Kostant (2010), p. 7, says that this representative is regular of order $h$ and belongs to the principal conjugacy class. Put $T_0=Z_G(c)^\circ$, and choose a positive base for $T_0$ in which all simple roots take the value $\zeta$ on $c$. Choose the representation with the indicated fundamental highest weight for the original based torus $T_1$. Inner conjugacy of based torus pairs transports this to a fundamental highest weight for the chosen based torus $T_0$; its index there is immaterial to CC-APG09. Thus the displayed Coxeter word and the principal coordinates refer to the same representation and apposition pair. No conjugacy theorem for Coxeter elements is needed in this construction. A change of lift of $c$ only multiplies all relevant eigenvalues by a common central scalar. Finally CC-APG01 transfers the resulting counterexample to every ordered apposition pair.

## Exact finite certificates

Use fundamental-weight coordinates $$v=(\langle v,\alpha_1^\vee\rangle,\ldots,
                          \langle v,\alpha_r^\vee\rangle).$$ The simply laced Cartan matrix has diagonal entries $2$, entry $-1$ on the edges $$(1,3),(2,4),(3,4),(4,5),(5,6),
          \quad\hbox{and additionally }(6,7)\hbox{ for }E_7,$$ and zero elsewhere. This specifies the numbering completely; it agrees with Milne (2017), Theorem C.56 and the following Dynkin diagrams, pp. 625–626. For this symmetric matrix $A$, reflections are $$s_j(v)_k=v_k-v_j A_{jk}.                 \tag{E.1}$$ Throughout $C=s_1\cdots s_r$, so $s_r$ is applied first. Listed reflection words are instead explicitly in application order. Each equality below can therefore be checked by integer substitution into (E.1), without a representation matrix.

## CC-APG10: $E_6$

Take $\lambda=\omega_1=(1,0,0,0,0,0)$ and $h=12$. The reflection word in application order $$1,3,4,2,5,4$$ sends $\lambda$ to $\mu=(0,0,1,-1,0,1)$. The complete short cycle is $$\begin{split}
 (0,0,1,-1,0,1)
     &\xmapsto{C}(-1,0,0,1,-1,0)\\
     &\xmapsto{C}(1,0,-1,0,1,-1)
       \xmapsto{C}(0,0,1,-1,0,1).
\end{split}                                                   \tag{E.2}$$ Thus $\mu\in W\lambda$ and $C^3\mu=\mu$, with $0<3<12$. CC-APG09 gives a nonopposite containing Borel pair. The single ordered-apposition-pair orbit proved in CC-APG01 transfers this conclusion to every pair in apposition in type $E_6$. In particular, the answer to the original *all choices* question is negative. $\square$

## CC-APG11: $E_7$

Take $\lambda=\omega_7=(0,0,0,0,0,0,1)$ and $h=18$. The reflection word in application order $$7,6,5,4,2,3,1,4,3,5,4,6$$ sends $\lambda$ to $\mu=(0,1,0,-1,1,-1,1)$. The short cycle is $$(0,1,0,-1,1,-1,1)
     \xmapsto{C}(0,-1,0,1,-1,1,-1)
     \xmapsto{C}(0,1,0,-1,1,-1,1).                         \tag{E.3}$$ Thus $C^2\mu=\mu$, with $0<2<18$. CC-APG09 again gives a nonopposite containing Borel pair, and CC-APG01 transfers it to every apposition pair. The original *all choices* question is negative in type $E_7$. $\square$

#### Scope of the computation.

The script `research/cc_minuscule_orbits.py` uses only the integer reflection formula (E.1). It checks the full Coxeter matrix orders $12,18$ on a basis, and independently enumerates the extremal Weyl orbits and obtains cycle lengths $$E_6:\ 3+12+12,\qquad
                  E_7:\ 2+18+18+18.$$ The proofs above need only the displayed words and short cycles. They do not use the full enumerations, the names or dimensions of minuscule representations, a numerical approximation, or a claim that the computational output is a literature theorem. The usual root-system Coxeter numbers are also directly compatible with the highest-root coefficient lists $(1,2,2,3,2,1)$ and $(2,2,3,4,3,2,1)$, respectively: their sums are $11$ and $17$.

#### Primary inputs and bibliography.

The apposition and principal-element inputs are Kostant (2010), Proposition 1.1, p. 5; Theorems 1.2–1.4, p. 6; the principal order-$h$ paragraph and Theorem 1.7, p. 7; and Proposition 1.8 and Theorem 1.9, p. 8. The representation-theoretic inputs are the numbered Milne statements cited above; the exceptional root systems are described in his §24(l), pp. 541–542, and the labeled Dynkin diagrams in Theorem C.56 and the following figure, pp. 625–626. These are retained as known inputs, not re-proved literature claims.

Kostant, B. (2010). Experimental evidence for the occurrence of $E_8$ in nature and the radii of the Gosset circles. *Selecta Mathematica, 16*, 419–438. <https://doi.org/10.1007/s00029-010-0023-1>. Author version: <https://arxiv.org/abs/1003.0046v1>.

Milne, J. S. (2017). *Algebraic groups: The theory of group schemes of finite type over a field*. Cambridge University Press. Author PDF: <https://www.jmilne.org/math/Books/iAG2017.pdf>.
