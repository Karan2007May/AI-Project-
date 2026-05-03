from sklearn.linear_model import LogisticRegression

# Data (hours studied)
X = [[1], [2], [3], [4]]

# Output (0 = Fail, 1 = Pass)
y = [0, 0, 1, 1]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

#Interact with User to get his study hours
print("Hey, I can predict if you will fail or not?\n Wanna know...\n \n .... I'm sure you want to!!")
yourhours = int(input("\nWell, How many hours do you study for? "))

# Predict
prediction = model.predict([[yourhours]])

print("\nPrediction for you: (0=Fail, 1=Pass):", prediction)

if prediction == [0]:
    print("\nOh you're quite a lazy bum. Keeping going and you will reach high....(whispers- Hehehe High poverty)")
else:
    print("\nOh well you'll pass....(whispers - that's not fun)")