"""Check for duplicate rows in a dataset."""


def validate_duplicate_rows(data):
    """Return whether duplicate rows are present."""
    return len(data) != len({tuple(row) for row in data}) if data is not None else False
