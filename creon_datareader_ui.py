# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creon_datareader.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1175, 893)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 20, 821, 811))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 361, 641))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setGeometry(QtCore.QRect(10, 30, 341, 601))
        self.tableView.setObjectName("tableView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 160, 431, 641))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableView_2 = QtWidgets.QTableView(self.groupBox_3)
        self.tableView_2.setGeometry(QtCore.QRect(10, 30, 411, 601))
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 100, 101, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 30, 101, 61))
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(65, 30, 81, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(155, 30, 291, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 120, 221, 31))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(29, 117, 111, 31))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 29, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 131, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(155, 60, 291, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 59, 71, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(540, 30, 106, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(540, 60, 116, 22))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(870, 29, 291, 801))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1175, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Creon_datareader v1.2"))
        self.groupBox_4.setTitle(_translate("MainWindow", "주가 데이터베이스 관리"))
        self.groupBox_2.setTitle(_translate("MainWindow", "PLUS 서버 DB"))
        self.groupBox_3.setTitle(_translate("MainWindow", "로컬 DB"))
        self.pushButton_4.setText(_translate("MainWindow", "전체\n"
"다운로드"))
        self.pushButton_3.setText(_translate("MainWindow", "검색 결과만\n"
"다운로드"))
        self.label_9.setText(_translate("MainWindow", "DB 경로"))
        self.lineEdit_4.setText(_translate("MainWindow", "./db/stock_price(5min).db"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "종목코드 or 종목명"))
        self.label_12.setText(_translate("MainWindow", "종목 필터"))
        self.pushButton_2.setText(_translate("MainWindow", "연결"))
        self.label_10.setText(_translate("MainWindow", "종목리스트 경로"))
        self.lineEdit_8.setText(_translate("MainWindow", "./db/code_list.csv"))
        self.pushButton_8.setText(_translate("MainWindow", "연결"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1분봉"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5분봉"))
        self.comboBox.setItemText(2, _translate("MainWindow", "일봉"))
        self.comboBox.setItemText(3, _translate("MainWindow", "주봉"))
        self.comboBox.setItemText(4, _translate("MainWindow", "월봉"))
        self.checkBox.setText(_translate("MainWindow", "ohlcv only"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">### 사용법 ###</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">step 0. Creon Plus에 로그인되어 있어야 함!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">step 1. DB 경로 입력 후 [연결] 버튼 클릭</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - db 파일이 새 파일인 경우 분봉/일봉 선택 가능</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - 기존에 사용하던 파일인 경우, 기존 데이터에 맞게 자동 선택됨</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">step 2. 다운로드</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    case A. 전체 종목(코스피 + 코스닥) 다운로드.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         - [전체 다운로드] 클릭</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    case B. 종목 검색하여 다운로드.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         - [종목 필터] 검색창에 종목코드/명 입력 후 [Enter]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         - [검색 결과만 다운로드] 클릭</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    case C. 미리 생성해놓은 \'종목리스트\'에 대해 다운로드.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         - 종목리스트 경로 입력 후 [연결] 버튼 클릭</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">         - [검색 결과만 다운로드] 클릭</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

