# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(1123, 737)
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_Map = QtWidgets.QGridLayout()
        self.gridLayout_Map.setObjectName("gridLayout_Map")
        self.verticalLayout_3.addLayout(self.gridLayout_Map)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_7 = QtWidgets.QLabel(mainForm)
        self.label_7.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label_7.setObjectName("label_7")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_CountOfPlants = QtWidgets.QLabel(mainForm)
        self.label_CountOfPlants.setMaximumSize(QtCore.QSize(167, 16777215))
        self.label_CountOfPlants.setText("")
        self.label_CountOfPlants.setObjectName("label_CountOfPlants")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_CountOfPlants)
        self.line = QtWidgets.QFrame(mainForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.verticalLayout_2.addLayout(self.formLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Slower = QtWidgets.QPushButton(mainForm)
        self.pushButton_Slower.setEnabled(False)
        self.pushButton_Slower.setMaximumSize(QtCore.QSize(167, 16777215))
        self.pushButton_Slower.setObjectName("pushButton_Slower")
        self.horizontalLayout_2.addWidget(self.pushButton_Slower)
        self.pushButton_Pause = QtWidgets.QPushButton(mainForm)
        self.pushButton_Pause.setEnabled(False)
        self.pushButton_Pause.setMaximumSize(QtCore.QSize(167, 16777215))
        self.pushButton_Pause.setObjectName("pushButton_Pause")
        self.horizontalLayout_2.addWidget(self.pushButton_Pause)
        self.pushButton_Faster = QtWidgets.QPushButton(mainForm)
        self.pushButton_Faster.setEnabled(False)
        self.pushButton_Faster.setMaximumSize(QtCore.QSize(167, 16777215))
        self.pushButton_Faster.setObjectName("pushButton_Faster")
        self.horizontalLayout_2.addWidget(self.pushButton_Faster)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.initButton = QtWidgets.QPushButton(mainForm)
        self.initButton.setMaximumSize(QtCore.QSize(167, 16777215))
        self.initButton.setObjectName("initButton")
        self.verticalLayout_2.addWidget(self.initButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Form"))
        self.label_7.setText(_translate("mainForm", "Количество живых растений:"))
        self.pushButton_Slower.setText(_translate("mainForm", "<"))
        self.pushButton_Pause.setText(_translate("mainForm", "||"))
        self.pushButton_Faster.setText(_translate("mainForm", ">"))
        self.initButton.setText(_translate("mainForm", "Начать новую симуляцию"))

