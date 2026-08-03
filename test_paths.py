from src.ingestion.loader import DataLoader
from src.validation.validator import Validator

loader = DataLoader()

datasets, metadata, summary = loader.run()

validator = Validator()

for dataset_name, dataframe in datasets.items():

    results = validator.validate_dataset(
        dataset_name,
        dataframe,
        datasets,
    )

    print()

    print(dataset_name)

    for r in results:

        print(r.to_dict())