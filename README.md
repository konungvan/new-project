Internet Traffic Analysis

This project analyzes internet usage data across different regions and tariff plans to identify user behavior, traffic patterns, and potential issues such as exceeding data limits.

---

Project Goals

 Analyze user distribution by region
 Compare traffic usage across tariff plans
 Identify users exceeding their limits
 Detect high-traffic regions
 Analyze monthly traffic trends

---

 Dataset

The dataset contains:
 user_id — unique user identifier
 region — user location
 tariff_plan — tariff type
 traffic_gb_used — data usage
 plan_limit_gb — traffic limit
 month — month of usage

---

 Technologies Used

 Python
 Pandas

---

Key Analysis

### 1. Data Cleaning
 Removed empty rows
 Filled missing traffic values
 Converted plan limits to numeric
 Created "over_limit" flag

### 2. Exploratory Data Analysis
 Users distribution by region
 Top regions by traffic
 Min/Max usage per tariff

### 3. Tariff Analysis
 Average traffic usage by tariff
 Total and average traffic
 Unique users per plan

### 4. User Behavior Analysis
 Users exceeding limits
 Violation percentage by tariff

### 5. Time Analysis
 Monthly traffic trends using pivot tables

---

Key Insights

 Some regions show significantly higher average traffic usage
 Standard plan users frequently exceed limits
 Certain tariffs have higher violation percentages
 Traffic usage varies significantly by month

---

How to Run

```bash
pip install -r requirements.txt
python main.py
