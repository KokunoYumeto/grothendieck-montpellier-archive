# AT27: reference-controlled finite-range completion

The full proof is in sections/A_reference_controlled_completion.tex.

The input includes actual maps g:X→D and r_i:D→A_i, together with actual path maps F_i:X→A_i^I having endpoint zero r_i g. The reference D has coefficient comparison through the stated finite degree range. This is concrete data, not a replacement for a missing common-reference construction.

A torsion pair in X_n is handled on the representable simplicial module R[Delta[n]], so all its faces are part of one actual map. Choose primitives in D_n. Their constant paths are corrected by vertical primitives in the endpoint-zero kernel P0A_i, whose uniform acyclicity follows from A002 using target bounds through d+3. This extends the prescribed endpoint maps.

Saturation adjoins rational zero-forms a with integral derivative and g_Q(a) integral in D. The path difference from the constant reference value lies in P0A_i, so the same acyclicity proves its integrality. This kills H1 without imposing X0=S. Iterating all simplex degrees kills the remaining forms through d.

Horizontal restoration adds corresponding free identity disks to the source and reference. The path discrepancy is filled using the horizontally contractible P0A_i rows. Explicit identity-disk differentials and a direct arity-pair tensor calculation, valid for torsionfree current terms preserve the finite vertical range through degree3 integrally or through degree2p−1 over Z_(p).

The result has global vertical comparison only in that finite range and all horizontal row comparisons. It retains actual source inclusions and endpoint maps. The construction can change low forms; it does not supply the strict low-form truncation isomorphism required in the opened SA08 C34 statement.
