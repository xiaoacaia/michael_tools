from michael_tools.openapi_op.call_model import call_model


def get_prompt(example_ans):
    instruction = """
        你的任务是识别用户输入的的信息
        提取出对应的时间(time),地点(Locations)、人物(character)
    """

    output = """
        并以JSON格式输出
    """

    input_text = """今天晚上 我会和我的闺蜜小美一起去酒馆喝酒"""

    examples = f"""
        在本周末，我将和我的同事王五一起去海洋公园玩耍。:{example_ans}
        """

    prompt = f"""
        {instruction}
        
        {output}
        
        {examples}
        
        用户输入：
        {input_text}
        """
    return prompt


def test_chinese_ans():
    chinese_ans = """
        {"时间": "本周末","地点": "海洋公园","人物": ["我", "我的同事王五"]}
    """
    prompt = get_prompt(chinese_ans)
    print(prompt)
    call_model(prompt)
    # 输出：{"时间": "今天晚上", "地点": "酒馆", "人物": ["我", "我的闺蜜小美"]}


def test_english_ans():
    chinese_ans = """
        {"time": "本周末","Locations": "海洋公园","character": ["我", "我的同事王五"]}
    """
    prompt = get_prompt(chinese_ans)
    print(prompt)
    call_model(prompt)
    # 输出：{"time": "今天晚上", "Locations": "酒馆", "character": ["我", "我的闺蜜小美"]}
