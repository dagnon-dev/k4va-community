from dataclasses import dataclass
from typing import Any, Callable

from k4va.models import Finding, Severity


@dataclass(frozen=True)
class CommunityRule:
    rule_id: str
    name: str
    category: str
    severity: Severity
    description: str
    remediation: str
    check: Callable[[dict[str, Any]], list[Finding]]


def _operations(document: dict[str, Any]):
    for path, item in document.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        for method, operation in item.items():
            if method.lower() in {"get", "post", "put", "patch", "delete", "options", "head", "trace"} and isinstance(operation, dict):
                yield path, method.lower(), operation


def _finding(rule: CommunityRule, path: str, detail: str | None = None) -> Finding:
    return Finding(rule.rule_id, rule.name, rule.category, rule.severity, path, detail or rule.description, rule.remediation)


def _missing_auth(document: dict[str, Any]) -> list[Finding]:
    if document.get("security") or document.get("components", {}).get("securitySchemes"):
        return []
    return [_finding(RULES_BY_ID["SEC-001"], "security", "No authentication scheme is declared in the contract.")]


def _missing_operation_summary(document: dict[str, Any]) -> list[Finding]:
    return [_finding(RULES_BY_ID["DOC-001"], f"{path}.{method}") for path, method, operation in _operations(document) if not operation.get("summary") and not operation.get("description")]


def _missing_error_response(document: dict[str, Any]) -> list[Finding]:
    return [_finding(RULES_BY_ID["DOC-002"], f"{path}.{method}") for path, method, operation in _operations(document) if not any(str(code).startswith(("4", "5")) for code in operation.get("responses", {}))]


def _missing_responses(document: dict[str, Any]) -> list[Finding]:
    return [_finding(RULES_BY_ID["API-001"], f"{path}.{method}") for path, method, operation in _operations(document) if not operation.get("responses")]


def _missing_operation_id(document: dict[str, Any]) -> list[Finding]:
    return [_finding(RULES_BY_ID["API-002"], f"{path}.{method}") for path, method, operation in _operations(document) if not operation.get("operationId")]


def _missing_contact(document: dict[str, Any]) -> list[Finding]:
    if document.get("info", {}).get("contact"):
        return []
    return [_finding(RULES_BY_ID["DOC-003"], "info.contact")]


def _missing_rate_limit_note(document: dict[str, Any]) -> list[Finding]:
    if document.get("externalDocs") or document.get("info", {}).get("description"):
        return []
    return [_finding(RULES_BY_ID["OBS-001"], "info.description")]


RULES = [
    CommunityRule("SEC-001", "Authentication scheme missing", "Security", Severity.HIGH, "No authentication scheme is declared.", "Declare an appropriate security scheme and apply it globally or to operations.", _missing_auth),
    CommunityRule("DOC-001", "Operation summary missing", "Documentation", Severity.MEDIUM, "An operation has no summary or description.", "Add concise documentation for every operation.", _missing_operation_summary),
    CommunityRule("DOC-002", "Error response not documented", "Documentation", Severity.MEDIUM, "An operation has no 4xx or 5xx response.", "Document the errors clients should expect.", _missing_error_response),
    CommunityRule("DOC-003", "API contact missing", "Documentation", Severity.LOW, "The API owner contact is not documented.", "Add an info.contact object with a support channel.", _missing_contact),
    CommunityRule("API-001", "Responses missing", "API Design", Severity.HIGH, "An operation does not declare responses.", "Declare at least one response for every operation.", _missing_responses),
    CommunityRule("API-002", "Operation ID missing", "API Design", Severity.LOW, "An operation has no stable operationId.", "Add a unique operationId for tooling and client generation.", _missing_operation_id),
    CommunityRule("OBS-001", "Operational guidance missing", "Observability", Severity.LOW, "The contract does not describe operational guidance.", "Document support, rate limits or operational expectations.", _missing_rate_limit_note),
]
COMMUNITY_RULES = tuple(RULES)
RULES_BY_ID = {rule.rule_id: rule for rule in COMMUNITY_RULES}
