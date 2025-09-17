def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("Welcome to the Physics Calculator (Speed, Time, Distance)")

while True:
    print("\nChoose calculation:")
    print("1 - Speed")
    print("2 - Time")
    print("3 - Distance")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    if choice == "1":  # Calculate speed
        distance = get_positive_float("Enter the distance (meters): ")
        time = get_positive_float("Enter the time (seconds): ")
        speed_m_s = distance / time
        unit = input("Choose the unit (m/s or km/h): ").lower()
        if unit == "km/h":
            speed = speed_m_s * 3.6
            print(f"Speed: {speed:.2f} km/h")
        else:
            print(f"Speed: {speed_m_s:.2f} m/s")

    elif choice == "2":  # Calculate time
        distance = get_positive_float("Enter the distance (meters): ")
        speed = get_positive_float("Enter the speed (m/s): ")
        time = distance / speed
        print(f"Time: {time:.2f} seconds")

    elif choice == "3":  # Calculate distance
        speed = get_positive_float("Enter the speed (m/s): ")
        time = get_positive_float("Enter the time (seconds): ")
        distance = speed * time
        print(f"Distance: {distance:.2f} meters")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break

