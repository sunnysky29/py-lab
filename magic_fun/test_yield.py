"""
yield 学习
生成器

"""

import sys
sys.path.append('..')
from utils import cal_time

nums = 66666

@cal_time
def cal_f1():
    list1= [i for i in range(nums)]
    
@cal_time
def cal_f2():
    list2= (i for i in range(nums))
    print('list2： ', type(list2)) #  <class 'generator'>

cal_f1()
cal_f2()


def add():
    print(f'1111')
    yield
    print(f'2222')
    yield
    print(f'33333')
    yield
    
f= add()
print(type(f))
next(f)
next(f)
next(f)
# next(f)

print(f'-'*30)

def foo(num):
    for i in range(num):
        yield i*2
        
for i in foo(4):
    print(i)
