from k4va.models import Finding, Severity
from k4va.scoring import Score


def render(contract: str, score: Score, findings: list[Finding]) -> str:
    lines = ["K4VA Community", "API Governance & Production Readiness", "", f"Contract: {contract}", "", "Production Readiness", "--------------------", "", f"Score: {score.overall}/100", ""]
    for category, value in score.categories.items():
        lines.append(f"{category:<16} {value}")
    lines.extend(["", "Findings", "--------", ""])
    for severity in (Severity.HIGH, Severity.MEDIUM, Severity.LOW):
        selected = [finding for finding in findings if finding.severity == severity]
        if selected:
            lines.append(severity.value)
            lines.extend(f"{item.rule_id} {item.name}" for item in selected)
            lines.append("")
    lines.append(f"{len(findings)} finding{'s' if len(findings) != 1 else ''} detected")
    return "\n".join(lines)
