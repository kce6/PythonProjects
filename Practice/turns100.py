print("Hello!\n")
name = input("What is your name? > ")
print("\n")
age = int(input("What is your age? > "))
print("\n")
repeats = int(input("Please enter a random number > "))

current_year = 2018
years_till_100 = 100 - age
turns100 = current_year + years_till_100

for num in range(repeats):
    print("By my calculations, %s will turn 100 years old in the year %s\n" % (name, turns100))
