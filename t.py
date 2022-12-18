li=list(map(int,input().split()))
for i in li:
    if(i<0):
        li.remove(i)
li.sort()
    # print(li)
ma=max(li)
mi=min(li)
new=[]
for j in range(mi,ma+1):
    new.append(j)
    #print(new)
if(li==new):
    print(max(li)+1)
else:
    for k in li:
        if(k in new):
            new.remove(k)
    print(new[0])
