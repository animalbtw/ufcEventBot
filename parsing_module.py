import requests
import re
from bs4 import BeautifulSoup
from data import URL, WIKI_CARDS


def getHtml(url):
    r = requests.get(url)
    try:
        return r.text
    except Exception:
        return Exception


def getCard(html, position):
    cardResults = []
    soup = BeautifulSoup(html, 'lxml')
    allTables = soup.findAll(class_='m-mmaf-pte-event-list__split-item')
    for fightTables in allTables:
        res = []
        allResults = fightTables.findAll('span', class_='m-mmaf-pte__decision')
        for results in allResults:
            res.append(results.text)
        cardResults.append(res)
    joinedResults = '\n\n'.join(cardResults[position])
    return(joinedResults)


def getTournament(html, tournamentName):
    cardResults = []
    soup = BeautifulSoup(html, 'lxml')
    allHeaders = soup.findAll('table', id_='Past_events')
    cardResults.append(allHeaders)
    return f'{tournamentName}.'


def getFighter(html, fighter):
    return f'{fighter}.'
    
    
def figterRecord(fighter):
    return getFighter(getHtml(URL), fighter)


def getTournamentResult(number):
    return getTournament(getHtml(WIKI_CARDS), number)


def lastCardResult(): 
    return getCard(getHtml(URL), 0)