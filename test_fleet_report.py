
"""Tests for the fleet health report."""

from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    """Only the nearly worn car should be due."""
    assert fleet_summary(SAMPLE)["due"] == 1


def test_missing_reading_does_not_crash_report():
    """A car without a last-service reading must not crash the report."""
    fleet = [
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
        {"id": "VOS-7788", "odometer": 92000},
    ]
    summary = fleet_summary(fleet)
    assert summary["count"] == 2
    assert "average_wear" in summary
