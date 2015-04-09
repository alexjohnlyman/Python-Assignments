
#Option 1 - without the letter check
mph = float(raw_input("Please enter a speed in miles/hour: "))
#Conversions
meter_hour = mph * 1609.34
barleycorn_day = meter_hour * 24
furlong =
CarDi = mph * 20
energy = (mph * 115000)/75700
cost = mph * 4

if mph == 0:
    mph = float(raw_input("You cannot use 0. Please enter a speed in miles/hour: "))

print "Original speed in mph is: %f" %(mph)
print "%f mph is equivalent of %f liters" %(mph, liter)
print "%f mph of gasoline requires %f barrels of oil" %(mph, barrel)
print "%f mph of gasoline produces %f pounds of CO2" %(mph, CarDi)
print "%f mph of gasoline is energy equivalent to %f mph of ethanol" %(mph, energy)
print "%f mph of gasoline requires $%f US dollars" %(mph, cost)


# # option 2
# try
#
#     except
