import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path):
    return OffsetImage(plt.imread(path))

orHeaders = ['Nombre', 'Condicion', 'Partidos', 'Minutos', 'Puntos', 'T2 Anotados', 'T2 Lanzados', '% T2', 'T3 Anotados', 'T3 Lanzados', '% T3', 'T1 Anotados', 'T1 Lanzados', '% T1', 'Reb. Ofensivos', 'Reb. Defensivos', 'Rebotes', 'Asistencias', 'Robos', 'Perdidas', 'Tapones', 'Tapones Recibidos', 'Mates', 'Faltas Cometidas', 'Faltas Recibidas', 'Valoracion', 'Posesiones', 'Ritmo', 'OER', '% TC Efectivo', '% Jugada', 'Frec. TL', '% Reb Def', '% Reb Of', '% Assis', '% Perd']


def draw2Features(teamStats,teamStatsAg,sDir,xAxisF,yAxisF,season,division,jI,jL):
    if len(division.split(',')) == 1:
        pathLogos = sDir + '/Logos/' + season + '/' + division + '/Resized/'
    elif len(division.split(',')) == 2 and division.split(',')[0] != 'PLATA':
        pathLogos = sDir + '/Logos/' + season + '/' + division.split(',')[0] + '/' + division.split(',')[1][0] + '/Resized/'
    else:
        pathLogos = sDir + '/Logos/' + season + '/PLATA/Resized/'

    imNamesReal = os.listdir(pathLogos)
    imNamesPath = [pathLogos + x for x in imNamesReal]
    imNames = [x[:-4].upper() for x in imNamesReal]

    if xAxisF[-3:] != 'Riv':
        if xAxisF[:3] == 'DER':
            posXfeat = orHeaders.index('OER')
            statsX = np.copy(teamStatsAg)
        else:
            posXfeat = orHeaders.index(xAxisF)
            statsX = np.copy(teamStats)
    else:
        if xAxisF[:3] == 'DER':
            posXfeat = orHeaders.index('OER')
            statsX = np.copy(teamStats)
        else:
            posXfeat = orHeaders.index(xAxisF[:-4])
            statsX = np.copy(teamStatsAg)

    if yAxisF[-3:] != 'Riv':
        if yAxisF[:3] == 'DER':
            posYfeat = orHeaders.index('OER')
            statsY = np.copy(teamStatsAg)
        else:
            posYfeat = orHeaders.index(yAxisF)
            statsY = np.copy(teamStats)
    else:
        if yAxisF[:3] == 'DER':
            posYfeat = orHeaders.index('OER')
            statsY = np.copy(teamStats)
        else:
            posYfeat = orHeaders.index(yAxisF[:-4])
            statsY = np.copy(teamStatsAg)

    featX = []
    featY = []
    teamName = []
    for iTeam in range(0,len(statsX)):
        featX.append(float(statsX[iTeam][posXfeat][0]))
        teamNameaux = statsX[iTeam][0]
        if teamNameaux[-7:] == 'Against':
            teamNameaux = teamNameaux[2:-9]
        else:
            teamNameaux = teamNameaux[2:-6]
        teamNameaux = teamNameaux.split(' ')
        for iPart in range(0,len(teamNameaux)):
            if teamNameaux[iPart].upper() in imNames:
                teamName.append(imNamesPath[imNames.index(teamNameaux[iPart].upper())])
                break
    for iTeam in range(0,len(statsX)):
        featY.append(float(statsY[iTeam][posYfeat][0]))

    if min(featX) > 1:
        iXmin = min(featX)-7
        iXmax = max(featX)+7
    else:
        iXmin = min(featX) - 0.05
        iXmax = max(featX) + 0.05

    if min(featY) > 1:
        iYmin = min(featY) - 7
        iYmax = max(featY) + 7
    else:
        iYmin = min(featY) - 0.05
        iYmax = max(featY) + 0.05

    fig, ax = plt.subplots()
    fig.set_figheight(20)
    fig.set_figwidth(30)
    # ax.scatter(featX, featY)

    for x0, y0, path in zip(featX, featY, teamName):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)
    fig.suptitle('Liga ' + division + '(' + season + ', J' + str(jI) + 'J' + str(jL) + ')', fontsize=30)
    plt.xlabel(xAxisF, fontsize=24)
    plt.ylabel(yAxisF, fontsize=24)
    plt.xticks(size=20)
    plt.yticks(size=20)

    plt.xlim((iXmin,iXmax))
    plt.ylim((iYmin,iYmax))
    # plt.show()
    plt.savefig(sDir + '/' + season + division + xAxisF.replace(' ','').replace('%','p') + yAxisF.replace(' ','').replace('%','p') + 'j' + str(jI) + 'j' + str(jL) + '.png')
