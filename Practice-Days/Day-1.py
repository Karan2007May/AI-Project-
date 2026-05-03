name = "Karan"
age = 19

print ("My name is", name)
print("I am", age, "years old")
if age >= 18:
    print("I can vote.")
else:
    print("I can't vote yet.")

for i in range(1,6):
    print("AI is the best, and I told it to", i)
print(f"Yeah! Yeah! {i} people.")

print("I also know multiplication tables: ")

table2 = [2, 4, 6, 8, 10]

print("Table of 2 starts with", table2[0])
for t in table2:
    if t != 2:
        print("And then", t)

print("Till ten it totals out to be", sum(table2))