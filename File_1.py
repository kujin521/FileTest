import os # 读取文件路径
import io # 输入输出
import time


root = 'D:\OneDrive\hexo\source\_posts\随心记'  # 你的文章地址
# root = '测试文件夹'  # 本地测试

# 读取文件内容并返回
def readFileContent(str):
    s=""
    for line in open(str,"r",encoding="utf-8", errors='ignore'):
        s+=line
    return s
str_modle=readFileContent('modle.md')

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
            sl=root.split("\\")
            file = os.path.join(root, filename) # 获取文件路径
            # 要动态修改模板内容
            content = str_modle.format(os.path.splitext(filename)[0], # 获取文件名替换标题
                                       time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(file))),
                                       time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getctime(file))),
              # str(list(sl)[6:]),   # 为文章添加多个分类，可以尝试以下 list 中的方法 下标 我这里是 6 开始截取
              sl[6],   # 为文章添加多个分类，可以尝试以下 list 中的方法 下标 我这里是 6 开始截取
              #os.path.splitext(filename)[0])+"\n"
              sl[6])+"\n"
            # 批量添加文件开头yaml
            batch_replace(filename, content)
            print("{} 替换完成".format(filename))