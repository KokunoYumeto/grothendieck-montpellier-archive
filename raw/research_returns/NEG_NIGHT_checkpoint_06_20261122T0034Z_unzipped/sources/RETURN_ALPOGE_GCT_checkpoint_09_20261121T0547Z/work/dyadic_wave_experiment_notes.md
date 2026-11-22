# Dyadic wave experiments — 2026-11-21T03:52:12.640365+00:00

These are exploratory finite calculations, not a proof of the remaining asymptotic estimate.

The exact script `compute_dyadic_wave.py` forms the actual normal character as Sym^3(chain weights) minus End(chain weights), and uses the actual residue convention eta=zeta^g. It inverts each factor modulo X^(M/2)+1 by signed permutation cycles in integral arithmetic with a power-of-two denominator. The inverse identity was checked at every step through n=12. The n=4 output is exactly (1+X+X^2+X^3)/8, matching the known cubic-four-variable Hilbert series. Full rational inverse vectors through n=12 and samples through n=14 are in dyadic_wave_experiments.json.

Primitive trace gives 2W(r)=(-1)^floor(r/(M/2)) times the coefficient indexed by r mod(M/2). The finite data have large positive and negative coefficients; uniform positivity cannot be assumed. For n>=8 in this sample, magnitudes rapidly grow. The sign patterns often look like short oscillations, but this observation proves no eventual pattern.

Separate floating direct sine products through n=17 are in dyadic_wave_magnitude_experiments.json. The largest pair in those finite cases is a=plus/minus(3g)^(-1) modM. The summed absolute contribution of all other embeddings, divided by one largest magnitude, decreases from about0.09424 atn8 to about1.02e-68 atn17. This is not an interval-arithmetic or infinite-family certificate.

The exploratory increments log|C_n(a)| minus log|C_(n-1)(-a mod(M/2))|, using eta rather than canonical zeta coordinates, are recorded in dyadic_increment_experiments.json. The largest observed increments for n7..17 are again at plus/minus3^(-1). A uniform trigonometric increment bound is unproved.

The valid index implication is the separately checked P56: positivity after a shift forces f_n(x)>=2W_n(x) at every later integer x. Hence a single large positive value in a short later window suffices; negative values alone supply no witness.
