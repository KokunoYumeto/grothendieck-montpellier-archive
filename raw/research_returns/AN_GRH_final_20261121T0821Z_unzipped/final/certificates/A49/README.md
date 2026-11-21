# A49 finite algebra certificate

Run `python3 verify_A49_finite_algebra.py` from any working directory.
Only the Python standard library is required. The exact arithmetic checks
the signed unit orbits modulo7 and9 and the integer cyclotomic norm103041.
It does not enumerate either curve or independently derive the retained
point counts and labels. Their complete source statements and hashes are
in inputs/. The original producer/output are retained; the portable copy
changes only two source-file locators, shown in path_only_changes.diff.
The portable replay has identical mathematical output after excluding
the expected source paths and script hash. This is a replay, not a new
arithmetic implementation or formal proof.
