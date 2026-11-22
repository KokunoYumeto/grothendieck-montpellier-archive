# Private LuaLaTeX compatibility notes

The system TeX tree had no configured filename databases or LuaLaTeX format. The build uses a private generated format and direct filesystem searching. Missing public CTAN dependencies were installed into that private tree; no system package or access-control file was modified.

During diagnosis the optional lfs readability/writability fast path in four privately downloaded lualibs Lua files was disabled in favor of the library's own IO fallback. The successful build also requires a relative TEXMFCACHE path in this runtime. These changes were made together during troubleshooting; the fast path has not been isolated as the sole cause of the initial failure. The explicit relative cache setting and generated AMS font map are retained in build_paper.py.

The first checkpoint preserves the failed build output. Later build and visual-QA JSON files record successful outputs with the actual PDF hash.
