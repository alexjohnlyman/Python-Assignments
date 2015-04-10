
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


# Option 2 with letter, 0, ".", and "enter" check
def get_input(message):
    user_input = str(raw_input(message))
    if user_input < "1":
        print("Cannot be 0 or a letter!")
    elif user_input.isdigit() and user_input is not 0 and user_input is not "" and user_input is not ".":
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