import json

def movie_language():
    file1=open("Task5.json","r")
    h=json.load(file1)
    list=[]
    for i in h:
        if i["Director"] not in list:
            list.append(i["Director"])
    dict8={}
    list9=[]
    for k in list:
        # print(k)
        i=0
        count=0
        while i<len(h):
           
            if k==h[i]["Director"]:
               
                count=count+1
            i=i+1
        dict8.update({k:count})
    list.append(dict8)
    with open("task7.json","w")as file:
        json.dump(dict8,file,indent=4)
movie_language()


