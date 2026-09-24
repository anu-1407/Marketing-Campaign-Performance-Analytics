import pandas as pd

# Load marketing campaign dataset
df = pd.read_csv(
    r"C:\Users\Anu\OneDrive\Desktop\Maketing campagin analysis\dataset\marketing_campagin_data.csv"
)

# Convert date column
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())
# Calculate marketing KPIs
df["CTR"] = (df["clicks"] / df["impressions"]) * 100
df["Conversion_Rate"] = (df["conversions"] / df["clicks"]) * 100
df["CPC"] = df["spend"] / df["clicks"]
df["CPA"] = df["spend"] / df["conversions"]
df["ROAS"] = df["revenue"] / df["spend"]
df["ROI"] = ((df["revenue"] - df["spend"]) / df["spend"]) * 100

# Display KPI results
print("\nMarketing KPIs:")
print(df[[
    "channel",
    "campaign",
    "CTR",
    "Conversion_Rate",
    "CPC",
    "CPA",
    "ROAS",
    "ROI"
]].head())
print("\nOverall Marketing Performance:")

total_spend = df["spend"].sum()
total_conversions = df["conversions"].sum()
total_revenue = df["revenue"].sum()

print("Total Spend:", round(total_spend, 2))
print("Total Conversions:", total_conversions)
print("Total Revenue:", round(total_revenue, 2))

print("Overall ROAS:", round(total_revenue / total_spend, 2))
print(
    "Overall ROI:",
    round((total_revenue - total_spend) / total_spend * 100, 2)
)
print("\nChannel Performance:")

channel_performance = df.groupby("channel").agg({
    "impressions": "sum",
    "clicks": "sum",
    "spend": "sum",
    "conversions": "sum",
    "revenue": "sum"
}).reset_index()

channel_performance["CTR"] = (
    channel_performance["clicks"] /
    channel_performance["impressions"] * 100
)

channel_performance["Conversion_Rate"] = (
    channel_performance["conversions"] /
    channel_performance["clicks"] * 100
)

channel_performance["CPC"] = (
    channel_performance["spend"] /
    channel_performance["clicks"]
)

channel_performance["CPA"] = (
    channel_performance["spend"] /
    channel_performance["conversions"]
)

channel_performance["ROAS"] = (
    channel_performance["revenue"] /
    channel_performance["spend"]
)

channel_performance["ROI"] = (
    (channel_performance["revenue"] -
     channel_performance["spend"]) /
    channel_performance["spend"] * 100
)

print(channel_performance.round(2))
print("\nCampaign Performance:")

campaign_performance = df.groupby("campaign").agg({
    "spend": "sum",
    "conversions": "sum",
    "revenue": "sum"
}).reset_index()

campaign_performance["CPA"] = (
    campaign_performance["spend"] /
    campaign_performance["conversions"]
)

campaign_performance["ROAS"] = (
    campaign_performance["revenue"] /
    campaign_performance["spend"]
)

campaign_performance["ROI"] = (
    (campaign_performance["revenue"] -
     campaign_performance["spend"]) /
    campaign_performance["spend"] * 100
)

campaign_performance = campaign_performance.sort_values(
    by="revenue",
    ascending=False
)

print(campaign_performance.round(2))
print("\nMonthly Performance:")

df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_performance = df.groupby("month").agg({
    "spend": "sum",
    "conversions": "sum",
    "revenue": "sum"
}).reset_index()

monthly_performance["ROAS"] = (
    monthly_performance["revenue"] /
    monthly_performance["spend"]
)

monthly_performance["ROI"] = (
    (monthly_performance["revenue"] -
     monthly_performance["spend"]) /
    monthly_performance["spend"] * 100
)

print(monthly_performance.round(2))
import matplotlib.pyplot as plt

# Revenue by channel
revenue_by_channel = df.groupby("channel")["revenue"].sum()

plt.figure(figsize=(10, 6))
revenue_by_channel.plot(kind="bar")

plt.title("Revenue by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# ROAS by channel
roas_by_channel = df.groupby("channel").apply(
    lambda x: x["revenue"].sum() / x["spend"].sum()
)

plt.figure(figsize=(10, 6))
roas_by_channel.plot(kind="bar")

plt.title("ROAS by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("ROAS")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Monthly revenue
monthly_revenue = df.groupby(
    df["date"].dt.to_period("M").astype(str)
)["revenue"].sum()

plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind="line", marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Monthly ROAS
monthly_roas = df.groupby(
    df["date"].dt.to_period("M").astype(str)
).apply(
    lambda x: x["revenue"].sum() / x["spend"].sum()
)

plt.figure(figsize=(10, 6))
monthly_roas.plot(kind="line", marker="o")

plt.title("Monthly ROAS")
plt.xlabel("Month")
plt.ylabel("ROAS")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Top 10 campaigns by revenue
top_campaigns = (
    df.groupby("campaign")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_campaigns.sort_values().plot(kind="barh")

plt.title("Top 10 Campaigns by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Campaign")
plt.tight_layout()

plt.show()
# Top 10 campaigns by ROAS
campaign_roas = df.groupby("campaign").apply(
    lambda x: x["revenue"].sum() / x["spend"].sum()
)

top_roas_campaigns = campaign_roas.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
top_roas_campaigns.sort_values().plot(kind="barh")

plt.title("Top 10 Campaigns by ROAS")
plt.xlabel("ROAS")
plt.ylabel("Campaign")
plt.tight_layout()

plt.show()
# Conversions by channel
conversions_by_channel = df.groupby("channel")["conversions"].sum()

plt.figure(figsize=(10, 6))
conversions_by_channel.plot(kind="bar")

plt.title("Conversions by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("Conversions")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# CTR by channel
ctr_by_channel = df.groupby("channel").apply(
    lambda x: x["clicks"].sum() / x["impressions"].sum() * 100
)

plt.figure(figsize=(10, 6))
ctr_by_channel.plot(kind="bar")

plt.title("CTR by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("CTR (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# CPA by channel
cpa_by_channel = df.groupby("channel").apply(
    lambda x: x["spend"].sum() / x["conversions"].sum()
)

plt.figure(figsize=(10, 6))
cpa_by_channel.plot(kind="bar")

plt.title("CPA by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("CPA")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Save analysis results

channel_performance.to_csv(
    r"C:\Users\Anu\OneDrive\Desktop\Maketing campagin analysis\python\channel_performance.csv",
    index=False
)

campaign_performance.to_csv(
    r"C:\Users\Anu\OneDrive\Desktop\Maketing campagin analysis\python\campaign_performance.csv",
    index=False
)

monthly_performance.to_csv(
    r"C:\Users\Anu\OneDrive\Desktop\Maketing campagin analysis\python\monthly_performance.csv",
    index=False
)

print("\nAnalysis files saved successfully!")