#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import sys, random
from database import ComicsDB
import functools as ft

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(321, 548)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 301, 511))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.textEdit = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
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
        self.ui.label.setText("Score : %d" % self.score)
 

    def checkAnswer(self, x):
        x = x - 1
        if x == self.t:
            self.score = self.score + 1
            self.ui.label.setText("Score : %d" % self.score)
            self.load()
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
