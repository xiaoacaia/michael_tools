import pandas as pd

from michael_tools.excel_op.excel_op import initialize_workbook, create_sheet_to_excel
from michael_tools.file_op.unique_filepath import get_unique_filepath

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
