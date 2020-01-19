from bs4 import BeautifulSoup
import requests
import numpy as np
import GetStatsGame
import GetStatsTeam
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from pandas import DataFrame
import GamesCommonFuctions as GC
import unicodedata
import platform

statsPlayers = []
statsHome = []
statsAway = []
statsWin = []
statsLost = []
statsLast3 = []
statsTop = []
statsBot = []
statsEasy = []
statsTough = []

def extractStatistics(html_doc,targetTeam,againstTeams,againstTeams2,season,jorFirst,jorLast,division,sDir,fases,sChrome,bAll,bTeam,sPlayers,bProj,sLeague,sOutput, sMinGames, sLang):

    html_doc_alt1 = html_doc + "&med=0"
    html_doc_alt2 = html_doc + "&med=1"
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    system = platform.system()

    if sLang == 'Castellano':
        aWin = 'Ganado'
        aLost = 'Perdido'
        sExt = 'Extrayendo Partidos:'
    else:
        aWin = 'Win'
        aLost = 'Lost'
        sExt = 'Extracting Games:'


    jornadas = soup.find_all('div', class_="contentTablaDataGrid")
    firstJornada = jornadas[0].text.split('/')[0]

    if system == 'Linux':
        iBenIn = 2
        iEndIn = -2
    elif system == 'Darwin':
        iBenIn = 0
        iEndIn = 0

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
                if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '')[2:-1].split(' '):
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

    jornada = []
    tipusPartit = []
    equipCon = []
    bHome = []
    bAgainst = []
    bAgainst2 = []
    resLoc = []
    resVis = []
    wl = []
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
        print(sExt + ' (' + str(page-pageIn+1) + '/' + str(pageFin-pageIn+1) + ')')
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
                # select = driver.find_element_by_link_text(str(page + 1)).click()
            else:
                #print(sChrome) # /Users/arbues/chromedriver
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
            jorTot += 1
            jornadaInd = jornadas[jornada]
            gamesJorn = jornadaInd.find_all('td')[3:]
            for k in range(0, len(gamesJorn), 3):
                if iEndIn != 0:
                    candName = str(unicodedata.normalize('NFKD', gamesJorn[k].text.replace('\n', ' ')).encode('ascii', 'ignore'))[iBenIn:iEndIn]
                else:
                    candName = str(unicodedata.normalize('NFKD', gamesJorn[k].text.replace('\n', ' ')).encode('ascii', 'ignore'))
                if targetTeam in candName:
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
                        if system == 'Linux' or system == 'Darwin':
                            candLocTeam = locTeam[2:-1]
                        else:
                            candLocTeam = locTeam

                        if targetTeam in candLocTeam:
                            if len(sPlayers) > 0 and sPlayers[0] != '':
                                a1 = GC.filterPlayers(a, sPlayers)
                            else:
                                a1 = a
                            lenReal = len(a1)
                            if len(a1) > 0:
                                dif = resLocIn - resVisIn
                                if a1[0] != []:
                                    statsPlayers.append(a1)
                                    statsHome.append(a1)
                                teamStats = GetStatsTeam.getStats(realLink, True)
                                teamStatsAgainst = GetStatsTeam.getStatsAgainst(realLink, False)
                                bHome.append(True)
                                bHome.append(True)
                                bHome.append(True)
                                statsPlayers.append(teamStats)
                                statsPlayers.append(teamStatsAgainst)
                                statsHome.append(teamStats)
                                statsHome.append(teamStatsAgainst)
                                statsAppend = a1
                        else:
                            if len(sPlayers) > 0 and sPlayers[0] != '':
                                b1 = GC.filterPlayers(b, sPlayers)
                            else:
                                b1 = b
                            lenReal = len(b1)
                            if len(b1) > 0:
                                dif = resVisIn - resLocIn
                                if b1[0] != []:
                                    statsPlayers.append(b1)
                                    statsAway.append(b1)
                                teamStats = GetStatsTeam.getStats(realLink, False)
                                teamStatsAgainst = GetStatsTeam.getStatsAgainst(realLink, True)
                                statsPlayers.append(teamStats)
                                statsPlayers.append(teamStatsAgainst)
                                statsAway.append(teamStats)
                                statsAway.append(teamStatsAgainst)
                                statsAppend = b1
                                bHome.append(False)
                                bHome.append(False)
                                bHome.append(False)
                        if lenReal > 0:
                            iAgainst = 0
                            iAgainst2 = 0
                            sDif.append(dif)
                            sLocal.append(locTeam)
                            sAway.append(visTeam)

                            if ((jorFirst-1)+jorTot) > (jorLast-3):
                                statsLast3.append(statsAppend)
                                statsLast3.append(teamStats)
                                statsLast3.append(teamStatsAgainst)

                            if system == 'Linux' or system == 'Darwin':
                                candLocTeam = locTeam[2:-1]
                            else:
                                candLocTeam = locTeam

                            if targetTeam in candLocTeam:
                                if system == 'Linux' or system == 'Darwin':
                                    candVisTeam = visTeam[2:-1]
                                else:
                                    candVisTeam = visTeam

                                visTeam = candVisTeam
                                for iText in range(0, len(visTeam.split(' '))):
                                    if visTeam.split(' ')[iText] in againstTeams:
                                        iAgainst = 1
                                        statsTop.append(statsAppend)
                                        statsTop.append(teamStats)
                                        statsTop.append(teamStatsAgainst)
                                    if visTeam.split(' ')[iText] in againstTeams2:
                                        iAgainst2 = 1
                                        statsBot.append(statsAppend)
                                        statsBot.append(teamStats)
                                        statsBot.append(teamStatsAgainst)
                            else:
                                if system == 'Linux' or system == 'Darwin':
                                    candLocTeam = locTeam[2:-1]
                                else:
                                    candLocTeam = locTeam
                                locTeam = candLocTeam
                                for iText in range(0, len(locTeam.split(' '))):
                                    if locTeam.split(' ')[iText] in againstTeams:
                                        iAgainst = 1
                                        statsTop.append(statsAppend)
                                        statsTop.append(teamStats)
                                        statsTop.append(teamStatsAgainst)
                                    if locTeam.split(' ')[iText] in againstTeams2:
                                        iAgainst2 = 1
                                        statsBot.append(statsAppend)
                                        statsBot.append(teamStats)
                                        statsBot.append(teamStatsAgainst)

                            if iAgainst == 0:
                                bAgainst.append(False)
                                bAgainst.append(False)
                                bAgainst.append(False)
                            else:
                                bAgainst.append(True)
                                bAgainst.append(True)
                                bAgainst.append(True)

                            if iAgainst2 == 0:
                                bAgainst2.append(False)
                                bAgainst2.append(False)
                                bAgainst2.append(False)
                            else:
                                bAgainst2.append(True)
                                bAgainst2.append(True)
                                bAgainst2.append(True)

                            if dif > 0:
                                sWin.append(aWin)
                                statsWin.append(statsAppend)
                                statsWin.append(teamStats)
                                statsWin.append(teamStatsAgainst)
                                wl.append('W')
                                if dif > 10:
                                    tipusPartit.append("EW")
                                    tipusPartit.append("EW")
                                    tipusPartit.append("EW")
                                    statsEasy.append(statsAppend)
                                    statsEasy.append(teamStats)
                                    statsEasy.append(teamStatsAgainst)
                                else:
                                    tipusPartit.append("TW")
                                    tipusPartit.append("TW")
                                    tipusPartit.append("TW")
                                    statsTough.append(statsAppend)
                                    statsTough.append(teamStats)
                                    statsTough.append(teamStatsAgainst)
                            else:
                                wl.append('L')
                                sWin.append(aLost)
                                statsLost.append(statsAppend)
                                statsLost.append(teamStats)
                                statsLost.append(teamStatsAgainst)

                                if np.abs(dif) > 10:
                                    tipusPartit.append("EL")
                                    tipusPartit.append("EL")
                                    tipusPartit.append("EL")
                                    statsEasy.append(statsAppend)
                                    statsEasy.append(teamStats)
                                    statsEasy.append(teamStatsAgainst)
                                else:
                                    tipusPartit.append("TL")
                                    tipusPartit.append("TL")
                                    tipusPartit.append("TL")
                                    statsTough.append(statsAppend)
                                    statsTough.append(teamStats)
                                    statsTough.append(teamStatsAgainst)
                            break
                    except:
                        pass

    if sLang == "Castellano":
        sAllR = "Jornadas"
    else:
        sAllR = "AllRounds"

    if sPlayers != []:
        sOutput = sOutput + '-' + str(len(sPlayers)) + 'Pl'

    if statsPlayers != []:
        GC.getAvStats(statsPlayers, bHome, tipusPartit, bAgainst, bAgainst2, targetTeam, season, jorFirst, jorLast, sDir,sOutput,bTeam, bProj, statsHome, statsAway, statsWin, statsLost, statsLast3, statsTop, statsBot, statsEasy, statsTough, sMinGames, sLang)
        GC.get5FasesStats(sLang, statsPlayers, season, jorFirst, jorLast, sDir, int(fases), targetTeam, sOutput,bTeam, bProj)
        if bAll:
            GC.get5FasesStats(sLang, statsPlayers, season, jorFirst, jorLast, sDir, int(1), targetTeam, sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif)
    else:
        print('Non-existent FEB Data')
