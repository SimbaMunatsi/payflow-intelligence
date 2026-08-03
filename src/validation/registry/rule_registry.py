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

from src.validation.structural.required_columns import (
    RequiredColumnsRule,
)

from src.validation.structural.missing_required_values import (
    MissingRequiredValuesRule,
)

from src.validation.structural.duplicate_primary_key import (
    DuplicatePrimaryKeyRule,
)

from src.validation.referential.merchant_exists import (
    MerchantExistsRule,
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
            RequiredColumnsRule(dataset_name),
            MissingRequiredValuesRule(dataset_name),
            DuplicatePrimaryKeyRule(dataset_name),
            MerchantExistsRule(dataset_name),
        ]

        return rules