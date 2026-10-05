from dataclasses import dataclass

from k4va.models import Finding, Severity


@dataclass(frozen=True)
class Score:
    overall: int
    categories: dict[str, int]


def calculate_score(findings: list[Finding]) -> Score:
    penalties = {Severity.HIGH: 18, Severity.MEDIUM: 9, Severity.LOW: 3}
    categories = {"Security": 100, "Governance": 100, "Documentation": 100, "API Design": 100, "Observability": 100}
    for finding in findings:
        penalty = penalties[finding.severity]
        categories[finding.category] = max(0, categories.get(finding.category, 100) - penalty)
    overall = round(sum(categories.values()) / len(categories))
    return Score(overall=overall, categories=categories)
