#
# Will creating a class called student with the attribute 'name'
#
class student:
    name = 'student'

    def name_fun(self):
        return self.name
    #
    # __init__ function will be called at the time of instantiation
    #
    def __init__(self):
        self.name = 'default'

#
#Instantiate the student class
#
x = student()
#
# Following line will output as: 'name:default'
#
print('name:' + x.name_fun())

x.name = 'Aragon'
#
# Will print 'name:Aragon'
#
print('name:' + x.name_fun())
#
# Can also directly refer to name
#
print('name:' + x.name)
