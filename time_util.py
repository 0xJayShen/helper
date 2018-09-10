# -*- coding: utf8 -*-
import datetime
import time


# 当前时间，可用于mysql datetime
def now_datetime_string():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def now_datetime():
    return datetime.datetime.now()


def now_date_string():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def now_timestamp():
    return time.time()
