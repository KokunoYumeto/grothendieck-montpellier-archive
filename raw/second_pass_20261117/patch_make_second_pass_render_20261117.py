"""17 Nov 2026 (~02:5x UTC): make make_second_pass.py work for every returned Pro final, not only the first ones.
- returns unpacked one level deeper (returns/<PKG>_unzipped/<PKG>/pages) are found;
- pages are ordered by the package's cote order (MANIFEST), then by scan;
- where the package's scans zip is gone (the packages of 11-12 Nov), the images are rendered again from the source PDFs
  exactly as the package builder made them (grothendieck_archive_tools_20261110/build_package.py page_image; autocontrast
  cutoff 1; unsharp mask r2 p120 t3; halves with 80 px overlap, 60 for spreads; JPEG q88);
- a second Pro run of the same package (returns/<PKG>_chatB_unzipped) is named in the prompt as a further witness.
usage: python -I -B patch_make_second_pass_render_20261117.py"""
import pathlib

M = pathlib.Path(__file__).resolve().parent / "make_second_pass.py"
m = M.read_text(encoding="utf-8")
if "render_missing" in m:
    raise SystemExit("already patched")


def rep(a, b):
    global m
    assert m.count(a) == 1, (m.count(a), a[:70])
    m = m.replace(a, b)


rep('ret = T / "returns" / f"{pkg}_unzipped"\n',
    '''ret = T / "returns" / f"{pkg}_unzipped"
if not (ret / "pages").is_dir() and (ret / pkg / "pages").is_dir():  # 17 Nov 2026: some returns unpacked one level deeper
    ret = ret / pkg
RET = ret.relative_to(T).as_posix()
MAN = T / "packages_work" / pkg / "MANIFEST.json"
TOOLS = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_tools_20261110")


def manifest_pdfs():
    """cote -> source PDF, in the package's order (both manifest formats: the multi-cote 'files' list, or one cote)."""
    import json
    if not MAN.exists():
        return {}
    man = json.loads(MAN.read_text(encoding="utf-8"))
    if "files" in man:
        return {str(f["cote"]): pathlib.Path(f["source_pdf"]) for f in man["files"]}
    return {str(man["cote"]): pathlib.Path(man["source_pdf"])}


PDFS = manifest_pdfs()


def cote_scan(p):
    """(cote, scan number) of a page file: <PKG>_<cote>_scanNNN.tex, or <PKG>_scanNNN.tex for a one-cote package."""
    key = p.stem[len(pkg) + 1:]
    if "_scan" in key:
        c, n = key.rsplit("_scan", 1)
        return c, int(n)
    return (next(iter(PDFS)) if len(PDFS) == 1 else ""), int(key[len("scan"):])


def page_order(p):
    c, n = cote_scan(p)
    order = list(PDFS)
    return (order.index(c) if c in order else len(order), c, n)


def render_missing(chunk, img):
    """The builder's images again, from the source PDF (see the docstring of the patch of 17 Nov 2026)."""
    import tempfile
    from PIL import ImageFilter, ImageOps
    sys.path.insert(0, str(TOOLS))
    from build_package import page_image
    with tempfile.TemporaryDirectory() as tmp:
        for p in chunk:
            if all((img / f"{p.stem}{suf}.jpg").exists() for suf in ("", "_a", "_b")):
                continue
            c, n = cote_scan(p)
            ctmp = pathlib.Path(tmp) / f"c_{c}_{n}"
            ctmp.mkdir()
            im = page_image(PDFS[c], n, ctmp)
            if im is None:
                print("  no image in the PDF for", p.name)
                continue
            im = ImageOps.autocontrast(im, cutoff=1).filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
            w, h = im.size
            if w > h:
                p1, p2 = im.crop((0, 0, w // 2 + 60, h)), im.crop((w // 2 - 60, 0, w, h))
            else:
                p1, p2 = im.crop((0, 0, w, h // 2 + 80)), im.crop((0, h // 2 - 80, w, h))
            im.save(img / f"{p.stem}.jpg", quality=88)
            p1.save(img / f"{p.stem}_a.jpg", quality=88)
            p2.save(img / f"{p.stem}_b.jpg", quality=88)


''')
rep('pages = sorted((ret / "pages").glob(f"{pkg}_*scan*.tex"))',
    'pages = sorted((ret / "pages").glob(f"{pkg}_*scan*.tex"), key=page_order)')
rep('''    with zipfile.ZipFile(zp) as z:
        names = set(z.namelist())
        for p in chunk:  # 17 Nov 2026: each image is named as its page file
            for suf in ("", "_a", "_b"):
                name = f"{p.stem}{suf}.jpg"
                if name in names and not (img / name).exists():
                    (img / name).write_bytes(z.read(name))
''', '''    if zp.exists():
        with zipfile.ZipFile(zp) as z:
            names = set(z.namelist())
            for p in chunk:  # 17 Nov 2026: each image is named as its page file
                for suf in ("", "_a", "_b"):
                    name = f"{p.stem}{suf}.jpg"
                    if name in names and not (img / name).exists():
                        (img / name).write_bytes(z.read(name))
    else:  # 17 Nov 2026: the scans zips of the packages of 11-12 Nov are gone: render from the source PDFs
        render_missing(chunk, img)
''')
rep('files = "\\n".join(f"  - returns/{pkg}_unzipped/pages/{p.name}" for p in chunk)',
    'files = "\\n".join(f"  - {RET}/pages/{p.name}" for p in chunk)')
rep("- Its notes, doubts and inventory: `returns/{pkg}_unzipped/{pkg}_notes.md`",
    "- Its notes, doubts and inventory: `{RET}/{pkg}_notes.md`")
rep('''em_step = (''', '''cb = T / "returns" / f"{pkg}_chatB_unzipped"  # 17 Nov 2026: a second Pro run of the same package, if any
if not (cb / "pages").is_dir() and (cb / pkg / "pages").is_dir():
    cb = cb / pkg
cb_line = ("\\n- A second Pro run of the same package (chat B), as a further witness: "
           f"`{cb.relative_to(T).as_posix()}/pages/`, with the same file names. Where the two runs differ, the image "
           "decides; a difference that neither the image nor the context settles goes in the unresolved places.") \\
    if (cb / "pages").is_dir() else ""
em_step = (''')
rep("`{done[0].relative_to(T).as_posix()}/PROMPT.md`.{em_line}", "`{done[0].relative_to(T).as_posix()}/PROMPT.md`.{em_line}{cb_line}")
M.write_text(m, encoding="utf-8", newline="\n")
print("patched", M.name)
