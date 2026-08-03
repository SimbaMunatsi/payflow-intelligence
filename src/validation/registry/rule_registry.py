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

from src.validation.referential.transaction_exists import (
    TransactionExistsRule,
)

from src.validation.business.net_amount import (
    NetAmountRule,
)

from src.validation.business.rail_charges import (
    RailChargesRule,
)

from src.validation.business.settlement_lag import (
    SettlementLagRule,
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
            TransactionExistsRule(dataset_name),
            NetAmountRule(dataset_name),
            RailChargesRule(dataset_name),
            SettlementLagRule(dataset_name),
        ]

        return rules