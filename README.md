# py-lab

关于 python 的学习记录




## help() ;python 查看内置函数
	$ python3
	Python 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> help(getattr)

## *args and **kwargs
当函数的参数不确定时使用。其中， args 传列表，kwargs传字典
~~~
	def myFun(*args, **kwargs):
		print("args: ", args)  # args: ('geeks', 'for', 'geeks')
		print("kwargs: ", kwargs)  # kwargs: {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
	myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
~~~

## 打印代码位置， 文件名+ 代码行号 + def()
	import sys
	print(f'{__file__} , line {sys._getframe().f_lineno} --> {sys._getframe().f_code.co_name}()')
	print(f'??**')
