import sys
import subprocess
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class qFenster(QMainWindow):   # QMainWindow oder Qwidget für menuebars
    def __init__(self):
        super().__init__()

        self.dein = " "
        self.ii = 0
        self.appproc = ""
        self.apppid = ""
        self.svc = ""
        self.count = 0
        self.btn_app = QPushButton(self)
        self.btn_cat = QPushButton(self)
        self.aobjectname = ""
        self.cobjectname = ""
        self.button = []
        self.appcategorie = []
        self.appcpath = []
        self.appcselect = 0
        self.appmenge = 0
        self.testbutton = "0"
        self.awalt = 0
        self.awneu = 0
        self.applist = []
        self.coverpm = []
        self.videoadr = []
        self.beschreibung = []
        self.appcom = []
        self.yt1 = "http://www.youtube.com/embed/"
        self.yt2 = "?autoplay=1&allowfullscreeen=1&showinfo=0&loop=1&playlist="
        self.fileurl = self.yt1 + "ef9vYcuEDL4" + self.yt2 + "ef9vYcuEDL4"
        self.cpath = os.path.dirname(os.path.abspath(__file__))
        self.catseinlesen()
        self.appseinlesen()
# ---------------------------------------------------------------------------

        # Hintergrund
        image = QPixmap(self.cpath + "/background.gif")
        background = QLabel(self)
        background.setPixmap(image)
        background.setFixedWidth(1000)
        background.setFixedHeight(700)
        background.setScaledContents(True)
        background.move(0, 0)

        # fortschritsbalken
        self.stimes = QProgressBar(self)
        self.timer = QBasicTimer()
        self.i = 0
        self.timer.start(100, self)
        self.stimes.move(20, 20)
        self.stimes.hide()

        # logo
        image = QPixmap(self.cpath + "/VerLinuxT-logo.png")
        logo = QLabel(self)
        logo.setPixmap(image)
        logo.setFixedWidth(300)
        logo.setFixedHeight(300)
        logo.setScaledContents(True)
        logo.move(-20, 450)

        # Youtube Video
        self.webview = QWebEngineView(self)
        self.webview.setUrl(QUrl(self.fileurl))
        self.webview.setMinimumWidth(400)
        self.webview.setMinimumHeight(225)
        self.webview.move(185, 50)
        self.webview.settings()

        # Cover
        image1 = QPixmap(self.coverpm[self.awneu])
        self.cover = QLabel(self)
        self.cover.setPixmap(image1)
        self.cover.setFixedWidth(360)
        self.cover.setFixedHeight(445)
        self.cover.setScaledContents(True)
        self.cover.move(620, 50)
        self.cover.setAlignment(Qt.AlignCenter)
        self.cover.setStyleSheet(
            "background: rgba(0, 0, 0, 0);"
        )

        # Label Spielname
        self.appname = QTextEdit(self)
        self.appname.setReadOnly(True)
        self.appname.setMinimumWidth(400)
        self.appname.setMinimumHeight(100)
        self.appname.setText("Super TuX Kart")
        self.appname.move(185, 270)
        self.appname.setStyleSheet(
            "background: rgba(0, 0, 0, 0);" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        # Beschreibung
        self.btext = QTextEdit(self)
        self.btext.setReadOnly(True)
        self.btext.setMinimumWidth(430)
        self.btext.setMinimumHeight(240)
        self.btext.setText(self.beschreibung[0])
        self.btext.move(170, 330)
        self.btext.setStyleSheet("background: rgba(0, 0, 0, 140); color: #ffffff;")

        # Installieren Button
        self.btn_install = QPushButton(self)
        self.btn_install.setText("Installieren")
        self.btn_install.move(650, 520)
        self.btn_install.setObjectName("2")
        self.btn_install.clicked.connect(self.installieren)
        self.btn_install.setMinimumWidth(300)
        self.btn_install.setMinimumHeight(50)
        self.btn_install.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: rgba(0, 200, 0, 255);" +
            "border-radius: 25px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )
        self.btn_install.hide()

        # De-Installieren Button
        self.btn_deinstall = QPushButton(self)
        self.btn_deinstall.setText("De-Installieren")
        self.btn_deinstall.move(700, 500)
        self.btn_deinstall.setObjectName("2")
        self.btn_deinstall.clicked.connect(self.deinstallieren)
        self.btn_deinstall.setMinimumWidth(200)
        self.btn_deinstall.setMinimumHeight(30)
        self.btn_deinstall.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #aa0000;" +
            "border-radius: 15px;" +
            "font-size: 20px;" +
            "color: #ffffff;"
        )
        self.btn_deinstall.hide()

        # Starten Button
        self.btn_start = QPushButton(self)
        self.btn_start.setText("Starten")
        self.btn_start.move(650, 540)
        self.btn_start.setObjectName("2")
        self.btn_start.clicked.connect(self.starten)
        self.btn_start.setMinimumWidth(300)
        self.btn_start.setMinimumHeight(50)
        self.btn_start.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: rgba(0, 200, 0, 255);" +
            "border-radius: 25px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        self.btn_start.hide()

        # Label Status
        self.stAnzeige = QLabel(self)
        self.stAnzeige.setFixedSize(150, 40)
        self.stAnzeige.setText(self.appcategorie[self.appcselect])
        self.stAnzeige.move(20, 50)
        self.stAnzeige.setAlignment(Qt.AlignCenter)
        self.stAnzeige.setStyleSheet(
            "background: rgba(0, 200, 0, 150);" +
            "font-size: 24px;" +
            "color: #00e500;" +
            "border: 4px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
        )

        self.status = QLabel(self)
        self.status.move(200, 575)
        self.status.setText("Status: keine aktivitäten")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("background: rgba(0, 0, 0, 200);")
        self.status.setFixedSize(400, 20)

        self.statusrun = QLabel(self)
        self.statusrun.move(200, 580)
        self.statusrun.setText("")
        self.statusrun.setAlignment(Qt.AlignCenter)
        self.statusrun.setAutoFillBackground(True)
        self.statusrun.setStyleSheet("background: rgba(0, 200, 0, 120);")
        self.statusrun.setFixedSize(50, 10)
        self.statusrun.hide()

        self.btnlist = []
        self.scroll = QScrollArea(self)
        self.scroll.setFixedSize(165, 370)
        self.scroll.move(2, 120)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet("background: rgba(50, 50, 50, 40);color: #ffffff;")
        self.scrollcontent = QWidget(self.scroll)
        self.scrolllayout = QVBoxLayout(self.scrollcontent)
        self.scrollcontent.setLayout(self.scrolllayout)

        # Label Status
        self.appselstatus = QLabel(self)
        self.appselstatus.setFixedSize(170, 20)
        self.appselstatus.move(5, 95)
        self.appselstatus.setStyleSheet("background: rgba(50, 50, 50, 40);color: #ffffff;")
        self.appselstatus.setAlignment(Qt.AlignCenter)

        self.catbtnmake()
        self.appchange()
        self.newcatchange()
        self.btnselect()
# ---------------------------------------------------------------------------------------------

        # konfiguration Fenster und zeigen
        self.setGeometry(0 + 50, 50, 1000, 600)  # x-pos, y-pos, breite, höhe
        self.setWindowTitle("VerFlatpakT")  # Title name
        self.setWindowIcon(QIcon(self.cpath + "/VerLinuxT-logo.png"))  # Datei für das logo des programms
        self.setFixedSize(1000, 600)  # fixe größe einstellen
        self.show()  # Fenster anzeigen

    def awknopf(self):
        e = self.sender()
        self.awalt = self.awneu
        self.awneu = int(e.objectName())
        self.appchange()
        self.btnselect()

    def btnselect(self):
        for i in range(self.appmenge+1):
            self.btnlist[i].setStyleSheet("background: rgba(50, 50, 50, 40);color: #ffffff;")
        self.btnlist[self.awneu].setStyleSheet("background: rgba(0, 100, 0, 255);color: #ffffff;")
        self.appselstatus.setText("App " + str(self.awneu + 1) + " von " + str(self.appmenge + 1) + " Apps")

    def cwknopf(self):
        e = self.sender()
        print("knopf " + e.objectName())
        self.appcselect = int(e.objectName())
        text = self.appcategorie[self.appcselect]
        self.stAnzeige.setText(text)
        self.awneu = 0
        self.appseinlesen()
        self.appchange()
        self.newcatchange()
        self.btnselect()

    def newcatchange(self):
        for i in self.btnlist:
            i.close()
            self.scrolllayout.removeWidget(i)
        self.scrollcontent.close()

        self.btnlist = []
        self.scrollcontent = QWidget(self.scroll)
        self.scrollcontent.setLayout(self.scrolllayout)
        for i in range(0, self.appmenge + 1):
            text = self.applist[i]
            # object = str(i)
            self.btnlist.append(QPushButton(text))
            self.scrolllayout.addWidget(self.btnlist[i])
            self.btnlist[i].setObjectName(str(i))
            self.btnlist[i].setMinimumHeight(30)
            self.btnlist[i].setStyleSheet("background: rgba(50, 50, 50, 40);color: #ffffff;")
            self.btnlist[i].clicked.connect(self.awknopf)

        self.scroll.setWidget(self.scrollcontent)
        self.scrollcontent.setFixedWidth(150)

    def appchange(self):
        self.appname.setText(self.applist[self.awneu])
        file = self.cpath + "/cover/" + self.coverpm[self.awneu]
        self.cover.setPixmap(QPixmap(file))
        self.btext.setText(self.beschreibung[self.awneu])
        self.fileurl = self.yt1 + self.videoadr[self.awneu] + self.yt2 + self.videoadr[self.awneu]
        self.webview.setUrl(QUrl(self.fileurl))
        self.update_btn()

    def update_btn(self):
        if self.appproc != "" and self.apppid != "":
            i = str(self.apppid)
            service_check = subprocess.call(["ps", "-c", i])
            if service_check == 0:
                # programminstallation läuft noch
                self.status.setText("Status: " + self.appproc + " wird" + self.dein + "installiert")
                self.btn_install.setDisabled(True)
                self.btn_install.setText("Bitte warten")
                self.btn_deinstall.setDisabled(True)
                self.btn_deinstall.setText("beschäftigt")
                self.btn_start.setDisabled(True)
                self.btn_start.setText("Bitte warten")
                self.statusrun.show()

            else:
                # programm de/installation wurde beendet
                self.appproc = ""
                self.apppid = ""
                self.btn_install.setDisabled(False)
                self.btn_install.setText("Installieren")
                self.btn_deinstall.setDisabled(False)
                self.btn_deinstall.setText("De-Installierne")
                self.btn_start.setDisabled(False)
                self.btn_start.setText("Starten")

        else:
            self.statusrun.hide()
            self.status.setText("Status: keine aktivitäten")

        s = subprocess.Popen(['flatpak', 'info', self.appcom[self.awneu]],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = s.communicate()
        if stderr.decode('utf-8') == "":
            self.btn_install.hide()
            self.btn_deinstall.show()
            self.btn_start.show()
        else:
            self.btn_install.show()
            self.btn_start.hide()
            self.btn_deinstall.hide()

    # noinspection PyUnusedLocal
    def installieren(self):
        self.status.setText("es wird installiert")
        self.btn_install.setDisabled(True)
        prozess1 = subprocess.Popen('flatpak install ' + self.appcom[self.awneu] + ' -y', shell=True)
        self.svc = str(int(prozess1.pid)+1)
        self.appproc = self.applist[self.awneu]
        self.apppid = self.svc
        self.dein = " "
        self.update_btn()

    # noinspection PyUnusedLocal
    def deinstallieren(self):
        self.status.setText("Es wird deinstalliert...")
        self.stAnzeige.show()
        prozess1 = subprocess.Popen(['flatpak', 'uninstall', self.appcom[self.awneu], '-y'])
        self.svc = str(int(prozess1.pid)+1)
        self.appproc = self.applist[self.awneu]
        self.apppid = self.svc
        self.dein = " de"
        self.update_btn()

    def starten(self):
        try:
            s = subprocess.Popen(['flatpak', 'run', self.appcom[self.awneu], '-y'])
            print("wird gestartet")
            print(s)
        finally:
            print("missed")

        self.update_btn()

    def timerEvent(self, e):
        if self.i >= 10:
            # self.timer.stop()
            self.i = 0
            # self.status.setText(self.s.stdout)
            self.update_btn()
        self.i = self.i + 1
        self.ii = self.ii + 1
        if self.ii >= 100:
            self.ii = 0
        if self.ii <= 50:
            self.statusrun.move(200 + self.ii * 7, 580)
        else:
            self.statusrun.move(900 - self.ii * 7, 580)
        self.stimes.setValue(int(self.i))

    def timerstartem(self):
        self.i = 0
        self.timer.start(1000, self)

# ------------- Appdaten einlesen ------------------------------------------------------------
    def appseinlesen(self):
        catpath = self.appcpath[self.appcselect]
        print(catpath)
        file1 = open(catpath, 'r')
        count = 0
        self.applist.clear()
        self.coverpm.clear()
        self.videoadr.clear()
        self.beschreibung.clear()
        self.appcom.clear()
        while True:
            line = file1.readline()
            if not line:
                break

            self.applist.append(line[0: len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.coverpm.append(line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.videoadr.append(line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            line1 = line.replace("QE", "\n")
            self.beschreibung.append(line1[0:len(line1) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.appcom.append(line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))

            count += 1
        self.appmenge = count - 1
        file1.close()

    def catseinlesen(self):
        cpath = os.path.dirname(os.path.abspath(__file__))
        print("cat " + cpath)
        file1 = open(cpath + "/data/categorie.data", 'r')
        count = 0
        while True:
            line = file1.readline()
            if not line:
                break

            self.appcategorie.append(line[0: len(line) - 1])
            print("sLine{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.appcpath.append(cpath + "/data/" + line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            print(self.appcpath[count])
            count += 1
        file1.close()

    # Applist Buttons
    def catbtnmake(self):
        self.count = 0
        for i in self.appcategorie:
            self.btn_cat = QPushButton(self)
            self.btn_cat.setText(i)
            self.btn_cat.move(10 + self.count * 92, 5)
            self.btn_cat.setMaximumWidth(90)
            self.cobjectname = str(self.count)
            self.btn_cat.setObjectName(self.cobjectname)
            self.btn_cat.setStyleSheet("background: rgba(50, 50, 50, 40);color: #ffffff;")
            self.btn_cat.clicked.connect(self.cwknopf)
            # print("catcount" + str(self.count) + " - " + i)
            self.count = self.count + 1
# --------------------------------------------------------------------------------------------


app = QApplication(sys.argv)
w = qFenster()
w.show()
sys.exit(app.exec())
