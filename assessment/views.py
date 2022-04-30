from django.shortcuts import render, redirect
import csv

from django.http import HttpResponse
from cricket.models import Players

def saving_data_into_model(request):
    file = open('data/most_runs_average_strikerate.csv')
    csvreader = csv.reader(file)
    print(csvreader)
    header = []
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        Players.objects.get_or_create(name=row[0], total_runs=row[1], out=row[2], balls=row[3], average=row[4], strikerate=row[5])


def dashboard(request):
    file = open('data/most_runs_average_strikerate.csv')
    csvreader = csv.reader(file)

    if len(Players.objects.all())==0:
        for row in csvreader:
                Players.objects.get_or_create(name=row[0], total_runs=row[1], out=row[2], balls=row[3], average=row[4], strikerate=row[5])

    ### for highest strike rate ###
    players = []
    strikeRateData = []
    for i in Players.objects.filter(balls__gte=1000).order_by("-strikerate")[0:11]:
            players.append(i.name)
            strikeRateData.append(float(i.strikerate))

    ### for highest average ###
    players4 = []
    averageData = []
    for i in Players.objects.filter(balls__gte=1000).order_by("-average")[0:11]:
            players4.append(i.name)
            averageData.append(float(i.average))

    ### for most runs ###
    players1 = []
    runs = []
    for i in Players.objects.all().order_by("-total_runs")[0:11]:
        players1.append(i.name)
        runs.append(i.total_runs)

    # for most no of outs ###
    players2 = []
    outs = []
    for i in Players.objects.all().order_by("-out")[0:11]:
        players2.append(i.name)
        outs.append(i.total_runs)

    ### for most balls faced ###
    players3 = []
    balls = []
    for i in Players.objects.all().order_by("-balls")[0:11]:
        players3.append(i.name)
        balls.append(i.balls)
 
    
    context = {
        "highest_strike_rate": {"labels": players, "data": strikeRateData},
        "highest_average": {"labels": players4, "data": averageData},
        "most_runs" : {"labels": players1, "data": runs},
        "most_outs" : {"labels": players2, "data": outs},
        "most_balls" : {"labels": players3, "data": balls}
        
    }
    print("context--", context['highest_average'])
    return render(request, 'dashboard.html', context=context)


    

    
            



    