"""Write the README, link RESEARCH_SA13 into TO_SEND/PRO/1_Archive_research_by_topic, pack it, add the ORDER.md line
(agent a84c887cf408574ed, Claude Opus 5.5 at effort max, 19 Nov 2026)."""
import os, subprocess, sys
DOC = r'C:\Users\user\Documents'
B = os.path.join(DOC, r'pro_prompt_builds\RESEARCH_SA13')
files = ['PROMPT.md', 'RESEARCH_SA13_study.zip', 'RESEARCH_SA13_transcriptions.zip', 'RESEARCH_SA13_literature.zip']
sizes = {f: os.path.getsize(os.path.join(B, f)) for f in files}
words = len(open(os.path.join(B, 'PROMPT.md'), encoding='utf-8').read().split())
readme = f"""# RESEARCH_SA13: research prompt for GPT-6 Astra (ChatGPT Pro mode)

Built 2026-11-19 about 15:10 UTC by Claude Opus 5.5 at effort max (agent a84c887cf408574ed, the SA13 lead of sweep 3, wave 1),
at the main session's word (19 Nov 2026), from `results_register/horizontal/sweep3/SA13/` and the builder
`results_register/horizontal/sweep3/_tools_a84c887c/build_research_sa13.py`.

- **What it is:** Grothendieck's SGA working papers (cotes 27-42). Main question A.1: his injective-dimension theorem of the 1965
  SGA 5 draft (33/170-178) with his Lazard-type question (33/174). Then: the strong form of Théorème 7.1 of the Griffiths draft
  (36/10-27); Ker(Γ → NS(X₀)) = Z/d (36/71); the "théorème de 1/2 continuité" (27/28-37); the étale scheme of irreducible
  components (41); networks of local rings (42); tori of the Cremona group (28:5); four smaller steps.
- **Account:** the one the main session assigns.
- **What to send:** all files of the send folder `TO_SEND/PRO/1_Archive_research_by_topic/15_SA13_SGA_working_papers_cotes_27-42_night/`
  (PROMPT.md and one ZIP after packing), no text.
- **Lint:** `push_rule_pro_prompts.py --lint-math`: files: 1 failing lint: 0; `paper_completeness_lint.py`: files: 1 failing: 0.
- **Sizes:** PROMPT.md {sizes['PROMPT.md']:,} bytes ({words:,} words); RESEARCH_SA13_study.zip 15 files, {sizes['RESEARCH_SA13_study.zip']/1e6:.2f} MB;
  RESEARCH_SA13_transcriptions.zip 44 files, {sizes['RESEARCH_SA13_transcriptions.zip']/1e6:.2f} MB; RESEARCH_SA13_literature.zip 7 files,
  {sizes['RESEARCH_SA13_literature.zip']/1e6:.2f} MB.
- **ZIPs:** LaTeX and text only; each has `MANIFEST.tsv` at its root (path, origin, SHA256). No scans.
"""
open(os.path.join(DOC, r'pro_prompt_builds\RESEARCH_SA13.README.md'), 'w', encoding='utf-8').write(readme)

SEND = os.path.join(DOC, r'TO_SEND\PRO\1_Archive_research_by_topic')
name = '15_SA13_SGA_working_papers_cotes_27-42_night'
order = open(os.path.join(SEND, 'ORDER.md'), encoding='utf-8').read()
if '\n15. ' in order or name in order:
    sys.exit('number 15 already taken in ORDER.md: choose the next number by hand')
d = os.path.join(SEND, name)
os.makedirs(d, exist_ok=False)
for f in files:
    os.link(os.path.join(B, f), os.path.join(d, f))
r = subprocess.run([sys.executable, '-I', '-B', os.path.join(DOC, r'claude_tools\prompts\pack_one_zip.py'), d],
                   capture_output=True, text=True, encoding='utf-8')
print(r.stdout[-1500:], r.stderr[-800:])
line = ("15. `15_SA13_SGA_working_papers_cotes_27-42_night`: Grothendieck's SGA working papers: his injective-dimension "
        "theorem of the 1965 SGA 5 draft (33/172, the 2n bound, with his Lazard question 33/174); the strong form of 7.1 "
        "of the Griffiths draft behind SGA 7 XX-XXI; Ker(Γ → NS) = Z/d (36/71); the 1/2-continuity theorem (cote 27); "
        "the étale scheme of components (41); networks of local rings (42); Cremona tori (28).\n")
with open(os.path.join(SEND, 'ORDER.md'), 'a', encoding='utf-8') as fo:
    if not order.endswith('\n'):
        fo.write('\n')
    fo.write(line)
print(sorted(os.listdir(d)), [os.path.getsize(os.path.join(d, x)) for x in sorted(os.listdir(d))])
