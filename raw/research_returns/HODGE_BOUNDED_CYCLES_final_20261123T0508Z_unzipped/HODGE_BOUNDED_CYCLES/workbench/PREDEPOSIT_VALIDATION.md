# Predeposit validation

The delivered version is a checked, unfiled candidate. The official Format 1 checker was run against the final repository layout. Its result is **not PASS**: it reports exactly **386 faults**, all caused by the permanent identifiers that the user will assign when filing.

| Official fault category | Count | Reason |
|---|---:|---|
| Provisional statement tags | 89 | `UNFILED.nnn` has not been replaced by an assigned `WB-nnnn.nnn`. |
| Provisional check-event tags | 296 | The events preserve those same provisional statement identities. |
| Work folder | 1 | `work/UNFILED` has not been renamed to the assigned work number. |
| Unexpected faults | 0 | No header, field-count, format, source-PDF, private-token, size or manifest fault was reported. |

The checker exit code was 1. Its exact final line was:

```text
workbench: 227 files, 386 faults
```

The checker is the catalogue's external program and is not bundled. Its SHA-256 is `13042772b472b1a65f35fd8d8c349dc55a5e9cdabb5e6e5e4434aa1d4b6f0291`; the inspected `FORMAT.md` has SHA-256 `b6cff6c746787fc706e3db621a372b83ab49b84e76b218776807154a7cd92832`. Obtain it from [mathematics-workbenches](https://github.com/KokunoYumeto/mathematics-workbenches) and run the following from that catalogue checkout, supplying the path to this repository candidate:

```sh
python3 -I -B tools/check_workbench.py PATH_TO_WORKBENCH
```

## Sealed delivered version

`work/UNFILED/v1/MANIFEST.sha256` contains 220 entries and hashes every version file except itself and a future `DEPOSITED.md`, following the official inclusion rule. Its SHA-256 is:

```text
9461ac3cc511b71673560eb0c1cc91c914c3df9d4fdbc870a461665d69521895
```

The manifest was independently reconstructed and compared byte for byte. The PDF identity and page review, complete source readings, exact replay results, source coverage and ownership screen are recorded inside the version. The metadata checks separately verified all allowed statuses and check types, 89 unique statement tags, all dependency references, all check-record paths and all 27 final TeX hashes. These checks are separate because the official program stops checking each provisional row after its tag fault.

## Filing actions still pending

The registry number and individual record page, actual public commit/version, paper seal and deposit are not assigned here. `FILING.md` explains the exact steps and the manifest self-reference issue. No `DEPOSITED.md` was created, no public push was made, and no stale or invented commit/hash was printed in the paper. The final paper is checked; its mathematical open questions remain open.
