#The program allows users to find authorized vehicles.

import sys # Import the sys module at the beginning

#Allowed Vehicles List
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

#Dislplay Menu 
print("*********************************")
print("AutoCountry Vehicle Finder v0.1")
print("*********************************")
print("Please enter the following number below form the following menu:")
print("1. PRINT all Authorized Vehicles")
print("2. Exit")

# Ask user for input
choice = input("Enter your choice: ")

#Process user choice
if choice == "1":
  print("Authorized Vehicles:")
  for vehicle in AllowedVehiclesList:
    print(vehicle)
elif choice == "2":
   print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
   input("Please Enter to exit...")
   sys.exit() # Exit the program 
else:
  print("Invalid choice. Please enter a valid option.")

#Display Menu again
print("********************************")
print("AutoCountry Vehicle Finder v0.1")
print("********************************")
print("Please enter the following number below form the following menu:")
print("1. PRINT all Authorized Vehicles")
print("2. Exit")
