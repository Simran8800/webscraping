from bs4 import BeautifulSoup
import requests
import json
from task_1 import top_movie_list


def details_movie(movie_url):
    movie_details = []
    movie_dic = {}
    page = requests.get(movie_url)
    
    soup = BeautifulSoup(page.text,'html.parser')
    
    title=soup.find("div",class_="col mob col-center-right col-full-xs mop-main-column")
    
    title1=title.find("div",class_="thumbnail-scoreboard-wrap")
    
    name=title1.find("h1",class_="scoreboard__title").get_text()
    
    movie_dic['name'] = name
    
    title = soup.find_all('div',class_='meta-label subtle')
    value = soup.find_all('div',class_='meta-value')

   
    
    for i in range(len(title)):
        movie_dic[str(title[i].get_text().strip())[:-1]] = value[i].get_text().replace(" ","").strip().replace("\n","")
    movie_details.append(movie_dic)

    with open('Task_4.json','w') as file:
        json.dump(movie_details,file,indent=4)


url=top_movie_list[0]["url"]
details_movie(url)

    
    
    
    
    
    
    
    
    
    
    
    
    
    