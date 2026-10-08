import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Dataset load karein
df = pd.read_csv("sales_data.csv")

# 2. Data Cleaning
# Unnecessary column (Row ID) drop karein
if "Row ID" in df.columns:
    df.drop(columns=["Row ID"], inplace=True)

# Postal Code ko text (string) mein convert karein
if "Postal Code" in df.columns:
    df["Postal Code"] = df["Postal Code"].astype(str)

# Missing values hataein
df.dropna(inplace=True)

# 3. Sales Calculations
print("--- Sales Analysis Summary ---")
print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Average Sale: ${df['Sales'].mean():,.2f}")

# 4. Top 10 Locations (Postal Codes) by Sales
top_locations = (
    df.groupby("Postal Code")["Sales"].sum().sort_values(ascending=False).head(10)
)
print("\n--- Top 10 Postal Codes by Sales ---")
print(top_locations)

# 5. Visualization (Graph)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_locations.index, y=top_locations.values, palette="crest")
plt.title("Top 10 Postal Codes by Total Sales")
plt.xlabel("Postal Code")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Graph screen par show karne ke liye
plt.show()