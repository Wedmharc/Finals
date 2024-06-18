def mm_to_cm():
    mm = float(input("Enter a value in millimeters: "))
    cm = mm / 10
    print(f"{mm} millimeters is equal to {cm} centimeters.")

def ft_to_m():
    ft = float(input("Enter a value in feet: "))
    m = ft * 0.3048
    print(f"{ft} feet is equal to {m} meters.")

def km_to_mi():
    km = float(input("Enter a value in kilometers: "))
    mi = km * 0.621371
    print(f"{km} kilometers is equal to {mi} miles.")

def oz_to_g():
    oz = float(input("Enter a value in ounces: "))
    g = oz * 28.3495
    print(f"{oz} ounces is equal to {g} grams.")

def c_to_f():
    c = float(input("Enter a value in Celsius: "))
    f = c * 9/5 + 32
    print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit.")

def main():
    print("Measurement Converter")
    print("1. Millimeters to Centimeters")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Ounces to Grams")
    print("5. Celsius to Fahrenheit")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        mm_to_cm()
    elif choice == "2":
        ft_to_m()
    elif choice == "3":
        km_to_mi()
    elif choice == "4":
        oz_to_g()
    elif choice == "5":
        c_to_f()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()