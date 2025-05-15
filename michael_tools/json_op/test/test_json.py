from michael_tools.file_op.read_file import read_file
from michael_tools.file_op.write_file import write_to_file
from michael_tools.json_op.json_op import dict_to_str, read_file_to_dict, write_dict_to_file, str_to_dict

data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "hobbies": ["reading", "coding"]
}
foo_json = "foo.json"


def test_convert():
    print(type(data))  # <class 'dict'>

    json_str = dict_to_str(data)
    print(type(json_str))  # <class 'str'>
    write_to_file(foo_json, json_str)

    str = str_to_dict(json_str)
    print(type(str))  # <class 'dict'>


def test_read_json_file():
    json_file = read_file(foo_json)
    print(type(json_file))  # <class 'str'>

    json_str = read_file_to_dict(foo_json)
    print(type(json_str))  # <class 'dict'>


def test_write_to_file():
    print(type(data))  # <class 'dict'>
    write_dict_to_file(data, "foo2.json")
