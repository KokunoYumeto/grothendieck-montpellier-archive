# SIGN_NEXT research package

The self-contained paper is `SIGN_NEXT.tex`. The question states, proof/source check events, dated ledger, and programme consequences are `QUESTIONS.tsv`, `CHECK_EVENTS.tsv`, `LEDGER.md`, and `IMPLICATIONS.md`.

This checkpoint is a live research state. The full arithmetic/geometric normalization of the intended Q6g chain is still being investigated. All other conclusions retain the exact scopes shown in the registers. The paper separates checked findings from unestablished stronger assertions.

`work/` contains proof components, independent review notes, source locators, integer computation programs and certificates. `build_paper.py` assembles a single LaTeX file without external inputs. `build_registers.py` merges the actual check-event files without inventing events. The effort setting is not exposed; all checks name the actual inherited model and agent/run.

The archive excludes redundant downloaded source PDFs and full extracted external source trees. They are inputs, not new deliverables, and the original attached archive plus source URLs/manifests are sufficient to recover them. `EXCLUDED_INPUTS.tsv` records the excluded paths and hashes. All newly written proofs, notes, programs, registers and computation results are included. No previous checkpoint ZIP is embedded.

The optional `SIGN_NEXT.pdf` is built from the self-contained source. The local TeX format and scalable-font map were repaired after the default installation failed; those environment repairs are not mathematical checks. The source, proof components, check register, and exact computational certificates are the primary mathematical deliverables.
