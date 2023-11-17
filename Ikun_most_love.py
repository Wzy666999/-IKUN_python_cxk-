import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt

length = 532
width = 349

# 定义字符集，根据需要自定义
char_set = "❶❺❽❺"
# 加载 GIF 文件
gif_path = "D:/Ikun/ikun.gif"#注意放对位置，或者你直接改地址
gif = Image.open(gif_path)
# 遍历每一帧
frames = []
for frame_index in range(64):
    # 选择当前帧
    gif.seek(frame_index)
    
    # 将图像转换为灰度
    gray_frame = gif.convert("L")
    
    # 将灰度图像转换为灰度矩阵
    gray_matrix = np.array(gray_frame)
    
    # 处理当前帧的灰度矩阵，例如进行字符图形转换
    # 定义一个空字符串变量来存储字符图形
    char_image = ""
    
    # 遍历灰度矩阵的每个像素
    for row in gray_matrix:
        for pixel in row:
            # 根据灰度值选择对应的字符
            # 计算灰度值在字符集中的索引，将灰度值映射到字符集的范围内
            index = int(pixel // (255 // len(char_set)))
            
            # 将对应的字符添加到字符图形中
            char_image += char_set[index]
        
        char_image += "\n"  # 在行末添加换行符
    
    # 将当前字符图形添加到帧列表中
    frames.append(char_image)
print('图像已分解完毕！')


# 打印第一帧的字符图形
#print(frames[0])

# 定义要保存的文件路径
output_file =  "D:/Ikun/char_image.txt"

# 将字符图形写入到文件中
for i in frames:
    with open(output_file, "a+",encoding="utf-8") as file:
        file.write(i)
print("字符图形已保存到文件：", output_file)


import tkinter as tk

def show_file_content():
    # 定义每批次输出的行数
    batch_size = 349#行像素

    # 定义文件路径
    file_path = "D:/Ikun/char_image.txt"

    # 创建新的窗口
    window = tk.Tk()

    # 设置窗口全屏显示
    window.attributes('-fullscreen', True)

    # 创建文本框
    text_box = tk.Text(window, font=("Arial", 1))
    text_box.pack(fill=tk.BOTH, expand=True)

    # 读取文件内容
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()
    cnt = 0
    while 1:
        cnt+=1
        if cnt>=2:
            break
        # 循环输出每批次的行数
        for i in range(0, len(content), batch_size):
            # 获取当前批次的行数内容
            batch = content[i:i+batch_size]

            # 将当前批次的内容添加到文本框中
            text_box.insert(tk.END, "".join(batch))
            text_box.see(tk.END)  # 滚动到文本框的末尾
            text_box.update()  # 更新文本框的显示

            # 删除已经显示的内容
            text_box.delete("1.0", tk.END)

            # 等待一段时间再继续显示下一个批次的内容
            window.after(24)  # 暂停1秒
    window.after(500, window.destroy)
    # 进入窗口的主循环
    window.mainloop()

# 调用函数显示文件内容
show_file_content()
