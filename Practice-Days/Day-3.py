from sklearn.linear_model import LinearRegression

# Data
X = [[1], [2], [3], [4], [5]]
y = [20000, 30000, 40000, 50000, 60000]

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
pred = model.predict([[5]])

print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

print("Predicted Salary:", int(pred[0]))