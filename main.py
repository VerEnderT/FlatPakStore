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
        self.count = 0
        self.btn_app = QPushButton(self)
        self.btn_cat = QPushButton(self)
        self.aobjectname = ""
        self.cobjectname = ""
        self.button = []
        self.appcategorie = []
        self.appcpath = []
        self.apppage = 0
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
        self.yt2 = "?autoplay=1&showinfo=0&loop=1&playlist="
        self.fileurl = self.yt1 + "ef9vYcuEDL4" + self.yt2 + "ef9vYcuEDL4"
        cpath = os.path.dirname(os.path.abspath(__file__))
        self.catseinlesen()
        self.appseinlesen()

# ---------------- AppButton ---------------------------------------------------

        self.btn_app0 = QPushButton(self)
        self.btn_app1 = QPushButton(self)
        self.btn_app2 = QPushButton(self)
        self.btn_app3 = QPushButton(self)
        self.btn_app4 = QPushButton(self)
        self.btn_app5 = QPushButton(self)
        self.btn_app6 = QPushButton(self)
        self.btn_app7 = QPushButton(self)
        self.btn_app8 = QPushButton(self)
        self.btn_app9 = QPushButton(self)

# ---------------------------------------------------------------------------

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
        self.btext.setMinimumHeight(250)
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
            "background: #0eff2a;" +
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
            "background: #0eff2a;" +
            "border-radius: 25px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        self.btn_start.hide()
        self.appbtnmake()
        self.catbtnmake()

        # Label Status
        self.stAnzeige = QLabel(self)
        self.stAnzeige.setMinimumWidth(150)
        self.stAnzeige.setMinimumHeight(50)
        self.stAnzeige.setText(self.appcategorie[self.appcselect])
        self.stAnzeige.move(20, 50)
        # self.stAnzeige.hide()
        self.stAnzeige.setAlignment(Qt.AlignCenter)
        self.stAnzeige.setStyleSheet(
            "background: rgba(0, 200, 0, 150);" +
            "font-size: 24px;" +
            "color: #00e500;" +
            "border: 4px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
        )
        self.appchange()

# ---------------------------------------------------------------------------------------------

        # konfiguration Fenster und zeigen
        self.setGeometry(0 + 50, 50, 1000, 600)  # x-pos, y-pos, breite, höhe
        self.setWindowTitle("VerFlatpakT")  # Title name
        self.setWindowIcon(QIcon(cpath + "/VerLinuxT-logo.png"))  # Datei für das logo des programms
        self.setFixedSize(1000, 600)  # fixe größe einstellen
        self.show()  # Fenster anzeigen

    def awknopf(self):
        e = self.sender()
        # print(e.objectName())
        self.awalt = self.awneu
        self.awneu = int(e.objectName())
        self.appchange()

    def cwknopf(self):
        e = self.sender()
        print("knopf " + e.objectName())
        self.appcselect = int(e.objectName())
        text = self.appcategorie[self.appcselect]
        self.stAnzeige.setText(text)
        self.btn_app.setUpdatesEnabled(True)
        self.btn_app0.close()
        self.btn_app1.close()
        self.btn_app2.close()
        self.btn_app3.close()
        self.btn_app4.close()
        self.btn_app5.close()
        self.btn_app6.close()
        self.btn_app7.close()
        self.btn_app8.close()
        self.btn_app9.close()
        self.awneu = 0
        self.appseinlesen()
        self.appbtnmake()
        self.appchange()

    def appchange(self):
        self.appname.setText(self.applist[self.awneu])
        self.cover.setPixmap(QPixmap(self.coverpm[self.awneu]))
        self.btext.setText(self.beschreibung[self.awneu])
        self.fileurl = self.yt1 + self.videoadr[self.awneu] + self.yt2 + self.videoadr[self.awneu]
        self.webview.setUrl(QUrl(self.fileurl))
        self.update_btn()

    def update_btn(self):
        s = subprocess.Popen(['flatpak', 'info', self.appcom[self.awneu]],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = s.communicate()
        if stderr.decode('utf-8') == "":
            self.btn_install.hide()
            self.btn_deinstall.show()
            self.btn_start.show()
            # print("ist installiert!")
        else:
            self.btn_install.show()
            self.btn_start.hide()
            self.btn_deinstall.hide()

    # noinspection PyUnusedLocal
    def installieren(self):
        self.stAnzeige.setText("es wird installiert")
        s = subprocess.Popen(['flatpak', 'install', self.appcom[self.awneu], '-y'])
        # stdout, stderr = s.communicate()
        # print(stdout.decode('utf-8'))
        print("wird installiert")
        self.update_btn()

    def deinstallieren(self):
        self.stAnzeige.setText("Es wird deinstalliert...")
        self.stAnzeige.show()
        s = subprocess.run(['flatpak', 'uninstall', self.appcom[self.awneu], '-y'])
        # stdout, stderr =s.communicate()
        print("wird de-installiert")
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
        if self.i >= 100:
            # self.timer.stop()
            self.i = 0
            # self.update_btn()
        self.i = self.i + 1
        self.stimes.setValue(int(self.i))

    def timerstartem(self):
        self.i = 0
        self.timer.start(1000, self)

# ------------- Appdaten einlesen ------------------------------------------------------------
    def appseinlesen(self):
        cpath = os.path.dirname(os.path.abspath(__file__))
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
            self.coverpm.append(cpath + line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.videoadr.append(line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.beschreibung.append(line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.appcom.append(line[0:len(line) - 1])
            print("Line{}: {}".format(count, line.strip()))

            count += 1
        self.appmenge = count - 1
        file1.close()

        # Applist Buttons
    def appbtn_make(self):
        self.count = 0
        for i in self.applist:
            self.btn_app = QPushButton(self)
            self.aobjectname = str(self.count)
            self.btn_app.setUpdatesEnabled(True)
            self.btn_app.setObjectName(self.aobjectname)
            self.btn_app.setText(self.applist[self.count])
            self.btn_app.clicked.connect(self.awknopf)
            self.btn_app.move(50, 130 + self.count * 35)
            self.count = self.count + 1
            print(i)

    def appbtnmake(self):
        print(self.appcategorie[self.appcselect])

        self.btn_app0 = QPushButton(self)
        self.btn_app0.move(50, 130 + 0 * 35)
        self.btn_app0.setObjectName("0")
        self.btn_app0.clicked.connect(self.awknopf)
        self.btn_app1 = QPushButton(self)
        self.btn_app1.move(50, 130 + 1 * 35)
        self.btn_app1.setObjectName("1")
        self.btn_app1.clicked.connect(self.awknopf)
        self.btn_app2 = QPushButton(self)
        self.btn_app2.move(50, 130 + 2 * 35)
        self.btn_app2.setObjectName("2")
        self.btn_app2.clicked.connect(self.awknopf)
        self.btn_app3 = QPushButton(self)
        self.btn_app3.move(50, 130 + 3 * 35)
        self.btn_app3.setObjectName("3")
        self.btn_app3.clicked.connect(self.awknopf)
        self.btn_app4 = QPushButton(self)
        self.btn_app4.move(50, 130 + 4 * 35)
        self.btn_app4.setObjectName("4")
        self.btn_app4.clicked.connect(self.awknopf)
        self.btn_app5 = QPushButton(self)
        self.btn_app5.move(50, 130 + 5 * 35)
        self.btn_app5.setObjectName("5")
        self.btn_app5.clicked.connect(self.awknopf)
        self.btn_app6 = QPushButton(self)
        self.btn_app6.move(50, 130 + 6 * 35)
        self.btn_app6.setObjectName("6")
        self.btn_app6.clicked.connect(self.awknopf)
        self.btn_app7 = QPushButton(self)
        self.btn_app7.move(50, 130 + 7 * 35)
        self.btn_app7.setObjectName("7")
        self.btn_app7.clicked.connect(self.awknopf)
        self.btn_app8 = QPushButton(self)
        self.btn_app8.move(50, 130 + 8 * 35)
        self.btn_app8.setObjectName("8")
        self.btn_app8.clicked.connect(self.awknopf)
        self.btn_app9 = QPushButton(self)
        self.btn_app9.move(50, 130 + 9 * 35)
        self.btn_app9.setObjectName("9")
        self.btn_app9.clicked.connect(self.awknopf)

# ----- Liste neu beschreiben -------------------------
        self.btn_app0.setText(self.applist[0])
        self.btn_app0.show()

        if self.appmenge >= self.apppage * 10 + 1:
            self.btn_app1.setText(self.applist[1])
            self.btn_app1.show()
            print("an" + self.applist[1])
        else:
            self.btn_app1.hide()

        if self.appmenge >= self.apppage * 10 + 2:
            self.btn_app2.setText(self.applist[2])
            self.btn_app2.show()
            print("an")
        else:
            self.btn_app2.hide()

        if self.appmenge >= self.apppage * 10 + 3:
            self.btn_app3.setText(self.applist[3])
            self.btn_app3.show()
            print("an")
        else:
            self.btn_app3.hide()

        if self.appmenge >= self.apppage * 10 + 4:
            self.btn_app4.setText(self.applist[4])
            self.btn_app4.show()
            print("an")
        else:
            self.btn_app4.hide()

        if self.appmenge >= self.apppage * 10 + 5:
            self.btn_app5.setText(self.applist[5])
            self.btn_app5.show()
            print("an")
        else:
            self.btn_app5.hide()

        if self.appmenge >= self.apppage * 10 + 6:
            self.btn_app6.setText(self.applist[6])
            self.btn_app6.show()
            print("an")
        else:
            self.btn_app6.hide()

        if self.appmenge >= self.apppage * 10 + 7:
            print(str(self.appmenge)+"-"+str(self.apppage * 10 + 7))
            self.btn_app7.setText(self.applist[7])
            self.btn_app7.show()
            print("an")
        else:
            self.btn_app7.hide()

        if self.appmenge >= self.apppage * 10 + 8:
            print(str(self.appmenge)+"-"+str(self.apppage * 10 + 8))
            self.btn_app8.setText(self.applist[8])
            self.btn_app8.show()
            print("an")
        else:
            self.btn_app8.hide()

        if self.appmenge >= self.apppage * 10 + 9:
            print("wtf" + str(self.appmenge)+"-"+str(self.apppage * 10 + 9))
            self.btn_app9.setText(self.applist[9])
            self.btn_app9.show()
            print("an")
        else:
            self.btn_app9.hide()

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
            self.btn_cat.setText(self.appcategorie[self.count])
            self.btn_cat.move(10 + self.count * 100, 5)
            self.cobjectname = str(self.count)
            self.btn_cat.setObjectName(self.cobjectname)
            self.btn_cat.clicked.connect(self.cwknopf)
            print("catcount" + str(self.count) + " - " + i)
            self.count = self.count + 1
# --------------------------------------------------------------------------------------------


app = QApplication(sys.argv)
w = qFenster()
w.show()
sys.exit(app.exec())
