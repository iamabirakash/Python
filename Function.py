def check(number):
    if(number>0):
        return f'{number} is Greater than 0'
    elif number<0:
        return f'{number} is Less than 0'
    else:
        return f"{number} is 0"

n = int(input("Enter a number: "))
print(check(n))
