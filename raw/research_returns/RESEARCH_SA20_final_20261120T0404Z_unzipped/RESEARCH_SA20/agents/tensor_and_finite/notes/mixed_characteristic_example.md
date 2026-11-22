# Concrete generic-characteristic p-squared tensor kernel

Research note, 2026-11-19; consequence of the audited B059 detector, not a separate theorem inventory item.

Let A=(Z/p²Z)[[t]], Q=A[1/t], q(X)=X^p-X. Then F=pq/t and H=q belong to Int(A). Indeed the constant coefficient of p(a^p-a) vanishes modulo p² for every a in A, by Fermat modulo p. The tensor F⊗H-H⊗F has zero polynomial image.

For every G in Int(A), G(p)-G(0)=pG′(0), since p²=0, so pG′(0) belongs to A. Thus G′(0) lies in M=A+pQ, and M/A is canonically a module over V=F_p[[t]]; it is killed by p. Define beta(G,H)=[G′(0)]*(H′(0) mod p) in M/A. This is A-balanced because the action on M/A factors through V. Its value on the displayed tensor is p/t+A, nonzero. This gives the smallest newly handled generic-characteristic example without a coefficient field in Q.

The base is infinite. A finite jet check may illustrate the integer-value and detector calculations but would not replace the proof above.
