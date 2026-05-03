noofsubjects = int(input("Hi! Can you let me know how many subjects you have? "))

print("\nOk enter the marks for these subjects then.")

marks = []
for i in range(noofsubjects):
    number = int(input(f"\nHow many did you score in {i+1} Subject?"))
    marks.append(number)

avg = sum(marks)/len(marks)

print("Average marks:", avg)

if avg > 50:
    print("Oh you passed. - Pass")
else:
    print("Hehehe you failed :> ")

