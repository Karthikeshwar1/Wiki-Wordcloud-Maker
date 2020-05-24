# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 436)
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 500, 441))
        self.scrollArea.setMinimumSize(QtCore.QSize(500, 400))
        self.scrollArea.setMaximumSize(QtCore.QSize(700, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 498, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(328, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Help"))
        self.pushButton.setText(_translate("Dialog", "Close"))
        self.label.setText(_translate("Dialog", "Just type a wikipedia article and press \'Generate\'!\n"
"To save the image, click on the disc icon when image is displayed"))
        self.label_2.setText(_translate("Dialog", "Program by :"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Karthikeshwar</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<a href=\"https://github.com/karthikeshwar1\">github.com/Karthikeshwar1</a>"))
        self.label_4.setText(_translate("Dialog", "Made with :"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Python, Wordcloud and PyQt5</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>Wordcloud is an open-source library and can be found at</p><p><a href=\"https://amueller.github.io/word_cloud/\"><span style=\" text-decoration: underline; color:#0000ff;\">amueller.github.io/word_cloud</span></a></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>PyQt5 is copyright (c) Riverbank Computing Limited.</p><p>Its homepage is </p><p><a href=\'https://www.riverbankcomputing.com/software/pyqt/\'>www.riverbankcomputing.com/software/pyqt</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

