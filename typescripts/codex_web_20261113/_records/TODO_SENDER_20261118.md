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
- The queue is `C:\Users\user\Documents\TO_SEND\PRO_QUEUE_20261118.md` (main session, 15:4x UTC): account 4 sends
  SA05 .. SA16 in order, then SA03 v2 and SA04 v2 from `_hold_until_v1_SA03_SA04_return/`; SA17 .. SA32 go from the
  user's accounts 1-3, never from here. Mark each send SENT with the time in that file. After round D.
- Also on account 4: P072 (sent 09:55), FRAISSE (sent 01:34; no Stop control; checkpoint_10 at 11:58). States to check.

## Round D: unsent after the credit-guard stop (17:26 UTC), for the 30-page Pro packages
64 folders, 998 pages, in ROUNDS.tsv order (pages in brackets). Each folder is split for Chrome in
`drag_split_next/<ID>/` (scans in `<ID>_scans_part*.zip`); none of them has been sent anywhere.
K157-4-05 (16), K157-4-06 (16), K157-4-07 (16), K157-4-08 (16), K157-4-09 (16), K157-4-10 (16), K157-4-11 (16),
K157-4-12 (16), K157-4-13 (16), K157-4-14 (16), K157-4-15 (15), K157-4-16 (15), K157-4-17 (15), K157-4-18 (15),
K157-4-19 (15), K157-4-20 (15), K157-4-21 (15), K157-4-22 (15), K157-4-23 (15), K157-4-24 (15), K157-4-25 (15),
K157-4-26 (15), K157-5-01 (16), K157-5-02 (16), K157-5-03 (16), K157-5-04 (16), K157-5-05 (16), K157-5-06 (16),
K157-5-07 (16), K157-5-08 (16), K157-5-09 (16), K157-5-10 (16), K157-5-11 (16), K157-5-12 (16), K157-5-13 (16),
K157-5-14 (16), K157-5-15 (16), K157-5-16 (16), K157-5-17 (16), K157-5-18 (16), K157-5-19 (16), K157-5-20 (16),
K157-5-21 (16), K157-5-22 (16), K157-5-23 (16), K157-5-24 (16), K157-5-25 (16), K157-5-26 (16), K157-5-27 (16),
K157-5-28 (16), K157-5-29 (15), K157-5-30 (15), K157-5-31 (15), K157-5-32 (15), K157-5-33 (15), K157-5-34 (15),
K157-5-35 (15), K157-5-36 (15), K157-5-37 (15), K157-5-38 (15), K157-5-39 (15), K157-5-40 (15), K157-5-41 (15),
K157-5-42 (15)

## State
### 17:49 UTC (end of round 5 of the max sender): collecting only
- Round D: 72 sent, 54 filed with every page (14 this round: K157-2-05/16/17/22/26/27, K157-3-02/03/04/07/08/09/11/12;
  filed 17:46 and 17:47 with the GitHub push), 18 out: K157-3-01, -06, -10, -13 .. -23, K157-4-01 .. -04.
  K157-3-01 (87 min) shows Stop and is writing its notes; the rest are within their normal runtime.
- The 64 unsent folders are now 32 Pro packages built by the main session in pro_derivateurs_20261118/ (not mine).
- Credits: 6,063 at 17:48 (9,551 at 17:26); the 18 out need about 3,500 more, so about 2,500 to spare.
- Next round: collect and file the rest; no sends; Pro held.
- THEN (main session, 17:5x UTC; the user: "The hope is the credits serve to do all of the devateurs"): when NOTHING
  of round D is out any more, read the meter. Send k pairs from the END of the unsent list only if
  credits >= 1,000 + 900 k (450 a folder), never more:
  pair 1 K157-5-41 + K157-5-42 (Pro package DP157-5_41-42), pair 2 K157-5-39 + -40 (DP157-5_39-40),
  pair 3 K157-5-37 + -38 (DP157-5_37-38), and so on down the list. GPT-6.2 Astra Max, files only, from
  drag_split_next/, logged in SENT_K. Then tell the main session which packages were taken (it removes them from the
  Pro set). Fewer than 1,900 credits: send nothing. Expected at about 18:30: about 2,500 credits, so 1 pair.

### 17:27 UTC (end of round 4 of the max sender): ROUND D SENDING STOPPED BY THE CREDIT GUARD
- Round D: 72 of 136 sent (round 4 added K157-3-14 .. K157-3-23 and K157-4-01 .. K157-4-04, 17:18-17:26). 40
  returned and filed with every page (28 more this round, filed 17:16 with the GitHub push). 32 out; they finish on
  the credits left. Unsent: the 64 folders above.
- Guard at 17:26 (9,551 credits, 32 out): the out folders still need about 6,700-7,900 credits plus the 1,500
  margin, leaving room for 0-3 more, so sending stopped (conservative case).
- Cost: 6.3 credits per session-minute (16:53-17:17, about 750 session-minutes); the 40 finished folders ran 42-82
  min, mean 61 (about 63 with the slow ones still out): about 400-420 credits a folder.
- Next rounds: collect and file the 32 out as they finish (filer with push); no round-D sends; Pro held.
- Meter: 17:17 credits 10,804; 17:26 credits 9,551 (weekly 0 %).

### 16:54 UTC (end of round 3 of the max sender)
- Round D: 58 of 136 sent (round 3 added K157-3-06 .. K157-3-13, 16:48-16:52). 12 returned and filed, every page
  (190 pages): K157-1-01/02/03/08/09/11/12/17, K157-2-01/03/04/12 (filed with --no-push 16:46 and 16:53; the next
  regular filer run pushes). 46 out. NEXT: K157-3-14.
- Measured cost: 16:08:30-16:53:17, 13,236 credits over about 2,000 round-D session-minutes = 6.6 credits per
  session-minute (6.0-7.1 in the separate intervals). Finished folders took 42-69 min; 9 of the 17 K157-1 folders
  are still out past 60 min, so the typical runtime is about 63-67 min and a folder costs about 430 credits (360-500).
- Guard at 16:53 (15,556 credits, 46 out): room for about 15 more (9-19). Round D then covers about 73 of 136
  (67-77); about 63 unsent folders would go to the 30-page Pro packages. Unsent now: K157-3-14 .. K157-3-23,
  K157-4-01 .. K157-4-26, K157-5-01 .. K157-5-42 (78).
- Pro: held (the main session, 16:4x: until the user has looked at account 4's Pro limit).
- Meter: 16:47 credits 17,217; 16:53 credits 15,556 (weekly 0 %).

### 16:30 UTC (end of round 2 of the max sender)
- Round D: 50 of 136 sent (round 2 added K157-2-20 .. K157-2-28 and K157-3-01 .. K157-3-05, 16:14-16:22); none
  returned yet (the canary is about 50 min in). NEXT: K157-3-06 in ROUNDS.tsv order, within the credit guard.
- Credit guard (main session, 16:1x): credits left must cover what the out folders will still use plus 1,500.
  Measured 16:11-16:28: 5,316 credits in 17 min with about 44 sessions = about 7.1 credits per session-minute, so
  about 440 credits a folder at 62 min (355 at 50 min, 532 at 75 min). At 16:28 (22,787 credits, 50 out) the guard
  leaves room for about 20 more (8-37 by runtime): the credits cover about 70 of the 136 (58-87). Re-measure with the
  first finished D folders (credits used against folders finished). Tool: scratchpad guard.py (NOW CREDITS RATE).
- When the guard stops round D: write the unsent round-D folders, in order, here (they become 30-page Pro packages).
- Pro: HELD. OBJ_H0D6 (pilot 1/7, sent 16:23:40) ended in about 3.5 min with a package headed "INCOMPLETE - research
  remains open" (OBJ_H0D6.zip, 14 KB, in Downloads): https://chatgpt.com/c/6afdd10c-38e0-83eb-bf68-e783f5428442.
  SA01 v2 (13:37) also ended without the work: https://chatgpt.com/c/6afda9ff-975c-83eb-b255-ec6a7515cac9.
  No further Pro until the main session decides (pilots 2-7, SA05-SA16, SA03/SA04 v2 wait).
- Meter: 16:11 credits 28,103; 16:28 credits 22,787 (weekly 0 %, usage source Credits, auto-reload off).

### 16:09 UTC (end of round 1 of the max sender)
- Work steps 1-2 DONE: all 37 unfiled sends had their out zip in Space; downloaded 15:33-15:34; the 15:34:45 filer run
  filed all 37 with every page (MISSING none). None stalled, so step 5 has nothing to resend so far.
- Step 3 DONE: canary K157-1-01 sent ~15:37; about 90 s in it had read its files ("All 64 scan images match the
  manifest. I'll transcribe scans 2–17 in order ...").
- Step 4 RUNNING: 36 of 136 round-D folders sent, K157-1-01 .. K157-1-17 and K157-2-01 .. K157-2-19 (15:37-16:08),
  every one GPT-6.2 Astra Max, files only, Stop shown; links in SENT_K. K157-1-13's chat would not load after a dropped
  tool connection; it was identified as the new chat that appeared 39 s after K157-1-12's.
- NEXT: K157-2-20, then on in ROUNDS.tsv order (100 left), 20-30 a round, about 50 out. The user (16:0x): use the
  credits; stop and report only if they run out. Pro stays until after round D.
- Meter: 15:36 weekly 10 %, credits 31,205; 16:08 weekly 0 %, credits 28,792, auto-reload off.
- Pro: nothing sent or checked this round (round D first). SA01 v2 and SA02 v2 still to be checked in Space.

### 15:30 UTC (files only)
- Unfiled sends (37): K84-10, K90-02, K93-13 (10:46-11:10); K14-01, K14-07, K15-03, K15-04, K15-09, K15-10, K18-01,
  K16-01, K16-03, K16-04, K47-01, K44-01, K18-02, K18-03, K18-04, K136-04, K136-05, K136-06 (12:18-12:49);
  K136-07, K136-08, K136-09, K136-10, K136-11, K136-13, K136-14, K136-16, K136-17, K136-18, K136-20, K137-02,
  K137-03, K137-05, K138-03, K138-05 (13:11-13:32).
- In Space at 14:44 (finished, not filed): K136-08/11/13/16/18/20, K137-02/05, K138-03.
- Meter: last read 13:37 UTC by the old sender, weekly 41 % left, credits 31,205.
