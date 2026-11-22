
"""Decide when a Vossberg Mobility car needs servicing."""

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: float, interval: int) -> float:
    """Calculate service-interval wear as a percentage."""
    return (km_since_service / interval) * 100


def needs_service(car: dict) -> bool:
    """Return whether a car has reached the service warning threshold."""
    last = car.get("last_service_km")
    if last is None:
        return False

    km_since = car["odometer"] - last
    pct = wear_percent(km_since, SERVICE_INTERVAL_KM)
    return pct >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list[str]:
    """Print and return IDs of cars due for service."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged
