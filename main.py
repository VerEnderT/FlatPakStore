import sys
import pathlib
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class qFenster(QMainWindow):   # QMainWindow oder Qwidget für menübars
    def __init__(self):
        super().__init__()

        self.beschreibung1 = "Karts. Nitro. Action! \n\nSuperTuxKart ist ein 3D-Open-Source-Arcade-Racer mit einer " \
                             "Vielzahl von Charakteren, Strecken und Spielmodi. \n" \
                             "Im Story-Modus musst du dich dem bösen Nolok stellen und ihn" \
                             "besiegen, um das Maskottchen-Königreich wieder sicher zu machen! Sie können alleine " \
                             "gegen den Computer antreten, an mehreren Grand-Prix-Pokalen teilnehmen oder versuchen, " \
                             "Ihre schnellste Zeit im Zeitfahrmodus zu schlagen. Sie können auch mit bis zu acht " \
                             "Freunden auf einem einzigen Computer Rennen fahren oder kämpfen, in einem lokalen " \
                             "Netzwerk spielen oder online mit anderen Spielern auf der ganzen Welt spielen. "
        self.beschreibung2 = "0 A.D. (kurz für Jahr null Anno Domini) ist ein kontinuierlich weiterentwickeltes " \
                             "freies Echtzeit-Strategiespiel von Wildfire Games. Zu den Schwerpunkten des Spiels " \
                             "zählt der Aufbau einer Wirtschafts- und Kriegsproduktion zur anschließenden Bekämpfung " \
                             "der Gegner. Die im Spiel enthaltenen Zivilisationen und Technologien sind in etwa von " \
                             "der realen historischen Entwicklung der Antike in den Jahren 500 bis 1 vor Christus " \
                             "beeinflusst. "

        # Hintergrund
        image = QPixmap("./background.gif")
        background = QLabel(self)
        background.setPixmap(image)
        background.setFixedWidth(1000)
        background.setFixedHeight(700)
        background.setScaledContents(True)
        background.move(0, 0)

        # Media player
        filename = str(pathlib.Path(__file__).parent.resolve()) + "/SuperTuxKart.mp4"
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setMinimumWidth(400)
        self.videoWidget.setMinimumHeight(225)
        self.videoWidget.move(185, 20)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.play()
        self.mediaPlayer.setVolume(0)
        self.mediaPlayer.stateChanged.connect(self.play)

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
        self.btext.setText(self.beschreibung1)
        self.btext.move(170, 300)
        self.btext.setStyleSheet("background: rgba(0, 0, 0, 140); color: #ffffff;")

        # Installieren Button
        self.btn_install = QPushButton(self)
        self.btn_install.setText("Installieren")
        self.btn_install.move(700, 500)
        self.btn_install.clicked.connect(self.knopf)
        self.btn_install.setMinimumWidth(200)
        self.btn_install.setMinimumHeight(50)
        self.btn_install.setStyleSheet(
            "border: 4px solid '#f0f0f0';" +
            "background: #0eff2a;" +
            "border-radius: 20px;" +
            "font-size: 35px;" +
            "color: #ffffff;"
        )

        # SuperTuxKart
        self.stk = QPushButton(self)
        self.stk.setText("SuperTuxKart")
        self.stk.move(50, 150)
        self.stk.clicked.connect(self.cgame0)

        # 0 A.D.
        self.nullad = QPushButton(self)
        self.nullad.setText("0 A.D.")
        self.nullad.move(50, 180)
        self.nullad.clicked.connect(self.cgame1)

# ---------------------------------------------------------------------------------------------

        # konfiguration Fenster und zeigen
        self.setGeometry(50, 50, 1000, 600)  # x-pos, y-pos, breite, höhe
        self.setWindowTitle("VerFlatpakT")  # Title name
        self.setWindowIcon(QIcon("VETlogo.png"))  # Datei für das logo des programms
        self.setFixedSize(1000, 600)  # fixe größe einstellen
        self.show()  # Fenster anzeigen

    def knopf(self):
        print(self.mediaPlayer.isAvailable())
        print(self.mediaPlayer.state())
        print(self.mediaPlayer.errorString())

    def play(self):
        self.mediaPlayer.play()

    def cgame0(self):
        self.cover.setPixmap(QPixmap("./SuperTuxKart.jpg"))
        self.gamename.setText("Super TuX Kart")
        self.btext.setText(self.beschreibung1)
        filename = str(pathlib.Path(__file__).parent.resolve()) + "/SuperTuxKart.mp4"
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

    def cgame1(self):
        self.cover.setPixmap(QPixmap("./nullad.jpg"))
        self.gamename.setText("0 A.D.")
        self.btext.setText(self.beschreibung2)
        filename = str(pathlib.Path(__file__).parent.resolve()) + "/nullAD.webm"
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))


app = QApplication(sys.argv)
w = qFenster()
w.show()
sys.exit(app.exec())
