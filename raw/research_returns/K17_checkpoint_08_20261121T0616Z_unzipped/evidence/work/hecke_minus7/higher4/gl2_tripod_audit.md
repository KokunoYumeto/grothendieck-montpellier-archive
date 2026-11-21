# Independent audit of the higher4 classical residual-ring calculation

Reviewer: `/root/tripod_integral`, GPT-6 Astra Pro. 21 November2026.

Scope currently completed: e26 and e28, both residual integers for each. No e30 result is included yet.

The complete saved `gl2_twist_residual_certificate.py` was read. Its `calculate` function was compared by Python AST, without source-location attributes, with the frozen and previously fully audited higher3 function. The functions are identical. The new wrapper reads the exact per-degree residual-support file and records both its hash and the executing source hash. I checked that every recorded modulus is present exactly once and that the hashes agree with the current files.

The generic proof already covers these weights. The coefficient space is the full integral Gamma1(7) cusp space, including all relevant diamond characters. Its conic basis has a unit triangular Fourier matrix; the dimension is 4e−3. The T2 coefficient formula includes its diamond correction, and the cube determinant covers all cubic twists. All eliminations are certified-unit operations over Z/M, with no primality or squarefreeness assumption.

I independently checked the stored complete matrix dimensions, every entry of the leading unit triangular matrix, every recorded determinant pivot's coprimality, the exact comparison point, the full modulus coverage and the final gcds. Results:

| e | full dimension | modulus M | recorded determinant, independently gcd-checked |
|---|---:|---:|---:|
|26|101|697446897311|564487428902|
|26|101|1346178024590512195284390892511906772585800385915601|540110375711722242001383842413974682809788702229075|
|28|109|323026426255399|291047394117369|
|28|109|1850161514202910077636429426241454885347275557889859421603|1361695747498278489585646473526121447210917280902628497429|

Every final gcd is1. Verdict: **PASS for the new code, wrapper and stated finite classical models**, using the already checked generic model proof. I did not repeat the author's full q-series execution in this audit. The derivation of the residual-support integers from the Eisenstein comparisons, the separate unitary calculation, and the global arithmetic application remain separate checks.

## Final higher4 TeX extension

The entire `gl2_residual_ring_section.tex` was independently read and reconstructed after the numerical/code audit above. SHA-256: `bc6fd4dfbf5396287acefba2049b5eef6c5341ca223e6d8e90c7d5b31bec432b`. Verdict: **PASS for all four displayed classical comparisons.** The full basis size 2(2e−2)+1=4e−3, precisions 2(d+8), complete diamond correction, determinant of the cube comparison, exact residues, and composite-modulus unit scope all match the generic construction and actual reports. The Fourier coefficient matrix is lower triangular when basis vectors are columns (the stored list of columns is its transpose). No unitary or global arithmetic conclusion is asserted by this classical-only proposition.
