# Excercise number 6
# when you call your functions one of them will have a try except wrapped in there

# open function
def open_me(filename):
    with open(filename) as f:
        text = f.read()
        print text

# # Try function
def try_me(filename):
    try:
        open_me(filename)
    except IOError:
        print "File does not exist. Please choose another file."



# include the try_except and open_me in here
def try_and_open_me(filename):
    open_me(filename):
    def try_me(filename):

try_me("exercise_five_hive")




# Examples
# try:
#     fh = open("/tmp/blah/blah/blah", "w")
#     fh.write("This is my test file for exception handling!!")
# except IOError:
#     print "Error: can't find file or read data"
# else:
#     print "Written content in the file successfully"
#
# # An example with a finally block, without an except block
# try:
#     fh = open("/tmp/blah/blah/testfile", "w")
#     fh.write("This is my test file for exception handling!!")
# finally:
#     print "Error: can't find file or read data"