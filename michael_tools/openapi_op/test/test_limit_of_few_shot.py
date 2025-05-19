from michael_tools.openapi_op.call_model import call_model


def get_prompt():
    prompt = """
这组数字中的奇数加起来是一个偶数：4、8、9、15、12、2、1。
A：答案是False。
这组数字中的奇数加起来是一个偶数：17、10、19、4、8、12、24。
A：答案是True。
这组数字中的奇数加起来是一个偶数：16、11、14、4、8、13、24。
A：答案是True。
这组数字中的奇数加起来是一个偶数：17、9、10、12、13、4、2。
A：答案是False。
这组数字中的奇数加起来是一个偶数：15、32、5、13、82、7、1。
A：
"""
    return prompt


def test_limit_of_few_shot_r1():
    prompt = get_prompt()
    print(prompt)
    call_model(prompt)
    # True ans：A：答案是False
    # deepseek-r1：A：答案是False


def test_limit_of_few_shot_v3():
    prompt = get_prompt()
    print(prompt)
    call_model(prompt, model_name="deepseek-v3")
    # deepseek-v3：根据上述分析，第五组数字中奇数相加的和为41，是奇数，因此答案为**False**。
    # deepseek-v3：这组数字中的奇数加起来不是一个偶数。**答案：** False。
