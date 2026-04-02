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
# REPORT 4
# =========================
# Сводная статистика по каждому тарифу:
# общий трафик, средний трафик и количество уникальных пользователей.


report_4 = df.groupby("tariff_plan").agg(
    total_traffic=("traffic_gb_used", "sum"),
    avg_traffic=("traffic_gb_used", "mean"),
    unique_users=("user_id", "nunique")
)