
# Breakdown history shows higher km_since_service, avg_daily_km, and load_factor
# for cars that broke down. Total mileage and vehicle age barely differ.

"""Analyze fleet history and rank cars by relative breakdown risk."""

import pandas as pd


def main() -> None:
    """Compare breakdown groups and print a relative risk score per car."""
    df = pd.read_csv("fleet_history.csv")

    factors = {
        "km_since_service": 0.5,
        "avg_daily_km": 0.3,
        "load_factor": 0.2,
    }

    print("BREAKDOWN HISTORY COMPARISON")
    print(df.groupby("broke_down").mean(numeric_only=True).round(2))
    print("\nRELATIVE BREAKDOWN RISK")

    risk = pd.Series(0.0, index=df.index)

    for column, weight in factors.items():
        minimum = df[column].min()
        maximum = df[column].max()

        if maximum > minimum:
            normalized = (df[column] - minimum) / (maximum - minimum)
        else:
            normalized = 0.0

        risk += normalized * weight

    df["risk_score"] = risk * 100

    results = df.sort_values("risk_score", ascending=False)

    print(
        results[["car_id", "risk_score", "broke_down"]].to_string(
            index=False,
            formatters={"risk_score": "{:.1f}".format},
        )
    )

    print(
        "\nNote: Risk scores are relative rankings, not calibrated "
        "breakdown probabilities."
    )
    print(
        "Total odometer mileage and vehicle age are not used because "
        "they barely distinguish the two groups."
    )


if __name__ == "__main__":
    main()
