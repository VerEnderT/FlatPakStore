import sys
# import subprocess
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
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
        self.cpath = os.path.dirname(os.path.abspath(__file__))
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

        # btn_addApp
        self.btn_addApp = QPushButton(self)
        self.btn_addApp.setMaximumWidth(20)
        self.btn_addApp.setMaximumHeight(20)
        self.btn_addApp.setText("+")
        self.btn_addApp.clicked.connect(self.addapp)
        # self.btn_addApp.setIcon(self.style().standardIcon(getattr(QStyle, "SP_FileDialogNewFolder")))
        self.btn_addApp.move(5, 107)
        self.btn_addApp.setStyleSheet("font-size: 20px;padding-top: -5px;")

        # btn_addcat
        self.btn_addcat = QPushButton(self)
        self.btn_addcat.setMaximumWidth(20)
        self.btn_addcat.setMaximumHeight(20)
        self.btn_addcat.setText("+")
        # self.btn_addApp.setIcon(self.style().standardIcon(getattr(QStyle, "SP_FileDialogNewFolder")))
        self.btn_addcat.move(10, 37)
        self.btn_addcat.setStyleSheet("font-size: 20px;padding-top: -5px;")

        # Label Appname
        self.appname = QTextEdit(self)
        self.appname.setReadOnly(False)
        self.appname.setMinimumWidth(400)
        self.appname.setMinimumHeight(100)
        self.appname.setText("Super TuX Kart")
        self.appname.textChanged.connect(self.appnamechange)
        self.appname.move(185, 270)
        self.appname.setStyleSheet(
            "background: rgba(0, 0, 0, 0);" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        # Label Appcomname
        self.appcomname = QTextEdit(self)
        self.appcomname.setReadOnly(False)
        self.appcomname.setFixedWidth(300)
        self.appcomname.setFixedHeight(30)
        self.appcomname.setText(self.appcom[0])
        self.appcomname.textChanged.connect(self.appcomnamechange)
        self.appcomname.move(660, 500)
        self.appcomname.setStyleSheet(
            "background: rgba(100, 100, 0, 100);" +
            "font-size: 15px;" +
            "color: #ffffff;"
        )

        # Beschreibung
        self.btext = QTextEdit(self)
        self.btext.setReadOnly(False)
        self.btext.setMinimumWidth(430)
        self.btext.setMinimumHeight(250)
        self.btext.setText(self.beschreibung[0])
        self.btext.textChanged.connect(self.beschreibungchange)
        self.btext.move(170, 330)
        self.btext.setStyleSheet("background: rgba(0, 0, 0, 140); color: #ffffff;")

        # Speichern
        self.btn_speichern = QPushButton(self)
        self.btn_speichern.setText("Speicherm")
        self.btn_speichern.move(650, 540)
        self.btn_speichern.setObjectName("2")
        self.btn_speichern.clicked.connect(self.speichern)
        self.btn_speichern.setMinimumWidth(300)
        self.btn_speichern.setMinimumHeight(50)
        self.btn_speichern.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #0eff2a;" +
            "border-radius: 25px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        # Youtube edit Button
        self.btn_youtube = QPushButton(self)
        self.btn_youtube.setText("ändern")
        self.btn_youtube.move(300, 50)
        self.btn_youtube.setObjectName("2")
        self.btn_youtube.clicked.connect(self.youtubeedit)
        self.btn_youtube.setMinimumWidth(150)
        self.btn_youtube.setMinimumHeight(30)
        self.btn_youtube.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #aa0000;" +
            "border-radius: 15px;" +
            "font-size: 20px;" +
            "color: #ffffff;"
        )

        # Cover ändern
        self.btn_cedit = QPushButton(self)
        self.btn_cedit.setText("ämderm")
        self.btn_cedit.move(725, 50)
        self.btn_cedit.setObjectName("2")
        self.btn_cedit.clicked.connect(self.coveredit)
        self.btn_cedit.setMinimumWidth(150)
        self.btn_cedit.setMinimumHeight(30)
        self.btn_cedit.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #aa0000;" +
            "border-radius: 15px;" +
            "font-size: 20px;" +
            "color: #ffffff;"
        )


        # Label Status
        self.stAnzeige = QLabel(self)
        self.stAnzeige.setMinimumWidth(150)
        self.stAnzeige.setMinimumHeight(40)
        self.stAnzeige.setText(self.appcategorie[self.appcselect])
        self.stAnzeige.move(20, 60)
        self.stAnzeige.setAlignment(Qt.AlignCenter)
        self.stAnzeige.setStyleSheet(
            "background: rgba(0, 200, 0, 150);" +
            "font-size: 24px;" +
            "color: #00e500;" +
            "border: 4px solid '#f0f0f0';" +
            "border-radius: 10px;" +
            "color: #ffffff;"
        )



        # Label Seitenanzeige
        self.pageshow = QLabel(self)
        self.pageshow.setFixedWidth(100)
        self.pageshow.setFixedHeight(20)
        self.pageshow.setText("Seite: " + str(self.apppage+1) + " / "+ str(int(self.count / 10) + 1))
        self.pageshow.move(50, 107)
        self.pageshow.setAlignment(Qt.AlignCenter)
        self.pageshow.setStyleSheet("background: rgba(255, 255, 255, 30);" )


        # Seite zurück Button
        self.btn_pageminus = QPushButton(self)
        self.btn_pageminus.setText("<")
        self.btn_pageminus.move(28, 107)
        #self.btn_pageminus.clicked.connect(self.pageminus)
        self.btn_pageminus.setMaximumWidth(20)
        self.btn_pageminus.setMaximumHeight(20)
        self.btn_pageminus.setStyleSheet("font-size: 20px;padding-top: -5px;")

        # Seite vor Button
        self.btn_pageplus = QPushButton(self)
        self.btn_pageplus.setText(">")
        self.btn_pageplus.move(152, 107)
        #self.btn_pageplus.clicked.connect(self.pageplus)
        self.btn_pageplus.setMaximumWidth(20)
        self.btn_pageplus.setMaximumHeight(20)
        self.btn_pageplus.setStyleSheet("font-size: 20px;padding-top: -5px;")



        self.appbtnmake()
        self.catbtnmake()
        self.appchange()

# ---------------------------------------------------------------------------------------------

        # konfiguration Fenster und zeigen
        self.setGeometry(0 + 50, 50, 1000, 600)  # x-pos, y-pos, breite, höhe
        self.setWindowTitle("VerFlatpakT")  # Title name
        self.setWindowIcon(QIcon(self.cpath + "/VerLinuxT-logo.png"))  # Datei für das logo des programms
        self.setFixedSize(1000, 600)  # fixe größe einstellen
        self.show()  # Fenster anzeigen

    def beschreibungchange(self):
        self.beschreibung[self.awneu] = self.btext.toPlainText()

    def appnamechange(self):
        self.applist[self.awneu] = self.appname.toPlainText()

    def appcomnamechange(self):
        self.appcom[self.awneu] = self.appcomname.toPlainText()

    def youtubeedit(self):
        text, ok = QInputDialog.getText(self, "Youtube ändern", "Youtube Video:")

        if ok:
            self.videoadr[self.awneu] = text
            self.fileurl = self.yt1 + self.videoadr[self.awneu] + self.yt2 + self.videoadr[self.awneu]
            self.appchange()

    def coveredit(self):
        text, ok = QInputDialog.getText(self, "Cover ändern", "bilddateiname: (im ordner/cover)")

        if ok:
            self.coverpm[self.awneu] = text
            self.appchange()

    def awknopf(self):
        e = self.sender()
        # print(e.objectName())
        self.awalt = self.awneu
        self.awneu = int(e.objectName()) + (self.apppage * 10)
        print(self.awneu)
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
        self.appcomname.setText(self.appcom[self.awneu])
        self.appname.setText(self.applist[self.awneu])
        file = self.cpath+"/cover/"+self.coverpm[self.awneu]
        self.cover.setPixmap(QPixmap(file))
        self.btext.setText(self.beschreibung[self.awneu])
        self.fileurl = self.yt1 + self.videoadr[self.awneu] + self.yt2 + self.videoadr[self.awneu]
        self.webview.setUrl(QUrl(self.fileurl))

    def starten(self):
        text, ok = QInputDialog.getText(self, "Cover ändern", ":")

        if ok:
            self.coverpm[self.awneu] = text
            self.appchange()

        self.update_btn()

# ------------- Appdaten einlesen ------------------------------------------------------------

    def appseinlesen(self):
        catpath = self.appcpath[self.appcselect]
        print(catpath)
        file1 = open(catpath, 'r')
        self.count = 0
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
            print("Line{}: {}".format(self.count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.coverpm.append(line[0:len(line) - 1])
            print("Line{}: {}".format(self.count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.videoadr.append(line[0:len(line) - 1])
            print("Line{}: {}".format(self.count, line.strip()))
            line = file1.readline()
            if not line:
                break
            line1 = line.replace("QE", "\n")
            self.beschreibung.append(line[0:len(line1) - 1])
            print("Line{}: {}".format(self.count, line.strip()))
            line = file1.readline()
            if not line:
                break
            self.appcom.append(line[0:len(line) - 1])
            print("Line{}: {}".format(self.count, line.strip()))

            self.count += 1
        self.appmenge = self.count - 1
        file1.close()

# --------- Speichern --------------------------------------------------------------------------------------------

    def speichern(self):
        catpath = self.appcpath[self.appcselect]
        # catpath = "test.data"
        print(catpath)
        file1 = open(catpath, 'w')
        # self.applist.clear()
        # self.coverpm.clear()
        # self.videoadr.clear()
        # self.beschreibung.clear()
        # self.appcom.clear()
        count = 0
        for i in self.applist:
            text = self.applist[count]+"\n"
            file1.write(text)
            print("Line{}: {}".format(count, text))

            text = self.coverpm[count]+"\n"
            file1.write(text)
            print("Line{}: {}".format(count, text))

            text = self.videoadr[count]+"\n"
            file1.write(text)
            print("Line{}: {}".format(count, text))
            text1 = self.beschreibung[count].replace("\n", "QE")
            text = text1 + "\n"
            file1.write(text)
            print("Line{}: {}".format(count, text))

            text = self.appcom[count]+"\n"
            file1.write(text)
            print("Line{}: {}".format(count, text))

            count += 1
        file1.close()
        self.appchange()
        self.appbtnmake()

# -------------- Applist Buttons ------------------------------------------------

    def appbtnmake(self):
        #print(self.appcategorie[self.appcselect])

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
        self.apppage = int(self.awneu/10)
        self.pageshow.setText("Seite: " + str(self.apppage + 1) + " / " + str(int(self.appmenge / 10) + 1))
        self.btn_app0.setText(self.applist[0 + self.apppage * 10])
        self.btn_app0.show()
        if self.apppage == 0:
            self.btn_pageminus.hide()
        else:
            self.btn_pageminus.show()
        if int(self.appmenge / 10) > self.apppage:
            self.btn_pageplus.show()
        else:
            self.btn_pageplus.hide()

        if self.appmenge >= self.apppage * 10 + 1:
            self.btn_app1.setText(self.applist[1 + self.apppage * 10])
            self.btn_app1.show()
            print("an" + self.applist[1])
        else:
            self.btn_app1.hide()

        if self.appmenge >= self.apppage * 10 + 2:
            self.btn_app2.setText(self.applist[2 + self.apppage * 10])
            self.btn_app2.show()
            print("an")
        else:
            self.btn_app2.hide()

        if self.appmenge >= self.apppage * 10 + 3:
            self.btn_app3.setText(self.applist[3 + self.apppage * 10])
            self.btn_app3.show()
            print("an")
        else:
            self.btn_app3.hide()

        if self.appmenge >= self.apppage * 10 + 4:
            self.btn_app4.setText(self.applist[4 + self.apppage * 10])
            self.btn_app4.show()
            print("an")
        else:
            self.btn_app4.hide()

        if self.appmenge >= self.apppage * 10 + 5:
            self.btn_app5.setText(self.applist[5 + self.apppage * 10])
            self.btn_app5.show()
            print("an")
        else:
            self.btn_app5.hide()

        if self.appmenge >= self.apppage * 10 + 6:
            self.btn_app6.setText(self.applist[6 + self.apppage * 10])
            self.btn_app6.show()
            print("an")
        else:
            self.btn_app6.hide()

        if self.appmenge >= self.apppage * 10 + 7:
            print(str(self.appmenge)+"-"+str(self.apppage * 10 + 7))
            self.btn_app7.setText(self.applist[7 + self.apppage * 10])
            self.btn_app7.show()
            print("an")
        else:
            self.btn_app7.hide()

        if self.appmenge >= self.apppage * 10 + 8:
            print(str(self.appmenge)+"-"+str(self.apppage * 10 + 8))
            self.btn_app8.setText(self.applist[8 + self.apppage * 10])
            self.btn_app8.show()
            print("an")
        else:
            self.btn_app8.hide()

        if self.appmenge >= self.apppage * 10 + 9:
            print("wtf" + str(self.appmenge)+"-"+str(self.apppage * 10 + 9))
            self.btn_app9.setText(self.applist[9 + self.apppage * 10])
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

# ---------------- Neue App hinzufügen -------------------------------------------------------
    def addapp(self):
        self.applist.append("neue App")
        print(self.applist)
        self.coverpm.append("default.gif")
        print(self.coverpm)
        self.videoadr.append("nRxToXoeqS4")
        self.beschreibung.append("das ist eine neue App")
        self.appcom.append("org.neueApp.neueApp")
        self.appmenge = self.appmenge + 1
        self.count = self.count + 1
        self.awneu = self.appmenge
        print(self.awneu)
        self.appchange()
        self.appbtnmake()

# --------------------------------------------------------------------------------------------


app = QApplication(sys.argv)
w = qFenster()
w.show()
sys.exit(app.exec())
