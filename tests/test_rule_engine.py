from k4va.engine import analyze
from k4va.parser import parse_openapi


def test_insecure_example_generates_community_findings():
    findings = analyze(parse_openapi("examples/insecure-api.yaml"))
    rule_ids = {finding.rule_id for finding in findings}
    assert "SEC-001" in rule_ids
    assert "DOC-001" in rule_ids
    assert "API-002" in rule_ids
    assert all(not finding.rule_id.startswith("BANK-") for finding in findings)


def test_good_example_has_no_findings():
    assert analyze(parse_openapi("examples/good-api.yaml")) == []
