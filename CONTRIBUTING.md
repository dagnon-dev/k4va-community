# Contributing to K4VA Community

1. Create a focused change with a test and documentation when behavior changes.
2. Keep rules generic, deterministic and safe to publish.
3. Do not add customer contracts, credentials, private endpoints or proprietary policy mappings.
4. Run `python -m pytest` and `k4va analyze examples/insecure-api.yaml --format json` before opening a change.

New rules should include an ID, category, severity, description, remediation and a synthetic test case.
