# Vikkypaedia — Paediatric Medical Education

Live: https://vikramsakaleshpurkumar-byte.github.io/

The landing page and learner Passport for every Vikkypaedia module. One self-contained HTML file: no framework, no CDN, no network request, works offline.

## Domain taxonomy

This repository acts as the hub for the Vikkypaedia learning ecosystem. The recommended professional domains and GitHub topics for the portfolio are captured in `REPO_DOMAINS.md`.

The most important domains across the Vikkypaedia repositories are:

- medical-education
- self-directed-learning
- self-paced-learning
- open-educational-resources
- mooc
- pediatric-care
- neonatal-care
- competency-based-medical-education
- offline-first
- evidence-based-medicine

## How the Passport works

Every module on the Vikkypaedia Standard engine writes a short summary (units mastered, checkpoints, retention, reviews due, best exam score, certified) into `localStorage` under `vkp.passport.v1`.

- No account, no server, no analytics. Nothing leaves the learner's browser (DPDP Act 2023: nothing is collected centrally).
- A different browser or device has its own Passport.
- The combined record is self-attested. Its checksum detects casual alteration; it does not prove the learner sat any assessment.

## Adding a module

Add an entry to `CATALOGUE` in `src.html` (`id` must equal the module's `MODULE.id`), set `std:true` once it runs the Standard engine, then rebuild:

```bash
python build_hub.py    # inlines the design tokens into index.html
```

## Licence

CC BY-NC-SA 4.0, excluding the Vikkypaedia name, the name and likeness of Dr Vikram Sakaleshpur Kumar, and any certificate signature block.

