import json

from k4va.cli import main


def test_cli_json_output(capsys):
    exit_code = main(["analyze", "examples/insecure-api.yaml", "--format", "json"])
    output = json.loads(capsys.readouterr().out)
    assert exit_code == 1
    assert output["product"] == "K4VA Community"
    assert output["findings"]


def test_cli_rules(capsys):
    assert main(["rules"]) == 0
    assert "SEC-001" in capsys.readouterr().out
