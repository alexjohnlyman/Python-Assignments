# I will have two functions (c->f) and (c<-f)
# Exercise 7

with open('exercise_7_temps.txt', 'r+') as f:
    text = f.readlines()
    no_commas = [i.replace(',', '') for i in text] #stripping quotes out of a list
    no_quotes = [i.replace('"', '') for i in no_commas] #stripping quotes out of a list
    final = zip(*[iter(no_quotes)]*1)
print final

# for key, value in thing:
#     print "%s ==> %s" % (key,value)



# # Function that creates a dictionary out of txt
# def temperature():
#     entry = {}
#     with open('exercise_7_temps.txt', 'r+') as f:
#         text = f.readlines()
#         no_quotes = [i.replace('"', '') for i in text] #stripping quotes out of a list
#         for i in no_quotes:
#             list = i.split()
#             zip(*[iter(list)]*2)
#             print list

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

# print c_or_f

# temperature()