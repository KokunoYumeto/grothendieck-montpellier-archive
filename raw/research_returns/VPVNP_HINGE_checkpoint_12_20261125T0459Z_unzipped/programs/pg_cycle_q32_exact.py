"""Exact finite high-ratio resource certificate for PG-CYCLE-Q32.

Only integer and Fraction arithmetic is used.  The lower approximation
sqrt(2)>7/5 enlarges the set of resource profiles under consideration.
The one exceptional profile is proved impossible below the threshold by
the separate dyadic-excess argument in price_geometry.tex.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


TYPES = [(512, 1), (1024, 1), (1024, 2),
         (1, 512), (1, 1024), (2, 1024)]
COST_LOWER = [Q(112, 5), Q(32), Q(224, 5),
              Q(112, 5), Q(32), Q(224, 5)]
EXCEPTION = (1, 0, 0, 1, 0, 0)


def removed_rank_two(items, big_cut):
    small_cut = 1-big_cut
    candidates = [0]
    for i, term in enumerate(items):
        if term[small_cut] <= 2:
            candidates.append(term[big_cut])
        for other in items[i+1:]:
            if term[small_cut]+other[small_cut] <= 2:
                candidates.append(term[big_cut]+other[big_cut])
    return max(candidates)


records = []
grouped = defaultdict(list)
for counts in product(*(range(int(Q(135)//w)+1) for w in COST_LOWER)):
    high_cost = sum(n*w for n, w in zip(counts, COST_LOWER))
    if high_cost >= 135:
        continue
    high = [t for t, n in zip(TYPES, counts) for _ in range(n)]
    total_r = sum(r for r, s in high)
    total_s = sum(s for r, s in high)
    total_min = sum(min(r, s) for r, s in high)
    remove_r = removed_rank_two(high, 0)
    remove_s = removed_rank_two(high, 1)
    low_r = max(0, 1024-total_r, 496+remove_r-total_r)
    low_s = max(0, 1024-total_s, 496+remove_s-total_s)
    low_min = max(0, 32-total_min)
    bound = high_cost+Q(low_r+low_s+15*low_min, 17)
    exceptional = counts == EXCEPTION
    assert exceptional or bound > 135
    key = "exception" if exceptional else str(sum(counts))
    grouped[key].append((bound, counts))
    records.append({"counts": counts, "high_cost_lower": str(high_cost),
                    "high_R": total_r, "high_S": total_s,
                    "high_min": total_min, "removed_R": remove_r,
                    "removed_S": remove_s, "low_R": low_r,
                    "low_S": low_s, "low_min": low_min,
                    "cost_lower": str(bound), "exception": exceptional})

assert len(records) == 205
assert len(grouped["exception"]) == 1
assert Q(99, 70)**2 > 2
assert 2**99 < 135**14  # 32^sqrt2 < 2^(99/14) < 135.
assert 32**2*2 > 45**2  # 32 sqrt2 + 90 > 135.
assert Q(10, 7)**2 > 2
assert 334+56*Q(10, 7) == 414 < 422

summary = [{"high_terms": k, "profiles": len(v),
            "minimum_lower_bound": str(min(v)[0]),
            "minimizer": min(v)[1]}
           for k, v in sorted(grouped.items())]
out = {"proof_status": "Exact rational finite enumeration certificate",
       "types": TYPES, "cost_lower": list(map(str, COST_LOWER)),
       "nprofiles": len(records), "summary": summary, "records": records,
       "remaining_exception": list(EXCEPTION),
       "exception_resolution": "Dyadic excess lemma in PG-CYCLE-Q32"}
target = Path(__file__).resolve().parents[1]/"outputs/pg_cycle_q32_exact.json"
target.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({k: v for k, v in out.items() if k != "records"}, indent=2))
