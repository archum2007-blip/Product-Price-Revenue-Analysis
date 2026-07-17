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