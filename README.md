# Vikkypaedia — Paediatric Medical Education

Live: https://vikramsakaleshpurkumar-byte.github.io/

The landing page and **learner Passport** for every Vikkypaedia module. One self-contained HTML file: no framework, no CDN, no network request, works offline.

## How the Passport works
Every module on the Vikkypaedia Standard engine writes a short summary (units mastered, checkpoints, retention, reviews due, best exam score, certified) into `localStorage` under `vkp.passport.v1`. Because every module is served from this same GitHub Pages origin, that one key is shared: the hub reads it, and a new module pre-fills enrolment from it.

- No account, no server, no analytics. Nothing leaves the learner's browser (DPDP Act 2023: nothing is collected centrally).
- A different browser or device has its own Passport.
- The **combined record** is self-attested. Its checksum detects casual alteration; it does not prove the learner sat any assessment.

## Faculty class report
`class-report.html` (linked from the hub) reads a batch of learners' completion records (`.json`, dropped as files or a folder) and shows:
- per learner: units, checkpoints, retention, best exam, attempts, all three criteria met, confident-and-wrong count, integrity flag;
- per unit (records from engine v2.1 onward, which carry `detail` + `detailChecksum`): right-first-time %, mastered %, retained %, misses, hints, confident-and-wrong, exam misses — weakest first;
- CSV export of both tables, print, and a fictional sample batch to try it.

Everything runs in the faculty member's browser; nothing is uploaded. Checksums detect casual alteration only — records are self-attested. Test: `python tests/test_report.py` (needs a built PALS module at `../pals/index.html`).

## Adding a module
Add an entry to `CATALOGUE` in `src.html` (`id` must equal the module's `MODULE.id`), set `std:true` once it runs the Standard engine, then rebuild:

```bash
python build_hub.py    # inlines the design tokens into index.html and class-report.html
```

## Licence
CC BY-NC-SA 4.0, excluding the Vikkypaedia name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and any certificate signature block.
