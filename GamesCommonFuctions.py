from pandas import DataFrame
import numpy as np
import datetime
import platform

def time2secs(timeVec):
    try:
        timeSec = (int(timeVec.split(":")[0]) * 60 + int(timeVec.split(":")[1]))
    except:
        timeSec = 0

    return timeSec

def parse_stats_scratch_player(statsPlayers, game, indPl, sType):
    lNames = []
    lNames.append(statsPlayers[game][0][indPl].encode('ascii',errors='ignore'))
    lTypes = []
    lTypes.append(sType)
    lGames = []
    lGames.append(int(1))
    lMins = []
    iMins = int(time2secs(statsPlayers[game][3][indPl]))
    lMins.append(iMins)
    lPts = []
    lPts.append(int(statsPlayers[game][4][indPl]))
    lt2S = []
    lt2S.append(int(statsPlayers[game][5][indPl].split("/")[0]))
    lt2A = []
    lt2A.append(int(statsPlayers[game][5][indPl].split("/")[1].split(" ")[0]))
    lt2p = []
    lt2p.append(int(statsPlayers[game][5][indPl].split("/")[1].split(" ")[1].split("%")[0]))
    lt3S = []
    lt3S.append(int(statsPlayers[game][6][indPl].split("/")[0]))
    lt3A = []
    lt3A.append(int(statsPlayers[game][6][indPl].split("/")[1].split(" ")[0]))
    lt3p = []
    lt3p.append(int(statsPlayers[game][6][indPl].split("/")[1].split(" ")[1].split("%")[0]))
    lt1S = []
    lt1S.append(int(statsPlayers[game][7][indPl].split("/")[0]))
    lt1A = []
    lt1A.append(int(statsPlayers[game][7][indPl].split("/")[1].split(" ")[0]))
    lt1p = []
    lt1p.append(int(statsPlayers[game][7][indPl].split("/")[1].split(" ")[1].split("%")[0]))
    lrOf = []
    lrOf.append(int(statsPlayers[game][8][indPl]))
    lrDef = []
    lrDef.append(int(statsPlayers[game][9][indPl]))
    lrReb = []
    lrReb.append(int(statsPlayers[game][8][indPl])+int(statsPlayers[game][9][indPl]))
    lAssis = []
    iAssis = int(statsPlayers[game][10][indPl])
    lAssis.append(iAssis)
    lRec = []
    lRec.append(int(statsPlayers[game][11][indPl]))
    lPer = []
    lPer.append(int(statsPlayers[game][12][indPl]))
    lTapF = []
    lTapF.append(int(statsPlayers[game][13][indPl]))
    lTapC = []
    lTapC.append(int(statsPlayers[game][14][indPl]))
    lMat = []
    lMat.append(int(statsPlayers[game][15][indPl]))
    lFalC = []
    lFalC.append(int(statsPlayers[game][16][indPl]))
    lFalF = []
    lFalF.append(int(statsPlayers[game][17][indPl]))
    lVal = []
    lVal.append(int(statsPlayers[game][18][indPl]))
    lAssisP = []
    lAssisP.append(0)
    lEffp = []
    lEffp.append(0)
    lTShoot = []
    lTShoot.append(0)
    lGScore = []
    lGScore.append(0)
    lScPoss = []
    lScPoss.append(0)
    lnScPoss = []
    lnScPoss.append(0)
    lTotPoss = []
    lTotPoss.append(0)
    lFloorPer = []
    lFloorPer.append(0)
    lPpshot = []
    lPpshot.append(0)
    lPerReb = []
    lPerDefReb = []
    lPerOfReb = []
    lPerReb.append(0)
    lPerDefReb.append(0)
    lPerOfReb.append(0)
    lStPer = []
    lStPer.append(0)
    lTouches = []
    lTouches.append(0)
    lUsage = []
    lUsage.append(0)
    lVersatility = []
    lVersatility.append(0)
    lWinScore = []
    lWinScore.append(0)
    lOERi = []
    lOERi.append(0)
    lDERi = []
    lDERi.append(0)
    lNet = []
    lNet.append(0)

    return [lNames, lTypes, lGames, lMins, lPts, lt2S, lt2A, lt2p, lt3S, lt3A, lt3p, lt1S, lt1A, lt1p, lrOf, lrDef, lrReb, lAssis, lRec, lPer, lTapF, lTapC, lMat, lFalC, lFalF, lVal, lAssisP, lEffp, lTShoot, lGScore, lScPoss, lnScPoss, lTotPoss, lFloorPer, lPpshot, lPerReb, lPerDefReb, lPerOfReb, lStPer, lTouches, lUsage, lVersatility, lWinScore, lOERi, lDERi, lNet]

def parse_stats_existing_player(statsPlayers, game, indPl, avStats, iPlayer, sType):
    avStats[indPl][2][0] = (int(avStats[indPl][2][0])+1)
    # Minutes
    try:
        iMins = time2secs(statsPlayers[game][3][iPlayer])
        avStats[indPl][3][0] = avStats[indPl][3][0]+iMins
    except:
        pass
    # Points
    iPts = int(statsPlayers[game][4][iPlayer])
    avStats[indPl][4][0] = int(avStats[indPl][4][0]) + iPts
    # lt2
    it2M = int(statsPlayers[game][5][iPlayer].split("/")[0])
    it2A = int(statsPlayers[game][5][iPlayer].split("/")[1].split(" ")[0])
    avStats[indPl][5][0] = int(avStats[indPl][5][0]) + it2M
    avStats[indPl][6][0] = int(avStats[indPl][6][0]) + it2A
    try:
        avStats[indPl][7][0] = float(avStats[indPl][5][0]) / float(avStats[indPl][6][0])
    except:
        avStats[indPl][7][0] = 0
    # lt3
    it3M = int(statsPlayers[game][6][iPlayer].split("/")[0])
    it3A = int(statsPlayers[game][6][iPlayer].split("/")[1].split(" ")[0])
    avStats[indPl][8][0] = int(avStats[indPl][8][0]) + it3M
    avStats[indPl][9][0] = int(avStats[indPl][9][0]) + it3A
    try:
        avStats[indPl][10][0] = float(avStats[indPl][8][0]) / float(avStats[indPl][9][0])
    except:
        avStats[indPl][10][0] = 0
    # lt1
    it1M =  int(statsPlayers[game][7][iPlayer].split("/")[0])
    it1A =  int(statsPlayers[game][7][iPlayer].split("/")[1].split(" ")[0])
    avStats[indPl][11][0] = int(avStats[indPl][11][0]) + it1M
    avStats[indPl][12][0] = int(avStats[indPl][12][0]) + it1A

    try:
        avStats[indPl][13][0] = float(avStats[indPl][11][0]) / float(avStats[indPl][12][0])
    except:
        avStats[indPl][13][0] = 0

    #Rebs
    iOfReb = int(statsPlayers[game][8][iPlayer])
    iDefReb = int(statsPlayers[game][9][iPlayer])
    avStats[indPl][14][0] = int(avStats[indPl][14][0]) + iOfReb
    avStats[indPl][15][0] = int(avStats[indPl][15][0]) + iDefReb
    avStats[indPl][16][0] = int(avStats[indPl][16][0]) + iOfReb + iDefReb
    # Resta
    iAssis = int(statsPlayers[game][10][iPlayer])
    avStats[indPl][17][0] = int(avStats[indPl][17][0]) + iAssis
    # Rec
    iRec = int(statsPlayers[game][11][iPlayer])
    avStats[indPl][18][0] = int(avStats[indPl][18][0]) + iRec
    # Per
    avStats[indPl][19][0] = int(avStats[indPl][19][0]) + int(statsPlayers[game][12][iPlayer])
    # Tap Fav
    iTapF = int(statsPlayers[game][13][iPlayer])
    avStats[indPl][20][0] = int(avStats[indPl][20][0]) + iTapF
    # Tap Contra
    avStats[indPl][21][0] = int(avStats[indPl][21][0]) + int(statsPlayers[game][14][iPlayer])
    # Mates
    avStats[indPl][22][0] = int(avStats[indPl][22][0]) + int(statsPlayers[game][15][iPlayer])
    # FCom
    avStats[indPl][23][0] = int(avStats[indPl][23][0]) + int(statsPlayers[game][16][iPlayer])
    # FSof
    avStats[indPl][24][0] = int(avStats[indPl][24][0]) + int(statsPlayers[game][17][iPlayer])
    # Val
    avStats[indPl][25][0] = int(avStats[indPl][25][0]) + int(statsPlayers[game][18][iPlayer])
    avStats[indPl][1][0] = sType

def computeAdvStatsTeam(teamStats, oppFGA, oppPer, oppFTa, oppORB, teamFGa, teamPer, teamFTa, teamORB, teamPts, teamFGm, team3Pm, teamFTm, teamDRB, oppDRB, teamAssis):
    oppPos = int(0.96 * (oppFGA + oppPer + 0.44 * oppFTa - oppORB))
    teamPoss = int(0.96 * (teamFGa + teamPer + 0.44 * teamFTa - teamORB))
    try:
        teamPace = float(teamPoss) / float(teamPoss+oppPos)
    except:
        pass
    try:
        teamOER = float(100 * teamPts) / float(teamPoss)
    except:
        pass
    teamEffPer = 100 * ((teamFGm + 0.5 * team3Pm) / float(teamFGa))
    try:
        teamScoringP = float(teamFGm + (1 - (1 - (teamFTm / teamFTa)) ** 2) * teamFTa * 0.4)
    except:
        pass
    teamPlayPer = 100 * (float(teamScoringP) / float(teamFGa + teamFTa * 0.4 + teamPer))
    teamt1R = 100 * (float(teamFTm) / float(teamFGa))
    teamDefRebR = 100 * (teamDRB / (teamDRB + oppORB))
    teamOfRebR = 100 * (teamORB / (teamORB + oppDRB))
    teamAssisR = 100 * (teamAssis / (teamFGa + 0.44 * teamFTa + teamAssis + teamPer))
    teamPerR = 100 * (teamPer) / (teamFGa+teamFTa*0.44+teamPer)

    teamStats[0][26][0] = teamPoss
    teamStats[0][27][0] = teamPace
    teamStats[0][28][0] = teamOER
    teamStats[0][29][0] = teamEffPer
    teamStats[0][30][0] = teamPlayPer
    teamStats[0][31][0] = teamt1R
    teamStats[0][32][0] = teamDefRebR
    teamStats[0][33][0] = teamOfRebR
    teamStats[0][34][0] = teamAssisR
    teamStats[0][35][0] = teamPerR

def computeAdvStats(statsPlayers, avStats, teamStats=None, teamStatsAg=None):
    teamMinsv = []
    teamFGmv = []
    teamFGav = []
    teamFTmv = []
    teamFTav = []
    team3Pmv = []
    teamAssisv = []
    teamPtsv = []
    teamORBv = []
    teamDRBv = []
    teamPerv = []
    teamTapv = []
    teamRecv = []
    teamFpv = []

    oppFGMv = []
    oppFGAv = []
    oppFTmv = []
    oppFTav = []
    oppPointsv = []
    oppORBv = []
    oppDRBv = []
    opp3PMv = []
    oppPerv = []
    oppFpv = []
    oppAssisv = []

    game = 0
    for gameAux in range(0, int(len(statsPlayers)/3)):
        teamMinsv.append(float(statsPlayers[game + 1][3][0].replace('\n', '').replace(':', '.')))
        teamPtsv.append(float(statsPlayers[game + 1][4][0]))
        teamFGmv.append(int(statsPlayers[game + 1][5][0].split("/")[0]) + int(statsPlayers[game + 1][6][0].split("/")[0]))
        teamFGav.append(int(statsPlayers[game + 1][5][0].split("/")[1].split(" ")[0]) + int(statsPlayers[game + 1][6][0].split("/")[1].split(" ")[0]))
        teamFTmv.append(int(statsPlayers[game + 1][7][0].split("/")[0]))
        teamFTav.append(int(statsPlayers[game + 1][7][0].split("/")[1].split(" ")[0]))
        team3Pmv.append(int(statsPlayers[game + 1][6][0].split("/")[0]))
        teamAssisv.append(int(statsPlayers[game + 1][10][0]))

        teamORBv.append(float(statsPlayers[game + 1][8][0]))
        teamDRBv.append(float(statsPlayers[game + 1][9][0]))
        teamRecv.append(float(statsPlayers[game + 1][11][0]))
        teamPerv.append(float(statsPlayers[game + 1][12][0]))
        teamTapv.append(float(statsPlayers[game + 1][13][0]))
        teamFpv.append(float(statsPlayers[game + 1][16][0]))

        oppFGMv.append(float(statsPlayers[game + 2][5][0].split("/")[0]) + int(statsPlayers[game + 2][6][0].split("/")[0]))
        oppFGAv.append(float(statsPlayers[game + 2][5][0].split("/")[1].split(" ")[0]) + int(statsPlayers[game + 2][6][0].split("/")[1].split(" ")[0]))
        oppFTmv.append(int(statsPlayers[game + 2][7][0].split("/")[0]))
        oppFTav.append(int(statsPlayers[game + 2][7][0].split("/")[1].split(" ")[0]))
        opp3PMv.append(int(statsPlayers[game + 2][6][0].split("/")[0]))
        oppPointsv.append(float(statsPlayers[game + 2][4][0]))
        oppAssisv.append(int(statsPlayers[game + 2][10][0]))
        oppORBv.append(float(statsPlayers[game + 2][8][0]))
        oppDRBv.append(float(statsPlayers[game + 2][9][0]))
        oppPerv.append(float(statsPlayers[game + 2][12][0]))
        oppFpv.append(float(statsPlayers[game + 2][16][0]))

        game = game+3

    if teamStats != None:
        teamPts = float(np.sum(np.array(teamPtsv)))
        teamFGm = float(np.sum(np.array(teamFGmv)))
        teamFGa = float(np.sum(np.array(teamFGav)))
        teamFTm = float(np.sum(np.array(teamFTmv)))
        teamFTa = float(np.sum(np.array(teamFTav)))
        team3Pm = float(np.sum(np.array(team3Pmv)))
        teamAssis = float(np.sum(np.array(teamAssisv)))
        teamORB = float(np.sum(np.array(teamORBv)))
        teamDRB = float(np.sum(np.array(teamDRBv)))
        teamPer = float(np.sum(np.array(teamPerv)))

        oppFGM = float(np.sum(np.array(oppFGMv)))
        oppFGA = float(np.sum(np.array(oppFGAv)))
        oppFTm = float(np.sum(np.array(oppFTmv)))
        oppFTa = float(np.sum(np.array(oppFTav)))
        oppPts = float(np.sum(np.array(oppPointsv)))
        oppORB = float(np.sum(np.array(oppORBv)))
        oppDRB = float(np.sum(np.array(oppDRBv)))
        oppPer = float(np.sum(np.array(oppPerv)))
        opp3PM = float(np.sum(np.array(opp3PMv)))
        oppAssis = float(np.sum(np.array(oppAssisv)))

        computeAdvStatsTeam(teamStats, oppFGA, oppPer, oppFTa, oppORB, teamFGa, teamPer, teamFTa, teamORB, teamPts, teamFGm, team3Pm, teamFTm, teamDRB, oppDRB, teamAssis)
        computeAdvStatsTeam(teamStatsAg, teamFGa, teamPer, teamFTa, teamORB, oppFGA, oppPer, oppFTa, oppORB, oppPts, oppFGM, opp3PM, oppFTm, oppDRB, teamDRB, oppAssis)


    for indPl in range(0, len(avStats)):
        if indPl == 5:
            a = 1
        name = avStats[indPl][0]
        bPlayed = []
        game = 0
        for gameAux in range(0, int(len(statsPlayers)/3)):
            namesGame = statsPlayers[game][0]
            if platform.system() == 'Linux' or platform.system() == 'Darwin':
                namesGame = ['\n' +  str(x.encode('ascii', errors='ignore'))[4:-3] +'\n' for x in namesGame]
                if '\n' + str(name[0])[4:-3] + '\n' in namesGame:
                    bPlayed.append(gameAux)
            else:
                namesGame = ['\n' +  str(x.encode('ascii', errors='ignore')) +'\n' for x in namesGame]
                if '\n' + str(name[0]) + '\n' in namesGame:
                    bPlayed.append(gameAux)

            game = game + 3
        if bPlayed != []:
            timePlayed = divmod(avStats[indPl][3][0], 60)
            iMins = float(str(timePlayed[0]) + '.' + str(float(timePlayed[1])/float(60))[2:])
            iPts = float(avStats[indPl][4][0])
            it2M = float(avStats[indPl][5][0])
            it2A = float(avStats[indPl][6][0])
            it3M = float(avStats[indPl][8][0])
            it3A = float(avStats[indPl][9][0])
            it1M = float(avStats[indPl][11][0])
            it1A = float(avStats[indPl][12][0])
            indFGm = it2M + it3M
            indFGa = it2A + it3A
            iOfReb = float(avStats[indPl][14][0])
            iDefReb = float(avStats[indPl][15][0])
            iAssis = float(avStats[indPl][17][0])
            iRec = float(avStats[indPl][18][0])
            iPer = float(avStats[indPl][19][0])
            iTapF = float(avStats[indPl][20][0])
            iFal = float(avStats[indPl][23][0])

            teamMins = float(np.sum(np.array(teamMinsv)[bPlayed]))
            teamPts = float(np.sum(np.array(teamPtsv)[bPlayed]))
            teamFGm = float(np.sum(np.array(teamFGmv)[bPlayed]))
            teamFGa = float(np.sum(np.array(teamFGav)[bPlayed]))
            teamFTm = float(np.sum(np.array(teamFTmv)[bPlayed]))
            teamFTa = float(np.sum(np.array(teamFTav)[bPlayed]))
            team3Pm = float(np.sum(np.array(team3Pmv)[bPlayed]))
            teamAssis = float(np.sum(np.array(teamAssisv)[bPlayed]))
            teamORB = float(np.sum(np.array(teamORBv)[bPlayed]))
            teamDRB = float(np.sum(np.array(teamDRBv)[bPlayed]))
            teamRec = float(np.sum(np.array(teamRecv)[bPlayed]))
            teamPer = float(np.sum(np.array(teamPerv)[bPlayed]))
            teamTap = float(np.sum(np.array(teamTapv)[bPlayed]))
            teamFp = float(np.sum(np.array(teamFpv)[bPlayed]))

            oppFGM = float(np.sum(np.array(oppFGMv)[bPlayed]))
            oppFGA = float(np.sum(np.array(oppFGAv)[bPlayed]))
            oppFTm = float(np.sum(np.array(oppFTmv)[bPlayed]))
            oppFTa = float(np.sum(np.array(oppFTav)[bPlayed]))
            oppPoints = float(np.sum(np.array(oppPointsv)[bPlayed]))
            oppORB = float(np.sum(np.array(oppORBv)[bPlayed]))
            oppDRB = float(np.sum(np.array(oppDRBv)[bPlayed]))
            oppPer = float(np.sum(np.array(oppPerv)[bPlayed]))
            oppFp = float(np.sum(np.array(oppFpv)[bPlayed]))

            try:
                teamScoringP = float(teamFGm + (1 - (1 - (teamFTm / teamFTa)) ** 2) * teamFTa * 0.4)
            except:
                pass
            teamPlayp = float(teamScoringP) / float(teamFGa + teamFTa * 0.4 + teamPer)
            teamORBp = float(teamORB) / float(teamORB + oppDRB)
            teamORBw = float((1 - teamORBp) * teamPlayp) / float((1 - teamORBp) * teamPlayp + teamORBp * (1 - teamPlayp))
            teamStats = (teamFGa + 0.4*teamFTa - 1.07 * (teamORB/(teamORB+oppDRB)) * (teamFGa-teamFGm) + teamPer)
            oppStats = (oppFGA + 0.4*oppFTa - 1.07 * (oppORB/(oppORB+teamDRB)) * (oppFGA-oppFGM) + oppPer)
            teamPoss = 0.5*(teamStats+oppStats)
            oppPos = teamPoss

            try:
                avStats[indPl][26][0] = (100*float(iAssis)/(((float(iMins)/(float(teamMins)/float(5)))*teamFGm)-indFGm))
            except:
                pass

            # eFG
            if indFGa != 0:
                avStats[indPl][27][0] = (float(indFGm+0.5*(int(it3M)))/float(indFGa))
            else:
                avStats[indPl][27][0] = 0

            # TS
            if float(2*(float(indFGa)+0.44*float(it1A))) != 0:
                avStats[indPl][28][0] = float(iPts)/float(2*(float(indFGa)+0.44*float(it1A)))
            else:
                avStats[indPl][28][0] = 0

            # Gscore
            avStats[indPl][29][0] = float(iPts)+0.4*float(indFGm)+0.7*float(iOfReb)+0.3*float(iDefReb)+float(iRec)+0.7*float(iAssis)+0.7*float(iTapF)-0.7*float(indFGa)-0.4*float(it1A-it1M)-0.4*float(iFal)-float(iPer)

            # qAst = ((float(iMins)/float(teamMins/5)) * (1.14 * (float(teamAssis-iAssis)/float(teamFGm)))) + ((((teamAssis / teamMins) * iMins * 5 - iAssis) / ((teamFGm / teamMins) * iMins * 5 - indFGm)) * (1 - (iMins / (teamMins / 5))))
            qAst = ((float(iMins)/float(teamMins/5)) * (float(teamAssis-iAssis)/float(teamFGm-indFGm))) + ((((teamAssis / teamMins) * iMins * 5 - iAssis) / ((teamFGm / teamMins) * iMins * 5 - indFGm)) * (1 - (iMins / (teamMins / 5))))
            try:
                FG_Part = indFGm * (1 - 0.5 * ((iPts - it1M) / (2 * indFGa)) * qAst)
            except:
                FG_Part = 0

            AST_Part = 0.5 * (((teamPts - teamFTm) - (iPts - it1M)) / (2 * (teamFGa - indFGa))) * iAssis
            try:
                FT_Part = (1 - (1 - (it1M / it1A)) ** 2) * 0.4 * it1A
            except:
                FT_Part = 0

            ORB_Part = iOfReb * teamORBw * teamPlayp
            scPoss = (FG_Part + AST_Part + FT_Part) * (1 - (teamORB / teamScoringP) * teamORBw * teamPlayp) + ORB_Part

            FGxPoss = (indFGa - indFGm) * (1 - 1.07 * teamORBp)
            try:
                FTxPoss = ((1 - (it1M /it1A)) ** 2) * 0.4 * it1A
            except:
                FTxPoss = 0

            nscPoss = FGxPoss + FTxPoss + iPer

            # Scored Poss
            avStats[indPl][30][0] = scPoss

            # Non Scored Poss
            avStats[indPl][31][0] = nscPoss

            # Tot Poss
            avStats[indPl][32][0] = int(scPoss+nscPoss)

            # Floor Percentage
            try:
                avStats[indPl][33][0] = avStats[indPl][33][0] + (float(100)*(float(scPoss)/float(nscPoss+scPoss)))
            except:
                pass

            # Points per Shot
            if float(it2A+it3A) != 0:
                fPointspshot = float(2*it2M+3*it3M)/float(it2A+it3A)
                avStats[indPl][34][0] = fPointspshot

            # % Reb
            teamAgRebs = oppDRB+oppORB
            teamRebs = teamDRB+teamORB
            fPerReb = 100*float((iOfReb+iDefReb)*(float(teamMins)/float(5)))/float(float(iMins)*(teamRebs+teamAgRebs))
            fPerDefReb = 100 * (float(iDefReb * float(teamMins) / float(5)) / float(float(iMins) * (teamDRB + oppORB)))
            fPerOfReb = 100 * (float(iOfReb * float(teamMins) / float(5)) / float(float(iMins) * (teamORB + oppDRB)))
            avStats[indPl][35][0] = fPerReb
            avStats[indPl][36][0] = fPerDefReb
            avStats[indPl][37][0] = fPerOfReb

            # % Steals
            fStPer = float(100)*(float(float(iRec)*(float(teamMins)/float(5)))/float(iMins*oppPos))
            avStats[indPl][38][0] = fStPer

            # Touches
            fTouches = indFGa + iPer + (iAssis/float(0.17)) + (it1A / (teamFTa / oppFp))
            avStats[indPl][39][0] = + fTouches

            fUsage1 = (float(indFGa)+0.44*it1A+iPer)*float(teamMins)
            fUsage2 = (float(teamFGm) + 0.44*teamFTa + teamPer) * float(5) * float(iMins)

            if fUsage2 != 0:
                fUsage = 100*(fUsage1)/(fUsage2)
                avStats[indPl][40][0] = fUsage

            # Versatility
            avStats[indPl][41][0] = (iPts*float(iOfReb+iDefReb)*iAssis)**(0.333)

            # Win Scores
            fWinScore = iPts + iDefReb + iOfReb + iRec + 0.5*iAssis + 0.5*iTapF - indFGa - iPer - 0.5*it1A - 0.5*iFal
            avStats[indPl][42][0] = fWinScore

            try:
                pPointsProd_FG_Part = 2*(indFGm + 0.5*it3M) * (1 - 0.5*(float(iPts-it1M)/float(2*indFGa)) * qAst)
            except:
                pPointsProd_FG_Part = 0
            pPointsProd_AST_Part = 2 * ((teamFGm - indFGm + 0.5 * (team3Pm - it3M)) / (teamFGm - indFGm)) * 0.5 * (((teamPts - teamFTm) - (iPts - it1M)) / (2 * (teamFGa - indFGa))) * iAssis
            pPointsProd_ORB_Part = iOfReb * teamORBw * teamPlayp * (teamPts / (teamFGm + (1 - (1 - (teamFTm / teamFTa))** 2) *0.4 * teamFTa))

            pProd = (pPointsProd_FG_Part + pPointsProd_AST_Part + it1M) * (1 - (teamORB / teamScoringP) * teamORBw * teamPlayp) + pPointsProd_ORB_Part
            try:
                OERi = 100*(float(pProd)/float(int(scPoss)+int(nscPoss)))
            except:
                OERi = 100*(float(teamPts) / float(teamPoss))

            if OERi < 1:
                OERi = 100*(float(teamPts) / float(teamPoss))

            DFGp = oppFGM / oppFGA
            DORp = float(oppORB) / (float(oppORB) + float(teamDRB))
            FMwt = (DFGp * (1 - DORp)) / (DFGp * (1 - DORp) + (1 - DFGp) * DORp)
            Stops1 = iRec + iTapF * FMwt * (1 - 1.07 * DORp) + iDefReb * (1 - FMwt)
            Stops2 = (((oppFGA - oppFGM - teamTap) / teamMins) * FMwt * (1 - 1.07 * DORp) + ((oppPer - teamRec) / teamMins)) * iMins + (iFal / teamFp) * 0.4 * oppFTa * ((1 - (oppFTm / oppFTa))**2)
            Stops = Stops1 + Stops2
            Stopp = (Stops * teamMins) / (teamPoss * iMins)
            DERating = 100 * (oppPoints / teamPoss)
            DpScore = oppPoints / (oppFGM + (1 - (1 - (oppFTm / oppFTa)) ** 2) * oppFTa * 0.4)
            DERi = DERating + 0.2 * (100 * DpScore * (1 - Stopp) - DERating)

            avStats[indPl][43][0] = OERi
            avStats[indPl][44][0] = DERi
            lNeti = float(OERi - DERi)
            avStats[indPl][45][0] = lNeti


def parse_stats_scratch_team(statsPlayers, game, indPl, sType, bAgainst):
    lNames = []
    lNames.append(statsPlayers[game][0][indPl].encode('ascii', errors='ignore'))
    lTypes = []
    lTypes.append(sType)
    lGames = []
    lGames.append(int(1))
    lMins = []
    lMins.append(int(time2secs(statsPlayers[game][3][indPl])))
    lPts = []
    lPts.append(int(statsPlayers[game][4][indPl]))
    lt2S = []
    lt2S.append(int(statsPlayers[game][5][indPl].split("/")[0]))
    lt2A = []
    lt2A.append(int(statsPlayers[game][5][indPl].split("/")[1].split(" ")[0]))
    lt2p = []
    lt2p.append(int(statsPlayers[game][5][indPl].split("/")[1].split(" ")[1].split("%")[0]))
    lt3S = []
    lt3S.append(int(statsPlayers[game][6][indPl].split("/")[0]))
    lt3A = []
    lt3A.append(int(statsPlayers[game][6][indPl].split("/")[1].split(" ")[0]))
    lt3p = []
    lt3p.append(int(statsPlayers[game][6][indPl].split("/")[1].split(" ")[1].split("%")[0]))
    lt1S = []
    lt1S.append(int(statsPlayers[game][7][indPl].split("/")[0]))
    lt1A = []
    lt1A.append(int(statsPlayers[game][7][indPl].split("/")[1].split(" ")[0]))
    lt1p = []
    lt1p.append(int(statsPlayers[game][7][indPl].split("/")[1].split(" ")[1].split("%")[0]))
    lrOf = []
    lrOf.append(int(statsPlayers[game][8][indPl]))
    lrDef = []
    lrDef.append(int(statsPlayers[game][9][indPl]))
    lrReb = []
    lrReb.append(int(statsPlayers[game][8][indPl]) + int(statsPlayers[game][9][indPl]))
    lAssis = []
    lAssis.append(int(statsPlayers[game][10][indPl]))
    lRec = []
    lRec.append(int(statsPlayers[game][11][indPl]))
    lPer = []
    lPer.append(int(statsPlayers[game][12][indPl]))
    lTapF = []
    lTapF.append(int(statsPlayers[game][13][indPl]))
    lTapC = []
    lTapC.append(int(statsPlayers[game][14][indPl]))
    lMat = []
    lMat.append(int(statsPlayers[game][15][indPl]))
    lFalC = []
    lFalC.append(int(statsPlayers[game][16][indPl]))
    lFalF = []
    lFalF.append(int(statsPlayers[game][17][indPl]))
    lVal = []
    lVal.append(int(statsPlayers[game][18][indPl]))
    lPoss = []
    lPoss.append(0)
    lPace = []
    lPace.append(0)
    lOER = []
    lOER.append(0)
    lEffPer = []
    lEffPer.append(0)
    lPlayPer = []
    lPlayPer.append(0)
    lt1R =[]
    lt1R.append(0)
    lOfRebR = []
    lOfRebR.append(0)
    lDefRebR = []
    lDefRebR.append(0)
    lAssR = []
    lAssR.append(0)
    lPerR = []
    lPerR.append(0)

    return [lNames, lTypes, lGames, lMins, lPts, lt2S, lt2A, lt2p, lt3S, lt3A, lt3p, lt1S, lt1A, lt1p, lrOf, lrDef,  lrReb, lAssis, lRec, lPer, lTapF, lTapC, lMat, lFalC, lFalF, lVal, lPoss, lPace, lOER, lEffPer, lPlayPer, lt1R, lDefRebR, lOfRebR, lAssR, lPerR]


def parse_stats_existing_team(statsPlayers, game, indPl, avStats, iPlayer, sType, bAgainst):
    # N Games
    avStats[indPl][2][0] = (int(avStats[indPl][2][0]) + 1)
    # Minutes
    try:
        avStats[indPl][3][0] = avStats[indPl][3][0] + time2secs(statsPlayers[game][3][iPlayer])
    except:
        pass
    # Points
    avStats[indPl][4][0] = int(avStats[indPl][4][0]) + int(statsPlayers[game][4][iPlayer])
    # lt2
    t2SAux = int(statsPlayers[game][5][iPlayer].split("/")[0])
    t2AAux = int(statsPlayers[game][5][iPlayer].split("/")[1].split(" ")[0])
    avStats[indPl][5][0] = int(avStats[indPl][5][0]) + t2SAux
    avStats[indPl][6][0] = int(avStats[indPl][6][0]) + t2AAux
    try:
        avStats[indPl][7][0] = float(avStats[indPl][5][0]) / float(avStats[indPl][6][0])
    except:
        avStats[indPl][7][0] = 0
    # lt3
    t3SAux = int(statsPlayers[game][6][iPlayer].split("/")[0])
    t3AAux = int(statsPlayers[game][6][iPlayer].split("/")[1].split(" ")[0])
    avStats[indPl][8][0] = int(avStats[indPl][8][0]) + t3SAux
    avStats[indPl][9][0] = int(avStats[indPl][9][0]) + t3AAux
    try:
        avStats[indPl][10][0] = float(avStats[indPl][8][0]) / float(avStats[indPl][9][0])
    except:
        avStats[indPl][10][0] = 0
    # lt1
    t1SAux = int(statsPlayers[game][7][iPlayer].split("/")[0])
    t1AAux = int(statsPlayers[game][7][iPlayer].split("/")[1].split(" ")[0])
    avStats[indPl][11][0] = int(avStats[indPl][11][0]) + t1SAux
    avStats[indPl][12][0] = int(avStats[indPl][12][0]) + t1AAux
    try:
        avStats[indPl][13][0] = float(avStats[indPl][11][0]) / float(avStats[indPl][12][0])
    except:
        avStats[indPl][13][0] = 0

    # Rebs
    rofAux = int(statsPlayers[game][8][iPlayer])
    rdefAux = int(statsPlayers[game][9][iPlayer])
    avStats[indPl][14][0] = int(avStats[indPl][14][0]) + rofAux
    avStats[indPl][15][0] = int(avStats[indPl][15][0]) + rdefAux
    avStats[indPl][16][0] = int(avStats[indPl][16][0]) + rofAux + rdefAux

    assisAux = int(statsPlayers[game][10][iPlayer])
    avStats[indPl][17][0] = int(avStats[indPl][17][0]) + assisAux
    recAux = int(statsPlayers[game][11][iPlayer])
    avStats[indPl][18][0] = int(avStats[indPl][18][0]) + recAux
    perAux = int(statsPlayers[game][12][iPlayer])
    avStats[indPl][19][0] = int(avStats[indPl][19][0]) + perAux
    tapAux = int(statsPlayers[game][13][iPlayer])
    avStats[indPl][20][0] = int(avStats[indPl][20][0]) + tapAux
    tapRAux = int(statsPlayers[game][14][iPlayer])
    avStats[indPl][21][0] = int(avStats[indPl][21][0]) + tapRAux
    matAux = int(statsPlayers[game][15][iPlayer])
    avStats[indPl][22][0] = int(avStats[indPl][22][0]) + matAux
    fcomAux = int(statsPlayers[game][16][iPlayer])
    avStats[indPl][23][0] = int(avStats[indPl][23][0]) + fcomAux
    frebAux = int(statsPlayers[game][17][iPlayer])
    avStats[indPl][24][0] = int(avStats[indPl][24][0]) + frebAux
    valAux = int(statsPlayers[game][18][iPlayer])
    avStats[indPl][25][0] = int(avStats[indPl][25][0]) + valAux
    avStats[indPl][1][0] = sType

def tot2Av(avStats, indPl):
    games = avStats[indPl][2][0]

    if len(avStats[0]) > 36:
        lP = [7, 10, 13, 26, 27, 28, 33, 34, 35, 36, 37, 38, 40, 43, 44, 45]
        avStats[indPl][3][0] = "%.2f" % round((float(avStats[indPl][3][0]/60)/float(games)),2)

        for iStat in range(4, 46):
            if iStat not in lP:
                try:
                    avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0])/float(games)),2)
                except:
                    pass
    else:
        lP = [7, 10, 13]
        avStats[indPl][3][0] = "%.2f" % round((float(avStats[indPl][3][0] / 60) / float(games)), 2)
        for iStat in range(4, 27):
            if iStat not in lP:
                try:
                    avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0]) / float(games)), 2)
                except:
                    pass

    return avStats

def tot2Proj(avStats, indPl, mins):
    fFac = float(40)/float(mins)
    lP = [7, 10, 13]

    for iStat in range(4, 46):
        if iStat not in lP:
            try:
                avStats[indPl][iStat][0] = "%.2f" % round((float(avStats[indPl][iStat][0])*fFac),2)
            except:
                pass

    return avStats

def parseGameData(iGame, players, stats, sType, statsPlayers, bTeam):
    try:
        game = statsPlayers[iGame]
    except:
        pass

    if bTeam == False:
        try:
            playersGame = game[0]
            for iPlayer in range(0, len(playersGame)):
                if playersGame[iPlayer] not in players:
                    players.append(playersGame[iPlayer])
                    stats.append(parse_stats_scratch_player(statsPlayers, iGame, iPlayer, sType))
                else:
                    index = players.index(playersGame[iPlayer])
                    parse_stats_existing_player(statsPlayers, iGame, index, stats, iPlayer, sType)
        except:
            pass
    else:
        try:
            playersGame = game[0]
            if playersGame[0][-4:] == 'inst' or playersGame[0][-4:] == 'ival':
                bAgainst = False
            else:
                bAgainst = True
            for iPlayer in range(0, len(playersGame)):
                if playersGame[iPlayer] not in players:
                    players.append(playersGame[iPlayer])
                    stats.append(parse_stats_scratch_team(statsPlayers, iGame, iPlayer, sType, bAgainst))
                else:
                    index = players.index(playersGame[iPlayer])
                    parse_stats_existing_team(statsPlayers, iGame, index, stats, iPlayer, sType, bAgainst)
        except:
            pass

def parseGameDataTit(iGame, playersTit, titStats, playersBench, benchStats, stats, statsPlayers, sLang):
    game = statsPlayers[iGame]
    playersGame = game[0]
    titStatsAux = []
    benchStatsAux = []

    if sLang == 'Castellano':
        sRow = '4 Titular'
        sRow2 = '4 Banquillo'
    else:
        sRow = '4 Initial5'
        sRow2 = '4 Bench'

    for iPlayer in range(0, len(playersGame)):
        if stats[iGame][2][iPlayer] == True:
            titStatsAux.append(list(np.array(stats[iGame])[:,iPlayer]))
            if playersGame[iPlayer] not in playersTit:
                playersTit.append(playersGame[iPlayer])
                titStats.append(parse_stats_scratch_player(statsPlayers, iGame, iPlayer, sRow))
            else:
                index = playersTit.index(playersGame[iPlayer])
                parse_stats_existing_player(statsPlayers, iGame, index, titStats, iPlayer, sRow)
        else:
            benchStatsAux.append(list(np.array(stats[iGame])[:,iPlayer]))
            if playersGame[iPlayer] not in playersBench:
                playersBench.append(playersGame[iPlayer])
                benchStats.append(parse_stats_scratch_player(statsPlayers, iGame, iPlayer, sRow2))
            else:
                index = playersBench.index(playersGame[iPlayer])
                parse_stats_existing_player(statsPlayers, iGame, index, benchStats, iPlayer, sRow2)
    titStatsAux = list(np.transpose(np.array(titStatsAux)))
    benchStatsAux = list(np.transpose(np.array(benchStatsAux)))
    return [l.tolist() for l in titStatsAux],[l.tolist() for l in benchStatsAux]

def tryAppend(mat, iPlayer):
    try:
        tot2Av(mat, iPlayer)
    except:
        pass

def tryAppendProj(mat, iPlayer):
    try:
        mins = float(mat[iPlayer][3][0])
        tot2Proj(mat, iPlayer, mins)
    except:
        pass

def substBrackets(df, tag):
    df[tag] = df[tag].str.get(0).astype(float)

def get5FasesStats(sLang, statsPlayers, season, jorFirst, jorLast, sDir, iFase, targetTeam, sFase, bTeam, bProj, sLocal=None, sAway=None, sWin=None, sDif=None):

    if iFase != 1:
        iTotFases = int(np.ceil(float(len(statsPlayers)/3) / float(iFase))) # int(float(jorLast-jorFirst)/float(iFase))+1
    else:
        iTotFases = int(float(len(statsPlayers)/3)) # int(float(jorLast - jorFirst) / float(iFase))

    iTotLast = jorLast-iFase*iTotFases

    strPlayersTot = []
    avStatsTot = []
    strPlayersTotT = []
    avStatsTotT = []
    strPlayersTotAg = []
    avStatsTotAg = []

    if sLang == 'Castellano':
        if iFase == 1:
            sJor = 'Jornada '
            sSave = 'Jornadas'
        else:
            sJor = 'Fase '
            sSave = 'Fases'
    else:
        if iFase == 1:
            sJor = 'Round '
            sSave = 'Rounds'
        else:
            sJor = 'Phase '
            sSave = 'Phases'

    if sLocal != None:
        bAddition = True
    else:
        bAddition = False

    statsPlayersAux = []
    for indFase in range(0,iTotFases):
        strPlayers = []
        avStats = []
        strPlayersT = []
        avStatsT = []
        strPlayersAg = []
        avStatsAg = []
        if indFase == iTotFases:
            nGames = (indFase)*iFase+iTotLast
        else:
            nGames = (indFase+1)*iFase

        iFirstGame = max(0, (indFase) * iFase)
        if indFase != (iTotFases-1):
            iLastGame = (indFase+1)*iFase
        else:
            iLastGame = ((indFase+1) * iFase)+iTotLast

        statsPlayersAux.append(statsPlayers[iFirstGame*3:iLastGame*3])
        bTitp = []
        for iGame in range((indFase)*iFase,nGames):
            iGame = iGame * 3
            parseGameData(iGame, strPlayers, avStats, sJor + str(indFase+1).zfill(2), statsPlayers, False)
            if bAddition:
                try:
                    bTitp.append(statsPlayers[iGame][2])
                except:
                    pass
            iGame = iGame + 1
            parseGameData(iGame, strPlayersT, avStatsT, sJor + str(indFase+1).zfill(2), statsPlayers, True)
            iGame = iGame + 1
            parseGameData(iGame, strPlayersAg, avStatsAg, sJor + str(indFase+1).zfill(2), statsPlayers, True)

        strPlayersTot.append(strPlayers)
        avStatsTot.append(avStats)
        strPlayersTotT.append(strPlayersT)
        avStatsTotT.append(avStatsT)
        strPlayersTotAg.append(strPlayersAg)
        avStatsTotAg.append(avStatsAg)

        if sLocal != None:
            avStatsTotT[indFase][0].append(sLocal[indFase])
            avStatsTotT[indFase][0].append(sAway[indFase])
            avStatsTotT[indFase][0].append(sWin[indFase])
            avStatsTotT[indFase][0].append(sDif[indFase])
            for iPlayer in range(0, len(avStatsTot[indFase])):
                avStatsTot[indFase][iPlayer].append(sLocal[indFase])
                avStatsTot[indFase][iPlayer].append(sAway[indFase])
                avStatsTot[indFase][iPlayer].append(sWin[indFase])
                avStatsTot[indFase][iPlayer].append(sDif[indFase])
                avStatsTot[indFase][iPlayer].append(bTitp[0][iPlayer])

    for indFase in range(0, iTotFases):
        computeAdvStats(statsPlayersAux[indFase], avStatsTot[indFase], avStatsTotT[indFase], avStatsTotAg[indFase])

    flat_avStatsTot = [item for sublist in avStatsTot for item in sublist]
    for iPlayer in range(0, len(flat_avStatsTot)):
        tryAppend(flat_avStatsTot, iPlayer)

    flat_avStatsTotT = [item for sublist in avStatsTotT for item in sublist]
    for iPlayer in range(0, len(flat_avStatsTotT)):
        tryAppend(flat_avStatsTotT, iPlayer)

    flat_avStatsTotAg = [item for sublist in avStatsTotAg for item in sublist]
    for iPlayer in range(0, len(flat_avStatsTotAg)):
        tryAppend(flat_avStatsTotAg, iPlayer)

    stats2csvFase(flat_avStatsTot, sDir + '/p'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + sSave + '.csv', bAddition, sLang)
    if bTeam:
        stats2csvFaseTeam(flat_avStatsTotT, flat_avStatsTotAg, sDir + '/t'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + sSave + '.csv', bAddition, sLang)

    if bProj == True:
        for iPlayer in range(0, len(flat_avStatsTot)):
            tryAppendProj(flat_avStatsTot, iPlayer)
        stats2csvFase(flat_avStatsTot, sDir + '/p' + targetTeam + season + 'J' + str(jorFirst) + 'J' + str(jorLast) + sFase + 'PeriodosProj.csv', bAddition)


def stats2csvFase(avStats,csvFile, bAddition, sLang):

    if sLang == 'Castellano':
        headers = ['Nombre', 'Jornada', 'Partidos', 'Minutos', 'Puntos', 'T2 Anotados', 'T2 Lanzados', '% T2', 'T3 Anotados', 'T3 Lanzados', '% T3', 'T1 Anotados', 'T1 Lanzados', '% T1', 'Reb. Ofensivos', 'Reb. Defensivos', 'Rebotes', 'Asistencias', 'Robos', 'Perdidas', 'Tapones', 'Tapones Recibidos', 'Mates', 'Faltas Cometidas', 'Faltas Recibidas', 'Valoracion', '% Asist', '% Tiro Efectivo', '% Tiro Verdadero', 'GScore', 'Posesiones Anotadas', 'Posesiones No Anotadas', 'Tot Posesiones', 'Floor Percentage', 'Puntos por Tiro', '% Rebotes', '% Rebotes Def', '% Rebotes Of', '% Robos', 'Toques', 'Uso', 'Versatilidad', 'Win Scores', 'Eficiencia Ofensiva', 'Eficiencia Defensiva', 'Diferencia eficiencia', 'Local', 'Visitante','Victoria','Diferencia','Titular']
    else:
        headers = ['Name', 'Round', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR', 'AST%', 'eFG%', 'TS%', 'GScore', 'Scored Poss.', 'Non-scored Poss.', 'Tot Poss.', 'Floor Percentage', 'PPS', 'TRB%', 'DRB%', 'ORB%', 'STL%', 'Touches', 'Usage', 'Versatility', 'Win Scores', 'OER', 'DER', 'Net','Local', 'Away','Win','Difference','Initial 5']

    if bAddition == False:
        headers = headers[:-5]

    if sLang == 'Castellano':
        sCon1 = 'Nombre'
        sCon2 = 'Jornada'
    else:
        sCon1 = 'Name'
        sCon2 = 'Round'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]

    if bAddition:
        iFac = 5
    else:
        iFac = 0
    for iStat in range(2, int(len(headers) - iFac)):
        substBrackets(df, headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def stats2csvTeam(avStats,last3Stats,homeStats,awayStats,winStats,lostStats,easyStats,toughStats,target1Stats,target2Stats,avStatsAg, last3StatsAg, homeStatsAg, awayStatsAg, winStatsAg, lostStatsAg, easyStatsAg, toughStatsAg, target1StatsAg, target2StatsAg,csvFile,sLang):
    if last3Stats != []:
        avStats.extend(last3Stats)
    if homeStats != []:
        avStats.extend(homeStats)
    if awayStats != []:
        avStats.extend(awayStats)
    if winStats != []:
        avStats.extend(winStats)
    if lostStats != []:
        avStats.extend(lostStats)
    if easyStats != []:
        avStats.extend(easyStats)
    if toughStats != []:
        avStats.extend(toughStats)
    if target1Stats != []:
        avStats.extend(target1Stats)
    if target2Stats != []:
        avStats.extend(target2Stats)
    if avStatsAg != []:
        avStats.extend(avStatsAg)
    if last3StatsAg != []:
        avStats.extend(last3StatsAg)
    if homeStatsAg != []:
        avStats.extend(homeStatsAg)
    if awayStatsAg != []:
        avStats.extend(awayStatsAg)
    if winStatsAg != []:
        avStats.extend(winStatsAg)
    if lostStatsAg != []:
        avStats.extend(lostStatsAg)
    if easyStatsAg != []:
        avStats.extend(easyStatsAg)
    if toughStatsAg != []:
        avStats.extend(toughStatsAg)
    if target1StatsAg != []:
        avStats.extend(target1StatsAg)
    if target2StatsAg != []:
        avStats.extend(target2StatsAg)

    if sLang == 'Castellano':
        headers = ['Nombre', 'Condicion', 'Partidos', 'Minutos', 'Puntos', 'T2 Anotados', 'T2 Lanzados', '% T2', 'T3 Anotados', 'T3 Lanzados', '% T3', 'T1 Anotados', 'T1 Lanzados', '% T1', 'Reb. Ofensivos', 'Reb. Defensivos', 'Rebotes', 'Asistencias', 'Robos', 'Perdidas', 'Tapones', 'Tapones Recibidos', 'Mates', 'Faltas Cometidas', 'Faltas Recibidas', 'Valoracion', 'Posesiones', 'Ritmo', 'OER', '% TC Efectivo', '% Jugada', 'Frec. TL', '% Reb Def', '% Reb Of', '% Assis', '% Perd']
    else:
        headers = ['Name', 'Condition', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR',  'Possessions', 'Pace', 'OER', 'eFG%', 'Play%', 'FTA Rate', 'DRB%', 'ORB%', 'Assist%', 'TOV%']

    if sLang == 'Castellano':
        sCon1 = 'Nombre'
        sCon2 = 'Condicion'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    for iStat in range(2,len(headers)):
        substBrackets(df,headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)


def stats2csvFaseTeam(avStatsT,avStatsAg,csvFile, bAddition, sLang):
    avStatsT.extend(avStatsAg)

    if sLang == 'Castellano':
        headers = ['Nombre', 'Condicion', 'Partidos', 'Minutos', 'Puntos', 'T2 Anotados', 'T2 Lanzados', '% T2', 'T3 Anotados', 'T3 Lanzados', '% T3', 'T1 Anotados', 'T1 Lanzados', '% T1', 'Reb. Ofensivos', 'Reb. Defensivos', 'Rebotes', 'Asistencias', 'Robos', 'Perdidas', 'Tapones', 'Tapones Recibidos', 'Mates', 'Faltas Cometidas', 'Faltas Recibidas', 'Valoracion', 'Posesiones', 'Ritmo', 'OER', '% TC Efectivo', '% Jugada', 'Frec. TL', '% Reb Def', '% Reb Of', '% Assis', '% Perd','Local', 'Visitante','Victoria','Diferencia']
    else:
        headers = ['Name', 'Condition', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR',  'Possessions', 'Pace', 'OER', 'eFG%', 'Play%', 'FTA Rate', 'DRB%', 'ORB%', 'Assist%', 'TOV%','Local', 'Away','Win','Difference']

    if bAddition == False:
        headers = headers[:-4]

    if sLang == 'Castellano':
        sCon1 = 'Nombre'
        sCon2 = 'Condicion'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStatsT, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    if bAddition:
        iFac = 4
    else:
        iFac = 0
    for iStat in range(2,int(len(headers)-iFac)):
        substBrackets(df,headers[iStat])


    df.sort_values([sCon2], inplace=True)
    df.to_csv(csvFile, index=False)

def stats2csv(avStats,last3Stats,homeStats,awayStats,titStats,benchStats,winStats,lostStats,easyStats,toughStats,target1Stats,target2Stats,csvFile,sLang):
    if last3Stats != []:
        avStats.extend(last3Stats)
    if homeStats != []:
        avStats.extend(homeStats)
    if awayStats != []:
        avStats.extend(awayStats)
    avStats.extend(titStats)
    avStats.extend(benchStats)
    if winStats != []:
        avStats.extend(winStats)
    if lostStats != []:
        avStats.extend(lostStats)
    if easyStats != []:
        avStats.extend(easyStats)
    if toughStats != []:
        avStats.extend(toughStats)
    if target1Stats != []:
        avStats.extend(target1Stats)
    if target2Stats != []:
        avStats.extend(target2Stats)
    if sLang == 'Castellano':
        headers = ['Nombre', 'Condicion', 'Partidos', 'Minutos', 'Puntos', 'T2 Anotados', 'T2 Lanzados', '% T2', 'T3 Anotados', 'T3 Lanzados', '% T3', 'T1 Anotados', 'T1 Lanzados', '% T1', 'Reb. Ofensivos', 'Reb. Defensivos', 'Rebotes', 'Asistencias', 'Robos', 'Perdidas', 'Tapones', 'Tapones Recibidos', 'Mates', 'Faltas Cometidas', 'Faltas Recibidas', 'Valoracion', '% Asist', '% Tiro Efectivo', '% Tiro Verdadero', 'GScore', 'Posesiones Anotadas', 'Posesiones No Anotadas', 'Tot Posesiones', 'Floor Percentage', 'Puntos por Tiro', '% Rebotes', '% Rebotes Def', '% Rebotes Of', '% Robos', 'Toques', 'Uso', 'Versatilidad', 'Win Scores', 'Eficiencia Ofensiva', 'Eficiencia Defensiva', 'Diferencia eficiencia']
    else:
        headers = ['Name', 'Condition', 'Games', 'Minutes', 'Points', '2PM', '2PA', '% 2P', '3PM', '3Pa', '% 3P', 'FTM', 'FTA', '% T1', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'TOV', 'BLK', 'BLKr', 'Dunks', 'PF', 'PFr', 'PIR', 'AST%', 'eFG%', 'TS%', 'GScore', 'Scored Poss.', 'Non-scored Poss.', 'Tot Poss.', 'Floor Percentage', 'PPS', 'TRB%', 'DRB%', 'ORB%', 'STL%', 'Touches', 'Usage', 'Versatility', 'Win Scores', 'OER', 'DER', 'Net']

    if sLang == 'Castellano':
        sCon1 = 'Nombre'
        sCon2 = 'Condicion'
    else:
        sCon1 = 'Name'
        sCon2 = 'Condition'

    df = DataFrame(avStats, columns=headers)
    df.sort_values([sCon1], inplace=True)
    df.sort_values([sCon2], inplace=True)

    df[sCon1] = df[sCon1].str[0]
    df[sCon2] = df[sCon2].str[0]
    for iStat in range(2,int(len(headers))):
        substBrackets(df,headers[iStat])

    df.sort_values([sCon1, sCon2], inplace=True)
    df.to_csv(csvFile, index=False)



def stats2csvTwice(avStats,csvFile):
    headers = ['Nombre', 'Condicion', 'Partidos', 'Minutos', 'Puntos', 'T2 Anotados', 'T2 Lanzados', '% T2', 'T3 Anotados', 'T3 Lanzados', '% T3', 'T1 Anotados', 'T1 Lanzados', '% T1', 'Reb. Ofensivos', 'Reb. Defensivos', 'Rebotes', 'Asistencias', 'Robos', 'Perdidas', 'Tapones', 'Tapones Recibidos', 'Mates', 'Faltas Cometidas', 'Faltas Recibidas', 'Valoracion', '% Asist', '% Tiro Efectivo', '% True Shooting', 'GScore', 'Posesiones Anotadas', 'Posesiones No Anotadas', 'Tot Posesiones', 'Floor Percentage', 'Puntos por Tiro', '% Rebotes', '% Rebotes Def', '% Rebotes Of', '% Robos', 'Toques', 'Usaje', 'Versatilidad', 'Win Scores', 'OER', 'DER', 'Net']

    df = DataFrame(avStats, columns=headers)
    df.sort_values(['Nombre'], inplace=True)
    df.sort_values(['Condicion'], inplace=True)

    df['Nombre'] = df['Nombre'].str[0]
    df['Condicion'] = df['Condicion'].str[0]
    for iStat in range(2,int(len(headers)-5)):
        substBrackets(df,headers[iStat])

    df.sort_values(['Nombre', 'Condicion'], inplace=True)
    df.to_csv(csvFile, index=False)



def getAvStats(statsPlayers, bHome, tipusPartit, bAgainst, bAgainst2, targetTeam,season, jorFirst, jorLast,sDir, strFase, bTeam, bProj, statsHome=None, statsAway=None, statsWin=None, statsLost=None, statsLast3=None, statsTop=None, statsBot=None, statsEasy=None, statsTough=None, sMinGames=None, sLang=None):
    players = []
    avStats = []
    playersT = []
    playersTAg = []
    teamStats = []
    teamStatsAg = []

    playersHome = []
    homeStats = []
    playersHomeT = []
    playersHomeTAg = []
    teamHomeStats = []
    teamHomeStatsAg = []

    playersAway = []
    awayStats = []
    playersAwayT = []
    playersAwayTAg = []
    teamAwayStats = []
    teamAwayStatsAg = []

    playersTit = []
    titStats = []

    playersBench = []
    benchStats = []

    playersLast3 = []
    last3Stats = []
    playersLast3T = []
    playersLast3TAg = []
    teamLast3Stats = []
    teamLast3StatsAg = []

    playersLost = []
    lostStats = []
    playersLostT = []
    playersLostTAg = []
    teamLostStats = []
    teamLostStatsAg = []

    playersWin = []
    winStats = []
    playersWinT = []
    playersWinTAg = []
    teamWinStats = []
    teamWinStatsAg = []

    playersEasy = []
    easyStats = []
    playersEasyT = []
    playersEasyTAg = []
    teamEasyStats = []
    teamEasyStatsAg = []

    playersTough = []
    toughStats = []
    playersToughT = []
    playersToughTAg = []
    teamToughStats = []
    teamToughStatsAg = []

    playersTarget1 = []
    target1Stats = []
    playersTarget1T = []
    playersTarget1TAg = []
    teamTarget1Stats = []
    teamTarget1StatsAg = []

    playersTarget2 = []
    target2Stats = []
    playersTarget2T = []
    playersTarget2TAg = []
    teamTarget2Stats = []
    teamTarget2StatsAg = []

    statsBench = []
    statsTit = []

    bCorrect = []
    for iGame in range(0, int(len(statsPlayers))):
        if statsPlayers[iGame][0] == []:
            bCorrect.append(False)
        else:
            bCorrect.append(True)


    if sLang == "Castellano":
        sGame = 'Partido'
        strAv = '1 Media'
        sWin = '2 Victoria'
        sLost = '2 Derrota'
        sLocal = '3 Local'
        sAway = '3 Visitante'
        sEasy = '5 Facil'
        sEasyt = '4 Facil'
        sTough = '5 Dificil'
        sTought = '4 Dificil'
        sTop = '6 Equipos Top'
        sTopt = '5 Equipos Top'
        sBottom = '6 Equipos Cola'
        sBottomt = '5 Equipos Cola'
        sLast3 = '7 Ultimos 3'
        sLast3t = '6 Ultimos 3'
        strAvT = 'Media'
        sCon = ' Rival'
    else:
        sGame = 'Game'
        strAv = '1 Average'
        sWin = '2 Win'
        sLost = '2 Lost'
        sLocal = '3 Local'
        sAway = '3 Away'
        sEasy = '5 Easy'
        sEasyt = '4 Easy'
        sTough = '5 Tough'
        sTought = '4 Tough'
        sTop = '6 Top Teams'
        sTopt = '5 Top Teams'
        sBottom = '6 Bot. Teams'
        sBottomt = '5 Bot. Teams'
        sLast3 = '7 Last 3'
        sLast3t = '6 Last 3'
        strAvT = 'Average'
        strAvTag = 'Average'
        sCon = ' Against'

    for iGame in range(0, int(len(statsPlayers)/3)):
        if bCorrect[iGame]:
            print(sGame + ' (' + str(iGame+1) + '/' + str(int(len(statsPlayers)/3)) + ')')
            #############################################
            iGame = iGame*3
            parseGameData(iGame, players, avStats, strAv,statsPlayers, False)
            if bHome[iGame] == True:
                parseGameData(iGame, playersHome, homeStats, sLocal,statsPlayers, False)
            else:
                parseGameData(iGame, playersAway, awayStats, sAway,statsPlayers, False)

            titStatsAux, benchStatsAux = parseGameDataTit(iGame, playersTit, titStats, playersBench, benchStats, statsPlayers, statsPlayers, sLang)

            statsTit.append(titStatsAux)
            statsTit.append(statsPlayers[iGame+1])
            statsTit.append(statsPlayers[iGame+2])
            statsBench.append(benchStatsAux)
            statsBench.append(statsPlayers[iGame + 1])
            statsBench.append(statsPlayers[iGame + 2])
            if ((len(statsPlayers)/3)-(iGame/3)) < 4:
                parseGameData(iGame, playersLast3, last3Stats, sLast3,statsPlayers, False)
            try:
                if tipusPartit[iGame][1] == 'L':
                    parseGameData(iGame, playersLost, lostStats,sLost,statsPlayers, False)
                else:
                    parseGameData(iGame, playersWin, winStats,sWin,statsPlayers, False)
            except:
                pass

            if tipusPartit[iGame][0] == 'E':
                parseGameData(iGame, playersEasy, easyStats,sEasy,statsPlayers, False)
            else:
                parseGameData(iGame, playersTough, toughStats,sTough,statsPlayers, False)

            if bAgainst[iGame] == True:
                parseGameData(iGame, playersTarget1, target1Stats,sTop,statsPlayers, False)

            if bAgainst2[iGame] == True:
                parseGameData(iGame, playersTarget2, target2Stats,sBottom,statsPlayers, False)

            #############################################
            iGameTeam = iGame+1
            parseGameData(iGameTeam, playersT, teamStats, strAv, statsPlayers, True)

            try:
                if bHome[iGameTeam] == True:
                    parseGameData(iGameTeam, playersHomeT, teamHomeStats, sLocal,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersAwayT, teamAwayStats, sAway,statsPlayers, True)

                if bAgainst[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget1T, teamTarget1Stats, sTopt,statsPlayers, True)

                if bAgainst2[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget2T, teamTarget2Stats, sBottomt,statsPlayers, True)

                if ((len(statsPlayers) / 3) - (iGame / 3)) < 4:
                    parseGameData(iGameTeam, playersLast3T, teamLast3Stats, sLast3t,statsPlayers, True)

                if tipusPartit[iGameTeam][1] == 'L':
                    parseGameData(iGameTeam, playersLostT, teamLostStats, sLost,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersWinT, teamWinStats, sWin,statsPlayers, True)

                if tipusPartit[iGameTeam][0] == 'E':
                    parseGameData(iGameTeam, playersEasyT, teamEasyStats, sEasyt,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersToughT, teamToughStats, sTought,statsPlayers, True)
            except:
                pass

            iGameTeam = iGame + 2
            parseGameData(iGameTeam, playersTAg, teamStatsAg, strAv + sCon,statsPlayers, True)
            try:
                if bHome[iGameTeam] == True:
                    parseGameData(iGameTeam, playersHomeTAg, teamHomeStatsAg, sLocal + sCon,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersAwayTAg, teamAwayStatsAg, sAway + sCon,statsPlayers, True)

                if bAgainst[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget1TAg, teamTarget1StatsAg, sTopt + sCon,statsPlayers, True)

                if bAgainst2[iGameTeam] == True:
                    parseGameData(iGameTeam, playersTarget2TAg, teamTarget2StatsAg, sBottomt + sCon,statsPlayers, True)

                if ((len(statsPlayers) / 3) - (iGame / 3)) < 4:
                    parseGameData(iGameTeam, playersLast3TAg, teamLast3StatsAg, sLast3t + sCon,statsPlayers, True)

                if tipusPartit[iGameTeam][1] == 'L':
                    parseGameData(iGameTeam, playersLostTAg, teamLostStatsAg, sLost + sCon,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersWinTAg, teamWinStatsAg, sWin + sCon,statsPlayers, True)

                if tipusPartit[iGameTeam][0] == 'E':
                    parseGameData(iGameTeam, playersEasyTAg, teamEasyStatsAg, sEasyt + sCon,statsPlayers, True)
                else:
                    parseGameData(iGameTeam, playersToughTAg, teamToughStatsAg, sTought + sCon,statsPlayers, True)
            except:
                pass

    computeAdvStats(statsPlayers, avStats, teamStats, teamStatsAg)
    if statsHome != None:
        if homeStats != []:
            computeAdvStats(statsHome, homeStats, teamHomeStats, teamHomeStatsAg)
        if awayStats != []:
            computeAdvStats(statsAway, awayStats, teamAwayStats, teamAwayStatsAg)
        computeAdvStats(statsTit, titStats)
        computeAdvStats(statsBench, benchStats)
        if lostStats != []:
            computeAdvStats(statsLost, lostStats, teamLostStats, teamLostStatsAg)
        if winStats != []:
            computeAdvStats(statsWin, winStats, teamWinStats, teamWinStatsAg)
        if easyStats != []:
            computeAdvStats(statsEasy, easyStats, teamEasyStats, teamEasyStatsAg)
        if toughStats != []:
            computeAdvStats(statsTough, toughStats, teamToughStats, teamToughStatsAg)
        if last3Stats != []:
            computeAdvStats(statsLast3, last3Stats, teamLast3Stats, teamLast3StatsAg)
        if target1Stats != []:
            computeAdvStats(statsTop,  target1Stats, teamTarget1Stats, teamTarget1StatsAg)
        if target2Stats != []:
            computeAdvStats(statsBot,  target2Stats, teamTarget2Stats, teamTarget2StatsAg)

    for iPlayer in range(0, len(avStats)):
        tryAppend(avStats, iPlayer)
        if homeStats != []:
            tryAppend(homeStats, iPlayer)
        if awayStats != []:
            tryAppend(awayStats, iPlayer)
        tryAppend(titStats, iPlayer)
        tryAppend(benchStats, iPlayer)
        if last3Stats != []:
            tryAppend(last3Stats, iPlayer)
        if lostStats != []:
            tryAppend(lostStats, iPlayer)
        if winStats != []:
            tryAppend(winStats, iPlayer)
        if easyStats != []:
            tryAppend(easyStats, iPlayer)
        if toughStats != []:
            tryAppend(toughStats, iPlayer)
        if target1Stats != []:
            tryAppend(target1Stats, iPlayer)
        if target2Stats != []:
            tryAppend(target2Stats, iPlayer)

    tryAppend(teamStats, 0)
    if homeStats != []:
        tryAppend(teamHomeStats, 0)
    if awayStats != []:
        tryAppend(teamAwayStats, 0)
    if last3Stats != []:
        tryAppend(teamLast3Stats, 0)
    if lostStats != []:
        tryAppend(teamLostStats, 0)
    if winStats != []:
        tryAppend(teamWinStats, 0)
    if easyStats != []:
        tryAppend(teamEasyStats, 0)
    if toughStats != []:
        tryAppend(teamToughStats, 0)
    if target1Stats != []:
        tryAppend(teamTarget1Stats, 0)
    if target2Stats != []:
        tryAppend(teamTarget2Stats, 0)
    tryAppend(teamStatsAg, 0)
    if homeStats != []:
        tryAppend(teamHomeStatsAg, 0)
    if awayStats != []:
        tryAppend(teamAwayStatsAg, 0)
    if last3Stats != []:
        tryAppend(teamLast3StatsAg, 0)
    if lostStats != []:
        tryAppend(teamLostStatsAg, 0)
    if winStats != []:
        tryAppend(teamWinStatsAg, 0)
    if easyStats != []:
        tryAppend(teamEasyStatsAg, 0)
    if toughStats != []:
        tryAppend(teamToughStatsAg, 0)
    if target1Stats != []:
        tryAppend(teamTarget1StatsAg, 0)
    if target2Stats != []:
        tryAppend(teamTarget2StatsAg, 0)

    avStatsArr = np.copy(np.array(avStats))
    stats2csv(avStats, last3Stats, homeStats, awayStats, titStats, benchStats, winStats, lostStats, easyStats, toughStats, target1Stats, target2Stats, sDir + '/p'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + strFase + '.csv', sLang)
    if bTeam:
        stats2csvTeam(teamStats, teamLast3Stats, teamHomeStats, teamAwayStats, teamWinStats, teamLostStats, teamEasyStats, teamToughStats, teamTarget1Stats, teamTarget2Stats, teamStatsAg, teamLast3StatsAg, teamHomeStatsAg, teamAwayStatsAg, teamWinStatsAg, teamLostStatsAg, teamEasyStatsAg, teamToughStatsAg, teamTarget1StatsAg, teamTarget2StatsAg, sDir + '/t'+targetTeam+season+ 'J' + str(jorFirst) + 'J' + str(jorLast) +  strFase + '.csv', sLang)

    namesArr = np.array(avStatsArr[:, 0])
    namesArr = np.array([str(x)[4:-4] for x in namesArr])
    gamesArr = np.array(avStatsArr[:, 2])
    gamesArr = np.array([int(x) for x in gamesArr])

    topStats = []

    if sMinGames != None and sMinGames != '':
        iMinGames = int(sMinGames)
    else:
        iMinGames = np.max(gamesArr) / 2

    for iStat in range(3, len(avStats[0])):
        statArr = np.array(avStatsArr[:, iStat])
        statArr = np.array([float(x) for x in statArr])
        statArr = statArr*(gamesArr>iMinGames)
        inds = statArr.argsort()[::-1]
        sortedPlayers = namesArr[inds]
        topStats.append(sortedPlayers)
        sortedVal = statArr[inds]
        topStats.append(sortedVal)

    ranking2csv(topStats, sDir + '/r'+targetTeam+season + 'J' + str(jorFirst) + 'J' + str(jorLast) + strFase + '.csv', sLang)

def ranking2csv(topStats, csvFile, sLang):
    if sLang == 'Castellano':
        headers = ['Minutos (jugador)', 'Minutos (valor)', 'Puntos (jugador)', 'Puntos (valor)', 'T2 Anotados (jugador)', 'T2 Anotados (valor)', 'T2 Lanzados (jugador)', 'T2 Lanzados (valor)', '% T2 (jugador)', '% T2 (valor)', 'T3 Anotados (jugador)', 'T3 Anotados (valor)', 'T3 Lanzados (jugador)', 'T3 Lanzados (valor)', '% T3 (jugador)', '% T3 (valor)', 'T1 Anotados (jugador)','T1 Anotados (valor)', 'T1 Lanzados (jugador)','T1 Lanzados (valor)', '% T1 (jugador)','% T1 (valor)', 'Reb. Ofensivos (jugador)', 'Reb. Ofensivos (valor)', 'Reb. Defensivos (jugador)', 'Reb. Defensivos (valor)', 'Rebotes (jugador)', 'Rebotes (valor)', 'Asistencias (jugador)', 'Asistencias (valor)', 'Robos (jugador)', 'Robos (valor)', 'Perdidas (jugador)', 'Perdidas (valor)', 'Tapones (jugador)', 'Tapones (valor)', 'Tapones Recibidos (jugador)', 'Tapones Recibidos (valor)', 'Mates (jugador)', 'Mates (valor)', 'Faltas Cometidas (jugador)', 'Faltas Cometidas (valor)', 'Faltas Recibidas (jugador)', 'Faltas Recibidas (valor)', 'Valoracion (jugador)', 'Valoracion (valor)',  '% Asist (jugador)', '% Asist (valor)', '% Tiro Efectivo (jugador)', '% Tiro Efectivo (valor)', '% Tiro Verdadero (jugador)', '% True Shooting (valor)', 'GScore (jugador)', 'GScore (valor)', 'Posesiones Anotadas (jugador)', 'Posesiones Anotadas (valor)', 'Posesiones No Anotadas (jugador)', 'Posesiones No Anotadas (valor)', 'Tot Posesiones (jugador)',  'Tot Posesiones (valor)', 'Floor Percentage (jugador)', 'Floor Percentage (valor)', 'Puntos por Tiro (jugador)', 'Puntos por Tiro (valor)',  '% Rebotes (jugador)', '% Rebotes (valor)', '% Rebotes Def (jugador)', '% Rebotes Def (valor)',  '% Rebotes Of (jugador)', '% Rebotes Of (valor)',  '% Robos (jugador)', '% Robos (valor)',  'Toques (jugador)', 'Toques (valor)',  'Uso (jugador)', 'Uso (valor)', 'Versatilidad (jugador)', 'Versatilidad (valor)', 'Win Scores (jugador)',  'Win Scores (valor)', 'Eficiencia Ofensiva (jugador)', 'Eficiencia Ofensiva (valor)', 'Eficiencia Defensiva (jugador)', 'Eficiencia Defensiva (valor)', 'Diferencia Eficiencia (jugador)', 'Diferencia Eficiencia (valor)']
    else:
        headers = ['Minutes (player)', 'Minutes (value)', 'Points (player)', 'Points (value)', '2PM (player)', '2PM (value)', '2PA (player)', '2PA (value)', '% 2P (player)', '% 2P (value)', '3PM (player)', '3PM (value)', '3PA (player)', '3PA (value)', '% 3P (player)', '% 3P (value)', 'FTM (player)','FTM (value)', 'FTA (player)','FTA (value)', '% FT (player)','% FT (value)', 'ORB (player)', 'ORB (value)', 'DRB (player)', 'DRB (value)', 'REB (player)', 'REB (value)', 'ASS (player)', 'ASS (value)', 'STL (player)', 'STL (value)', 'TOV (player)', 'TOV (value)', 'BLK (player)', 'BLK (value)', 'BLKr (player)', 'BLKr (value)', 'Dunks (player)', 'Dunks (value)', 'PF (player)', 'PF (value)', 'PFr (player)', 'PFr (value)', 'PIR (player)', 'PIR (value)',  'ASS% (player)', 'ASS% (value)', 'eFG% (player)', 'eFG% (value)', 'TS% (player)', 'TS% (value)', 'GScore (player)', 'GScore (value)', 'Scored Poss. (player)', 'Scored Poss. (value)', 'Non-scored Poss. (player)', 'Non-scored Poss. (value)', 'Tot. Possessions (player)',  'Tot. Possessions (value)', 'Floor Percentage (player)', 'Floor Percentage (value)', 'PPS (player)', 'PPS (value)',  'REB% (player)', 'REB% (value)', 'DRB% (player)', 'DRB% (value)',  'ORB% (player)', 'ORB% (value)',  'STL% (player)', 'STL% (value)',  'Touches (player)', 'Touches (value)',  'Usage (player)', 'Usage (value)', 'Versatility (player)', 'Versatility (value)', 'Win Scores (player)',  'Win Scores (value)', 'OER (player)', 'OER (value)', 'DER (player)', 'DER (value)', 'Net (player)', 'Net (value)']

    df = DataFrame(np.transpose(topStats), columns=headers)
    df.to_csv(csvFile, index=False)

def filterPlayers(inPlayers,sPlayers):
    outPlayers = []
    aTrans = np.transpose(np.array(inPlayers))
    for p in range(0, aTrans.shape[0]):
        try:
            playInd = str(aTrans[p][0].replace('\n','').replace(',','')).split(' ')
            for iPlay in range(0, len(sPlayers)):
                if sPlayers[iPlay].replace(' ','') in playInd:
            # if len([i for i in sPlayers if i in playInd]) > 0:
                    outPlayers.append(aTrans[p])
        except:
            pass
    outPlayers = list(np.transpose(outPlayers))
    return outPlayers

