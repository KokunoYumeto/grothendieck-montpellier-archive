"""Version-2 metadata of hexagon:2611.01018 (HNAM) from version 1's and the v2 files of ae2754d9 (Claude Fable 5.2 at
effort max), rechecked by a25c2acb (Claude Opus 5.5 at effort high); main session 329fb1e6, 25 Nov 2026."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")


def text(name):
    return open(name, encoding="utf-8").read().strip()


m = json.load(open("HEXAGON_METADATA_HNAM.json", encoding="utf-8"))
m["abstract"] = re.sub(r"\s+", " ", text("v2/ABSTRACT.txt"))
m["comments"] = text("v2/COMMENTS_FIELD.txt")
src = text("v2/PROVENANCE_V2_SENTENCE.txt").split("\n\n")
v2_para = src[0].strip()
new_sentence = src[1].split("now reads: ", 1)[1].strip()
old_sentence = ("Lagarias-Odlyzko 1977 and Boppana-Hastad-Zachos 1987 were not opened and are used as quoted by Rojas, by "
                "OpenAI's preprint on factorization, and by Pak-Robichaux.")
p = m["provenance"]
assert p.count(old_sentence) == 1, "old sentence not found exactly once"
p = p.replace(old_sentence, new_sentence)
key = "Where the records are."
assert key in p
p = p.replace(key, v2_para + "\n\n" + key)
m["provenance"] = p
assert len(m["comments"]) <= 2000, len(m["comments"])
json.dump(m, open("HEXAGON_METADATA_HNAM_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in m.items() if isinstance(v, str)})
