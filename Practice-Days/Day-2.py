from sklearn.linear_model import LogisticRegression

#Data (hours studied)
X = [[1], [2], [3], [4]]

#Output (0 = Fail, 1 = Pass)
y = [0, 0, 1, 1]

#Create Model
model = LogisticRegression()

#Train Model
model.fit(X, y)

#Predict
prediction = model.predict([[5]])

print("Prediction (0=Fail, 1=Pass):", prediction)