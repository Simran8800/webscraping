# print(2%6)

# print(-18 // 4)

# a=["python","miraki"]
# print("-".join(a))

# l=[None]*10
# print(len(l))

# a = 4
# b = 11
# print(a | b)
# print(a >> 2)

# var = "James" * 2  * 3
# print(var)


# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# str = "pynative"
# print (str[1:3])

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
# print(listOne == listTwo)
# print(listOne is listTwo)

# salary = 8000
# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
# printSalary()
# print("Salary:", salary)


# p, q, r = 10, 20 ,30
# print(p, q, r)


# var= "James Bond"
# print(var[2::-1])


# for x in range(0.5, 5.5, 0.5):
#     print(x)

# a=[1,0,0,1,1,0,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(1)
#     elif a[i]==1:
#         b.append(0)
#     i=i+1
# print(b)

# print(2%6)

# def add(a,b):
#     c=a+b
#     return c
# x=int(input("enter the no"))
# y=int(input("enter the point"))
# z=add(x,y)
# print(z)

# l=[1,5,12,11,16]
# l_2=[3,7,56,21,6]
# a=l+l_2
# # print(a)
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]>a[j]:
#             a[i],a[j]==a[j],a[i]
#         j+=1
#     i+=1
# print(a)
        


# a=[10,67,34,65]
# b=[9,6,54,87,79]
# a+=b
# for i in range (0,len(a)):
#     for j in range (i+1,len(a)):
#         if (a[i]>a[j]):
#             a[i],a[j]=a[j],a[i]
# print(a)


# import json

# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"]) 


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y = json.dumps(x)
# print(y) 



# a=[[2,4,5],[5,4,3],[4,5,4],4]
# i=0
# sum=0
# while i<len(a):
#     while i<len(a):
#         if type(a[i])==list:
#             j=0
#             while j<len(a[i]):
#                 sum=sum+a[i][j]
#                 j=j+1
#         else:
#             sum=sum+a[i]
#         i=i+1
# print(sum)
    


# a="simran mishra"
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print('',end='')
#         j+=1
#     i+=1
#     print(a[-i])
    

# def k(var):
#     words=var.split()
#     if  len(words)==0:
#         return 0
#     return len(words[-1])
# print(k('hello world '))


# def lengthOfLastWord(a):
#     l = 0
#     x = a.strip()
 
#     for i in range(len(x)):
#         if x[i] == " ":
#             l = 0
#         else:
#             l += 1
#     return l
# if __name__ == "__main__":
#     inp = "Geeks For Geeks "
#     print(lengthOfLastWord(inp))
 

# def length_of_last_word(s):
#         words = s.split()
#         if len(words) == 0:
#             return 0
#         return len(words[-1])
# print(length_of_last_word("Python Exercises"))



            
            