"""Validate rail charge business rules."""


def validate_rail_charges(amount):
    """Return whether rail charges are acceptable."""
    return amount >= 0
