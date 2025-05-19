import pymysql

from michael_tools.json_op.json_op import read_file_to_dict
from michael_tools.sql_op.connect_db import db_connection_test, execute_sql_query

# 获取配置文件的绝对路径
db_config = read_file_to_dict('db_config.json')
db_config['cursorclass'] = pymysql.cursors.DictCursor

def test_connect():
    assert db_connection_test(db_config) == True

def test_query():
    sql = """SELECT COUNT(*) FROM `t_apply`"""
    res = execute_sql_query(db_config, sql)
    print(f"result: {res}")