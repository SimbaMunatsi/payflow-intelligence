from src.transformation.results import TransformationResult

result = TransformationResult(
    stage="Transformation",
    operation="Trim Whitespace",
    dataset="transactions",
    success=True,
    records_processed=180720,
    values_changed=412,
    details={
        "columns": [
            "merchant_id",
            "status",
        ]
    },
)

print(result)

print()

print(result.to_dict())