# Second passes by route: the inventory and the coverage audit (17 Nov 2026, ~00:5x UTC)

Main session (Claude Opus 5.5 at effort max), at the user's word of 16 Nov ~23:2x-23:56 UTC: Pro-transcribed
packages, which carry Pro's research notes, get their second pass from Claude (text against the scans, plus reading
and organizing Pro's notes for the field experts). The material transcribed by GPT-6 Astra at reasoning effort max over
Codex web, which has no commentary, gets a Pro second pass that adds the commentary. "The organization of the second
pass prerequisites could happen now." This updates SECOND_PASS_PLAN_20261115.md (method there, section 4) with the
counts of 17 Nov and the new split.

## 1. What exists, by route (counted 17 Nov from the files)

| Route | Model | Units | Scans | Commentary | Second pass done |
|---|---|---:|---:|---|---|
| Pro packages, final returns | GPT-6 Astra (ChatGPT Pro mode) | 70 packages | 2,923 | yes: notes.md, doubts.md and inventory per package, with the context packets | Longue Marche core only: 6 packages, 390 pages (second_pass/out, Claude Opus 5.5 at effort max) |
| Codex web | GPT-6 Astra at reasoning effort max | 137 units (180 return folders) | 1,060 | notes written without the context packets | none |
| API typescripts | see api_typescripts_20261112/API_TYPESCRIPTS_REPORT.md | — | — | — | — |

Pro first passes measured about 0.8 errors per 100 words, Codex web about 0.2 (SECOND_PASS_PLAN_20261115.md, section 1).

## 2. Coverage audit (tools_20261113/coverage_audit.py; COVERAGE_AUDIT_20261117.md, coverage_audit_20261117.tsv)

- 77 sent packages asked for 3,221 scans. Scans the Codex-web route had already transcribed are left out, as each
  prompt says.
- Every final that came back holds every scan its package asked for.
- Seven packages have no final:

| Package | Scans | State | What is missing |
|---|---:|---|---|
| P045_185_MPL_84_097-145 | 48 | running (checkpoint 01 filed) | 5 not yet in a checkpoint |
| P046_88_MPL_12_150-168+15_002-033 | 45 | running (checkpoint 01 filed) | none: checkpoint 01 already has every scan |
| P033_91_MPL_15_139-194 | 45 | stalled on the frozen account (checkpoint 01 only) | 14 scans: cote 15, 170-171, 179-194 |
| P021_230_MPL_57_226-270 | 43 | no return at all | all |
| P030_156_MPL_93_221-236+161-5 | 43 | no return at all | all |
| P032_220_MPL_122 | 32 | sent 16 Nov ~17:58 UTC; no checkpoint in 7 hours | all |
| P037_194_MPL_46_002-048 | 42 | sent 16 Nov ~17:4x UTC; no checkpoint in 7 hours | all |

Packages with hourly checkpoints that have sent none after about seven hours are almost certainly dead (frozen
account or lost session). **For the user:** are P021, P030, P032 and P037 still running anywhere? If not, their
folders go back from packages_done/ to packages/ to be sent again (160 scans). P033's 14 scans go in a small package.

## 3. Split for tomorrow (the user's routing)

1. **Claude second pass of the Pro packages** (70 finals, 2,923 scans; minus the 390 pages of the Longue Marche core
   already done).
   - Text against the scans, with Hua's text as a second witness where it exists.
   - Read and organize Pro's notes for the field experts: which notes bear on which runs and prompts.
   - Order as in SECOND_PASS_PLAN_20261115.md section 6: what nobody has seen first; the Longue Marche neighbourhood
     (141-152) early. In chunks of whole packages.
   - Who: Claude Opus 5.5 at effort max for the text (as for the Longue Marche core). The notes part goes to the field
     expert of the subject or an intake agent. On the fresh account, after the user's word on the agents and the
     budget.
   - **Ready (17 Nov 03:01 UTC).** `second_pass/make_second_pass.py PKG` builds the block prompts for every returned
     final: 71 packages, 3,541 scans, of which 65 packages remain after the Longue Marche core. What it now does:
     - renders the images again from the source PDFs where a package's scans zip is gone (the packages of 11-12 Nov);
       the result is byte-identical to the original images, checked on cote 142, scan 1;
     - finds returns that were unpacked one level deeper;
     - orders pages by the package's cote order;
     - names a second Pro run of the package (chat B) as a further witness;
     - names the package's edition matters (`second_pass/edition_matters_20261117/<PKG>.md`: 495 items in 50 files,
       from the follow-ups reader), with a method step for them.

     Backups: make_second_pass_before_edition_matters_20261117.py and make_second_pass_before_render_20261117.py. The
     images of MPL_146_100-134 were rendered as the test (img/MPL_146_100-134, 99 files, 39 MB).
   - **Built 03:05-03:11 UTC** (`second_pass/build_all_second_pass_20261117.py`; log `BUILD_ALL_20261117.log`): the
     block prompts and images of all 65 remaining packages, with 0 failures. That is 202 new prompts (225 in all, 133
     of them naming edition matters) and 10,623 images (every page has its three), 5.1 GB.
2. **Pro second pass with commentary for the Codex-web material** (137 units, 1,060 scans), with the template of
   section 4.2 of the plan (second_pass_pro_20261114/SECOND_PASS_CODEX_NOTES_TEMPLATE.md):
   - the Codex text checked against the ink, Hua's text as a second witness;
   - the research notes a first-pass Pro package writes, with the cote's context packet and the newest headline results;
   - large chunks: about 90-135 scans per prompt, so about 9-12 prompts.
   - Whether the packages of second_pass_pro_20261114/ are built for this route: to check before sending.
3. **The two-witness Pro packages built on 14 Nov (S001-S029, for Pro first passes)** are superseded for the Pro
   packages by item 1. They stay in their folder in case the user prefers Pro for part of it.
