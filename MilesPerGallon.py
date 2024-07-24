#Display the title
print("                            ")
print("Miles Per Gallon Application")
print("-----2023 Nissan Altima-----")
print("----------------------------")

#User input
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_driven = float(input("Enter gallons of gas used:\t"))

#Calculations from user input
mpg = miles_driven / gallons_driven
mpg = round(mpg, 2)
totalMiles = miles_driven
gasUsed = gallons_driven

#Display results and testing inputs
if mpg > 37 and totalMiles > 599.4 and gasUsed > 16.2:
    print("This is not possible for your car!")
else:
    print(f"Miles Per Gallon:\t\t{mpg}")

