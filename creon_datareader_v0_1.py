# coding=utf-8
import sys
import pandas as pd
import sqlite3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import decorators
import creonAPI

form_class = uic.loadUiType("creon_datareader_v0_1.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.objChart = creonAPI.CpStockChart()

        self.rcv_data = dict()  # RQ후 받아온 데이터 저장 멤버
        self.return_status_msg = ''  # status bar 에 출력할 메세지 저장 멤버

        # timer 등록. tick per 1s
        self.timer_1s = QTimer(self)
        self.timer_1s.start(1000)
        self.timer_1s.timeout.connect(self.timeout_1s)

        # label '종목코드' 오른쪽 lineEdit 값이 변경 될 시 실행될 함수 연결
        self.lineEdit.textChanged.connect(self.codeEditChanged)
        self.lineEdit.setText('005930')  #삼성전자 종목코드로 초기화

        # pushButton '실행'이 클릭될 시 실행될 함수 연결
        self.pushButton.clicked.connect(self.fetch_chart_data)

    def timeout_1s(self):
        current_time = QTime.currentTime()

        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        if self.return_status_msg == '':
            statusbar_msg = time_msg
        else:
            statusbar_msg = time_msg + " | " + self.return_status_msg

        self.statusbar.showMessage(statusbar_msg)

    # label '종목' 우측의 lineEdit의 이벤트 핸들러
    def codeEditChanged(self):
        code = self.lineEdit.text()
        self.setCode(code)

    def setCode(self, code):
        if len(code) < 6:
            return

        if not (code[0] == "A"):
            code = "A" + code

        name = creonAPI.g_objCodeMgr.CodeToName(code)

        if len(name) == 0:
            print("종목코드 확인")
            return

        self.lineEdit.setText(code)
        self.lineEdit_2.setText(name)

    @decorators.return_status_msg_setter
    def fetch_chart_data(self):

        code = self.lineEdit.text()
        tick_unit = self.comboBox.currentText()
        tick_range = int(self.comboBox_2.currentText())
        count = int(self.lineEdit_3.text())

        # 일봉 데이터 받기
        if tick_unit == '일봉':
            if self.objChart.RequestDWM(code, ord('D'), count, self) == False:
                exit()

        # 분봉 데이터 받기
        elif tick_unit == '분봉':
            if self.objChart.RequestMT(code, ord('m'), tick_range, count, self) == False:
                exit()

            # 분봉의 경우 날짜와 시간을 하나의 문자열로 합침
            self.rcv_data['date'][:] = list(map(lambda x, y: '{}{:04}'.format(x, y),
                                                self.rcv_data['date'], self.rcv_data['time']))

        # sqlite3 .db 파일로 데이터 저장
        df = pd.DataFrame(self.rcv_data, columns=['open', 'high', 'low', 'close', 'volume'],
                index=self.rcv_data['date'])

        con = sqlite3.connect("./stock_price.db")
        df.to_sql(code, con, if_exists='replace')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
