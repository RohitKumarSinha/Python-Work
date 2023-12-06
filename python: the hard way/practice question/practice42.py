# # MyClass is a object
# class MyClass:
# 	"This is my second class"
# 	a = 10
#     # MyClass has-a method func
# 	def func(self):
# 		print('Hello')
#
# # create a new MyClass
# # ob is-a myclass
# ob = MyClass()
#
# # Output: <function MyClass.func at 0x000000000335B0D0>
# # MyClass has-a func
# print(MyClass.func)
#
# # Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
# # ob has a func
# print(ob.func)
#
# # Calling function func()
# # Output: Hello
# # ob has-a func
# ob.func()
#

# ComplexNumber is-a object
class ComplexNumber:
    # ComplexNumber has-a __init__ function
    def __init__(self,r = 0,i = 0):
        # __init__ function has-a variable named r and i
        self.real = r
        self.imag = i
# ComplexNumber has-a getData function
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
# c1 is-a ComplexNumber
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
# c1 has-a getData function
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
# c2 is-a ComplexNumber
c2 = ComplexNumber(5)
# c2 has-a attr
c2.attr = 10

# Output: (5, 0, 10)
# c2 has-a real, img and attr function
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# c1 has attr
c1.attr
