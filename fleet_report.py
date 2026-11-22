
"""Generate the nightly fleet-health report."""

from km_wachter import wear_percent, needs_service, SERVICE_INTERVAL_KM
from config_loader import load_settings, get_setting
from log_util import log, flush_log
import fleet_utils


def car_wear(car: dict) -> float:
    """Calculate wear for a car with a known last-service reading."""
    last = car.get("last_service_km")
    if last is None:
        return 0.0
    return wear_percent(car["odometer"] - last, SERVICE_INTERVAL_KM)


def fleet_summary(fleet: list[dict]) -> dict:
    """Return the fleet count, due count, and average wear."""
    total = 0.0
    due = 0

    for car in fleet:
        total += car_wear(car)
        if needs_service(car):
            due += 1

    average = total / len(fleet) if fleet else 0.0
    return {
        "count": len(fleet),
        "due": due,
        "average_wear": average,
    }


def print_report(fleet: list[dict]) -> None:
    """Print and log the nightly fleet-health report."""
    settings = load_settings()
    log(get_setting(settings, "report_title", "Nightly fleet report"))

    summary = fleet_summary(fleet)
    print(f"Fleet: {summary['count']} cars")
    print(f"Due for service: {summary['due']}")
    print(f"Average wear: {summary['average_wear']:.1f}%")

    total_km = sum(car["odometer"] for car in fleet)
    miles = fleet_utils.km_to_miles(total_km)
    print(f"Fleet distance: {fleet_utils.format_number(miles)} miles")

    flush_log(get_setting(settings, "log_file", "km_wachter.log"))
