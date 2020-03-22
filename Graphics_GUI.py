# encoding: utf-8
from tkinter import *
from tkinter import ttk
import GetAllGamesCommon
import GetAllLeagueCommon
import GetAllLeagueBothPlata
import unicodedata
from importlib import reload
import os
import platform
import numpy as np
import DrawingFunctions as libDraw

system = platform.system()

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.TeamLabel = Label(self)
        self.text_team = ''
        self.SeasonLabel = Label(self)
        self.text_season = ''
        self.jFirstLabel = Label(self)
        self.text_jFirst = ''
        self.jLastLabel = Label(self)
        self.text_jLast = ''
        self.divisionLabel = Label(self)
        self.text_division = ''
        self.folderLabel = Label(self)
        self.text_folder = ''
        self.perLabel = Label(self)
        self.text_periodos = ''
        self.confLabel = Label(self)
        self.text_chrome = ''
        self.xaxisLabel = Label(self)
        self.yaxisLabel = Label(self)

        self.choices = {'%','Puntos','T2 Anotados','T2 Lanzados','% T2','T3 Anotados','T3 Lanzados','% T3','T1 Anotados','T1 Lanzados','% T1','Reb. Ofensivos','Reb. Defensivos','Asistencias','Robos','Perdidas','Tapones','Tapones Recibidos','Mates','Faltas Cometidas','Faltas Recibidas','Valoracion','Posesiones','Ritmo','OER','DER','% TC Efectivo','% Jugada','Frec. TL','% Reb Def','% Reb Of','% Assis','% Perd','Puntos Riv','T2 Anotados Riv','T2 Lanzados Riv','% T2 Riv','T3 Anotados Riv','T3 Lanzados Riv','% T3 Riv','T1 Anotados Riv','T1 Lanzados Riv','% T1 Riv','Reb. Ofensivos Riv','Reb. Defensivos Riv','Asistencias Riv','Robos Riv','Perdidas Riv','Tapones Riv','Tapones Recibidos Riv','Mates Riv','Faltas Cometidas Riv','Faltas Recibidas Riv','Valoracion Riv','Posesiones Riv','Ritmo Riv','OER Riv','DER Riv','% TC Efectivo Riv','% Jugada Riv','Frec. TL Riv','% Reb Def Riv','% Reb Of Riv','% Assis Riv','% Perd Riv'}
        self.choices = sorted(self.choices)
        self.xAxis = StringVar()
        self.xAxis.set('%')
        self.yAxis = StringVar()
        self.yAxis.set('%')

        self.create_widgets()

    def create_widgets(self):
        self.create_season_widget()
        self.create_rounds_widget()
        self.create_division_widget()
        self.create_xAxis_widget()
        self.create_yAxis_widget()

        self.create_export_widget()
        self.create_folder()

    def create_season_widget(self):
        self.SeasonLabel['text'] = '1. Temporada:'
        self.SeasonLabel.grid(row=0, column=0, sticky=W)
        #self.SeasonLabel = Label(self, text="2. Temporada:").grid(row=2, column=0, sticky=W)
        self.text_season = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_season.grid(row=0, column=1, columnspan=1, sticky=W)
        self.text_season.insert(END, "2019")
        # self.text_season.configure(state="disabled")

    def create_rounds_widget(self):
        self.jFirstLabel['text'] = "3. Primera Jornada:"
        self.jFirstLabel.grid(row=2, column=0, sticky=W)
        self.jLastLabel['text'] = "4. Ultima Jornada:"
        self.jLastLabel.grid(row=3, column=0, sticky=W)

        self.text_jFirst = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jFirst.grid(row=2, column=1, columnspan=1, sticky=W)
        self.text_jFirst.insert(END, "1")
        # self.text_jFirst.configure(state="disabled")

        self.text_jLast = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jLast.grid(row=3, column=1, columnspan=1, sticky=W)
        self.text_jLast.insert(END, "2")
        # self.text_jLast.configure(state="disabled")

    def create_division_widget(self):
        self.divisionLabel['text'] = '2. Categoria:'
        self.divisionLabel.grid(row=1, column=0, sticky=W)
        self.text_division = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_division.grid(row=1, column=1, columnspan=1, sticky=W)
        self.text_division.insert(END, "Oro")
        # self.text_division.configure(state="disabled")

    def create_folder(self):
        self.folderLabel['text'] = 'Carpeta Destino:'
        self.folderLabel.grid(row=4, column=0, sticky=W)
        self.text_folder = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_folder.grid(row=4, column=1, columnspan=1, sticky=W)
        self.text_folder.insert(END, os.path.dirname(os.path.abspath(__file__)) + "/Images")
        # self.text_folder.configure(state="disabled")

    def create_xAxis_widget(self):
        self.xaxisLabel['text'] = 'Eje X:'
        self.xaxisLabel.grid(row=5, column=0, sticky=W)

        self.xAxisMenu = ttk.OptionMenu(self, self.xAxis, *self.choices)
        self.xAxisMenu.grid(row=5, column=1)
        #self.xAxisMenu.pack()

    def create_yAxis_widget(self):
        self.yaxisLabel['text'] = 'Eje Y:'
        self.yaxisLabel.grid(row=6, column=0, sticky=W)

        self.yAxisMenu = ttk.OptionMenu(self, self.yAxis, *self.choices)
        self.yAxisMenu.grid(row=6, column=1)
        #self.yAxisMenu.pack()

    def create_export_widget(self):
        self.button_compare = ttk.Button()
        self.button_compare.configure(text="Extraer Estadisticas")
        self.button_compare.grid(row=7, column=1, sticky=W)
        self.button_compare["command"] = self.save_stats
        # self.button_compare.configure(state="disabled")
        # self.button_compare.place(x = 100, y = 320)

    def save_stats(self):
        self.text_chrome = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver'
        bAll = 0
        bTeam = 0
        bProj = False

        iBenIn = 2
        iEndIn = -3

        if iEndIn != 0:
            season = str(unicodedata.normalize('NFKD', self.text_season.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            division = str(unicodedata.normalize('NFKD', self.text_division.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()[iBenIn:iEndIn]
        else:
            season = str(unicodedata.normalize('NFKD', self.text_season.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            division = str(unicodedata.normalize('NFKD', self.text_division.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()

        bUnaFase = False
        divSplit = division.split(',')[0]
        try:
            groupSplit = division.split(',')[1]
        except:
            pass
        if division == 'ORO':
            groupFeb = '1'
        elif division == 'DIA' or division == 'LF':
            groupFeb = '4'
        elif divSplit == 'PLATA':
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
            if groupSplit[0] == 'A':
                groupFeb = '3'
            elif groupSplit[0] == 'B':
                groupFeb = '5'
            elif groupSplit[0] == 'C':
                if int(season) > 2018:
                    if groupSplit[1] == 'A':
                        groupFeb = '6'
                    elif groupSplit[1] == 'B':
                        groupFeb = '46'
                else:
                    groupFeb = '6'
            elif groupSplit[0] == 'D':
                groupFeb = '7'
            elif groupSplit[0] == 'E':
                groupFeb = '8'
        elif divSplit == 'LF2':
            groupFeb = '9'

        sLang = 'Castellano'

        html_doc = "http://competiciones.feb.es/Estadisticas/Calendario.aspx?g=" + groupFeb + "&t=" + season + "&"
        targetTeam = 'Liga'
        sPlayers = ''
        sMinGames = ''

        if iEndIn != 0:
            jorFirst = int(str(unicodedata.normalize('NFKD', self.text_jFirst.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn])
            jorLast = int(str(unicodedata.normalize('NFKD', self.text_jLast.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn])
            sDir = str(unicodedata.normalize('NFKD', self.text_folder.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
        else:
            jorFirst = int(str(unicodedata.normalize('NFKD', self.text_jFirst.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', ''))
            jorLast = int(str(unicodedata.normalize('NFKD', self.text_jLast.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', ''))
            sDir = str(unicodedata.normalize('NFKD', self.text_folder.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')

        if division == 'ORO' or division == 'DIA' or division == 'ENDESA':
            fileLoad = sDir + '/' + division + str(season) + 'J' + str(jorFirst) + 'J' + str(jorLast) + '.npy'
        elif divSplit == 'PLATA':
            if bUnaFase:
                fileLoad = sDir + '/' + division.replace(',', '-') + str(season) + 'J' + str(jorFirst) + 'J' + str(jorLast) + '.npy'
            else:
                fileLoad = sDir + '/' + division.replace(',', '-') + str(season) + 'J' + str(jorFirst) + 'J' + str(jorLast*2) + '.npy'
        else:
            fileLoad = sDir + '/' + division.replace(',', '-') + str(season) + 'J' + str(jorFirst) + 'J' + str(jorLast) + '.npy'

        bExisting = os.path.exists(fileLoad)

        if bExisting == False:
            if targetTeam == 'Liga' or targetTeam == 'LIGA':
                if division == 'ORO' or division == 'DIA' or division == 'ENDESA':
                    GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division, sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, True)
                elif divSplit == 'PLATA':
                    if bUnaFase == False:
                        GetAllLeagueBothPlata.extractStatisticsPlataAll(html_doc,targetTeam,season,jorFirst,jorLast,division.split(',')[1],division.split(',')[2],sDir,self.text_chrome,bTeam,sPlayers,bProj,division,'',sMinGames, sLang, True)
                        reload(GetAllLeagueBothPlata)
                    else:
                        GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, '', 'Fase1', sMinGames, sLang, True)
                elif divSplit == 'EBA':
                    GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, True)
                elif divSplit == 'LF2':
                    GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, True)
                reload(GetAllLeagueCommon)

        xAxisF = self.xAxis.get()
        yAxisF = self.yAxis.get()

        teamStats = np.load(fileLoad, allow_pickle=True)
        teamStatsAg = np.load(fileLoad, allow_pickle=True)
        libDraw.draw2Features(teamStats, teamStatsAg, sDir, xAxisF, yAxisF, season, division, jorFirst, jorLast)
        a = 1

#if __name__ == '__main__':
root = Tk()
root.title("BueStats Graphics (Adrià Arbués-Sangüesa, @arbues6)")
root.geometry("950x450")
root.columnconfigure(0, weight=1)
root.resizable(0, 0)

app = Application(root)
app.mainloop()
