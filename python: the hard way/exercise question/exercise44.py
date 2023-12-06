# class parent(object):
#
#     def implict(self):
#         print("parent implict()")
#
# class child(parent):
#
#     pass
#
# dad = parent()
# son = child()
#
# dad.implict()
# son.implict()

# class parent(object):
#
#     def override(self):
#         print("parent override()")
#
# class child(parent):
#
#     def override(self):
#         print("child override()")
#
# dad = parent()
# son = child()
#
# dad.override()
# son.override()

# class parent(object):
#
#     def altered(self):
#         print("parent altered")
#
# class child(parent):
#
#     def altered(self):
#         print("child altered")
#         super(child, self).altered()
#         print("after super child altered")
#
# dad = parent()
# son = child()
#
# dad.altered()
# son.altered()

# class parent(object):
#
#     def override(self):
#         print("parent override")
#
#     def implict(self):
#         print("parent implict")
#
#     def altered(self):
#         print("parent altered")
#
# class child(parent):
#
#     def override(self):
#         print("child override")
#
#     def altered(self):
#         print("before super child altered")
#         super(child, self).altered()
#         print("after super child altered")
#
# dad = parent()
# son = child()
#
# dad.override()
# dad.implict()
# dad.altered()
#
#
# son.override()
# son.implict()
# son.altered()

# class other(object):
#
#     def override(self):
#         print("other override()")
#
#     def implict(self):
#         print("other implict()")
#
#     def altered(self):
#         print("other altered()")
#
# class child(object):
#
#     def __init__(self):
#         self.other = other()
#
#     def implict(self):
#         self.other.implict()
#
#     def override(self):
#         print("child override()")
#
#     def altered(self):
#         print("before self child altered")
#         self.other.altered()
#         print("after self child altered")
#
# son = child()
#
# son.implict()
# son.override()
# son.altered()

class intro(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def post(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")

class child(object):
    def __init__(self):
        self.bb = intro()

    def name(self):
        self.bb.post()


dad = intro('rohit', 18)
son = child('rohit', 18)
son.name()
