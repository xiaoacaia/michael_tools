import pandas as pd

from michael_tools.excel_op.excel_op import initialize_workbook, create_sheet_to_excel, format_pd_datetime_columns
from michael_tools.file_op.unique_filepath import get_unique_filepath
from michael_tools.sql_op.connect_db import execute_sql_query
from michael_tools.sql_op.test.test_connect_db import db_config

data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
}
demo_data = pd.DataFrame(data)

def test_export_excel():
    workbook = initialize_workbook()
    create_sheet_to_excel(workbook, "sheet_name_demo", demo_data, width_multiplier=5)
    demo_data_xlsx = "demo_data.xlsx"
    workbook.save(get_unique_filepath(demo_data_xlsx))


def test_update_df_columns():
    global demo_data
    demo_data = demo_data.rename(columns={'姓名': 'Name', '年龄': 'Age'})

    # 重新排序列
    new_order = ['城市', 'Age', 'Name']
    demo_data = demo_data[new_order]

    # 删除某个列
    demo_data = demo_data.drop(columns=['Age'])

    workbook = initialize_workbook()
    create_sheet_to_excel(workbook, "sheet_name_demo", demo_data, width_multiplier=5)
    demo_data_xlsx = "demo_data.xlsx"
    workbook.save(get_unique_filepath(demo_data_xlsx))



def test_export_excel_use_db():

    sql = """
          SELECT tu.user_name, tu.real_name, tu.phone, tu.email, tu.age, tu.sex, tu.ability_level, tu.vip_level, tu.create_time, tu.modify_time
          FROM `t_user` tu
                   INNER JOIN t_user_sub_info ts ON tu.id = ts.user_id
          WHERE
              (ts.base_language = 'vi-VN'
                  OR JSON_UNQUOTE(JSON_EXTRACT(ts.exts, '$.regionCode')) = 'VN' OR (phone LIKE '84%'))
            AND (create_time LIKE '%2025-05-18%' OR modify_time LIKE '%2025-05-18%')
            AND LEFT(tu.phone, 4) != 'tour'
          ORDER BY create_time
    """
    res = execute_sql_query(db_config, sql)
    db_res = res[0]

    df = format_pd_datetime_columns(db_res)
    workbook = initialize_workbook()
    create_sheet_to_excel(workbook, "sheet_name_demo", df, width_multiplier=5)
    demo_data_xlsx = "demo_data.xlsx"
    workbook.save(get_unique_filepath(demo_data_xlsx))


def test_isinstance():
    x = 5
    print(isinstance(x, int))   # True，因为 x 是整数
    print(isinstance(x, str))   # False，因为 x 不是字符串