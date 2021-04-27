
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_AboutWindow(QMainWindow):

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
        self.resize(905, 726)

        self.setMinimumSize(900,700)
        self.setMaximumSize(905,726)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
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
        self.Text_privacy.setGeometry(QtCore.QRect(180, 240, 571, 431))
        self.Text_privacy.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Text_privacy.setObjectName("Text_privacy")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 121, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Maskperson.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(300, 90, 321, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Button_france = QtWidgets.QPushButton(self.centralwidget)
        self.Button_france.setGeometry(QtCore.QRect(300, 150, 101, 51))
        self.Button_france.setStyleSheet("background-color: rgb(43,43,43);")
        #self.Button_france.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_france.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/flag-france_1f1eb-1f1f7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_france.setIcon(icon)
        self.Button_france.setIconSize(QtCore.QSize(88, 70))
        self.Button_france.setObjectName("Button_france")
        self.Button_anglais = QtWidgets.QPushButton(self.centralwidget)
        self.Button_anglais.setGeometry(QtCore.QRect(410, 150, 101, 51))
        self.Button_anglais.setStyleSheet("background-color: rgb(43,43,43);")
        #self.Button_anglais.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_anglais.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/flag-united-kingdom_1f1ec-1f1e7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_anglais.setIcon(icon1)
        self.Button_anglais.setIconSize(QtCore.QSize(96, 70))
        self.Button_anglais.setObjectName("Button_anglais")
        self.Button_espganol = QtWidgets.QPushButton(self.centralwidget)
        self.Button_espganol.setGeometry(QtCore.QRect(520, 150, 101, 51))
        self.Button_espganol.setStyleSheet("background-color: rgb(43,43,43);")
        #self.Button_espganol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Button_espganol.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/flag-spain_1f1ea-1f1f8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_espganol.setIcon(icon2)
        self.Button_espganol.setIconSize(QtCore.QSize(95, 70))
        self.Button_espganol.setObjectName("Button_espganol")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)



        # self.Button_espganol.clicked.connect(self.clique_espagnol)
        # self.Button_anglais.clicked.connect(self.clique_anglais)
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


    def clique_francais(self , theme , appui):

        if ((theme == "light") and (appui=="fr")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Notre projet</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Dans le cadre de notre 4ème année d\'école d\'ingénieurs, nous avons comme projet de réaliser un détecteur de port du masque en utilisant l\'Intelligence Artificielle, plus précisément du deep learning. </span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Technologies utilisées</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Pour réaliser notre détecteur, nous avons dans un premier temps utilisé des CNN (Convolutional Neural Network) pré-entrainé pour détecter le visage. Ce dernier étant envoyé à 3 CNN que nous avons nous-mêmes entrainés qui font chacun une prédiction (Correct/Incorrect/No Mask) que nous traitons avec pondération. La prédiction est donc une combinaison de ces prédictions. Ces CNN sont entrainés sur un dataset de 1500 images par classe.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#000000;\">Lien GitHub</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#000000;\">Vous pouvez retrouver notre code sur GitHub avec ce lien : </span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#000000;\">Nous contacter</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#000000;\">Si vous souhaitez nous contacter, merci de vous adresser aux adresses mails suivantes : mael.fouqueau@isen-ouest.yncrea.fr ou augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;color:#000000;\"><br /></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\">A propos - Détection du port du masque</p></body></html>")

        elif((theme=="dark")and(appui =="fr")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Notre projet</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Dans le cadre de notre 4ème année d\'école d\'ingénieurs, nous avons comme projet de réaliser un détecteur de port du masque en utilisant l\'Intelligence Artificielle, plus précisément du deep learning. </span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Technologies utilisées</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Pour réaliser notre détecteur, nous avons dans un premier temps utilisé des CNN (Convolutional Neural Network) pré-entrainé pour détecter le visage. Ce dernier étant envoyé à 3 CNN que nous avons nous-mêmes entrainés qui font chacun une prédiction (Correct/Incorrect/No Mask) que nous traitons avec pondération. La prédiction est donc une combinaison de ces prédictions. Ces CNN sont entrainés sur un dataset de 1500 images par classe.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#ffffff;\">Lien GitHub</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#ffffff;\">Vous pouvez retrouver notre code sur GitHub avec ce lien : </span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#ffffff;\">Nous contacter</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#ffffff;\">Si vous souhaitez nous contacter, merci de vous adresser aux adresses mails suivantes : mael.fouqueau@isen-ouest.yncrea.fr ou augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\">A propos - Détection de port du masque</p></body></html>")

    def clique_espagnol(self , theme , appui):

        if ((theme == "light") and(appui =="esp")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Nuestro proyecto</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">En el marco de nuestro 4º año de escuela de ingeniería, teníamos como proyecto realizar un detector de uso de la máscara utilizando la Inteligencia Artificial, más precisamente el aprendizaje profundo.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Tecnologías utilizadas</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Para realizar nuestro detector, primero utilizamos una CNN (Convolutional Neural Network) preentrenada para detectar la cara. Esta última se envía a 3 CNNs que hemos entrenado nosotros mismos, cada una de las cuales hace una predicción (Correcta/Incorrecta/Sin máscara) que procesamos con ponderación. La predicción es entonces una combinación de estas predicciones. Estas CNN se entrenan con un conjunto de datos de 1500 imágenes por clase.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#000000;\">Enlace a GitHub</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#000000;\">Puedes encontrar nuestro código en GitHub con este enlace : </span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#000000;\">Contacto con nosotros</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#000000;\">Si desea ponerse en contacto con nosotros, utilice las siguientes direcciones de correo electrónico : mael.fouqueau@isen-ouest.yncrea.fr o augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\">Acerca de - Detección del desgaste de la máscara</p></body></html>")

        elif((theme=="dark")and(appui == "esp")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Nuestro proyecto</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">En el marco de nuestro 4º año de escuela de ingeniería, teníamos como proyecto realizar un detector de uso de la máscara utilizando la Inteligencia Artificial, más precisamente el aprendizaje profundo.</span></p>\n"
    "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Tecnologías utilizadas</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Para realizar nuestro detector, primero utilizamos una CNN (Convolutional Neural Network) preentrenada para detectar la cara. Esta última se envía a 3 CNNs que hemos entrenado nosotros mismos, cada una de las cuales hace una predicción (Correcta/Incorrecta/Sin máscara) que procesamos con ponderación. La predicción es entonces una combinación de estas predicciones. Estas CNN se entrenan con un conjunto de datos de 1500 imágenes por clase.</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#ffffff;\">Enlace a GitHub</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#ffffff;\">Puedes encontrar nuestro código en GitHub con este enlace : </span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#ffffff;\">Contacto con nosotros</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#ffffff;\">Si desea ponerse en contacto con nosotros, utilice las siguientes direcciones de correo electrónico : mael.fouqueau@isen-ouest.yncrea.fr o augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\">Acerca de - Detección del desgaste de la máscara</p></body></html>")


    def clique_anglais(self , theme , appui):

        if ((theme == "light") and(appui =="angl")):
            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Our project</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Within the framework of our 4th year of engineering school, we had as a project to realize a detector of wearing of the mask by using Artificial Intelligence, more specifically deep learning. </span></p>\n"
        "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Technologies used</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">To realize our detector, we first used pre-trained CNN (Convolutional Neural Network) to detect the face. The latter is sent to 3 CNNs that we have trained ourselves, each of which makes a prediction (Correct/Incorrect/No Mask) that we process with weighting. The prediction is therefore a combination of these predictions. These CNNs are trained on a dataset of 1500 images per class.</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#000000;\">GitHub link</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#000000;\">You can find our code on GitHub with this link: </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#000000;\">Contact us</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#000000;\">If you wish to contact us, please use the following email addresses : mael.fouqueau@isen-ouest.yncrea.fr or augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;color:#000000;\"><br /></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#000000;\">About - Face mask detection</p></body></html>")

        elif((theme=="dark")and(appui =="angl")):

            self.Text_privacy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Our project</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Within the framework of our 4th year of engineering school, we had as a project to realize a detector of wearing of the mask by using Artificial Intelligence, more specifically deep learning. </span></p>\n"
        "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Technologies used</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">To realize our detector, we first used pre-trained CNN (Convolutional Neural Network) to detect the face. The latter is sent to 3 CNNs that we have trained ourselves, each of which makes a prediction (Correct/Incorrect/No Mask) that we process with weighting. The prediction is therefore a combination of these predictions. These CNNs are trained on a dataset of 1500 images per class.</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#ffffff;\">GitHub link</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#ffffff;\">You can find our code on GitHub with this link: </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;color:#ffffff;\">Contact us</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;color:#ffffff;\">If you wish to contact us, please use the following email addresses : mael.fouqueau@isen-ouest.yncrea.fr or augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>")
            self.textBrowser_2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;color:#ffffff;\">About - Face mask detection</p></body></html>")




    def retranslateUi(self, MainWindow , theme):

        if (theme == "light"):

            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "About"))
            MainWindow.setWindowIcon(QtGui.QIcon("images/about_icon.png"))
            self.Text_privacy.setHtml(_translate("MainWindow" , "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Our project</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">Within the framework of our 4th year of engineering school, we had as a project to realize a detector of wearing of the mask by using Artificial Intelligence, more specifically deep learning. </span></p>\n"
        "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000;\">Technologies used</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\">To realize our detector, we first used pre-trained CNN (Convolutional Neural Network) to detect the face. The latter is sent to 3 CNNs that we have trained ourselves, each of which makes a prediction (Correct/Incorrect/No Mask) that we process with weighting. The prediction is therefore a combination of these predictions. These CNNs are trained on a dataset of 1500 images per class.</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">GitHub link</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">You can find our code on GitHub with this link: </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Contact us</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">If you wish to contact us, please use the following email addresses : mael.fouqueau@isen-ouest.yncrea.fr or augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>"))
            self.textBrowser_2.setHtml(_translate("MainWindow" , "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">About - Face mask detection</p></body></html>"))

        elif(theme=="dark"):

            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "About"))
            MainWindow.setWindowIcon(QtGui.QIcon("images/about_icon.png"))
            self.Text_privacy.setHtml(_translate("MainWindow" , "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Our project</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">Within the framework of our 4th year of engineering school, we had as a project to realize a detector of wearing of the mask by using Artificial Intelligence, more specifically deep learning. </span></p>\n"
        "<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#ffffff;\">Technologies used</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:8pt; font-style:italic; color:#ffffff;\">To realize our detector, we first used pre-trained CNN (Convolutional Neural Network) to detect the face. The latter is sent to 3 CNNs that we have trained ourselves, each of which makes a prediction (Correct/Incorrect/No Mask) that we process with weighting. The prediction is therefore a combination of these predictions. These CNNs are trained on a dataset of 1500 images per class.</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;; color:#ffffff;\">GitHub link</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;; color:#ffffff;\">You can find our code on GitHub with this link: </span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;; color:#ffffff;\">Contact us</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;; color:#ffffff;\">If you wish to contact us, please use the following email addresses : mael.fouqueau@isen-ouest.yncrea.fr or augustin.rochard@isen-ouest.yncrea.fr </span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;; color:#ffffff;\"><br /></p></body></html>"))
            self.textBrowser_2.setHtml(_translate("MainWindow" , "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\">About - Face mask detection</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_AboutWindow(theme=1)
    win.show()
    sys.exit(app.exec_())

    #MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_AboutWindow()
    # ui.setupUi(MainWindow)
