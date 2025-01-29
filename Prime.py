a=int(input("Enter a number:- "))
cnt = 1
for i in range (2,a):
    if a/i==0:
        cnt = cnt + 1
print(cnt)
if(cnt==0):
    print("Prime")
else:
    print("Not a Prime")
