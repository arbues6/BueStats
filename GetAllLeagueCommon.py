from bs4 import BeautifulSoup
import requests
import numpy as np
import GetStatsGame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
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

def extractStatisticsAllLeague(html_doc,targetTeam,season,jorFirst,jorLast,division,sDir,sChrome,bTeam,sPlayers,bProj,sLeague,sOutput,sMinGames, sLang, bOnlyTeam):

    html_doc_alt1 = html_doc + "&med=0"
    html_doc_alt2 = html_doc + "&med=1"
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    system = platform.system()

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

    jornadas = soup.find_all('table')
    firstJornada = jornadas[0].text.split('/')[0]

    chrome_options = Options()
    # maximized window
    chrome_options.add_argument("--start-maximized")

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

    for page in range(pageIn,pageFin):
        print(sExtr)
        for jornada in range(jorProcessFirst, jorProcessLast):
            print(sJor + str(jorProcessFirst + (jornada-jorProcessFirst) + 1))
            jorTot += 1
            jornadaInd = jornadas[jornada]
            gamesJorn = jornadaInd.find_all('td')
            itOdd = 0
            for k in range(0, len(gamesJorn), 3):
                itOdd += 1

                gameCode = gamesJorn[k+1].find_all('a')[0]['href']
                realLink = "http://competiciones.feb.es/Estadisticas/" + gameCode
                a, b = GetStatsGame.getStats(realLink)

                locTeam = str(unicodedata.normalize('NFKD', gamesJorn[k].text.split('\n')[1]).encode('ascii', 'ignore'))[iBenIn:iEndIn]
                visTeam = str(unicodedata.normalize('NFKD', gamesJorn[k+2].text.split('\n')[1]).encode('ascii', 'ignore'))[iBenIn:iEndIn]

                resLocIn = int(gamesJorn[k+1].text.split('\n')[1].split('-')[0])
                resVisIn = int(gamesJorn[k+1].text.split('\n')[1].split('-')[1])

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
                        difa = float(resVis[-1])-float(resLoc[-1])
                        if difa > 0:
                            sWin.append(True)
                        else:
                            sWin.append(False)
                        sDif.append(difa)
                except:
                    pass

    if sPlayers != [] and bOnlyTeam == False:
        sOutput = sOutput + '-' + str(len(sPlayers)) + 'Pl'

    if bOnlyTeam == False:
        GLC.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast, sDir,sOutput,bTeam, bProj, teamNames,sMinGames, sLang, True)
        GLC.get5FasesStats(statsPlayers, season, jorFirst, jorLast, sDir, int(1), sLeague.split(',')[0], sAllR+sOutput, bTeam, False, sLocal, sAway, sWin, sDif, teamNames, sLang, len(sPlayers))
    else:
        if targetTeam[4:9] == 'PLATA' or targetTeam[4:7] == 'LF2' or targetTeam[4:7] == 'EBA':
            sOutput = targetTeam[4:]
            sLeague = ''
        GLC.getAvStatsLeague(statsPlayers, sLeague.split(',')[0], season, jorFirst, jorLast, sDir,sOutput,bTeam, bProj, teamNames,sMinGames, sLang, True)
