#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import sys, random
from database import ComicsDB
import functools as ft

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 554)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 260, 391, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 381, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow, "", "", "", "", "")
        MainWindow.load()
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), ft.partial(MainWindow.checkAnswer, 1))
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), ft.partial(MainWindow.checkAnswer, 3))
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), ft.partial(MainWindow.checkAnswer, 5))
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), MainWindow.load)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), ft.partial(MainWindow.checkAnswer, 2))
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), ft.partial(MainWindow.checkAnswer,4))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, a, b, c, d, e):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ExKaySeeDee", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", a , None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", b, None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", c, None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", d, None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", e, None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))

class MyForm(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.db = ComicsDB('data.db')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.score = 0

    def checkAnswer(self, x):
        if x == self.t:
            self.ui.textEdit.setText("Your Answer is correct, please reload to change question.")
            self.score = self.score + 1
        else:
            self.ui.textEdit.setText("Your Answer is not correct, please try again or hit reload to change question.")
        
    def load(self):
        id = random.randrange(1,842,1)
        alt = "Alt Text : " + self.db.getAlt(id)
        titlet = self.db.getTitle(id)
        title = [self.db.getTitle(random.randrange(1,840,1))]
        for i in range(1,5):
            title.append(self.db.getTitle(random.randrange(1,840,1)))
        self.t = random.randrange(0,5,1)
        title[self.t] = titlet
        self.ui.retranslateUi(self, title[0], title[1], title[2], title[3], title [4])
        self.ui.textEdit.setText(alt)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
