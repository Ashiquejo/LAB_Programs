a=int(input("Enter the no of elements: "))
d=[]
print("Enter the num: ")
for i in range(a):
    num=int(input())
    d.append(num)
newlist=[]
for i in range(len(d)):
    if d[i] not in newlist:
        newlist.append(d[i])
print(newlist)
