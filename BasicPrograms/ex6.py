# message='python is fun'
# print(message.upper())

#
class Parent:
    def function1(self):
        print("This is f1")

class Child(Parent):
    def function2(self,a):
        print("this is f2")
        print(a)
    b=20
y=Child()
y.function1()
y.function2(10)
print(y.b)
