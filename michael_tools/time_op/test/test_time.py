from michael_tools.time_op.time_op import get_current_date_str, get_current_time_str, to_logger_time, get_current_time, \
    get_n_days_ago


def test_time():
    print()
    print(get_current_time())  # 2025-05-14 14:41:24.497731
    print(get_n_days_ago(1))  # 2025-05-13 14:41:24.497748
    print(get_current_time_str())  # 2025-05-14 14:41:24
    print(get_current_date_str())  # 2025-05-14
    print(to_logger_time(get_current_time()))  # 14/May/2025
