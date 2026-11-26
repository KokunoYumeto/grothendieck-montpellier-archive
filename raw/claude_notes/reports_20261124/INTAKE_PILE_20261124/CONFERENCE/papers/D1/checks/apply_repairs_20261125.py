"""Applies the repairs R1-R4, R7, R8 of CHECK_D1_INDEPENDENT.md (section 5) and the citation changes of
25 Nov 2026 to the section files of paper D1. R5, R6 (sec6), the abstract and the bibliography are edited by hand.
By afbbdefd94c5db150 (Claude Fable 5.2 at effort max). Run once, from papers/D1. Each replacement must match
exactly once (spaces in the pattern match any white space), otherwise the script stops without writing."""
import re, io, sys

def rep(s, old, new, name):
    pat = r'\s+'.join(re.escape(w) for w in old.split())
    ms = list(re.finditer(pat, s))
    if len(ms) != 1:
        sys.exit('STOP: %s matched %d times' % (name, len(ms)))
    m = ms[0]
    return s[:m.start()] + new + s[m.end():]

def patch(fn, edits):
    p = 'src/' + fn
    s = io.open(p, encoding='utf-8').read()
    for name, old, new in edits:
        s = rep(s, old, new, name)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print(fn, len(edits), 'edits')

patch('sec1_intro.tex', [
 ('R1', r'Let $\Cd$ be the category of finite linearly ordered $3$-uniform hypergraphs',
  'Let $\\Cd$ be the category of non-empty finite linearly ordered $3$-uniform\nhypergraphs'),
 ('R7', r'\cite[Theorems~1 and~3]{IM73}, and it is not filtered',
  '\\cite[Theorems~1 and~3]{IM73} (their category is that of the order-preserving\n'
  'injections of finite totally ordered sets; $\\Delta_{\\mathrm{inj}}$ is a full\n'
  'cosieve of it, and common successors and affine equalizers pass to a\n'
  'non-empty cosieve), and it is not filtered'),
])

patch('sec2_classes.tex', [
 ('Q-nat', r'contractible \cite[\S 1, Proposition~2 and Corollary~2]{Quillen}.',
  'contractible \\cite{Quillen}, \\cite[IV.3.2 and Example~IV.3.2.2]{Kbook}.'),
 ('Q-A', r"Quillen's Theorem~A \cite[\S 1]{Quillen}: if every",
  "Quillen's Theorem~A \\cite{Quillen}, \\cite[IV.3.7]{Kbook}: if every"),
 ('Q-cov', r'arises in this way \cite[\S 1, Proposition~1]{Quillen}.',
  'arises in this way \\cite{Quillen}, \\cite[IV.3.5.1 and Exercise~IV.3.1]{Kbook}.'),
 ('R4', r"\cite{IM73,IM76}; an element $t$ as in (QF2) is an \emph{affine equalizer} in their terminology, "
        r"and conditions of the form (QF1), (QF2) are studied in \cite{IM76} and, under the name quasi-filtered, "
        r"by Ad\'amek, Koubek and Reiterman \cite{AKR}. We use these two conditions only as stated here.",
  '\\cite{IM73,IM76}; we call an element $t$ as in (QF2) an \\emph{affine\n'
  'equalizer} of $f$ and $g$. (QF1) and (QF2) are the conditions I and IV of\n'
  '\\cite[\\S 2]{IM76} for the representable functors; in \\cite[p.~369]{AKR} a\n'
  "category is called quasi-filtered (after Ad\\'amek and Reiterman) if every\n"
  'parallel pair has a quasi-filter and any two objects have a common successor,\n'
  'and by \\cite[{Theorem~[1]}]{AKR} and \\cite[Lemma~2.1]{IM76} a connected\n'
  'category is quasi-filtered in that sense if and only if it satisfies (QF1)\n'
  'and (QF2).'),
 ('R8', r'and in \cite{Rosicky}, which concerns', 'and in \\cite[Remark~4.5(1)]{Rosicky}, which concerns'),
 ('BK', r'\cite[XII.5.2]{BK}, and the map',
  '\\cite[Chapter~XII]{BK}, \\cite[Sections~21 and~22]{JardineL8}, and the map'),
 ('GJ', r'the map of diagonals \cite[IV, Proposition~1.7]{GJ}.',
  'the map of diagonals \\cite[Lemma~21.1]{JardineL8}, \\cite[Chapter~IV]{GJ}.'),
 ('Weibel', r'\cite[Theorem~2.6.15]{Weibel}.', '\\cite[Section~2.6]{Weibel}.'),
 ('AR', r'A category $A$ is \emph{sifted} if it is non-empty and the diagonal $\Delta\colon A\to A\times A$ is final \cite{AR}.',
  'A category $A$ is \\emph{sifted} if it is non-empty and the diagonal\n'
  '$\\Delta\\colon A\\to A\\times A$ is final, that is, if for all objects $a,b$ the\n'
  'category $(a,b)\\backslash\\Delta$ of the pairs of arrows $a\\to c\\leftarrow b$ is\n'
  'non-empty and connected. By \\cite[Theorem~1.6]{AR} this holds if and only if\n'
  'colimits over $A$ of diagrams of sets commute with finite products, which is\n'
  'the definition of sifted categories in \\cite[Definition~1.1]{AR}.'),
])

patch('sec3_reduction.tex', [
 ('Q-A3', r"Quillen's Theorem~A \cite[\S 1]{Quillen}, $J$ is a weak equivalence.",
  "Quillen's Theorem~A (Section~\\ref{sec:classes}), $J$ is a weak equivalence."),
])

patch('sec4_cdelta.tex', [
 ('Q-nat4', r'so $B\mathcal U$ is contractible \cite[\S 1, Proposition~2]{Quillen}.',
  'so $B\\mathcal U$ is contractible \\cite[IV.3.2]{Kbook}.'),
])

patch('sec5_twographs.tex', [
 ('Seidel', r'(The triples with $c=1$ then form a two-graph in the sense of Seidel \cite{Seidel}.)',
  '(The triples with $c=1$ then form a two-graph in the\nusual sense; see \\cite{Seidel}.)'),
 ('Q-cov5', r'$\mathcal T$ is connected, so by \cite[\S 1, Proposition~1]{Quillen} it suffices',
  '$\\mathcal T$ is connected, so by the correspondence between covering spaces\n'
  'and functors that invert all arrows (Section~\\ref{sec:classes}) it\nsuffices'),
 ('R2', r'By Lemma~\ref{lem:pi1} all action components of $\mathcal T$ are simply connected, so',
  'By Lemma~\\ref{lem:pi1} all action components of $\\mathcal T$ are\n'
  'simply connected (each is weakly contractible or weakly equivalent to\n$\\mathcal T$), so'),
])
print('done')
