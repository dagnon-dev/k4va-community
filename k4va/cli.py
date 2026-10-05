import argparse
import json
import sys

from k4va import __version__
from k4va.engine import analyze
from k4va.parser import OpenAPIParseError, parse_openapi
from k4va.reporters.console import render
from k4va.reporters.json_reporter import build_report
from k4va.rules import COMMUNITY_RULES
from k4va.scoring import calculate_score


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="k4va", description="K4VA Community OpenAPI governance analyzer")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)
    analyze_command = commands.add_parser("analyze", help="Analyze an OpenAPI YAML or JSON file")
    analyze_command.add_argument("contract")
    analyze_command.add_argument("--format", choices=("console", "json"), default="console")
    commands.add_parser("rules", help="List Community rules")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "rules":
        for rule in COMMUNITY_RULES:
            print(f"{rule.rule_id} [{rule.severity}] {rule.name} ({rule.category})")
        return 0
    try:
        document = parse_openapi(args.contract)
    except OpenAPIParseError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    findings = analyze(document)
    score = calculate_score(findings)
    if args.format == "json":
        print(json.dumps(build_report(args.contract, score, findings), indent=2))
    else:
        print(render(args.contract, score, findings))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
