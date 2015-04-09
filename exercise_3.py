
#option 1
gal = float(raw_input("Please enter the number of gallons of gasoline: "))
liter = gal * 3.7854
barrel = gal / 19.5
CarDi = gal * 20
energy = (gal * 115000)/75700
cost = gal * 4

if gal == 0:
    gal = float(raw_input("You cannot use 0. Please enter the number of gallons of gasoline: "))

print "Original number of gallons is: %f" %(gal)
print "%f gallons is equivalent of %f liters" %(gal, liter)
print "%f gallons of gasoline requires %f barrels of oil" %(gal, barrel)
print "%f gallons of gasoline produces %f pounds of CO2" %(gal, CarDi)
print "%f gallons of gasoline is energy equivalent to %f gallons of ethanol" %(gal, energy)
print "%f gallons of gasoline requires $%f US dollars" %(gal, cost)


# option 2
try

    except
