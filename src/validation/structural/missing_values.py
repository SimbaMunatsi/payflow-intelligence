"""Check for missing values in a dataset."""


def validate_missing_values(data):
    """Return the number of missing values in the dataset."""
    if data is None:
        return 0
    return sum(1 for row in data for value in row if value is None)
