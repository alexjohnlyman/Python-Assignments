baseball = {}

# I want to take the last part of the line and add that to the value portion of the key:value pair

positions = {}
with open('project_8.dat', 'r+') as f:
    text = f.readlines()
    for i in text:
        list = i.rsplit()
        for j in list:
            last = list[-1]
            for j in positions:
                positions[key] = list[-1]



print text
print list
print last
print positions


# for key, value in result:
#     print "%s ==> %s" % (key,value)


# words = {}
# with open('exercise_5_John.txt', 'r+') as f:
#     text = f.readlines()
#     for i in text:
#         list = i.split()
#         for j in list:
#             if j in words:
#                 words[j] += 1
#             else:
#                 words[j] = 1

