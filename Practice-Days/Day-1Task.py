print("Hey! Hello, everyone!")

numbers = []
for i in range(5):
    num = input(f"\nCan you enter the {i+1} number?\n")
    numbers.append(int(num))

print("\nOkay, so the numbers are", numbers)

print("\nWell then the average is ", sum(numbers)/ len(numbers))

if int(sum(numbers)/len(numbers)) < 50:
    print("Ha Ha that's lower than 50, you fail!!!!")
else:
    print("Oh that's a good sequence, kinda disappointed though")