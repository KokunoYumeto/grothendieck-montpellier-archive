# Prepared mathematical workbench

This folder contains the current Part A papers, their editable sources and PDFs, statement tables, individual check events, citations, and verification records. The papers concern finite-field isogeny descent, tori in apposition, and symmetric-group lattices over local rings. The complete local-ring classification remains open. Parts B and C have not yet begun.

## Reading and rebuilding

Each project in `work/pending-A*/v0/` is self-contained. Read its main.pdf or edit main.tex and the local inputs; BUILD.md gives the exact commands. Checks are distinguished as targeted proof checks, statement-only same-model reconstructions, and finite computations. No human verification is claimed. The independent records in `checks/` are preserved as evidence, including the development of earlier partial checks.

## Filing status

The structure follows format1 of the mathematics-workbenches registry as far as possible before filing. The pending names are temporary folder labels, not permanent workbench numbers. No WB number, permanent statement tag, deposit commit, or public deposit has been invented. On filing, allocate numbers in the central registry, replace the temporary folder names and statement tags, print the final manifest identifier and commit in the papers, rebuild, verify the final manifests, and write DEPOSITED.md only after deposition. No version in this prepared tree is marked deposited.

All Part A papers use the requested algebraic-groups-and-representations-workbench destination. The central records address is https://github.com/KokunoYumeto/mathematics-workbenches . No external repository was modified. Third-party works are cited and linked; no copies of them or of the uploaded source archive are included. Our text and programs are dedicated to CC0 1.0.

### Distinguished-monic symbolic certificate

Run `python programs/distinguished_monic_examples.py` with Python3 and SymPy from this workbench directory. Expected output/certificate: PASS, the exact root identity and involution/mesh identities for p2,F=t³+2t+4, plus the degree3 residue-field check. The generated certificate is checks/A133_distinguished_monic_example_certificate.json. This is an identity certificate only; the full categorical nonvanishing proof is in the paper.
