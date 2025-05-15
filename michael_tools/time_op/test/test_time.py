from michael_tools.time_op.time_op import get_current_date_str, get_current_time_str, to_logger_time, get_current_time, \
    get_n_days_ago


def test_time():
    print()
    print(get_current_time())  # 2025-05-15 23:35:38.241667
    print(get_n_days_ago(1))  # 2025-05-14 23:35:38.241684
    print(get_current_time_str())  # 2025-05-15 23:35:38
    print(get_current_date_str())  # 2025-05-15
    print(to_logger_time(get_current_time()))  # 15/May/2025
