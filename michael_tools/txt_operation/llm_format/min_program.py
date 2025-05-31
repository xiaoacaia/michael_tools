import tkinter as tk
from tkinter import messagebox
import re
import pyperclip  # 需要安装：pip install pyperclip

class LatexConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("LaTeX 格式转换器")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f0f0')

        self.setup_ui()

    def setup_ui(self):
        # 主容器 - 使用pack布局
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 标题
        title_label = tk.Label(main_frame,
                               text="LaTeX 格式转换器",
                               font=('Microsoft YaHei', 18, 'bold'),
                               fg='#333333',
                               bg='#f0f0f0')
        title_label.pack(pady=(0, 10))

        # 副标题
        subtitle_label = tk.Label(main_frame,
                                  text="将 LaTeX 公式标记转换为标准格式",
                                  font=('Microsoft YaHei', 10),
                                  fg='#666666',
                                  bg='#f0f0f0')
        subtitle_label.pack(pady=(0, 20))

        # 输入区域
        input_label = tk.Label(main_frame,
                               text="输入内容",
                               font=('Microsoft YaHei', 12, 'bold'),
                               fg='#333333',
                               bg='#f0f0f0')
        input_label.pack(anchor='w', pady=(0, 5))

        # 输入文本框
        self.input_text = tk.Text(main_frame,
                                  height=8,
                                  font=('Consolas', 11),
                                  wrap=tk.WORD,
                                  relief='solid',
                                  bd=1,
                                  padx=10,
                                  pady=10,
                                  bg='white',
                                  fg='#333333')
        self.input_text.pack(fill=tk.X, pady=(0, 15))

        # 按钮区域 - 这里是关键！
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=(0, 15))

        # 转换按钮
        convert_btn = tk.Button(button_frame,
                                text="转换",
                                font=('Microsoft YaHei', 11, 'bold'),
                                bg='#007acc',
                                fg='white',
                                relief='flat',
                                bd=0,
                                padx=20,
                                pady=10,
                                cursor='hand2',
                                command=self.convert_text,
                                width=8)
        convert_btn.pack(side=tk.LEFT, padx=(0, 10))

        # 清空按钮
        clear_btn = tk.Button(button_frame,
                              text="清空",
                              font=('Microsoft YaHei', 11),
                              bg='#cccccc',
                              fg='#333333',
                              relief='flat',
                              bd=0,
                              padx=20,
                              pady=10,
                              cursor='hand2',
                              command=self.clear_all,
                              width=8)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))

        # 复制结果按钮
        copy_btn = tk.Button(button_frame,
                             text="复制结果",
                             font=('Microsoft YaHei', 11, 'bold'),
                             bg='#28a745',
                             fg='white',
                             relief='flat',
                             bd=0,
                             padx=20,
                             pady=10,
                             cursor='hand2',
                             command=self.copy_result,
                             width=10)
        copy_btn.pack(side=tk.LEFT)

        # 输出区域
        output_label = tk.Label(main_frame,
                                text="转换结果",
                                font=('Microsoft YaHei', 12, 'bold'),
                                fg='#333333',
                                bg='#f0f0f0')
        output_label.pack(anchor='w', pady=(0, 5))

        # 输出文本框
        self.output_text = tk.Text(main_frame,
                                   height=8,
                                   font=('Consolas', 11),
                                   wrap=tk.WORD,
                                   relief='solid',
                                   bd=1,
                                   padx=10,
                                   pady=10,
                                   bg='#f8f9fa',
                                   fg='#333333',
                                   state=tk.DISABLED)
        self.output_text.pack(fill=tk.X, pady=(0, 10))

        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("准备就绪")
        status_label = tk.Label(main_frame,
                                textvariable=self.status_var,
                                font=('Microsoft YaHei', 9),
                                fg='#888888',
                                bg='#f0f0f0')
        status_label.pack(anchor='w')

        # 绑定快捷键
        self.root.bind('<Control-Return>', lambda e: self.convert_text())
        self.root.bind('<F5>', lambda e: self.convert_text())

    def convert_latex_format(self, text):
        """原始的转换函数"""
        second_translation_marker = "### 第二次翻译（意译）："
        if second_translation_marker in text:
            start_pos = text.find(second_translation_marker)
            content_after_marker = text[start_pos + len(second_translation_marker):].strip()
            converted_text = re.sub(r'\\?\\\(\s*(.*?)\s*\\?\\\)', r'$$\1$$', content_after_marker)
            return converted_text
        else:
            return ""

    def convert_text(self):
        """转换按钮的回调函数"""
        try:
            input_content = self.input_text.get("1.0", tk.END).strip()

            if not input_content:
                messagebox.showwarning("提示", "请输入要转换的内容！")
                return

            # 执行转换
            result = self.convert_latex_format(input_content)

            # 显示结果
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)

            if result:
                self.output_text.insert("1.0", result)
                self.status_var.set("✓ 转换完成")
            else:
                self.output_text.insert("1.0", "未找到标记 '### 第二次翻译（意译）：'")
                self.status_var.set("⚠ 未找到指定标记")

            self.output_text.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("错误", f"转换失败：{str(e)}")
            self.status_var.set("✗ 转换失败")

    def clear_all(self):
        """清空所有内容"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set("已清空所有内容")

    def copy_result(self):
        try:
            result = self.output_text.get("1.0", tk.END).strip()
            if result:
                pyperclip.copy(result)
                self.status_var.set("✓ 已复制到剪贴板")
                # messagebox.showinfo("成功", "结果已复制到剪贴板！")
            else:
                messagebox.showwarning("提示", "没有可复制的内容！")
        except Exception as e:
            messagebox.showerror("错误", f"复制失败：{str(e)}")

def main():
    root = tk.Tk()
    app = LatexConverter(root)

    # 设置窗口居中
    root.update_idletasks()
    width = 800
    height = 600
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    root.mainloop()


# 打包
# pip install pyinstaller
# pyinstaller --noconfirm --nowindowed --onefile min_program.py
if __name__ == "__main__":
    main()