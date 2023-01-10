print("Welcome to the tip calculator")

bill = float(input("What was the total bill ? $"))

tip = float(input("What percentage tip would you like to give? 10, 12 or 15 ? $"))

split_by_people = float(input("How many perople to split the bill ? "))


print("Each person should pay $",(bill * (tip/100) + bill)/split_by_people)t