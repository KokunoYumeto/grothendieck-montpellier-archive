# Independent whole-proof reviews: AM-K022, AM-R-012 and AM-DO-028

Reviewer: GPT-6 Astra Pro, /root/lift_accounting, ALP_MACHINE, 21 November 2026 UTC. This file records targeted independent proof checks, not independent re-proofs of the accepted DP background.

## AM-K022 — PASS in its stated finite-jet scope

I read the full file selected_schur_permitted_jets.md, J1–J30 and its scope paragraphs. The carried DP59 integral half-orbit basis is used explicitly, rather than replaced by a full theta-group span.

The numerical threshold is justified over the residue field: \(L^3\) supplies parameters and a frame nonzero at zero, and \(L^m\) has a unit-value section for \(m\ge2\). The displayed homogenization has line degree \(3D+(M-3D)=M\) and interpolates all total jets through degree \(D\). Tensoring the single-factor maps suffices for all total product jets with the same threshold. The étale pullback by \(\alpha\), whose norm is prime to11, is a formal isomorphism over the local DVR and preserves surjectivity up to the actual integral frame unit.

The proof correctly uses a section with all lower algebraic jets zero. Therefore a possibly nonintegral Chern gauge cannot alter its top degree. Applying the homogeneous differential symbol gives \(c_\beta\beta!\), and that factorial has not been divided out. The integral basis expansion then forces at least one actual allowed tuple to satisfy the stated upper valuation bound. The diagonal monomial of the highest bideterminant has coefficient one because any off-diagonal determinant choice introduces an off-diagonal variable; its exponents telescope to the partition entries.

The selected finite input is one Heisenberg translate and has norm one. The source period is \(C=\theta[0;0](0;\tau)c\), giving \(C^{2ab}\), consistently with the common host. J30 follows from the two Cauchy–Binet inclusions using an integral right inverse of the finite free jet-surjection matrix. Fractional derivative matrices are handled by a common denominator. No class integration, later image saturation, integral reduced gauge, or global interpolation coefficient bound is inferred. These scope restrictions are essential and correct.

## AM-R-012 — PASS in its stated actual-first-edge scope

I read the full file selected_even_first_lift.md, including the newly added HC-only \(6\to20\) example and final source locators, after reading AM-K022.

The globally admissible common character has the prescribed infinity exponents and the correct inverse restriction on \(\mu_{28}\). At nonsplit finite places it is trivial on the full norm-one group; at split places its compact conductor divides29. The actual permitted half-orbit parameter is in one isotropic split position space. Principal congruence modulo \(M\) changes it by an integral vector in that same space, so both the alternating half-pairing and trace-one lattice-character phase vanish. The same argument applies to the source and target actions. The common splitting characters are trivial on that principal subgroup.

The identity-class stabilizer is finite by integral preservation and compactness at infinity. Its inclusion in \(1+29M_a(\mathbf Z_{29})\) kills its torsion: the displayed binomial valuation argument treats both a power prime to29 and a power of29. The six split-place index is
\[
 I_a(M)=29^{6a^2(e-1)}|\mathrm{GL}_a(\mathbf F_{29})|^6
       =M^{6a^2}\prod_{i=1}^a(1-29^{-i})^6.
\]
With real compact volume one and standard finite compact volume one, the supporting class has mass \(I_a(M)^{-1}\), with no total-quotient rescaling.

The source oscillator type is \(\sigma=\rho_0^\vee\). The class-supported input \(\overline{\langle u,\sigma(k)u\rangle}\) has right type \(\rho_0\), and the bilinear source theta integral gives the displayed Schur factor \(1/\dim\rho_0\). The scalar relating the primitive bideterminant to unit Schur vectors remains in the actual kernel functional. Thus both the output and input norm in R12.12 retain all mass and dimension factors. Primitive coefficient value one at identity is not confused with integrality of all real scalar values.

For the HC-only example, \(D=6\cdot6=36\), \(M=29^2\), the factorial upper bound is zero, and \(29\bmod11=7\) has order10. Hence no \(29^i-1\) for \(i\le6\) is divisible by11 and \(v_{11}(I_6)=0\). The period exponent is \(2ab=240\). The Gaussian norm is consistent with 240 ordinary J factors: its vacuum factor is \(\det(2Y)^{-120}\), its six determinant Fischer norms contribute \((6!)^6\), and each of the three metric directions occurs with total degree12. The upper valuation bound is not promoted to equality or to a uniform row gain. The noncompact Hyp3 and full source-record comparisons remain explicitly outside the result.

## AM-DO-028 — PASS in its stated even-character scope

I read the full file definite_oscillator_doubling_dictionary.md, including the completed global determinant-root calculation DO28.13a.

The pure-tensor trace pairing gives the actual Hom form, and \(g\mapsto g^{-t}\) gives exactly the inverse source action. The tensor labels \(\chi_V=\chi_T,\chi_U=\chi_S\) produce the source determinant-root inverse and target determinant-root direct character. Conjugating the automorphic input and transporting it through the dual-source group cancels the two parameter contragrediences, giving the claimed unramified standard parameter.

The doubled character \(d_\chi=\nu_\chi\circ\det\) restricts to \(\chi(\det A)\) on the Siegel Levi. It therefore transports induced sections and their good-section ideals; its fixed Weyl scalar introduces no zero or pole. With the conjugated matrix coefficient, multiplication of the section is exactly the inverse determinant twist of the representation. In the global formula, \(\chi(t)=\nu_\chi(t)^2\) for norm-one \(t\), so the extra second-group factor reduces to \(d_\chi(g_1)d_\chi(g_2)^{-1}\) and matches the two conjugated input factors. This checks the square-root convention, not merely the local formal ratio.

The resulting standard factor is \(BC(\sigma)\chi_T^{-1}\); conjugating the E-places gives \(BC(\sigma)^\vee\chi_T\). That equivalence must be taken with both components of a split F-place, as the file states. The inserted old-block ratio is \(\mu_r\mu_j^{-1}\). Its strict angular type follows from the actual selected \(e_j\) recurrence. The proof does not itself supply a local theta parameter theorem or global nonvanishing; ALP-LIFT-14 supplies those separately.

