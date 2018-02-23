# coding=utf-8
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from creon_datareader_v0_1 import MainWindow

import win32com.client

g_objCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
g_objCpStatus = win32com.client.Dispatch('CpUtil.CpCybos')


def check_PLUS_status(original_func):
    """original_func 콜하기 전에 PLUS 연결 상태 체크하는 데코레이터"""
    def wrapper(*args, **kwargs):
        bConnect = g_objCpStatus.IsConnect
        if (bConnect == 0):
            print("PLUS가 정상적으로 연결되지 않음.")
            exit()

        return original_func(*args, **kwargs)

    return wrapper


class CpStockChart:
    def __init__(self):
        self.objStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

    def _check_rq_status(self):
        """
        self.objStockChart.BlockRequest() 로 요청한 후 이 메소드로 통신상태 검사해야함
        :return: None
        """
        rqStatus = self.objStockChart.GetDibStatus()
        rqRet = self.objStockChart.GetDibMsg1()
        if rqStatus == 0:
            print("통신상태 정상[{}]{}".format(rqStatus, rqRet), end=' ')
        else:
            print("통신상태 오류[{}]{} 종료합니다..".format(rqStatus, rqRet))
            exit()

    # 차트 요청 - 최근일 부터 개수 기준
    @check_PLUS_status
    def RequestDWM(self, code, dwm, count, caller: 'MainWindow'):
        """
        :param code: 종목코드
        :param dwm: 'd':일봉, 'w':주봉, 'm':월봉
        :param count: 요청할 데이터 개수
        :param caller: 이 메소드 호출한 인스턴스. 결과 데이터를 caller의 멤버로 전달하기 위함
        :return: None
        """
        self.objStockChart.SetInputValue(0, code)  # 종목코드
        self.objStockChart.SetInputValue(1, ord('2'))  # 개수로 받기
        self.objStockChart.SetInputValue(4, count)  # 최근 count개
        self.objStockChart.SetInputValue(5, [0, 2, 3, 4, 5, 8])  # 요청항목 - 날짜,시가,고가,저가,종가,거래량
        self.objStockChart.SetInputValue(6, dwm)  # '차트 주기 - 일/주/월
        self.objStockChart.SetInputValue(9, '1')  # 수정주가 사용

        # 요청한 항목들을 튜플로 만들어 사용
        rq_column = ('date', 'open', 'high', 'low', 'close', 'volume')

        rcv_data = {}
        for col in rq_column:
            rcv_data[col] = []

        rcv_count = 0
        while count > rcv_count:
            self.objStockChart.BlockRequest()  # 요청! 후 응답 대기
            self._check_rq_status()  # 통신상태 검사

            len = self.objStockChart.GetHeaderValue(3)  # 받아온 데이터 개수
            len = min(len, count - rcv_count)  # 정확히 count 개수만큼 받기 위함
            for i in range(len):
                for col_idx, col in enumerate(rq_column):
                    rcv_data[col].append(self.objStockChart.GetDataValue(col_idx, i))

            rcv_count += len
            print('{} / {}'.format(rcv_count, count))
            caller.return_status_msg = '{} / {}'.format(rcv_count, count)

            # 서버가 가진 모든 데이터를 요청한 경우 break.
            # self.objStockChart.Continue 는 개수로 요청한 경우
            # count만큼 이미 다 받았더라도 계속 1의 값을 가지고 있어서
            # while 조건문에서 count > rcv_count를 체크해줘야 함.
            if not self.objStockChart.Continue:
                break

        caller.rcv_data = rcv_data  # 받은 데이터를 caller의 멤버에 저장
        return

    # 차트 요청 - 분간, 틱 차트
    @check_PLUS_status
    def RequestMT(self, code, dwm, tick_range, count, caller: 'MainWindow'):
        """
        :param code: 종목 코드
        :param dwm: 'm':분봉, 'T':틱봉
        :param tick_range: 1분봉 or 5분봉, ...
        :param count: 요청할 데이터 개수
        :param caller: 이 메소드 호출한 인스턴스. 결과 데이터를 caller의 멤버로 전달하기 위함
        :return:
        """
        self.objStockChart.SetInputValue(0, code)  # 종목코드
        self.objStockChart.SetInputValue(1, ord('2'))  # 개수로 받기
        self.objStockChart.SetInputValue(4, count)  # 조회 개수
        self.objStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 8])  # 요청항목 - 날짜, 시간,시가,고가,저가,종가,거래량
        self.objStockChart.SetInputValue(6, dwm)  # '차트 주기 - 분/틱
        self.objStockChart.SetInputValue(7, tick_range)  # 분틱차트 주기
        self.objStockChart.SetInputValue(9, '1')  # 수정주가 사용

        # 요청한 항목들을 튜플로 만들어 사용
        rq_column = ('date', 'time', 'open', 'high', 'low', 'close', 'volume')

        rcv_data = {}
        for col in rq_column:
            rcv_data[col] = []

        rcv_count = 0
        while count > rcv_count:
            self.objStockChart.BlockRequest()  # 요청! 후 응답 대기
            self._check_rq_status()  # 통신상태 검사

            len = self.objStockChart.GetHeaderValue(3)  # 받아온 데이터 개수
            len = min(len, count - rcv_count)  # 정확히 count 개수만큼 받기 위함
            for i in range(len):
                for col_idx, col in enumerate(rq_column):
                    rcv_data[col].append(self.objStockChart.GetDataValue(col_idx, i))

            rcv_count += len
            print('{} / {}'.format(rcv_count, count))
            caller.return_status_msg = '{} / {}'.format(rcv_count, count)

            # 서버가 가진 모든 데이터를 요청한 경우 break.
            # self.objStockChart.Continue 는 개수로 요청한 경우
            # count만큼 이미 다 받았더라도 계속 1의 값을 가지고 있어서
            # while 조건문에서 count > rcv_count를 체크해줘야 함.
            if not self.objStockChart.Continue:
                break

        caller.rcv_data = rcv_data  # 받은 데이터를 caller의 멤버에 저장
        return
