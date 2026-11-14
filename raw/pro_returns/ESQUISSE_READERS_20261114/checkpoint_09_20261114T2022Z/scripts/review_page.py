"""Compact entry point for a reviewer's explicit, completed image inspection.

Calling commit certifies that the reviewer has just inspected both image halves
listed in the packet. It has no default review observations and cannot be used
to mark a page reviewed merely because the files exist.
"""
from pathlib import Path
import json, subprocess, sys

def commit(key, *, notes, patches, macro, diffs, full,
           difference_overrides=None, macro_overrides=None, additional=None):
    edition=Path(__file__).resolve().parent.parent
    root=edition.parent
    packet=json.loads((root/"review_packets"/f"{key}.json").read_text())
    if len(notes)!=len(packet["note_items"]):
        raise ValueError(f"{key}: {len(notes)} explicit note observations supplied for {len(packet['note_items'])} note targets")
    for name,value in [("macro",macro),("diffs",diffs),("full",full)]:
        if not isinstance(value,str) or not value.strip():raise ValueError(f"{name} requires an explicit observed result")
    observations={}
    for note,observation in zip(packet["note_items"],notes):
        if isinstance(observation,str):
            if not observation.strip():raise ValueError("An empty note observation is not a review")
            observation={"image_reading":observation,"reason":observation}
        observations[note["item_id"]]=observation
    review={"key":key,"inspected_images":packet["required_images"],
        "inspection_statement":full,"full_text_confirmation":full,
        "patches":patches,"confirm_all_original_macros":True,
        "macro_confirmation_reason":macro,"macro_observations":macro_overrides or {},
        "note_observations":observations,"confirm_all_differences":True,
        "differences_confirmation_reason":diffs,"difference_outcomes":difference_overrides or {},
        "additional_decisions":additional or [],"finalize":True}
    path=edition/"reviews"/f"{key}.json";path.parent.mkdir(parents=True,exist_ok=True)
    serialized=json.dumps(review,ensure_ascii=False,indent=2)+"\n"
    if path.exists() and path.read_text()!=serialized:
        # Preserve an earlier explicit judgment when further image evidence
        # changes a classification or reading. The active TSV is regenerated,
        # while this history retains the superseded declaration and rows.
        history=edition/"reviews/history";history.mkdir(parents=True,exist_ok=True)
        serial=1
        while (history/f"{key}_review_{serial:03d}.json").exists():serial+=1
        (history/f"{key}_review_{serial:03d}.json").write_text(path.read_text())
        from audit_inventory import read_tsv,write_tsv
        for name in ["CHECK_DECISIONS.tsv","DIFFERENCES_OUTCOMES.tsv"]:
            record=edition/name
            if record.exists():
                rows=[r for r in read_tsv(record) if r.get("key")==key]
                if rows:write_tsv(history/f"{key}_{serial:03d}_{name}",rows,list(rows[0]))
    path.write_text(serialized)
    result=subprocess.run([sys.executable,str(edition/"scripts/audit_apply.py"),str(path),"--work",str(root)],
                          check=True,capture_output=True,text=True)
    print(result.stdout.strip())
    return json.loads(result.stdout)
