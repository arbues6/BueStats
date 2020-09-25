from bs4 import BeautifulSoup
import requests
import numpy as np
import GetStatsGame
import GetStatsTeam
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from pandas import DataFrame
from selenium.webdriver.chrome.options import Options
import GamesCommonFunctionsAllLeague as GLC
import GamesCommonFuctions as GC
import unicodedata
import platform


teamNames = []
sLocal = []
sAway = []
sWin = []
sDif = []
chrome_options = Options()
# maximized window
chrome_options.add_argument("--start-maximized")


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

def extractStatisticsPlataAll(html_doc,targetTeam,season,jorFirst,jorLast,division1,division2,sDir,sChrome,bTeam,sPlayers,bProj,sLeague,sOutput,sMinGames, sLang, bOnlyTeam):
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

    if bOnlyTeam == False:
        GLC.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast*2, sDir,sOutput,bTeam, bProj, teamNames,sMinGames, sLang, False)
        GLC.get5FasesStats(statsPlayers, season, jorFirst, jorLast*2, sDir, int(1), sLeague.split(',')[0], sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif, teamNames, sLang)
    else:
        GLC.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast*2, sDir,'-'+division1+'-'+division2,bTeam, bProj, teamNames, sMinGames, sLang, True)

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

    jornadas = soup.find_all('table')

    if system == 'Linux':
        iBenIn = 2
        iEndIn = -1
    elif system == 'Darwin' or system == 'Windows':
        iBenIn = 0
        iEndIn = 0

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

        select.select_by_visible_text(select.options[iSelect].text)
        # time.sleep(5)
        to_soup = driver.page_source
        driver.close()
        soup = BeautifulSoup(to_soup, 'lxml')
        jornadas = soup.find_all('table')
        firstJornada = jornadas[0].text.split('/')[0]

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

                        resLocIn = int(gamesJorn[iSearch].text.split('\n')[1].split('-')[0])
                        resVisIn = int(gamesJorn[iSearch].text.split('\n')[1].split('-')[1])
                        resLoc.append(resLocIn)
                        resVis.append(resVisIn)
                        try:
                            if len(sPlayers) > 0 and sPlayers[0] != '':
                                a1 = GC.filterPlayers(a, sPlayers)
                            else:
                                a1 = a
                            if a1 != []:
                                a1p = [list(x) for x in list(np.array(a1)[:, :-1])]
                                statsPlayers.append(a1p)
                                teamStats = list(np.array(a1)[:, -1])
                                teamStatsAgainst = list(np.array(b)[:, -1])
                                if sLang == 'Castellano':
                                    teamStats[0] = 'Equipo'
                                    teamStatsAgainst[0] = 'Equipo Rival'
                                else:
                                    teamStats[0] = 'Team'
                                    teamStatsAgainst[0] = 'Team Against'

                                statsPlayers.append(teamStats)
                                statsPlayers.append(teamStatsAgainst)
                                teamNames.append('Players')
                                teamNames.append(locTeam)
                                teamNames.append(visTeam)
                                sLocal.append(locTeam)
                                sAway.append(visTeam)
                                difa = float(resLoc[-1]) - float(resVis[-1])
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
                                b1p = [list(x) for x in list(np.array(b1)[:, :-1])]
                                teamStats = list(np.array(b1)[:, -1])
                                teamStatsAgainst = list(np.array(a)[:, -1])
                                if sLang == 'Castellano':
                                    teamStats[0] = 'Equipo'
                                    teamStatsAgainst[0] = 'Equipo Rival'
                                else:
                                    teamStats[0] = 'Team'
                                    teamStatsAgainst[0] = 'Team Against'
                                statsPlayers.append(b1p)
                                statsPlayers.append(teamStats)
                                statsPlayers.append(teamStatsAgainst)
                                teamNames.append('Players')
                                teamNames.append(visTeam)
                                teamNames.append(locTeam)
                                sLocal.append(locTeam)
                                sAway.append(visTeam)
                                difa = float(resVis[-1]) - float(resLoc[-1])
                                if difa > 0:
                                    sWin.append(True)
                                else:
                                    sWin.append(False)
                                sDif.append(difa)
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

    jornadas = soup.find_all('table')
    firstJornada = jornadas[0].text.split('/')[0]

    if system == 'Linux':
        iBenIn = 2
        iEndIn = -1
    elif system == 'Darwin' or system == 'Windows':
        iBenIn = 0
        iEndIn = 0

    if sLang == "Castellano":
        sAllR = "Jornadas"
        sJor = 'Jornada: '
        sExtr = 'Extrayendo Partidos:'
    else:
        sAllR = "AllRounds"
        sJor = 'Round: '
        sExtr = 'Extracting Games:'

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
                if str(division.encode('ascii', 'ignore')).upper()[2:-1] in str(select.options[listPhase].text.encode('ascii', 'ignore')).upper().replace('"', '').replace('-','')[2:-1].split(' '):
                    iSelect = listPhase

        select.select_by_visible_text(select.options[iSelect].text)
        # time.sleep(5)
        to_soup = driver.page_source
        driver.close()
        soup = BeautifulSoup(to_soup, 'lxml')
        jornadas = soup.find_all('table')
        firstJornada = jornadas[0].text.split('/')[0]

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

    resLoc = []
    resVis = []
    sLocal = []
    sAway = []
    sWin = []
    sDif = []

    jorTot = 0

    pageIn = 0
    pageFin = 1
    jorProcessFirst = int(jorFirst)-1
    jorProcessLast = int(jorLast)

    sPlayers = sPlayers.split(',')
    sPlayers = [x.upper() for x in sPlayers]

    for page in range(pageIn, pageFin):
        print(sExtr)
        for jornada in range(jorProcessFirst, jorProcessLast):
            print(sJor + str(jorProcessFirst + (jornada - jorProcessFirst) + 1))
            jorTot += 1
            jornadaInd = jornadas[jornada]
            gamesJorn = jornadaInd.find_all('td')
            itOdd = 0
            for k in range(0, len(gamesJorn), 3):
                itOdd += 1

                gameCode = gamesJorn[k + 1].find_all('a')[0]['href']
                realLink = "http://competiciones.feb.es/Estadisticas/" + gameCode
                a, b = GetStatsGame.getStats(realLink)

                locTeam = str(unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[1]).encode('ascii', 'ignore'))[iBenIn:iEndIn]
                visTeam = str(unicodedata.normalize('NFKD', gamesJorn[k + 2].text.split('\n')[1]).encode('ascii', 'ignore'))[iBenIn:iEndIn]

                resLocIn = int(gamesJorn[k + 1].text.split('\n')[1].split('-')[0])
                resVisIn = int(gamesJorn[k + 1].text.split('\n')[1].split('-')[1])

                resLoc.append(resLocIn)
                resVis.append(resVisIn)
                try:
                    if len(sPlayers) > 0 and sPlayers[0] != '':
                        a1 = GC.filterPlayers(a, sPlayers)
                    else:
                        a1 = a
                    if a1[0] != []:
                        a1p = [list(x) for x in list(np.array(a1)[:, :-1])]
                        statsPlayers.append(a1p)
                        teamStats = list(np.array(a1)[:, -1])
                        teamStatsAgainst = list(np.array(b)[:, -1])
                        if sLang == 'Castellano':
                            teamStats[0] = 'Equipo'
                            teamStatsAgainst[0] = 'Equipo Rival'
                        else:
                            teamStats[0] = 'Team'
                            teamStatsAgainst[0] = 'Team Against'

                        statsPlayers.append(teamStats)
                        statsPlayers.append(teamStatsAgainst)
                        teamNames.append('Players')
                        teamNames.append(locTeam)
                        teamNames.append(visTeam)
                        sLocal.append(locTeam)
                        sAway.append(visTeam)
                        difa = float(resLoc[-1]) - float(resVis[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)

                    if len(sPlayers) > 0 and sPlayers[0] != '':
                        b1 = GC.filterPlayers(b, sPlayers)
                    else:
                        b1 = b
                    if b1[0] != []:
                        b1p = [list(x) for x in list(np.array(b1)[:, :-1])]
                        teamStats = list(np.array(b1)[:, -1])
                        teamStatsAgainst = list(np.array(a)[:, -1])
                        if sLang == 'Castellano':
                            teamStats[0] = 'Equipo'
                            teamStatsAgainst[0] = 'Equipo Rival'
                        else:
                            teamStats[0] = 'Team'
                            teamStatsAgainst[0] = 'Team Against'
                        statsPlayers.append(b1p)
                        statsPlayers.append(teamStats)
                        statsPlayers.append(teamStatsAgainst)
                        teamNames.append('Players')
                        teamNames.append(visTeam)
                        teamNames.append(locTeam)
                        sLocal.append(locTeam)
                        sAway.append(visTeam)
                        difa = float(resVis[-1]) - float(resLoc[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)
                except:
                    pass

    return statsPlayers, sLocal, sAway, sWin, sDif, teamNames


