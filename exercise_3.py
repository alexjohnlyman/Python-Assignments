
#Option 1 - without the letter check
mph = float(raw_input("Please enter a speed in miles/hour: "))
#Conversions
meter_hour = mph * 1609.34
barleycorn_day = meter_hour * 24
furlong_hour = mph * 1760
fortnight = 336 #hours in a fortnight
furlong_fort = furlong_hour * fortnight
mach = (((mph/60)/60)/5280)  #feet in a mile = 5280
PSL = ((meter_hour/60)/299792458)

if mph == 0:
    mph = float(raw_input("You cannot use 0. Please enter a speed in miles/hour: "))
print "Original speed in mph is: %.2f" %(mph)
print "Converted to barleycorn/day is: %.2e" %(barleycorn_day)
print "Converted to furlongs per fortnight is: %.2f" %(furlong_fort)
print "Converted to Mach number is: %.2f" %(mach)
print "Converted to the percentage of the speed of light is: %.2e" %(PSL)


# # option 2
# try
#
#     except
