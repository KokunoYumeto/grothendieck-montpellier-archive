# A1 research notebook

## Route 2 exact gate
For a genus-two curve C in characteristic 2, let Theta_B be the theta divisor for the locally exact differential sheaf, and let S_C be the odd primes ell for which a nonzero L in J_C[ell] lies on Theta_B. Hooley under Masullo supplies positive density of A_2={ell: ord_ell(2)=ell-1}; it does not yet supply S_C intersect A_2 nonempty. The weaker +/- version asks <2,-1>=F_ell^*.

## Candidate fully checked elementary geometric bridge
If one connected cyclic etale cover D->C of odd prime degree ell has p-rank-zero new part P=im(sigma-1) on J_D, then any prime-to-p point-section collision gives lifts Pprime,Qprime with T=[Qprime-Pprime] p-primary. Therefore (sigma-1)T=0. The equality sigma(Qprime)+Pprime ~ Qprime+sigma(Pprime) gives a degree-two pencil unless the divisors are equal; equality is excluded by freeness and Pprime!=Qprime. But D cannot be hyperelliptic: an odd-order deck automorphism descends nontrivially to P1, has a fixed point, and fixes a point over it since that fiber has <=2 points, contradicting freeness. Thus no collision. Need full proof of lifting/Kummer implication or cite supplied A.3 after obtaining full source.

## Candidate cohomological bridge
For genus2, each H1(C,L^i), i nonzero, is a line. Absolute p-Frobenius permutes these lines by i->pi. If p generates F_ell^*, they form one cycle. A theta incidence makes one edge zero; then the entire cycle is nilpotent, so the new p-rank is0. For <p,-1>, need symmetry of Theta_B to meet both p-orbits when -1 not in <p>. Prime primitive condition avoids this extra proof.

## Failed arithmetic implication: exact counterexample to density inference
Primes ell=1 mod8 have density1/4, but 2 and -1 are both squares, hence <2,-1> is proper. Infinitely many, even positive-density theta-support primes would not by itself suffice. This is not a curve counterexample and not a logical independence theorem for GRH.

## Literature approaches
- Hooley: original density (verify numbered theorem), Fan-Pollack Theorem1.1 gives modern exact locator.
- Lenstra 1977 Theorem3.1 supports Artin inside a FIXED finite Frobenius condition; 4.1/4.2 determine zero density. Need a finite Galois encoding of S_C and nonzero compatible density; none supplied.
- Goldfeld Artin on average averages base a, not geometry-selected primes for fixed a=2.
- Pop-Saidi Proposition2.1 and Corollary2.3 say pairwise prime orders; proof shows pairwise COPRIME orders, not prime integer orders. Proposition2.4 passes to a new cover and its theta divisor. These do not give the prime-order gate, and genus rises.
- Higher genus: singular Frobenius on one edge does not imply nilpotence when character spaces have dimension g-1>1. Example one edge diag(0,1,...,1), all others identity preserves a stable rankg-2 summand.
- Saidi-Tamagawa 2009 proves almost injectivity, exceptional set may remain; inspect later A.1 full proof recovered from Library.
