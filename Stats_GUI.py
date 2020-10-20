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
        self.tTopLabel = Label(self)
        self.text_equiposTop = ''
        self.tBotLabel = Label(self)
        self.text_equiposBott = ''
        self.divisionLabel = Label(self)
        self.text_division = ''
        self.folderLabel = Label(self)
        self.text_folder = ''
        self.perLabel = Label(self)
        self.text_periodos = ''
        self.confLabel = Label(self)
        self.text_conf = ''
        self.text_chrome = ''
        self.jugadoresLabel = Label(self)
        self.text_jugadores = ''
        self.minPartidosLabel = Label(self)
        self.text_minPartidos = ''
        self.chEquipoLabel = Label(self)
        self.checkEquipo = IntVar(value=1)
        self.chAllLabel = Label(self)
        self.checkAll = IntVar(value=1)
        self.checkProj = IntVar(value=0)
        self.chRankLabel = Label(self)
        self.checkRank = IntVar(value=1)
        self.language = StringVar(value="Castellano")
        #self.Options = ["Castellano", "English"]
        self.create_widgets()

    def create_widgets(self):
        self.create_season_widget()
        self.create_rounds_widget()
        self.create_target_widget()
        self.create_against1_widget()
        self.create_against2_widget()
        self.create_division_widget()
        self.create_conf_button()
        self.create_export_widget()
        self.create_folder()
        self.create_periodos_widget()
        self.create_conf_widget()
        self.create_players_widget()
        self.create_boxTeam_widget()
        self.create_boxGames_widget()
        self.create_language_widget()
        ###self.create_proj_widget()
        self.create_rank_widget()

    def create_season_widget(self):
        self.SeasonLabel['text'] = '2. Temporada:'
        self.SeasonLabel.grid(row=2, column=0, sticky=W)
        #self.SeasonLabel = Label(self, text="2. Temporada:").grid(row=2, column=0, sticky=W)
        self.text_season = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_season.grid(row=2, column=1, columnspan=1, sticky=W)
        self.text_season.insert(END, "2018")
        # self.text_season.configure(state="disabled")


    def create_rounds_widget(self):
        self.jFirstLabel['text'] = "4. Primera Jornada:"
        self.jFirstLabel.grid(row=4, column=0, sticky=W)
        self.jLastLabel['text'] = "5. Ultima Jornada:"
        self.jLastLabel.grid(row=5, column=0, sticky=W)

        self.text_jFirst = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jFirst.grid(row=4, column=1, columnspan=1, sticky=W)
        self.text_jFirst.insert(END, "1")
        # self.text_jFirst.configure(state="disabled")

        self.text_jLast = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jLast.grid(row=5, column=1, columnspan=1, sticky=W)
        self.text_jLast.insert(END, "34")
        # self.text_jLast.configure(state="disabled")

    def create_target_widget(self):
        self.TeamLabel['text'] = '1. Equipo:'
        self.TeamLabel.grid(row=1, column=0, sticky=W)
        #Label(self, text="1. Equipo:").grid(row=1, column=0, sticky=W)
        #self.LabelTeam.grid(row=1, column=0, sticky=W)
        self.text_team = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_team.grid(row=1, column=1, columnspan=1, sticky=W)
        self.text_team.insert(END, "Araberri")
        # self.text_team.configure(state="disabled")

    def create_against1_widget(self):
        self.tTopLabel['text'] = "6. Equipos Top:"
        self.tTopLabel.grid(row=6, column=0, sticky=W)
        self.text_equiposTop = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_equiposTop.grid(row=6, column=1, columnspan=1, sticky=W)
        self.text_equiposTop.insert(END, "BETIS,BILBAO,PALMA,MELILLA")
        # self.text_equiposTop.configure(state="disabled")

    def create_against2_widget(self):
        self.tBotLabel['text'] = '7. Equipos Cola:'
        self.tBotLabel.grid(row=7, column=0, sticky=W)
        self.text_equiposBott = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_equiposBott.grid(row=7, column=1, columnspan=1, sticky=W)
        self.text_equiposBott.insert(END, "CACERES,CANOE,PRAT,ARABERRI,TAU")
        # self.text_equiposBott.configure(state="disabled")

    def create_division_widget(self):
        self.divisionLabel['text'] = '3. Categoria:'
        self.divisionLabel.grid(row=3, column=0, sticky=W)
        self.text_division = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_division.grid(row=3, column=1, columnspan=1, sticky=W)
        self.text_division.insert(END, "Oro")
        # self.text_division.configure(state="disabled")

    def create_periodos_widget(self):
        self.perLabel['text'] = "8. Intervalos:"
        self.perLabel.grid(row=8, column=0, sticky=W)
        self.text_periodos = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_periodos.grid(row=8, column=1, columnspan=1, sticky=W)
        self.text_periodos.insert(END, "5")
        # self.text_periodos.configure(state="disabled")

    def create_players_widget(self):
        self.jugadoresLabel['text'] = "9. Jugadores:"
        self.jugadoresLabel.grid(row=9, column=0, sticky=W)
        self.text_jugadores = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_jugadores.grid(row=9, column=1, columnspan=1, sticky=W)
        self.text_jugadores.insert(END, "")
        # self.text_jugadores.configure(state="disabled")

    def create_boxTeam_widget(self):
        self.chEquipoLabel['text'] = "Extraer Estadisticas de Equipo:"
        self.chEquipoLabel.grid(row=12, column=0, sticky=W)
        self.checkButtonTeam = ttk.Checkbutton()
        #self.checkButtonTeam.configure(width=12, var=self.checkEquipo,height=1, relief=RIDGE, borderwidth=2)
        self.checkButtonTeam.configure(width=2, var=self.checkEquipo)
        self.checkButtonTeam.grid(row=12, column=0, columnspan=1, sticky=W)
        if system == 'Windows':
            self.checkButtonTeam.place(x=290, y = 220)
        else:
            self.checkButtonTeam.place(x=305, y = 245)

    def create_boxGames_widget(self):
        self.chAllLabel['text'] = "Extraer Todas las Jornadas:"
        self.chAllLabel.grid(row=11, column=0, sticky=W)
        self.checkButtonGames = ttk.Checkbutton()
        #self.checkButtonGames.configure(width=12, var=self.checkAll,height=1, relief=RIDGE, borderwidth=2)
        self.checkButtonGames.configure(width=2, var=self.checkAll)
        # self.checkButtonGames.grid(row=11, column=0, columnspan=1, sticky=W)
        if system == 'Windows':
            self.checkButtonGames.place(x=290, y = 200)
        else:
            self.checkButtonGames.place(x=305, y = 225)

    def create_proj_widget(self):
        Label(self, text="Extraer Proyecciones:").grid(row=13, column=0, sticky=W)
        self.checkButtonProj = ttk.Checkbutton()
        #self.checkButtonProj.configure(width=12, var=self.checkProj, height=1, relief=RIDGE, borderwidth=2)
        self.checkButtonProj.configure(width=2, var=self.checkProj)
        self.checkButtonProj.grid(row=11, column=0, columnspan=1, sticky=W)
        self.checkButtonProj.place(x=305, y=265)

    def create_rank_widget(self):
        self.chRankLabel['text'] = "Extraer Rankings:"
        self.chRankLabel.grid(row=13, column=0, sticky=W)
        self.checkButtonRank = ttk.Checkbutton()
        if system == 'Linux':
            #self.checkButtonRank.configure(width=12, var=self.checkRank, height=1, relief=RIDGE, borderwidth=2)
            self.checkButtonRank.configure(width=12, var=self.checkRank)
        else:
            #self.checkButtonRank.configure(width=2, var=self.checkRank, height=1, relief=RIDGE, borderwidth=2)
            self.checkButtonRank.configure(width=2, var=self.checkRank)
        self.checkButtonRank.grid(row=13, column=0, sticky=W)
        if system == 'Windows':
            self.checkButtonRank.place(x=290, y=240)
        else:
            self.checkButtonRank.place(x=305, y=265)

        if system == 'Linux':
            self.minPartidosLabel['text'] = "Minimo Partidos:"
            self.minPartidosLabel.place(x=350, y=267)
            self.text_minPartidos = Text(self, width=15, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
            self.text_minPartidos.place(x=460, y=265)
            self.text_minPartidos.insert(END, "")
        elif system == 'Windows':
            self.minPartidosLabel['text'] = "Minimo Partidos:"
            self.minPartidosLabel.place(x=300, y=235)
            # Label(self, text="Minimo Partidos:").place(x=300, y=265)
            self.text_minPartidos = Text(self, width=15, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
            self.text_minPartidos.place(x=410, y=235)
            self.text_minPartidos.insert(END, "")
        else:
            self.minPartidosLabel['text'] = "Minimo Partidos:"
            self.minPartidosLabel.place(x=300, y=265)
            #Label(self, text="Minimo Partidos:").place(x=300, y=265)
            self.text_minPartidos = Text(self, width=15, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
            self.text_minPartidos.place(x=410, y=265)
            self.text_minPartidos.insert(END, "")

    def create_export_widget(self):
        self.button_compare = ttk.Button()
        self.button_compare.configure(text="Extraer Estadisticas")
        self.button_compare.grid(row=18, column=1, sticky=W)
        self.button_compare["command"] = self.save_stats
        # self.button_compare.configure(state="disabled")
        # self.button_compare.place(x = 100, y = 320)

    def create_conf_button(self):
        self.button_conf = ttk.Button()
        self.button_conf.configure(text="Cargar Configuracion")
        self.button_conf.grid()
        if system == 'Linux':
            self.button_conf.place(x=80, y=405)
        else:
            self.button_conf.place(x=110, y=400)
        # self.button_conf.place(x=110, y=400)
        self.button_conf["command"] = self.load_conf
        # self.button_conf.place(x = 100, y = 350)

    def create_conf_widget(self):
        self.confLabel['text'] = "Carpeta Configuracion:"
        self.confLabel.grid(row=16, column=0, sticky=W)
        self.text_conf = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_conf.grid(row=16, column=1, columnspan=1, sticky=W)
        self.text_conf.insert(END, os.path.dirname(os.path.abspath(__file__)) + "/ValoresDefectoPLATA2.txt")

    def create_folder(self):
        self.folderLabel['text'] = 'Carpeta Destino:'
        self.folderLabel.grid(row=18, column=0, sticky=W)
        self.text_folder = Text(self, width=53, height=1, wrap=WORD, relief=RIDGE, borderwidth=2)
        self.text_folder.grid(row=18, column=1, columnspan=1, sticky=W)
        self.text_folder.insert(END, os.path.dirname(os.path.abspath(__file__)) + "/Reports")
        # self.text_folder.configure(state="disabled")

    def create_language_widget(self):
        # self.language_drop = ttk.OptionMenu(self,self.language,*self.Options).grid(row=24, column=0, sticky=W)
        # # self.language_drop.pack()
        self.changeLang = ttk.Button()
        self.changeLang.configure(text="Change Language")
        self.changeLang.grid()
        if system == 'Linux':
            self.changeLang.place(x=80, y=375)
        else:
            self.changeLang.place(x=112, y=365)
        self.changeLang["command"] = self.change_language

    def change_language(self):
        if self.language.get() == "Castellano":
            self.language = StringVar(value="English")
        else:
            self.language = StringVar(value="Castellano")

        if self.language.get() == "Castellano":
            #self.create_labels_cast()
            self.TeamLabel['text'] = '1. Equipo:'
            self.SeasonLabel['text'] = '2. Temporada:'
            self.divisionLabel['text'] = '3. Categoria:'
            self.jFirstLabel['text'] = "4. Primera Jornada:"
            self.jLastLabel['text'] = "5. Ultima Jornada:"
            self.tTopLabel['text'] = "6. Equipos Top:"
            self.tBotLabel['text'] = '7. Equipos Cola'
            self.perLabel['text'] = "8. Intervalos:"
            self.jugadoresLabel['text'] = "9. Jugadores"
            self.chEquipoLabel['text'] = "Extraer Estadisticas de Equipo:"
            self.chAllLabel['text'] = "Extraer Todas las Jornadas:"
            self.chRankLabel['text'] = "Extraer Rankings:"
            self.minPartidosLabel['text'] = "Min. Partidos:"
            self.confLabel['text'] = "Carpeta Configuracion:"
            self.folderLabel['text'] = 'Carpeta Destino:'

            self.button_conf.configure(text="Cargar Configuracion")
            self.button_compare.configure(text="Extraer Estadisticas")
            self.changeLang.configure(text="Change Language")
        else:
            self.TeamLabel['text'] = '1. Team:'
            self.SeasonLabel['text'] = '2. Season:'
            self.divisionLabel['text'] = '3. Division:'
            self.jFirstLabel['text'] = "4. First Round:"
            self.jLastLabel['text'] = "5. Last Round:"
            self.tTopLabel['text'] = "6. Top Teams:"
            self.tBotLabel['text'] = '7. Bottom Teams:'
            self.perLabel['text'] = "8. Intervals:"
            self.jugadoresLabel['text'] = "9. Players"
            self.chEquipoLabel['text'] = "Extract Team Stats:"
            self.chAllLabel['text'] = "Extract Stats from All Games:"
            self.chRankLabel['text'] = "Extract Player Rankings:"
            self.minPartidosLabel['text'] = "Minimum Games:"
            self.confLabel['text'] = "Configuration Folder:"
            self.folderLabel['text'] = 'Output Folder:'
            self.button_conf.configure(text="Load Configuration")
            self.button_compare.configure(text="Extract Statistics")
            self.changeLang.configure(text="Cambiar Idioma")

    def load_conf(self):
        f = open(str(unicodedata.normalize('NFKD', self.text_conf.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[2:-3], "r")
        text = f.read()
        parts = text.split('\n')[:-1]
        for part in range(0, len(parts)):
            if len(parts[part]) > 0:
                parts[part] = parts[part].split('=')[1]

        self.text_season.configure(state="normal")
        self.text_season.delete('1.0',END)
        self.text_season.insert(END, parts[1])

        self.text_periodos.configure(state="normal")
        self.text_periodos.delete('1.0',END)
        self.text_periodos.insert(END, parts[7])

        self.text_division.configure(state="normal")
        self.text_division.delete('1.0',END)
        self.text_division.insert(END, parts[2])

        self.text_equiposBott.configure(state="normal")
        self.text_equiposBott.delete('1.0', END)
        self.text_equiposBott.insert(END, parts[6])

        self.text_equiposTop.configure(state="normal")
        self.text_equiposTop.delete('1.0', END)
        self.text_equiposTop.insert(END, parts[5])

        self.text_team.configure(state="normal")
        self.text_team.delete('1.0', END)
        self.text_team.insert(END,parts[0])

        self.text_jFirst.configure(state="normal")
        self.text_jFirst.delete('1.0', END)
        self.text_jFirst.insert(END,parts[3])

        self.text_jLast.configure(state="normal")
        self.text_jLast.delete('1.0', END)
        self.text_jLast.insert(END, parts[4])

        self.text_jugadores.configure(state="normal")
        self.text_jugadores.delete('1.0', END)
        self.text_jugadores.insert(END, parts[8])

        self.button_compare.configure(state="normal")

    def save_stats(self):
        self.text_chrome = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver'

        if self.checkAll.get() == 1:
            bAll = 1
        else:
            bAll = 0

        if self.checkEquipo.get() == 1:
            bTeam = 1
        else:
            bTeam = 0

        if self.checkProj.get() == 1:
            bProj = True
        else:
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

        if division == 'ENDESA' or division == 'LF':
            division = 'DIA'
        if division == 'ORO' or division.split(',')[0] == 'ORO':
            groupFeb = '1'
        elif division == 'DIA':
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
                    if groupSplit[1] == 'A':
                        groupFeb = '5'
                    else:
                        groupFeb = '57'
                else:
                    groupFeb = '5'
            elif groupSplit[0] == 'C': # C1 C2 C3
                if int(season) > 2018:
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
                    else:
                        groupFeb = '39'
                else:
                    groupFeb = '8'
        elif divSplit == 'LF2': # A B C
            if int(season) > 2019:
                if groupSplit == 'A':
                    groupFeb = '9'
                elif groupSplit == 'B':
                    groupFeb = '10'
                elif groupSplit == 'C':
                    groupFeb = '56'
            else:
                groupFeb = '9'

        sLang = self.language.get()

        html_doc = "http://competiciones.feb.es/Estadisticas/Calendario.aspx?g=" + groupFeb + "&t=" + season + "&"
        if iEndIn != 0:
            targetTeam = str(unicodedata.normalize('NFKD', self.text_team.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()[iBenIn:iEndIn]
            againstTeams1 = str(unicodedata.normalize('NFKD', self.text_equiposTop.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn].split(',')
            againstTeams2 = str(unicodedata.normalize('NFKD', self.text_equiposBott.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn].split(',')
            jorFirst = int(str(unicodedata.normalize('NFKD', self.text_jFirst.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn])
            jorLast = int(str(unicodedata.normalize('NFKD', self.text_jLast.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn])
            sDir = str(unicodedata.normalize('NFKD', self.text_folder.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            sPeriodos = str(unicodedata.normalize('NFKD', self.text_periodos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            sPlayers = str(unicodedata.normalize('NFKD', self.text_jugadores.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
            sMinGames = str(unicodedata.normalize('NFKD', self.text_minPartidos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')[iBenIn:iEndIn]
        else:
            targetTeam = str(unicodedata.normalize('NFKD', self.text_team.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').upper()
            againstTeams1 = str(unicodedata.normalize('NFKD', self.text_equiposTop.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').split(',')
            againstTeams2 = str(unicodedata.normalize('NFKD', self.text_equiposBott.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '').split(',')
            jorFirst = int(str(unicodedata.normalize('NFKD', self.text_jFirst.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', ''))
            jorLast = int(str(unicodedata.normalize('NFKD', self.text_jLast.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', ''))
            sDir = str(unicodedata.normalize('NFKD', self.text_folder.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            sPeriodos = str(unicodedata.normalize('NFKD', self.text_periodos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            sPlayers = str(unicodedata.normalize('NFKD', self.text_jugadores.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')
            sMinGames = str(unicodedata.normalize('NFKD', self.text_minPartidos.get("1.0", END)).encode('ascii', 'ignore')).replace('\n', '')

        if targetTeam == 'Liga' or targetTeam == 'LIGA':
            if division == 'ORO' or division == 'DIA' or division == 'ENDESA' or division == 'LF':
                GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division, sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, False)
            elif divSplit == 'ORO':
                GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, False)
            elif divSplit == 'PLATA':
                if bUnaFase == False:
                    GetAllLeagueBothPlata.extractStatisticsPlataAll(html_doc,targetTeam,season,jorFirst,jorLast,division.split(',')[1],division.split(',')[2],sDir,self.text_chrome,bTeam,sPlayers,bProj,division,'',sMinGames, sLang, False)
                    reload(GetAllLeagueBothPlata)
                else:
                    GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, '', 'Fase1', sMinGames, sLang, False)
            elif divSplit == 'EBA':
                GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, False)
            elif divSplit == 'LF2':
                GetAllLeagueCommon.extractStatisticsAllLeague(html_doc, 'Liga'+division.replace(',','-'), season, jorFirst, jorLast, division.split(',')[1], sDir, self.text_chrome, bTeam, sPlayers, bProj, division, '', sMinGames, sLang, False)
            reload(GetAllLeagueCommon)
        else:
            targetTeams = targetTeam.replace(' ', '').split(',')
            for k in range(0, len(targetTeams)):
                if sDir[-1] == '/':
                    sDir = sDir[:-1]
                if division == 'ORO' or division == 'DIA' or division == 'ENDESA' or division == 'LF':
                    GetAllGamesCommon.extractStatistics(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, division, sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, division, '', sMinGames, sLang)
                elif divSplit == 'ORO':
                    GetAllGamesCommon.extractStatistics(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, division.split(',')[1], sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, division, '', sMinGames, sLang)
                elif divSplit == 'PLATA':
                    if bUnaFase == False:
                        GetAllLeagueBothPlata.extractStatisticsPlata(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, division.split(',')[1], division.split(',')[2], sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, division, '', sMinGames, sLang)
                        reload(GetAllLeagueBothPlata)
                    else:
                        GetAllGamesCommon.extractStatistics(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, division.split(',')[1], sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, '', 'Fase1', sMinGames, sLang)
                elif divSplit == 'EBA':
                    GetAllGamesCommon.extractStatistics(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, division.split(',')[1], sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, division, '', sMinGames, sLang)
                elif divSplit == 'LF2':
                    GetAllGamesCommon.extractStatistics(html_doc, targetTeams[k], againstTeams1, againstTeams2, season, jorFirst, jorLast, division.split(',')[1], sDir, sPeriodos, self.text_chrome, bAll, bTeam, sPlayers, bProj, division, '', sMinGames, sLang)

            reload(GetAllGamesCommon)

#if __name__ == '__main__':
root = Tk()
root.title("BueStats (Adrià Arbués-Sangüesa, @arbues6)")
root.geometry("950x450")
root.columnconfigure(0, weight=1)
root.resizable(0, 0)

app = Application(root)
app.mainloop()
