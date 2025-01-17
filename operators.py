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

#BOOLEAN OPERATORS
import random
a=random.randint(1,9)
b=random.randint(1,9)
ans=eval(input("What is "+str(a)+" "+str(b)+" :- "))
print("Your ans is :-",a+b==ans)
