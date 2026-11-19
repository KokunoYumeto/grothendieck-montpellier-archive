# Reproducing the LuaLaTeX build

The installed LuaHBTeX executable is version1.18.0 (TeX Live2025/dev/Debian). Its installed macro and font data are present, but the system has no `ls-R` databases or ready `lualatex.fmt`, and lacks several Lua font-loader data packages. We repaired this only within the current workspace.

From the `RESEARCH_SA09` directory, the working command is:

```sh
python code/tex_runtime.py lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA09_paper.tex
python code/tex_runtime.py bibtex RESEARCH_SA09_paper
python code/tex_runtime.py lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA09_paper.tex
python code/tex_runtime.py lualatex -interaction=nonstopmode -halt-on-error RESEARCH_SA09_paper.tex
```

Use the bibliography command appropriate to the master source if its bibliography route changes. With `-output-directory=DIR`, give BibTeX `DIR/RESEARCH_SA09_paper` instead. Run from the same working directory so section and bibliography paths resolve identically.

## If reconstructing the local runtime

The saved runtime tree is `tex-runtime/`. To recreate it from the available system TeX data and official CTAN data archives:

```sh
python code/tex_runtime_install.py > logs/tex_runtime_install.json
python code/tex_runtime.py --build-format > logs/tex-format-attempt.log
```

The installer reuses already downloaded archives, otherwise downloads the four official packages `luaotfload`, `lualibs`, `luatexbase`, and `lua-uni-algos` from the Princeton CTAN mirror. It installs only into `tex-runtime/texmf`. It builds a local `pdftex.map` from installed Latin Modern, AMS and rsfs maps. The wrapper sets the relevant TeX search/cache/output variables to workspace paths and removes database-only lookup from read-only system tree paths. It does not change a home directory, system package, system config, or system font cache.

The wrapper also sets `TEXMFOUTPUT` to the current deliverable root so the TeX engine's own restricted output handling permits its Lua font cache to be written inside the authorized workspace. It does not broaden filesystem sandbox permissions.

## Verification scope

`code/a2_a4_texcheck.py` builds only a temporary A2/A4 harness, with its stdout and statistics in `logs/a2_a4_texcheck.stdout.txt` and `logs/a2_a4_texcheck.json`. After BibTeX and the necessary reruns this syntax/layout test succeeded: 10 pages, zero warnings, zero undefined references, and zero overfull boxes. The final integrated manuscript must be compiled, checked and visually inspected separately; the harness is not the published PDF.

Initial failed attempts were: missing format; missing Lua font loader; cache-output configuration; missing `lua-uni-case`; missing PDF font maps. These were resolved in that order. Failed-run zero overflow counts are not successful checks. All helper programs and the latest outputs are saved. The finite mathematics certificates are independent of this typesetting environment.
