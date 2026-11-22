# Borel–Serre finite component-covering subgroup: primary-source audit

Date: 2026-11-21. Reader: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS, with exact scope.** Borel, A., & Serre, J.-P. (1964).
*Théorèmes de finitude en cohomologie galoisienne*.
*Commentarii Mathematici Helvetici, 39*, 111–164.

Primary author archive:
https://www.college-de-france.fr/media/jean-pierre-serre/UPL6720771035987925133_Borel_Serre_Theoremes_de_finitude.pdf

Read the complete statement and proof of **Lemma 5.11, printed p. 152,
PDF page 42 (zero-based page 41)**, including its footnote. The displayed
proof gives a finite subgroup meeting every geometric connected component
of a linear algebraic group in characteristic zero. It does not assume
reductivity. Its finite subgroup consists of algebraic-closure points;
over the present field C there is no descent issue. The broader perfect-field,
possibly nonlinear assertion in the footnote is not used.

The proof reduces by a Cartan normalizer to nilpotent identity component,
then by its central series to commutative identity component. Multiplication
by the component-group order has finite kernel and is onto; the resulting
H² exact sequence supplies a finite extension covering all components.
All displayed steps were read, not merely the statement.

## Reconstruction of the terse induction

For completeness, the central-series reduction can be checked without a
splitting assumption. If the connected nilpotent identity component has
class greater than one, let A be its last nonzero connected central-series
term. It is connected, commutative, and characteristic, hence normal in
the whole group. Inductively choose a finite component-covering subgroup
in the quotient by A. Its preimage has identity component A. Applying the
commutative-kernel case to this preimage produces a finite subgroup of the
original group covering every original component. No finite complement to
the connected component is asserted or needed.

## Application checked for K-031

The group J=H<r> is a closed finite union of cosets of the algebraic
stabilizer H. Thus it is linear algebraic over C and J°=H°. The theorem
applies directly even if the preceding normalizer is not reductive.
If F meets every component of J, then F∩H meets every component of H.
Since the determinant character is trivial on H°, its image on F∩H
equals its image on H. This is the precise bridge needed by K-031;
neither a splitting J=J°⋊F nor a bound on |F| is required.

Root separately checked the modern generalization in Lucchini Arteche
(2017), Theorem 3.2. This audit independently checks the classical
characteristic-zero input and does not claim to recheck that entire
modern proof.
