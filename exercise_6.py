# A good place to start:

# Excercise number 6
when you call your functions one of them will have a try except wrapped in there
def open_me(filename):
    with open(filename) as f:
        (more code)

try:
    open_me(filename)

except:
    IOError



def open_me_try_except()
#     include the try_except in here