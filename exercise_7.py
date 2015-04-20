# I will have two functions (c->f) and (c<-f)
# Exercise 7

cities = {"Boston": "0 C", "Boise": "48 F", "Phoenix": "85 F", "Miami": "40 C", "Riverside": "30 C", "Baltimore": "32 F"}



# for key, value in thing:
#     print "%s ==> %s" % (key,value)



#
def temperature():
    converted_cities = {}
    for v in cities:
        for i in v:
            if i == "C":
                number = split.v()
                print number
                new_number = number * 33.8
                print new_number
                letter = "F"
                value = new_number + letter
                converted_cities[value].append(letter)

            # if i == "F":
            #     number, letter = split.v()
            #     new_number = ((number - 32)/1.8)
            #     letter = "F"
            #     key, value = new_number, letter
    print cities
            # if i == "F":
            #     number, letter = split.value(

temperature()

# def f2c():
#
#
# def c2f():




        # new_list = []
            # for j in list:
            #     new_list.append(j)
            # print new_list
        # print entry


# entry[new_list[0]] = new_list[1] + new_list[-1] #pushing to a dict
    # print entry
    # #which will print the value of key1


# for i in entry:
#     temp = entry[i]
#     c_or_f = temp[-1]


# with open('exercise_7_temps.txt', 'r+') as f:
#     text = f.readlines()
#     no_commas = [i.replace(',', '') for i in text] #stripping quotes out of a list
#     no_quotes = [i.replace('"', '') for i in no_commas] #stripping quotes out of a list
#     final = zip(*[iter(no_quotes)]*1)
# print final

    # text = f.readlines()
    # no_quotes = [i.replace('"', '') for i in text] #stripping quotes out of a list

    # for i in no_quotes:
    #     list = i.split()
    #     zip(*[iter(list)]*2)
    #     print list