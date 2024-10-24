# CarFinder Program for AutoCountry

# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_vehicles():
    print("\nAuthorized Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
    print()  # Print a newline for spacing after the list

def main():
    while True:
        display_menu()
        user_input = input("\nEnter your choice: ")

        if user_input == '1':
            print_vehicles()
        elif user_input == '2':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please try again.")

# Program entry point
if __name__ == "__main__":
    main()