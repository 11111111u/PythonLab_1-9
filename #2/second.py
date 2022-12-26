class MyClass:
    int_field = 8
    str_field = "a string"

object1 = MyClass()
object2 = MyClass()

print(MyClass.int_field)
print(MyClass.str_field)
print(object2.str_field)
print("///////////////")
MyClass.int_field = 10
print(MyClass.int_field)
print(object1.int_field)
print(object2.int_field)
print("///////////////")
object1.str_field ="another string"
print(MyClass.str_field)
print(object1.str_field)
print(object2.str_field)

