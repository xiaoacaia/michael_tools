GitHub: https://github.com/xiaoacaia/michael_tools
pypi: https://pypi.org/project/michael-tools
Personal toolkit

file_operation
- create_file(file_path)
- delete_file(file_path)
- read_file(file_path)
- write_to_file(file_path, content)
- append_to_file(file_path, content)
- get_unique_filepath(file_name)

json_operation
- dict_to_str(python_obj)
- str_to_dict(json_str)
- read_file_to_dict(file_path)
- write_dict_to_file(python_obj, file_path)

time_operation
- get_current_time()
- get_n_days_ago(n)
- get_current_time_str()
- get_current_date_str()

openapi_operation
- call_model(prompt, model_name="deepseek-r1", show_process=True, stream=True)

txt_operation
- remove_trailing_newline(txt)

`0.0.6` add openapi_op
`0.0.5` add time

Hope it helps you!