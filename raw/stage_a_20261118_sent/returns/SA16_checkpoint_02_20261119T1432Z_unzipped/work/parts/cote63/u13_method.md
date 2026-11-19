# Exact U13 computation and its scope

This is a check of the numerical assertions in the archived Atkin exposition,
not development of a Stage6 direction. All arithmetic in `c63_u13.py` is exact
integer or modular arithmetic. The output includes the matrix actually used.

Put `z=(η(13τ)/η(τ))²` and `t=13z`. Maier2009, Tables2,4,5 in the opened
arXiv version, gives the two degree14 maps from X0(13) to the j-line:

* `j(τ)=Q(t)/t`, where `Q(T)=(T²+5T+13)(T⁴+7T³+20T²+19T+1)³`;
* `j(13τ)=F(t)/t¹³`, where
  `F(T)=(T²+5T+13)(T⁴+247T³+3380T²+15379T+28561)³`.

Fricke involution sends `t` to `13/t=1/z`. Consequently
`j(τ)=F(1/z)z¹³`. The program checks the rational identity between these
presentations symbolically; the source normalization is not silently changed.

The fourteen roots of `F(T)−j(τ)T^13` consist of `1/z(τ)` and the thirteen values
`13z((τ+k)/13)`, for `0≤k<13`. Newton sums therefore give the exact formula

`U13(z^n) = (S_n − z^(−n))/13^(n+1)`,

where `S_n` is the n-th power sum of those fourteen roots. The program computes
these sums recursively, confirms cancellation of all nonpositive powers after
removing the extra root, and checks divisibility by `13^(n+1)` before dividing.
It retains precision `13^(MAXD+α+1)` with `MAXD=100` and `α=8`, so every such
division leaves at least the required `13^8` precision. No division by a
nonunit is performed after reducing to the target modulus.

For the initial Laurent term, the reciprocal-root sum gives
`U13(z^−1)=−2−z`. Since `j−744=z^−1+2+Σ A_n z^n`, the constants cancel. The
subsequent eight iterates are polynomials in z modulo `13^8`; their actual
degrees are recorded, and the program asserts that no needed degree exceeds
the computed matrix range. Thus no truncation in the z-degree is assumed.

An independent q-series implementation computes `E4³/Δ` directly and checks
the first200 coefficients of `U13(j−744)` and the first15 of its second iterate.
This catches normalization, root removal and trace-division mistakes independently
of the Newton recurrence. The q-series are truncated only after the largest
requested output index; since z has valuation1, terms above that index cannot
affect earlier coefficients.

The output recomputes the archived valuation table at indices `13^6 n` for
`n=7,11,77,154,757,5299`: the valuations are `1,1,2,2,2,3`. It also checks
1,715 normalized Hecke pairs at each exponent α=1,…,8. These are exact finite
certificates. The all-index, all-exponent theorem is a literature result,
separately attributed in C-SA16-827; it does not follow from the finite tests.
