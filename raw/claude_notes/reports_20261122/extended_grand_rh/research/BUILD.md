# Building the workshop papers

The four-page papers in the second reading are standalone pdfLaTeX sources, each with editable TikZ. Compile `workshop/RH_FROM_SHELLS.tex` and `workshop/sextic_bridge.tex` twice. The other two papers are `erdos_straus/shell_means.tex` and `elliptic_frame/elliptic_frame.tex`. Their bibliographies are in the source.

Use Python's standard library for `workshop/check_RH_from_shells.py`, `workshop/check_ideal_shell.py`, `workshop/check_sextic_bridge.py`, `workshop/verify_sextic_rough.py` and `workshop/check_sextic_shell_weight.py`. The rigorous nonvanishing calculation in `workshop/certify_cubic_real_value.py` uses python-flint 0.9.0. Its decimal endpoints, tail and comparison assertions are in the source. [Second reading](SECOND_READING.md)

Compile each of the two root TeX sources twice with pdfLaTeX in a fresh directory. The prime-race figure is editable TikZ. Both sources contain their bibliographies. The research workspace uses the shared one-slot TeX build wrapper for local compilation.

```text
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape cubic_prime_races.tex
pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape cubic_prime_races.tex
```

The prime-race study has six pages. Use the same two commands with `rough_composites.tex` for the three-page follow-up. Run `python -I -B prime_race_checks.py` and `python -I -B check_rough_race.py` for their numerical examples. The independent coefficient test is `connes/check_squarefree_sieve.py`. The criteria, tensor identities and unconditional sieve estimate have proofs in editable TeX. The required one-sided bound on either the primes or the composites alone remains open here.
