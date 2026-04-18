import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_excel("data/mo_financials.xlsx")

# Features (exclude Income Tax)
X = df[["Year", "Sales Tax ($)", "Other Revenue ($)"]]
y = df["Adjusted Balance ($)"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Predictions on test set (for evaluation)
y_pred = model.predict(X_test)

print("Predicted Budget Balances:", y_pred)
print("MSE:", mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)
print("R²:", r2)

comparison = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print(comparison)

# Predictions for full dataset (for visualization)
y_pred_all = model.predict(X)

# Plot
plt.scatter(y, y_pred_all, color="#6FB5CB", s=40, alpha=0.7)

# 45-degree reference line
min_val = min(y.min(), y_pred_all.min())
max_val = max(y.max(), y_pred_all.max())
plt.plot([min_val, max_val], [min_val, max_val], color="#E8A81A", linewidth=2)

plt.xlabel("Actual Adjusted Balance ($)")
plt.ylabel("Predicted Adjusted Balance ($)")
plt.title("Predicted vs Actual Adjusted Budget Balance")

# Format axes in billions
plt.gca().xaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f'{x/1e9:.1f}B')
)
plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda y, _: f'{y/1e9:.1f}B')
)

# Add R² annotation
plt.text(
    0.05, 0.95,
    f"R² = {r2:.2f}",
    transform=plt.gca().transAxes,
    verticalalignment='top'
)

plt.grid(alpha=0.3)

plt.show()