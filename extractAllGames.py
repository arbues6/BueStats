import GetAllGamesCommon
import GetAllLeagueCommon
import GetAllLeagueBothPlata
from importlib import reload

def extractStats(division, season, targetTeam, jorFirst, jorLast, sDir, chromeDriver):
    print(division)
    divSplit = division.split(',')[0]
    try:
        groupSplit = division.split(',')[1]
    except:
        pass

    if division == 'ENDESA' or division == 'LF':
        html_name = 'lfendesa'
        division = 'DIA'
    if division == 'ORO' or division.split(',')[0] == 'ORO':
        html_name = 'ligaleboro'
        groupFeb = '1'
    elif division == 'DIA':
        html_name = 'lfendesa'
        groupFeb = '4'
    elif divSplit == 'PLATA':
        html_name = 'ligalebplata'
        bUnaFase = False
        if len(division.split(',')) == 3:
            if int(season) > 2017:
                if division.split(',')[2] == 'A1':
                    groupFeb = '2'
                else:
                    groupFeb = '18'
            else:
                groupFeb = '2'
        else:
            bUnaFase = True
            if int(season) > 2017:
                if division.split(',')[1] == 'ESTE':
                    groupFeb = '2'
                else:
                    groupFeb = '18'
            else:
                groupFeb = '2'
    elif divSplit == 'EBA':
        html_name = 'ligaeba'
        if groupSplit[0] == 'A': # AA AB AC
            if int(season) > 2019:
                if groupSplit[1] == 'A':
                    groupFeb = '3'
                else:
                    groupFeb = '17'
            else:
                groupFeb = '3'
        elif groupSplit[0] == 'B': # BA BBA
            if int(season) > 2019:
                if int(season) < 2021:
                    if groupSplit[1] == 'A':
                        groupFeb = '5'
                    else:
                        groupFeb = '57'
                else:
                    groupFeb = '5'
            else:
                groupFeb = '5'
        elif groupSplit[0] == 'C': # C1 C2 C3
            if int(season) > 2019:
                if groupSplit[1] == '1':
                    groupFeb = '48'
                elif groupSplit[1] == '2':
                    groupFeb = '49'
                elif groupSplit[1] == '3':
                    groupFeb = '59'
                elif groupSplit[1] == '4':
                    groupFeb = '60'
                elif groupSplit[1] == '5':
                    groupFeb = '61'
            elif int(season) > 2018:
                if groupSplit[1] == 'A':
                    groupFeb = '6'
                elif groupSplit[1] == 'B' or groupSplit[1] == '2':
                    groupFeb = '46'
                elif groupSplit[1] == 'C' or groupSplit[1] == '3':
                    groupFeb = '46'
            else:
                groupFeb = '6'
        elif groupSplit[0] == 'D': # DA DB
            if int(season) > 2019:
                if groupSplit[1] == 'A':
                    groupFeb = '7'
                else:
                    groupFeb = '47'
            else:
                groupFeb = '7'
        elif groupSplit[0] == 'E': # EA EB
            if int(season) > 2019:
                if groupSplit[1] == 'A':
                    groupFeb = '8'
                elif groupSplit[1] == 'B':
                    groupFeb = '39'
                elif groupSplit[1] == 'C':
                    groupFeb = '53'
            else:
                groupFeb = '8'
    elif divSplit == 'LF2': # A B C
        html_name = 'ligaeba'
        if int(season) > 2019:
            if groupSplit == 'A':
                groupFeb = '9'
            elif groupSplit == 'B':
                groupFeb = '10'
            elif groupSplit == 'C':
                groupFeb = '56'
        else:
            groupFeb = '9'
    elif divSplit == 'LFCHALLENGE':  # A B C
        html_name = 'lfchallenge'
        groupFeb = '67'

    html_doc = "https://baloncestoenvivo.feb.es/calendario/" + html_name + '/' + groupFeb + '/' + season
    if division == 'ORO' or division == 'DIA' or division == 'ENDESA' or division == 'LF' or division == 'LFCHALLENGE':
        GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division, sDir, chromeDriver, 1, '', False, division, '', '', 'Castellano', False)
    elif divSplit == 'ORO':
        GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, chromeDriver, 1, '', False, division, '', '', 'Castellano', False)
    elif divSplit == 'PLATA':
        if bUnaFase == False:
            GetAllLeagueBothPlata.extractStatisticsPlataAll(html_doc,targetTeam,season,jorFirst,jorLast,division.split(',')[1],division.split(',')[2],sDir,chromeDriver,1,'',False,division,'','', 'Castellano', False)
            reload(GetAllLeagueBothPlata)
        else:
            GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, chromeDriver, 1, '', False, '', 'Fase1', '', 'Castellano', False)
    elif divSplit == 'EBA':
        GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, chromeDriver, 1, '', False, division, '', '', 'Castellano', False)
    elif divSplit == 'LF2':
        GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, chromeDriver, 1, '', False, division, '', '', 'Castellano', False)
    reload(GetAllLeagueCommon)

path = '/Users/adriaarbues/Documents/BueStats/2022Ver27Oct/BueStats-master/'
#extractStats('ORO,OROCLASIF', '2020', 'Liga', 1, 18, path + 'Reports/', path + 'chromedriver')
#extractStats('ORO,OROPERMAN', '2020', 'Liga', 1, 12, path + 'Reports/', path + 'chromedriver')

extractStats('ORO', '2021', 'Liga', 1, 12, path + 'Reports/Oro/', path + 'chromedriver')
extractStats('ENDESA', '2021', 'Liga', 1, 13, path + 'Reports/LF/', path + 'chromedriver')
extractStats('LFCHALLENGE', '2021', 'Liga', 1, 16, path + 'Reports/LFCHALLENGE/', path + 'chromedriver')
extractStats('PLATA,ESTE', '2021', 'Liga', 1, 11, path + 'Reports/PLATA/ESTE/', path + 'chromedriver')
extractStats('PLATA,OESTE', '2021', 'Liga', 1, 11, path + 'Reports/PLATA/OESTE/', path + 'chromedriver')
extractStats('LF2,A', '2021', 'Liga', 1, 12, path + 'Reports/LF2/A/', path + 'chromedriver')
extractStats('LF2,B', '2021', 'Liga', 1, 12, path + 'Reports/LF2/B/', path + 'chromedriver')
extractStats('EBA,AA', '2021', 'Liga', 1, 14, path + 'Reports/EBA/AA/', path + 'chromedriver')
extractStats('EBA,AB', '2021', 'Liga', 1, 15, path + 'Reports/EBA/AB/', path + 'chromedriver')
extractStats('EBA,B', '2021', 'Liga', 1, 14, path + 'Reports/EBA/B/', path + 'chromedriver')
extractStats('EBA,C1', '2021', 'Liga', 1, 11, path + 'Reports/EBA/C1/', path + 'chromedriver')
extractStats('EBA,C2', '2021', 'Liga', 1, 11, path + 'Reports/EBA/C2/', path + 'chromedriver')
extractStats('EBA,C3', '2021', 'Liga', 1, 11, path + 'Reports/EBA/C3/', path + 'chromedriver')
extractStats('EBA,DA', '2021', 'Liga', 1, 11, path + 'Reports/EBA/DA/', path + 'chromedriver')
extractStats('EBA,DB', '2021', 'Liga', 1, 11, path + 'Reports/EBA/DB/', path + 'chromedriver')
extractStats('EBA,EA', '2021', 'Liga', 1, 12, path + 'Reports/EBA/EA/', path + 'chromedriver')
extractStats('EBA,EB', '2021', 'Liga', 1, 12, path + 'Reports/EBA/EB/', path + 'chromedriver')
extractStats('EBA,EC', '2021', 'Liga', 1, 12, path + 'Reports/EBA/EC/', path + 'chromedriver')