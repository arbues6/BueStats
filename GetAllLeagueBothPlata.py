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


teamNames = []
sLocal = []
sAway = []
sWin = []
sDif = []

def extractStatisticsPlata(html_doc,targetTeam,againstTeams,againstTeams2,season,jorFirst,jorLast,division1,division2,sDir,fases,sChrome,bAll,bTeam,sPlayers,bProj,sLeague,sOutput, sMinGames, sLang):
    if sLang == "Castellano":
        sAllR = "Jornadas"
    else:
        sAllR = "AllRounds"

    bHome1, tipusPartit1, bAgainst1, bAgainst21, statsPlayers1, statsHome1, statsAway1, statsEasy1, statsTough1, statsTop1, statsBot1, statsWin1, statsLost1, statsLast31,  sLocal1, sAway1, sWin1, sDif1 = extractStatistics(html_doc, targetTeam, againstTeams, againstTeams2, season, jorFirst, jorLast, division1, sDir, fases, sChrome, bAll, bTeam, sPlayers, bProj, sLeague, sOutput, sMinGames, sLang, True)
    bHome2, tipusPartit2, bAgainst2, bAgainst22, statsPlayers2, statsHome2, statsAway2, statsEasy2, statsTough2, statsTop2, statsBot2, statsWin2, statsLost2, statsLast32,  sLocal2, sAway2, sWin2, sDif2  = extractStatistics(html_doc, targetTeam, againstTeams, againstTeams2, season, jorFirst, jorLast, division2, sDir, fases, sChrome, bAll, bTeam, sPlayers, bProj, sLeague, sOutput, sMinGames, sLang, True)

    bHome = []
    tipusPartit = []
    bAgainst = []
    bAgainst2 = []
    statsPlayers = []
    statsHome = []
    statsAway = []
    statsEasy = []
    statsTough = []
    statsTop = []
    statsBot = []
    statsWin = []
    statsLost = []
    sLocal = []
    sAway = []
    sWin = []
    sDif = []

    if bHome1 != []:
        bHome.extend(bHome1)
        tipusPartit.extend(tipusPartit1)
        bAgainst.extend(bAgainst1)
        bAgainst2.extend(bAgainst21)
        statsPlayers.extend(statsPlayers1)
        statsHome.extend(statsHome1)
        statsAway.extend(statsAway1)
        statsEasy.extend(statsEasy1)
        statsTough.extend(statsTough1)
        statsTop.extend(statsTop1)
        statsBot.extend(statsBot1)
        statsWin.extend(statsWin1)
        statsLost.extend(statsLost1)
        sLocal.extend(sLocal1)
        sAway.extend(sAway1)
        sWin.extend(sWin1)
        sDif.extend(sDif1)

    if bHome2 != []:
        bHome.extend(bHome2)
        tipusPartit.extend(tipusPartit2)
        bAgainst.extend(bAgainst2)
        bAgainst2.extend(bAgainst22)
        statsPlayers.extend(statsPlayers2)
        statsHome.extend(statsHome2)
        statsAway.extend(statsAway2)
        statsEasy.extend(statsEasy2)
        statsTough.extend(statsTough2)
        statsTop.extend(statsTop2)
        statsBot.extend(statsBot2)
        statsWin.extend(statsWin2)
        statsLost.extend(statsLost2)
        sLocal.extend(sLocal2)
        sAway.extend(sAway2)
        sWin.extend(sWin2)
        sDif.extend(sDif2)

    if statsLast32 == []:
        statsLast3 = statsLast31
    else:
        statsLast3 = statsLast32

    if sPlayers != []:
        sOutput = sOutput + '-' + str(len(sPlayers)) + 'Pl'

    GC.getAvStats(statsPlayers, bHome, tipusPartit, bAgainst, bAgainst2, targetTeam, season, jorFirst, jorLast*2, sDir,sOutput,bTeam, bProj, statsHome, statsAway, statsWin, statsLost, statsLast3, statsTop, statsBot, statsEasy, statsTough, sMinGames, sLang)
    GC.get5FasesStats(sLang, statsPlayers, season, jorFirst, jorLast*2, sDir, int(fases), targetTeam, sOutput,bTeam, bProj)
    if bAll:
        GC.get5FasesStats(sLang, statsPlayers, season, jorFirst, jorLast*2, sDir, int(1), targetTeam, sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif)

def extractStatisticsPlataAll(html_doc,targetTeam,season,jorFirst,jorLast,division1,division2,sDir,sChrome,bTeam,sPlayers,bProj,sLeague,sOutput,sMinGames, sLang):
    if sLang == "Castellano":
        sAllR = ""
        sFase = 'Fase '
    else:
        sAllR = ""
        sFase = 'Round '

    statsPlayers1 = []
    statsPlayers2 = []

    print(sFase + ' 1')
    statsPlayers1, sLocal1, sAway1, sWin1, sDif1, teamNames1 = extractStatisticsAllLeague(html_doc, targetTeam, season, jorFirst, jorLast,  division1, sDir, sChrome, bTeam, sPlayers, bProj, sLeague, '', sMinGames, sLang, statsPlayers1)
    print(sFase + ' 2')
    statsPlayers2, sLocal2, sAway2, sWin2, sDif2, teamNames2 = extractStatisticsAllLeague(html_doc, targetTeam, season, jorFirst, jorLast,  division2, sDir, sChrome, bTeam, sPlayers, bProj, sLeague, '', sMinGames, sLang, statsPlayers2)

    statsPlayers = []
    statsPlayers.extend(statsPlayers1)
    statsPlayers.extend(statsPlayers2)
    sLocal = []
    sLocal.extend(sLocal1)
    sLocal.extend(sLocal2)
    sAway = []
    sAway.extend(sAway1)
    sAway.extend(sAway2)
    sWin = []
    sWin.extend(sWin1)
    sWin.extend(sWin2)
    sDif = []
    sDif.extend(sDif1)
    sDif.extend(sDif2)
    teamNames = []
    teamNames.extend(teamNames1)
    teamNames.extend(teamNames2)

    GLC.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast*2, sDir,sOutput,bTeam, bProj, teamNames, sMinGames, sLang)
    GLC.get5FasesStats(statsPlayers, season, jorFirst, jorLast*2, sDir, int(1), sLeague.split(',')[0], sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif, teamNames, sLang)

def extractStatistics(html_doc,targetTeam,againstTeams,againstTeams2,season,jorFirst,jorLast,division,sDir,fases,sChrome,bAll,bTeam,sPlayers,bProj,sLeague,sOutput, sMinGames, sLang, bLast):

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

    if system == 'Linux' or system == 'Windows':
        iBenIn = 2
        iEndIn = -2
    elif system == 'Darwin':
        iBenIn = 0
        iEndIn = 0

    if sLeague != 'ORO' and sLeague != 'DIA':
        driver = webdriver.Chrome(sChrome)
        driver.get(html_doc)
        select = Select(driver.find_element_by_id('gruposDropDownList'))
        if system == 'Linux' or system == 'Windows':
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

    statsPlayers = []
    statsHome = []
    statsAway = []
    statsEasy = []
    statsTough = []
    if bLast:
        statsLast3 = []
    statsTop = []
    statsBot = []
    statsWin = []
    statsLost = []

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
                        if system == 'Linux' or system == 'Windows':
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

                            jorTot += 1
                            if jorTot > jorLast and bLast == True:
                                statsLast3.append(statsAppend)
                                statsLast3.append(teamStats)
                                statsLast3.append(teamStatsAgainst)

                            if system == 'Linux' or system == 'Windows':
                                candLocTeam = locTeam[2:-1]
                            else:
                                candLocTeam = locTeam

                            if targetTeam in candLocTeam:
                                if system == 'Linux' or system == 'Windows':
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
                                if system == 'Linux' or system == 'Windows':
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


    if statsPlayers == []:
        print('Non-existent FEB Data')

    if bLast:
        return bHome, tipusPartit, bAgainst, bAgainst2, statsPlayers, statsHome, statsAway, statsEasy, statsTough, statsTop, statsBot, statsWin, statsLost, statsLast3,  sLocal, sAway, sWin, sDif,
    else:
        return bHome, tipusPartit, bAgainst, bAgainst2, statsPlayers, statsHome, statsAway, statsEasy, statsTough, statsTop, statsBot, statsWin, statsLost,  sLocal, sAway, sWin, sDif,


def extractStatisticsAllLeague(html_doc,targetTeam,season,jorFirst,jorLast,division,sDir,sChrome,bTeam,sPlayers,bProj,sLeague,sOutput,sMinGames, sLang, statsPlayers):

    html_doc_alt1 = html_doc + "&med=0"
    html_doc_alt2 = html_doc + "&med=1"
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    system = platform.system()

    jornadas = soup.find_all('div', class_="contentTablaDataGrid")
    firstJornada = jornadas[0].text.split('/')[0]

    if sLang == "Castellano":
        sAllR = "Jornadas"
        sJor = 'Jornada: '
        sExtr = 'Extrayendo Partidos:'
    else:
        sAllR = "AllRounds"
        sJor = 'Round: '
        sExtr = 'Extracting Games:'

    if sLeague != 'ORO' and sLeague != 'DIA':
        driver = webdriver.Chrome(sChrome)
        driver.get(html_doc)
        select = Select(driver.find_element_by_id('gruposDropDownList'))
        if system == 'Linux' or system == 'Windows':
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
    return statsPlayers, sLocal, sAway, sWin, sDif, teamNames


