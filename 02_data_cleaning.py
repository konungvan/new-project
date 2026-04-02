# 1. Remove fully empty rows
df = df.dropna(how="all")

# 2. Fill NaN in traffic_gb_used
df["traffic_gb_used"] = df["traffic_gb_used"].fillna(0)

# 3. Convert plan limit to numeric (Unlimited -> NaN)
df["plan_limit_gb_num"] = pd.to_numeric(df["plan_limit_gb"], errors="coerce")

# 4. Create over_limit flag
df["over_limit"] = df["traffic_gb_used"] > df["plan_limit_gb_num"]