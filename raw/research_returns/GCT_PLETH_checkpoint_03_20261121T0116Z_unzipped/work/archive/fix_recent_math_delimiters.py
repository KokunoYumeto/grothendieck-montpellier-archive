from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
NAMES = ["FIVE_POINT_POWERS.md", "FIVE_POINT_COX_MAP.md",
         "GENERAL_FIBER_REVIEW.md", "OUTER4_FREE_MODULE_REVIEW.md"]

def repair_nested(text):
    stack, out, repairs = [], [], 0
    i = 0
    while i < len(text):
        token = text[i:i+2]
        if token in (r"\(", r"\["):
            if stack:
                stack.append(("nested", token))
                out.append("(" if token == r"\(" else "[")
                repairs += 1
            else:
                stack.append(("outer", token))
                out.append(token)
            i += 2
        elif token in (r"\)", r"\]"):
            assert stack, ("unmatched closer", i)
            role, opener = stack.pop()
            assert (opener, token) in ((r"\(",r"\)"),(r"\[",r"\]")), (opener,token,i)
            out.append(token if role == "outer" else (")" if token == r"\)" else "]"))
            i += 2
        else:
            out.append(text[i])
            i += 1
    assert not stack
    return "".join(out), repairs

def plain_pairs(text):
    result, stack = [], []
    i = 0
    while i < len(text):
        if text.startswith(chr(96)*3, i):
            j = text.find(chr(96)*3, i+3)
            assert j >= 0
            i = j+3
        elif text[i] == chr(96):
            j = text.find(chr(96), i+1)
            assert j >= 0
            i = j+1
        elif text[i:i+2] in (r"\(",r"\["):
            close = r"\)" if text[i:i+2] == r"\(" else r"\]"
            j = text.find(close, i+2)
            assert j >= 0
            i = j+2
        elif text[i] == "(":
            stack.append(i)
            i += 1
        elif text[i] == ")":
            if stack:
                start = stack.pop()
                if not stack:
                    result.append((start, i+1, text[start+1:i]))
            i += 1
        else:
            i += 1
    return result

for name in NAMES:
    path = ROOT/name
    text, nested = repair_nested(path.read_text())
    changes = []
    for start,end,inside in plain_pairs(text):
        if inside.startswith(("https:", "http:", "sandbox:")):
            continue
        if "\n" in inside or len(inside)>220 or r"\(" in inside or r"\[" in inside:
            continue
        mathematical = bool(re.search(r"\\[A-Za-z]+|[_^=]|[<>≥≤∈]", inside))
        mathematical |= bool(re.fullmatch(r"[A-Za-z](?:[0-9]+)?", inside))
        if mathematical and not re.search(r"\b(?:and|with|since|because|for|the|this|these|proof|source|file|see)\b", inside):
            changes.append((start,end, r"\("+inside+r"\)"))
    for start,end,new in reversed(changes):
        text = text[:start]+new+text[end:]
    text2, n2 = repair_nested(text)
    assert text2 == text and n2 == 0
    path.write_text(text)
    print(name, "nested repaired", nested, "plain math restored", len(changes),
          "inline pairs",text.count(r"\("),text.count(r"\)"))
    for _,_,inside in plain_pairs(text):
        if re.search(r"\\[A-Za-z]+|[_^=]",inside) and not inside.startswith(("https:","http:","sandbox:")):
            print("REVIEW REMAINDER",repr(inside))
