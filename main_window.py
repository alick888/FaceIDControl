# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 603)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(160, 166, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 561))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.canvas = QtWidgets.QLabel(self.formLayoutWidget)
        self.canvas.setGeometry(QtCore.QRect(70, 90, 350, 240))
        self.canvas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.canvas.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.identification = QtWidgets.QPushButton(self.formLayoutWidget)
        self.identification.setGeometry(QtCore.QRect(70, 340, 351, 31))
        self.identification.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.identification.setObjectName("identification")
        self.name = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.name.setGeometry(QtCore.QRect(70, 390, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.pushButton_delete = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(320, 390, 93, 28))
        self.pushButton_delete.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.pushButton_pz = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_pz.setGeometry(QtCore.QRect(70, 440, 191, 28))
        self.pushButton_pz.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_pz.setObjectName("pushButton_pz")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(320, 439, 91, 31))
        self.pushButton_exit.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 494, 171, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/tupian/image/tianmaxingkong-words.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别"))
        self.identification.setText(_translate("MainWindow", "辨识身份"))
        self.name.setPlaceholderText(_translate("MainWindow", "输入名字"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.label.setText(_translate("MainWindow", "AI刷脸智慧门锁"))
        self.pushButton_pz.setText(_translate("MainWindow", "拍照"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出"))
import imagerc_rc
