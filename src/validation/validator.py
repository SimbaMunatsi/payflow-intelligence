"""
Validation Engine.

Executes validation rules against datasets.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.utils.logger import get_logger
from src.validation.analytics.dashboard import (
    ValidationDashboardBuilder,
)
from src.validation.registry.rule_registry import RuleRegistry

logger = get_logger(__name__)


class Validator:
    """
    Executes validation rules.
    """

    def __init__(self):

        self.dashboard_builder = (
            ValidationDashboardBuilder()
        )

    def validate_dataset(
        self,
        dataset_name,
        dataframe,
        datasets,
    ):
        """
        Validate a single dataset.
        """

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
                    f"[PASS] {result.rule_name}"
                )

            else:

                logger.warning(
                    f"[FAIL] {result.rule_name}"
                )

        return results

    def validate_all(
        self,
        datasets,
    ):
        """
        Validate every staged dataset.

        Returns
        -------
        tuple[
            list[ValidationResult],
            DashboardModel
        ]
        """

        logger.info("=" * 60)
        logger.info("STARTING VALIDATION LAYER")
        logger.info("=" * 60)

        all_results = []

        for dataset_name, dataframe in datasets.items():

            dataset_results = self.validate_dataset(
                dataset_name=dataset_name,
                dataframe=dataframe,
                datasets=datasets,
            )

            all_results.extend(
                dataset_results
            )

        dashboard = (
            self.dashboard_builder.build(
                all_results
            )
        )

        logger.info("=" * 60)
        logger.info("VALIDATION LAYER COMPLETED")
        logger.info("=" * 60)

        return (
            all_results,
            dashboard,
        )