from k4va.models import Finding, Severity
from k4va.scoring import calculate_score


def test_scoring_applies_severity_by_category():
    findings = [Finding("SEC-001", "Auth", "Security", Severity.HIGH, "security", "missing", "add it")]
    score = calculate_score(findings)
    assert score.categories["Security"] == 82
    assert score.overall < 100
