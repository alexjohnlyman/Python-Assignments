# My string generator
import operator

words = {}
with open('exercise_5_John.txt', 'r+') as f:
    text = f.readlines()
    for i in text:
        list = i.split()
        for j in list:
            if j in words:
                words[j] += 1
            else:
                words[j] = 1

# John's way of sorting
sorted_dict = sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True)
print sorted_dict

for key, value in sorted_dict():
    print "%s ==> %s" % (key,value)

# sorted(words.items(), key=lambda sorted_dict: sorted_dict[1])

# with open('exercise_5_John.txt', 'r+') as f:
#     text = f.readlines()
#     sorted(words.values(), reverse=True)
#
# sorted_list = sorted(words.values(), reverse=True)
# print sorted_list
#



# s = sorted(words, key=words.values__getitem__)
# print s



# words = sorted(words, key=lambda words: words[0])
# sorted(words, key=lambda k: words[k][1])
# x = [k for (k,v) in sorted(words.items(), key=lambda (k, v): v[1])]
# sorted_list = sorted(words.items)
#
# def getKey(item):
#     return item[1]
# print sorted(words, key=getKey(words))


