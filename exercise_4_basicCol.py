# Sample Output:
#    ******************************
#     EXERCISE 4 - MENU
#    ******************************
#    1. Write input to file
#    2. Write input to screen
#    3. Quit
# ******************************
# Enter your choice [1-3] : 2
# Enter a phrase: Yet another phrase
# You entered: 'Yet another phrase'
# ******************************
#  EXERCISE 4 - MENU
# ******************************
# 1. Write input to file
# 2. Write input to screen
# 3. Quit
# ******************************
# Enter your choice [1-3] : 1
# Enter a phrase: This should be written out to a file
# Writing 'This should be written out to a file' to a file...
# Consider the following:
# - Extend this program to prompt the user until they enter menu option 3.


print "   ******************************"
print "       EXERCISE 4 - MENU"
print "   ******************************"
print "      1. Write input to file"
print "      2. Write input to screen"
print "      3. Quit"
print "   ******************************"




def get_input(message):
    user_input = str(raw_input(message))
    if user_input >= "1" and user_input <= "3":
        second_choice = str(raw_input("Enter a phrase:  "))
        if first_choice == "1":
            new_file = open('text.txt', 'w+')
            new_file.write(second_choice)
            new_file.close()
            print new_file
            return first_choice
        elif first_choice == "2":
            print "You entered: " + second_choice
            return first_choice
        else:
            print "You are quitting"
            return first_choice
    else:
        print("Must be 1, 2, 3")
        return None

first_choice = None
while first_choice is None:
    first_choice = get_input("Enter your choice [1-3]: ")






# def get_input(message):
#     user_input = str(raw_input(message))
#     if user_input >= "1" and user_input <= "3":
#         return user_input
#     else:
#         print("Must be 1, 2, 3")
#     return None
#
# def get_input_2(second_message):
#     user_input_2 = str(raw_input(second_message))
#     if first_choice == "1":
#         new_file = open('text.txt', 'w+')
#         new_file.write(first_choice)
#         new_file.close()
#         print new_file
#         return first_choice
#     elif first_choice == "2":
#         print "You entered: " + user_input_2
#         return None
#     else:
#         print "You are quitting"
#
#
# first_choice = None
# while first_choice is None:
#     first_choice = get_input("Enter your choice [1-3]: ")
#
# second_choice = None
# while second_choice is None:
#     second_choice = get_input_2("Enter a phrase:  ")


# John's way
# def choose():
#     print " Menu \n What would you like to do? \n 1. Write input to file \n 2. Write input to screen \n 3. Quit"
#     choice = raw_input("Which do you choose?: ")
#     if choice == "1":
#         text = raw_input("Type text here: ")
#         f = open('text.txt', 'a+')
#         f.write(text)
#         f.close
#         return choose()
#     elif choice == "2":
#         text = raw_input("Type text here: ")
#         print text
#         return choose()
#     elif choice == "3":
#         return choice
#     else:
#         print "Please choose 1, 2, or 3"
#         return choose()
# choose()


















