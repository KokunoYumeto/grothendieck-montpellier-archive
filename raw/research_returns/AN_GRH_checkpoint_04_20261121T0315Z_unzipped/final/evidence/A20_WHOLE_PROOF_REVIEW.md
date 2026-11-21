# Independent whole-proof review of A20

**PASS.** Read all of `final/proof_sources/no_three_power_theta.tex`, SHA256 `1eba0156de920f306c086164d77388916d486515576f73d9a1141061360a55bb`. No final file was edited.

The curve and its Frobenius twist coincide over F2. The stated Weil polynomial agrees with the previously checked A09 counts. The displayed quotient Q(T) multiplies the reduction of P(T) to T^20-1 in F3[T], checked independently. Cayley–Hamilton therefore makes all J[3] rational over F_(2^20), without requiring a companion matrix to be an actual Tate-module matrix.

The independent companion calculation gives det(I-C^20)=1099812538656=3^4*13577932576, with cofactor congruent1 modulo3. The rational3-primary group consequently has exactly as many points as J[3], which is already contained in it. Its exponent is therefore3. A19 places every geometric3-primary theta point in this rational group. A10 rules out every nonzero order3 theta point because the base has2-rank1. Finally B=O(P) supplies the origin, proving the stated equality rather than only containment. The exact13 witness remains compatible with this fixed-prime obstruction.

The saved independent checker `check_A20_companion.py` and output `check_A20_companion.json` pass. A separate one-off SymPy multiplication also checked the complete displayed quotient polynomial and the cofactor residue. The initial checker output had a SymPy integer JSON serialization error after its arithmetic assertions passed; converting matrix entries to Python ints and rerunning corrected this. No mathematical failure is suppressed.
