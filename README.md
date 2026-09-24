# Vikkypaedia — Paediatric Medical Education

Live: https://vikramsakaleshpurkumar-byte.github.io/

The landing page and **learner Passport** for every Vikkypaedia module. One self-contained HTML file: no framework, no CDN, no network request, works offline.

## How the Passport works
Every module on the Vikkypaedia Standard engine writes a short summary (units mastered, checkpoints, retention, reviews due, best exam score, certified) into `localStorage` under `vkp.passport.v1`. Because every module is served from this same GitHub Pages origin, that one key is shared: the hub reads it, and a new module pre-fills enrolment from it.

- No account, no server, no analytics. Nothing leaves the learner's browser (DPDP Act 2023: nothing is collected centrally).
- A different browser or device has its own Passport.
- The **combined record** is self-attested. Its checksum detects casual alteration; it does not prove the learner sat any assessment.

## Adding a module
Add an entry to `CATALOGUE` in `src.html` (`id` must equal the module's `MODULE.id`), set `std:true` once it runs the Standard engine, then rebuild:

```bash
python build_hub.py    # inlines the design tokens into index.html
```

## Licence
CC BY-NC-SA 4.0, excluding the Vikkypaedia name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and any certificate signature block.
