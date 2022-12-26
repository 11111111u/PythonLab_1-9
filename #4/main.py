s1 = 'row 1'
s2 = 'row 2'
s3 = str(8);
print(s3)
s4 = """Lesson2. variables and data types
    Some data types explained in this lesson:
    -int, -bool,-float,-complex,-str"""
print(s4)
s5 = "started " \
     "continued"
print(s5)
print("//////////////B////////////")
string = "a string"
print(string[0])
print(string[2])
print(string[-1])
print("//////////////C////////////")
print(string[2:5])
print(string[:5])
print(string[2:])
print(string[::2])
print(string[2]+string[-3:])
print("/////////////D/////////////")
row = input("Input line: ")
if 'q' in row:
     print("there is \"q\" in this line ")
else:
     print("there is no \"q\" in this line ")
print("/////////////E/////////////")
inp = input("Input line: ")
print("The length of this line is : ", len(inp))