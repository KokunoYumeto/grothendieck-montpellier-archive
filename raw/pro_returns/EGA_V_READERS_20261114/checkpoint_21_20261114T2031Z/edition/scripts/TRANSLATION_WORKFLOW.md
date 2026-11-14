# Translation interface

The translation source is the current annotated file in `master_pages/fr/`, prepared from its checked page. Translate into the matching key in `master_pages/en/`. Never translate an unchecked original or silently fill a missing checked page.

Keep each mathematical token string, including spaces and delimiters inside formulas and whole TikZ diagrams, exactly as in the French master. This includes the page-reading branch of every variant. Text inside a math formula remains literal. Explain it in a translator note when needed. Preserve source uncertainties, incomplete fragments, references and mathematical slips; do not supply a missing argument or repair a formula.

Retain variant IDs and their order. Translate the prose inside both branches, retaining the physical kind. When a French spelling or agreement correction has no English effect, omit that English variant and record it in the omissions table. Do not create an artificial English misspelling to imitate a French spelling slip. If an omitted French-only correction contains a doubt, retain that source uncertainty in a linked translator note. A change expressed by a different grammatical unit in English receives a short variant note explaining the mapping.

Use `\tnote{25-SITE-N}{...}` for English explanations. Notes are printed only in the annotated English form. A live uncertainty must remain in the running text so that it also survives in the reading form. An uncertainty solely within canceled French text can remain in its translated apparatus or an explanatory translator note.

Follow the supplied terminology standard. Current context decisions include connexion as connectedness at site25, rare as nowhere dense, and Remords as second thoughts. Keep source abbreviations where their force matters; explain n and s, loc, geom, and similar abbreviations when needed.

## Concurrent annotation records

Each translator owns distinct page files. Do not overwrite another translator's pages. The shared status and annotation tables are updated through scripts so concurrent work cannot overwrite rows.

Prepare a page or batch JSON file in `records/translation_work/` with any of these arrays:

```json
{
  "omissions": [
    {
      "key": "ega25_25_999",
      "source_id": "ega25_25_999-v0001",
      "reason": "Explain the French-only correction and why English is unchanged."
    }
  ],
  "variant_notes": [
    {
      "source_id": "ega25_25_999-v0002",
      "note": "Explain a necessary grammatical mapping in the translated variant."
    }
  ],
  "glossary": [
    {
      "key": "ega25_25_999",
      "french": "source term",
      "english": "translated term",
      "glossary_entry": "existing entry or not listed",
      "reason": "Explain the context choice."
    }
  ]
}
```

Merge only authored, reviewed annotations:

```sh
python edition/scripts/translation_records.py edition/records/translation_work/batch.json
```

Existing identical rows are harmless. A conflicting row stops the merge; use `--replace` only after reviewing the existing decision.

Record completed pages:

```sh
python edition/scripts/check_translation.py --record ega25_25_999
```

The validator compares exact formula strings in both branches and checks the variant-ID sequence after documented omissions. It records hashes of the checked source, French master, and English translation. Validation does not replace the translator's review of prose.

Run without `--record` to detect later source or translation changes. Do not refresh a stale record until the changed source has been reviewed and incorporated. The English reader builder refuses stale or unrecorded translations. Reader assembly and PDF compilation remain with the pipeline owner; translation authors should not regenerate readers while a compilation is running.
