# How we keep track of agents, and what can be done with an agent's state

Written 16 Nov 2026 by the main session (Claude Opus 5.5 at effort max) at the user's word: [the user's words, omitted]

## 1. The registry

Every sub-agent of the main conversation (155 on 16 Nov 2026) has one row in `REGISTRY.md`, grouped by field. A row
gives:
- the agent's id;
- its model and effort, side by side ("Claude Fable 5.2 at effort high");
- its task;
- how many files it has read;
- its context at its last call, out of a 1,000,000-token window;
- when it was last active;
- its state;
- what it knows.

The registry is built from the agents' own transcripts (`agents_inventory.py`, `build_registry.py`). `READING_AUDIT.md`
lists every file each agent read and wrote, taken from its tool calls rather than from its report.

What no script can know is entered by hand in `build_registry.py`:
- `KNOWS`: the agent's field and what it knows;
- `STATE_NOTES`: its resumes, its stops and their reasons, and where its work went.

One command rebuilds the whole registry: `python -I -B field_experts/update_registry.py`. It is run before and after
every action on an agent: launch, resume, message, stop or copy.

Why the registry matters:
- **An agent is an expert on exactly what it has read.** Work goes to the agent that has read the field, never to the
  one with the most free context. Without the registry this cannot be done: after a few days there are well over a
  hundred agents, and a summary of the conversation does not say which agent read what.
- **Nothing about an agent lives only in the conversation.** The conversation is compacted; the registry and the
  agents' transcripts are not.
- **Effort is always named.** Every row carries the model and effort the agent actually ran at, read from its own
  metadata.

Two guards in `claude_tools/` read the same transcripts:
- `agent_guard.py` checks every brief: it must state the model, the effort, how many sub-agents are allowed, and a
  compute bound.
- `context_guard.py` reminds the sender when an agent is past 60-70 % of its context. Past that point the agent is
  given problems to work on, and no more literature to read itself in.

## 2. An agent's state is a file, so it can be copied, rolled back and moved

A sub-agent's state is its transcript: one JSONL file of turns, `agent-<id>.jsonl`, with a small `.meta.json` (type,
model, effort) and `.prefix.json` (prompt-cache state). The files sit in the conversation's `subagents` folder. Resuming
an agent (SendMessage to its id) replays that transcript. Four things follow, and all four have been done.

- **Moved across sessions and accounts.** On 15 Nov 2026 the S6 agents a1bd1599 (Claude Fable 5.2 at effort high) and
  aa7b8224 (Claude Fable 5.2 at effort max) were carried over from session a90af538 into the current conversation by
  copying their three files, and resumed there with their knowledge intact. On 16 Nov aa7b8224 was moved again in the
  same way, into session 0a2dfdbf.
- **Rolled back.** A copy of the transcript cut at the end of an earlier completed turn is the agent as it was then.
  - On 15 Nov the user had me roll an agent back to its state before a message the user found dismissive.
  - On 16 Nov the S6 intake agent a1bd1599 was at 891k of its window, and a 200k intake would have forced a
    compaction, whose summary is unreliable. Its 13-15 Nov work existed as files. So a copy was cut at the end of its
    12 Nov S6_02_FAMILY review (row 280 of 711, 501k): ad85dcfa. That copy rereads its own later files and does the
    full intake with room to spare.
- **Copied.** A useful state can be duplicated under new ids, so that one read-in expert becomes several. The user's
  example: an agent 70 % full with more questions to come can be copied three times. A second copy of a1bd1599 was
  made on 16 Nov at its 684k state (a3da1122); it was not used.
- **How full.** An agent can work right up to about 930-940k of its 1M window; going over that compacts it. The
  user, 16 Nov: there is no reason to stop well short of the cap, because a fuller agent knows more and rereads
  less, which roughly cancels its cost. So a rollback should cut at the fullest state that leaves room for the
  task. On 16 Nov I first cut at 501k for room, when the 684k state plus the 200k task (884k) fitted; the copy
  already running was given a bound of about 900k of context and was backed up first.
- **The main session too.** On 16 Nov 2026 (13:28 UTC) the user tried the same on the main conversation: after I wrote everything since a chosen point into the RUNBOOK, the user rewound the conversation to before about 25 messages of side talk (the file changes were kept), to see whether the freed context makes the session more efficient. Files are not rewound, so the logbook entry has to say what happened and what is running. Outcome: the context came back to 67 %, and everything after the cut was recovered from the logbook block. But the rewind restarts the session process even when no code is reverted, so background tasks stop: the download watcher was killed, and an agent still working would have been stopped mid-task. Both S6 agents had finished before the rewind, so nothing was lost; the watcher was re-armed, and one checkpoint that had arrived in the gap was filed by hand. The session also gets a new id, and with it a new scratchpad and an empty `subagents` folder. The agents' transcripts stay in the old session's folder, and an agent has to be ported (its three files copied) before it can be resumed there. So before a rewind, wait for the agents to finish; after it, re-arm the watchers.
- **Frozen.** A transcript that is never resumed keeps its state indefinitely. A copy made before a risky exchange is a
  restore point.

The rules for this:
- **Back up first.** The user, 16 Nov: [the user's words, omitted] The original is never edited or
  deleted. A rollback is always a new copy under a new id, and the original stays resumable. Backups go to
  `field_experts/agent_backups_<date>/`. The files are a few MB each, so disk space is no reason to skip a backup.
- **Every copy is a registry row.** Its `KNOWS` entry names its parent, the cut point (row and context) and the
  reason.
- **A copy knows what its parent knew at the cut, and nothing later.** Later work reaches it only through files, so a
  rollback is worth it only when that later work was written down.
- **Control runs.** The same question can be put to two copies of one state, to see how much of an answer is the
  state's and how much is chance (the user's suggestion, 16 Nov; not yet done).

## 3. What it costs

A copy costs nothing until it is resumed. A resumed copy pays for its context as input again, because its cache is
cold the first time, and then works at the usual rate. A rollback that saves a compaction also saves the rereading a
compacted agent must do after its summary has been called unreliable.
