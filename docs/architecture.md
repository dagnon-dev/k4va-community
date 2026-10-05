# Architecture

K4VA Community is intentionally small and local:

1. `parser` loads and validates the OpenAPI document.
2. `engine` runs the explicit Community rule catalog.
3. `models` provides immutable findings.
4. `scoring` calculates a transparent baseline score.
5. `reporters` renders console or JSON output.
6. `cli` connects these pieces without authentication, persistence or network calls.

It has no imports from the commercial K4VA project.
