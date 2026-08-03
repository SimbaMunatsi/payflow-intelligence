from src.validation.framework.results import ValidationResult

result = ValidationResult(

    rule_name="Duplicate Transactions",

    dataset="transactions",

    passed=False,

    severity="CRITICAL",

    message="12 duplicate transaction IDs found.",

    rows_affected=12,

    recommendation="Remove duplicate transaction references.",

)

print(result)

print()

print(result.to_dict())