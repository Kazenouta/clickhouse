from clickhouse_driver import Client
from sqlalchemy import create_engine

ENGINE_100_ORA = create_engine('oracle://c##ark:E2718281828@192.168.123.100:1521/ORCLCDB', echo=False,max_identifier_length=128)


ENGINE_100_CH = Client(
    host='192.168.123.100', 
    database='ark',user='ark' ,
    password='E2718281828')

ENGINE_101_CH = Client(
    host='192.168.123.101', 
    database='ark',user='bxz',
    password='123456')