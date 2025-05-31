from michael_tools.file_op.read_file import read_file
from michael_tools.txt_operation.llm_format_change import convert_latex_format

def test_llm_format_change():
    res = convert_latex_format(read_file("llm_output.txt"))
    print()
    print(res)