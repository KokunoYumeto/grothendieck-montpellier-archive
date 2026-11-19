#!/usr/bin/env python3
"""Reproduce this agent's primary-source downloads (read-only HTTP GETs)."""
from pathlib import Path
import argparse
import hashlib
import subprocess
import urllib.request
from time import perf_counter

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "grothendieck_hilbert1961": "https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf",
    "grothendieck_hilbert_erratum1962": "https://www.numdam.org/item/SB_1961-1962__7__302_1.pdf",
    "dejong1996_alterations": "https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf",
    "kleiman_picard2005v1": "https://arxiv.org/pdf/math/0504020v1",
    "cheng_ji_larson_olander2021": "https://chngr.github.io/assets/theorem-of-the-base.pdf",
    "elkik1973": "https://numdam.org/item/10.24033/asens.1258.pdf",
    "carvajal_stabler2023": "https://content.algebraicgeometry.nl/2023-6/2023-6-025.pdf",
    "milne_abelian2022": "https://www.jmilne.org/math/xnotes/AVs.pdf",
    "illusie1972_torsors": "https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/ce/24/ce243c31-2953-498e-92cb-c8b2e70d207d/i_illusie-64.pdf",
    "illusie_halifax_errata": "https://www.imo.universite-paris-saclay.fr/~luc.illusie/ErrHalifax.pdf",
    "milne_jacobians2021": "https://www.jmilne.org/math/xnotes/JVs.pdf",
    "totaro_moving": "https://www.math.ucla.edu/~totaro/papers/public_html/moving.pdf",
    "huybrechts_thomas_v2": "https://arxiv.org/pdf/0805.3527v2",
    "varbaro2009_published": "https://www.matteovarbaro.com/Connectedness%20properties%20of%20Groebner%20deformations.pdf",
    "boutot1978_introduction": "https://link.springer.com/content/pdf/bfm:978-3-540-35936-4/1",
    "wlodarczyk2005": "https://www.math.purdue.edu/~wlodarcz/singularities/Resolution.pdf",
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
    started = perf_counter()
    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="*", choices=tuple(SOURCES))
    args = parser.parse_args()
    folder = ROOT / "sources"
    folder.mkdir(exist_ok=True)
    for name in args.names or SOURCES:
        source_started = perf_counter()
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
        print(f"{name} runtime_seconds: {perf_counter()-source_started:.6f}")
    print(f"Total runtime seconds: {perf_counter()-started:.6f}")

if __name__ == "__main__":
    main()
