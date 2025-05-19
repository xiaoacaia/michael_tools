from michael_tools.file_op.dir_op import get_upper_dir, path_join
from michael_tools.file_op.read_file import read_file
from openai import OpenAI
import time  # 导入time模块用于记录时间

# 全局变量存储API密钥
openapi_key = read_file("openapi_key")
if openapi_key is None:
    print("读取上一级目录 ......", end="")
    openapi_key = read_file(path_join(get_upper_dir(), "openapi_key"))
    if openapi_key is not None:
        print(" 'openapi_key' 已找到，读取成功。\n")
_global_api_key = openapi_key


def set_api_key(api_key):
    _global_api_key = api_key


def create_client():
    if not _global_api_key:
        raise ValueError("API 密钥未设置，请使用 set_api_key() 函数设置有效的 API 密钥")

    return OpenAI(
        api_key=_global_api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )


def prepare_request_params(prompt, model_name, stream=True):
    request_params = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    if stream:
        request_params["stream"] = True

        # 返回Token使用量
        # request_params["stream_options"] = {"include_usage": True}

    return request_params


def process_stream_response(completion, show_process=True):
    reasoning_content = ""  # 思考过程
    answer_content = ""  # 回答内容
    is_answering = False  # 是否开始回答

    if show_process:
        print("思考过程：", end='')

    for chunk in completion:
        # 处理usage信息
        if not chunk.choices:
            if show_process:
                print(f"\nUsage:{chunk.usage}")
            continue

        delta = chunk.choices[0].delta

        # 处理思考过程
        if hasattr(delta, 'reasoning_content') and delta.reasoning_content is not None:
            reasoning_content += delta.reasoning_content
            if show_process:
                print(delta.reasoning_content, end='', flush=True)
        # 处理回答内容
        else:
            # 首次进入回答阶段，显示标题
            if delta.content and not is_answering and show_process:
                print("\n完整回复：", end='')
                is_answering = True

            answer_content += delta.content or ""
            if show_process:
                print(delta.content or "", end='', flush=True)

    return reasoning_content, answer_content


def process_non_stream_response(completion, show_process=True):
    reasoning_content = completion.choices[0].message.reasoning_content
    answer_content = completion.choices[0].message.content

    if show_process:
        print(f"思考过程：{reasoning_content}\n")
        print(f"完整回复：{answer_content}\n\n")

    return reasoning_content, answer_content


# https://help.aliyun.com/zh/model-studio/deepseek-api
# - DeepSeek-V3：通用模型
# - DeepSeek-R1：推理模型
# - Qwen3-235B-A22B：通用模型
def call_model(prompt, model_name="deepseek-r1", show_process=False, stream=False, record_time=False):
    start_time = time.time()  # 记录开始时间
    
    client = create_client()

    # 准备请求参数
    request_params = prepare_request_params(prompt, model_name, stream)

    # 发送请求
    completion = client.chat.completions.create(**request_params)

    if stream:
        thinking_process, complete_reply = process_stream_response(completion, show_process)
    else:
        thinking_process, complete_reply = process_non_stream_response(completion, show_process)
    
    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算花费时间
    
    if record_time:
        if show_process:
            print(f"\n花费时间: {elapsed_time:.2f} 秒")
        return thinking_process, complete_reply, elapsed_time
    else:
        return thinking_process, complete_reply

def call_model_verbose(prompt):
    return call_model(prompt, show_process=True, stream=True, record_time=True)
