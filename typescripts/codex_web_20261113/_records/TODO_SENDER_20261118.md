# To-do of the account-4 sender (Claude Opus 5.5 at effort max), 18 Nov 2026

Kept by the sender, updated every round. The brief: `SENDER_MAX_BRIEF_20261118.md`. The main session's word of
18 Nov ~15:3x UTC (at the user's word) sets the list below. The user: "For Les Derivateurs, everything not yet
transcribed that is not also currently running from the list of stalled things, that needs to be on the sender agent's
to-do list. Make the sender agent just organize that." On Pro: "Two at a time is not unthinkable, but three at a time
maybe after we finish the transcription of Les Derivateurs."

## Rules
- Work: GPT-6.2 Astra Max (label checked in every new chat), files only, no text typed.
- Pace: 20-30 sends a round, about 50 Work sessions out at a time.
- Stop at the first failure of a kind (a send that fails, a session that cannot open its files, ends in seconds, or a
  page that will not load), report it with the link, and wait.
- No follow-up prompts; never Escape on chatgpt.com; never a reset; never Delete in Space.
- Log every send in `SENT_K_20261117.tsv` (Pro also in `../SENT_PRO_CHROME_20261117.tsv`); the meter at each round.
- Pro: at most 2 at a time on account 4; 3 only on the user's word, after Les Dérivateurs is transcribed. The first Pro
  send is the test: if it fails in seconds or cannot open its files, no more Pro; report and go on with Work only.

## Work, in order
1. Collect: download every finished return in Space; run `tools/file_returns.py`.
2. Classify the 37 unfiled sends (list at 15:30 UTC, below) from Space and their chats: finished (download), running
   (leave), stalled (no progress or an error).
3. Canary K157-1-01 (round D, Les Dérivateurs). It must open its files and start reading.
4. Round D in `drag_split_next/ROUNDS.tsv` order: 136 folders, K157-1-01 .. K157-5-42 (16 pages a folder or 15).
5. Resend the stalled ones that are not running, each in a new chat with the same files.
6. Then round 9's unsent folders in their order: 229 at 15:30 UTC, from K138-06.

## Pro, in order (`../stage_a_20261118/README_V2_20261118.md`)
- SA01 v2: sent 13:37 UTC, https://chatgpt.com/c/6afda9ff-975c-83eb-b255-ec6a7515cac9 (state to check in Space).
- SA02 v2: UNCERTAIN at 13:38 (tab group closed mid-send; folder not moved). Check Recents/Space before any resend.
- Then SA03 v2 and SA04 v2 from `_hold_until_v1_SA03_SA04_return/` (the README: send them if the v1 runs come back in
  minutes or provisional; v1 SA04 came back in 9 s as a provisional checkpoint, v1 SA03 asked back instead of working).
- Then SA05 .. SA32.
- Also on account 4: P072 (sent 09:55), FRAISSE (sent 01:34; no Stop control; checkpoint_10 at 11:58). States to check.

## State
### 15:30 UTC (files only)
- Unfiled sends (37): K84-10, K90-02, K93-13 (10:46-11:10); K14-01, K14-07, K15-03, K15-04, K15-09, K15-10, K18-01,
  K16-01, K16-03, K16-04, K47-01, K44-01, K18-02, K18-03, K18-04, K136-04, K136-05, K136-06 (12:18-12:49);
  K136-07, K136-08, K136-09, K136-10, K136-11, K136-13, K136-14, K136-16, K136-17, K136-18, K136-20, K137-02,
  K137-03, K137-05, K138-03, K138-05 (13:11-13:32).
- In Space at 14:44 (finished, not filed): K136-08/11/13/16/18/20, K137-02/05, K138-03.
- Meter: last read 13:37 UTC by the old sender, weekly 41 % left, credits 31,205.
