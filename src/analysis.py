import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv('data/inventory_q2024.csv')

print("Quarterly Data:\n", df)

# Compute average
avg = df['inventory_turnover'].mean()
print(f"Computed Average Inventory Turnover (2024): {avg:.2f}")

# Save average for verification
with open("computed_average.txt", "w") as f:
    f.write(f"{avg:.2f}")

# Visualization
benchmark = 8
quarters = df['quarter']
values = df['inventory_turnover']

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
