from michael_tools.file_op.read_file import read_file
from michael_tools.txt_operation.remove_trailing_newline import remove_trailing_newline

def test_remove_trailing_newline():
    print(remove_trailing_newline(read_file("ref.txt")))