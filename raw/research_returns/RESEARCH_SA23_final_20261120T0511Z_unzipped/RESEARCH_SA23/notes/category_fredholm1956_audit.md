# Independent audit of the 1956 Fredholm article

Date: 2026-11-20. Auditor: GPT-6 Astra, inherited effort, category agent.

Primary source opened and read: A. Grothendieck, *La théorie de Fredholm*,
Bulletin de la Société Mathématique de France 84 (1956), 319–384,
https://www.numdam.org/article/BSMF_1956__84__319_0.pdf .
Local source: `notes/geometry_Fredholm1956.pdf`; extracted full text:
`notes/geometry_Fredholm1956_full.txt`. This audit independently read the
relevant theorem architecture, rather than adopting a keyword-search conclusion.
Rendered source pages and hashes are preserved by
`code/category_completeness_source_audit.py` and its log. Printed pages
348, 350 and 383 were also visually checked at readable resolution.

## Finding

The article does **not print a complete proof of the genus-zero product or
Lidskii trace formula for arbitrary nonnormal trace-class Hilbert operators**.
It prints sufficient determinant foundations for the complete short reconstruction
now proved in `category_simon_fredholm_audit.md`. Its mixed-rank exterior
vanishing (I§1,p327) and Hilbert multilinear estimate give minimal exponential
type by a finite-rank-tail bound. The printed zero correspondence then gives
the quasinilpotent case, and a global primary-space/quotient argument gives the
full trace formula. These deductions are not displayed in the article. The
finding is about explicit proof content, not mathematical insufficiency of
the published foundations or an exclusion of Grothendieck's priority.

| Exact locator | What the text proves | Remaining distinction |
|---|---|---|
| Chapter I, §3, equations (4)–(6), printed pp.330–331 | Determinant expansion, multiplicativity, and eigenvalue coefficient identities for finite-rank operators, reduced expressly to finite dimension | The eigenvalue coefficient formula is not extended here to arbitrary Hilbert trace-class operators |
| Chapter II, §2, Proposition 1, printed pp.346–348 | Continuity of the multilinear coefficients, entire determinant and minors; all finite-rank algebraic identities extend in their stated tensor-algebra variables | The Hilbert observation `k_n=1` on p.348 yields an exponential coefficient bound; the text does not derive a genus-zero eigenvalue product from it |
| Chapter II, §3, equations (2)–(5), printed p.350 | `det(exp u)=exp(Tr u)` and, for small nuclear norm, `det(1+u)=exp(Tr log(1+u))`, with coefficient identities in traces of powers | This identifies the logarithmic determinant with operator traces, not operator trace with the sum of nonzero eigenvalues |
| Chapter II, §4, Theorem 2 and corollary, printed pp.354–355 | Zeros of the determinant correspond to nonzero spectrum and the resolvent is meromorphic | It does not determine a possible zero-free exponential factor |
| Chapter II, §4, Theorem 4 and proof, printed pp.359–361 | Zero multiplicity equals algebraic spectral multiplicity, including nonnormal operators | No global eigenvalue summability or genus-zero step is supplied afterwards |
| Chapter II, §4 end and §5, printed pp.361–369 | Local spectral decomposition and extension of the Fredholm theory to locally convex spaces | The second Hilbert mention, pp.363–364, concerns normal operators having no nilpotent spectral block |
| Chapter III, §§1–2, printed pp.369–381 | Integral representations and classical Fredholm solution formulae | These are applications of the established determinant/resolvent machinery, not a Hilbert genus-zero proof |
| Chapter III, §3 end, printed p.383 | Order zero for nuclear operators **on nuclear spaces**, citing the memoir, II §2 no.4 | The paragraph expressly distinguishes these operators from general Fredholm operators on Banach spaces; it cannot be substituted for the requested Hilbert theorem |

All of Chapter II §§2–5 and Chapter III §§1–3 was read for this audit.
Chapter I §3 and the setup of Chapter II were read to determine exactly
what continuity extends. The final conclusion is not based on absence of
the words “genre” or “Weyl”. The subsequent Simon1977 comparison explicitly
resolves the alternative-proof risk: a complete derivation from these
ingredients is now supplied and independently audited, without assuming
spectral continuity or completeness of eigenvectors. It is our reconstruction
from the printed foundations, not a displayed argument in this article.

## Dating and edition scope

The introduction, printed p.319, dates the first drafting of **this article**
to 1952 and says the definitive manuscript had been accepted in 1953.
Its final printed page records receipt in February 1956. Neither statement
dates the crossed-out manuscript sheets in cote 1. The separate 1953 letter
in the dossier likewise cannot date every sheet.

The prompt asks whether the 1955–56 papers print the argument. Inspecting
a clearly identified later printing of the 1955 memoir can answer what
that work's inspected text contains, with the printing accurately stated.
The prompt does not independently require collating every physical printing,
and no unproved revision should be hypothesized as a new completion gate.
The dates of the particular manuscript sheets remain a distinct archival
question until a witness connects them to a date.

This note does not claim a complete line-by-line proof audit of every
theorem of the 1956 paper, and makes no priority attribution.
