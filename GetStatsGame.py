from bs4 import BeautifulSoup
import requests



def getStats(html_doc):
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    playersList = soup.find_all('tr', class_="itemAlternativoTabla")
    playersList.extend(soup.find_all('tr', class_="itemTabla"))
    playersHome = []
    playersAway = []
    numHome = []
    numAway = []
    init5Home = []
    init5Away = []
    minHome = []
    minAway = []
    ptsHome = []
    ptsAway = []
    t2Home = []
    t2Away = []
    t3Home = []
    t3Away = []
    t1Home = []
    t1Away = []
    rOfHome = []
    rOfAway = []
    rDefHome = []
    rDefAway = []
    assisHome = []
    assisAway = []
    recHome = []
    recAway = []
    perHome = []
    perAway = []
    tapFavHome = []
    tapFavAway = []
    tapConHome = []
    tapConAway = []
    matHome = []
    matAway = []
    falComHome = []
    falComAway = []
    falSofHome = []
    falSofAway = []
    valHome = []
    valAway = []


    for i in range(0,len(playersList)):
        if playersList[i].contents[17].span['id'][9:12] == 'Loc':
            bLoc = True
            playersHome.append(playersList[i].contents[3].text)
            numHome.append(playersList[i].contents[17].text)
            try:
                if playersList[i].contents[1].img['src'] == 'imagenes/punto.gif':
                    init5Home.append(True)
            except:
                init5Home.append(False)
            minHome.append(playersList[i].contents[4].text)
            ptsHome.append(playersList[i].contents[5].text)
            t2Home.append(playersList[i].contents[6].text)
            t3Home.append(playersList[i].contents[7].text)
            t1Home.append(playersList[i].contents[9].text)
            rOfHome.append(playersList[i].contents[10].find_all('span')[1].text)
            rDefHome.append(playersList[i].contents[10].find_all('span')[0].text)
            assisHome.append(playersList[i].contents[11].text)
            recHome.append(playersList[i].contents[12].text)
            perHome.append(playersList[i].contents[13].text)
            tapFavHome.append(playersList[i].contents[14].find_all('span')[0].text)
            tapConHome.append(playersList[i].contents[14].find_all('span')[1].text)
            matHome.append(playersList[i].contents[15].text)
            falComHome.append(playersList[i].contents[16].find_all('span')[0].text)
            falSofHome.append(playersList[i].contents[16].find_all('span')[1].text)
            valHome.append(playersList[i].contents[17].text)


        else:
            bLoc = False
            playersAway.append(playersList[i].contents[3].text)
            numAway.append(playersList[i].contents[17].text)
            try:
                if playersList[i].contents[1].img['src'] == 'imagenes/punto.gif':
                    init5Away.append(True)
            except:
                init5Away.append(False)
            minAway.append(playersList[i].contents[4].text)
            ptsAway.append(playersList[i].contents[5].text)
            t2Away.append(playersList[i].contents[6].text)
            t3Away.append(playersList[i].contents[7].text)
            t1Away.append(playersList[i].contents[9].text)
            rOfAway.append(playersList[i].contents[10].find_all('span')[1].text)
            rDefAway.append(playersList[i].contents[10].find_all('span')[0].text)
            assisAway.append(playersList[i].contents[11].text)
            recAway.append(playersList[i].contents[12].text)
            perAway.append(playersList[i].contents[13].text)
            tapFavAway.append(playersList[i].contents[14].find_all('span')[0].text)
            tapConAway.append(playersList[i].contents[14].find_all('span')[1].text)
            matAway.append(playersList[i].contents[15].text)
            falComAway.append(playersList[i].contents[16].find_all('span')[0].text)
            falSofAway.append(playersList[i].contents[16].find_all('span')[1].text)
            valAway.append(playersList[i].contents[17].text)

    return [playersHome, numHome, init5Home, minHome, ptsHome, t2Home, t3Home, t1Home, rOfHome, rDefHome, assisHome, recHome, perHome, tapFavHome, tapConHome, matHome, falComHome, falSofHome, valHome], \
           [playersAway, numAway, init5Away, minAway, ptsAway, t2Away, t3Away, t1Away, rOfAway, rDefAway, assisAway, recAway, perAway, tapFavAway, tapConAway, matAway, falComAway, falSofAway, valAway]
