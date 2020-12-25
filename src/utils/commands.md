- 查询
clickhouse-client -t --query 'select count(*) from ark.stk_bar_1min'

- 表重命名
rename table default.dept to scott.dept;


- 导入数据
clickhouse-client -t --query "INSERT INTO ark.b_stk_bar_1min FORMAT CSVWithNames" --max_insert_block_size=1000000 < 20170101_20201010.csv.his

- 导出到CSV
clickhouse-client -t --query "select open from test.stk_bar_1min prewhere s_time>=toDateTime('2020-08-01 00:00:00') FORMAT CSV" > open_>20200801.csv

- 远程连接
    1. 取消config.xml文件中的<listen_host>::</listen_host>注释
    2. 打开防火墙
        sudo firewall-cmd --query-port=80/tcp
        sudo firewall-cmd --permanent --add-port=80/tcp
        sudo service firewalld restart
    3. 新建 /etc/metrika.xml 文件, 写入
        <yandex> 
            <networks> 
                <ip>::/0</ip> 
            </networks>
        </yandex>