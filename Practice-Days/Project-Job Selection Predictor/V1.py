from sklearn.linear_model import LinearRegression

# Data (working exp. [years])
X = [[1], [2], [3], [4], [5]]

# Salary (in some units)
y = [20000, 30000, 40000, 50000, 60000]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

#Interact with User to get his study hours
print("Hey, I can predict your salary?\n\n Wanna know if I really can?...\n \n .... I'm sure you want to!!")
yourexp = float(input("\nWell, How many years of work experience you have? "))

# Predict
prediction = model.predict([[yourexp]])

print("\nWell I predict your salary is:", int(prediction[0]))

if prediction < [50000]:
    print("\nOh you're quite naive yet. Keeping going and you will reach somewhere high....(whispers- Maybe not)")
else:
    print("\nOh well you're quite a earner....(whispers - that's not fun)")