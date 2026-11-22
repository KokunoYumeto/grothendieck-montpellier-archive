"""Check the current public publisher and the archive linked by IMS itself."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
from ROOT_Pfluger_public_route import fetch

targets = {
    "current_publisher": "https://informaticsjournals.com/",
    "ims_linked_archive": "https://informaticsjournals.co.in/index.php/jims/issue/archive",
}

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows = list(pool.map(fetch, targets.items()))
    root = Path(__file__).resolve().parents[1]
    (root / "logs/ROOT_Pfluger_publisher_followup.json").write_text(json.dumps(rows, indent=2) + "\n")
    for row in rows:
        short = {k: v for k, v in row.items() if k not in {"text", "response_text", "links"}}
        if "text" in row:
            short["text_prefix"] = row["text"][:6000]
            short["links"] = row["links"]
        print(json.dumps(short, indent=2))
