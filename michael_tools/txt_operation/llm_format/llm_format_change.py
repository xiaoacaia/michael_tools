import re

def convert_latex_format(text):
    second_translation_marker = "### 第二次翻译（意译）："
    if second_translation_marker in text:
        start_pos = text.find(second_translation_marker)
        content_after_marker = text[start_pos + len(second_translation_marker):].strip()
        converted_text = re.sub(r'\\?\\\(\s*(.*?)\s*\\?\\\)', r'$\1$', content_after_marker)
        return converted_text
    else:
        return ""
