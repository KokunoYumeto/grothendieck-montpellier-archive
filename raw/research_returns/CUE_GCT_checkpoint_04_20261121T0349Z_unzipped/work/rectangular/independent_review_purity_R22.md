# Targeted independent proof review: R-22, sections 6–9

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.

Review recorded: 2026-11-21T03:37:43Z.

The complete fragment was read. At the root agent's explicit division of review work, the independent complete verification and rederivation here covers sections 6–9 and the row-only coefficient-restriction dependency used in section 5. The local staircase/Fourier identities in sections 1–5 are inputs checked separately by root and isolation; this record does not claim a duplicate independent verification of all of them. No broad matrix tests were rerun.

**PASS for the stated scope.**

## Joint spaces and coefficient restriction

After removing their common geometric factor of degree \(N=k-2b+1\), the row and column spaces have coprime fixed factors of degree \(b-1\). Their intersection is their product times the two-dimensional space of linear forms, exactly the cyclic base. Their sum therefore equals the full \(2b\)-dimensional binary space of degree \(2b-1\).

For a nonzero interior character, the coefficient indices satisfy the ordinary equality \(i+j=t\), not a wrapping ambiguity. The allowed interval has length
\[
\min\{k,t,m-k,m-t\}+1\ge2b.
\]

Any \(2b\) consecutive allowed indices begin at \(0\le e\le N\). The coefficient-restriction determinant is dual Jacobi–Trudi for the rectangle \(((2b)^e)\) on the \(N\) geometric variables. Its Weyl exponents are distinct integers between zero and \(N+2b-1=k<m\). Evaluation at a primitive \(m\)th root therefore gives a nonzero Vandermonde numerator and denominator. The \(N=0\) endpoint is the identity matrix. The row-only version uses \(b+1\) columns, factor degree \(k-b\), and the same largest exponent \(k<m\); hence it also proves the restriction fact needed in section 5.

## One parameter choice and all modes

The row determinant has \(X\)-exponents in \([b-1,2b-1]\), and the column determinant in \([-b,0]\). Multiplying their product by \(X\) gives an ordinary polynomial of degree at most \(2b\). Its total degree in the motif parameters is at most \(4(b-1)\), since each normal column is quadratic and there are \(b-1\) in each matrix.

For fixed \(m,b,q\), the product over all \(T=m-4b+3\) bidegrees is a nonzero polynomial over \(\mathbb Q(q)\) by the separately checked determinant nonvanishing. Interpolation over \(\mathbb Q(q)(X)\) justifies one integer grid choice with all coordinates in \(0,\ldots,4(b-1)T\). It is legitimate for this choice to depend on \(m,q\). After this choice, every bidegree loses at most \(2b\) of its distinct interior root values, leaving at least \(m-6b+3\) good characters.

Each value of \(q^{bt}\) has at most \(\gcd(b,m)\le b\) preimages, so the good characters contain at least \(h=\lfloor(m-6b+3)/b\rfloor\) distinct evaluation points. The ordinary Vandermonde system therefore separates the \(h\) translates for every one of the \(2b-2\) normal families.

## Simultaneous differential

The selected full limits have leading bidegrees \(k\) and only lower remaining components. Since the cyclic base space is bigraded, choosing the largest degree in a proposed relation and descending proves independence of all full limits modulo the base.

Each exact cofactor relation, multiplied by its simultaneous outside permanent, is in the differential image of the same pencil for nonzero deformation parameter. Divisibility by the square of that parameter follows from the local identity; division thus gives polynomial families. Appending these to base columns produces one minor nonzero at zero, hence nonzero at one common generic nonzero parameter. This avoids adding ranks from different pencils or from incompatible parameter choices.

## Numerical bounds

The estimates
\[
h\ge m/b-7,\qquad
J_{m,b}\ge(2-2/b)m^2-22bm
\]

are valid under \(m\ge8b\). With \(b=\lfloor\sqrt{m/11}\rfloor\) and \(m\ge99\), the loss is at most \(6\sqrt{11}\,m^{3/2}<20m^{3/2}\). The padding inequality follows because the padded dimension adds three to the permanent cone dimension. Solving the ratio inequality gives precisely \(100/(2-\rho^2)^2\), and \(\rho=4/3\) gives 2025. The final example \(m\ge169,\ n\le\sqrt2m-4\sqrt m\) also satisfies the needed inequality by direct squaring. The row–column upper bound prevents this dimension method from crossing the asymptotic ratio \(\sqrt2\).

No equality formula for the permanent projection dimension, polynomial-time motif search, or gap conclusion beyond the stated dimension method is inferred.
