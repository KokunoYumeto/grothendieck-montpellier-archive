# Independent complete proof review: R-23

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.

Completed and recorded: 2026-11-21T03:42:50Z.

Scope: the complete final R23 fragment, including the revised height-five obstruction for every \(m\ge3\). The primary ELSW/BCMV source locators were checked by root and the author; they were not reopened here. The first-syzygy case actually needed in this proof was independently rederived from the written monomial argument.

**PASS.** No mathematical correction requested.

## First syzygies and their specialization

The squared-entry monomial identifies the omitted row/column and the doubled row/column uniquely, so it eliminates every coefficient whose multiplying entry has neither the omitted row nor the omitted column. For a repeated column with all rows used once, the two possible terms give pairwise opposite coefficients; three distinct rows in characteristic zero force all these coefficients to be zero. The row analogue is identical.

For the remaining coefficients \(a_{ij}X_{ij}G_{ij}\), comparing permutation monomials differing by a two-column switch gives \(a_{ij}=\alpha_i+\beta_j\). The permutation-sum constraint and the scalar redundancy leave exactly \(2m-2\) dimensions. The generators \(G_{ij}\) have no constant relations, already from their missing-row/missing-column multidegrees, so no earlier minimal syzygy degree is omitted.

The displayed row/column expansion differences remain independent after the cyclic restriction: the nonzero diagonal and cyclic entries impose \(\alpha_i+\beta_i=\alpha_i+\beta_{i+1}=0\). Connectivity forces constants, and the zero-sum normalization forces zero. This supplies the requisite nonempty open independence condition.

## Constant relations and the degree-m complex

For each \(k\), the stated cyclic cofactor has one matching and bidegree \((m-k-1,k)\). Its geometric binary factors have no zero coefficient because their lengths are less than \(m\). Every character \(0,\ldots,m-1\) occurs, since the two exponent ranges sum to that full interval. Its \(m\) cyclic translates are therefore independent by Fourier inversion. Distinct bidegrees separate the \(m\) different orbits, proving independence of all \(m^2\) restricted cofactors.

Tensoring the minimal resolution and taking degree \(m\) gives exactly
\[
\mathbb C^{2m-2}\longrightarrow S_1^{m^2}\longrightarrow S_m.
\]

Higher-degree first-syzygy generators do not contribute to this degree. Its first map is injective on the proved open set. The second is the differential of the pencil-to-permanent map. In characteristic zero its general rank equals the image dimension, so its first homology has dimension \(4m^2-c_m-(2m-2)\), exactly the asserted Tor defect.

Below degree \(m-1\), the first free module contributes nothing; in degree \(m-1\), the proved cofactor independence makes its map injective. Thus every asserted lower degree of Tor1 vanishes.

## Numerical values and limitations

The known \(m=3,\ldots,16\) image dimensions give the displayed positive defect list, including endpoints 12 and 25. At the cyclic section the differential rank \(2m^2+2\), together with the same \(2m-2\) old relations, gives the distinct special defect \(2m(m-1)\). The R-22 lower bound gives \(0\le\epsilon_m\le20m^{3/2}-2m\).

Taking the stated primary-source input \(\operatorname{ht}J_m\ge5\) for \(m\ge3\), the final inequality
\[
\operatorname{depth}(R/J_m)\le m^2-5<m^2-4
\]

rules out the full proposed regular sequence for every such \(m\). The stronger height-six theorem is consistent but unnecessary for that conclusion. This does not force the particular degree-m Tor component to be nonzero; it only blocks the attempted global exactness justification. The text correctly leaves its vanishing for \(m\ge17\) as a separate, smaller gate.
