
import pandas as pd

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Display first five rows
print("First Five Rows")
print(df.head())

# Display dataset information
print("\nDataset Information")
print(df.info())

# Display dataset size
print("\nDataset Shape")
print(df.shape)

# Display column names
print("\nColumn Names")
print(df.columns)

# Display churn count
print("\nChurn Distribution")
print(df["Churn"].value_counts())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("\nMissing Values After Conversion")
print(df.isnull().sum())

# Remove missing rows
df = df.dropna()
print("\nShape After Removing Missing Values")
print(df.shape)

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates")
print(df.shape)

print("\nData Types")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")


import os

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Total Customers
total_customers = len(df)

print("\nTotal Customers:", total_customers)

# Churn Rate
churn_rate = (df["Churn"] == "Yes").mean() * 100

print(f"Churn Rate: {churn_rate:.2f}%")
avg_monthly = df["MonthlyCharges"].mean()

print(f"Average Monthly Charges: ₹{avg_monthly:.2f}")
avg_tenure = df["tenure"].mean()

print(f"Average Tenure: {avg_tenure:.2f} months")

import matplotlib.pyplot as plt

gender_counts = df["gender"].value_counts()

plt.figure(figsize=(6,4))
gender_counts.plot(kind="bar")
plt.title("Customer Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("images/gender_distribution.png")
plt.show()

plt.figure(figsize=(6,4))

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Customers")

plt.tight_layout()
plt.savefig("images/churn_distribution.png")
plt.show()

contract_churn = pd.crosstab(df["Contract"], df["Churn"])

plt.figure(figsize=(7,5))

contract_churn.plot(kind="bar")

plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Customers")

plt.tight_layout()
plt.savefig("images/contract_churn.png")
plt.show()

internet_churn = pd.crosstab(df["InternetService"], df["Churn"])

plt.figure(figsize=(7,5))

internet_churn.plot(kind="bar")

plt.title("Internet Service vs Churn")
plt.xlabel("Internet Service")
plt.ylabel("Customers")

plt.tight_layout()
plt.savefig("images/internet_churn.png")
plt.show()

payment_churn = pd.crosstab(df["PaymentMethod"], df["Churn"])

plt.figure(figsize=(8,5))

payment_churn.plot(kind="bar")

plt.title("Payment Method vs Churn")
plt.xlabel("Payment Method")
plt.ylabel("Customers")

plt.tight_layout()
plt.savefig("images/payment_churn.png")
plt.show()

df.to_csv("dashboard_data.csv", index=False)

print("\nDashboard data saved successfully!")