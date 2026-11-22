# Read-only cyclic-certificate performance diagnosis

The e38 log entry `whole characteristic polynomial` is a completion marker, not a start marker. The frozen integral driver inserts it immediately after the verifier assertion comparing the fully certified polynomial to the saved coefficients. The exact integer Horner identity and modular cyclicity witness have therefore already passed for p=7 when this marker appears.

Following that marker, the frozen verifier multiplies the saved factors, evaluates the comparison polynomial, checks two extra points, and begins the next prime's complete transformed-evaluation loop. The p=13 transform loop is substantially larger than the p=7 loop. A long gap after the p=7 marker does not identify a Horner bottleneck.

The carried standalone e36 whole-polynomial certificates used clearing denominators 276821228877050 (48 bits) and 968874301069675 (50 bits), completing in 21.8916 and 23.5509 seconds respectively. The e36 full sum-first replay took 2813.748 seconds. These are actual previously completed timings; they do not predict an exact current completion time under shared CPU load.

Common-denominator integer Horner can in principle be replaced in a future separate verifier by exact rational-vector Horner with common-content cancellation. The current source/timing evidence gives no concrete reason to add that implementation now. No running source or report was modified, no process was interrupted, and no redundant large verification was launched for this diagnosis. The JSON records the exact inspected source/report hashes.
