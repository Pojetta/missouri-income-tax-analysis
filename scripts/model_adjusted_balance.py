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

# Define metrics (FIX)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Predicted Budget Balances:", y_pred)
print("MSE:", mse)
print("R²:", r2)

comparison = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print(comparison)

# Predictions for full dataset (for visualization)
y_pred_all = model.predict(X)

# Save model results to a text file
output_file = "model_results.txt"

with open(output_file, "w") as f:
    f.write("Model: Linear Regression\n\n")

    f.write("Performance Metrics:\n")
    f.write(f"R-squared (R^2): {r2:.4f}\n")
    f.write(f"Mean Squared Error (MSE): {mse:.4f}\n\n")

    f.write("Model Coefficients:\n")
    for name, coef in zip(X.columns, model.coef_):
        f.write(f"{name}: {coef:.4f}\n")

    f.write(f"\nIntercept: {model.intercept_:.4f}\n")

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