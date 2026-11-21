# Permanent ten-plane gate after P-20

## Proved status

In characteristic zero, the uniform seventh minimum and retained-dimension propagation give \(\mu_{10}(U^{\mathrm{per}}_{4,2})\ge17\). P-20 gives an explicit integral eighteen-term degeneration for the coordinate subset

\[
S=\{0,1,2,3,4,6,7,8,9,10\},
\]

so the current proved interval is **17 to 18**. The upper curve works in every characteristic. No claim deciding the interval is made here.

## A proved barrier for the particular Boolean construction family

Fix a row anchor and a column anchor. Write an evaluation vector as

\[
v(u,z)=\left(e_0+\sum_i u_i e_i\right)
       \otimes\left(f_0+\sum_j z_j f_j\right).
\]

The coefficient in \(v(u,z)\otimes v(u,z)\) indexed by a nonempty squarefree row support \(I\) and a nonempty squarefree column support \(J\) of size at most two is the ordered permanent rectangle tensor (with the anchor completing a singleton support). The usual Boolean finite-difference formula extracts this coefficient using all evaluation nodes indexed by subsets of \(I\cup J\).

Consider exactly this construction: independently labelled rectangle outputs, each extracted by its ordinary Boolean difference, with equal evaluation nodes collected. Let \(\mathcal S\) be the set of \(j\) selected pairs \((I,J)\), and let \(D\) be their downward closure. Every node in \(D\) has a nonzero first-factor coefficient: at least one independently labelled output uses it, and its coefficient is a nonzero signed Laurent monomial. Thus the number of pure summands in the collected formula is exactly \(|D|\).

Let \(r\) be the number of distinct nonempty row supports occurring in \(\mathcal S\), and \(c\) the analogous column count. Since the selected pairs are distinct, \(rc\ge j\). The downward closure contains four disjoint collections: the \(j\) selected mixed supports, the \(r\) row-only supports, the \(c\) column-only supports, and the empty support. Therefore

\[
|D|\ge j+r+c+1\ge j+\lceil2\sqrt j\rceil+1.
\]

For \(j=10\), this is at least eighteen. The P-20 product construction has \(r=2\), \(c=5\), and its downward closure has exactly eighteen nodes, so it is optimal within this precisely specified family.

This is **not a border-rank lower bound** for the tensor and does not exclude a seventeen-term degeneration using other nodes, cancellations involving additional coefficient extractions, multiple centers, nonsymmetric factors, or any other construction. It only closes the search for seventeen terms by the ordinary independently labelled Boolean formula just defined.

## Recorded exploratory attempts

1. Full ten-plane Koszul maps: A,p4 has exact modular rank 1,810 and pure cost126 (bound15); A,p3 has rank1,228 and cost84 (bound15); B,p5 has rank7,143 and cost462 (bound16); B,p4 has rank4,976 and cost330 (bound16). The record is `per10_product_koszul.json`. These discovery pivot data have not received a separate standalone minor replay, and are not used for a new theorem.

2. Every one of the 120 coordinate seven-subsets was tested with A,p3 and the balanced support-factor Koszul map. Among the resulting strongest bounds, 104 are14 and16 are13. Thus this test does not certify the hereditary condition that every seven-subset have border rank at least15. The general seventh-minimum theorem independently supplies14 in every case. Files: `per10_hereditary_probe.py` and `per10_hereditary_probe.json`.

3. A non-coordinate A9 projection with slices \(Q_i+(i+1)Q_9\), \(0\le i<9\), has modular Koszul rank996 and cost70 (bound15). This one projection is recorded in `per10_noncoordinate_A9.json`; it makes no claim about all projections.

4. The upper-triangular stabilizer of the specific permanent tensor was computed by exact rational linear equations. The Borel-flag extension search already leaves three continuous socle branches at level one. Rigid states remaining after levels one, two and three are21,229 and1,723, with respectively3,72 and863 continuous branches encountered. There was no first-prolongation pruning through level three. The exploratory run was stopped after these levels because rigid enumeration alone cannot settle its continuous branches. It is recorded honestly as incomplete in `per10_stabilizer_partial.json`; `per10_stabilizer_probe.py` is its source. No obstruction or exhaustive classification is claimed from this attempt.

The current useful next step would be a new construction outside the Boolean family, or a stronger closed apolar obstruction for the remaining extension parameters. Repeating the displayed flattenings does not settle the gate.
