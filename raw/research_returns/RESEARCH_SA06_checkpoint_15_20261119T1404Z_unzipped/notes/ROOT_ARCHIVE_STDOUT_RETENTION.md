# Complete command-output retention in checkpoint 14 and the final archive

The packaging program formerly retained `.out` files under `code/` and excluded `.out` elsewhere as TeX auxiliary output. A concrete audit of the new C.3be builder showed that the owner saves full compiler stdout under `agents/frobenius/output/*_build.out`, alongside the retained JSON timing record and final `.log`. The directory-based rule would omit those full pass outputs. Similar earlier owner outputs remain present in the workspace.

We changed `code/package_work.py` to inspect `.out` content. Empty files and files consisting only of Hyperref BOOKMARK/auxiliary commands remain excluded as generated TeX auxiliaries. All other `.out` files are retained, regardless of directory. This conservatively preserves scientific certificates, command stdout, intermediate build warnings, and their repairs. No earlier immutable archive is changed. Checkpoint 14 and the final archive include the formerly omitted stdout files that are still present.

This correction concerns completeness of retained output, not mathematical results or progress-clock movement. It does not recreate any missing output or assert that a command was rerun.
