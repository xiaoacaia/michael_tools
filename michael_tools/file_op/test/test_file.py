from michael_tools.file_op.create_file import create_file
from michael_tools.file_op.delete_file import delete_file
from michael_tools.file_op.read_file import read_file
from michael_tools.file_op.unique_filepath import get_unique_filepath
from michael_tools.file_op.dir_op import get_curr_work_dir, get_upper_dir, path_join
from michael_tools.file_op.write_file import write_to_file, append_to_file

test_filename = "llm_output.txt"


def test_get_curr_work_dir():
    print(get_curr_work_dir())


def test_get_upper_dir():
    print(get_upper_dir())


def test_path_join():
    print(path_join(get_upper_dir(), test_filename))


def test_create_file():
    create_file(test_filename)
    create_file(test_filename)


def test_delete_file():
    delete_file(test_filename)


def test_read_file():
    content = read_file(test_filename)
    print(f"content: {content}")


def test_write_file():
    write_to_file(test_filename, "hello world")


def test_append_file():
    append_to_file(test_filename, "\nhello world")


def test_get_unique_filepath():
    unique_filepath = get_unique_filepath(test_filename)
    print(f"unique_filepath: {unique_filepath}")
