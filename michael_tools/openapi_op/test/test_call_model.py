from michael_tools.openapi_op.call_model import call_model, set_api_key


def test_call_model():
    user_prompt = "你是谁"

    # 流式输出示例
    print("=== 流式输出示例 ===")
    reasoning1, answer1 = call_model(user_prompt, stream=True)

    # 非流式输出示例
    print("\n=== 非流式输出示例 ===")
    reasoning2, answer2 = call_model(user_prompt, stream=False)
