#!/usr/bin/env python3
"""Download the opened primary sources needed for Part B.

The manifest contains public URLs actually opened/discovered during this run.
Existing downloads are retained. The JSON receipt records bytes and SHA256.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "B_Ancona_1806.03216.tar": "https://arxiv.org/src/1806.03216",
    "B_Broe_2608.28651.tar": "https://arxiv.org/src/2608.28651",
    "B_Mumford_1969.pdf": "https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969e--0-cycles-Euclid.pdf",
    "B_Kleiman_1968.pdf": "https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf",
    "B_Kleiman_1994.pdf": "https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische1994.Kleiman.Standard.Conjectures.pdf",
    "B_Kahn_2003.pdf": "https://webusers.imj-prg.fr/~bruno.kahn/preprints/cell-ASENS.pdf",
    "B_CeresaCollino_1983.pdf": "https://msp.org/pjm/1983/105-2/pjm-v105-n2-p04-s.pdf",
    "B_Bloch_2010_excerpt.pdf": "https://assets.cambridge.org/97805211/18422/excerpt/9780521118422_excerpt.pdf",
    "B_Broe_2026.pdf": "https://arxiv.org/pdf/2608.28651",
    "B_Geisser_2010.pdf": "https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p06-p.pdf",
    "B_Greenberg_1966.pdf": "https://www.numdam.org/item/PMIHES_1966__31__59_0.pdf",
    "B_RamisRuget_1970.pdf": "https://www.numdam.org/item/PMIHES_1970__38__77_0.pdf",
    "B_Pink_2000.pdf": "https://people.math.ethz.ch/~pink/ftp/EP.pdf",
    "B_Crew_1984.pdf": "https://www.numdam.org/item/CM_1984__52_1_31_0.pdf",
    "B_Milne_LEC.pdf": "https://www.jmilne.org/math/CourseNotes/LEC.pdf",
    "B_Suzuki_1803.09291.tar": "https://arxiv.org/src/1803.09291",
    "B_Milne_ADT.pdf": "https://www.jmilne.org/math/Books/ADTnot.pdf",
    "B_ILO_GTG.pdf": "https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/GTG/GTG.pdf",
    "B_Raynaud_1970.pdf": "https://www.numdam.org/item/PMIHES_1970__38__27_0.pdf",
    "B_DeligneMilne_1982.pdf": "https://www.jmilne.org/math/xnotes/tc2022.pdf",
    "B_BhattMathew_1807.04725.tar": "https://arxiv.org/src/1807.04725",
    "B_CisinskiDeglise_0912.2110.tar": "https://arxiv.org/src/0912.2110",
    "B_KatoSaito_math0402010.tar": "https://arxiv.org/src/math/0402010",
    "B_ContouCarrere_2013.pdf": "https://www.numdam.org/item/RSMUP_2013__130__1_0.pdf",
    "B_Gabber_1994.pdf": "https://link.springer.com/content/pdf/10.1007/BF02773001.pdf",
    "B_Fujiwara_1995.pdf": "https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-95-08002-8",
}


def download(item):
    name, url = item
    target = ROOT / "literature" / name
    start = time.perf_counter()
    try:
        existed = target.exists()
        if not existed:
            data = urllib.request.urlopen(url, timeout=45).read()
            target.write_bytes(data)
        data = target.read_bytes()
        valid = not name.endswith(".pdf") or data.lstrip().startswith(b"%PDF")
        return {"filename": name, "url": url, "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "retained_existing": existed,
                "seconds": round(time.perf_counter() - start, 6), "status": "ok" if valid else "invalid_pdf_html_response"}
    except Exception as exc:
        return {"filename": name, "url": url, "status": "error",
                "error": str(exc), "seconds": round(time.perf_counter() - start, 6)}


if __name__ == "__main__":
    (ROOT / "literature").mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=5) as pool:
        receipts = list(pool.map(download, SOURCES.items()))
    output = json.dumps(receipts, indent=2)
    (ROOT / "logs" / "B_source_downloads.json").write_text(output + "\n")
    print(output)
