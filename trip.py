print("Trip expenditure")
days= int(input("Duration of your trip in days: "))
hotel= float(input("Hotel cost per days: "))
totalHotelCost= days*hotel

plane= float(input("Enter plane ticket cost: "))

vehicle= int(input("Enter the vehicle rental cost (per day): "))
totalVehicle= vehicle*days
totalExpenditure= totalHotelCost+plane+totalVehicle
print("\n")
print("Total expenditure:")
print("Total hotel cost= ", totalHotelCost)
print("Plane and vehicle rental amount=", plane+ totalVehicle)
print("Total Cost=", totalExpenditure)