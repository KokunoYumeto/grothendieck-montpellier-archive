# Independent audit of linear canonical-map ranges

Statement **A-063**, reviewing all of R-034,
work/rectangular/linear_second_row_canonical_ranges.md,
LP.1–LP.22, every proof paragraph and displayed threshold.
Checked 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Complete proof PASS.** The new arbitrary-power annihilator
injection proves the two stated surjectivity ranges for the
actual normalized grid map, with complete multiplicity spaces.

## 1. Exact directional kernel and spectator factors

On the Cauchy summand with two-letter weight \((p,q)\),
the literal derivative \(z\partial_y\) multiplies its weight
line by \(p-j\). For \(p>q\), every \(j\le q\) gives
a nonzero scalar. For \(p\le q\), exactly \(j=p\)
vanishes, leaving the actual \(S_{(q,p)}W\) summand.
This proves LP.7, including all dimensions and multiplicities.

Tensoring this map with the actual other-variable polynomial
spaces tensors its kernel with those same spaces. Each is a
symmetric power of \(W\), so successive Pieri steps retain
the diagram \((q,p)\) in every constituent. The second row
of every resulting kernel type is at least \(p\).
Consequently \(p>t\) gives injectivity on the complete
second-row band, even without the stronger \(p>q\).
No spectator factors have been dropped or replaced.

## 2. Exact lower-kernel membership for arbitrary power

The split product \((x^L+c z^L)Q\) is a product of
\(b\) linear forms over \(\mathbf C\). The coefficient
of \(c\) in its canonical diagonal vanishing is precisely
\(r+1\) times LP.13. The directional derivative composition
of the last argument \(z^b\) contributes the exact scalar
\(b!/L!\), giving LP.15.

The substitution defining \(G_F\) is linear and equivariant
in \(F\), so its image retains the same entire isotypic label.
Before derivative \(i\), its exchanged degrees are
\(p=b-i+1,q=r\); its spectator degrees are exactly \(rL\)
in \(x\), \(r+1\) in the already used factors, and \(r\)
in the others. In particular \(p\ge L+1\).
The two parameter cases in the proof are exhaustive:
\(L\ge r\) gives \(p>q\), while \(t\le L<r\)
gives \(p>t\) and hence the band injectivity of §1.
All intermediate derivatives preserve the same type.
Removing them successively therefore proves \(G_F=0\).

Evaluation in \(x,z\) separates the two outer symmetric
factors. The remaining diagonal vanishing is exactly the lower
canonical kernel condition. The actual coefficient-extraction
composite is LP.16, with scalar \(\binom bL^r\).
Two Pieri steps show that every lower kernel type contributing
to the original output is contained in it, giving precisely
the second-row band in the codomain.

## 3. Full injectivity and both iterations

The arbitrary-power R-018 inverse uses the factors
\(\prod_i\binom{b-d_i}{L}\) after separate
dehomogenization. Every highest polynomial has block degree
at most its second row, so these factors are nonzero for
\(\nu_2\le b-L\). This proves injectivity on the whole
isotypic component. After the normalized outer comultiplication,
Pieri gives \(\nu_2\le\lambda_2\le t\le b-L\).
Multiplication is a left inverse of that comultiplication.
Thus the composite is genuinely injective, proving LP.12.

Taking \(L=t\) at every step gives
\(b_s=b-t(a-s)\) and \(b_2\ge t\). Every intermediate
step satisfies its required inequality. The exact degree-two
canonical base is surjective for \(b_2\ge1\), by the
previously source-checked Sra theorem, so its transpose kernel
is zero. This proves LP.2 through the scalar-one pairing.

For the degree-five profile, \(B_t\ge t\) in every case.
At step \(r+1\to r\), the choice \(L=\min(r,t)\)
leaves inner degree \(b_r\ge B_t\ge t\).
The composition therefore has exactly the tensor factors and
total degree in LP.20. The degree-five base vanishes on the
band in every asserted range: the complete low tables give
the \(t=1\) cases, the eight square-map kernel labels all
have second row at least five, and degrees at least six are
fully injective. These are precisely the already audited
R-031 actual-map statements. The resulting zero codomain proves
LP.4.

The five small-\(t\) thresholds follow by summing the
constant cap \(t\). For \(t\ge6\), summing the uncapped
terms up to \(t\) and the capped terms afterward gives
both branches of LP.5; they agree at \(a=t+1\).
Every uniform sufficient threshold in the table follows.
Rational matrices and the explicit nonzero scalars give the
same ranks over all characteristic-zero fields. Dimensions
zero and one have the stated direct checks.

## 4. Exact boundary failure

The polynomial \(D^2x_1x_2x_3x_4\) is slot-symmetric,
nonzero, of separate degree three and highest weight
\((6,2,2,2)\). The target of \(h_{4,3}\) has at most
three rows by its actual tensor inclusion and Pieri, so this
four-row vector belongs to its kernel.

After substituting a common vector in the first three slots,
the determinant has joint parameter degree at most one:
any term with that common vector in two columns vanishes.
Its square contributes at most two, and the first-coordinate
product at most three. The coefficient of
\(z_1^2z_2^2z_3^2\), of total degree six, is therefore zero.
This proves the claimed failure of injectivity when
\(r=3,L=t=2,b=3\), with \(b-L<t\), by the stated
actual map. It verifies the role of the hypothesis without
asserting an outside-range classification.

This event is a complete proof review. No additional numerical
sweep is claimed, and the previously recorded primary-source
checks are not counted again.

