"""Build h07_note_v3.tex from h07_note_v2.tex: new front (title to the proof overview), the body of v2 with the
editor's repairs (each an exact replacement that must match once), and a new end (proof of the corollary, what
remains open, note on method, bibliography). v1 and v2 are not touched.
Claude Fable 5.2 at effort max (agent a2fedc2a31aa5abb9), 23 Nov 2026.
usage: python -I -B make_v3.py"""
import sys
from pathlib import Path

D = Path("<local>/Documents/reports_20261123/h07_note")
P = D / "_v3_parts"
v2 = (D / "h07_note_v2.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
front = (P / "front_v3.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
tail = (P / "tail_v3.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

a = v2.index("\\title[")
b = v2.index("\\section{The finite-field case}")
c = v2.index("\\section{What remains open}")
head, body = v2[:a], v2[b:c]


def rep(text, old, new, n=1):
    k = text.count(old)
    if k != n:
        sys.exit("replacement matched %d times, expected %d: %s" % (k, n, old[:70]))
    return text.replace(old, new)


head = rep(head, "\\newtheorem{thm}{Theorem}[section]",
           "\\newtheorem{maincor}[theorem]{Corollary}\n\\newtheorem{thm}{Theorem}[section]")

R = [
    # the pro-r kernel: G in place of K (K is the base field elsewhere)
    ("For a profinite group $K$ let $N(K)$ be the intersection of the open normal subgroups of $K$ of $r$-power index, so that $K^{(r)}=K/N(K)$; $N(K)$ is characteristic in $K$.",
     "For a profinite group $G$ let $N(G)$ be the intersection of the open normal subgroups of $G$ of $r$-power index, so that $G^{(r)}=G/N(G)$ is the maximal pro-$r$ quotient of $G$; the subgroup $N(G)$ is characteristic in $G$."),
    # Lemma on free groups: W in place of Q (Q is a point), and the count of lifts
    ("For a finite $r$-group $Q$ with Frattini subgroup $\\Phi(Q)$, the kernel of $\\Aut(Q)\\to\\Aut(Q/\\Phi(Q))$ is an $r$-group: by Burnside's basis theorem it acts freely on the $|\\Phi(Q)|^d$ tuples lifting a fixed basis of $Q/\\Phi(Q)$. For $Q=L^{(r)}/U$, the group $Q/\\Phi(Q)$ is a quotient of $L/[L,L]L^r$, on which $H$ acts through an $r$-group; so $H$ acts on each $Q$ through an $r$-group, and",
     "For a finite $r$-group $W$ with Frattini subgroup $\\Phi(W)$, the kernel of $\\Aut(W)\\to\\Aut(W/\\Phi(W))$ is an $r$-group: by Burnside's basis theorem it acts freely on the set of tuples lifting a fixed basis of $W/\\Phi(W)$, and the cardinality of this set is a power of $r$. For $W=L^{(r)}/U$, the group $W/\\Phi(W)$ is a quotient of $L/[L,L]L^r$, on which $H$ acts through an $r$-group; so $H$ acts on each $W$ through an $r$-group, and"),
    # the decomposition group of the diagonal, defined
    ("Let $\\mathcal D\\subset\\mathcal G$ be a decomposition group of the diagonal.",
     "Let $\\mathcal D\\subset\\mathcal G$ be a decomposition group of the diagonal: the stabilizer in $\\mathcal G$ of a point above the generic point of the diagonal in the normalization of $C\\times C$ in the pro-cover defined by $\\mathcal G$."),
    # Lemma on r-quotients: stated for K_F, with its conclusion
    ("Let $K\\triangleleft F$ be closed and $N=N(K)$. Every open subgroup",
     "Let $N=N(K_F)$. Every open subgroup"),
    ("Let $I/J$ be a finite $r$-quotient, $I_0$ the core of $I$ in $F$, and $M$ the core of $J\\cap I_0$ in $F$.",
     "Let $I/J$ be a finite $r$-quotient, $I_0$ the intersection of the conjugates of $I$ in $F$, and $M$ the intersection of the conjugates of $J\\cap I_0$ in $F$."),
    ("and the image of $K$ in $F/I_0$ is an $r$-group because $N\\subseteq I_0$; so the image of $K$ in $F/M$ is an $r$-group, hence $N\\subseteq M\\subseteq J$.",
     "and the image of $K_F$ in $F/I_0$ is an $r$-group because $N\\subseteq I_0$; so the image of $K_F$ in $F/M$ is an $r$-group, hence $N\\subseteq M\\subseteq J$. As $J$ was arbitrary, $N\\subseteq N(I)$, which is the assertion."),
    # Step 4: the exceptional set, named apart from the group E_c
    ("By Sa\\\"idi and Tamagawa there is a finite set $E_C$ of closed points of $C$, for the cofinite set of primes different from $p$, outside which the decomposition group in $\\Pi_C$, even up to commensurability, determines the point \\cite[Definitions 1.3, 1.5, 1.10, Proposition 1.8(vi)]{ST09}; it serves for every constant extension \\cite[Remark 1.2]{ST09}. Hence $T=R$ whenever $R\\notin E_C\\cup\\{P,Q\\}$.",
     "By Sa\\\"idi and Tamagawa there is a finite set $\\mathcal E_C$ of closed points of $C$, their exceptional set for the set of all primes different from $p$, with this property: a closed point of the pro-cover of $C$ which does not lie above $\\mathcal E_C$ is determined by its decomposition group in $\\Pi_C$, even up to commensurability \\cite[Definitions 1.3, 1.5, 1.10, Proposition 1.8(vi)]{ST09}. The set is the same for every constant extension \\cite[Remark 1.2]{ST09}. Hence $T=R$ whenever $R$ does not lie above $\\mathcal E_C$."),
    # Step 4: the groups over L named; the last sentence says what is used
    ("Let $L/k$ be finite, $R\\in(C-P)(L)$, $D_R\\subset (G_P)_L$ a decomposition group, and $S=\\beta(D_R)$.",
     "Let $L/k$ be finite, and write $(G_P)_L$ and $(G_Q)_L$ for the inverse images of $G_L$ in $G_P$ and $G_Q$. Let $R\\in(C-P)(L)$, let $D_R\\subset (G_P)_L$ be a decomposition group of $R$, and put $S=\\beta(D_R)$."),
    ("and, being over the identity of $\\Pi_C$, it sends the proper decomposition group of $R$ to that of $T$.",
     "and, since $\\beta$ induces the identity on $\\Pi_C$, the decomposition groups of $R$ and of $T$ in $\\Pi_{C_L}$ coincide."),
    ("Let $R\\notin E_C\\cup\\{P,Q\\}$ be a closed point", "Let $R\\notin\\mathcal E_C\\cup\\{P,Q\\}$ be a closed point"),
    ("The points of $E_C\\cup\\{P,Q\\}$", "The points of $\\mathcal E_C\\cup\\{P,Q\\}$"),
    # Step 5: inflation-restriction needs no cohomological dimension
    ("By inflation--restriction, and since $G_k$ has cohomological dimension one, $H^1(\\Pi_C,M)=H^1(G_k,M)$:",
     "By the inflation--restriction sequence, $H^1(\\Pi_C,M)=H^1(G_k,M)$:"),
    # Step 5: Lemma 1.7 of [ST09] cited for what it states
    ("By Step~4, $\\bar\\beta(D_R^P)$ is conjugate to $D_R^Q$; the conjugator projects to the normalizer of $D_R$ in $\\Pi_{C_L}$, which is $D_R$ itself \\cite[Lemma 1.7]{ST09}, so after multiplying by an element of $D_R^Q$ it lies in $M$.",
     "Let $D_R^P\\subset E_P$ and $D_R^Q\\subset E_Q$ be the images of decomposition groups of an $L$-rational point above $R$, chosen with the same image $D_R$ in $\\Pi_{C_L}$. By Step~4, $\\bar\\beta(D_R^P)$ is conjugate to $D_R^Q$, and the conjugator projects to the normalizer of $D_R$ in $\\Pi_{C_L}$. By \\cite[Lemma 1.7]{ST09} the projection to $G_L$ is injective on this normalizer; as $D_R$ already maps onto $G_L$, the normalizer is $D_R$. So after multiplying the conjugator by an element of $D_R^Q$ it lies in $M$."),
    # genus one: K' must also split the fibre above P
    ("after a finite extension $K'$ of $K$ the points of $E[m]$ and of $[m]^{-1}(S)$ are rational. The section $s_Q|_{G_{K'}}=\\gamma s_P|_{G_{K'}}\\gamma^{-1}$ lands in $\\Pi_{X'}$, which is normal, so $Q$ lifts to a point $Q'\\in X'(K')$;",
     "after a finite extension $K'$ of $K$ the points of $E[m]$, of $[m]^{-1}(S)$ and of $[m]^{-1}(P)$ are rational. Then $s_P|_{G_{K'}}$ has its image in $\\Pi_{X'}$, and so has $s_Q|_{G_{K'}}=\\gamma s_P|_{G_{K'}}\\gamma^{-1}$, because $\\Pi_{X'}$ is normal in $\\Pi_{X_{K'}}$; so $Q$ lifts to a point $Q'\\in X'(K')$;"),
]
for old, new in R:
    body = rep(body, old, new)

out = head + front + body + tail
(D / "h07_note_v3.tex").write_text(out, encoding="utf-8", newline="\n")
print("written h07_note_v3.tex:", len(out), "characters;", len(R) + 1, "replacements in head and body")
