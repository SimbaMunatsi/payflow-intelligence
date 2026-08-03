"""Check whether a merchant exists in the reference data."""


def validate_merchant_exists(merchant_id, merchants):
    """Return whether the merchant identifier exists."""
    return merchant_id in merchants if merchants is not None else False
