import os
import time
import code


def search_file(path):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if os.path.isdir(file_path):
            search_file(file_path)
        else:
            if key in f:
                print(file_path)


# 双击运行模式
key = input("请输入你要查找文件的文件名关键词：")
upath = input("请输入你要查找的目录:")

# 命令行执行模式
# key = sys.argv[1]
# upath = sys.argv[2]

if not os.path.exists(upath):
    print("目录输入有误，请关闭后重试。")
else:
    print("查找中请等待。。。。。")
    time.sleep(2)
    print("查找文件路径如下：".format(key))
    search_file(upath)

# # 交互模式
# code.interact(banner="", local=locals())
