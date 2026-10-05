import json

from k4va.models import Finding, Severity
from k4va.reporters.console import render
from k4va.reporters.json_reporter import build_report
from k4va.scoring import calculate_score


def test_console_report_contains_score_and_findings():
    finding = Finding("DOC-001", "Summary missing", "Documentation", Severity.MEDIUM, "get /orders", "missing", "document it")
    output = render("orders.yaml", calculate_score([finding]), [finding])
    assert "K4VA Community" in output
    assert "Score:" in output
    assert "DOC-001" in output


def test_json_report_is_serializable():
    finding = Finding("OBS-001", "Guidance missing", "Observability", Severity.LOW, "info", "missing", "add it")
    report = build_report("orders.yaml", calculate_score([finding]), [finding])
    assert json.loads(json.dumps(report))["findings"][0]["severity"] == "LOW"
