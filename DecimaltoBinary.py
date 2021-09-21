a = 25
print(25 // 2)
print(25 % 2)


def deciBin(num):
    if num >= 1:
        deciBin(num // 2)
        print(num % 2, end="")


deciBin(a)
print()

#x = int(input("enter value of x> "))
#y = int(input("enter value of y> "))
#z = int(input("enter value of z> "))
x = 10
y = 9
z = 1
if x > y and x > y:
    print(x, 'is bigger')
elif y > x and y > z:
    print(y, 'is bigger')
else:
    print(z, 'is bigger')


i=1
while i<=5:
    print(i)
    i=i+1


