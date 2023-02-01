a=open("new_sort.txt","r")
b=open("sort.txt","w")
for i in a.readlines():
    c=sorted(list(map(int,i.split())))
    for k in c:
        b.write(str(k)+" ")
    b.write("\n")
print(b)
