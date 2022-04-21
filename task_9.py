import os
import random
import time
import json
from bs4 import BeautifulSoup
from task_1 import top_movie_list
from task_44 import details_movie


list1=[]
for i in top_movie_list[:10]:
    Url=i["url"]
    def movie_details_with_url(URL):
        random_sleep=random.randint(1,3)
        for i in top_movie_list:
            if i["url"]==URL:
                url1=i["url"][33:]
        var=os.path.exists("/home/simran/Desktop/web scraping/"+url1+".json")
        # print(var)
        if var==True:
            with open ("/home/simran/Desktop/web scraping/"+url1+".json","r") as f:
                a=json.load(f)
        else:
            time.sleep(random_sleep)
            data=details_movie(URL)
            list1.append(data)
            # print(data)
            with open ("task_9.json","w") as f:
                json.dump(list1,f,indent=4)
        return list1
    movie_details_with_url(Url)
    
# for i in top_movie_list[:10]:
#     Url=i["url"]
#     def movie_details_with_url(URL):
#         for i in top_movie_list:
#             if i["url"]==URL:
#                 url1=i["url"][33:]
#                 return url1
#     print(movie_details_with_url(Url))
                

