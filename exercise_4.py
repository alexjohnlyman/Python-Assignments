
#Option 1 - without the letter check
years = raw_input("How many years: ")

population = 307357870
seconds = (((((years)*365)*24)*60)*60)
birth_rate = population +=
death_rate =
immigrant_rate =
total_increase = (birth_rate + immigrant_rate) - death_rate
new_population = (population += total_increase)



if mph == 0:
    mph = float(raw_input("You cannot use 0. Please enter a speed in miles/hour: "))
print "New population in %i years will change by %f to be %f" %(years, total_increase, new_population)









# # option 2 letter check
# def get_info():
#     mph = raw_input("Please enter a speed in miles/hour: ")
#     if mph.isdigit() and float(mph) > 0:
#         return mph
#     else:
#         print "You can't enter 0 or a word. Try again."
#         return get_info()
#
#
# mph = get_info()
# meter_hour = float(mph) * 1609.34
# barleycorn_day = meter_hour * 24
# furlong_hour = mph * 1760
# fortnight = 336 #hours in a fortnight
# furlong_fort = furlong_hour * fortnight
# mach = (((mph/60)/60)/5280)  #feet in a mile = 5280
# PSL = ((meter_hour/60)/299792458)
#
# print "Original speed in mph is: %.2f" %(mph)
# print "Converted to barleycorn/day is: %.2e" %(barleycorn_day)
# print "Converted to furlongs per fortnight is: %.2f" %(furlong_fort)
# print "Converted to Mach number is: %.2f" %(mach)
# print "Converted to the percentage of the speed of light is: %.2e" %(PSL)
#
# jared solution to look at
# def get_input(message):
#         user_input = str(raw_input(message))
#         sanitized_input = ""
#         dot_count = 0
#         for char in user_input:
#             if char.isdigit() or (char is "." and dot_count < 1):
#                 if char is ".":
#                     dot_count += 1
#                 sanitized_input = str(sanitized_input + char)
#             elif char is ".":
#                 dot_count += 1
#         if sanitized_input is not "0" and sanitized_input is not "" and sanitized_input is not ".":
#             sanitized_input = float(sanitized_input)
#             if dot_count > 1:
#                 print("You entered multiple '.' so we assumed you meant only the first one. ;)")
#             print "Your original input was '{}' but we extracted {} gallons.".format(user_input, sanitized_input)
#             return sanitized_input
#         print("Cannot be 0 or a letter!")
#         return None
#
# gallons = None
#
# while gallons is None:
#     gallons = get_input("Please input the number of gallons: ")
#
#
# liters = gallons * 3.7854
# barrels = round(gallons / 19.5, 2)
# co2 = round(gallons * 20, 2)
# ethanol = round((gallons * 115) / 75.7, 2)
# price = round(gallons * 4.00, 2)
#
# print "Total liters: {} liters".format(liters)
# print "Number of barrels of oil required: {} barrels".format(barrels)
# print "Number of pounds of CO2 produced: {}lbs".format(co2)
# print "Equivalent energy amount of ethanol gas: {} gallons. That is a difference of {} gallons."\
#     .format(ethanol, round(ethanol - gallons, 2))
# print "Total cost: ${}".format(price)