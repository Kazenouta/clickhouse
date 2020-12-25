from clickhouse_driver import Client
from datetime import datetime
import pandas as pd
import subprocess, os
import functools
from sqlalchemy import create_engine


# 计时器
def timer(func):
    @functools.wraps(func)
    def deco(*args, **kw):
        start = datetime.now()
        res = func(*args, **kw)
        end = datetime.now()
        delta = end - start
        print(f"{func.__name__} runed ", delta)
        return res
    return deco

@timer
def sqlalchemy():
    ENGINE_101_CH = create_engine('clickhouse://bxz:123456@192.168.123.101:8123/test')
    sql = "select open from stk_bar_1min limit 100000000"
    df1 = pd.read_sql(sql, ENGINE_101_CH)

@timer
def ch_driver():
    client = Client(host='192.168.123.101', database='test',user='bxz' ,password='123456')
    sql = "select open from stk_bar_1min prewhere s_time>=toDateTime('2020-08-01 00:00:00')"
    sql = "select open from stk_bar_1min limit 100000000"
    # df1 = HandleCH.read_sql(sql)
    data = client.execute(sql)
    # df = pd.DataFrame(data)

@timer
def http():
    sql = 'select open from test.stk_bar_1min limit 100000000'
    cmd = f"echo '{sql}' | curl 'http://192.168.123.101:8123/' --data-binary @-"
    data = subprocess.getoutput(cmd)

@timer
def tcp():
    sql = 'select open from test.b_stk_bar_1min limit 1'
    sql = 'select max(low) from test.b_stk_bar_1min'
    cmd = f"clickhouse-client --query '{sql}'"
    ret = os.system(cmd)
    # data = subprocess.getoutput(cmd)
    # data = pd.DataFrame({'open': data.split('\n')})
    # print(data)
    # return data

@timer
def tcp_02():
    sql = "select symbol, s_time, open, close from test.b_stk_bar_1min where s_time >= toDateTime('2020-06-30 09:00:00') and s_time <= toDateTime('2020-06-30 15:00:00')"
    cmd = f'clickhouse-client -t --query "{sql}"'
    print(cmd)
    ret = subprocess.getoutput(cmd)

# print('sqlalchemy: ', sqlalchemy())
# ch_driver())
tcp_02()