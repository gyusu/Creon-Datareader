# coding=utf-8
import datetime


def call_printer(original_func):
    """original 함수 call 시, 현재 시간과 함수 명을 출력하는 데코레이터"""
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print('[{:.22s}] func `{}` is called'.format(timestamp, original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper


def return_status_msg_setter(original_func):
    """
    original 함수 exit 후, QMainWindow 인스턴스의 statusbar에 표시할 문자열을 수정하는 데코레이터
    이 데코레이터는 QMainWindow 클래스의 메소드에만 사용하여야 함
    args[0]는 self 를 참조하게 된다
    """
    def wrapper(*args, **kwargs):
        ret = original_func(*args, **kwargs)

        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        msg = '`{}` 완료됨[{}]'.format(original_func.__name__, timestamp)
        print(msg)
        args[0].return_status_msg = msg

        return ret

    return wrapper
