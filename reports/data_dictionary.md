# Data Dictionary

## dim_fund
- amfi_code - Unique Mutual Fund Identifier
- scheme_name - Mutual Fund Scheme Name
- fund_house - Fund House Name
- category - Fund Category
- sub_category - Fund Sub Category
- plan - Regular/Direct Plan
- risk_category - Risk Classification

## fact_nav
- amfi_code - Mutual Fund Identifier
- date - NAV Date
- nav - Net Asset Value

## fact_transactions
- investor_id - Investor ID
- transaction_date - Transaction Date
- transaction_type - SIP/Lumpsum/Redemption
- amount_inr - Investment Amount
- state - Investor State
- city - Investor City
- payment_mode - Payment Method
- kyc_status - KYC Verification Status

## fact_performance
- return_1yr_pct - 1 Year Return
- return_3yr_pct - 3 Year Return
- return_5yr_pct - 5 Year Return
- expense_ratio_pct - Expense Ratio
- aum_crore - Assets Under Management

## fact_aum
- fund_house - Fund House
- aum_crore - Assets Under Management
- num_schemes - Number of Schemes