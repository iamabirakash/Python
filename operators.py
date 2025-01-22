'''Arithmetic Unary Comparison Bitwise Assignment
Logical Membership Identity'''

#ARITHMETIC OPERATORS
'Addition'
a=5
b=3
print("ADDITION")
print("The value of a is :-",a)
print("The value of b is :-",b)

print("Addition of a and b is :-",a+b)

'Substraction'
print("Substraction of a and b is :-",a-b)

'Multiplication'
print("Multiplication of a and b is :-",a*b)

'Divison'
print("Divison of a and b is :-",a/b)

'Power'
print("Power of a and b is :-",a**b)

'Floor Divison'
print("Floor Divison of a and b is :-",a//b)

'Modulus'
print("Modulus of a and b is :-",a%b)

print("-----------------------------------------")

a = [1,2,3]
b = [4,5,6]
print("List Individual Addition :-",a[0]*b[0])
print("List Addition :-",a+b)

a = (1,2,3)
b = (4,5,6)
print("Tuple Individual Addition :-",a[0]+b[0])
print("Tuples Addition :-",a+b)

a = {1:'a',2:'b',3:'c'}
b = {4:'d',5:'e',6:'f'}
print("Dictionaries can't be added")


print("-----------------------------------------")

#BOOLEAN OPERATORS
'''import random
a=random.randint(1,9)
b=random.randint(1,9)
ans=eval(input("What is "+str(a)+" "+str(b)+" :- "))
print("Your ans is :-",a+b==ans)'''
print("-----------------------------------------")

#COMPARSION OPERATORS
print("COMPARSION")
print(10>5)
print(True>False)
print(5.5>5)
print('x'>'@')
print('Z'<'5')
print("Comparison operators compares the ASCII ")
a = [1,200,2]
b = [1,200,3]
print(a<=b)

print("-----------------------------------------")
print("-----------------------------------------")

#BITWISE OPERATORS
print("BITWISE")
'''AND,OR,NOT,LEFT SHIFT,RIGHT SHIFT'''
print(0 & 1)
print(1 | 2)
print(1 ^ 2) #Different True, Same False
print(~ 100) #-(n+1)
print(5 << 2)
print(5 >> 2)

print("-----------------------------------------")
print("-----------------------------------------")

#LOGICAL OPERATORS
print("LOGICAL")

print(0 and 1)
print(0 or 50)
print((2>3) and (3>2))
print((2>3) or (3>2))
print(not((2>3) or (3>2)))

print("-----------------------------------------")
print("-----------------------------------------")

#IDENTITY OPERATORS
print("IDENTITY")
print("It compares the memory allocation of two identity operators")
a = 5
b = 5
print(a is b)
print(a is 5)
print(a is not 5)
print(1 is 1)
print('a' is 'a')
a = [1,2,3]
b = [1,2,3]
print(a is b) #Memory Allocation is different

print("-----------------------------------------")
print("-----------------------------------------")

#MEMBERSHIP OPERATORS
print("MEMBERSHIP")

b = ['a','b','c']
print('b' in b)
print('d' in b)

print("-----------------------------------------")
print("-----------------------------------------")
