hello = "\nHello there! Please, write your age for view price.\n"

while True:
    age = input(hello)
    age = int(age)
    if age < 3:
        print("Price is $0")
    elif age == 100:
        break
    elif 3 <= age <= 12:
        print("Price is $10")
    elif age > 12:
        print("Price is $15")
