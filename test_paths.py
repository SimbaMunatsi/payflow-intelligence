import pandas as pd

from src.transformation.cleaning import DataCleaner

df = pd.DataFrame(
    {
        "merchant": [" MER001 ", "MER002 ", ""],
        "status": [" SUCCESS ", "FAILED ", " NULL "],
    }
)

cleaner = DataCleaner()

result = cleaner.clean(df)

print(result)
print()
print(result.dtypes)