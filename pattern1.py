import array as arr
for i in range(1,5):
    for j in range(5-i):
        print(i+j,end="")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()



for i in range(4):
    for j in range(4):
        if(i<j):
            print(chr(65+14+j), end=" ")
        else :
            print(chr(65+j), end=" ")
    print()


m=[3,4,5,6]
vals= arr.array('i', [3,5,6])
vals.reverse()
