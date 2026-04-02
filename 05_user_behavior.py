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


