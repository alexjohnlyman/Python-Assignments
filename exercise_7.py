# I will have two functions (c->f) and (c<-f)
# Exercise 7

cities = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}


def c2f(ctemp):
    return ((ctemp * 9)/5)+32.0


def f2c(ftemp):
    return ((ftemp -32)*5)/9

def convert_temperatures(city_temps):
    for city, temps in city_temps.iteritems():
        split = temps.split()
        if split[1] == "F":
            new_temp = f2c(int(split[0]))
            print "In %s it is %s degrees Fahrenheit, which is equivalent to %s degrees Celsius" % (city, temps, new_temp)
        if split[1] == "C":
            new_temp = c2f(int(split[0]))
            print "In %s it is %s degrees Fahrenheit, which is equivalent to %s degrees Celsius" % (city, temps, new_temp)


convert_temperatures(cities)



# def f2c():
#
#
# def c2f():

# Tuples
# get
    # Takes 2 parameters, a key and a default value
# has_key
    # Deprecated in Python 3 - use the in keyword
# items
    # Returns a list of tuples
# keys
    # Returns a list of keys
# values
    # Returns a list of values


# Bob's solution
# from temperature import f2c, c2f
#
# def c2f(ctemp):
#     return (ctemp * 1.8) + 32.0
#
#
# def f2c(ftemp):
#
# temps_dict = {
#     "Boston": "0 C",
#     "Boise": "48 F",
#     "Phoenix": "85 F",
#     "Miami": "40 C",
#     "Riverside": "30 C",
#     "Baltimore": "32 F"
# }
#
#
# def conversion(city_temps):
#     for city, temp in city_temps.iteritems():
#         split = temp.split()
#         if split[1] == "F":
#             new_temp = f2c(int(split[0]))
#             print "In %s it is %s degrees Fahrenheit,\n\t which is equivalent to %s degrees Celsius" % (city, temp, new_temp)
#
#         if split[1] == "C":
#             new_temp = c2f(int(split[0]))
#             print "In %s it is %s degrees Celsius,\n\t which is equivalent to %s degrees Fahrenheit" % (city, temp, new_temp)
#
# conversion(temps_dict)
