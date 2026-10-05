# Community Rules

| ID | Name | Category | Severity | Description | Remediation |
| --- | --- | --- | --- | --- | --- |
| SEC-001 | Authentication scheme missing | Security | High | No authentication scheme is declared. | Declare and apply an appropriate security scheme. |
| DOC-001 | Operation summary missing | Documentation | Medium | An operation has no summary or description. | Document every operation. |
| DOC-002 | Error response not documented | Documentation | Medium | An operation has no 4xx or 5xx response. | Document expected client and server errors. |
| DOC-003 | API contact missing | Documentation | Low | The API owner contact is not documented. | Add `info.contact`. |
| API-001 | Responses missing | API Design | High | An operation does not declare responses. | Declare at least one response. |
| API-002 | Operation ID missing | API Design | Low | An operation has no stable operationId. | Add a unique operationId. |
| OBS-001 | Operational guidance missing | Observability | Low | Operational guidance is not described. | Document support, rate limits or operational expectations. |
