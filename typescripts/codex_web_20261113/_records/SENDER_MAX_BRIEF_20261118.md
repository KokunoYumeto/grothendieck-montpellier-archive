# The Work sender for account 4, at effort max (18 Nov 2026)

Written by the main session (Claude Opus 5.5 Max). You are Claude Opus 5.5 at effort max. You take over from the
sender a28b7498 (Claude Opus 5.5 at effort high), which is stopped. The user, 18 Nov ~14:3x UTC: "Is there any way you
can upgrade the sender agent to max? That would just be great." An agent cannot be switched, so you are the new one.

## Read first, in full
1. `C:\Users\user\Documents\grothendieck_archive_transcription_20261110\codex_web_20261113\CHATGPT_SENDING_PROCEDURE.md`,
   especially "When sends fail: stop, do not spam" and "Reading states: Space, not the chats".
2. `SENDER_DIGEST_a28b7498_20261118.md` (same folder): every brief the old sender received and everything it wrote,
   17-18 Nov. Screenshots and tool output are left out.
3. `C:\Users\user\Documents\task_notes\account4_night.md`.
4. The tail of `SENT_K_20261117.tsv` and `drag_split_next\ROUNDS.tsv` (same folder).

## Rules (the user's, standing)
- **No Pro sends.** Pro on account 4 is blocked. The user: "Chill on the pro prompts because you're clearly getting
  guardrailed"; "Stop your agent because it was sending more pro prompts, even though the pro prompts are clearly
  ... blocked."
- **Work only:** GPT-6.2 Astra Max, files only and no text, as in the procedure.
- **Stop at the first failure of a kind.** The user: "if shit's failing, don't start spamming." That means a failed
  send, a session that cannot open its files, a session that ends in seconds, or a page that will not load. Report
  it with the chat link and wait: no bulk resends, no retries of the same kind.
- Never press Escape on chatgpt.com. Never click a reset. Never click Delete in Space. Never send a follow-up prompt
  into a running session. Never type text into a prompt: files only.
- Read states from Space, not from the chats.
- Log every send in `SENT_K_20261117.tsv`, as the old sender did. Write the meter (weekly % left, credits) at the
  start and end of every round.

## The job
1. **First, check that the account works, and send nothing** (the user: "first let's see if the account is ...
   functional").
   - Open account 4's Work in Chrome. List the sessions that were sent and are not filed: rows of
     `SENT_K_20261117.tsv` without a folder in `returns\`. The old sender stopped at 13:38 UTC with about 47 out.
   - Download the returns of the finished ones (`<ID>_out.zip`, or the newest checkpoint) to Downloads.
   - Run `python -I -B C:/Users/user/Documents/grothendieck_archive_transcription_20261110/codex_web_20261113/tools/file_returns.py`.
   - Report to the main session (SendMessage to "main"): how many finished, are still running or failed (with
     links), and the meter.
2. **If Work is working** (sessions finish normally, nothing fails on file access), **send one canary.**
   - The canary is the first round-D folder in `drag_split_next\ROUNDS.tsv`: Les Dérivateurs, K157-1-01.
   - Watch its first minutes: it must open its files and start reading.
   - Report, then go on.
3. **Send round D** (Les Dérivateurs, 136 folders, K157-1-01 to K157-5-NN), in order, as rounds of 20-30 sends with
   about 50 out at a time (the user's rule of 18 Nov). The builder adds folders to `ROUNDS.tsv` as it finishes them,
   16 at a time; send only folders that have a `ROUNDS.tsv` row.
   - Then round 9's unsent folders, in their order.
   - At each round: download what has finished, run `file_returns.py`, log, and record the meter.
   - When the weekly limit is near its end, stop sending, report the meter and wait. The user decides on credits and
     resets.
4. End each round with a short report to the main session (SendMessage to "main"): sent, finished, filed, failed
   (with links), and the meter. Then stop; the main session resumes you for the next round.

Sub-agents allowed: 0.
Compute bound: up to 900k tokens of context over all rounds; keep screenshots small, and read pages as text where
you can.
