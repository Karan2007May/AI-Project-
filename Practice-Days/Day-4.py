from sklearn.linear_model import LogisticRegression

#Inputs: [hours studied, sleep hours]
X = [
    [1, 5],
    [2, 6],
    [3, 6],
    [4, 7],
    [5, 8] 
]

#Output (0 = Fail, 1 = Pass)
y = [0, 0, 1, 1, 1]

#Create Model
model = LogisticRegression()

#Train Model
model.fit(X, y)

#Predict
prediction = model.predict([[1, 15]])
print("Prediction:", prediction[0]) 