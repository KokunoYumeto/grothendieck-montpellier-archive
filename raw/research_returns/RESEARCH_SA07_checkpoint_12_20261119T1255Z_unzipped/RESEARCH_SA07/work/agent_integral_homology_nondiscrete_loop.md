# An actual profinite loop with integral homology on every finite cover

19 November 2026. Work proof for the E.2.22 recognition map. No Galois automorphism, automorphism of the profinite free group, or full compatible motivic transporter is constructed here.

## LP1. The precise geometric statement

Let X=P^1(C)\{0,1,infinity}, choose basepoint 1/2 and the usual positively oriented simple free generators x,y about 0 and 1. Put F=pi1_top(X,1/2)=<x,y> and G=Fhat=pi1_et(X,1/2), using the actual finite-cover comparison. For every open H of G, let F_H=F intersect H; it is the actual discrete fundamental group of the pointed finite cover Y_H. Its integral homology lattice is

    Lambda_H = F_H/[F_H,F_H] = H1(Y_H(C),Z).

The finite-index subgroup comparison and abelianization identify

    H^ab = Lambda_H tensor Zhat.

There exists an explicitly specified g in G with all of the following properties:

1. g is not conjugate in G to any element of F.
2. For every open H, every integer m, and every t in G for which t g^m t^-1 belongs to H, its image under the actual map H -> H^ab belongs to the diagonal integral lattice Lambda_H.
3. g is nontrivial, lies in the closed commutator of G, and belongs to no conjugate of a cusp inertia subgroup.

Thus even the integral classes of all powers and all finite-cover lifts do not by themselves recognize a discrete conjugacy class. The statement concerns this exact element-to-homology map. It makes no assertion that g is the image of a generator under a Galois element or under an automorphism preserving every motivic comparison.

## LP2. Fixed enumerations and the finite matrix maps

Order the four letters x,x^-1,y,y^-1 in that order, and enumerate all reduced words f_1,f_2,... by length and then lexicographic order, starting with f_1=1.

For m=1,2,..., enumerate every ordered pair of permutations of {1,...,m} in lexicographic order of their value tuples. Sending x,y to that pair defines a finite homomorphism phi_i:F->S_(m_i). Include every pair, even when its image is not transitive or duplicates another kernel. Write N_i=ker(phi_i:G->S_(m_i)). These are open normal subgroups. The sequence is cofinal among finite quotients: every finite quotient embeds into a symmetric group by its regular action, and the corresponding pair occurs. Thus intersection_i N_i=1, and for every open H some N_i is contained in its normal core.

Define the actual homomorphism

    rho:F -> SL2(Z),
    rho(x)=U=[[1,3],[0,1]], rho(y)=V=[[1,0],[3,1]].

No faithfulness of rho is needed. Reduction modulo any positive integer r gives an actual finite quotient map rho_r:G->SL2(Z/r). Every matrix in rho(F) is congruent to I modulo3, so its trace is2 modulo3 and in particular is not zero.

For d>=1 put h_d=[x^d,y^d]. Writing z=3d, direct multiplication gives

    rho(h_d)=[[1+z^2+z^4,-z^3],[z^3,1-z^2]],
    det rho(h_d)=1,  Tr rho(h_d)=2+z^4>2.                 (LP.1)

The normality and commutator freedom used below are exact: whenever x^d and y^d belong to an open normal subgroup W of G, the discrete word h_d lies in [F intersect W,F intersect W].

## LP3. An induction that never stalls

Set p_0=1 and V_0=G. Suppose p_(n-1), V_(n-1), and positive moduli r_1,...,r_(n-1) have been chosen. Let

    W_n=V_(n-1) intersect N_n.

Choose d_n to be the least positive integer for which x^d_n,y^d_n belong to W_n. Concretely it is the least common multiple of the orders of the x,y images in phi_i for i<=n and in rho_(r_j) for j<n. Every factor is finite, so d_n exists and is specified without a choice. Put h_n=h_(d_n), P=rho(p_(n-1)), B=rho(h_n), and c=Tr rho(f_n).

At least one m in {0,1,2} has Tr(P B^m) different from c. Indeed, if all three were c, Cayley–Hamilton B^2-(Tr B)B+I=0 would give

    (Tr B-2)c=0.

Equation (LP.1) gives Tr B>2, while c=Tr P would be2 modulo3 and hence nonzero. This is a contradiction. Choose the least such m=m_n, and define

    p_n=p_(n-1) h_n^m_n,
    Delta_n=Tr rho(p_n)-Tr rho(f_n) !=0,
    r_n=|Delta_n|+1,
    V_n=W_n intersect ker rho_(r_n).                      (LP.2)

Here r_n>=2; in fact Delta_n is a nonzero multiple of3, so r_n>=4 and is prime to3. Thus the congruence quotient is well-defined even when r_n is composite. The trace difference is nonzero modulo r_n because its absolute value is smaller than r_n.

Every step is determined by the fixed enumerations and these least choices. The words p_n are finite words; exponents can be stored as integers without expanding them. Since h_n belongs to W_n subset V_(n-1), and V_n subset V_(n-1), one has

    p_n V_n subset p_(n-1) V_(n-1).

These are nested nonempty compact subsets of G. Their intersection is a singleton, because V_n is contained in intersection_(i<=n) N_i and those intersections tend to1. Denote the unique point by g. Equivalently p_n tends to g in the actual profinite group.

## LP4. Entire profinite conjugacy classes are excluded

Since g belongs to p_n V_n and V_n is contained in ker rho_(r_n),

    Tr rho_(r_n)(g)=Tr rho_(r_n)(p_n)
                       !=Tr rho_(r_n)(f_n).

Trace is invariant under conjugation in the finite matrix group SL2(Z/r_n). Consequently g is not conjugate in G to f_n. This excludes the whole profinite conjugacy class, not merely equality with that discrete word. Every word occurs, so g is not conjugate to any discrete element, including1.

The exclusion uses the actual finite quotient rho_(r_n), which remains frozen by all subsequent tails. Its existence is compatible with commutator-tail freedom by the three-term trace argument in LP3; no separation theorem about conjugacy classes is assumed.

## LP5. Every finite-cover lift has an integral prefix class

Fix an open H of G. Choose i so that N_i is contained in the normal core of H. Let

    K_i=F intersect N_i,
    C_i=closure_G([K_i,K_i]).

The subgroup K_i is normal in F; its commutator is normal in F. By continuity and density, C_i is normal in G. Also K_i is contained in F_H, so C_i is contained in the kernel of the actual abelianization H->H^ab.

For every j>=i, the word h_j^m_j belongs to [K_i,K_i], since W_j is contained in N_i. Hence the limit of all those tails gives

    g=p_(i-1) c_i,  with c_i in C_i.                      (LP.3)

Because C_i is normal, equality (LP.3) in G/C_i implies for EVERY integer m that

    g^m C_i=p_(i-1)^m C_i.                               (LP.4)

This is the needed power map. In particular, whenever g^m belongs to H, the actual finite word p_(i-1)^m also belongs to H and therefore to F_H. Their difference lies in C_i and vanishes under abelianization. Thus

    ab_H(g^m)=ab_H(p_(i-1)^m) in Lambda_H.

It is unnecessary, and generally unjustified, to assert p_(i-1) itself belongs to H.

Now treat every pointed lift or profinite conjugate. Let t in G satisfy t g^m t^-1 in H. Since F is dense and H is open, choose a finite word a in F in the left coset H t. Write t=h a with h in H. Conjugation by h acts trivially on H^ab. Normality of C_i and (LP.4) give

    a g^m a^-1 C_i=a p_(i-1)^m a^-1 C_i.

The right representative a p_(i-1)^m a^-1 is in F, and because the left side belongs to H and C_i subset H, it also belongs to H. Therefore it is an actual element of F_H. Abelianization now gives the literal integral lattice equality

    ab_H(t g^m t^-1)
       =ab_H(a p_(i-1)^m a^-1) in Lambda_H.                (LP.5)

This proves property2 in LP1, including all finite-cover lifts, and identifies exactly which finite prefix lies in each cover.

The comparison H^ab=Lambda_H tensor Zhat follows from the finite-index subgroup topology and abelianization of its finite-rank free fundamental group. Thus (LP.5) is membership in the actual geometric Betti lattice. Passing to a compactification sends this integral class to its integral proper-homology class by the actual filling map. No arbitrary replacement lattice is used.

## LP6. Nonperipherality and the retained E.2 scope

Every p_n is a product of commutators in F. Hence g has zero image in G^ab=Zhat^2. The three cusp inertia generators of X are x,y,(xy)^-1 up to conjugacy and inversion. Their homology vectors are primitive. If g were conjugate to a cusp power with exponent alpha in Zhat, its abelianized class would be alpha times one of these primitive vectors, forcing alpha=0 and g=1. LP4 excludes g=1. Thus g is nonperipheral.

F.3.33 consequently says that this particular procyclic subgroup closure<g> does not have an arithmetic normalizer with open Galois image. This is consistent with the construction, which imposed geometric integral-homology conditions only.

The proved limitation for E.2.22 is precise: a proposed recognition step using only integrality of every finite-cover homology class of every power and lift cannot infer that an element is a discrete loop up to profinite conjugacy. The actual E.2.22 question also prescribes one Galois automorphism on the entire cover tower and all its compatible maps. This note constructs no such automorphism or full transporter, and leaves that exact requirement open.
