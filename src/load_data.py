import requests
import pandas as pd  # pyright: ignore[reportMissingModuleSource]
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
def get_world_bank_data(indicator, country="KE", start=1980, end=2024):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start}:{end}&format=json"
    response = requests.get(url)
    data = response.json()
    records = []
    for entry in data[1]:
        records.append({
            "year": int(entry["date"]),
            "value": entry["value"],
        })
    df = pd.DataFrame(records)
    df = df.sort_values(by="year").reset_index(drop=True)
    return df   

inflation = get_world_bank_data("FP.CPI.TOTL.ZG")
inflation = inflation.rename(columns={"value": "inflation"})

gdp_growth = get_world_bank_data("NY.GDP.MKTP.KD.ZG")
gdp_growth = gdp_growth.rename(columns={"value": "gdp_growth"})

exchange_rate = get_world_bank_data("PA.NUS.FCRF")
exchange_rate = exchange_rate.rename(columns={"value": "exchange_rate"})    

broad_money = get_world_bank_data("FM.LBL.BMNY.ZG")
broad_money = broad_money.rename(columns={"value": "broad_money"})

private_credit = get_world_bank_data("FS.AST.PRVT.GD.ZS")
private_credit = private_credit.rename(columns={"value": "private_credit_gdp"}) 

interest_spread = get_world_bank_data("FR.INR.LNDP")
interest_spread = interest_spread.rename(columns={"value": "interest_rate_spread"})

external_debt = get_world_bank_data("DT.DOD.DECT.GN.ZS")
external_debt = external_debt.rename(columns={"value":  "external_debt_gni"})

debt_service = get_world_bank_data("DT.TDS.DECT.EX.ZS")
debt_service = debt_service.rename(columns={"value": "debt_service_exports"})

df = pd.merge(inflation, gdp_growth, on="year", how="outer")
df = pd.merge(df, exchange_rate, on="year", how="outer")
df = pd.merge(df, broad_money, on="year", how="outer")
df = pd.merge(df, private_credit, on="year", how="outer")
df = pd.merge(df, interest_spread, on="year", how="outer")
df = pd.merge(df, external_debt, on="year", how="outer")
df = pd.merge(df, debt_service, on="year", how="outer")

df["country"] = "Kenya"

df = df[(df["year"] >= 1980) & (df["year"] <= 2024)]

print(df.shape)
print(df.isnull().sum())
print(df.head())

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="kenya_financial_deepening")

cursor = connection.cursor()

insert_query = """
INSERT IGNORE INTO economic_indicators
(country, year, inflation, gdp_growth, exchange_rate, broad_money_gdp, private_credit_gdp, interest_rate_spread, external_debt_gni, debt_service_exports)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row["country"],
        int(row["year"]),
        None if pd.isnull(row["inflation"]) else float(row["inflation"]),
        None if pd.isnull(row["gdp_growth"]) else float(row["gdp_growth"]),
        None if pd.isnull(row["exchange_rate"]) else float(row["exchange_rate"]),
        None if pd.isnull(row["broad_money"]) else float(row["broad_money"]),
        None if pd.isnull(row["private_credit_gdp"]) else float(row["private_credit_gdp"]),
        None if pd.isnull(row["interest_rate_spread"]) else float(row["interest_rate_spread"]),
        None if pd.isnull(row["external_debt_gni"]) else float(row["external_debt_gni"]),
        None if pd.isnull(row["debt_service_exports"]) else float(row["debt_service_exports"])
    ))
connection.commit()
print(f"Inserted {cursor.rowcount} rows into MySQL")

cursor.close()
connection.close()

df.to_csv("data/cleaned/kenya_financial_deepening.csv", index=False)
print("saved to csv")