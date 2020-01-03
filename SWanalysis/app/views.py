from django.shortcuts import render 
from django.http import HttpResponse
from .models import Planetss , SaveDataa

import json
import requests

# code to display the planets
def planets(request):
    response = requests.get("https://swapi.co/api/planets/")  
    planets_data = response.json()
    x=[ ]
    for i in planets_data['results']:
        x.append(i['name'])
    data = { 'planets': x,}     
    myModel = Planetss()
    myModel.name = json.dumps(x)
    myModel.save()
    return render(request,"planets.html",data )

# code to display the titles
def titles(request):
    response1 = requests.get("https://swapi.co/api/films/")
    movies_data = response1.json()
    y=[ ]
    for i in movies_data['results']:
        y.append(i['title'])
    t_data = {'movies':y}    
    return render(request,"movies.html",t_data)

# code to search by planet
def search(request):
    pl_name=request.GET["p_name"]
    response = requests.get("https://swapi.co/api/planets/")  
    planets_data = response.json()
    x= [ ]
    v= [ ]
    y = [ ]
    w=[ ]
    for i in planets_data['results']:
        if pl_name == i['name']:
            x=i['films']
            y=i['residents']
            rp = i['rotation_period']
            op = i['orbital_period']
            dp = i['diameter']
            cp = i['climate']
            gp = i['gravity']

    for i in x:
        r1 = requests.get(i)
        f_data = r1.json()
        v.append(f_data['title'])    
    if y!= [ ]:
        for i in y:
            r2 = requests.get(i)
            r_data = r2.json()
            w.append(r_data['name'])

    myModel = SaveDataa()
    myModel.film = json.dumps(v)
    myModel.resident = json.dumps(w)
    myModel.rperiod = json.dumps(rp)
    myModel.operiod = json.dumps(op)
    myModel.diam = json.dumps(dp)
    myModel.cli = json.dumps(cp)
    myModel.grav = json.dumps(gp)
    myModel.save()        
        

    return render(request,"result.html",{ 'name': pl_name,'f1':v ,'f2':w , "r":rp ,  'o':op , "d":dp , "c":cp ,"g":gp
                                           })    


def intro(request):
    return render(request,"intro.html")    














