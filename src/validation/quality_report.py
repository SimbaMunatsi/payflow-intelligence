"""Quality report helpers."""


def build_quality_report(results):
    """Build a simple quality report from validation results."""
    return {"passed": sum(1 for result in results if result), "total": len(results)}
