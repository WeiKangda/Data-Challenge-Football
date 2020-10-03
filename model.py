# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:17:38 2020

@author: hanso
"""

import csv
import os
path1 = 'FootballDatasets/CollegeFootball/CumulativeStats'
path2 = 'FootballDatasets/CollegeFootball/RegSeason'
path3 = 'FootballDatasets/NFL/CumulativeStats'
path4 = 'FootballDatasets/NFL/RegSeason'
path5 = 'NFL_teams.csv'
path6 = 'College_teams.csv'

team1 = []
team2 = []
with open(path5) as f:
    read = csv.reader(f)
    for row in f:
        team1.append(row)
    for i in team1:
        team2.append(i.replace("\n", ""))
   
for file in os.listdir(path3):
    path = os.path.join(path3,file)
    with open(path) as f:
        read = csv.reader(f, delimiter=',')
        next(read)
        teams = {}
        wins = {}
        for i in team2:
            teams[i] = []
            wins[i] = 0
        for row in read:
            #print(row)
            if row[2] > row[14]:
                    wins[row[1]] = wins[row[1]] + 1
            for i in range(2, 24):
                if (len(teams[row[1]]) < 23):
                   
                    teams[row[1]].append(float(row[i]))
                else:
                    #print(row[i])
                    if row[i] == '' or '':
                        teams[row[1]][i-2] = teams[row[1]][i-2]
                    else:
                        teams[row[1]][i-2] = teams[row[1]][i-2] + float(row[i])
        #print(teams)
        print(wins)
        for i in team2:
            teams[i].append(wins[i])
    p = os.path.join('FootballDatasets/NFL/TeamDataBySeason', file)
    with open(p, 'w', newline ='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['TeamName', 'ScoreOff', 'FirstDown', 'RushAttOff', 'RushYdsOff', 'PassAttOff', 'PassCompOff', 'PassYdsOff', 'PassIntOff', 'FumblesOff', 'SackYdsOff', 'PenYdsOff', 'PuntAvgOff', 'ScoreDef', 'FirstDownDef', 'RushAttDef', 'RushYdsDef', 'PassAttDef', 'PassCompDef', 'PassYdsDef', 'PassIntDef', 'FumblesDef', 'SackYdsDef', 'PenYdsDef', 'Wins'])
        for i in teams:
            data = teams[i]
            data.insert(0, i)
            filewriter.writerow(teams[i])


team3 = []
team4 = []
with open(path6) as f:
    read = csv.reader(f)
    for row in f:
        team3.append(row)
    for i in team3:
        team4.append(i.replace("\n", ""))
   
for file in os.listdir(path1):
    path = os.path.join(path1,file)
    with open(path) as f:
        read = csv.reader(f, delimiter=',')
        next(read)
        teams = {}
        wins = {}
        for i in team4:
            teams[i] = []
            wins[i] = 0
        for row in read:
            #print(row)
            if row[2] > row[10]:
                    wins[row[1]] = wins[row[1]] + 1
            for i in range(2, 17):
                if (len(teams[row[1]]) < 16):
                    
                    teams[row[1]].append(float(row[i]))
                else:
                    #print(row[i])
                    if row[i] == '':
                        teams[row[1]][i-2] = teams[row[1]][i-2]
                    else:
                        teams[row[1]][i-2] = teams[row[1]][i-2] + float(row[i])
        #print(teams)
        #print(wins)
        for i in team4:
            teams[i].append(wins[i])
            #print(teams)
    p = os.path.join('FootballDatasets/CollegeFootball/TeamDataBySeason', file)
    with open(p, 'w', newline ='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['TeamName', 'ScoreOff', 'RushAttOff', 'RushYdsOff', 'PassAttOff', 'PassCompOff', 'PassYdsOff', 'PassIntOff', 'FumblesOff', 'ScoreDef', 'RushAttDef', 'RushYdsDef', 'PassAttDef', 'PassCompDef', 'PassYdsDef', 'PassIntDef', 'FumblesDef','Wins'])
        for i in teams:
            data = teams[i]
            data.insert(0, i)
            #print(teams[i])
            filewriter.writerow(teams[i])