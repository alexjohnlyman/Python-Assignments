# My string generator
import string
import random

def generator(size=10, chars=string.ascii_uppercase + string.digits):
    second_choice = ''.join(random.choice(chars) for _ in range(size))
    new_file = open('exercise_five.dat.txt', 'w+')
    new_file.write(second_choice)
    new_file.close()
print generator()

new_list= [new_file]


# this is tuple unpacking
for key, value in new_file.items():
    print "%s ==> %s" % (key,value)

# for i in len(new_list):
#     lines.append(string + \n)
# return '\n'.join(lines)

#
# def insert_newlines(string):
#     lines = []
#     for i in len(string), every):
#         lines.append(string[i:i+every])
#     return '\n'.join(lines)


lines = []
#
# for char in 'exercise_five.dat.txt':
#     lines = char \n
#     print lines
#
# # puts each line into a list
# with open('exercise_five.dat.txt', 'r+') as f:
#     text = f.readlines()
#     for line in text:
#         lines = line.split()



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