GitHub: https://github.com/xiaoacaia/michael_tools
pypi: https://pypi.org/project/michael-tools
Personal toolkit

测试代码，在 GitHub 工具函数，同级目录下的 test 文件中
需安装：pip install pytest

file_operation
- create_file(file_path)
- delete_file(file_path)
- read_file(file_path)
- write_to_file(file_path, content)
- append_to_file(file_path, content)
- get_unique_filepath(file_name)
- get_curr_work_dir()
- get_upper_dir(path=None)
- path_join(*parts)

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
- call_model_verbose(prompt)
- call_model(prompt, model_name="deepseek-r1")
- ChatSession.load_from_file(file_name)
- chat.send_message(self, message)

txt_operation
- remove_trailing_newline(txt)
  
`0.1.3` chat_session
`0.0.9` call_model_verbose
`0.0.7` add file_op
`0.0.6` add openapi_op
`0.0.5` add time

Hope it helps you!