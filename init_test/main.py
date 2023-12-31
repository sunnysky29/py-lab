"""
参考：https://zhuanlan.zhihu.com/p/115350758

__init__.py  的使用
通过 init 简化 import 的导入
"""

# from my_package.test2.writer import write
# write()


from my_package import *

write()