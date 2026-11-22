
"""Load and access fleet application settings."""

SETTINGS_FILE = "settings.cfg"

KNOWN_KEYS = {
    "service_interval_km",
    "warn_at_percent",
    "report_title",
    "history_file",
    "log_file",
    "mileage_unit",
}


def load_settings(path: str | None = None) -> dict[str, str]:
    """Read recognized settings from a configuration file."""
    if path is None:
        path = SETTINGS_FILE

    settings = {}

    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key in KNOWN_KEYS:
                settings[key] = value

    return settings


def get_int(settings: dict[str, str], key: str, fallback: int) -> int:
    """Return a setting as an integer, or its fallback if invalid."""
    try:
        return int(settings[key])
    except (KeyError, ValueError):
        return fallback


def get_setting(
    settings: dict[str, str], key: str, fallback: str = ""
) -> str:
    """Return a setting or its fallback value."""
    return settings.get(key, fallback)
