from typing import Any

from k4va.models import Finding
from k4va.rules.community.catalog import COMMUNITY_RULES


def analyze(document: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for rule in COMMUNITY_RULES:
        findings.extend(rule.check(document))
    return sorted(findings, key=lambda item: (item.severity.value, item.rule_id, item.path))
