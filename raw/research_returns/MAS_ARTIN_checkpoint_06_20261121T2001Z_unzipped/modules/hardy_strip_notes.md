# Actual partial strip at s = 0

## Results

The new module is modules/hardy_strip.tex, statements MA-HY-001–003.
It uses the actual Hilbert closure of the centered theta ideal.
The polynomial weight parameter is exactly zero throughout.

- **MA-HY-001:** Replace the max exponential weight by the equivalent sum weight, apply Mellin Plancherel, and use the exact half-derivative conformal unitary to the disk. The actual ideal closure is the multiplier range closure of Ξ(a+z), hence its inner factor times H². The finite boundary zeros cannot carry singular atoms because Ξ is analytic across them. The two infinite ends cannot carry atoms because MT-M18.8 gives selected-height lower bounds much larger than the double-exponential decay an atom would force. The inner factor is therefore exactly the Blaschke product of the completed zeros strictly inside the strip.
- **MA-HY-002:** Actual quotient convolution is a compressed analytic multiplier. The Malmquist basis is derived without a separation hypothesis, including repeated zeros. Its boundary mass is harmonic measure at each zero. Strip Poisson tails are uniform even as the real part approaches either edge. Rapid boundary decay and the local zero count give Hilbert–Schmidt multipliers; factoring a compact-test Mellin multiplier into two such factors gives trace class. The trace is then computed in this actual orthonormal basis. The actual translation resolvent itself is Hilbert–Schmidt, and its square is trace class.
- **MA-HY-003:** The resolvent square supplies precisely the arithmetic premise needed by the operator proof of MA-LIFT-002. Its half-line integration by parts with the cusp term at zero gives actual C_g P_Z trace class at s = 0 for an arbitrary centered partial strip. MA-LIFT-003 then supplies the geometric-order cutoff trace limit. The result is the partial open-strip zero sum, including multiplicity.

All three have author whole-proof review events. A separate independent review is being coordinated by root. The module does not claim a full Hardy–Sobolev closure theorem or a full return to Meyer on a partial strip.

## Source checks

1. **Canonical generator and unconditional end bounds.**
   sources/RETURN_GRH_NIGHT_checkpoint_07_20261121T0617Z/work/root/block_arithmetic_synthesis.tex, opening definition and M18.5–M18.9. The Mellin generator is exactly Ξ, not Ξ times a Gaussian. M18.6 makes Ξ bounded on every fixed vertical strip. M18.8 is unconditional and applies on the new strip centerline at selected positive and negative heights.
2. **Primary canonical factorization and closure theorem.**
   Beurling, A. (1949). On two problems concerning linear transformations in Hilbert space. *Acta Mathematica, 81*, 239–255. DOI: https://doi.org/10.1007/BF02395019.
   Primary paper: https://www1.cmc.edu/pages/faculty/MONeill/Math%20138/papers138/Beurling.pdf.
   Read the complete Factorization Lemma in §7, pp.245–246, including the singular measure; read Theorem I and its complete proof in §9, pp.247–249. The theorem gives the closed cyclic subspace determined by the inner factor. The new argument proves separately that the singular measure vanishes.
3. **The two strip Hardy-space conventions.**
   Bakan, A., & Kaijser, S. (2007). Hardy spaces for the strip. *Journal of Mathematical Analysis and Applications, 333*(1), 347–364. DOI: https://doi.org/10.1016/j.jmaa.2006.10.088.
   Publisher metadata: https://www.sciencedirect.com/science/article/pii/S0022247X06011668.
   Author-uploaded primary PDF: https://www.researchgate.net/profile/Andrew-Bakan/publication/235664302_Hardy_spaces_for_the_strip/links/5a39942da6fdcc34776a32cd/Hardy-spaces-for-the-strip.pdf.
   Equations (2.1)–(2.3), Theorems 2.1–2.2 are on p.349; Corollary 2.1 runs pp.349–350. Their distinction between composition-only conformal Hardy space and the unweighted translation-invariant space is essential. Their §3, pp.351–352, supplies the conformal and Poisson conventions; proofs of Theorems 2.1–2.2 are in §4, pp.352–355. The invoked statements and normalizations were checked; no full independent audit of their whole paper is claimed.
4. **Existing actual-operator lift.**
   modules/lift_trace.tex, MA-LIFT.9–MA-LIFT.19, was read again in full. After replacing only its trace-class quotient resolvent premise by MA-HY.17, the half-line integration-by-parts and cutoff proofs apply with k = 2 and s = 0. The source's final all-zero trace is replaced by the newly proved partial trace.

Useful source retrieval references, for root to open directly before using any web citation in final chat: Beurling turn784941444view0; author Bakan–Kaijser PDF turn693640451view0; exact pp.349–352 text turn731332697view0; publisher metadata turn664747729search0. These are retrieval notes rather than file bibliography identifiers.

## Scope

No A, M, or new outside preprint is used. Published Hardy-space theory and the unconditional inherited completed-L estimates remain explicit inputs. Boundary evaluation of every finite Mellin derivative is unbounded at s = 0, in agreement with the absence of boundary jets from the Blaschke closure. This fact changes when a polynomial weight supplies sufficient Sobolev regularity, so the proof does not cover the original s ≥ 3 completion by a formal substitution.

The partial trace need not equal the full Meyer trace. MA-HM-003 still excludes a full return factorization for arbitrary compact tests if a strictly exterior zero block is present. MA-HY-003 proves convergence of the traces of the actual geometric-order operators and trace-norm convergence of the spectral correction. It does not assert trace-norm convergence of the geometric operators themselves.
