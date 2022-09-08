from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 526)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 581, 51))
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 90, 581, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.yuzdebtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.yuzdebtn.setFont(font)
        self.yuzdebtn.setObjectName("yuzdebtn")
        self.gridLayout.addWidget(self.yuzdebtn, 0, 2, 1, 1)
        self.yuzdebtn.clicked.connect(self.yuzde)

        self.yedibtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.yedibtn.setFont(font)
        self.yedibtn.setObjectName("yedibtn")
        self.gridLayout.addWidget(self.yedibtn, 1, 0, 1, 1)
        self.yedibtn.clicked.connect(self.tus_7)

        self.dortbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dortbtn.setFont(font)
        self.dortbtn.setObjectName("dortbtn")
        self.gridLayout.addWidget(self.dortbtn, 2, 0, 1, 1)
        self.dortbtn.clicked.connect(self.tus_4)

        self.solparanbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.solparanbtn.setFont(font)
        self.solparanbtn.setObjectName("solparanbtn")
        self.gridLayout.addWidget(self.solparanbtn, 0, 0, 1, 1)
        self.solparanbtn.clicked.connect(self.paranac)

        self.birbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.birbtn.setFont(font)
        self.birbtn.setObjectName("birbtn")
        self.gridLayout.addWidget(self.birbtn, 3, 0, 1, 1)
        self.birbtn.clicked.connect(self.tus_1)

        self.ikibtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ikibtn.setFont(font)
        self.ikibtn.setObjectName("ikibtn")
        self.gridLayout.addWidget(self.ikibtn, 3, 1, 1, 1)
        self.ikibtn.clicked.connect(self.tus_2)

        self.esittirbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.esittirbtn.setFont(font)
        self.esittirbtn.setObjectName("esittirbtn")
        self.gridLayout.addWidget(self.esittirbtn, 4, 3, 1, 1)
        self.esittirbtn.clicked.connect(self.sonuc)


        self.sifirbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sifirbtn.setFont(font)
        self.sifirbtn.setObjectName("sifirbtn")
        self.gridLayout.addWidget(self.sifirbtn, 4, 1, 1, 1)
        self.sifirbtn.clicked.connect(self.tus_0)

        self.ucbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ucbtn.setFont(font)
        self.ucbtn.setObjectName("ucbtn")
        self.gridLayout.addWidget(self.ucbtn, 3, 2, 1, 1)
        self.ucbtn.clicked.connect(self.tus_3)

        self.sekizbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sekizbtn.setFont(font)
        self.sekizbtn.setObjectName("sekizbtn")
        self.gridLayout.addWidget(self.sekizbtn, 1, 1, 1, 1)
        self.sekizbtn.clicked.connect(self.tus_8)

        self.dokuzbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dokuzbtn.setFont(font)
        self.dokuzbtn.setObjectName("dokuzbtn")
        self.gridLayout.addWidget(self.dokuzbtn, 1, 2, 1, 1)
        self.dokuzbtn.clicked.connect(self.tus_9)

        self.eksibtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eksibtn.setFont(font)
        self.eksibtn.setObjectName("eksibtn")
        self.gridLayout.addWidget(self.eksibtn, 3, 3, 1, 1)
        self.eksibtn.clicked.connect(self.eksi)

        self.artibtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.artibtn.setFont(font)
        self.artibtn.setObjectName("artibtn")
        self.gridLayout.addWidget(self.artibtn, 2, 3, 1, 1)
        self.artibtn.clicked.connect(self.arti)

        self.bolbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bolbtn.setFont(font)
        self.bolbtn.setObjectName("slasbtn")
        self.gridLayout.addWidget(self.bolbtn, 0, 3, 1, 1)
        self.bolbtn.clicked.connect(self.bol)

        self.clearbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clearbtn.setFont(font)
        self.clearbtn.setObjectName("clearbtn")
        self.gridLayout.addWidget(self.clearbtn, 4, 0, 1, 1)
        self.clearbtn.clicked.connect(self.sil)

        self.altibtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.altibtn.setFont(font)
        self.altibtn.setObjectName("altibtn")
        self.gridLayout.addWidget(self.altibtn, 2, 2, 1, 1)
        self.altibtn.clicked.connect(self.tus_6)

        self.carpbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.carpbtn.setFont(font)
        self.carpbtn.setObjectName("carpbtn")
        self.gridLayout.addWidget(self.carpbtn, 1, 3, 1, 1)
        self.carpbtn.clicked.connect(self.carp)

        self.besbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.besbtn.setFont(font)
        self.besbtn.setObjectName("besbtn")
        self.gridLayout.addWidget(self.besbtn, 2, 1, 1, 1)
        self.besbtn.clicked.connect(self.tus_5)

        self.noktabtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.noktabtn.setFont(font)
        self.noktabtn.setObjectName("noktabtn")
        self.gridLayout.addWidget(self.noktabtn, 4, 2, 1, 1)
        self.noktabtn.clicked.connect(self.tus_nokta)

        self.sagparanbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sagparanbtn.setFont(font)
        self.sagparanbtn.setObjectName("sagparanbtn")
        self.gridLayout.addWidget(self.sagparanbtn, 0, 1, 1, 1)
        self.sagparanbtn.clicked.connect(self.parankapa)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(450, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HesapMakinesi"))
        self.yuzdebtn.setText(_translate("Dialog", "Mod"))
        self.yedibtn.setText(_translate("Dialog", "7"))
        self.dortbtn.setText(_translate("Dialog", "4"))
        self.solparanbtn.setText(_translate("Dialog", "("))
        self.birbtn.setText(_translate("Dialog", "1"))
        self.ikibtn.setText(_translate("Dialog", "2"))
        self.esittirbtn.setText(_translate("Dialog", "="))
        self.sifirbtn.setText(_translate("Dialog", "0"))
        self.ucbtn.setText(_translate("Dialog", "3"))
        self.sekizbtn.setText(_translate("Dialog", "8"))
        self.dokuzbtn.setText(_translate("Dialog", "9"))
        self.eksibtn.setText(_translate("Dialog", "-"))
        self.artibtn.setText(_translate("Dialog", "+"))
        self.bolbtn.setText(_translate("Dialog", "/"))
        self.clearbtn.setText(_translate("Dialog", "C"))
        self.altibtn.setText(_translate("Dialog", "6"))
        self.carpbtn.setText(_translate("Dialog", "X"))
        self.besbtn.setText(_translate("Dialog", "5"))
        self.noktabtn.setText(_translate("Dialog", "."))
        self.sagparanbtn.setText(_translate("Dialog", ")"))
        self.label.setText(_translate("Dialog", "Made by encoderas"))


    def tus_1(self):
        icerik = self.lineEdit.text()
        icerik += "1"
        self.lineEdit.setText(icerik)


    def tus_2(self):
        icerik = self.lineEdit.text()
        icerik += "2"
        self.lineEdit.setText(icerik)

    def tus_3(self):
        icerik = self.lineEdit.text()
        icerik += "3"
        self.lineEdit.setText(icerik)

    def tus_4(self):
        icerik = self.lineEdit.text()
        icerik += "4"
        self.lineEdit.setText(icerik)

    def tus_5(self):
        icerik = self.lineEdit.text()
        icerik += "5"
        self.lineEdit.setText(icerik)

    def tus_6(self):
        icerik = self.lineEdit.text()
        icerik += "6"
        self.lineEdit.setText(icerik)

    def tus_7(self):
        icerik = self.lineEdit.text()
        icerik += "7"
        self.lineEdit.setText(icerik)

    def tus_8(self):
        icerik = self.lineEdit.text()
        icerik += "8"
        self.lineEdit.setText(icerik)

    def tus_9(self):
        icerik = self.lineEdit.text()
        icerik += "9"
        self.lineEdit.setText(icerik)

    def tus_0(self):
        icerik = self.lineEdit.text()
        icerik += "0"
        self.lineEdit.setText(icerik)

    def tus_nokta(self):
        icerik = self.lineEdit.text()
        icerik += "."
        self.lineEdit.setText(icerik)


    def paranac(self):
        icerik = self.lineEdit.text()
        icerik += "("
        self.lineEdit.setText(icerik)

    def parankapa(self):
        icerik = self.lineEdit.text()
        icerik += ")"
        self.lineEdit.setText(icerik)

    def yuzde(self):
        icerik = self.lineEdit.text()
        icerik += "%"
        self.lineEdit.setText(icerik)

    def arti(self):
        icerik = self.lineEdit.text()
        icerik += "+"
        self.lineEdit.setText(icerik)

    def eksi(self):
        icerik = self.lineEdit.text()
        icerik += "-"
        self.lineEdit.setText(icerik)

    def bol(self):
        icerik = self.lineEdit.text()
        icerik += "/"
        self.lineEdit.setText(icerik)

    def carp(self):
        icerik = self.lineEdit.text()
        icerik += "*"
        self.lineEdit.setText(icerik)

    def sonuc(self):
        icerik = self.lineEdit.text()
        try:
            icerik = eval(icerik)
            self.lineEdit.setText(str(icerik))
        except:
            self.lineEdit.setText("")


    def sil(self):
        byt = len(self.lineEdit.text())
        icerik = self.lineEdit.text()
        self.lineEdit.setText(icerik[:byt-1:])
        #self.lineEdit.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

