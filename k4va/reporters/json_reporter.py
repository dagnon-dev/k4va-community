from typing import Any

from k4va.models import Finding
from k4va.scoring import Score


def build_report(contract: str, score: Score, findings: list[Finding]) -> dict[str, Any]:
    return {"product": "K4VA Community", "contract": contract, "score": {"overall": score.overall, "categories": score.categories}, "findings": [finding.to_dict() for finding in findings]}
