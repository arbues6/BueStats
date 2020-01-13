from bs4 import BeautifulSoup
import requests



def getStats(html_doc, bLoc):
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    teamList = soup.find_all('td', class_="totales")
    
    players = []
    num = []
    init5 = []
    min = []
    pts = []
    t2 = []
    t3 = []
    t1 = []
    rOf = []
    rDef = []
    assis = []
    rec = []
    per = []
    tapFav = []
    tapCon = []
    mat = []
    falCom = []
    falSof = []
    val = []

    if bLoc == True:
        players.append('Team')
        num.append('None')
        init5.append(False)
        min.append(teamList[1].text)
        pts.append(teamList[2].text)
        t2.append(teamList[3].text)
        t3.append(teamList[4].text)
        t1.append(teamList[6].text)
        rOf.append(teamList[7].find_all('span')[1].text)
        rDef.append(teamList[7].find_all('span')[0].text)
        assis.append(teamList[8].text)
        rec.append(teamList[9].text)
        per.append(teamList[10].text)
        tapFav.append(teamList[11].find_all('span')[0].text)
        tapCon.append(teamList[11].find_all('span')[1].text)
        mat.append(teamList[12].text)
        falCom.append(teamList[13].find_all('span')[0].text)
        falSof.append(teamList[13].find_all('span')[1].text)
        val.append(teamList[14].text)
    else:
        players.append('Team')
        num.append('None')
        init5.append(False)
        min.append(teamList[17].text)
        pts.append(teamList[18].text)
        t2.append(teamList[19].text)
        t3.append(teamList[20].text)
        t1.append(teamList[22].text)
        rOf.append(teamList[23].find_all('span')[1].text)
        rDef.append(teamList[23].find_all('span')[0].text)
        assis.append(teamList[24].text)
        rec.append(teamList[25].text)
        per.append(teamList[26].text)
        tapFav.append(teamList[27].find_all('span')[0].text)
        tapCon.append(teamList[27].find_all('span')[1].text)
        mat.append(teamList[28].text)
        falCom.append(teamList[29].find_all('span')[0].text)
        falSof.append(teamList[29].find_all('span')[1].text)
        val.append(teamList[30].text)

    return [players, num, init5, min, pts, t2, t3, t1, rOf, rDef, assis, rec, per, tapFav, tapCon, mat, falCom, falSof, val]


def getStatsAgainst(html_doc, bLoc):
    req = requests.get(html_doc)
    soup = BeautifulSoup(req.text, 'lxml')

    teamList = soup.find_all('td', class_="totales")

    players = []
    num = []
    init5 = []
    min = []
    pts = []
    t2 = []
    t3 = []
    t1 = []
    rOf = []
    rDef = []
    assis = []
    rec = []
    per = []
    tapFav = []
    tapCon = []
    mat = []
    falCom = []
    falSof = []
    val = []

    if bLoc == True:
        players.append('Against')
        num.append('None')
        init5.append(False)
        min.append(teamList[1].text)
        pts.append(teamList[2].text)
        t2.append(teamList[3].text)
        t3.append(teamList[4].text)
        t1.append(teamList[6].text)
        rOf.append(teamList[7].find_all('span')[1].text)
        rDef.append(teamList[7].find_all('span')[0].text)
        assis.append(teamList[8].text)
        rec.append(teamList[9].text)
        per.append(teamList[10].text)
        tapFav.append(teamList[11].find_all('span')[0].text)
        tapCon.append(teamList[11].find_all('span')[1].text)
        mat.append(teamList[12].text)
        falCom.append(teamList[13].find_all('span')[0].text)
        falSof.append(teamList[13].find_all('span')[1].text)
        val.append(teamList[14].text)
    else:
        players.append('Against')
        num.append('None')
        init5.append(False)
        min.append(teamList[17].text)
        pts.append(teamList[18].text)
        t2.append(teamList[19].text)
        t3.append(teamList[20].text)
        t1.append(teamList[22].text)
        rOf.append(teamList[23].find_all('span')[1].text)
        rDef.append(teamList[23].find_all('span')[0].text)
        assis.append(teamList[24].text)
        rec.append(teamList[25].text)
        per.append(teamList[26].text)
        tapFav.append(teamList[27].find_all('span')[0].text)
        tapCon.append(teamList[27].find_all('span')[1].text)
        mat.append(teamList[28].text)
        falCom.append(teamList[29].find_all('span')[0].text)
        falSof.append(teamList[29].find_all('span')[1].text)
        val.append(teamList[30].text)

    return [players, num, init5, min, pts, t2, t3, t1, rOf, rDef, assis, rec, per, tapFav, tapCon, mat, falCom, falSof, val]
