from src.ingestion.loader import DataLoader

loader = DataLoader()

datasets, metadata = loader.run()

print("\nLoaded datasets:")

for name, df in datasets.items():
    print(f"{name}: {len(df):,} rows")

print("\nMetadata:")

for item in metadata:
    print(item)