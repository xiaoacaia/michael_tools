from michael_tools.openapi_op.multi_chat import ChatSession

def test_first_chat_demo():
    chat = ChatSession()
    # 第一轮对话
    print("=" * 20 + "第一轮对话" + "=" * 20)
    thinking, reply = chat.send_message("你好", show_process=True, stream=True)
    # 第二轮对话
    print("=" * 20 + "第二轮对话" + "=" * 20)
    thinking, reply = chat.send_message("你是谁", show_process=True, stream=True)
    # 显示完整对话历史
    print("=" * 20 + "对话历史" + "=" * 20)
    for msg in chat.get_history():
        print(f"{msg['role']}: {msg['content']}")


def test_load_history_file():
    # 演示加载已有会话
    print("=" * 20 + "加载已有会话" + "=" * 20)
    # 列出所有可用会话
    available_sessions = ChatSession.list_available_sessions()
    if available_sessions:
        print("可用会话列表:")
        for i, session in enumerate(available_sessions):
            print(f"{i + 1}. {session}")

        # 加载第一个会话文件（示例）
        if len(available_sessions) > 0:
            loaded_chat = ChatSession.load_session(available_sessions[0])

            # 继续对话
            thinking, reply = loaded_chat.send_message("继续我们的对话", show_process=True, stream=True)
    else:
        print("没有找到可用的会话文件")


def test_load_specify_history_file():
    loaded_chat = ChatSession.load_session("chat_2025_05_20__14_35_57.json")
    # 继续对话
    thinking, reply = loaded_chat.send_message("我喜欢科技", show_process=True, stream=True)