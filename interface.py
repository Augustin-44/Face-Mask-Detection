from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from privacy import Ui_PrivacyWindow
from instructions import Ui_InstructionsWindow
from about import Ui_AboutWindow
import cv2
import numpy as np
import os
from torchvision import models, transforms
from PIL import Image
import torch
from f_utils import init_models, get_output_count, get_index_max, list_ports
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.closeFlag = False
        self.retranslateUi(MainWindow=self)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1884, 945)
        self.adjustSize()
        self.setMinimumSize(1800,940)



        # Partie 1 colorisation de l'interface et de ses widgets
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setPalette(palette)
        self.setStyleSheet("background-color: rgb(43,43,43);")
        #Fin de la 1ere partie colorisation


        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(590, 170, 751, 621))
        self.label_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label_camera.setLineWidth(3)
        self.label_camera.setText("")
        self.label_camera.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_camera.setObjectName("label_camera")
        self.Button_francais = QtWidgets.QPushButton(self.centralwidget)
        self.Button_francais.setGeometry(QtCore.QRect(840, 20, 71, 51))
        self.Button_francais.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.Button_francais.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/flag-france_1f1eb-1f1f7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_francais.setIcon(icon)
        self.Button_francais.setIconSize(QtCore.QSize(96, 71))
        self.Button_francais.setObjectName("Button_francais")
        self.Button_angleterre = QtWidgets.QPushButton(self.centralwidget)
        self.Button_angleterre.setGeometry(QtCore.QRect(940, 20, 71, 51))
        self.Button_angleterre.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.Button_angleterre.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/flag-united-kingdom_1f1ec-1f1e7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_angleterre.setIcon(icon1)
        self.Button_angleterre.setIconSize(QtCore.QSize(96, 71))
        self.Button_angleterre.setObjectName("Button_angleterre")
        self.Button_espagne = QtWidgets.QPushButton(self.centralwidget)
        self.Button_espagne.setGeometry(QtCore.QRect(1040, 20, 71, 51))
        self.Button_espagne.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.Button_espagne.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/flag-spain_1f1ea-1f1f8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_espagne.setIcon(icon2)
        self.Button_espagne.setIconSize(QtCore.QSize(96, 71))
        self.Button_espagne.setObjectName("Button_espagne")
        self.Button_start_detection = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start_detection.setGeometry(QtCore.QRect(840, 90, 271, 51))


        #2e partie colorisation widgets
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.Button_start_detection.setPalette(palette)
        #Fin 2e partie colorisation widgets

        font = QtGui.QFont()
        font.setPointSize(11)
        self.Button_start_detection.setFont(font)
        self.Button_start_detection.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.Button_start_detection.setObjectName("Button_start_detection")
        self.label_verdict = QtWidgets.QLabel(self.centralwidget)
        self.label_verdict.setGeometry(QtCore.QRect(590, 810, 751, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_verdict.setPalette(palette)
        self.label_verdict.setFrameShape(QtWidgets.QFrame.Box)
        self.label_verdict.setObjectName("label_verdict")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.label_verdict.setFont(font)
        self.label_verdict.setLineWidth(1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.label_verdict.setAlignment(QtCore.Qt.AlignCenter)

        # 3e partie colorisation
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 43, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setStyle(QtCore.Qt.SolidPattern)

        #Fin 3e partie colorisation



        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1884, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuMode = QtWidgets.QMenu(self.menuOptions)
        self.menuMode.setObjectName("menuMode")
        self.menuCamera = QtWidgets.QMenu(self.menuOptions)
        self.menuCamera.setObjectName("menuCamera")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.actionDark = QtWidgets.QAction(self)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(self)
        self.actionLight.setObjectName("actionLight")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConfidentiality = QtWidgets.QAction(self)
        self.actionConfidentiality.setObjectName("actionConfidentiality")
        self.actionInstructions = QtWidgets.QAction(self)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionCam_0 = QtWidgets.QAction(self)
        self.actionCam_0.setObjectName("actionCam_0")
        self.menuMode.addAction(self.actionDark)
        self.menuMode.addAction(self.actionLight)

        self.menuOptions.addAction(self.menuCamera.menuAction())
        self.menuOptions.addAction(self.menuMode.menuAction())
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionConfidentiality)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        self.cam1 = QtWidgets.QAction(self)
        self.cam1.setObjectName("cam1")
        self.cam2 = QtWidgets.QAction(self)
        self.cam2.setObjectName("cam2")
        self.cam3 = QtWidgets.QAction(self)
        self.cam3.setObjectName("cam3")
        self.menubar.setStyleSheet("background-color: rgb(60, 63, 65);" "color:rgb(255,255,255)")
        self.tete = True
        self.faces_count = 0
        self.text = 'Undefined'
        self.appui = 'rien'
        self.preds_words = ['Correct', 'Incorrect', 'No Mask']
        self.label_camera.setScaledContents(True) # Pour que l'image de la webcam occupe tout le label
        self.label_camera.setStyleSheet("color : rgb(255,255,255)")
        self.cap = cv2.VideoCapture(0)
        self.choose_webcam()
        self.couleur = "dark"


        #Connexion des boutons et de la MenuBar
        self.Button_start_detection.clicked.connect(self.clique_camera)
        self.actionLight.triggered.connect(self.mode_light)
        self.actionDark.triggered.connect(self.mode_dark)
        self.Button_francais.clicked.connect(self.clique_francais)
        self.Button_espagne.clicked.connect(self.clique_espagnol)
        self.Button_angleterre.clicked.connect(self.clique_anglais)
        self.actionConfidentiality.triggered.connect(self.open_privacy)
        self.actionInstructions.triggered.connect(self.open_instructions)
        self.actionAbout.triggered.connect(self.open_about)
        self.actionCam_0.triggered.connect(self.choose_cam0)
        self.cam1.triggered.connect(self.choose_cam1)
        self.cam2.triggered.connect(self.choose_cam2)


    def closeEvent(self, a0 : QtGui.QCloseEvent):
        self.closeFlag=True
        #print("See you soon")

    def choose_webcam(self):
        if (list_ports() == 1):
            self.menuCamera.addAction(self.actionCam_0)
        if (list_ports()== 2):
            self.menuCamera.addAction(self.actionCam_0)
            self.menuCamera.addAction(self.cam1)
        if (list_ports()==3):
            self.menuCamera.addAction(self.actionCam_0)
            self.menuCamera.addAction(self.cam1)
            self.menuCamera.addAction(self.cam2)
        if (list_ports()==4):
            self.menuCamera.addAction(self.actionCam_0)
            self.menuCamera.addAction(self.cam1)
            self.menuCamera.addAction(self.cam2)
            self.menuCamera.addAction(self.cam3)


    def choose_cam0(self):
        self.cap = cv2.VideoCapture(0)
    def choose_cam1(self):
        self.cap = cv2.VideoCapture(1)
    def choose_cam2(self):
        self.cap = cv2.VideoCapture(2)
    def choose_cam3(self):
       self.cap = cv2.VideoCapture(3)

    def mode_light(self):
        self.couleur = "light"
        self.setStyleSheet("background-color : rgb(255,235,228)")
        self.Button_francais.setStyleSheet("background-color : rgb(255,235,228)")
        self.Button_angleterre.setStyleSheet("background-color : rgb(255,235,228)")
        self.Button_espagne.setStyleSheet("background-color : rgb(255,235,228)")
        self.menubar.setStyleSheet("background-color : rgb(255,184,171)")
        self.Button_start_detection.setStyleSheet("background-color : rgb(255,235,228)")
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.Button_start_detection.setPalette(palette)
        self.label_camera.setStyleSheet("color : rgb(0,0,0)")
        self.label_verdict.setStyleSheet("color : rgb(0,0,0)")
    def mode_dark(self):
        self.couleur = "dark"
        self.setStyleSheet("background-color : rgb(43,43,43)")
        self.Button_francais.setStyleSheet("background-color : rgb(43,43,43);")
        self.Button_angleterre.setStyleSheet("background-color : rgb(43,43,43)")
        self.Button_espagne.setStyleSheet("background-color : rgb(43,43,43)")
        self.menubar.setStyleSheet("background-color : rgb(60, 63, 65);""color:rgb(255,255,255)")
        self.Button_start_detection.setStyleSheet("background-color : rgb(43,43,43)")
        self.Button_start_detection.setStyleSheet("color:rgb(255,255,255)")
        self.label_camera.setStyleSheet("color : rgb(255,255,255)")
        self.label_verdict.setStyleSheet("color : rgb(255,255,255)")

    def clique_camera(self):

        FRAME_THICKNESS = 2
        modelFile = os.getcwd() + os.sep + "models" + os.sep + "res10_300x300_ssd_iter_140000.caffemodel"
        configFile = os.getcwd() + os.sep + "models" + os.sep + "deploy-prototxt.txt"
        print(configFile)
        print(os.path.isfile(configFile))
        net = cv2.dnn.readNet(configFile, modelFile)

        GREEN = (0, 255, 0)
        ORANGE = (0, 165, 255)
        RED = (0, 0, 255)
        BLUE = (255, 0, 0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.6
        num_classes = 3

        image_transforms = transforms.Compose([transforms.Resize(size=(224, 224)), transforms.ToTensor(),
                                               transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

        resnet18 = models.resnet18(pretrained=True)
        vgg16 = models.vgg16(pretrained=True)
        densenet = models.densenet161(pretrained=True)
        googlenet = models.googlenet(pretrained=True)
        shufflenet = models.shufflenet_v2_x1_0(pretrained=True)
        mobilenet_v3_large = models.mobilenet_v3_large(pretrained=True)
        resnext50_32x4d = models.resnext50_32x4d(pretrained=True)
        wide_resnet50_2 = models.wide_resnet50_2(pretrained=True)
        mnasnet = models.mnasnet1_0(pretrained=True)

        cnn_models = [resnet18, vgg16, densenet, googlenet, shufflenet, mobilenet_v3_large, resnext50_32x4d,
                      wide_resnet50_2, mnasnet]
        init_models(cnn_models, num_classes)

        resnet18.load_state_dict(torch.load(r"models\facemask1500\resnet18_10epochs_10bs.pth"))
        vgg16.load_state_dict(torch.load(r"models\facemask1500\vgg16_10epochs_10bs.pth"))
        densenet.load_state_dict(torch.load(r"models\facemask1500\densenet_10epochs_10bs.pth"))
        googlenet.load_state_dict(torch.load(r"models\facemask1500\googlenet_10epochs_10bs.pth"))
        mnasnet.load_state_dict(torch.load(r"models\facemask1500\mnasnet_10epochs_10bs.pth"))
        mobilenet_v3_large.load_state_dict(torch.load(r"models\facemask1500\mobilenet_v3_large_10epochs_10bs.pth"))
        resnext50_32x4d.load_state_dict(torch.load(r"models\facemask1500\resnext50_32x4d_10epochs_10bs.pth"))
        shufflenet.load_state_dict(torch.load(r"models\facemask1500\shufflenet_10epochs_10bs.pth"))
        wide_resnet50_2.load_state_dict(torch.load(r"models\facemask1500\wide_resnet50_2_10epochs_10bs.pth"))

        cnn_models = [vgg16, resnext50_32x4d, densenet]

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        for model in cnn_models:
            model.eval()
            model = model.to(device)

        #preds_words = ['Correct', 'Incorrect', 'NoMask']
        preds_color = [GREEN, ORANGE, RED]
        color = BLUE
        #text = 'Undefined'
        fps = 0
        faces_preds_list = []
        last_faces_count = 0
        faces_change = False


        # Main Loop
        while True:
            img = self.cap.read()[1]
            h, w = img.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
            net.setInput(blob)
            faces = net.forward()
            #faces_count = 0
            self.faces_count = 0


            for j in range(faces.shape[2]):
                confidence = faces[0, 0, j, 2]
                if confidence > 0.5:
                    self.faces_count += 1
                    #print("Nb visage :",self.faces_count)
                    if (self.faces_count > 1):
                        self.tete = False
                    if (self.faces_count == 1):
                        self.tete = True


            if self.faces_count != last_faces_count:
                faces_change = True
                last_faces_count = self.faces_count

            self.faces_count = 0
            if fps == 15 or faces_change:
                fps = 0
                faces_change = False
                faces_preds_list = []

            for i in range(faces.shape[2]):
                confidence = faces[0, 0, i, 2]
                if confidence > 0.5:
                    # print("Tete n° :", faces_count)
                    self.faces_count += 1

                    box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (x, y, x1, y1) = box.astype("int")
                    # print(x, y, x1, y1)
                    preds_list = []

                    if fps == 0:
                        # DEBUT IF
                        img_face = img[y:y1, x:x1]
                        img_opencv = cv2.resize(img_face, (224, 224))
                        img_opencv = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2RGB)
                        img_pil = Image.fromarray(img_opencv)
                        img_tensor = image_transforms(img_pil).unsqueeze_(0)
                        img_tensor = img_tensor.to(device)

                        for model in cnn_models:
                            output = model(img_tensor)
                            _, preds = torch.max(output, 1)
                            preds_list.append(preds[0].item())

                        output_avg, vgg16_flag = get_output_count(preds_list)
                        index_value = get_index_max(output_avg, vgg16_flag)
                        #print(preds_list, index_value)
                        self.text = self.preds_words[index_value]
                        color = preds_color[index_value]
                        faces_preds_list.append([self.text, color])
                        # FIN IF
                        #print("Nb tête :" , self.tete)

                        if ((self.preds_words[index_value]=="No Mask") and (self.appui=="fr") and (self.tete==True)):
                            self.text = "Pas de masque"
                            self.label_verdict.setText("Mettez votre masque correctement")
                        if ((self.preds_words[index_value]=="No Mask") and (self.appui=="esp")and (self.tete==True)):
                            self.text = "Sin mascara"
                            self.label_verdict.setText("Póngase la máscara correctamente")
                        if ((self.preds_words[index_value]=="No Mask") and (self.appui=="angl")and (self.tete==True)):
                            self.text = "No Mask"
                            self.label_verdict.setText("Put on your mask properly")
                        if ((self.preds_words[index_value]=="Correct") and (self.appui=="fr")and (self.tete==True)):
                            self.text = "Masque correct"
                            self.label_verdict.setText("Ne changez rien ! C'est parfait")
                        if ((self.preds_words[index_value]=="Correct") and (self.appui=="esp")and (self.tete==True)):
                            self.text = "Mascara correcta"
                            self.label_verdict.setText("No cambies nada. Es perfecto")
                        if ((self.preds_words[index_value]=="Correct") and (self.appui=="angl")and (self.tete==True)):
                            self.text = "Mask correct"
                            self.label_verdict.setText("Don't change anything ! It is perfect")
                        if ((self.preds_words[index_value]=="Incorrect") and (self.appui=="fr")and (self.tete==True)):
                            self.text = "Masque incorrect"
                            self.label_verdict.setText("Couvrez bien tout votre visage avec le masque")
                        if ((self.preds_words[index_value]=="Incorrect") and (self.appui=="esp")and (self.tete==True)):
                            self.text = "Mascara incorrecta"
                            self.label_verdict.setText("Cubrir toda la cara con la máscara")
                        if ((self.preds_words[index_value]=="Incorrect") and (self.appui=="angl")and (self.tete==True)):
                            self.text = "Mask incorrect"
                            self.label_verdict.setText("Cover your entire face with the mask")
                        if ((self.preds_words[index_value]=="Incorrect") and (self.appui =="rien")and (self.tete==True)):
                            self.label_verdict.setText("Cover your entire face with the mask")
                        if ((self.preds_words[index_value]=="No Mask") and (self.appui =="rien")and (self.tete==True)):
                            self.label_verdict.setText("Put on your mask properly")
                        if ((self.preds_words[index_value]=="Correct") and (self.appui =="rien")and (self.tete==True)):
                            self.label_verdict.setText("Don't change anything ! It is perfect")
                        if ((self.tete == False) and (self.appui=="angl") ):
                            self.label_verdict.setText("Make sure you cover the entire face with your mask")
                        if ((self.tete == False) and (self.appui=="fr") ):
                            self.label_verdict.setText("Veillez à couvrir l'entièreté du visage avec votre masque")
                        if ((self.tete == False) and (self.appui=="esp") ):
                            self.label_verdict.setText("Asegúrate de que tu máscara cubre toda la carae")
                        if ((self.tete == False) and (self.appui=="rien") ):
                            self.label_verdict.setText("Make sure you cover the entire face with your mask")



                    cv2.rectangle(img, (x, y), (x1, y1), faces_preds_list[self.faces_count-1][1], FRAME_THICKNESS)
                    cv2.putText(img, faces_preds_list[self.faces_count-1][0], (x+10, y+20), font, fontScale, faces_preds_list[self.faces_count-1][1], 2, cv2.LINE_AA)

            fps += 1
            #cv2.imshow('webcam', img)
            self.displayImage(img , 1)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            if (self.closeFlag == True):
                break

        self.cap.release()
        cv2.destroyAllWindows()


    def displayImage(self , img , imgWindow = 1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2] == 4):
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img , img.shape[1] , img.shape[0] , qformat)
        img = img.rgbSwapped()
        self.label_camera.setPixmap(QPixmap.fromImage(img))
        self.label_camera.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def clique_francais(self):
        self.appui = "fr"
        self.Button_start_detection.setText("Commencer la détection")
        self.setWindowTitle("Détection du port du masque")
        self.menuHelp.setTitle("Aide")
        self.actionInstructions.setText("Instructions")
        self.actionAbout.setText("A propos")
        self.actionConfidentiality.setText("Confidentialité")
        self.menuCamera.setTitle("Caméra")
        self.menuMode.setTitle("Thème")
        self.actionDark.setText("Sombre")
        self.actionLight.setText("Jour")

    def clique_anglais(self):
        self.appui = "angl"
        self.Button_start_detection.setText("Start Detection")
        self.setWindowTitle("Face mask detection")
        self.menuHelp.setTitle("Help")
        self.actionInstructions.setText("Instructions")
        self.actionAbout.setText("About")
        self.actionConfidentiality.setText("Confidentiality")
        self.menuCamera.setTitle("Camera")
        self.menuMode.setTitle("Theme")
        self.actionDark.setText("Dark")
        self.actionLight.setText("Light")

    def clique_espagnol(self):
        self.appui = "esp"
        self.Button_start_detection.setText("Inicio de la detección")
        self.setWindowTitle("DetecFlbcion de mascaras faciales")
        self.menuHelp.setTitle("Ayuda")
        self.actionInstructions.setText("Instrucciones")
        self.actionAbout.setText("Acerca de")
        self.actionConfidentiality.setText("Confidencialidad")
        self.menuCamera.setTitle("Camara")
        self.menuMode.setTitle("Tema")
        self.actionDark.setText("Oscuro")
        self.actionLight.setText("Dia")

    def open_privacy(self):
        self.win = Ui_PrivacyWindow(theme=self.couleur)
        self.win.show()

    def open_instructions(self):
        self.win = Ui_InstructionsWindow(theme=self.couleur)
        self.win.show()

    def open_about(self):
        self.win = Ui_AboutWindow(theme=self.couleur)
        self.win.show()



    def retranslateUi(self , MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face mask Detection"))
        MainWindow.setWindowIcon(QtGui.QIcon("images/MaskIcon.png"))
        self.Button_start_detection.setText(_translate("MainWindow", "Start Detection"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuMode.setTitle(_translate("MainWindow", "Theme"))
        self.menuCamera.setTitle(_translate("MainWindow", "Camera"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDark.setText(_translate("MainWindow", "Dark "))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionConfidentiality.setText(_translate("MainWindow", "Confidentiality"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionCam_0.setText(_translate("MainWindow", "Cam 0"))
        self.cam1.setText(_translate("MainWindow" , "Cam 1"))
        self.cam2.setText(_translate("MainWindow" , "Cam 2"))
        self.cam3.setText(_translate("MainWindow" , "Cam 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())


