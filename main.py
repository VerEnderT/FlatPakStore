import sys
import subprocess
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtMultimedia import QMediaContent


class qFenster(QMainWindow):   # QMainWindow oder Qwidget für menuebars
    def __init__(self):
        super().__init__()

        self.testbutton = "0"
        self.awalt = 0
        self.awneu = 0
        self.applist = []
        self.appisinstall = []
        self.coverpm = []
        self.videoadr = []
        self.beschreibung = []
        self.appcom = []
        self.yt1 = "http://www.youtube.com/embed/"
        self.yt2 = "?autoplay=1&showinfo=0&loop=1&playlist="
        self.fileurl = self.yt1 + "ef9vYcuEDL4" + self.yt2 + "ef9vYcuEDL4"

# ------------- Appdaten einlesen ------------------------------------------------------------
        cpath = os.path.dirname(os.path.abspath(__file__))
        file1 = open(cpath + "/appdaten.data", 'r')
        count = 0
        while True:
            count += 1
            line = file1.readline()
            if not line:
                break

            self.applist.append(line[0: len(line)-1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.coverpm.append(cpath + "/" + line[0:len(line)-1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.videoadr.append(line[0:len(line)-1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.beschreibung.append(line[0:len(line)-1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.appcom.append(line[0:len(line)-1])
            print("Line{}: {}".format(count, line.strip()))

            s = subprocess.call(['flatpak', 'info', line[0:len(line)-1]])
            self.appisinstall.append(s)
            if s == 0:
                print("ist installiert!")
            else:
                print("ist nicht installiert")
            count += 1
        file1.close()

# --------------------------------------------------------------------------------------------

        # Hintergrund
        image = QPixmap(cpath + "/background.gif")
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
        image = QPixmap(cpath + "/VerLinuxT-logo.png")
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
        self.webview.move(185, 20)
        self.webview.settings()

        # Cover
        image1 = QPixmap(cpath + "/SuperTuxKart.jpg")
        self.cover = QLabel(self)
        self.cover.setPixmap(image1)
        self.cover.setFixedWidth(331)
        self.cover.setFixedHeight(445)
        self.cover.setScaledContents(True)
        self.cover.move(620, 25)

        # Label Spielname
        self.gamename = QTextEdit(self)
        self.gamename.setReadOnly(True)
        self.gamename.setMinimumWidth(400)
        self.gamename.setMinimumHeight(100)
        self.gamename.setText("Super TuX Kart")
        self.gamename.move(185, 240)
        self.gamename.setStyleSheet(
            "background: rgba(0, 0, 0, 0);" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        # Beschreibung
        self.btext = QTextEdit(self)
        self.btext.setReadOnly(True)
        self.btext.setMinimumWidth(430)
        self.btext.setMinimumHeight(280)
        self.btext.setText(self.beschreibung[0])
        self.btext.move(170, 300)
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
            "background: #0eff2a;" +
            "border-radius: 25px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )
        if self.appisinstall[self.awneu] == 0:
            self.btn_install.hide()
        else:
            self.btn_install.show()

        # De-Installieren Button
        self.btn_deinstall = QPushButton(self)
        self.btn_deinstall.setText("De-Installieren")
        self.btn_deinstall.move(700, 480)
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
        if self.appisinstall[self.awneu] == 1:
            self.btn_deinstall.hide()
        else:
            self.btn_deinstall.show()

        # Starten Button
        self.btn_start = QPushButton(self)
        self.btn_start.setText("Starten")
        self.btn_start.move(650, 520)
        self.btn_start.setObjectName("2")
        self.btn_start.clicked.connect(self.starten)
        self.btn_start.setMinimumWidth(300)
        self.btn_start.setMinimumHeight(50)
        self.btn_start.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #0eff2a;" +
            "border-radius: 25px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )
        if self.appisinstall[self.awneu] == 1:
            self.btn_start.hide()
        else:
            self.btn_start.show()

        # Applist Buttons
        self.count = 0
        for i in self.applist:
            self.gamebtn = QPushButton(self)
            self.gamebtn.setText(self.applist[self.count])
            self.gamebtn.move(50, 150 + self.count * 35)
            self.aobjectname = str(self.count)
            self.gamebtn.setObjectName(self.aobjectname)
            self.count = self.count + 1
            self.gamebtn.clicked.connect(self.awknopf)
            print(i)

        # Label Status
        self.stAnzeige = QLabel(self)
        self.stAnzeige.setMinimumWidth(800)
        self.stAnzeige.setMinimumHeight(100)
        self.stAnzeige.setText("Es wird Installiert ...")
        self.stAnzeige.move(100, 240)
        self.stAnzeige.hide()
        self.stAnzeige.setAlignment(Qt.AlignCenter)
        self.stAnzeige.setStyleSheet(
            "background: rgba(0, 200, 0, 150);" +
            "font-size: 68px;" +
            "color: #00e500;" +
            "border: 4px solid '#f0f0f0';" +
            "border-radius: 50px;" +
            "color: #ffffff;"
        )

# ---------------------------------------------------------------------------------------------

        # konfiguration Fenster und zeigen
        self.setGeometry(0 + 50, 50, 1000, 600)  # x-pos, y-pos, breite, höhe
        self.setWindowTitle("VerFlatpakT")  # Title name
        self.setWindowIcon(QIcon(cpath + "/VerLinuxT-logo.png"))  # Datei für das logo des programms
        self.setFixedSize(1000, 600)  # fixe größe einstellen
        self.show()  # Fenster anzeigen

    def awknopf(self):
        e = self.sender()
        print(e.objectName())
        self.awalt = self.awneu
        self.awneu = int(e.objectName())
        self.gamechange()

    def gamechange(self):
        s = subprocess.call(['flatpak', 'info', self.appcom[self.awneu]])
        if s == 0:
            self.appisinstall[self.awneu] = 0
            print("ist installiert!")
        else:
            self.appisinstall[self.awneu] = 1
            print("ist nicht installiert")
        self.gamename.setText(self.applist[self.awneu])
        self.cover.setPixmap(QPixmap(self.coverpm[self.awneu]))
        self.btext.setText(self.beschreibung[self.awneu])
        self.fileurl = self.yt1 + self.videoadr[self.awneu] + self.yt2 + self.videoadr[self.awneu]
        self.webview.setUrl(QUrl(self.fileurl))
        if self.appisinstall[self.awneu] == 0:
            self.btn_install.hide()
            self.btn_deinstall.show()
            self.btn_start.show()
        else:
            self.btn_install.show()
            self.btn_start.hide()
            self.btn_deinstall.hide()

    def update_btn(self):
        s = subprocess.call(['flatpak', 'info', self.appcom[self.awneu]])
        if s == 0:
            self.appisinstall[self.awneu] = 0
            print("ist installiert!")
        else:
            self.appisinstall[self.awneu] = 1
            print("ist nicht installiert")
        if self.appisinstall[self.awneu] == 0:
            self.btn_install.hide()
            self.btn_deinstall.show()
            self.btn_start.show()
        else:
            self.btn_install.show()
            self.btn_start.hide()
            self.btn_deinstall.hide()

    def installieren(self):
        self.stAnzeige.show()
        self.stAnzeige.setText("Es wird installiert ...")
        try:
            s = subprocess.Popen(['flatpak', 'install', self.appcom[self.awneu], '-y'])
            print("wird installiert" + s)
        finally:
            print("missed")

        s = subprocess.call(['flatpak', 'info', self.appcom[self.awneu]])
        if s == 0:
            self.appisinstall[self.awneu] = 0
            print("ist installiert!")
        else:
            self.appisinstall[self.awneu] = 1
            print("ist nicht installiert")
        self.gamechange()
        self.stAnzeige.hide()

    def deinstallieren(self):
        self.stAnzeige.setText("Es wird deinstalliert...")
        self.stAnzeige.show()
        s = subprocess.Popen(['flatpak', 'uninstall', self.appcom[self.awneu], '-y'])
        print("wird deinstalliert")
        print(s)

        s = subprocess.call(['flatpak', 'info', self.appcom[self.awneu]])
        if s == 0:
            self.appisinstall[self.awneu] = 0
            print("ist installiert!")
        else:
            self.appisinstall[self.awneu] = 1
            print("ist nicht installiert")
        self.gamechange()
        self.stAnzeige.hide()

    def starten(self):
        try:
            s = subprocess.Popen(['flatpak', 'run', self.appcom[self.awneu], '-y'])
            print("wird gestartet")
            print(s)
        finally:
            print("missed")
            self.exit()

        s = subprocess.call(['flatpak', 'info', self.appcom[self.awneu]])

        if s == 0:
            self.appisinstall[self.awneu] = 0
            print("ist installiert!")
        else:
            self.appisinstall[self.awneu] = 1
            print("ist nicht installiert")
        self.gamechange()

    def timerEvent(self, e):
        if self.i >= 100:
            # self.timer.stop()
            self.i = 0
            self.update_btn()
        self.i = self.i + 1
        self.stimes.setValue(int(self.i))

    def timerstartem(self):
        self.i = 0
        self.timer.start(1000, self)


app = QApplication(sys.argv)
w = qFenster()
w.show()
sys.exit(app.exec())
