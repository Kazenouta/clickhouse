from src.utils.funcs import *
from src.utils.config import *

class HandleCH:
    
    @staticmethod
    def create_engine(kw='100_ark'):
        from clickhouse_driver import Client
        if kw == '100_ark':
            engine = Client(
                host='192.168.123.100', 
                database='ark',user='ark' ,
                password='E2718281828')
        elif kw == '101_ark':
            engine = Client(
                host='192.168.123.101', 
                database='ark',user='bxz',
                password='123456')
        
        return engine

    @staticmethod
    def exe_cmd(cmd):
        ret = os.system(cmd)
        if ret != 0: raise Exception(f'"{cmd}" failed!')
        else: print(f'"{cmd}" success!')

    @staticmethod
    def drop_db(db_name='ark'):
        cmd = f"clickhouse-client --query 'drop database if exists {db_name}'"
        HandleCH.exe_cmd(cmd)

    @staticmethod
    def create_db(db_name='ark'):
        HandleCH.drop_db(db_name)
        cmd = f"clickhouse-client --query 'create database {db_name}'"
        HandleCH.exe_cmd(cmd)

    @staticmethod
    def drop_tb(tb_name, db_name='ark'):
        sql = f'DROP TABLE IF EXISTS {db_name}.{tb_name}'
        cmd = f"clickhouse-client --query '{sql}'"
        HandleCH.exe_cmd(cmd)

    @staticmethod
    def create_tb(
        tb_name, db_name='ark',
        partition_by='t_date', 
        order_by=['symbol', 't_date'],
        index_granularity=8192):

        order_by = ','.join(order_by)
        sql = f'''CREATE TABLE {db_name}.{tb_name}
            (
                `symbol` String,
                `t_date` DateTime,
                `s_time` DateTime,
                `e_time` DateTime,
                `open`   Float32,
                `high`   Float32,
                `low`    Float32,
                `close`  Float32,
                `volume` Float32,
                `amount`  Float32,
                `change` Float32,
                `ret`    Float32
            )
            ENGINE = MergeTree()
            PARTITION BY toYYYYMM({partition_by})
            ORDER BY ({order_by})
            SETTINGS index_granularity = {index_granularity};
        '''
        cmd = f"clickhouse-client --query '{sql}'"
        HandleCH.exe_cmd(cmd)

    @staticmethod
    def load_data(tb_name, path=None, db_name='ark'):
        if path == None:
            path = '/data/ark/rawdata/choice/stock/b_stk_bar_5min/20170101_20201010.csv.his'
        sql = f'INSERT INTO {db_name}.{tb_name} FORMAT CSVWithNames'
        cmd = f"""clickhouse-client -t --query '{sql}' --max_insert_block_size=1000000 < {path}"""
        HandleCH.exe_cmd(cmd)

    @staticmethod
    def read_sql(sql, engine='101_ark', _type='df'):
        engine = HandleCH.create_engine(engine)
        if _type == 'list':
            data, columns = engine.execute(
                sql, columnar=True, 
                with_column_types=True)
        elif _type == 'df':
            data, columns = engine.execute(
                sql, columnar=True, 
                with_column_types=True)
            data = pd.DataFrame({re.sub(r'\W', '_', col[0]): d for d, col in zip(data, columns)})
        elif _type == 'str':
            cmd = f'clickhouse-client -t --query "{sql}"'
            data = subprocess.getoutput(cmd)

        return data

    @staticmethod
    def to_sql(df, tb_name, db_name='ark', engine='101_ark'):
        engine = HandleCH.create_engine(engine)
        columns = df.columns.tolist()
        data = df.to_dict('records')
        engine.execute(
            f"INSERT INTO {tb_name} ({','.join(columns)}) VALUES",
            df.to_dict('records'))

    @staticmethod
    def log(sql, engine=ENGINE_101_CH):
        cmd = f'clickhouse-client --send_logs_level=debug <<< "{sql}" > /dev/null'
        ret = subprocess.getoutput(cmd)
        log_path = os.path.expanduser('~/projects/clickhouse/src/log/query.log')
        with open(log_path, 'a') as f:
            f.write('\n')
            f.write(ret)
            f.write('\n') 