import pandas as pd

from src.transformation.standardization import DataStandardizer

df = pd.DataFrame(
    {
        "currency": ["usd", "zwg"],
        "status": ["success", "failed"],
        "amount": ["100.50", "250"],
        "attempt_count": ["1", "2"],
        "initiated_at": [
            "2026-03-01 08:00:00",
            "2026-03-02 10:15:00",
        ],
    }
)

standardizer = DataStandardizer()

result = standardizer.standardize(
    "transactions",
    df,
)

print(result)
print()
print(result)