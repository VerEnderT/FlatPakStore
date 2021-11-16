import sys
# import pathlib
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtMultimedia import QMediaContent


class qFenster(QMainWindow):   # QMainWindow oder Qwidget für menübars
    def __init__(self):
        super().__init__()

        self.testbutton = "0"
        self.awalt = 0
        self.awneu = 0
        self.gameslist = ["Super Tux Kart", "0 A.D.", "Minecraft"]
        self.coverpm = ["./SuperTuxKart.jpg", "./nullad.jpg", "./minecraft.jpg"]
        self.videoadr = ["ef9vYcuEDL4", "D3vxXZygHIk", "0maWbr0FHKY"]
        self.yt1 = "http://www.youtube.com/embed/"
        self.yt2 = "?autoplay=1&showinfo=0&controls=0&loop=1&playlist="
        self.fileurl = self.yt1 + self.videoadr[0] + self.yt2 + self.videoadr[0]
        self.beschreibung = ["Karts. Nitro. Action! \n\nSuperTuxKart ist ein 3D-Open-Source-Arcade-Racer mit einer " +
                             "Vielzahl von Charakteren, Strecken und Spielmodi. \n" +
                             "Im Story-Modus musst du dich dem bösen Nolok stellen und ihn" +
                             "besiegen, um das Maskottchen-Königreich wieder sicher zu machen! Sie können alleine " +
                             "gegen den Computer antreten, an mehreren Grand-Prix-Pokalen teilnehmen oder versuchen, " +
                             "Ihre schnellste Zeit im Zeitfahrmodus zu schlagen. Sie können auch mit bis zu acht " +
                             "Freunden auf einem einzigen Computer Rennen fahren oder kämpfen, in einem lokalen " +
                             "Netzwerk spielen oder online mit anderen Spielern auf der ganzen Welt spielen. ",
                             "0 A.D. (kurz für Jahr null Anno Domini) ist ein kontinuierlich weiterentwickeltes " +
                             "freies Echtzeit-Strategiespiel von Wildfire Games. Zu den Schwerpunkten des Spiels " +
                             "zählt der Aufbau einer Wirtschafts- und Kriegsproduktion zur anschließenden Bekämpfung " +
                             "der Gegner. Die im Spiel enthaltenen Zivilisationen und Technologien sind in etwa von " +
                             "der realen historischen Entwicklung der Antike in den Jahren 500 bis 1 vor Christus " +
                             "beeinflusst. ", "spielen mit klötzchen und noch ganz viel meer "]

        # Hintergrund
        image = QPixmap("./background.gif")
        background = QLabel(self)
        background.setPixmap(image)
        background.setFixedWidth(1000)
        background.setFixedHeight(700)
        background.setScaledContents(True)
        background.move(0, 0)

        # webkit test
        self.webview = QWebEngineView(self)
        self.webview.setUrl(QUrl(self.fileurl))
        self.webview.setMinimumWidth(400)
        self.webview.setMinimumHeight(225)
        self.webview.move(185, 20)
        self.webview.settings()

        # Cover
        image1 = QPixmap("./SuperTuxKart.jpg")
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
        self.btn_install.move(700, 500)
        self.btn_install.setObjectName("2")
        # self.btn_install.clicked.connect(self.knopf)
        self.btn_install.setMinimumWidth(200)
        self.btn_install.setMinimumHeight(50)
        self.btn_install.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #0eff2a;" +
            "border-radius: 20px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )
        self.count = 0

        for i in self.gameslist:
            self.gamebtn = QPushButton(self)
            self.gamebtn.setText(self.gameslist[self.count])
            self.gamebtn.move(50, 150 + self.count * 35)
            self.aobjectname = str(self.count)
            self.gamebtn.setObjectName(self.aobjectname)
            self.count = self.count + 1
            self.gamebtn.clicked.connect(self.awknopf)
            print(i)

# ---------------------------------------------------------------------------------------------

        # konfiguration Fenster und zeigen
        self.setGeometry(1280 + 50, 50, 1000, 600)  # x-pos, y-pos, breite, höhe
        self.setWindowTitle("VerFlatpakT")  # Title name
        self.setWindowIcon(QIcon("VETlogo.png"))  # Datei für das logo des programms
        self.setFixedSize(1000, 600)  # fixe größe einstellen
        self.show()  # Fenster anzeigen

    def awknopf(self):
        e = self.sender()
        print(e.objectName())
        self.awalt = self.awneu
        self.awneu = int(e.objectName())
        self.gamechange()

    def gamechange(self):
        self.gamename.setText(self.gameslist[self.awneu])
        self.cover.setPixmap(QPixmap(self.coverpm[self.awneu]))
        self.btext.setText(self.beschreibung[self.awneu])
        self.fileurl = self.yt1 + self.videoadr[self.awneu] + self.yt2 + self.videoadr[self.awneu]
        self.webview.setUrl(QUrl(self.fileurl))


app = QApplication(sys.argv)
w = qFenster()
w.show()
sys.exit(app.exec())
