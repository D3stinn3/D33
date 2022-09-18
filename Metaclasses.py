"""object creation and manipulation via metaclasses"""

class The_Object_Creator(object):

    """this is an class and object instance"""

    pass

my_object = The_Object_Creator() # classes are objects too

# as soon as you pass in the class, python execs and creates an object form the class
print(my_object)


# the my_object which in this case is an instance, is able hatch other objects
# the class/object instance can be assigned a variable which in tis case is the my_object
# the class/object instance can also be copies since it can be assigned as a variable
# the class/object instance can be added on attributes to it
# the class/object instance can also be passed as a function parameter


print(The_Object_Creator) # the class can be printed out because it is an object

def echo(o = The_Object_Creator): # the class can be parsed as a paramter

    return o

print(echo())

attribute_check = hasattr(The_Object_Creator, 'new_attribute') # this checks if the class has an attribute, as new_attribute

# The class/object instance has no attribute and will return False
# However when assigned an attribute, the latter changes!

attribute_assignment = The_Object_Creator.__doc__

attribute_check2 = hasattr(The_Object_Creator, '__doc__')


"""to check the attribute assignments using if statements"""

if attribute_check is True:

    print('first check is True')

else:
    print('first check is False')

if attribute_check2 is True:

    print('second check is True and... ' + str(attribute_assignment))
else:
    print('second check is False')


"""if classes are objects then they too can be passed in like any other object"""


def Destiny(obj):

    if obj == 'Destinne' and iter(obj):

        class Foo:

            def __init__(self, second_object):

                self.second_object = second_object

        class ObjS(Foo):

            def __init__(self):
                pass

            def deep_obj(self):

                print(f'{obj} and {self.second_object} are the same!')

        return Destiny
    
    else:

        class Maria:
            pass

        return Maria


object_Destinne = Destiny('Maria') # gives a local argument  inside class Maria
print(object_Destinne)




