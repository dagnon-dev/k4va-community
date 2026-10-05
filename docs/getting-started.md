# Getting Started

K4VA Community runs locally and does not require an account, network access or a K4VA SaaS connection.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
k4va analyze examples/insecure-api.yaml
```

The command returns a non-zero status when findings are detected, which makes it useful in local scripts and CI.
