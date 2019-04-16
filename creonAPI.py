# coding=utf-8
import win32com.client
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from creon_datareader_v1_0 import MainWindow

g_objCpStatus = win32com.client.Dispatch('CpUtil.CpCybos')


# original_func 콜하기 전에 PLUS 연결 상태 체크하는 데코레이터
def check_PLUS_status(original_func):

    def wrapper(*args, **kwargs):
        bConnect = g_objCpStatus.IsConnect
        if (bConnect == 0):
            print("PLUS가 정상적으로 연결되지 않음.")
            exit()

        return original_func(*args, **kwargs)

    return wrapper


# 서버로부터 과거의 차트 데이터 가져오는 클래스
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
    def RequestDWM(self, code, dwm, count, caller: 'MainWindow', from_date=0):
        """
        :param code: 종목코드
        :param dwm: 'D':일봉, 'W':주봉, 'M':월봉
        :param count: 요청할 데이터 개수
        :param caller: 이 메소드 호출한 인스턴스. 결과 데이터를 caller의 멤버로 전달하기 위함
        :return: None
        """
        self.objStockChart.SetInputValue(0, code)  # 종목코드
        self.objStockChart.SetInputValue(1, ord('2'))  # 개수로 받기
        self.objStockChart.SetInputValue(4, count)  # 최근 count개
        self.objStockChart.SetInputValue(5, [0, 2, 3, 4, 5, 8])  # 요청항목 - 날짜,시가,고가,저가,종가,거래량
        self.objStockChart.SetInputValue(6, dwm)  # '차트 주기 - 일/주/월
        self.objStockChart.SetInputValue(9, ord('1'))  # 수정주가 사용

        # 요청한 항목들을 튜플로 만들어 사용
        rq_column = ('date', 'open', 'high', 'low', 'close', 'volume')

        rcv_data = {}
        for col in rq_column:
            rcv_data[col] = []

        rcv_count = 0
        while count > rcv_count:
            self.objStockChart.BlockRequest()  # 요청! 후 응답 대기
            self._check_rq_status()  # 통신상태 검사
            time.sleep(0.25)  # 시간당 RQ 제한으로 인해 장애가 발생하지 않도록 딜레이를 줌

            rcv_batch_len = self.objStockChart.GetHeaderValue(3)  # 받아온 데이터 개수
            rcv_batch_len = min(rcv_batch_len, count - rcv_count)  # 정확히 count 개수만큼 받기 위함
            for i in range(rcv_batch_len):
                for col_idx, col in enumerate(rq_column):
                    rcv_data[col].append(self.objStockChart.GetDataValue(col_idx, i))

            if len(rcv_data['date']) == 0:  # 데이터가 없는 경우
                print(code, '데이터 없음')
                return False

            # rcv_batch_len 만큼 받은 데이터의 가장 오래된 date
            rcv_oldest_date = rcv_data['date'][-1]

            rcv_count += rcv_batch_len
            print('{} / {}'.format(rcv_count, count))
            caller.return_status_msg = '{} / {}'.format(rcv_count, count)

            # 서버가 가진 모든 데이터를 요청한 경우 break.
            # self.objStockChart.Continue 는 개수로 요청한 경우
            # count만큼 이미 다 받았더라도 계속 1의 값을 가지고 있어서
            # while 조건문에서 count > rcv_count를 체크해줘야 함.
            if not self.objStockChart.Continue:
                break
            if rcv_oldest_date < from_date:
                break

        caller.rcv_data = rcv_data  # 받은 데이터를 caller의 멤버에 저장
        return True

    # 차트 요청 - 분간, 틱 차트
    @check_PLUS_status
    def RequestMT(self, code, dwm, tick_range, count, caller: 'MainWindow', from_date=0):
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
        self.objStockChart.SetInputValue(9, ord('1'))  # 수정주가 사용

        # 요청한 항목들을 튜플로 만들어 사용
        rq_column = ('date', 'time', 'open', 'high', 'low', 'close', 'volume')

        rcv_data = {}
        for col in rq_column:
            rcv_data[col] = []

        rcv_count = 0
        while count > rcv_count:
            self.objStockChart.BlockRequest()  # 요청! 후 응답 대기
            self._check_rq_status()  # 통신상태 검사
            time.sleep(0.25)  # 시간당 RQ 제한으로 인해 장애가 발생하지 않도록 딜레이를 줌

            rcv_batch_len = self.objStockChart.GetHeaderValue(3)  # 받아온 데이터 개수
            rcv_batch_len = min(rcv_batch_len, count - rcv_count)  # 정확히 count 개수만큼 받기 위함
            for i in range(rcv_batch_len):
                for col_idx, col in enumerate(rq_column):
                    rcv_data[col].append(self.objStockChart.GetDataValue(col_idx, i))

            if len(rcv_data['date']) == 0:  # 데이터가 없는 경우
                print(code, '데이터 없음')
                return False

            # len 만큼 받은 데이터의 가장 오래된 date
            rcv_oldest_date = int('{}{:04}'.format(rcv_data['date'][-1], rcv_data['time'][-1]))

            rcv_count += rcv_batch_len
            print('{} / {}'.format(rcv_count, count))
            caller.return_status_msg = '{} / {}(maximum)'.format(rcv_count, count)

            # 서버가 가진 모든 데이터를 요청한 경우 break.
            # self.objStockChart.Continue 는 개수로 요청한 경우
            # count만큼 이미 다 받았더라도 계속 1의 값을 가지고 있어서
            # while 조건문에서 count > rcv_count를 체크해줘야 함.
            if not self.objStockChart.Continue:
                break
            if rcv_oldest_date < from_date:
                break

        # 분봉의 경우 날짜와 시간을 하나의 문자열로 합친 후 int로 변환
        rcv_data['date'] = list(map(lambda x, y: int('{}{:04}'.format(x, y)),
                 rcv_data['date'], rcv_data['time']))
        del rcv_data['time']
        caller.rcv_data = rcv_data  # 받은 데이터를 caller의 멤버에 저장
        return True

# 종목코드 관리하는 클래스
class CpCodeMgr:
    def __init__(self):
        self.objCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

    # 마켓에 해당하는 종목코드 리스트 반환하는 메소드
    def get_code_list(self, market):
        """
        :param market: 1:코스피, 2:코스닥, ...
        :return: market에 해당하는 코드 list
        """
        code_list = self.objCodeMgr.GetStockListByMarket(market)
        return code_list

    # 부구분코드를 반환하는 메소드
    def get_section_code(self, code):
        section_code = self.objCodeMgr.GetStockSectionKind(code)
        return section_code

    # 종목 코드를 받아 종목명을 반환하는 메소드
    def get_code_name(self, code):
        code_name = self.objCodeMgr.CodeToName(code)
        return code_name
