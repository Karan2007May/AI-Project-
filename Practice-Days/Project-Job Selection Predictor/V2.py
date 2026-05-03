from sklearn.linear_model import LogisticRegression

#Inputs: [Skills Score, Communication Score, Experience]]
X = [
    [7, 6, 1],
    [8, 7, 2],
    [5, 5, 0],
    [9, 8, 3] 
]

#Output (0 = Fail, 1 = Pass)
y = [1, 1, 0, 1]

#Create Model
model = LogisticRegression()

#Train Model
model.fit(X, y)

#Predict
prediction = model.predict([[7, 6, 1]])
print("Prediction:", prediction[0]) 