weight = float(input("Enter your weight: "))

unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not a valid weight unit.")
