from .config import *
import pandas as pd
import os, re, subprocess
from datetime import datetime


# 计时器
def timer(func):
    @functools.wraps(func)
    def deco(*args, **kw):
        start = datetime.now()
        res = func(*args, **kw)
        end = datetime.now()
        delta = end - start
        print("func runed ", delta)
        return res
    return deco

class HandleCH:

    @staticmethod
    def read_sql(sql, engine=ENGINE_101_CH):
        df = pd.read_sql(sql, engine)

        return df

class HandleORA:
    @staticmethod
    def read_sql(sql, engine=ENGINE_100_ORA):
        df = pd.read_sql(sql, engine)

        return df