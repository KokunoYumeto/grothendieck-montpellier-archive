# Exact supplement attempts

The initial execution completed the order-five Gauss-sum census, then
stopped while SymPy sorted the order-eleven cyclotomic factors. The error
was `TypeError: nmods cannot be ordered` in `polytools._sorted_factors`.
No mathematical assertion had failed. The factor extraction was replaced
by `flint.nmod_poly([1]*prime, 3).factor()`, with the same deterministic
selection by integer coefficient tuples. All computations were then rerun.
