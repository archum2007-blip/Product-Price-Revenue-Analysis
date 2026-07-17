import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    "Price": [20, 25, 30, 35, 40],
    "Bottles Sold": [120, 110, 90, 80, 70]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Create Revenue column
df["Revenue"] = df["Price"] * df["Bottles Sold"]

print("\nUpdated Dataset:")
print(df)

# Find highest revenue
highest_revenue = df["Revenue"].max()
best_price = df.loc[df["Revenue"].idxmax(), "Price"]

print("\nHighest Revenue:", highest_revenue)
print("Best Price:", best_price)

# Plot bar chart
plt.bar(df["Price"], df["Revenue"])
plt.title("Price vs Revenue")
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.show()
print("\nConclusion:")

print("The highest revenue earned is ₹2800, achieved at both ₹35 and ₹40.")
print("However, ₹35 is the better selling price because it generates the same revenue while selling more bottles.")
print("Therefore, the shop owner should choose ₹35 as the selling price.")