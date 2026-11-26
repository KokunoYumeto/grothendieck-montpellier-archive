# Filing preparation for format 1

The governing format is FORMAT.md, format 1 dated 22 November 2026, at
https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/FORMAT.md.
It was fetched and read on 23 November 2026. That source itself is not copied
into this package.

No permanent WB number or repository commit has been allocated. The owner
explicitly assigns the work number and permanent page when filing. Local
paper numbers and source IDs in these working records are therefore staging
identifiers, never fabricated permanent tags. No version is marked deposited.

After mathematical completion and allocation, each coherent paper is placed
under `work/WB-nnnn/v1/` with its standalone source and PDF, STATEMENTS.tsv,
CHECK_EVENTS.tsv, SOURCES.tsv, checks/, and MANIFEST.sha256. The paper's
recordurl is then replaced with the allocated permanent page. Paper 5 belongs
to the algebraic-cycles-and-motives workbench; the others belong to the
schemes-and-moduli workbench. Known comparison material is identified as such.

The current folder is a filing preparation, not a claim that permanent tags,
remote commits, or immutable deposit events already exist. A final manifest
will cover all version files except itself. Printing that same byte manifest
hash inside a file covered by it is self-referential; the filing record must
specify a detached identity page or an explicit normalized-hash convention
before adding such an identifier to the covered paper. No hash or commit is
invented to mask that issue.

All published literature remains outside the return package. Citations,
public URLs, source SHA-256 values, and pages used are recorded instead.

Each current standalone project now has its own MANIFEST.sha256, refreshed only within the working tree before an immutable scheduled archive. The per-project manifest excludes itself and transient TeX build files. The outer archive manifest includes these manifests. Earlier checkpoint ZIPs remain untouched.
