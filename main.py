from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enter_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_lineEdit.setText("")
        self.enter_lineEdit.setObjectName("enter_lineEdit")
        self.verticalLayout.addWidget(self.enter_lineEdit)
        self.page_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.page_textBrowser.setObjectName("page_textBrowser")
        self.verticalLayout.addWidget(self.page_textBrowser)
        self.scrap_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.scrap_pushButton.clicked.connect(self.scrapWeb)
        self.scrap_pushButton.setObjectName("scrap_pushButton")
        self.verticalLayout.addWidget(self.scrap_pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def scrapWeb(self):
        lineedit = self.enter_lineEdit.text()
        html = urlopen(lineedit)
        bsobj = BeautifulSoup(html, 'lxml')
        self.page_textBrowser.append(str(bsobj))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scrapping Application"))
        self.enter_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Website URL"))
        self.scrap_pushButton.setText(_translate("MainWindow", "Scrap URL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
