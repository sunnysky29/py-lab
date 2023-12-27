#-*- coding:utf-8 -*-
"""
==============================================================================
Time : 2022/10/8
Author : Dufy

文件拷贝
==============================================================================
"""
import random
import os
import shutil
from tqdm import tqdm


old_path = r'D:\datas\corpus\mini-imagenet\images'
new_path = r'D:\datas\corpus\mini-imagenet\images1'
numbers = 3000

random.seed(12345)
print(f'原始文件夹有文件数：{len(os.listdir(old_path))}')
select_files = random.sample(os.listdir(old_path), numbers)
print(f'选择的文件：{select_files}')

for i in tqdm(select_files):
    old_file_path = os.path.join(old_path, i)
    new_file_path = os.path.join(new_path, i)
    shutil.copy(old_file_path, new_file_path)


