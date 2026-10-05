import json

import pytest

from k4va.parser import OpenAPIParseError, parse_openapi


def test_parser_accepts_yaml_and_json(tmp_path):
    document = {"openapi": "3.1.0", "info": {"title": "Test", "version": "1.0.0"}, "paths": {}}
    yaml_path = tmp_path / "api.yaml"
    yaml_path.write_text("openapi: 3.1.0\ninfo:\n  title: Test\n  version: 1.0.0\npaths: {}\n", encoding="utf-8")
    json_path = tmp_path / "api.json"
    json_path.write_text(json.dumps(document), encoding="utf-8")
    assert parse_openapi(yaml_path)["openapi"] == "3.1.0"
    assert parse_openapi(json_path)["info"]["title"] == "Test"


def test_parser_rejects_invalid_document(tmp_path):
    path = tmp_path / "invalid.yaml"
    path.write_text("not: an openapi document", encoding="utf-8")
    with pytest.raises(OpenAPIParseError):
        parse_openapi(path)
