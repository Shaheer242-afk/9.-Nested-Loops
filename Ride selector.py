print("===============================")
print("         Ride Selector         ")
print("===============================")
print()

print("Please select a vehicle")
print("1 - Bike")
print("2 - Car")
print()

choice = int(input("Please enter the number"))
print()

if choice == 1:
    print("Please select the Bike you want")
    print("1 - Scooter")
    print("2 - Mountain Bike")

    bike_type = int(input("Please enter the number"))
    print()

    if bike_type == 1:
      print("You Have selected the Scooter")
      print("Top speed = 80 kmph")
      print("Best for City roads")

    elif bike_type == 2:
      print("You Have selected the Mountain Bike")
      print("Top speed = 40 kmph")
      print("Best for Mountain Road")


elif choice == 2:
    print("Please select the Car you want")
    print("1 - Sedan")
    print("2 - Suv")

    car_type = int(input("Please enter the number"))
    print()

    if car_type == 1:
      print("You Have selected the Sedan")
      print("Seats = 5")
      print("Best for Family trips")

    elif car_type == 2:
      print("You Have selected the SUV")
      print("Seats = 7")
      print("Best for Offroad")

else:
   print("Please enter a valid answer")
   print("Please pick 1 for bike or 2 for car")

print("===============================")
print("     Custom ride is ready      ")
print("      Enjoy your Journey       ")
print("===============================")
print()