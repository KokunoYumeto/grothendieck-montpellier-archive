"""Content comparison of retired checkpoints with the surviving returns.

The retired folders are gone.  What survives of their content is (a) the verbatim output of my own read commands,
kept in this agent's transcript, and (b) one preserved manifest (handled separately).  For each range that a command
printed, the same range of the surviving file is compared as a string with the stored output.  Nothing is inferred
about lines that were not printed.  Read-only; own code; imports the standard library only.
"""
import json, pathlib, re, sys

T = pathlib.Path(sys.argv[1])
R = pathlib.Path(sys.argv[2])
calls, results = [], {}
for line in T.open(encoding='utf-8'):
    try:
        rec = json.loads(line)
    except ValueError:
        continue
    content = (rec.get('message') or {}).get('content')
    if not isinstance(content, list):
        continue
    for c in content:
        if not isinstance(c, dict):
            continue
        if c.get('type') == 'tool_use' and c.get('name') == 'Bash':
            calls.append((c['id'], c['input'].get('command', '')))
        elif c.get('type') == 'tool_result':
            body = c.get('content')
            if isinstance(body, list):
                body = ''.join(x.get('text', '') for x in body if isinstance(x, dict))
            results[c['tool_use_id']] = (body or '').replace('\r\n', '\n')


def outputs(*needles):
    return [results.get(i, '') for i, cmd in calls if all(n in cmd for n in needles)]


def lines(p):
    return p.read_bytes().decode('utf-8').replace('\r\n', '\n').rstrip('\n').split('\n')


def cut(ls, w):
    return [l.encode('utf-8')[:w].decode('utf-8', 'ignore') for l in ls] if w else ls


def test(label, path, a, b, w, *needles):
    ls = lines(path)
    b = len(ls) if b is None else min(b, len(ls))
    want = '\n'.join(x.rstrip() for x in cut(ls[a - 1:b], w)).strip()
    got = ['\n'.join(x.rstrip() for x in o.split('\n')) for o in outputs(*needles)]
    ok = any(want in o for o in got)
    scope = 'WHOLE FILE' if a == 1 and b == len(ls) and not w else 'lines %d-%d of %d%s' % (a, b, len(ls), ' (first %d bytes of each)' % w if w else '')
    print('%-9s %-44s %s' % ('SAME' if ok else ('DIFFERS' if got else 'NOOUTPUT'), label, scope))
    if not ok and got:
        miss = [a + i for i, l in enumerate(cut(ls[a - 1:b], w)) if l.strip() and not any(l.rstrip() in o for o in got)]
        print('          lines absent from the stored output:', len(miss), miss[:12])


