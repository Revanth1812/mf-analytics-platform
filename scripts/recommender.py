import pandas as pd
scheme_performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip().title()

if risk == "Low":
    risk_filter = ["Low"]
elif risk == "Moderate":
    risk_filter = ["Moderate"]
elif risk == "High":
    risk_filter = ["High", "Very High", "Moderately High"]
else:
    print("Invalid Risk Appetite")
    exit()

recommendation = (
    scheme_performance[
        scheme_performance["risk_grade"].isin(risk_filter)
    ]
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

print("\nTop 3 Recommended Mutual Funds\n")

print(
    recommendation[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "aum_crore"
        ]
    ].to_string(index=False)
)