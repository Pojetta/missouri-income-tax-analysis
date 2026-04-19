# Missouri Income Tax Analysis

## Overview
This project evaluates the fiscal impact of eliminating Missouri’s individual income tax. Using historical state revenue and expenditure data, the analysis examines how removing income tax revenue affects the state’s budget balance.

The project combines exploratory data analysis (EDA) and predictive modeling to assess fiscal stability under a no-income-tax scenario.

---

## Data
Source: U.S. Census Bureau

- State Government Finances (expenditures)
- Quarterly Summary of State and Local Taxes (revenue)

The final dataset (`mo_financials.xlsx`) includes annual data from 1996–2024 with the following fields:
- Total Revenue
- Income Tax
- Sales Tax
- Other Revenue
- Total Expenditures
- Budget Balance
- Adjusted Revenue (excluding income tax)
- Adjusted Budget Balance

---

## Project Structure

- `data/`
  - `state35.txt` files (raw Census expenditure data)
  - `mo_financials.xlsx` (final dataset)

- `images/`
  - `revenue_vs_expenditures.png`
  - `predicted_vs_actual.png`

- `scripts/`
  - `model_adjusted_balance.py`
  - `support/`
    - `expenditures.py`

- `requirements.txt`
- `README.md`

---

## Analysis

### Exploratory Data Analysis
A line chart compares:
- Total Revenue
- Total Expenditures
- Adjusted Revenue (no income tax)

Key finding:
Missouri maintains a surplus with income tax, but recent years show deficits when it is removed.

---

### Predictive Modeling
Model: Linear Regression

Features:
- Year
- Sales Tax
- Other Revenue

Target:
- Adjusted Budget Balance

Performance:
- R² ≈ 0.93

A predicted vs. actual chart shows strong alignment between model predictions and observed values.

---

## Key Findings
- Missouri has become increasingly dependent on income tax revenue
- Removing income tax results in sustained deficits in recent years
- Adjusted budget balance shows higher variability, indicating instability
- Revenue composition plays a critical role in fiscal outcomes

---

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt

```

2. Run the model:
```bash
python scripts/model_adjusted_balance.py
```

---

## Notes
- Analysis is limited to tax revenue and does not include federal funding or non-tax revenue
- Results should be interpreted as an evaluation of tax structure, not total state finances

---

## Repository
https://github.com/Pojetta/missouri-income-tax-analysis