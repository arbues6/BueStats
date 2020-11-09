from bs4 import BeautifulSoup
import requests
import numpy as np
import GetStatsGame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
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


    jornadas = soup.find_all('table')
    # firstJornada = jornadas[0].text.split('/')[0]

    iBenIn = 2
    iEndIn = -1

    chrome_options = Options()
    # maximized window
    chrome_options.add_argument("--start-maximized")

    firstJornada = jornadas[0].text.split('/')[0]
    if sLeague != 'ORO' and sLeague != 'DIA':
        if sLeague[:3] == 'ORO':
            division = sLeague[4:]
        driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
        driver.get(html_doc)
        # select = Select(driver.find_element_by_id('gruposDropDownList'))
        select = Select(driver.find_element_by_id('_ctl0_MainContentPlaceHolderMaster_gruposDropDownList'))
        if system == 'Linux' or system == 'Darwin':
            for listPhase in range(0, len(select.options)):
                if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '')[2:-1].split(' '):
                    iSelect = listPhase
        else:
            for listPhase in range(0, len(select.options)):
                if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '')[2:-1].split(' '):
                    iSelect = listPhase

        if sLeague == 'EBA,C4' or sLeague == 'EBA,C5':
            html_doc = 'https://baloncestoenvivo.feb.es/calendario/ligaeba/3/2020'
            driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
            driver.get(html_doc)
            # select = Select(driver.find_element_by_id('gruposDropDownList'))
            select = Select(driver.find_element_by_id('_ctl0_MainContentPlaceHolderMaster_gruposDropDownList'))
            if system == 'Linux' or system == 'Darwin':
                for listPhase in range(0, len(select.options)):
                    if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '')[2:-1].split(' '):
                        iSelect = listPhase
            else:
                for listPhase in range(0, len(select.options)):
                    if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-', '')[2:-1].split(' '):
                        iSelect = listPhase
        select.select_by_visible_text(select.options[iSelect].text)
        # time.sleep(5)
        to_soup = driver.page_source
        driver.close()

        soup = BeautifulSoup(to_soup, 'lxml')
        jornadas = soup.find_all('table')

        if jornadas[0].text.split('/')[0] == firstJornada and iSelect != 0:
            driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
            driver.get(html_doc_alt1)
            select = Select(driver.find_element_by_id('_ctl0_MainContentPlaceHolderMaster_gruposDropDownList'))
            select.select_by_visible_text(select.options[iSelect].text)
            # time.sleep(5)
            to_soup = driver.page_source
            driver.close()
            soup = BeautifulSoup(to_soup, 'lxml')
            jornadas = soup.find_all('div', class_="contentTablaDataGrid")
            try:
                if jornadas[0].text.split('/')[0] == firstJornada and iSelect != 0:
                    driver = webdriver.Chrome(sChrome, chrome_options=chrome_options)
                    driver.get(html_doc_alt2)
                    select = Select(driver.find_element_by_id('_ctl0_MainContentPlaceHolderMaster_gruposDropDownList'))
                    select.select_by_visible_text(select.options[iSelect].text)
                    # time.sleep(5)
                    to_soup = driver.page_source
                    driver.close()
                    soup = BeautifulSoup(to_soup, 'lxml')
                    jornadas = soup.find_all('div', class_="contentTablaDataGrid")
            except:
                pass
        jornadas = soup.find_all('table')

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

    pageIn = 0
    pageFin = 1

    sPlayers = sPlayers.split(',')
    sPlayers = [x.upper() for x in sPlayers]
    
    againstTeams = [x.upper() for x in againstTeams]
    againstTeams2 = [x.upper() for x in againstTeams2]
    
    for page in range(pageIn,pageFin):
        print(sExt)

        jorProcessFirst = int(jorFirst)
        jorProcessLast = int(jorLast)+1

        for jornada in range(jorProcessFirst, jorProcessLast):
            jorTot += 1
            jornadaInd = jornadas[jornada-1]
            gamesJorn = jornadaInd.find_all('td')
            itOdd = 0
            for k in range(0, len(gamesJorn)):
                if np.mod(k-1,3) != 0:
                    itOdd += 1
                    if iEndIn != 0:
                        candName = str(unicodedata.normalize('NFKD', gamesJorn[k].text.replace('\n', ' ')).encode('ascii', 'ignore'))[iBenIn:iEndIn]
                    else:
                        candName = str(unicodedata.normalize('NFKD', gamesJorn[k].text.replace('\n', ' ')).encode('ascii', 'ignore'))
                    if targetTeam in candName:
                        if np.mod(itOdd,2) == 1:
                            iSearch = k+1
                            iLocInd = k
                            iVisInd = k+2
                        else:
                            iSearch = k-1
                            iLocInd = k-2
                            iVisInd = k

                        gameCode = gamesJorn[iSearch].find_all('a')[0]['href']
                        realLink = "http://competiciones.feb.es/Estadisticas/" + gameCode
                        a, b = GetStatsGame.getStats(realLink)

                        # locTeam = str(unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[1]).encode('ascii', 'ignore'))
                        locTeam = str(unicodedata.normalize('NFKD', gamesJorn[iLocInd].text.split('\n')[1]).encode('ascii', 'ignore'))[iBenIn:iEndIn]
                        visTeam = str(unicodedata.normalize('NFKD', gamesJorn[iVisInd].text.split('\n')[1]).encode('ascii', 'ignore'))[iBenIn:iEndIn]

                        try:
                            resLocIn = int(gamesJorn[iSearch].text.split('\n')[1].split('-')[0])
                            resVisIn = int(gamesJorn[iSearch].text.split('\n')[1].split('-')[1])
                            resLoc.append(resLocIn)
                            resVis.append(resVisIn)

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
                                        a1p = [list(x) for x in list(np.array(a1)[:,:-1])]
                                        statsPlayers.append(a1p)
                                        statsHome.append(a1p)
                                    # teamStats = GetStatsTeam.getStats(realLink, True)
                                    teamStats = list(np.array(a1)[:,-1])
                                    # teamStatsAgainst = GetStatsTeam.getStatsAgainst(realLink, False)
                                    teamStatsAgainst = list(np.array(b)[:,-1])
                                    if sLang == 'Castellano':
                                        teamStats[0] = 'Equipo'
                                        teamStatsAgainst[0] = 'Equipo Rival'
                                    else:
                                        teamStats[0] = 'Team'
                                        teamStatsAgainst[0] = 'Team Against'

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
                                        b1p = [list(x) for x in list(np.array(b1)[:, :-1])]
                                        statsPlayers.append(b1p)
                                        statsAway.append(b1p)
                                    # teamStats = GetStatsTeam.getStats(realLink, False)
                                    teamStats = list(np.array(b1)[:,-1])
                                    teamStatsAgainst = list(np.array(a)[:,-1])
                                    if sLang == 'Castellano':
                                        teamStats[0] = 'Equipo'
                                        teamStatsAgainst[0] = 'Equipo Rival'
                                    else:
                                        teamStats[0] = 'Team'
                                        teamStatsAgainst[0] = 'Team Against'

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

                                if (jorTot) > (jorLast-4):
                                    statsLast3.append(statsAppend)
                                    statsLast3.append(teamStats)
                                    statsLast3.append(teamStatsAgainst)

                                candLocTeam = locTeam
                                if targetTeam in candLocTeam:
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
