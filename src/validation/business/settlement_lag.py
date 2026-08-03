"""Validate settlement lag business rules."""


def validate_settlement_lag(days):
    """Return whether settlement lag is acceptable."""
    return days >= 0
