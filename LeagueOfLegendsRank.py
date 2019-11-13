'''
Created of November 12, 2019
@author: Fabricio Flores
Description: Creates a program that takes in League of Legends information and returns rank
'''

import requests

def getSummonerInformation(region, summonerName, APIKey):
    jsonFileURL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(jsonFileURL)
    return response.json()

def getSummonerRankedData(region, summonerID, APIKey):
    jsonFileURL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerID + "?api_key=" + APIKey
    response = requests.get(jsonFileURL)
    return response.json()

def main():
    summonerName = input("What is your summoner name? ")
    print("BR1 EUN1 EUW1 JP1 KR LA1 LA2 NA1 OC1 TR1 RU")
    region = input("From which of the regions above is your account in? ")
    APIKey = input("Please enter your Riot Games API Key: ")

    retrievedJson = getSummonerInformation(region, summonerName, APIKey)
    summonerID = str(retrievedJson['id'])
    retrievedJsonRank =  getSummonerRankedData(region, summonerID, APIKey)

    x = len(retrievedJsonRank)
    for n in range(0,x):
        queueType = retrievedJsonRank[n]['queueType']
        if queueType == "RANKED_SOLO_5x5":
            index = n
            break
        
    tier = retrievedJsonRank[index]['tier']
    rank = retrievedJsonRank[index]['rank']  
    print("Your rank, " + summonerName + ", is " + tier + " " + rank + ".")

if __name__ == '__main__':
    print("\n")
    main()
