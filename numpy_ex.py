from numpy import *

ar1=array([1,2,3,4,5])
ar2=array([6,7,8,9,10])
print(ar1)
print(ar2)
print(len(ar1))
for i in range(len(ar1)):
    print(ar1[i]+ar2[i],end=" ")
print()
max=ar2[0]

for i in range(len(ar2)):
    if ar2[i]>max:
        max=ar2[i]

print(max)



