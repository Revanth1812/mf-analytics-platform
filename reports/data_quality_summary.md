# Data Quality Summary

## Validation Results

- Successfully loaded all 10 CSV datasets.
- Verified dataset structure using shape(), dtypes(), and head().
- Successfully fetched live NAV data from mfapi.in.
- Successfully fetched NAV data for 5 mutual fund schemes.
- Explored fund master dataset (fund houses, categories, sub-categories, risk categories).
- Validated AMFI codes between fund_master and nav_history.
- All 40 AMFI codes are present in nav_history.
- No missing AMFI codes were found.