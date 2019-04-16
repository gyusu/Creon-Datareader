import datetime as dt

def is_market_open():
    # 장 중이면 True, 아니면 False 리턴
    now = dt.datetime.now()

    if now.hour > 15 and now.minute > 30:
        return False
    if now.hour < 9:
        return False
    return True

def available_latest_date():
    now = dt.datetime.now()
    if is_market_open():
        return None

    if now.hour > 15:
        latest_date = now.replace(hour=15, minute=30)
        return cvt_dt_to_int(latest_date)
    else:
        latest_date = now.replace(hour=15, minute=30)
        latest_date = latest_date - dt.timedelta(days=1)
        return cvt_dt_to_int(latest_date)

def cvt_dt_to_int(date_time):
    return int(date_time.strftime("%Y%m%d%H%M"))
