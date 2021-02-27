# Kilometer to miles calculator
str1 = "KILOMETER TO MILES"
print(str1 + "\n" + "*" * (str.__len__(str1)))
inp = float(input("Please provide the kilometers here : "))
miles = round(inp * 0.621371, 2)
print(f"{inp} kilometers means {miles} Miles")
input()
