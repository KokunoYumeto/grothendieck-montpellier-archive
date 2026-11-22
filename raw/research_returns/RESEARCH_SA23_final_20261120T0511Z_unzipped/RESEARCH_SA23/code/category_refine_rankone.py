from pathlib import Path
p=Path('RESEARCH_SA23/sections/category_J.tex');s=p.read_text()
s=s.replace(r'''Take $G=\mathbf G_m$, the trivial $\rho$,
the weight-zero cocharacter $j=0$, and the neutral torsors
$Q_K=P_K=\mathbf G_{m,K}$; here $U''=1$ and $R_K$ is the point.
Then $E=C^\times\rtimes\Gamma$ and the already fixed section is
$\alpha_0(g)=(1,(g,0))$.
For each $a\in\mathbf Q_p^\times$ the section
$(g,n)\mapsto(a^n,(g,n))$ extends this same $\alpha_0$ and retains
all the same $\rho,j,Q,R,P$ data.''',r'''One may take $G=\mathbf G_m$ and trivial $\rho$, as the abstract
section problem permits.  To require also that $G$ be the actual
Tannaka group of a representation, take instead the unramified
character $\rho$ sending arithmetic Frobenius to $1+p$.
Its image is infinite and hence Zariski dense in $\mathbf G_m$.
It is the Tate representation of an etale $p$-divisible group: at
each level descend the constant cyclic group using the unramified
action on $\mathbf Z/p^n\mathbf Z$, and take the compatible system.
Thus it has Hodge--Tate weight zero.
In either version $j=0$, $U''=1$, $R_K$ is the point, and $Q_K=P_K$
is the rank-one Hodge--Tate frame torsor, which is neutral over $K$.
In a $C$-frame with its original descent action,
$E=C^\times\rtimes\Gamma$ and
$\alpha_0(g)=(\rho(g),(g,0))$.
For each $a\in\mathbf Q_p^\times$ the section
$(g,n)\mapsto(a^n\rho(g),(g,n))$ extends this same $\alpha_0$ and
retains all the same $\rho,j,Q,R,P$ data.''')
p.write_text(s);print('Added genuine Tannaka rank-one option')
