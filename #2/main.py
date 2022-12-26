class MyClass : pass

AnotherClass = MyClass

obj = MyClass()

if __name__ == '__main__':
    print(type(obj))
    print(type(MyClass))
    print(type(AnotherClass))
    print(isinstance(obj,AnotherClass))


