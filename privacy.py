
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_PrivacyWindow(QMainWindow):
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
        #MainWindow.resize(905, 934)
        self.setGeometry(450,70,905,934)
        self.setMinimumSize(900,930)
        self.setMaximumSize(900,930)
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
        self.Text_privacy.setGeometry(QtCore.QRect(180, 220, 571, 650))
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
        self.Button_france.setIconSize(QtCore.QSize(88, 65))
        self.Button_france.setObjectName("Button_france")
        self.Button_anglais = QtWidgets.QPushButton(self.centralwidget)
        self.Button_anglais.setGeometry(QtCore.QRect(410, 150, 91, 51))
        self.Button_anglais.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_anglais.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/flag-united-kingdom_1f1ec-1f1e7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_anglais.setIcon(icon1)
        self.Button_anglais.setIconSize(QtCore.QSize(96, 65))
        self.Button_anglais.setObjectName("Button_anglais")
        self.Button_espganol = QtWidgets.QPushButton(self.centralwidget)
        self.Button_espganol.setGeometry(QtCore.QRect(510, 150, 91, 51))
        self.Button_espganol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_espganol.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/flag-spain_1f1ea-1f1f8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_espganol.setIcon(icon2)
        self.Button_espganol.setIconSize(QtCore.QSize(95, 65))
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

    def clique_francais(self, theme , appui):

        if ((theme == "light") and (appui=="fr")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">D??claration de service</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Vous comprenez et acceptez que si vous utilisez le service de d??tection de masques faciaux, vous ??tes r??put?? avoir pleinement lu et accept?? le contenu de cette d??claration, sinon, veuillez arr??ter ce service imm??diatement.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">1. Contenu du service</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Ce service est fourni aux utilisateurs sous la forme d'une interface. Vous pouvez obtenir le service en ouvrant l???application pour r??aliser la fonction de d??tection automatique et de rappel du port de masques.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2. Protection de la vie priv??e</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.1 Collecte des donn??es</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Vous comprenez et acceptez qu'afin de fournir des services, vous acceptez d'allumer la cam??ra sur l'application et d'identifier le contenu captur??. Ce service ne collecte pas d'informations sur le port de masques.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.2 Stockage et protection des donn??es</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Ce service ne stocke ni ne t??l??charge les contenus vid??o, audio et image captur??s. Le processus de d??tection est effectu?? en temps r??el dans votre ordinateur.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">3. D??claration et garantie</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Vous devez vous assurer que votre utilisation de ce service r??pond aux exigences des lois et r??glements, et vous ??tes responsable de la l??galit?? et de la conformit?? de vos sources de contenu et de vos acquisitions. Ce service vous fournit uniquement un service de d??tection de masques faciaux conform??ment ?? vos instructions et n'est pas responsable de la conformit?? l??gale de votre utilisation de ce service.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">4. Notification et correction</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Vous comprenez et acceptez que, pour r??pondre aux besoins des politiques et du service, nous mettrons ?? jour le contenu de cette d??claration de service lorsque cela sera n??cessaire et nous la publierons sur cette application. Veuillez vous r??f??rer ?? cette d??claration de service pour conna??tre les mises ?? jour dans le temps.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">Derni??re mise ?? jour: 24 Mars 2021</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D??tection port du masque - Confidentialit??</p></body></html>")
        elif((theme=="dark")and(appui =="fr")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">D??claration de service</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Vous comprenez et acceptez que si vous utilisez le service de d??tection de masques faciaux, vous ??tes r??put?? avoir pleinement lu et accept?? le contenu de cette d??claration, sinon, veuillez arr??ter ce service imm??diatement.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">1. Contenu du service</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Ce service est fourni aux utilisateurs sous la forme d'une interface. Vous pouvez obtenir le service en ouvrant l???application pour r??aliser la fonction de d??tection automatique et de rappel du port de masques.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2. Protection de la vie priv??e</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.1 Collecte des donn??es</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Vous comprenez et acceptez qu'afin de fournir des services, vous acceptez d'allumer la cam??ra sur l'application et d'identifier le contenu captur??. Ce service ne collecte pas d'informations sur le port de masques.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.2 Stockage et protection des donn??es</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Ce service ne stocke ni ne t??l??charge les contenus vid??o, audio et image captur??s. Le processus de d??tection est effectu?? en temps r??el dans votre ordinateur.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">3. D??claration et garantie</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Vous devez vous assurer que votre utilisation de ce service r??pond aux exigences des lois et r??glements, et vous ??tes responsable de la l??galit?? et de la conformit?? de vos sources de contenu et de vos acquisitions. Ce service vous fournit uniquement un service de d??tection de masques faciaux conform??ment ?? vos instructions et n'est pas responsable de la conformit?? l??gale de votre utilisation de ce service.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">4. Notification et correction</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Vous comprenez et acceptez que, pour r??pondre aux besoins des politiques et du service, nous mettrons ?? jour le contenu de cette d??claration de service lorsque cela sera n??cessaire et nous la publierons sur cette application. Veuillez vous r??f??rer ?? cette d??claration de service pour conna??tre les mises ?? jour dans le temps.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#ffffff;\">Derni??re mise ?? jour: 24 Mars 2021</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff\">D??tection port du masque - Confidentialit??</p></body></html>")

    def clique_espagnol(self, theme , appui):

        if ((theme == "light") and(appui =="esp")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Declaraci??n de servicio</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Usted entiende y est?? de acuerdo en que si utiliza el servicio de detecci??n de m??scaras faciales, se considera que ha le??do completamente y est?? de acuerdo en aceptar el contenido de esta declaraci??n, de lo contrario, por favor, deje este servicio inmediatamente.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">1. Contenido del servicio</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Este servicio se ofrece a los usuarios en forma de interfaz. Puede obtener el servicio abriendo la aplicaci??n para realizar la funci??n de detectar y recordar autom??ticamente el uso de mascarillas.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2. Protecci??n de la intimidad</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.1 Recogida de datos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Usted entiende y acepta que, para la prestaci??n de los servicios, se compromete a encender la c??mara de la aplicaci??n y a identificar el contenido capturado. Este servicio no recoge informaci??n sobre el uso de la m??scara.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.2 Almacenamiento y protecci??n de datos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Este servicio no almacena ni carga el contenido de v??deo, audio e imagen capturado. El proceso de detecci??n se realiza en tiempo real en su ordenador.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">3. Declaraci??n y garant??a</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Usted debe asegurarse de que su uso de este servicio cumple con los requisitos de las leyes y reglamentos, y es responsable de la legalidad y el cumplimiento de sus fuentes de contenido y adquisiciones. Este servicio s??lo le proporciona un servicio de detecci??n de m??scaras faciales de acuerdo con sus instrucciones y no es responsable del cumplimiento legal de su uso de este servicio.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">4. Aviso y correcci??n</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Usted entiende y acepta que, con el fin de satisfacer las necesidades de las pol??ticas y el servicio, actualizaremos el contenido de esta declaraci??n de servicio cuando sea necesario y lo publicaremos en este aplicaci??n. Por favor, consulte esta declaraci??n de servicio para ver las actualizaciones en el tiempo.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">??ltima actualizaci??n: 24 de marzo de 2021</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Detecci??n de la m??scara facial - Confidentialidad</p></body></html>")
        elif((theme=="dark")and(appui == "esp")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Declaraci??n de servicio</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Usted entiende y est?? de acuerdo en que si utiliza el servicio de detecci??n de m??scaras faciales, se considera que ha le??do completamente y est?? de acuerdo en aceptar el contenido de esta declaraci??n, de lo contrario, por favor, deje este servicio inmediatamente.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">1. Contenido del servicio</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Este servicio se ofrece a los usuarios en forma de interfaz. Puede obtener el servicio abriendo la aplicaci??n para realizar la funci??n de detectar y recordar autom??ticamente el uso de mascarillas.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2. Protecci??n de la intimidad</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.1 Recogida de datos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Usted entiende y acepta que, para la prestaci??n de los servicios, se compromete a encender la c??mara de la aplicaci??n y a identificar el contenido capturado. Este servicio no recoge informaci??n sobre el uso de la m??scara.</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.2 Almacenamiento y protecci??n de datos</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Este servicio no almacena ni carga el contenido de v??deo, audio e imagen capturado. El proceso de detecci??n se realiza en tiempo real en su ordenador.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">3. Declaraci??n y garant??a</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Usted debe asegurarse de que su uso de este servicio cumple con los requisitos de las leyes y reglamentos, y es responsable de la legalidad y el cumplimiento de sus fuentes de contenido y adquisiciones. Este servicio s??lo le proporciona un servicio de detecci??n de m??scaras faciales de acuerdo con sus instrucciones y no es responsable del cumplimiento legal de su uso de este servicio.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">4. Aviso y correcci??n</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Usted entiende y acepta que, con el fin de satisfacer las necesidades de las pol??ticas y el servicio, actualizaremos el contenido de esta declaraci??n de servicio cuando sea necesario y lo publicaremos en este aplicaci??n. Por favor, consulte esta declaraci??n de servicio para ver las actualizaciones en el tiempo.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#ffffff;\">??ltima actualizaci??n: 24 de marzo de 2021</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff\">Detecci??n de la m??scara facial - Confidentialidad</p></body></html>")


    def clique_anglais(self, theme , appui):

        if ((theme == "light") and(appui =="angl")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Service Statement</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You understand and agree that if you use the face mask detection service, you are deemed to have fully read and agree to accept the content of this statement, otherwise, please stop this service immediately.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">1. Service content</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">This service is provided to users in the form of an interface. You can obtain the service by opening the application to realize the function of automatically detecting and reminding the wearing of masks.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2. Privacy protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.1 Data collection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You understand and agree that, in order to provide services, you agree to turn on the camera on the application and identify the captured content. This service does not collect information about mask-wearing</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.2 Data storage and protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">This service does not store or upload the captured video, audio, and image content. The detection process is performed in real-time in your computer.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">3. Declaration and Guarantee</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You should ensure that your use of this service meets the requirements of laws and regulations, and you are responsible for the legality and compliance of your content sources and acquisitions. This service only provides you with a face mask detection service in accordance with your instructions and is not responsible for the legal compliance of your use of this service.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">4. Notice and Correction</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You understand and agree that, in order to meet the needs of policies and service, we will update the content of this service statement when necessary and publish it on this application. Please refer to this service statement for updates in time.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">Last updated: March 24, 2021</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Face-Mask Detection - Confidentiality</p></body></html>")

        elif((theme=="dark")and(appui =="angl")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Service Statement</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You understand and agree that if you use the face mask detection service, you are deemed to have fully read and agree to accept the content of this statement, otherwise, please stop this service immediately.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">1. Service content</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">This service is provided to users in the form of an interface. You can obtain the service by opening the application to realize the function of automatically detecting and reminding the wearing of masks.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2. Privacy protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.1 Data collection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You understand and agree that, in order to provide services, you agree to turn on the camera on the application and identify the captured content. This service does not collect information about mask-wearing</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.2 Data storage and protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">This service does not store or upload the captured video, audio, and image content. The detection process is performed in real-time in your computer.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">3. Declaration and Guarantee</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You should ensure that your use of this service meets the requirements of laws and regulations, and you are responsible for the legality and compliance of your content sources and acquisitions. This service only provides you with a face mask detection service in accordance with your instructions and is not responsible for the legal compliance of your use of this service.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">4. Notice and Correction</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You understand and agree that, in order to meet the needs of policies and service, we will update the content of this service statement when necessary and publish it on this application. Please refer to this service statement for updates in time.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#ffffff;\">Last updated: March 24, 2021</span></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color : #ffffff\">Face-Mask Detection - Confidentiality</p></body></html>")


    def retranslateUi(self , MainWindow , theme):

        if (theme == "light"):

            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Confidentiality"))
            MainWindow.setWindowIcon(QtGui.QIcon("images/cadenas.png"))
            self.Text_privacy.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Service Statement</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You understand and agree that if you use the face mask detection service, you are deemed to have fully read and agree to accept the content of this statement, otherwise, please stop this service immediately.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">1. Service content</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">This service is provided to users in the form of an interface. You can obtain the service by opening the application to realize the function of automatically detecting and reminding the wearing of masks.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2. Privacy protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.1 Data collection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You understand and agree that, in order to provide services, you agree to turn on the camera on the application and identify the captured content. This service does not collect information about mask-wearing</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">2.2 Data storage and protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">This service does not store or upload the captured video, audio, and image content. The detection process is performed in real-time in your computer.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">3. Declaration and Guarantee</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You should ensure that your use of this service meets the requirements of laws and regulations, and you are responsible for the legality and compliance of your content sources and acquisitions. This service only provides you with a face mask detection service in accordance with your instructions and is not responsible for the legal compliance of your use of this service.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">4. Notice and Correction</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">You understand and agree that, in order to meet the needs of policies and service, we will update the content of this service statement when necessary and publish it on this application. Please refer to this service statement for updates in time.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">Last updated: March 24, 2021</span></p></body></html>"))
            self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Face-Mask Detection - Confidentiality</p></body></html>"))

        elif(theme=="dark"):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Confidentiality"))
            MainWindow.setWindowIcon(QtGui.QIcon("images/cadenas.png"))
            self.Text_privacy.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Service Statement</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You understand and agree that if you use the face mask detection service, you are deemed to have fully read and agree to accept the content of this statement, otherwise, please stop this service immediately.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">1. Service content</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">This service is provided to users in the form of an interface. You can obtain the service by opening the application to realize the function of automatically detecting and reminding the wearing of masks.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2. Privacy protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.1 Data collection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You understand and agree that, in order to provide services, you agree to turn on the camera on the application and identify the captured content. This service does not collect information about mask-wearing</span><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#000000;\">.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">2.2 Data storage and protection</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">This service does not store or upload the captured video, audio, and image content. The detection process is performed in real-time in your computer.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">3. Declaration and Guarantee</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You should ensure that your use of this service meets the requirements of laws and regulations, and you are responsible for the legality and compliance of your content sources and acquisitions. This service only provides you with a face mask detection service in accordance with your instructions and is not responsible for the legal compliance of your use of this service.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">4. Notice and Correction</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">You understand and agree that, in order to meet the needs of policies and service, we will update the content of this service statement when necessary and publish it on this application. Please refer to this service statement for updates in time.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; color:#ffffff;\">Last updated: March 24, 2021</span></p></body></html>"))
            self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color : #ffffff\">Face-Mask Detection - Confidentiality</p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_PrivacyWindow(theme=1)
    win.show()
    sys.exit(app.exec_())
