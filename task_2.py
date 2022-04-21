import json
from task_1 import top_movie_list

def group_by_year(movies):
    years=[]
    movie_dict={}
    for i in movies:
        year=i["year"]
        
        if year not in years:
            years.append(year)
    for i in years:
        movie_dict.update({i:[]})
    for i in movies:
        year=i['year']
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)

    with open("movie_year.json","w") as f:
        json.dump(movie_dict,f,indent=6)
    return movie_dict
    
print(group_by_year(top_movie_list))
            
  
