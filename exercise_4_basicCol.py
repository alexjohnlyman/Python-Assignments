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

def get_input():
    first_choice = str(raw_input("Enter your choice [1-3]: "))
    if first_choice >= "1" and first_choice <= "3":
        if first_choice == "1":
            second_choice = str(raw_input("Enter a phrase to write to a file:  "))
            new_file = open('text.txt', 'w+')
            new_file.write(second_choice)
            new_file.close()
            return get_input()
        elif first_choice == "2":
            second_choice = str(raw_input("Enter a phrase to print to the screen:  "))
            print "You entered: " + second_choice
            return get_input()
        elif first_choice == "3":
            print "You are quitting"
    else:
        print("Must be 1, 2, 3")
        return get_input()

get_input()
