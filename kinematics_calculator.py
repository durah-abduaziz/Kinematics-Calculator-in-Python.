while True:
    try:
        speed = float(input("Enter speed (meters / second) :"))
        if speed <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid numper.")

while True:
    try:
        time = float(input("Enter time (second): "))
        if time <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid numper.")

distance = speed * time
print(f"The distance traveld = {distance} meters")
again = input("Do you want to calculate again? (yes/no): ").lower()
if again != ("yes"):
    exit()

print("Calculating speed, time, or distance")

while True:
    try:
        choice = input("Choose calculation: (1) Speed  (2) Time  (3) Distance : ").strip()

        if choice == "1":  # Calculate speed
            distance = float(input("Enter the distance (in meters): "))
            time = float(input("Enter the time (in seconds): "))
            speed_m_s = distance / time

            unit = input("Choose the unit (m/s) or (km/h): ").lower()
            if unit == "km/h":
                speed = speed_m_s * 3.6
                print(f"Particle speed: {speed:.2f} km/h")
            else:
                print(f"Particle speed: {speed_m_s:.2f} m/s")

        elif choice == "2":  # Calculate time
            distance = float(input("Enter the distance (in meters): "))
            speed_m_s = float(input("Enter the speed (in m/s): "))
            time = distance / speed_m_s
            print(f"Time: {time:.2f} seconds")

        elif choice == "3":  # Calculate distance
            speed_m_s = float(input("Enter the speed (in m/s): "))
            time = float(input("Enter the time (in seconds): "))
            distance = speed_m_s * time
            print(f"Distance: {distance:.2f} meters")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            break

    except ValueError:
        print("Invalid input. Please enter numeric values.")
