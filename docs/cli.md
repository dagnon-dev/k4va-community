# CLI

Analyze YAML or JSON contracts:

```bash
k4va analyze examples/good-api.yaml
k4va analyze examples/insecure-api.yaml --format json
k4va rules
```

Exit codes:

- `0`: the contract was analyzed with no findings.
- `1`: the contract was analyzed and findings were detected.
- `2`: the contract could not be loaded or is not supported OpenAPI.
