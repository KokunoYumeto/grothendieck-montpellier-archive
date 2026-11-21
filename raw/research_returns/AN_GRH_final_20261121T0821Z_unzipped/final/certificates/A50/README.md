# A50 finite certificate

Run `python3 verify_trace31_packet.py` and
`python3 check_trace31_independent.py`. Both use only the Python standard
library and work from any current directory. Each retains all1024 exact
trace-code words. Their source arithmetic was authored separately; these
packaged executions are unchanged replays, not additional implementations.
Both outputs are byte-identical to their retained expected outputs, and
all1024 parameter/word/weight tuples agree between implementations.
The producer also checks the modulo8 idempotent arithmetic. The complete
proof establishes the minimum8 for all integral annihilators; no bounded
operator search is substituted for that proof. No curve is constructed,
and no geometric realization of the abstract module is claimed.
