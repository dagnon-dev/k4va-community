# K4VA Community

K4VA Community
Copyright (c) 2026 K4VA

Know before you ship.

K4VA Community is an open-source API Governance & Production Readiness analyzer for OpenAPI contracts.

Detect security, governance, documentation and API design issues before they reach production.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
k4va analyze examples/insecure-api.yaml
```

## Installation

Python 3.10 or newer is supported. Community runs locally and does not connect to K4VA SaaS.

## CLI usage

```bash
k4va analyze openapi.yaml
k4va analyze openapi.json --format json
k4va rules
```

The console report includes an overall score, category scores and findings. JSON output is suitable for scripts. The CLI exits with `1` when findings are detected and `2` for invalid input.

## Example output

```text
K4VA Community
API Governance & Production Readiness

Contract: examples/insecure-api.yaml

Production Readiness
--------------------

Score: 91/100

Security         82
Governance       100
Documentation    79
API Design       97
Observability    97

Findings
--------

HIGH
SEC-001 Authentication scheme missing

MEDIUM
DOC-001 Operation summary missing
DOC-002 Error response not documented

6 findings detected
```

## Supported contracts

OpenAPI 3.0.x and 3.1.x YAML or JSON files are supported. This initial release does not promise full semantic validation of every OpenAPI extension.

## Rule categories

Community rules cover basic Security, Documentation, API Design and Observability practices. See [docs/community-rules.md](docs/community-rules.md) for IDs, severities and remediation guidance.

## Community vs K4VA Platform

| Feature | Community | K4VA Platform |
| --- | --- | --- |
| OpenAPI parsing | Yes | Yes |
| Community rules | Yes | Yes |
| Local CLI analysis | Yes | Yes |
| Basic score | Yes | Yes |
| JSON output | Yes | Yes |
| Production Review | Limited | Full |
| Advanced rule packs | No | Yes |
| Marketplace | No | Yes |
| Analysis history | No | Yes |
| Collaboration | No | Yes |
| Enterprise governance | No | Yes |
| Banking Governance | No | Yes |

## Commercial Platform

K4VA Community provides the open-source local analysis engine and Community rule set.

The K4VA Platform adds advanced Production Review, rule packs, history, collaboration, Marketplace, enterprise governance, and specialized editions.

https://www.k4va.com

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep rules deterministic, generic and safe to publish. Do not submit customer contracts, credentials or private policies.

## Security

See [SECURITY.md](SECURITY.md). Do not report suspected vulnerabilities in public Issues.

## License

K4VA Community is licensed under the Mozilla Public License 2.0 (`MPL-2.0`). See [LICENSE](LICENSE) for the complete license text. See [LICENSE_RECOMMENDATION.md](LICENSE_RECOMMENDATION.md) for the license decision record.

## Disclaimer

K4VA Community provides developer feedback. Scores and findings are not certifications, compliance determinations, security guarantees or professional advice. Review results in the context of your system and risk requirements.
