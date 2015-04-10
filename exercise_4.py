
#Option 1 - without the letter check
# years = float(raw_input("How many years: "))
#
# if years == 0:
#     years = float(raw_input("You cannot use 0. Please enter an amount of years into the future: "))
#
# population = 307357870
# seconds = (((((years)*365)*24)*60)*60)
# birth_rate = (seconds/7)
# death_rate = (seconds/13)
# immigrant_rate = (seconds/35)
# total_increase = ((birth_rate + immigrant_rate) - death_rate)
# new_population = (population + total_increase)
# print "New population in %i years will change by %.2f to be %.2f" % (years, total_increase, new_population)

# Option 2
def get_input(message):
    user_input = str(raw_input(message))
    if user_input.isdigit() and user_input is not "0" and user_input is not "" and user_input is not ".":
        user_input = float(user_input)
        return user_input
    else:
        print("Cannot be 0 or a letter!")
    return None

years = None

while years is None:
    years = get_input("Please enter an amount of years into the future: ")

population = 307357870
seconds = (((((years)*365)*24)*60)*60)
birth_rate = (seconds/7)
death_rate = (seconds/13)
immigrant_rate = (seconds/35)
total_increase = ((birth_rate + immigrant_rate) - death_rate)
new_population = (population + total_increase)
print "New population in %i years will change by %.2f to be %.2f" % (years, total_increase, new_population)

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