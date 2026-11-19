#!/usr/bin/env python3
"""Reproduce this agent's primary-source downloads (read-only HTTP GETs)."""
from pathlib import Path
import argparse
import hashlib
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "bhatt_dejong2014": "https://www.numdam.org/item/10.24033/asens.2228.pdf",
    "kollar2016_local_picard": "https://content.algebraicgeometry.nl/2016-4/2016-4-022.pdf",
    "tate1968": "https://www.numdam.org/article/SB_1968-1969__11__95_0.pdf",
    "geisser2004": "https://arxiv.org/pdf/math/0404425",
    "flach_morin": "https://www.math.u-bordeaux.fr/~bmorin/flach-morin-169.pdf",
    "milne1994_corrected": "https://jmilne.org/math/xnotes/Seattle1.pdf",
    "milne2002_published": "https://arxiv.org/pdf/math/0103175",
    "milne2003_gerbes": "https://www.jmilne.org/math/articles/2003b.pdf",
    "kisin2017": "https://people.math.harvard.edu/~kisin/dvifiles/lr.pdf",
    "milne_adt2006": "https://www.jmilne.org/math/Books/ADTnot.pdf",
    "milne_cft2020": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
    "geisser_dedekind2004": "https://www2.rikkyo.ac.jp/web/geisser/Dedekind.pdf",
    "voevodsky2011": "https://www.math.ias.edu/vladimir/sites/math.ias.edu.vladimir/files/on_motivic_with_Zl_published.pdf",
    "vanhoften_sempliner2026": "https://polvanhoften2.github.io/Pol%20van%20Hoften%20and%20Jack%20Sempliner%20-%20The%20Hodge%20conjecture%20for%20CM%20abelian%20varieties.pdf",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="*", choices=tuple(SOURCES))
    args = parser.parse_args()
    folder = ROOT / "sources"
    folder.mkdir(exist_ok=True)
    for name in args.names or SOURCES:
        path = folder / f"{name}.pdf"
        if not path.exists():
            request = urllib.request.Request(SOURCES[name], headers={"User-Agent": "Research-source-verification/1.0"})
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read()
            if not data.startswith(b"%PDF"):
                raise ValueError(f"{name}: response is not a PDF")
            path.write_bytes(data)
        data = path.read_bytes()
        print(f"{name}\t{len(data)} bytes\tsha256={hashlib.sha256(data).hexdigest()}")
        text_path = path.with_suffix(".txt")
        subprocess.run(["pdftotext", "-layout", str(path), str(text_path)], check=True)

if __name__ == "__main__":
    main()
