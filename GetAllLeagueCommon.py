from bs4 import BeautifulSoup
import requests
import numpy as np
import GetStatsGame
import GetStatsTeam
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from pandas import DataFrame
import GamesCommonFunctionsAllLeague as GLC
import GamesCommonFuctions as GC
import unicodedata
import platform

statsPlayers = []
teamNames = []
sLocal = []
sAway = []
sWin = []
sDif = []

def extractStatisticsAllLeague(html_doc,targetTeam,season,jorFirst,jorLast,division,sDir,sChrome,bTeam,sPlayers,bProj,sLeague,sOutput,sMinGames, sLang):

    html_doc_alt1 = html_doc + "&med=0"
    html_doc_alt2 = html_doc + "&med=1"
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    system = platform.system()

    if sLang == "Castellano":
        sAllR = "Jornadas"
        sJor = 'Jornada: '
        sExtr = 'Extrayendo Partidos:'
    else:
        sAllR = "AllRounds"
        sJor = 'Round: '
        sExtr = 'Extracting Games:'

    jornadas = soup.find_all('div', class_="contentTablaDataGrid")
    firstJornada = jornadas[0].text.split('/')[0]

    if sLeague != 'ORO' and sLeague != 'DIA':
        driver = webdriver.Chrome(sChrome)
        driver.get(html_doc)
        select = Select(driver.find_element_by_id('gruposDropDownList'))
        if system == 'Linux' or system == 'Darwin':
            for listPhase in range(0, len(select.options)):
                if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '')[2:-1].split(' '):
                    iSelect = listPhase
        else:
            for listPhase in range(0, len(select.options)):
                if str(division.encode('ascii', 'ignore')).upper() in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '').split(' '):
                    iSelect = listPhase
        time.sleep(5)
        driver.close()

        if jornadas[0].text.split('/')[0] == firstJornada and iSelect != 0:
            driver = webdriver.Chrome(sChrome)
            driver.get(html_doc_alt1)
            select = Select(driver.find_element_by_id('gruposDropDownList'))
            select.select_by_visible_text(select.options[iSelect].text)
            time.sleep(5)
            to_soup = driver.page_source
            driver.close()
            soup = BeautifulSoup(to_soup, 'lxml')
            jornadas = soup.find_all('div', class_="contentTablaDataGrid")
            if jornadas[0].text.split('/')[0] == firstJornada and iSelect != 0:
                driver = webdriver.Chrome(sChrome)
                driver.get(html_doc_alt2)
                select = Select(driver.find_element_by_id('gruposDropDownList'))
                select.select_by_visible_text(select.options[iSelect].text)
                time.sleep(5)
                to_soup = driver.page_source
                driver.close()
                soup = BeautifulSoup(to_soup, 'lxml')
                jornadas = soup.find_all('div', class_="contentTablaDataGrid")

    resLoc = []
    resVis = []
    sLocal = []
    sAway = []
    sWin = []
    sDif = []

    jorTot = 0

    pageIn = int(float(jorFirst-1)/float(8))
    pageFin = int(float(jorLast-1)/float(8))
    jorFirstPage = int(float(jorFirst) - float(pageIn)*float(8))-1
    jorLastPage = int(float(jorLast) - float(pageFin)*float(8))

    sPlayers = sPlayers.split(',')
    sPlayers = [x.upper() for x in sPlayers]

    for page in range(pageIn,pageFin+1):
        print(sExtr + ' (' + str(page-pageIn+1) + '/' + str(pageFin-pageIn+1) + ')')
        if page != 0:
            if sLeague != 'ORO' and sLeague != 'DIA':
                driver = webdriver.Chrome(sChrome)
                driver.get(html_doc)
                driver.delete_all_cookies()
                select = Select(driver.find_element_by_id('gruposDropDownList'))
                select.select_by_visible_text(select.options[iSelect].text)
                time.sleep(5)
                try:
                    select = driver.find_element_by_link_text(str(page + 1)).click()
                except:
                    pass
            else:
                driver = webdriver.Chrome(sChrome)
                # driver = webdriver.PhantomJS()
                driver.get(html_doc)
                driver.delete_all_cookies()
                select = driver.find_element_by_link_text(str(page + 1)).click()

            time.sleep(5)
            to_soup = driver.page_source
            driver.close()
            soup = BeautifulSoup(to_soup, 'lxml')
            jornadasNew = soup.find_all('div', class_="contentTablaDataGrid")
            if firstJornada != jornadasNew[0].text.split('/')[0]:
                jornadas = jornadasNew
            else:
                driver = webdriver.Chrome(sChrome)
                if sLeague != 'ORO' and sLeague != 'DIA':
                    driver.get(html_doc_alt1)
                    driver.delete_all_cookies()
                    select = Select(driver.find_element_by_id('gruposDropDownList'))
                    select.select_by_visible_text(select.options[iSelect].text)
                    time.sleep(5)
                    select = driver.find_element_by_link_text(str(page + 1)).click()
                    time.sleep(5)
                    to_soup = driver.page_source
                    driver.close()
                else:
                    # driver = webdriver.PhantomJS()
                    driver.get(html_doc_alt1)
                    driver.delete_all_cookies()
                    select = driver.find_element_by_link_text(str(page + 1)).click()
                    time.sleep(5)
                    to_soup = driver.page_source
                    driver.close()

                soup = BeautifulSoup(to_soup, 'lxml')
                jornadasNew = soup.find_all('div', class_="contentTablaDataGrid")
                if firstJornada != jornadasNew[0].text.split('/')[0]:
                    jornadas = jornadasNew
                else:
                    driver = webdriver.Chrome(sChrome)
                    if sLeague != 'ORO' and sLeague != 'DIA':
                        driver.get(html_doc_alt2)
                        driver.delete_all_cookies()
                        select = Select(driver.find_element_by_id('gruposDropDownList'))
                        select.select_by_visible_text(select.options[iSelect].text)
                        time.sleep(5)
                        select = driver.find_element_by_link_text(str(page + 1)).click()
                        time.sleep(5)
                        to_soup = driver.page_source
                        driver.close()
                    else:
                        driver.get(html_doc_alt2)
                        driver.delete_all_cookies()
                        select = driver.find_element_by_link_text(str(page + 1)).click()
                        time.sleep(5)
                        to_soup = driver.page_source
                        driver.close()
                    soup = BeautifulSoup(to_soup, 'lxml')
                    jornadasNew = soup.find_all('div', class_="contentTablaDataGrid")
                    if firstJornada != jornadasNew[0].text.split('/')[0]:
                        jornadas = jornadasNew
        if page == pageFin and pageFin != 0:
            jorProcessFirst = 0
            jorProcessLast = jorLastPage
        elif pageFin == 0:
            jorProcessFirst = jorFirst-1
            jorProcessLast = jorLast
        elif page == pageIn:
            jorProcessFirst = jorFirstPage
            jorProcessLast = 8
        else:
            jorProcessFirst = 0
            jorProcessLast = 8

        for jornada in range(jorProcessFirst, jorProcessLast):
            print(sJor + str(jorProcessFirst + (jornada-jorProcessFirst) + 1))
            jorTot += 1
            jornadaInd = jornadas[jornada]
            gamesJorn = jornadaInd.find_all('td')[3:]
            for k in range(0, len(gamesJorn), 3):
                gameCode = gamesJorn[k + 1].find_all('a')[0]['href']
                realLink = "http://competiciones.feb.es/Estadisticas/" + gameCode
                a, b = GetStatsGame.getStats(realLink)

                locTeam = str(unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[1]).encode('ascii', 'ignore'))
                visTeam = str(unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[2]).encode('ascii', 'ignore'))

                resLocIn = int(gamesJorn[k + 1].text.split('\n')[1])
                resVisIn = int(gamesJorn[k + 1].text.split('\n')[2])

                resLoc.append(resLocIn)
                resVis.append(resVisIn)
                try:
                    if len(sPlayers) > 0 and sPlayers[0] != '':
                        a1 = GC.filterPlayers(a, sPlayers)
                    else:
                        a1 = a
                    if a1 != []:
                        statsPlayers.append(a1)
                        teamStats = GetStatsTeam.getStats(realLink, True)
                        teamStatsAgainst = GetStatsTeam.getStatsAgainst(realLink, False)
                        statsPlayers.append(teamStats)
                        statsPlayers.append(teamStatsAgainst)
                        teamNames.append('Players')
                        teamNames.append(locTeam)
                        teamNames.append(visTeam)
                        sLocal.append(locTeam)
                        sAway.append(visTeam)
                        difa = float(resLoc[-1])-float(resVis[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)

                    if len(sPlayers) > 0 and sPlayers[0] != '':
                        b1 = GC.filterPlayers(b, sPlayers)
                    else:
                        b1 = b
                    if b1 != []:
                        statsPlayers.append(b1)
                        teamStats = GetStatsTeam.getStats(realLink, False)
                        teamStatsAgainst = GetStatsTeam.getStatsAgainst(realLink, True)
                        statsPlayers.append(teamStats)
                        statsPlayers.append(teamStatsAgainst)
                        teamNames.append('Players')
                        teamNames.append(visTeam)
                        teamNames.append(locTeam)
                        sLocal.append(locTeam)
                        sAway.append(visTeam)
                        difa = float(resVis[-1])-float(resLoc[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)
                except:
                    pass

    if sPlayers != []:
        sOutput = sOutput + '-' + str(len(sPlayers)) + 'Pl'
    GLC.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast, sDir,sOutput,bTeam, bProj, teamNames,sMinGames, sLang)
    GLC.get5FasesStats(statsPlayers, season, jorFirst, jorLast, sDir, int(1), sLeague.split(',')[0], sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif, teamNames, sLang, len(sPlayers))

