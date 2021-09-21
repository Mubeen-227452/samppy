n = int(input("enter a number: "))


def Palindrome(x):
    q = x
    rem = 0
    res = 0
    while q != 0:
        rem = q % 10
        res = res * 10 + rem
        q = q // 10
    if res == n:
        print("Palindrome")
    else:
        print("Not a Palindrome")


Palindrome(n)
