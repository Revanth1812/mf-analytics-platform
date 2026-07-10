import pandas as pd
import numpy as np


def calculate_daily_returns(nav_df):
    """
    Calculate daily returns for each mutual fund.
    """
    nav_df = nav_df.copy()
    nav_df = nav_df.sort_values(["amfi_code", "date"])

    nav_df["daily_return"] = (
        nav_df.groupby("amfi_code")["nav"]
        .pct_change()
    )

    return nav_df


def calculate_rolling_sharpe(nav_df, window=90):
    """
    Calculate rolling Sharpe Ratio.
    """
    nav_df = nav_df.copy()

    nav_df["rolling_sharpe"] = (
        nav_df.groupby("amfi_code")["daily_return"]
        .transform(
            lambda x: (
                x.rolling(window).mean()
                /
                x.rolling(window).std()
            ) * np.sqrt(252)
        )
    )

    return nav_df


def calculate_var_cvar(returns, confidence=0.95):
    """
    Calculate Historical VaR and CVaR.
    """

    returns = returns.dropna()

    var = np.percentile(
        returns,
        (1 - confidence) * 100
    )

    cvar = returns[
        returns <= var
    ].mean()

    return var, cvar


if __name__ == "__main__":

    print("Performance Metrics Module Loaded Successfully.")