# Independent whole-proof review of A23

**PASS.** Read the entire `work/row_audit/A23_B3_ORDINARY_OBSTRUCTION.tex`, initially at SHA256 e5a4726aecc69f7ad0b0d7dced6a538149fe0ffd59f9893d4cf0f6ec08bb40e2 and then reread the current full source at SHA256 `64debc1b1bd28665535090a0041f0e5e78f938adcb19824c47938a3f017271ce`. Also reopened the entire recovered A1 B.3 claim and proof at lines2488-2546 in `recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex`.

The Artin–Schreier curve is the already checked ordinary A13 curve. Its F2/F4 point counts give P2(T)=T^4-T^2+4. Squaring its four Frobenius roots gives the two roots of T^2-T+4, each twice, establishing the squared F4 polynomial without an isogeny-class assertion. The integer recurrence and Weil bound make e_m=4^m+1-t_m a positive integer for every m>=1.

The exact identities N_m=2e_m-(Q+1) and J_m=e_m^2 imply that every prime ell dividing J_m divides e_m and is at most e_m. Since N_m>=0, ell*N_m<=e_m*N_m=2e_m^2-(Q+1)e_m<2J_m. This proves the universal quantifier symbolically, not by the finite recurrence checks.

Recovered B.CL.2 actually requires N>=2|H| and ell>N for a quotient to Z/ell, in addition to primitive-root p. The kernel size J_m/ell turns the first inequality into ell*N_m>=2J_m, exactly the condition contradicted. This excludes the sufficient test over every constant extension, not other separating covers.

The exact4159 theta points over F_(2^7) persist to F_(2^14)=F_(4^7), preserving order and theta incidence. Their signed-unit condition is correctly distinguished from primitive-root2. No final/ files were edited.
