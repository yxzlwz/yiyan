import os
thisDir = os.path.dirname(os.path.abspath(__file__))


data_from = "local"  # 可选local, remote, 分别对应下面两行的设置

dir = f"{thisDir}/data/"  # 若使用本地文件，文件所在文件夹
url = "https://cdn.jsdelivr.net/gh/Danny-Yxzl/yiyan@master/data/"  # 若使用互联网文件，互联网文件根目录

# 暂时没有文件和数据的分类可以先删去
cate = "abcdefghijyz"  # 使用data文件夹
# cate = "abcdefghijy"  # 使用data_hitokoto文件夹
