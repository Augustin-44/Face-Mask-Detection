
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_InstructionsWindow(QMainWindow):

    def __init__(self , theme):
        super().__init__()
        self.setupUi()
        self.setTheme(theme)
        self.retranslateUi(MainWindow=self , theme=theme)
        self.lancer_fr(them=theme)
        self.lancer_esp(them=theme)
        self.lancer_rien(them=theme)

    def setTheme(self , theme):

        if (theme =="light"):
            self.setStyleSheet("background-color : rgb(255,235,228)")
            self.Button_espganol.setStyleSheet("background-color : rgb(255,235,228)")
            self.Button_anglais.setStyleSheet("background-color : rgb(255,235,228)")
            self.Button_france.setStyleSheet("background-color : rgb(255,235,228)")

        if (theme =="dark"):
            self.setStyleSheet("background-color : rgb(43,43,43)")
            self.Button_anglais.setStyleSheet("background-color : rgb(43,43,43)")
            self.Button_france.setStyleSheet("background-color : rgb(43,43,43)")
            self.Button_espganol.setStyleSheet("background-color : rgb(43,43,43)")

    def setupUi(self):
        self.setObjectName("MainWindow")
        #MainWindow.resize(905, 830)
        self.setGeometry(450,70,905,830)
        self.setMinimumSize(900,800)
        self.setMaximumSize(900,800)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Text_privacy = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_privacy.setGeometry(QtCore.QRect(180, 240, 571, 481))
        self.Text_privacy.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Text_privacy.setObjectName("Text_privacy")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 121, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Maskperson.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(310, 90, 291, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Button_france = QtWidgets.QPushButton(self.centralwidget)
        self.Button_france.setGeometry(QtCore.QRect(310, 150, 91, 51))
        self.Button_france.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_france.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/flag-france_1f1eb-1f1f7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_france.setIcon(icon)
        self.Button_france.setIconSize(QtCore.QSize(91, 65))
        self.Button_france.setObjectName("Button_france")
        self.Button_anglais = QtWidgets.QPushButton(self.centralwidget)
        self.Button_anglais.setGeometry(QtCore.QRect(410, 150, 91, 51))
        self.Button_anglais.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_anglais.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/flag-united-kingdom_1f1ec-1f1e7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_anglais.setIcon(icon1)
        self.Button_anglais.setIconSize(QtCore.QSize(96, 66))
        self.Button_anglais.setObjectName("Button_anglais")
        self.Button_espganol = QtWidgets.QPushButton(self.centralwidget)
        self.Button_espganol.setGeometry(QtCore.QRect(510, 150, 91, 51))
        self.Button_espganol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_espganol.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/flag-spain_1f1ea-1f1f8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_espganol.setIcon(icon2)
        self.Button_espganol.setIconSize(QtCore.QSize(95, 66))
        self.Button_espganol.setObjectName("Button_espganol")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def lancer_fr(self , them):
        if them == "light":
            self.Button_france.clicked.connect(lambda : self.clique_francais(theme=them , appui="fr"))
        if them == "dark":
            self.Button_france.clicked.connect(lambda : self.clique_francais(theme=them , appui="fr"))
    def lancer_rien(self , them):
        if them == "light":
            self.Button_anglais.clicked.connect(lambda : self.clique_anglais(theme=them , appui="angl"))
        if them == "dark":
            self.Button_anglais.clicked.connect(lambda : self.clique_anglais(theme=them , appui="angl"))
    def lancer_esp(self , them):
        if them == "light":
            self.Button_espganol.clicked.connect(lambda : self.clique_espagnol(theme=them , appui="esp"))
        if them == "dark":
            self.Button_espganol.clicked.connect(lambda : self.clique_espagnol(theme=them , appui="esp"))




    def clique_anglais(self , theme , appui):
        if ((theme == "light") and(appui =="angl")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color : #000000;\">Instructions for optimal detection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">It is important to place your head in front of the camera, so that your whole face appears on the screen and the detection can work optimally</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">Depending on how you wear your mask, instructions will appear on the screen to help you wear your mask for maximum protection.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color : #000000;\">Language</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">It is possible to change the language of the interface in order to use the detector in the best possible way. Click on the flag corresponding to the language you want to use.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color : #000000;\">Camera</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">If you have several webcams, it is possible to choose which one you prefer to use for detection. In the Options menu, choose the one you want among those detected by the interface.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color : #000000;\">Theme</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">It is possible to change the background colour of the interface by choosing either a dark or a light mode. Click on Options then Theme to select preferred mode.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color : #000000;\">About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">If you want to know how we made this mask detector and with which tools, click in the menu Help then About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color : #000000;\">Confidentiality</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color : #000000;\">Find our privacy policy in the Help menu</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\">Face mask detection - Instructions</p></body></html>")
        elif((theme=="dark")and(appui =="angl")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Instructions for optimal detection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">It is important to place your head in front of the camera, so that your whole face appears on the screen and the detection can work optimally</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Depending on how you wear your mask, instructions will appear on the screen to help you wear your mask for maximum protection.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Language</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">It is possible to change the language of the interface in order to use the detector in the best possible way. Click on the flag corresponding to the language you want to use.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Camera</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">If you have several webcams, it is possible to choose which one you prefer to use for detection. In the Options menu, choose the one you want among those detected by the interface.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Theme</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">It is possible to change the background colour of the interface by choosing either a dark or a light mode. Click on Options then Theme to select preferred mode.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">If you want to know how we made this mask detector and with which tools, click in the menu Help then About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Confidentiality</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Find our privacy policy in the Help menu</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\">Face mask detection - Instructions</p></body></html>")

    def clique_francais(self , theme , appui):
        if ((theme == "light") and (appui=="fr")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Instructions pour une détection optimale</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Il est important de placer votre tête en face de la caméra, afin que votre visage entier apparaisse à l'écran et que la détection puisse fonctionner de manière optimale.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Selon la façon dont vous portez votre masque, des instructions apparaitront à l'écran pour vous aider à porter votre masque pour une protection maximale.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Langue</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Il est possible de changer la langue de l'interface afin d'utiliser le détecteur de la meilleure façon possible. Cliquez sur le drapeau correspondant à la langue que vous souhaitez utiliser.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Caméra</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Si vous avez plusieurs webcams, il est possible de choisir celle que vous préférez utiliser pour la détection. Dans le menu Options, choisissez celle que vous voulez parmi celles détectées par l'interface.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Thème</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Il est possible de modifier la couleur de fond de l'interface en choisissant un mode sombre ou clair. Cliquez sur Options puis sur Thème pour sélectionner le mode souhaité.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">A propos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Si vous voulez savoir comment nous avons réalisé ce détecteur de masque et avec quels outils, cliquez dans le menu Aide puis A propos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Confidentialité</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Retrouvez notre politique de confidentialité dans le menu Aide</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\">Détection de port du masque - Instructions</p></body></html>")
        elif((theme=="dark")and(appui =="fr")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Instructions pour une détection optimale</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Il est important de placer votre tête en face de la caméra, afin que votre visage entier apparaisse à l'écran et que la détection puisse fonctionner de manière optimale.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Selon la façon dont vous portez votre masque, des instructions apparaitront à l'écran pour vous aider à porter votre masque pour une protection maximale.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Langue</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Il est possible de changer la langue de l'interface afin d'utiliser le détecteur de la meilleure façon possible. Cliquez sur le drapeau correspondant à la langue que vous souhaitez utiliser.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Caméra</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Si vous avez plusieurs webcams, il est possible de choisir celle que vous préférez utiliser pour la détection. Dans le menu Options, choisissez celle que vous voulez parmi celles détectées par l'interface.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Thème</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Il est possible de modifier la couleur de fond de l'interface en choisissant un mode sombre ou clair. Cliquez sur Options puis sur Thème pour sélectionner le mode souhaité.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">A propos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Si vous voulez savoir comment nous avons réalisé ce détecteur de masque et avec quels outils, cliquez dans le menu Aide puis A propos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Confidentialité</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Retrouvez notre politique de confidentialité dans le menu Aide</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\">Détection de port du masque - Instructions</p></body></html>")

    def clique_espagnol(self , theme , appui):
        if ((theme == "light") and(appui =="esp")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Instrucciones para una detección óptima</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Es importante que coloques tu cabeza frente a la cámara, para que toda tu cara aparezca en la pantalla y la detección pueda funcionar de forma óptima.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Según la forma de llevar la máscara, aparecerán en la pantalla instrucciones que le ayudarán a ponerse la máscara para obtener la máxima protección.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Idioma</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Es posible cambiar el idioma de la interfaz para utilizar el detector de la mejor manera posible. Haga clic en la bandera correspondiente al idioma que desea utilizar.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Cámara</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Si tiene varias cámaras web, puede elegir la que prefiera utilizar para la detección. En el menú Opciones, elija la que desee entre las detectadas por la interfaz.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Tema</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Es posible cambiar el color de fondo de la interfaz eligiendo un modo oscuro o claro. Haga clic en Opciones y luego en Tema para seleccionar el modo deseado.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Acerca</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Si quieres saber cómo hemos hecho este detector de máscaras y con qué herramientas, haz clic en el menú Ayuda y luego en Acerca.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-weight:600;\">Confidentialidad</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\"><span style=\" font-style:italic;\">Encuentre nuestra política de privacidad en el menú de Ayuda</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #000000;\">Detección de máscaras faciales - Instrucciones</p></body></html>")
        elif((theme=="dark")and(appui == "esp")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Instrucciones para una detección óptima</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Es importante que coloques tu cabeza frente a la cámara, para que toda tu cara aparezca en la pantalla y la detección pueda funcionar de forma óptima.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Según la forma de llevar la máscara, aparecerán en la pantalla instrucciones que le ayudarán a ponerse la máscara para obtener la máxima protección.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Idioma</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Es posible cambiar el idioma de la interfaz para utilizar el detector de la mejor manera posible. Haga clic en la bandera correspondiente al idioma que desea utilizar.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Cámara</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Si tiene varias cámaras web, puede elegir la que prefiera utilizar para la detección. En el menú Opciones, elija la que desee entre las detectadas por la interfaz.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Tema</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Es posible cambiar el color de fondo de la interfaz eligiendo un modo oscuro o claro. Haga clic en Opciones y luego en Tema para seleccionar el modo deseado.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Acerca</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Si quieres saber cómo hemos hecho este detector de máscaras y con qué herramientas, haz clic en el menú Ayuda y luego en Acerca.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-weight:600;\">Confidentialidad</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\"><span style=\" font-style:italic;\">Encuentre nuestra política de privacidad en el menú de Ayuda</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff;\">Detección de máscaras faciales - Instrucciones</p></body></html>")

    def retranslateUi(self, MainWindow , theme):
        if (theme == "light"):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Instructions"))
            MainWindow.setWindowIcon(QtGui.QIcon("images/instructions_icon.png"))
            self.Text_privacy.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-weight:600;\">Instructions for optimal detection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">It is important to place your head in front of the camera, so that your whole face appears on the screen and the detection can work optimally</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">Depending on how you wear your mask, instructions will appear on the screen to help you wear your mask for maximum protection.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-weight:600;\">Language</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">It is possible to change the language of the interface in order to use the detector in the best possible way. Click on the flag corresponding to the language you want to use.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-weight:600;\">Camera</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">If you have several webcams, it is possible to choose which one you prefer to use for detection. In the Options menu, choose the one you want among those detected by the interface.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-weight:600;\">Theme</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">It is possible to change the background colour of the interface by choosing either a dark or a light mode. Click on Options then Theme to select preferred mode.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-weight:600;\">About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">If you want to know how we made this mask detector and with which tools, click in the menu Help then About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-weight:600;\">Confidentiality</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\"><span style=\" font-style:italic;\">Find our privacy policy in the Help menu</span></p></body></html>"))
            self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\">Face mask detection - Instructions</p></body></html>"))

        elif(theme=="dark"):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Instructions"))
            MainWindow.setWindowIcon(QtGui.QIcon("images/instructions_icon.png"))
            self.Text_privacy.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-weight:600;\">Instructions for optimal detection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">It is important to place your head in front of the camera, so that your whole face appears on the screen and the detection can work optimally</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">Depending on how you wear your mask, instructions will appear on the screen to help you wear your mask for maximum protection.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-weight:600;\">Language</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">It is possible to change the language of the interface in order to use the detector in the best possible way. Click on the flag corresponding to the language you want to use.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-weight:600;\">Camera</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">If you have several webcams, it is possible to choose which one you prefer to use for detection. In the Options menu, choose the one you want among those detected by the interface.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-weight:600;\">Theme</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">It is possible to change the background colour of the interface by choosing either a dark or a light mode. Click on Options then Theme to select preferred mode.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-weight:600;\">About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">If you want to know how we made this mask detector and with which tools, click in the menu Help then About</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-weight:600;\">Confidentiality</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\"><span style=\" font-style:italic;\">Find our privacy policy in the Help menu</span></p></body></html>"))
            self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\">Face mask detection - Instructions</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_InstructionsWindow(theme=1)
    win.show()
    sys.exit(app.exec_())
