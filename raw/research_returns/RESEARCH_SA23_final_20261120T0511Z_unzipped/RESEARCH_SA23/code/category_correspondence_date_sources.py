"""Retrieve and preserve public sources for the specific cote-1 dating inquiry.

This is a source-retrieval and text-location aid, not a proof that missing words
or catalogue entries establish the nonexistence of correspondence.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
from urllib.request import urlopen
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("Guichardet2004_Schwartz_archives", "https://smf.emath.fr/system/files/filepdf/Gaz-100.pdf"),
    ("Dieudonne1989_early_work", "https://csg.igrothendieck.org/wp-content/uploads/2024/06/GrothDieud89scan.pdf"),
    ("Schneps_chapter3", "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Mathematics/chap3.pdf"),
    ("Grothendieck_Serre_English", "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/GS.pdf"),
    ("Dieudonne_archive_11J", "https://www.academie-sciences.fr/pdf/dossiers/fonds_pdf/11J_Jean_Dieudonne.pdf"),
    ("Weyl_ETH_findingaid", "https://doi.org/10.3929/ethz-a-000310478"),
]

def fetch(item):
    key, url = item
    try:
        with urlopen(url, timeout=28) as response:
            content = response.read()
            final_url = response.geturl()
            status = response.status
            content_type = response.headers.get('Content-Type', '')
        is_pdf = content.startswith(b"%PDF")
        suffix = ".pdf" if is_pdf else ".html"
        destination = ROOT / "notes" / ("category_date_" + key + suffix)
        destination.write_bytes(content)
        lines = [
            f"KEY {key}", f"REQUESTED {url}",
            f"FINAL {final_url}", f"STATUS {status}",
            f"TYPE {content_type}",
            f"BYTES {len(content)}",
            f"SHA256 {hashlib.sha256(content).hexdigest()}",
            f"SAVED {destination}",
        ]
        if is_pdf:
            text_path = destination.with_suffix(".txt")
            extraction = subprocess.run(['pdftotext', '-layout', str(destination), str(text_path)], text=True, capture_output=True)
            lines.extend([f"PDFTOTEXT_STATUS {extraction.returncode}",
                          f"PDFTOTEXT_STDERR {extraction.stderr!r}", f"TEXT {text_path}"])
        return "\n".join(lines)
    except Exception as exc:
        return f"KEY {key}\nREQUESTED {url}\nFAILED {type(exc).__name__}: {exc}"

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=6) as pool:
        for result in pool.map(fetch, SOURCES):
            print(result)
            print()
