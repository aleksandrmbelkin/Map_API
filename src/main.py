import sys
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from map_func import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(625, 656)
        self.centralwidget = QtWidgets.QWidget(parent=Main)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 540, 151, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 540, 151, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 510, 47, 14))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 510, 47, 14))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 550, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 22))
        self.menubar.setObjectName("menubar")

        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Map_API", "Map_API"))
        self.label.setText(_translate("Main", "Долгота"))
        self.label_2.setText(_translate("Main", "Широта"))
        self.pushButton.setText(_translate("Main", "Показать"))

    def start(self):
        requesting(self.lineEdit_2.text(), self.lineEdit_3.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
