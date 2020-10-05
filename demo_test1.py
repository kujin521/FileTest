import os  # 读取文件路径
import io  # 输入输出
import time # 时间类

root = 'D:\OneDrive\hexo\source\_posts\随心记'  # 你的文章地址


# root = '测试文件夹'  # 本地测试


# 批量替换
def batch_replace(file, content):
    # 读取文件内容
    with io.open(os.path.join(root, file), "r", encoding="utf-8", errors='ignore') as f:
        for line in f:
            content += line
    # 写入内容
    with io.open(os.path.join(root, file), "w", encoding="utf-8", errors='ignore') as f:
        f.write(content)


# 遍历目录下文件
for root, subFolder, filenames in os.walk(root):
    # 遍历文件
    for filename in filenames:
        # 以 .md 结尾的文件
        if os.path.splitext(filename)[1] == '.md':
            file=os.path.join(root, filename)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(file))))

