"""
Validation Rule Registry.

Responsible for registering and providing
validation rules to the validator.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from src.validation.structural.dataset_not_empty import (
    DatasetNotEmptyRule,
)


class RuleRegistry:
    """
    Registry of all validation rules.
    """

    @staticmethod
    def get_rules(dataset_name: str):
        """
        Return validation rules for a dataset.
        """

        rules = [
            DatasetNotEmptyRule(dataset_name),
        ]

        return rules