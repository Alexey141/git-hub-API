# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python\gui\file.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 600)
        Dialog.setStyleSheet("background-color: green;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 550, 120, 30))
        self.pushButton.setStyleSheet("background-color:white;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 550, 120, 30))
        self.pushButton_2.setStyleSheet("background-color:white;\n"
"font: 75 10pt \"Comic Sans MS\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 500, 500, 30))
        self.lineEdit.setStyleSheet("background-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 450, 70, 30))
        self.comboBox.setStyleSheet("background-color: white;")
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 580, 360))
        self.textEdit.setStyleSheet("background: white;")
        self.textEdit.setObjectName("textEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 450, 90, 30))
        self.comboBox_2.setStyleSheet("background-color: white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(350, 450, 70, 30))
        self.comboBox_3.setStyleSheet("background-color: white;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Search Ports"))
        self.pushButton_2.setText(_translate("Dialog", "Open port"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "50"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "75"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "110"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "150"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "200"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "300"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "600"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "1200"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "1800"))
        self.comboBox_2.setItemText(9, _translate("Dialog", "2400"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "4800"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "9600"))
        self.comboBox_2.setItemText(12, _translate("Dialog", "19200"))
        self.comboBox_2.setItemText(13, _translate("Dialog", "38400"))
        self.comboBox_2.setItemText(14, _translate("Dialog", "57600"))
        self.comboBox_2.setItemText(15, _translate("Dialog", "115200"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "..."))
