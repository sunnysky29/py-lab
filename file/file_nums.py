# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/12/13 15:12
Author : Dufy
File : file_nums.py

文件夹中文件数量统计
==============================================================================      
"""

def show_file_num(local_path):
    # local_path = r'data/imagenet'

    i= 0
    for name in os.listdir(local_path):
        dir = os.path.join(local_path, name)
        if os.path.isdir(dir):
            print(f'{name} 文件数量：{len(os.listdir(dir))}')
        else:
            i +=1
    print(f'{local_path} 文件数量：{i}')


import os, time
if __name__ == "__main__":
    pass
    path1= r'data/imagenet'
    path2= r'/data/bert/2048_shards_uncompressed'
    while 1:
        print(f'-'*20)
        time.sleep(5)
        show_file_num(path1)
        show_file_num(path2)

