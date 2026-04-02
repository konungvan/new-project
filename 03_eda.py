# =========================
# REPORT 1
# =========================
# Считаем количество записей в каждом регионе.
# Показывает, где больше всего пользователей/активности.

report_1 = (
    df.groupby("region")
      .size()
      .sort_values(ascending=False)


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
