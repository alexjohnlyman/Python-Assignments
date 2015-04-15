# My string generator

import string
import random

def generate_ran():
    minLength = 1
    maxLength = 15
    for i in range(1, 11):
        length = random.randint(minLength, maxLength)
        chars = (''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(length)))
        with open('exercise_five.dat.txt', 'a+') as f:
            f.write(chars)
            f.write("\n")
generate_ran()


lines = {}
with open('exercise_five.dat.txt', 'r+') as f:
    text = f.readlines()
    for j in text:
        for i in j:
            if i in lines:
                lines[i] += 1
            else:
                lines[i] = 1

# this is tuple unpacking
for key, value in lines.items():
    print "%s ==> %s" % (key,value)


# for i in len(new_list):
#     lines.append(string + \n)
# return '\n'.join(lines)



# print person.items() # creates a list or key:value pairs or a tuple/ tuples are always in ()
#
# for key, val in person.items(): # this is tuple unpacking
#     print "%s ==> %s" % (key,value)
#
# with open('text.txt', 'r+') as f:
#     lines = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
#     f.writelines(lines) # this will write 3 new lines in the


# num_A = 'exercise_five.dat'.count("A")
# print num_A

## changing one letter in a file to be something else
# with open('exercise_five.dat.', 'r+') as f:
#     for i in f:
#         i = i.replace(i, i + " ")
#         f.writelines(i)





# sorted_list = sorted('exercise_five.dat')