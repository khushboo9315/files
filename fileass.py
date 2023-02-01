
'''1. Write a Python program to read an entire text file.'''

# f=open("fileass.txt","r")
# print(f.read())

'''2. Write a Python program to read the first n lines of a file.'''

# f=open("fileass.txt","r")
# for i in range(int(input())):
#     print(f.readline())

'''3. Write a Python program to append text to a file and display the text.'''

# f=open("fileass.txt","a")
# f.write("  this is a appended text")
# f1=open("fileass.txt","r")
# print(f1.read())

'''4. Write a Python program to read the last n lines of a file.''' 
# n=int(input())
# f=open("fileass.txt","r")
# a=(f.readlines())
# print(a[-n:])

'''5. Write a Python program to read a file line by line and store it into a list.'''

# l=[]
# f=open("fileass.txt","r")
# for i in f:
#     l.append(i)
# print(l)

'''6. Write a Python program to read a file line by line and store it into a string variable.'''

# l=" "
# f=open("fileass.txt","r")
# for i in f:
#     l+=i
# print(l)

'''7. Write a program to store a matrix into a nested list. (Matrix in a text file) '''

# l=[]
# # l1=[]
# f=open("abc.txt","r")
# for i in f:
#     l1=[]
#     l1.append(str(i).replace("\n",""))
#     l.append(l1)
# print(l)


'''8. Write a python program to find the longest words in a text file.'''

# f=open("fileass.txt","r")
# l=f.read().split()
# long=len(max(l,key=len))
# result=[word for word in l if len(word)==long]
# print(result)
# f.close()

'''9. Write a Python program to count the number of lines in a text file.'''

# f=open("fileass.txt","r")
# c=0
# l=f.readlines()
# for i in l:
#     c+=1
# print(c)


'''10. Write a Python program to count the frequency of words in a file.'''

# f=open("fileass.txt","r")
# d={}
# l=f.read().split()
# for i in l:
#     d.setdefault(i,0)
#     d[i]+=1    
# print(d)


'''11. Write a python program to store the names and birthdays of your friends in a text file .'''

# f=open("fleass1.txt","a+")
# # a,b=map(input().split())
# n=int(input())
# for i in range(n):
#     x=f.write(input()+":")
#     x=f.write(input()+"\n")
# print(x)


'''12. Write a Python program to write a list to a file.'''

# f=open("fileass2.txt","w")
# n=[1,2,"khushi","my name",21,"my age"]
# for i in n:
#     x=f.write(str(i)+"\n")
# print(x)

 
'''13. Write a Python program to copy the contents of a file to another file .'''

# f=open("fileass.txt","r")
# f1=open("fileass2.txt","a")
# for i in f:
#     # a=f.readlines()
#     # b=a.copy()
#     x=f1.write(str(i))
# print(x)

'''14. Write a Python program to combine each line from the first file with the corresponding 
line in the second file.'''

# f1=open("fileass.txt","r")
# f2=open("fileass2.txt","r")
# for a,b in zip(f1,f2):
#     print(a+b)


'''15. Write a Python program to read a random line from a file.'''
# import random
# f1=open("fileass.txt","r")
# x=f1.read().splitlines()
# a=random.choice(x)
# print(a)


'''16. Write a Python program to assess if a file is closed or not.'''

# f=open("fileass.txt","r")
# print(f.closed)
# f.close()
# print(f.closed)


'''17. Write a Python program to remove newline characters from a file.'''

# f=open(("fileass.txt"))       ########  not done
# for i in f.readline():
#     print(i)




'''18. Write a Python program that takes a text file as input and returns the number of words of 
a given text file.
 Note: Some words can be separated by a comma with no space.
'''
# f=open("fileass3.txt","w")
# a=input()
# f.write(a)
# f=open("fileass3.txt","r")
# i=f.read()
# j=i.replace(","," ")
# x=j.split()
# print(len(x))


'''19. Write a Python program to extract characters from various text files and put them into a list.'''



'''20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'''

# import os
# # for i in range(97,97+26):
# #     f=open(chr(i)+".txt","w")
# for i in range(97,97+26):
#     os.remove(chr(i)+".txt")



'''21. Write a Python program to create a file where all letters of the English alphabet are
 listed by specified number of letters on each line.
E.g	
  1 A
	2 B
	3 C
	4 D    and so on…'''

# f=open("alpha.txt","w")
# for i in range(26):
#     f.write(str(i+1)+" "+chr(65+i)+"\n")

 
'''22. Using names.txt , a 46K text file containing over five thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for 
each name, multiply it by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 
938 × 53 = 49714.
What is the total of all the name scores in the file?'''

# al=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# f=open("toxic.txt","r")
# for i in f. readlines():
#     c=sorted(map(str,i.split(",")))
# # print(len(c))
# # c.sort()
# l=[]
# for j in c:
#     l.append(j[1:-1])
# # print(l)
# sum1=0
# for k in l:
#     sum=0
#     for m in k:
#         sum+=al.index(m)+1
#     print(k," ",sum*(l.index(k))+1)
#     s=sum*((l.index(k))+1)
#     sum1+=s
# print(sum1)


'''23. The nth term of the sequence of triangle numbers is given by tn = ½n(n+1); so the first ten 
triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding 
these values, we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number, then we shall call the word a triangle word.
Using words.txt, a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?'''

 


'''24. By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt a 15K 
text file containing a triangle with one-hundred rows.



'''

# l=[]
# f=open("triangle.txt","r")
# for i in f.readlines():
# 	l1=[]
# 	l1.append(i.split())
# 	# l1.remove(\n)
# 	l.append(l1)
# sum=(l[0][0])
# print(l)
# print(l[1][0])
# print(len(l[0]))
# for j in range(1,len(l)):
# 	sum+=(int(l[j][j-1]))
# print(sum)



# f=open("triangle.txt","r")
# l=[]
# for i in f.readlines():
# 	c=list(map(int,i.split()))
# 	l.append(c)
# sum=l[0][0]
# for j in range(1,len(l)):
# 	sum+=(int(l[j][j-1]))
# print(sum)


