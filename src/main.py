from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from map_func import *
import sys

# У меня на клавиатуре нет Page Up/Down поэтому я их переставил на другие кнопки:
# Приближение = Left Shift
# Отдаление = Left Ctrl
# Смена темы = T

geocode = ''
theme = 'light'
dolgota = 0
shirota = 0
dolgota_met = 0
shirota_met = 0
oblast = [1, 1]
flag_good_request = True
was_request = False

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(625, 750)
        self.centralwidget = QtWidgets.QWidget(parent=Main)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_geo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_geo.setGeometry(QtCore.QRect(30, 660, 100, 14))
        self.label_geo.setObjectName("label_geo")

        self.geocode_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.geocode_line.setGeometry(QtCore.QRect(10, 680, 151, 41))
        self.geocode_line.setObjectName("geocode")

        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(440, 590, 151, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(225, 590, 151, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 590, 151, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 560, 47, 14))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(275, 560, 47, 14))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 560, 47, 14))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 530, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)

        self.pushButton_geo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_geo.setGeometry(QtCore.QRect(260, 680, 75, 23))
        self.pushButton_geo.setObjectName("pushButton_geo")
        self.pushButton_geo.clicked.connect(self.search)

        self.pushButton_geo_sbros = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_geo_sbros.setGeometry(QtCore.QRect(430, 680, 180, 23))
        self.pushButton_geo_sbros.setObjectName("pushButton_geo")
        self.pushButton_geo_sbros.clicked.connect(self.search)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 22))
        self.menubar.setObjectName("menubar")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Map_API", "Map_API"))
        self.label_geo.setText(_translate("Main", "Введите запрос"))
        self.label.setText(_translate("Main", "Долгота"))
        self.label_2.setText(_translate("Main", "Широта"))
        self.label_3.setText(_translate("Main", "Область"))
        self.pushButton.setText(_translate("Main", "Показать"))
        self.pushButton_geo.setText(_translate("Main", "Искать"))
        self.pushButton_geo_sbros.setText(_translate("Main", "Сброс поискового результата"))

    def start(self):
        global dolgota, shirota, oblast, flag_good_request, my_path, geocode
        try:
            dolgota = float(self.lineEdit_3.text())
            shirota = float(self.lineEdit_2.text())
            oblast = [float(self.lineEdit_1.text()), float(self.lineEdit_1.text())]
            geocode = ''
            my_path = 'data/map.png'
            self.req()
            
            global was_request
            was_request = True
        except Exception:
            print('Неправильные значения!')
        
    def search(self):
        global dolgota, shirota, oblast, flag_good_request, my_path, geocode, dolgota_met, shirota_met
        try:
            if self.geocode_line.text() != '':
                geocode = '+'.join(self.geocode_line.text().split())
                flag_good_request, dolgota, shirota = geocode_requesting(geocode)
                shirota_met = shirota
                dolgota_met = dolgota
            self.req()
            
            global was_request
            was_request = True
        except Exception:
             print('Неправильные значения!')

    def keyPressEvent(self, event):
        global dolgota, shirota, oblast, my_path, flag_good_request
        # print(str(event.key()))
        if (str(event.key()) == '87' or str(event.key()) == '1062') and dolgota <= 180:
            if flag_good_request:
                shirota += 0.1 * oblast[0]
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_up.png'
                elif my_path == 'data/map_down.png':
                    my_path = 'data/map_ctrl.png'

        elif (str(event.key()) == '83' or str(event.key()) == '1067') and dolgota >= -180:
            if flag_good_request:
                shirota -= 0.1 * oblast[0]
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_down.png'
                elif my_path == 'data/map_up.png':
                    my_path = 'data/map_ctrl.png'

        elif (str(event.key()) == '65' or str(event.key()) == '1060') and shirota >= -180:
            if flag_good_request:
                dolgota -= 0.1 * oblast[0]
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_left.png'
                elif my_path == 'data/map_right.png':
                    my_path = 'data/map_ctrl.png'

        elif (str(event.key()) == '68' or str(event.key()) == '1042') and shirota <= 180:
            if flag_good_request:
                dolgota += 0.1 * oblast[0]
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_right.png'
                elif my_path == 'data/map_left.png':
                    my_path = 'data/map_ctrl.png'

        elif str(event.key()) == '16777249':
            if flag_good_request:
                if int(oblast[0]) * 2 < 90:
                    oblast[0] *= 2
                    oblast[1] *= 2
            else:
                my_path = 'data/map_ctrl.png'
        elif str(event.key()) == '16777248':
            if flag_good_request:   
                if oblast[0] > 0.001:
                    oblast[0] /= 2
                    oblast[1] /= 2
            else:
                my_path = 'data/map_shift.png'
        elif str(event.key()) == '84' or str(event.key()) == '1045':
            global theme
            if theme == 'light':
                theme = 'dark'
            else:
                theme = 'light'
        elif str(event.key()) == '16777220':
            self.search()

        if was_request:
            self.req()

    def req(self):
        global flag_good_request, my_path, dolgota, shirota
        flag_good_request = requesting(dolgota, shirota, oblast, theme, dolgota_met, shirota_met, geocode)
        if not flag_good_request and my_path == 'data/map.png':
            my_path = 'data/map_ctrl.png'
        self.show_image()

    def show_image(self):
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        self.image.setGeometry(QtCore.QRect(50, 10, 500, 500))
        self.image.setPixmap(QtGui.QPixmap(my_path))
        self.image.setScaledContents(True)
        self.image.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
