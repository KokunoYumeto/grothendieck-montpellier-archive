"""Archive the primary sources used in the independent C.6 audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib, json, subprocess, time, urllib.request

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "MilneSVp22": "https://www.jmilne.org/math/articles/SVp22.pdf",
    "Noot2006": "https://irma.math.unistra.fr/~noot/publications/pp-jrms.pdf",
    "DokchitserDokchitser2024": "https://discovery.ucl.ac.uk/id/eprint/10205744/1/weil2-ems.pdf",
    "OpenAIRationality2026": "https://raw.githubusercontent.com/openai/math/main/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf",
    "MadapusiRationality2026": "https://keerthimadapusi.com/assets/ai-notes/milne-rationality/milne-rationality.pdf",
    "SerreTate1968": "https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf",
    "VanDobbenDeBruyn2020": "https://epiga.episciences.org/6931/pdf",
    "Fontaine1994VIII": "https://www.numdam.org/item/AST_1994__223__321_0.pdf",
    "Ochiai1999": "https://www.ochiai.math.sci.titech.ac.jp/lind.pdf",
    "SaitoGaloisSurvey": "https://www.ms.u-tokyo.ac.jp/~t-saito/pp/suams.pdf",
    "Laskar2013Hyperkahler": "https://archive.mpim-bonn.mpg.de/3706/1/preprint_2013_11.pdf",
    "Serre1970LocalFactors": "https://www.college-de-france.fr/media/jean-pierre-serre/UPL7750118224972622059_Serre_facteurs_locaux.pdf",
    "LuZheng2019": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/48/9290-1801.03221v5.pdf",
    "AyoubNearbyCycles2007": "https://www.math.uzh.ch/user/ayoub/PDF-Files/Leiden.pdf",
    "CadoretTamagawaRamification": "https://webusers.imj-prg.fr/~anna.cadoret/Trivial.pdf",
    "Saito2003Weights": "https://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2r.pdf",
    "Serre1993Course": "https://www.college-de-france.fr/sites/default/files/media/document/2023-03/1992-1993_serre.pdf",
}

HTML_SOURCES = {
    "AyoubAuthorPage2026": "https://www.math.uzh.ch/user/ayoub/",
}

def fetch(item):
    name, url = item
    target = ROOT / "sources" / (name + ".pdf")
    started = time.time()
    if not target.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research source verification)"})
        data = urllib.request.urlopen(request, timeout=90).read()
        if not data.startswith(b"%PDF"):
            raise ValueError((url, "not a PDF"))
        target.write_bytes(data)
    subprocess.run(["pdftotext", "-layout", str(target), str(target.with_suffix(".txt"))], check=True)
    data = target.read_bytes()
    return {"name":name, "url":url, "bytes":len(data), "sha256":hashlib.sha256(data).hexdigest(), "seconds":time.time()-started}

def fetch_html(item):
    name, url = item
    target = ROOT / "sources" / (name + ".html")
    started = time.time()
    if not target.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research source verification)"})
        target.write_bytes(urllib.request.urlopen(request, timeout=90).read())
    data = target.read_bytes()
    return {"name":name, "url":url, "bytes":len(data), "sha256":hashlib.sha256(data).hexdigest(), "seconds":time.time()-started}

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        records = list(executor.map(fetch, SOURCES.items()))
        records.extend(executor.map(fetch_html, HTML_SOURCES.items()))
    output = json.dumps(records, indent=2)
    (ROOT / "fetch_c6_sources_output.json").write_text(output + "\n")
    print(output)
