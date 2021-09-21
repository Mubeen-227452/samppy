data=[]
n= int(input("enter the thw how may numbers:> "))

for i in range(1,n+1):
    x=int(input("enter value {}:> ".format(i)))
    data.append(x)

def even_odd_count(d):
    odd=0
    even=0
    for i in d:
        if i %2==0:
            even+=1
        else:
            odd+=1
    return even,odd

#even,odd=even_odd_count(data)

#print(f"Even Count:{even}\nOdd Count:{odd}")


data1=[]
n1=int(input("enter how many names you want to enter:> "))

for i in range(1,n+1):
    x=input(f"enter the name{i}: ")
    data1.append(x)


def name_count(d2):
    name=0
    for i in d2:
        if len(i)>5:
            name+=1
    return name

res=name_count(data1)
print(f"No of user has name length greter than 5 letter :{res}")



