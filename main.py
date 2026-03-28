
import pandas as pd

# =========================
# Project: Internet traffic analysis
# =========================

# 1. Load data
df = pd.read_csv("internet_traffic_jan_feb_mar.csv")

print("=== BASIC INFO ===")
print(df.info())
print()

# 2. Remove fully empty rows
df = df.dropna(how="all")

# 3. Fill NaN in traffic_gb_used
df["traffic_gb_used"] = df["traffic_gb_used"].fillna(0)

# 4. Convert plan limit to numeric (Unlimited -> NaN)
df["plan_limit_gb_num"] = pd.to_numeric(df["plan_limit_gb"], errors="coerce")

# 5. Create over_limit flag
df["over_limit"] = df["traffic_gb_used"] > df["plan_limit_gb_num"]

# =========================
# REPORT 1
# =========================
# Считаем количество записей в каждом регионе.
# Показывает, где больше всего пользователей/активности.

report_1 = (
    df.groupby("region")
      .size()
      .sort_values(ascending=False)
)

# =========================
# REPORT 2
# =========================
# Считаем средний объем трафика для тарифов
# только в регионах Bishkek и Osh.
# Помогает сравнить потребление трафика по тарифам в крупных городах.
report_2 = (
    df[df["region"].isin(["Bishkek", "Osh"])]
    .groupby("tariff_plan")["traffic_gb_used"]
    .mean()
)

# =========================
# REPORT 3
# =========================
# Выводим пользователей из Bishkek с тарифом Standard,
# которые превысили лимит трафика.
# Это список "проблемных" клиентов.

report_3 = df[
    (df["region"] == "Bishkek") &
    (df["tariff_plan"] == "Standard") &
    (df["over_limit"])
][["user_id", "traffic_gb_used", "month"]]

# =========================
# REPORT 4
# =========================
# Сводная статистика по каждому тарифу:
# общий трафик, средний трафик и количество уникальных пользователей.


report_4 = df.groupby("tariff_plan").agg(
    total_traffic=("traffic_gb_used", "sum"),
    avg_traffic=("traffic_gb_used", "mean"),
    unique_users=("user_id", "nunique")
)

# =========================
# REPORT 5
# =========================
# Топ-5 регионов по среднему объему потребленного трафика.
# Показывает, где пользователи наиболее активны.

report_5 = (
    df.groupby("region")["traffic_gb_used"]
      .mean()
      .sort_values(ascending=False)
      .head(5)
)

# =========================
# REPORT 6
# =========================
report_6 = df.groupby("tariff_plan")["traffic_gb_used"].agg(
    min_traffic="min",
    max_traffic="max"
)

# =========================
# REPORT 7
# =========================
limited = df[df["tariff_plan"] != "Unlimited"]

total_users = limited.groupby("tariff_plan")["user_id"].nunique()

violators = (
    limited.groupby(["tariff_plan", "user_id"])["over_limit"]
    .any()
    .reset_index()
    .query("over_limit == True")
    .groupby("tariff_plan")["user_id"]
    .nunique()
)

report_7 = pd.concat([total_users, violators], axis=1)
report_7.columns = ["total_users", "violators"]
report_7["violators"] = report_7["violators"].fillna(0).astype(int)
report_7["violation_percent"] = report_7["violators"] / report_7["total_users"] * 100

# =========================
# REPORT 8
# =========================
report_8 = pd.pivot_table(
    df,
    index="tariff_plan",
    columns="month",
    values="traffic_gb_used",
    aggfunc="sum"
)

# =========================
# PRINT ALL REPORTS
# =========================
print("\n=== REPORT 1: records by region ===")
print(report_1)

print("\n=== REPORT 2: avg traffic (Bishkek & Osh) ===")
print(report_2)

print("\n=== REPORT 3: problem users (Bishkek, Standard, over limit) ===")
print(report_3.head(10))

print("\n=== REPORT 4: tariff summary ===")
print(report_4)

print("\n=== REPORT 5: top-5 regions by avg traffic ===")
print(report_5)

print("\n=== REPORT 6: min / max traffic ===")
print(report_6)

print("\n=== REPORT 7: over limit analysis ===")
print(report_7)

print("\n=== REPORT 8: pivot table (traffic by month) ===")
print(report_8)
