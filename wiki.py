import wikipediaapi
import json
import os
import sys
import urllib.request
import re

wiki = wikipediaapi.Wikipedia("english")

# wikipedia pages and subsections
pages = ["Portrayals of Alice in Wonderland", "Hatter (Alice's Adventures in Wonderland)", 
         "Aurora (Sleeping Beauty)", "Maleficent", "Cinderella (Disney character)",
         "Prince Charming", "Fairy godmother", "Snow White (Disney character)", "Evil Queen (Disney)"]
subsections = ['Animated film', "Films", "Conception and writing", "No", "No", "No", "No", "In Snow White and the Seven Dwarfs", "No"]

data_list = []

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

for i in range(len(pages)):
    data = {}
    page = wiki.page(pages[i])
    title = page.title
    
    data["title"] = title
    
    context = ""
    
    if subsections[i] != "No":
        section = page.section_by_title(subsections[i])
        context = section.text
    else:
        context = page.summary

    encText = urllib.parse.quote(context)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read().decode("utf-8")
        print(response_body)
    else:
        print("Error Code:" + rescode)
    
    data["context"] = context
    data_list.append(data)

save_path = "data/character.json"
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)
    
    
    
    