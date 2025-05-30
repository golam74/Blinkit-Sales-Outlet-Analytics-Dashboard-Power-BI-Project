# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Data 
data = pd.read_csv("C:/Users/MECH 5/OneDrive/New folder/New folder/BlinkIT Grocery Data.csv")  # Replace with your file path

# Basic Info
print("🔍 Dataset Info:\n")
print(data.info())
print("\n📊 Summary:\n", data.describe())

# Check for missing values
print("\n🧹 Missing Values:\n", data.isnull().sum())

# Top Item Types by Average Sales
top_items = data.groupby("Item Type")["Sales"].mean().sort_values(ascending=False)
print("\n💡 Top Item Types by Avg Sales:\n", top_items)

# Sales by Outlet Type
outlet_sales = data.groupby("Outlet Type")["Sales"].sum()
print("\n🏪 Total Sales by Outlet Type:\n", outlet_sales)

# Visualization - Sales by Item Type
plt.figure(figsize=(12, 6))
sns.barplot(x="Sales", y="Item Type", data=data.sort_values("Sales", ascending=False))
plt.title("Sales by Item Type")
plt.xlabel("Sales")
plt.ylabel("Item Type")
plt.tight_layout()
plt.show()

# Visualization - Sales by Outlet Type
plt.figure(figsize=(8, 5))
sns.boxplot(x="Outlet Type", y="Sales", data=data)
plt.title("Sales Distribution by Outlet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Analysis
corr = data[["Item Visibility", "Item Weight", "Sales"]].corr()
print("\n🔗 Correlation Matrix:\n", corr)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Year-wise Outlet Establishment Analysis
plt.figure(figsize=(10, 5))
sns.countplot(x="Outlet Establishment Year", data=data)
plt.title("Number of Outlets Established per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

