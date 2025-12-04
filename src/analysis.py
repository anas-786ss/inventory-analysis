import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv('data/inventory_q2024.csv')

print("Quarterly Data:\n", df)

# Filter invalid data
valid_df = df[df['inventory_turnover'] >= 0]
if len(valid_df) < len(df):
    print(f"Warning: Excluded {len(df) - len(valid_df)} records with negative turnover.")
    print("Excluded data:\n", df[df['inventory_turnover'] < 0])

# Compute average
avg = valid_df['inventory_turnover'].mean()
print(f"Computed Average Inventory Turnover (2024): {avg:.2f}")

# Save average for verification
with open("computed_average.txt", "w") as f:
    f.write(f"{avg:.2f}")

# Visualization
benchmark = 8
quarters = valid_df['quarter']
values = valid_df['inventory_turnover']

plt.figure(figsize=(8,4))
plt.plot(quarters, values, marker='o', linewidth=2)
plt.axhline(benchmark, color='red', linestyle='--', label='Industry Target = 8')
plt.title('Inventory Turnover Ratio — 2024 Quarterly Trend')
plt.xlabel('Quarter')
plt.ylabel('Inventory Turnover Ratio')
plt.legend()
plt.tight_layout()

plt.savefig("viz/inventory_trend.png")
print("Visualization saved to viz/inventory_trend.png")
