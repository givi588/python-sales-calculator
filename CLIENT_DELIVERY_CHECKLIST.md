# Client delivery checklist

Use this checklist when handing over a small Python script or CSV automation to a client. This document is a **portfolio example**, not a claim that the sample sales calculator is production-ready.

## 1. Agree on the scope

- [ ] Confirm the problem the client wants to solve, the inputs, and the expected outputs.
- [ ] Confirm the source-file format (including required CSV columns and character encoding).
- [ ] Agree on the currency, rounding rules, validation requirements, and delivery date.
- [ ] State what is **not** included (for example, integrations, hosting, or ongoing support).
- [ ] Agree on an acceptance test and a clear handover process before beginning work.

## 2. Develop on a separate branch

- [ ] Create a branch such as `feature/client-request` from the latest `main`.
- [ ] Make one focused change at a time, using descriptive commits.
- [ ] Avoid uploading client data, credentials, access tokens, or private documents.
- [ ] Add or update tests for the client's requirements.

## 3. Verify before opening a pull request

For this example repository, run:

```bash
python -m unittest discover -s tests -v
python main.py
python automation.py
```

- [ ] Confirm the output totals and sample CSV report are correct.
- [ ] Check invalid or incomplete CSV input and review the program's error behavior.
- [ ] Confirm where generated reports are written and whether any files are overwritten.
- [ ] Open a pull request and review **Files changed** and the automated checks.
- [ ] Merge into `main` only after reviewing the diff and resolving any failures.

## 4. Handover and acceptance

- [ ] Share the source-code repository or agreed deliverable and the instructions to run it.
- [ ] Demonstrate the script with **sample data**, not confidential client records.
- [ ] Ask the client to confirm the agreed acceptance criteria.
- [ ] Provide a concise note about known limitations and where to report bugs.
- [ ] Clarify any support or maintenance period; do not promise indefinite free support.

## Current demo limitations

The current calculator expects integer prices and quantities in a specific CSV structure and reports monetary values in USD. `automation.py` overwrites `sales_report.csv` whenever it successfully runs; it catches several input errors and prints them rather than returning a nonzero exit code. It is a learning/portfolio tool and should be adapted and checked against actual requirements before client use.
