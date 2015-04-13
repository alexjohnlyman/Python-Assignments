# # "is a" relationship is the same as inheritance
# class Fish (object):   you will want to put 'object' when defining a new class
#     Pass
# class Salmon (Fish):
#     Pass
#


# class = Person(object):
#       person_count = 0
#       some_variable = 5
#         Methods (or functions inside of classes)
#          def __init__(self):   (you will need to specify a name for  bob = Person("Bob") from then on)
#               self.name = name
#               self.message = message
#               Person.person_count += 1
#          def speak(self):
#               print self.message          (would print bob's message)
#               print "%s says: %s" % (self.name, self.message)
#           def __str__(self):
#               return self.name + " is the best"

# bob = Person()
#
# print isinstance(bob, Person) (Will return true)
#
# print bob.some_variable (will return 5)
# print Person.some_variable (will also return 5)
#
#
# bob.age = 30 (to add a new attribute that was not previously defined in the class)
# print bob.age
# print bob.__dict_ (this would print out the key and values pairs of the object)
#
#print bob (for the string)
#
#
#hasattr()     (this will take 2 arg and an object and return True/False if that object has the attribute)
# print hasattr(bob, "age") --> True
#
#getattr()      (this will return the value of the key of the object that you specified)
# print getattr(bob, "age")
#
#setattr()      (object, attr, value of attr)
# setattr(bob, "age", 31)
#  print bob.age
#
# delattr(bob, "age")
#  print bob.age   --> False
#
#
# To return the name of the object, like in the recipe organizer
# def __str__(self):
#     return str.name

# Garbage collection (this would remove bob from memory after the program runs, although you wouldn't really use this)
# def __del__(self):
#     print "Removing this from memory"
#
# class Recipe():
#
#     def __init__(self, name, description, directions):
#         self.name = name
#         self.descripton = description
#         self.direction = directions
#
# spaghetti = Recipe("Spaghetti", "Yummy", "Cook")
# print spaghetti.name


# JAYS NOTES
# class Person(object):
# some_variable = 5
#
#
# bob = Person() # this is instantiating an object of the Person class
# mary = Person() # this is instantiating an object of the Person class
#
# print isinstance(bob, Person)  # return true because bob is an instance if the Person class
# print bob.some_variable  # will print some_variable from the Person class
# print mary.some_variable  # will print some_variable from the Person class
# print Person.some_variable  # will print some_variable from the Person class

########################################################################################################################
#
# class Person(object):
#     some_variable = 5
#     person_count = 0  # initialize the person_count variable
#
#     def __init__(self, name, message):  # this is called a function a method in a class is referred to as a function.
#         print "Hitting the __init__ method"  # will print when any object is instantiated
#         self.name = name  # defines name attribute of the Person object
#         self.message = message  # defines name attribute of the Person object
#         Person.person_count += 1  # will increment whenever a new object is created
#
#     def __add__(self, other):
#         return "{} and {}".format(self.name,
#                                   other.name)  # will be called when 2 objects are in this form= <object> + <object>
#
#     def speak(self):
#         print "{} says: {}".format(self.name, self.message)  # will return this if the <object name>.speak() is called
#
#     def __str__(self):  # Will be called when just the object name is referenced, ie, < print bob >
#         return self.name + " is the best!"
#
#
# print Person.person_count  # no objects have been created, so this will print 0
#
# bob = Person("Bob", "Hi there")  # this is instantiating an object of the Person class named "Bob"
# mary = Person("Mary", "I'm Mary")  # this is instantiating an object of the Person class named "Mary"
# print bob
# bob.speak()  # will do what is in the Person speak() function for the object bob
# mary.speak()  # will do what is in the Person speak() function for the object mary
#
# print bob.name  # using dot notation we will reference the name attribute of the object
#
# bob.age = 30  # age does not exist in the object, so it is created for this object only
# print bob.age
#
# print bob.__dict__  # will print out a dictionary of bob's attributes and will contain age
# print mary.__dict__  # will print out a dictionary of mary's attributes, will not contain age
#
# print bob + mary  # will do what is in the __add__ function for the object bob, using mary as a second parameter
# print Person.person_count  # two objects have been created, bob and mary, so this will print 2
#
# print hasattr(bob, "age")  # return a True or False depending on whether the attribute exists
# print hasattr(mary, "age")  # return a True or False depending on whether the attribute exists
#
# print getattr(bob, "age")
#
# setattr(bob, "age", 31)  # sets the age attribute to 31
#
# print bob.age
#
# delattr(bob, "age")  # this will delete the actual attribute, not just the value
#
# print bob.age  # will throw and exception, because we removed bob's age attribute

#######################################################################################################################




# class Recipe():
#     def __init__(self, name, description, directions):  # must reference each
#         self.name = name
#         self.description = description
#         self.directions = directions
#
#
# spaghetti = Recipe("Spaghetti", "Blah", "Blah Blah")  # instantiate instance of the Recipe class named spaghetti
#                                                       # when creating an object you must send the same amount of
#                                                       # attributes as it is expecting in the __init__
#
#
#
#
#
# #######################################################################################################################

class car():
    wheels = "4 wheels"
    def __init__(self, color, year, owner, model):
        self.color = color
        self.year = year
        self.owner = owner
        self.model = model
    def __str__(self):
        return "{} has a {} {} with {}".format(self.owner, self.color, self.year, self.wheels)

car1 = car("white", 2003, "Jessica", "Dodge")
car2 = car("black", 2001, "Jim", "Ford")
car3 = car("yellow", 1985, "J", "BMW")

print car1
print car2
print car3











