# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_share.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        Dialog.setMinimumSize(QtCore.QSize(320, 240))
        Dialog.setMaximumSize(QtCore.QSize(320, 240))
        Dialog.setStyleSheet("background:url(:/bk_pic/post-bg-desk.jpg);\n"
"font: 75 11pt \"Arial\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 11pt \"Arial\";")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 151, 21))
        self.lineEdit.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(33, 20, 71, 20))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 151, 21))
        self.lineEdit_2.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 91, 20))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 75, 23))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 171, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connect to share host"))
        self.lineEdit.setToolTip(_translate("Dialog", "Pls input remote share host ip address"))
        self.label.setText(_translate("Dialog", "Remote IP"))
        self.lineEdit_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Pls input remote share host port(default is 9999, if you don\'t know real port, pls keep this.</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Remote Port"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#000000;\">Test if this connection can be used.</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Test"))

import bk_pic_rc
