from bs4 import BeautifulSoup
import requests
import numpy as np


def getStats(html_doc):
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    playersList = soup.find_all('td', class_="nombre jugador")
    numbersList = soup.find_all('td', class_="dorsal")
    inicialList = soup.find_all('td', class_="inicial")
    minsList = soup.find_all('td', class_="minutos")
    puntosList = soup.find_all('td', class_="puntos")
    t2List = soup.find_all('td', class_="tiros dos")
    t3List = soup.find_all('td', class_="tiros tres")
    t1List = soup.find_all('td', class_="tiros libres")
    rebofList = soup.find_all('td', class_="rebotes ofensivos")
    rebdefList = soup.find_all('td', class_="rebotes defensivos")
    assisList = soup.find_all('td', class_="asistencias")
    recList = soup.find_all('td', class_="recuperaciones")
    perList = soup.find_all('td', class_="perdidas")
    tapfList = soup.find_all('td', class_="tapones favor")
    tapcList = soup.find_all('td', class_="tapones contra")
    matList = soup.find_all('td', class_="mates")
    falcList = soup.find_all('td', class_="faltas cometidas")
    falsList = soup.find_all('td', class_="faltas recibidas")
    valList = soup.find_all('td', class_="valoracion")

    names = []
    for i in range(0, len(playersList)):
        names.append(playersList[i].text)
    names = np.array(names)
    nLocals = np.argmax(names=='')

    # playersList.extend(soup.find_all('tr', class_="itemTabla"))
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
        # if playersList[i].contents[17].span['id'][9:12] == 'Loc':
        if i < nLocals+1:
            playersHome.append(playersList[i].text)
            numHome.append(numbersList[i].text)
            try:
                if inicialList[i].text == '':
                    init5Home.append(False)
                else:
                    init5Home.append(True)
            except:
                pass
            minHome.append(minsList[i].text)
            ptsHome.append(puntosList[i].text)
            t2Home.append(t2List[i].text)
            t3Home.append(t3List[i].text)
            t1Home.append(t1List[i].text)
            rOfHome.append(rebofList[i].text)
            rDefHome.append(rebdefList[i].text)
            assisHome.append(assisList[i].text)
            recHome.append(recList[i].text)
            perHome.append(perList[i].text)
            tapFavHome.append(tapfList[i].text)
            tapConHome.append(tapcList[i].text)
            matHome.append(matList[i].text)
            falComHome.append(falcList[i].text)
            falSofHome.append(falsList[i].text)
            valHome.append(valList[i].text)
        else:
            playersAway.append(playersList[i].text)
            numAway.append(numbersList[i].text)
            if inicialList[i].text == '':
                init5Away.append(False)
            else:
                init5Away.append(True)
            minAway.append(minsList[i].text)
            ptsAway.append(puntosList[i].text)
            t2Away.append(t2List[i].text)
            t3Away.append(t3List[i].text)
            t1Away.append(t1List[i].text)
            rOfAway.append(rebofList[i].text)
            rDefAway.append(rebdefList[i].text)
            assisAway.append(assisList[i].text)
            recAway.append(recList[i].text)
            perAway.append(perList[i].text)
            tapFavAway.append(tapfList[i].text)
            tapConAway.append(tapcList[i].text)
            matAway.append(matList[i].text)
            falComAway.append(falcList[i].text)
            falSofAway.append(falsList[i].text)
            valAway.append(valList[i].text)

    return [playersHome, numHome, init5Home, minHome, ptsHome, t2Home, t3Home, t1Home, rOfHome, rDefHome, assisHome, recHome, perHome, tapFavHome, tapConHome, matHome, falComHome, falSofHome, valHome], \
           [playersAway, numAway, init5Away, minAway, ptsAway, t2Away, t3Away, t1Away, rOfAway, rDefAway, assisAway, recAway, perAway, tapFavAway, tapConAway, matAway, falComAway, falSofAway, valAway]
