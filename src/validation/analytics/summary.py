"""
Validation Summary Builder.

Aggregates ValidationResult objects into dashboard-ready
summary statistics.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from collections import defaultdict

from src.validation.analytics.models import (
    DatasetSummary,
    ValidationSummary,
)

from src.validation.framework.results import ValidationResult


class ValidationSummaryBuilder:
    """
    Builds validation summary statistics.
    """

    def build(
        self,
        results: list[ValidationResult],
    ) -> ValidationSummary:

        total_rules = len(results)

        passed = sum(
            result.passed
            for result in results
        )

        failed = total_rules - passed

        critical = sum(
            (
                not result.passed
                and result.severity == "CRITICAL"
            )
            for result in results
        )

        errors = sum(
            (
                not result.passed
                and result.severity == "ERROR"
            )
            for result in results
        )

        warnings = sum(
            (
                not result.passed
                and result.severity == "WARNING"
            )
            for result in results
        )

        infos = sum(
            (
                not result.passed
                and result.severity == "INFO"
            )
            for result in results
        )

        # --------------------------------------------
        # Dataset Summary
        # --------------------------------------------

        dataset_results = defaultdict(list)

        for result in results:

            dataset_results[
                result.dataset
            ].append(result)

        datasets = {}

        for dataset, dataset_rules in dataset_results.items():

            datasets[dataset] = DatasetSummary(

                dataset=dataset,

                total_rules=len(dataset_rules),

                passed=sum(
                    r.passed
                    for r in dataset_rules
                ),

                failed=sum(
                    not r.passed
                    for r in dataset_rules
                ),

                critical=sum(
                    (
                        not r.passed
                        and r.severity == "CRITICAL"
                    )
                    for r in dataset_rules
                ),

                errors=sum(
                    (
                        not r.passed
                        and r.severity == "ERROR"
                    )
                    for r in dataset_rules
                ),

                warnings=sum(
                    (
                        not r.passed
                        and r.severity == "WARNING"
                    )
                    for r in dataset_rules
                ),

                infos=sum(
                    (
                        not r.passed
                        and r.severity == "INFO"
                    )
                    for r in dataset_rules
                ),

            )

        # --------------------------------------------
        # Category Summary
        # --------------------------------------------

        category_summary = defaultdict(
            lambda: {
                "total": 0,
                "passed": 0,
                "failed": 0,
            }
        )

        for result in results:

            category = result.category

            category_summary[category]["total"] += 1

            if result.passed:

                category_summary[category]["passed"] += 1

            else:

                category_summary[category]["failed"] += 1

        return ValidationSummary(

            total_rules=total_rules,

            passed=passed,

            failed=failed,

            critical=critical,

            errors=errors,

            warnings=warnings,

            infos=infos,

            datasets=datasets,

            categories=dict(category_summary),

        )