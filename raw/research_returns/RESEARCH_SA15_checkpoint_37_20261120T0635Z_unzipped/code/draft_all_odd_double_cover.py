"""Form an isolated complete candidate from the retained monodromy proof note."""
from pathlib import Path
import datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
source=w/'agents/monodromy/post_CP37_all_odd_double_cover_proof_note.tex'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='6786c808858ae016e5eadabb267cfd663a1c2417eac9b7b039883ab80dc5da28'
t=source.read_text();body=t[t.index('Let \\(E:y^2+y=x^3\\)'):t.index('\\paragraph{Scope for the independent audit.}')]
needle='''finite; both surfaces are smooth, so it is flat. The degree-two elliptic
linear-system involution is'''
replacement='''finite by the proper finite-fibre criterion of
\\cite[Lemma~37.44.1, Tag~02LS]{StacksProperFiniteCP38}.
The degree-two elliptic linear-system involution is'''
assert needle in body;body=body.replace(needle,replacement)
needle='''Thus \\(\\pi\\) is the quotient by this involution. More explicitly,
it factors through the finite normal quotient \\(A/\\langle\\iota\\rangle\\);
the resulting finite birational map to the normal surface \\(S\\) is
an isomorphism. This also supplies an actual descent of the line bundle,
not only numerical invariance under the involution.'''
replacement=r'''Indeed two points on the fibre over \(x\) define the same
degree-two divisor precisely when their sum is \(-x\). Thus
\(\pi\iota=\pi\); its degree-two function-field extension is
separable and has this nonidentity automorphism. On an affine
open of the smooth, hence normal, surface \(S\), the invariant
subring of the finite coordinate algebra of its inverse image
is integral over the base ring and contained in its fraction
field. Normality makes this invariant subring equal to the base
ring. Hence \(\pi\) is the actual quotient. The displayed
pullback of \(\mathcal O_S(1)\) supplies descent of the line
bundle itself, not just invariance of its numerical class.'''
assert needle in body;body=body.replace(needle,replacement)
needle='''The completed invariant ring is exactly'''
replacement='''Invariants commute with this completion: they are the kernel
of the endomorphism \\(\\iota-1\\) of the finite pushforward
module, and completion of the noetherian base is flat. A fixed
point is the only point above its quotient image, since its
degree-two fibre divisor is twice that point. Thus the completed
invariant ring is exactly'''
assert needle in body;body=body.replace(needle,replacement)
needle='''Off \\(R\\), the quotient \\(\\pi\\) is etale. On \\(R\\), its'''
replacement='''Off \\(R\\), the quotient \\(\\pi\\) is etale. One can
see this without a tame-quotient assertion: at an orbit of two
distinct points, the completed finite algebra is the product of
their completed local rings. The involution exchanges the two
factors, and its invariants are one factor. The completed local
map at either point is consequently an isomorphism. On \\(R\\), its'''
assert needle in body;body=body.replace(needle,replacement)
needle='''are independent formal coefficient parameters. At the reduced'''
replacement='''are independent formal coefficient parameters. In detail, at
the chosen exact double point the quadratic leading coefficient
is nonzero, while the differential of \\(s\\mapsto(b,a)\\)
is an invertible triangular transform of evaluation of \\(s\\)
and its first derivative there. The map to these two jets is
surjective because \\(\\deg N_m(-2P)=n-2>0\\).
The other \\(n-2\\) simple roots lift uniquely over the complete
local parameter ring. Localizing that ring at \\((a)\\) and
strict-henselizing gives a trait whose generic point maps to the
reduced-divisor open; its finite permutation image is therefore
a subgroup of the global geometric image. At the reduced'''
assert needle in body;body=body.replace(needle,replacement)
needle='''etale and fixed after strict henselization. This supplies an'''
replacement='''etale and fixed after strict henselization. Nonsquareness of
the residue of \\(b\\) follows from \\(db\\ne0\\) in the
residue fraction field of the power-series ring; separable
algebraic extension preserves this nonzero differential. Thus
the quadratic factor is irreducible there and its order-two
automorphism actually occurs in inertia. This supplies an'''
assert needle in body;body=body.replace(needle,replacement)
needle='''is fixed. This would identify the actual relative geometric
Lang image with \\(S_n\\), and its nonzero orbits with the
complement-paired subset weights \\(1,\\ldots,(n-1)/2\\).'''
replacement='''is fixed. This identifies the actual relative geometric
Lang image with \\(S_n\\). The canonical branch-module
isomorphism is Galois-equivariant for the arithmetic action as
well. All the objects were defined over \\(\\mathbf F_2\\),
so the arithmetic image is contained in this same \\(S_n\\)
and contains the full geometric image; it is equal to it.
The determinant is trivial because \\(\\mathbf F_2^\\times=1\\).
The ambient surface has zero stable cohomology, so the natural
Artin--Schreier and stable hypersurface sequences identify this
module with the requested relative Lang module, exactly as in
Lemma~\\ref{lem:root-double-cover-branch-module} and
Theorem~\\ref{thm:root-primitive-prime-permutation-counterexamples}.
No prime-dependent Cartier certificate has been used.'''
assert needle in body;body=body.replace(needle,replacement)
head=r'''% Root isolated candidate; full independent audit and finite supplement pending.
\subsection{Exact symmetric image in every odd primitive degree}

\begin{theorem}[The entire elliptic double-cover family]
\label{thm:root-all-odd-double-cover-symmetric-image}
\status{Candidate; complete written proof awaiting independent audit and supplement.}
Let \(E:y^2+y=x^3\) over \(\mathbf F_2\), let
\(A=E\times E\), and put
\[
 L_m=\mathcal O_A(mV+H+\Gamma),\quad
 V=\{O\}\times E,\quad H=E\times\{O\},\quad
 \Gamma=\{(x,y):x+y=0\},\quad n=2m+1,\quad m\ge1.
\]
On a nonempty parameter open the curves in \(|L_m|\) are
smooth and connected, have genus \(n+1\), and have
\(2\)-rank \(n-1\). Their coherent relative Frobenius has
generic stable rank \(n-1\), equal to its full rank.
The actual geometric and arithmetic relative Lang images are
both the faithful symmetric group
\[
 S_n\longrightarrow\operatorname{GL}
       (\mathbf F_2^n/\mathbf F_2\mathbf1).
\]
The determinant character is trivial. For \(n=3\) this is
\(\operatorname{GL}_2(\mathbf F_2)\); for every odd
\(n\ge5\) it is a proper subgroup of
\(\operatorname{GL}_{n-1}(\mathbf F_2)\).
\end{theorem}
\begin{proof}
'''
tail=r'''
The stated properness for every \(n\ge5\) follows from the
integer order comparison already proved for all integers
\(n\ge5\): it starts with \(120<20160\), and the next
linear-group order grows by \(2^{n-1}(2^n-1)>n+1\).
\end{proof}

\begin{corollary}[Irreducibility and the exact connected components]
\label{cor:root-all-odd-double-cover-orbits}
\status{Candidate; complete written proof awaiting independent audit and supplement.}
For every odd \(n=2m+1\ge3\), the relative
\(\mathbf F_2[S_n]\)-module is irreducible. The nonzero
relative Lang cover has exactly \((n-1)/2\) geometric
connected components, of degrees
\[
              \binom n1,\binom n2,\ldots,
                             \binom n{(n-1)/2}.
\]
Each component is defined over \(\mathbf F_2\).
\end{corollary}
\begin{proof}
Since \(n\) is odd, projection modulo the all-one line
identifies the quotient with the even-sum subspace of
\(\mathbf F_2^n\). Any nonzero vector there has two
coordinates with different entries. Subtracting its image under
the transposition of those coordinates gives \(e_i+e_j\).
Thus any nonzero invariant subspace contains one such vector,
and conjugating under \(S_n\) gives every \(e_i+e_j\).
These span the even-sum subspace, proving irreducibility.

Every nonzero class has a unique subset representative of
cardinality \(1\le j\le(n-1)/2\), up to taking its
complement. The full symmetric group is transitive on each
set of a fixed cardinality. These are exactly the nonzero
orbits and have the displayed binomial sizes. Finite-cover
components correspond to these orbits. Arithmetic and geometric
images agree and preserve every cardinality, giving the final
descent assertion.
\end{proof}

\begin{remark}[Scope and reproducible evidence]
\label{rem:root-all-odd-double-cover-scope}
\status{Candidate scope; no fixed-embedding large-degree conclusion.}
The proof extends the actual prime examples to every odd degree,
and determines their exact image and components. The fibre
degree remains two, so none of these lines is very ample and
this varying primitive family is not the sequence of powers of
a fixed embedding line. General A.4 remains open.
The original proper finite-fibre criterion and its complete
proof were opened at Tag~02LS; the noetherian formal-functions
proof at Tag~02OG was also read in full. The exact quotient,
formal invariant ring and wild quadratic inertia are proved
above. A separate symbolic supplement is being prepared; this
candidate is not promoted before that program/output and the
complete independent written audits are retained.
\end{remark}
'''
out=w/'notes/all_odd_double_cover_candidate.tex';assert not out.exists();out.write_text(head+body+tail)
record={'status':'ISOLATED COMPLETE WRITTEN CANDIDATE; AUDIT AND SUPPLEMENT PENDING','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate':str(out.relative_to(w)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'author':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root, based on the independently retained monodromy proof note','source_note_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'primary_sources_opened':['https://stacks.math.columbia.edu/tag/02LS','https://stacks.math.columbia.edu/tag/02OG'],'source_refs':['turn813518147view0','turn813518147view1'],'source_scope':'Both complete printed proofs actually read; first uses elementary etale neighborhoods and fpqc descent, second uses formal functions plus the H1 affine criterion. No external scroll classification or characteristic-zero monodromy theorem is imported.','no_CP37_promotion':True}
(w/'notes/all_odd_double_cover_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
