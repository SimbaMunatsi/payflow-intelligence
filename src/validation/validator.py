"""
Validation Engine.

Executes validation rules against datasets.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.utils.logger import get_logger
from src.validation.registry.rule_registry import RuleRegistry

logger = get_logger(__name__)


class Validator:
    """
    Executes validation rules.
    """

    def validate_dataset(
        self,
        dataset_name,
        dataframe,
        datasets,
    ):

        logger.info(
            f"Validating {dataset_name}"
        )

        rules = RuleRegistry.get_rules(
            dataset_name
        )

        results = []

        for rule in rules:

            result = rule.execute(
                dataframe,
                datasets,
            )

            results.append(result)

            if result.passed:

                logger.info(
                    f"[PASS]{result.rule_name}"
                )

            else:

                logger.warning(
                    f"[FAIL]{result.rule_name}"
                )

        return results