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
