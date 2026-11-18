# Sending prompts through Claude in Chrome: the procedure (17 Nov 2026, learned by the main session)

The user's word (17 Nov): Claude may send prompts on the user's ChatGPT account in Chrome and download the results,
including while the user sleeps. "You're doing the same thing that I'm doing manually."

## Accounts and browsers
- **Chrome:** account 4 ("HR"), the expiring account. It renews 21 Nov, so finish by Friday evening.
- **Vivaldi:** account 1, used by the user. The Claude tab group in Chrome is ours; never touch the user's other tabs.

## The ChatGPT interface
- **Left bar:**
  - Home: Projects, then Recents, the chats; a spinner marks a run that is still working.
  - Space: All / Pages / Slides / Sites / Images, with Recents files.
  - Also: Scheduled, Plugins, Explore, Sites, Usage, and the profile.
- **The usage meter:** the round icon at the bottom left, above the avatar. Hover it: "Weekly · NN% left".
  - Usage → Manage usage → Resets: three banked resets, which expire 30 Nov, 1 Dec and 12 Dec.
  - The USER clicks the resets.
  - Past 100 %, Codex draws on the credits (about 62,500). A reset restores the weekly allowance, not the credits.
- **Top of the page:** the Chat / Work toggle.
  - **Chat:** the model is always Pro. Pro runs at most 3 at a time, 2 if runs time out.
    **The user, 17 Nov ~23:4x UTC: "2 to 3, with 2 if the workspace ever failed."** Account 4's workspaces failed on
    17 Nov (below), so account 4 takes at most **2** Pro runs at once from now on.
  - **Work (Codex):** GPT-6 Astra at **Max**, the second slider position from the right. The rightmost is Ultra,
    which spawns sub-agents: never use it for transcription, which is one stream. Open the model button, then
    "Select model" (›), then GPT-6 Astra, then the slider. Work runs: as many as wanted, while the meter allows.
- **Space files:** each row has a "…" menu: Share, Rename, **Download**, Add to Favorites, Move to folder, **Delete**.
  Never click Delete.
  - Downloads go straight to `C:\Users\user\Downloads`, with no dialog (the user changed the Chrome setting).
  - `watch_returns_new.py` and the filer pick them up.

## Sending one Codex folder (Work)
1. Use a new chat in Work, GPT-6 Astra Max, and check the model label before sending.
2. Attach the files of `drag_split/<ID>/` with `file_upload` to the "Attach files" input. One call must stay under
   10 MB, so use one call per zip part, and PROMPT.md, PREAMBLE.tex and the smallest part together.
3. Wait until no tile spins and the Send button is enabled.
   - If a tile hangs on "Uploading" or shows "Upload failed": hover it, click its × (top-right corner), and attach it
     again, or press F5 and start over.
   - A duplicate name gets "(n)" added (PROMPT(5).md, PREAMBLE(2).tex). The split prompts say such a file is the
     same file.
4. Press the big white Send button. **No text is needed: it reads PROMPT.md.** Check that it starts ("Thinking").
5. Log it in `SENT_K_20261117.tsv`: ID, UTC time, account, chat URL.
6. Do not watch the session. The result zip appears in Space, and a session that times out shows up there or does
   not. Download from Space; never delete.

## Lessons (17 Nov, ~17:5x UTC)
- **Never press Escape on a chat page.** In a chat with a running response, Escape opens "Stop this response?". Click
  **Keep thinking** if it appears (it appeared once, in P057's Pro run; the run went on). Close panels by clicking
  elsewhere, never with Escape.
- **A PROMPT.md sent with `file_upload` can fail to load.** K34-01's first send: the model wrote "the attachment failed
  to load", worked 58 s and stopped, while the zips and PREAMBLE.tex loaded. The .md shows as "Document", the others as
  "File". So attach PROMPT.md **and** `<ID>_PROMPT.zip` (PROMPT.md inside; make it with python zipfile), and type one
  line naming both. Then check, about 30 s after Send, that the model says it read the task.
- **A run that ends with no final message may still have delivered: look in Space first** (the user, 17 Nov
  ~20:0x UTC). K34-01's second run ended at 52 min with no final message and an empty Outputs panel, but its
  K34-01_out.zip was in Space (complete: 16 of 16 pages). I re-prompted the chat instead of looking: on Work that
  costs only meter, but **never re-prompt a Pro chat whose run ended: it costs a Pro prompt.** Open Space, see
  what the last file is, download it.
- **The model picker defaults to a new model.** On 17 Nov ~20:0x UTC (GPT-6.2 Sol and Astra released) a new Work
  chat opened on GPT-6.2 Sol Light. Set the model and the effort in every new chat before attaching anything.
- The Recents spinner is not reliable: P057's chat ran without one in the list. Open the chat to see its state.

## What was sent
- K34-01 is sent by this procedure: 17 Nov ~17:2x UTC, chat c/6afc8e3c-a3f8-83eb-addf-d39dc0c1a98f.
- The other 34 round-1 folders are split and ready in `drag_split/`.
- Rounds 2-6 (`drag_next/`) wait for the pilot verdict on CTRL-148 and CTRL-145.

## 17 Nov 2026, ~21:00-21:40 UTC: round 1 of batch K lost on a workspace failure (read before any Work send)
- Sent on account 4 between 20:10 and 20:56 UTC: 34 Work sessions in 40 minutes by the round-1 sender a678d6d5 (Claude
  Opus 5.5 at effort high), plus K34-01 and two CTRL-148 tests by the main session: about 37 Work sessions at once,
  with 2-3 Pro runs. Each folder held 15-16 scans (about 2 h a session), twice the size of batch H.
- Between about 21:00 and 21:40 UTC the workspaces failed: the 13 chats checked all ended after 40-76 min with
  "workspace unavailable / disconnected / failed / environment failed" and no ZIP. Three left recovery pages in Space
  (K34-02, K34-11, K43-01). Delivered before the failure: 7 folders, 106 pages. Meter: 92 % -> 41 % left (about 10x).
- The Codex-web prompts keep no checkpoints (removed 14 Nov), so whatever a workspace held is gone with it unless the
  chat's Outputs panel or Space has it.
- The user stopped the sender (~23:29 UTC): "I'm stopping that because that seems like just complete destruction."
- **Rule until the limit is known: no burst of Work sessions.** The safe number of Work sessions at once on one
  account is not known; 32 small ones went through on 14 Nov (another account), 37 large ones failed on 17 Nov. Find
  the limit by testing small, with the user, before anything larger goes.

## Rules of the night of 17-18 Nov 2026 (the user, 18 Nov ~00:3x UTC): read before any round
- **Pro: 2 at once on an account that also runs Work.** "Apparently the third hits and that cancels the workspace even for
  a second. All Astras go fucking haywire." Three is acceptable only with the zap protocol below.
- **The zap protocol.** If the Work workspaces zap out (chats end with "workspace unavailable / offline / failed"):
  1. wait until the workspace is restored;
  2. then send each stopped Work chat one message to continue its task.
  The workspaces keep their files: on 17 Nov, continued chats delivered complete ZIPs.
- **No rush on Work sends.** The user: "I can YOLO them any minute. It's just like a little bit of manual labor."
- **The Work meter, the resets and the credits.**
  - The meter read 15 % left on 18 Nov ~00:3x UTC.
  - A reset is clicked only when the weekly meter is at 0. A reset above 0 throws away what was left ("rip. You just
    destroyed the compute"). The user clicks the resets.
  - At 0 the sessions keep running on the 62,500 credits. If the credits are used up too, the user resets it by hand.

## Reading states: Space, not the chats (18 Nov 2026, 02:3x UTC)

The user: "unless there's an outage, it just keeps going ... none of the threads will load after 3 hours ever ... They keep chugging along and dumping stuff in spaces. That's where you look." So:
- states are read from Space (out zips, checkpoints, finals); chats are not opened to check;
- "Could not load this ChatGPT conversation" and "Error in message stream" are not failures and never slow the sends;
- a chat is opened only to send: a new task, or the one continue message to a Work session whose out zip is overdue in Space (about 90 minutes for a folder of about 15 scans); Pro chats never.
- just before that continue message, search Space again for `<ID>_out.zip`: on 18 Nov, K161-2-06 had delivered a minute before its continue went, and K161-2-01 and K161-3-02 delivered within 2-3 minutes of theirs (the chat view lags the session).

## Pro concurrency (18 Nov 2026, 02:3x UTC)

Pro on account 4: 3 runs; when a Pro session has a real workspace failure, down to 2; after two hours of cooling off, up to 3 again (the user, 18 Nov 02:3x UTC: "3 runs cuts down to 2 when the pro sessions have a workspace bullshit. And then like let it cool off for 2 hours and then try 3 again").
