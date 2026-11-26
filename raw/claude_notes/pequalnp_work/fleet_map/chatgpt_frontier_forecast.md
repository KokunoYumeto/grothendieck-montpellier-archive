# What mathematical requests are likely next?

[Shared proof map](FLEET_MAP.md) · [Dated forecasts](<local>/Documents/Codex/2026-11-22/the-two-tracks-share-no-sound/work/fleet_proof_map/frontier_forecast_20261123T164434Z.json)

**Issued 2026-11-23T16:44:34+00:00.** The next two-hour forecast covers **16:50–18:50 UTC on 23 November 2026**. Prepare the existing forest generator for larger orders first. Point-line lower bounds with few NOT gates and small-graph lower bounds on the number of AND gates are the next two candidates. In the final hour before the freeze, all 182 new statements were filed under meta-complexity, but 180 came from just two circuit-lower-bound seats. This concentration makes individual extrapolations uncertain. [Frozen feed](https://data.pequalnp.com/data/feed/page-000060.6558482231e8.json)

## What was already present

The six-program export was generated at 2026-11-23T16:39:29.869Z, version `c22e5e0031b89e03`. All 2,961 contiguous events, from sequence 1 to 2,961, were recovered from the page index plus its separate current page. Exactly 1,469 distinct proposal IDs matched the six program maps. The independent public gap list was last updated at 2026-11-23T16:40:03.298Z and fetched at 16:41:21 UTC. Of 198 listed IDs, 189 had positive weight and were absent from the withdrawn registry. The table uses the program attached to the statement. A circuit-lower-bound seat can file a meta-complexity statement. [Frozen map](https://data.pequalnp.com/data/map/overview.04a6da0078ad.json) · [Frozen page index](https://data.pequalnp.com/data/feed/pages.4f15e885af16.json) · [Public desk list](https://data.pequalnp.com/data/desk/gaps.json)

| Program | Total rows | Checked | Proposed last 3 h | Checked last 3 h | Public gaps | Latest proposal UTC |
|---|---:|---:|---:|---:|---:|---|
| Meta-complexity | 903 | 341 | 246 | 77 | 171 | 11-23 16:36:27 |
| Library | 209 | 183 | 19 | 14 | 1 | 11-23 15:05:49 |
| Geometric complexity theory | 218 | 137 | 0 | 4 | 16 | 11-23 10:27:28 |
| Circuit lower bounds | 41 | 28 | 0 | 0 | 1 | 11-23 01:43:37 |
| Proof complexity | 92 | 71 | 0 | 0 | 0 | 11-23 00:59:35 |
| SAT algorithm search | 6 | 0 | 0 | 0 | 0 | 11-22 22:00:19 |

The program maps exposed 128 recorded dependency entries, of which three cross program boundaries, all to library results. Proof imports and pending hypotheses add further dependencies. The four GCT acceptances with zero new GCT proposals illustrate why the checker feed alone is a poor measure of new requests. The local cycle-parity proof already fits three *existing* desk entries, 366, 367 and 369. Those matches remain useful independent of this forecast. [L-meta-366](https://data.pequalnp.com/data/lemma/L-meta-366.735f2406fc86.json) [L-meta-367](https://data.pequalnp.com/data/lemma/L-meta-367.872bbcceba20.json) [L-meta-369](https://data.pequalnp.com/data/lemma/L-meta-369.5be866b60da1.json)

## Ranked predictions

**1. Edge circuits for larger families of forests.** Confidence is moderately high. A newly proposed lemma states an exact circuit-size family for forests with at least eight vertices including a disconnected example, or for trees with at least nine vertices. A single additional example already subsumed by L-meta-902/903 does not count; a stronger general classification does.

The desk already listed a mix of individual circuit examples, including 760, 790 and 820. The research feed already proposed a conjunction for all 16 specified 7-vertex forests at 16:36:18 (902) and all 22 specified 8-vertex trees at 16:36:27 (903); both were conjectures and neither was on the public gap list. The forest generator and kernel-checked spider are the assets to reuse. Prepare canonical representatives for disconnected forests on eight vertices or trees on nine, preserving the file's exact edge ordering. [L-meta-756](https://data.pequalnp.com/data/lemma/L-meta-756.b4dae5b21be2.json) [L-meta-902](https://data.pequalnp.com/data/lemma/L-meta-902.87f5f7b7bfb9.json) [L-meta-903](https://data.pequalnp.com/data/lemma/L-meta-903.70842563a97b.json)

**2. Gate lower bounds for incidence systems with few negations.** Confidence is moderate. A newly proposed lemma either instantiates a positive few-NOT lower bound for a finite plane of order at least 11, or explicitly allows both some NOT gates and outputs accepting only specified proper subsets of the incident points in its theorem. It must state a new mathematical bound. A check of L-meta-745 or another numerical case at order 8 or 9 does not count.

At 16:32:23 the strategy note identified partial acceptance as a target. The conditional recursive bound 745 was checked. The body of 782 already studies incomplete singleton acceptance by monotone outputs, and 885, 894 and 900 already state conditional few-NOT bounds, including orders 8 and 9. Treat those orders as fixtures. A reusable arithmetic and incidence certificate should check both the restricted negation hypothesis and the actual numerical bound. Desk rows 738, 739 and 792 offer related lower-level work. [L-meta-745](https://data.pequalnp.com/data/lemma/L-meta-745.711af7f2a33f.json) [L-meta-782](https://data.pequalnp.com/data/lemma/L-meta-782.a2a12bfdb60a.json) [L-meta-885](https://data.pequalnp.com/data/lemma/L-meta-885.eccce831fe04.json) [L-meta-894](https://data.pequalnp.com/data/lemma/L-meta-894.480ba6eb76f6.json) [L-meta-900](https://data.pequalnp.com/data/lemma/L-meta-900.c391bdfdb699.json) [L-meta-792](https://data.pequalnp.com/data/lemma/L-meta-792.55ed25ccfb0f.json)

**3. Maximal-independent-set partial-function AND certificates.** Confidence is moderate for research feed, lower for a prompt on the public desk. A newly proposed lemma either gives a concrete lower bound on the AND count of the maximal-independent-set partial function for a graph on at least eight vertices, or gives a new transformation that lowers a broader class of such instances to smaller graphs with an explicit additive cost. The posted isolate, disjoint-edge and tight-union rules, including mere restatements, do not count.

Last-hour title matches were 104, but these occupied just three distinct (seat, ten-minute interval) pairs. Most repeated the same question for another named graph of at most seven vertices. The desk exposed only two title matches in this category, 150 and 217, including nearby AND-count questions with their own models. Use maximal independent sets and their one-vertex extensions to specify test rows. A circuit lower bound also requires a proof for *every* circuit below the given gate budget. The checked full-edge forest formula cannot serve as that lower bound under the partial-function promise. [L-meta-775](https://data.pequalnp.com/data/lemma/L-meta-775.8d6bb849c953.json) [L-meta-777](https://data.pequalnp.com/data/lemma/L-meta-777.9b1bf2bb6d87.json) [L-meta-783](https://data.pequalnp.com/data/lemma/L-meta-783.604061963f2a.json) [L-meta-884](https://data.pequalnp.com/data/lemma/L-meta-884.7c0eb2b5186d.json) [L-meta-901](https://data.pequalnp.com/data/lemma/L-meta-901.445dc9bd626b.json) [L-meta-150](https://data.pequalnp.com/data/lemma/L-meta-150.64d88ea67a83.json) [L-meta-217](https://data.pequalnp.com/data/lemma/L-meta-217.bce05e8312ce.json)


Each prediction is scored on distinct new proposal IDs in the two-hour window. Inspect the formal statement to resolve ambiguous titles. A previously posted theorem changing status, a duplicate, or an old conjecture entering the public queue does not earn a hit. Record a miss if the interval closes without a qualifying proposal. Evaluate public-queue appearances separately, since most research proposals do not appear there at once.

## Historical check on the forecasting signals

Six consecutive 45-minute test windows use only proposals filed before the start of that window to rank families. The chronological test windows do not overlap. All six programs participate. Each non-meta program has its own category. Meta titles are classified by the first matching rule for partial-function AND count, incidence, orientations, edge-function size, Boolean encodings, local gate structure, or the remaining meta category. Labels are coarse and the vocabulary was set retrospectively after reading the fleet. This is a historical check, not a blinded experiment.

A hit means the new row belonged to either of the two predicted categories. The four rules rank all available categories by historical count since launch, by count in the previous 45 minutes, by count in the previous 90 minutes, and by count in the previous 90 minutes allowing just one vote per family, seat and ten-minute interval. The last protects against machine-generated graph batches. Alphabetical order breaks ties.

| Test starts UTC | New rows | Since launch | Previous 45 min | Previous 90 min | 90 min, capped |
|---|---:|---:|---:|---:|---:|
| 12:00 | 47 | 5 | 34 | 34 | 36 |
| 12:45 | 42 | 5 | 15 | 15 | 15 |
| 13:30 | 18 | 2 | 10 | 5 | 5 |
| 14:15 | 23 | 9 | 9 | 9 | 3 |
| 15:00 | 48 | 23 | 25 | 25 | 32 |
| 15:45 | 152 | 13 | 60 | 17 | 60 |
| **Total** | **330** | **57** | **153** | **105** | **151** |

The simple previous-window rule performed best overall, covering 153 of 330 rows (46.4%). The capped method covered 151 (45.8%); it offers no demonstrated aggregate improvement. Both anticipated the edge-function batch in the final window and missed the much larger partial-function AND surge. A single generic category captured some hits without predicting a mathematical task. The narrower predictions above therefore carry qualitative judgments rather than calibrated probabilities.

In the last hour, edge-function titles occupied six distinct seat/ten-minute pairs, incidence titles four, and partial-function AND titles three. This breadth, the official strategy note, and the large disparity between research feed and public backlog determine the ordering. Historical frequency alone would overweight the 104-row AND batch. A genuine new SAT algorithm, a separation theorem, or any one assigned desk ID is beyond the predictive evidence here.

The private machine-readable forecast records the issue time, precise predicates and future window. The private frozen evidence includes the mutable desk list, complete event history, six program maps, exact source URLs and the classifier in the companion scoring script.
