from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from map_func import *
import sys

# У меня на клавиатуре нет Page Up/Down поэтому я их переставил на другие кнопки:
# PageUp = Left Shift
# PageDown = Left Ctrl

dolgota = 0
shirota = 0
oblast = [0, 0]
flag_good_request = True
was_request = False

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(625, 656)
        self.centralwidget = QtWidgets.QWidget(parent=Main)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(440, 560, 151, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(225, 560, 151, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 560, 151, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 530, 47, 14))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 530, 47, 14))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 530, 47, 14))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 620, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 22))
        self.menubar.setObjectName("menubar")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Map_API", "Map_API"))
        self.label.setText(_translate("Main", "Долгота"))
        self.label_2.setText(_translate("Main", "Широта"))
        self.label_3.setText(_translate("Main", "Область"))
        self.pushButton.setText(_translate("Main", "Показать"))

    def start(self):
        global dolgota, shirota, oblast, flag_good_request, my_path
        try:
            dolgota = float(self.lineEdit_3.text())
            shirota = float(self.lineEdit_2.text())
            oblast = [float(self.lineEdit_1.text()), float(self.lineEdit_1.text())]
            my_path = 'data/map_ctrl.png'
            self.req()
            
            global was_request
            was_request = True
        except Exception:
            print('Неправильные значения!')
        
    def keyPressEvent(self, event):
        global dolgota, shirota, oblast, my_path, flag_good_request
        if (str(event.key()) == '87' or str(event.key()) == '1062') and dolgota <= 180:
            if flag_good_request:
                dolgota += 0.01
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_up.png'
                elif my_path == 'data/map_down.png':
                    my_path = 'data/map_ctrl.png'

        elif (str(event.key()) == '83' or str(event.key()) == '1067') and dolgota >= -180:
            if flag_good_request:
                dolgota -= 0.01
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_down.png'
                elif my_path == 'data/map_up.png':
                    my_path = 'data/map_ctrl.png'

        elif (str(event.key()) == '65' or str(event.key()) == '1060') and shirota >= -180:
            if flag_good_request:
                shirota -= 0.01
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_left.png'
                elif my_path == 'data/map_right.png':
                    my_path = 'data/map_ctrl.png'

        elif (str(event.key()) == '68' or str(event.key()) == '1042') and shirota <= 180:
            if flag_good_request:
                shirota += 0.01
            else:
                if my_path == 'data/map_ctrl.png':
                    my_path = 'data/map_right.png'
                elif my_path == 'data/map_left.png':
                    my_path = 'data/map_ctrl.png'

        elif str(event.key()) == '16777248':
            oblast[0] += 0.01
            oblast[1] += 0.01
            my_path = 'data/map_shift.png'
        elif str(event.key()) == '16777249':
            oblast[0] -= 0.01
            oblast[1] -= 0.01
            my_path = 'data/map_ctrl.png'

        if was_request:
            self.req()

    def req(self):
        global flag_good_request
        flag_good_request = requesting(dolgota, shirota, oblast)
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
