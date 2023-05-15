import numpy as np
import os
import requests
import json

#rootdir = "D:\Oculus\Software\hyperbolic-magnetism-beat-saber\Beat Saber_Data\CustomLevels"
rootdir = input("Enter location of 'CustomLevels' folder: ")

def fileLines(file):
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    return(line_count)

def songPuller(file):
    with open(file, 'rt') as fl_lines:
        lines = fl_lines.readlines()
    count = fileLines(lines)
    
    with open(file, 'rt') as fl:
        text = fl.read()
    
    if count <= 1:
        modStartSn = 11
        modEndSn = 1
        modStartAn = 18
        modEndAn = 1
        modStartMn = 19
        modEndMn = 1
    else:
        modStartSn = 12
        modEndSn = 1
        modStartAn = 19
        modEndAn = 1
        modStartMn = 20
        modEndMn = 1
        
    indxStartSn = text.index('songName')
    indxEndSn = text.find(',', indxStartSn, len(text) ) 
    songName = text[indxStartSn+modStartSn:indxEndSn-modEndSn]

    indxStartAn = text.index('_songAuthorName')
    indxEndAn = text.find(',', indxStartAn, len(text) ) 
    artistName = text[indxStartAn+modStartAn:indxEndAn-modEndAn]
    
    indxStartMn = text.index('_levelAuthorName')
    indxEndMn = text.find(',', indxStartMn, len(text) ) 
    modderName = text[indxStartMn+modStartMn:indxEndMn-modEndMn]
    
    return(songName,artistName,modderName)

songList = {0: {'songName': 'test', 'artistName': 'test', 'modderName': 'test'}
           }

i=0
for subdir, dirs, files in os.walk(rootdir):
    if "info.dat" in files:
        filePath = subdir + "\info.dat"
        sN,aN,mN = songPuller(filePath)
        songList[i] = {'songName': sN, 'artistName': aN, 'modderName': mN}
        i += 1
        continue
    elif "Info.dat" in files:
        filePath = subdir + "\Info.dat"
        sN,aN,mN = songPuller(filePath)
        songList[i] = {'songName': sN, 'artistName': aN, 'modderName': mN}
        i +=1
        continue
    else:
        continue

for songNum, songInfo in songList.items():
    print(songInfo['songName'],",",songInfo['artistName'],",",songInfo['modderName'])


url = "https://api.beatsaver.com/search/text/0?q=24K%20Magic%2C%20Bruno%20Mars%2C%20BennyDaBeast&sortOrder=Relevance"

response = requests.get(url)

print(response.status_code)

response_json = response.json()
response_dict = json.loads(response_json)
print(response_dict)
