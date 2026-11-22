
"""Utility functions used by fleet reporting."""

KM_PER_MILE = 1.609


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km / KM_PER_MILE


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"
