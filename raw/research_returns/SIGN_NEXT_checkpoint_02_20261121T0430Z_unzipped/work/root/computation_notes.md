# Exterior-order arithmetic: exactness and performance

The first SN-15 implementation formed all subset-orbit rows and used integer Hermite/Smith normal form. It reproduced all eight ordinary/projector orders for n=1 through4. Its n5 execution was stopped after coefficient growth made it slow. A second attempt removed the dependent rows but still used global HNF/Smith; that execution was also stopped. Neither unfinished computation supplies a claimed result.

The proved Pascal row identity reduces to exactly r_n rows, and the shift k-l=a-c gives an integral block decomposition. `finite_index_padic.py` evaluates those blocks locally. Its operations are unit pivot elimination modulo p^c and division of an entirely p-divisible residual matrix. It refuses a result if precision runs out and doubles the precision. In the n1–6 run, precision16 sufficed; the largest accepted local exponent was8. SN-15 proves that no prime larger than n can occur, so the prime list is exhaustive.

`verify_finite_index_padic.py` uses exact fractions and minimal-valuation Schur complements instead. It checked all144 block/prime cases for n5 andn6. It shares the reviewed integer matrix formula with the producer but does not share its modular elimination, precision logic, or any HNF/Smith routine. This is a second exact computational method, not a separate formal proof kernel.

For n1–4, every local invariant factor agrees with the integer normal-form output, which in turn agrees with both the original right-word closure and the independently built full-exterior left-word closure. The independent agent's signed-exterior entry check additionally verified634,970 entries and operator identities for n0–4. Full files identify the actual checker, model, run and date.

Reproduce the completed results with:

```sh
python3 work/root/finite_index_formula.py --max-n 4
python3 work/root/finite_index_padic.py --max-n 6
python3 work/root/verify_finite_index_padic.py
```

The first command is optional when only the extended table is needed; the other two compute and verify the new table directly. No floating point numbers are used in these arithmetic computations.
