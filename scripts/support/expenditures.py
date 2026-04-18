import pandas as pd
import os

def process_year(file, year):

    if year == 1999:
        df = pd.read_fwf(file, header=None)
        df.columns = ["gov_id", "survey_year", "item_code", "amount"]
    else:
        df = pd.read_fwf(
            file,
            colspecs=[(0,14), (14,17), (17,29), (29,31), (31,33), (33,35)],
            header=None
        )
        df.columns = ["gov_id", "item_code", "amount", "survey_year", "year_of_data", "origin"]

    df = df[df["gov_id"].astype(str).str.startswith("29")]
    df = df[df["item_code"].str.startswith(("E", "F"))]

    df["group"] = df["item_code"].str[0]

    result = df.groupby("group")["amount"].sum()

    return {
        "year": year,
        "E": result.get("E", 0),
        "F": result.get("F", 0),
        "Total": df["amount"].sum()
    }

files = [(f"data/{str(year)[-2:]}state35.txt", year) for year in range(1996, 2025)]

results = []

for file, year in files:
    year_result = process_year(file, year)
    results.append(year_result)
    
df_results = pd.DataFrame(results)

df_results[["E", "F", "Total"]] = df_results[["E", "F", "Total"]] * 1_000

print(df_results)

#df_results.to_csv("expenditures_summary.csv", index=False)

#print(df_results["E"].to_string(index=False))



