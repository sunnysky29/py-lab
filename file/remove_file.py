# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/10/13 17:25
Author : Dufy
File : remove_file.py
删除文件
==============================================================================      
"""
import os

if __name__ == "__main__":
    pass
    path = r'Downloads\test'
    remove_list = []
    for file in os.listdir(path):
        if file.startswith('ad_'):
            print(file)
            remove_list.append(os.path.join(path, file))
    for i in remove_list:
        os.remove(i)
