print("=== Electrical Engineering Calculator ===")
print()
print("1. Calculate Current (I = V/R)")
print("2. Calculate Voltage (V = I * R)")
print("3. Calculate Resistance (R = V/I)")
print("4. Calculate Power (P = V * I)")
print()
choice = input("Choose an option (1-4): ")
if choice == "1":
   try:
    V = float(input("Enter Voltage (V): "))
    R = float(input("Enter Resistance (Ohms): "))
    print("Current =", round(V/R, 2), "Amps")
   except ValueError:
    print("Invalid Input, Please enter a number.")
   except ZeroDivisionError:
       print("Value Cannot be Zero, Please enter another value.")
elif choice == "2":
   try:
    I = float(input("Enter Current (Amps): "))
    R = float(input("Enter Resistance (Ohms): "))
    print("Voltage =", round(I*R, 2), "Volts")
   except ValueError:
       print("Invalid Input, Please enter a number.")

elif choice == "3":
   try:
    V = float(input("Enter Voltage (V): "))
    I = float(input("Enter Current (Amps): "))
    print("Resistance =", round(V/I, 2), "Ohms")
   except ValueError:
    print("Invalid Input, Please enter a number.")
   except ZeroDivisionError:
       print("Value Cannot be Zero, Please enter another value.")

elif choice == "4":
   try:
    V = float(input("Enter Voltage (V): "))
    I = float(input("Enter Current (Amps): "))
    print("Power =", round(V*I, 2), "Watts")
   except ValueError:
    print("Invalid Input, Please enter a number.")
else:
    print("Invalid Choice, Please choose a number between (1 and 4)")

input("Please Enter to exit...")


