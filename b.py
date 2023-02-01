# f=open("a.txt")
# q=f.read()
# print(q)
# a=f.read()
# print(a)
# b=f.close()
# print(b)
# c=f.readlines()
# print(c)
# a=f.readlines()

# f=open("a.txt","w")
# f.write("hello there.\n 1 2 3")  
# f.close()



# f=open("file1.txt","r")
# f1=open("file2.txt","r")
# f3=open("result.txt","w")
# print(f)
# print(f1)
# a,b=[],[]
# for val in f.readlines():
#     a.append(int(val))
# for val in f1.readlines():
#     b.append(int(val))
# for i in range(len(a)):
#     f3.write(str(a[i]+b[i])+"\n")
# c=open("result.txt","r")
# print(c)

# f=open("abc.txt","a")
# f.write("kggdtvmn")


# f=open("abc.txt","w")
# f.write("khushboo sharma")
# f.close()
# f=open("abc.txt","r")
# print(f.read())
# f=open("abc.txt","w")
# print(f.read())   #this will give a new file .....
# import os
# os.remove("abc.txt")
# import os 
# if os.path.exists("my.txt"):
#     os.remove("my.txt")
# else:
    # print("file dont exists")