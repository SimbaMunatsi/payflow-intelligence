"""Check whether a transaction exists in the reference data."""


def validate_transaction_exists(transaction_id, transactions):
    """Return whether the transaction identifier exists."""
    return transaction_id in transactions if transactions is not None else False
