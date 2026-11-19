# Depth scan of the RESEARCH_SA09 paper: for each numbered statement (\paragraph{A1.1 (...)}), the words of its statement and
# of the proof environments before the next statement. a34c04448e8299803 (Claude Opus 5.5 at effort max), 19 Nov 2026.
# Usage: python -I -B proof_depth_scan.py <sections folder>
import re, sys, glob, os
sys.stdout.reconfigure(encoding='utf-8')
S = sys.argv[1]
HEAD = re.compile(r'\\paragraph\{([AB]\d+\.\d+)\s*\(([^)]*)\)')
PROOF = re.compile(r'\\begin\{proof\}(.*?)\\end\{proof\}', re.S)
for f in sorted(glob.glob(os.path.join(S, '*.tex'))):
    t = open(f, encoding='utf-8').read()
    heads = list(HEAD.finditer(t))
    if not heads:
        continue
    print('==', os.path.basename(f))
    for k, m in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else len(t)
        block = t[m.end():end]
        p0 = block.find('\\begin{proof}')
        sw = len((block if p0 < 0 else block[:p0]).split())
        proofs = PROOF.findall(block)
        print('  %-6s %-48s stmt %4d w  proofs %d: %5d w' % (m.group(1), m.group(2)[:48], sw, len(proofs),
                                                         sum(len(p.split()) for p in proofs)))
