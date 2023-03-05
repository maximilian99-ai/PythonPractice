from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(5, 150, 80, 40))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(95, 150, 80, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(185, 150, 80, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 200, 80, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(95, 200, 80, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(185, 200, 80, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(5, 250, 80, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(95, 250, 80, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(185, 250, 80, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(95, 300, 80, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 5, 80, 330))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{ \n"
        "border : 2px solid black;\n"
        "background : white;\n"
        "}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", " "))

        # adding action to each of the button
        self.pushButton_1.clicked.connect(self.action1)
        self.pushButton_2.clicked.connect(self.action2)
        self.pushButton_3.clicked.connect(self.action3)
        self.pushButton_4.clicked.connect(self.action4)
        self.pushButton_5.clicked.connect(self.action5)
        self.pushButton_6.clicked.connect(self.action6)
        self.pushButton_7.clicked.connect(self.action7)
        self.pushButton_8.clicked.connect(self.action8)
        self.pushButton_9.clicked.connect(self.action9)
        self.pushButton_10.clicked.connect(self.action_clear)


    def action1(self):
        # appending label text
        self.label.setText("1×1= 1\n1×2= 2\n1×3= 3\n1×4= 4\n1×5= 5\n1×6= 6\n1×7= 7\n1×8= 8\n1×9= 9")

    def action2(self):
        # appending label text
        self.label.setText("2×1= 2\n2×2= 4\n2×3= 6\n2×4= 8\n2×5=10\n2×6=12\n2×7=14\n2×8=16\n2×9=18")

    def action3(self):
        # appending label text
        self.label.setText("3×1= 3\n3×2= 6\n3×3= 9\n3×4=12\n3×5=15\n3×6=18\n3×7=21\n3×8=24\n3×9=27")

    def action4(self):
        # appending label text
        self.label.setText("4×1= 4\n4×2= 8\n4×3=12\n4×4=16\n4×5=20\n4×6=24\n4×7=28\n4×8=32\n4×9=36")

    def action5(self):
        # appending label text
        self.label.setText("5×1= 5\n5×2=10\n5×3=15\n5×4=20\n5×5=25\n5×6=30\n5×7=35\n5×8=40\n5×9=45")

    def action6(self):
        # appending label text
        self.label.setText("6×1= 6\n6×2=12\n6×3=18\n6×4=24\n6×5=30\n6×6=36\n6×7=42\n6×8=48\n6×9=54")

    def action7(self):
        # appending label text
        self.label.setText("7×1= 7\n7×2=14\n7×3=21\n7×4=28\n7×5=35\n7×6=42\n7×7=49\n7×8=56\n7×9=63")

    def action8(self):
        # appending label text
        self.label.setText("8×1= 8\n8×2=16\n8×3=24\n8×4=32\n8×5=40\n8×6=48\n8×7=56\n8×8=64\n8×9=72")

    def action9(self):
        # appending label text
        self.label.setText("9×1= 9\n9×2=18\n9×3=27\n9×4=36\n9×5=45\n9×6=54\n9×7=63\n9×8=72\n9×9=81")

    def action_clear(self):
        # clearing the label text
        self.label.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())