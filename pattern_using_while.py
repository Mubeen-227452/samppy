i = 1
while i <= 4:
    print("#", end="")
    j = 1
    while j <= 3:
        print("#", end="")
        j = j + 1
    i = i + 1
    print()
"""
####
####
####
####
above prog 
"""

"""print num 1to 100 which are not divisibe by 3 or 5"""

m = 1
while m <= 100:
    if m % 3 == 0 or m%5==0:
        m=m+1
        continue
    else:
        print(m,end=" ")
    m = m + 1

