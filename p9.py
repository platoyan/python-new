#命令行参数
import sys
print('Program arguments:',sys.argv) #python p9.py la 结果: Program arguments:['sys.argv','la']

#模块
#就是一个python文件
#导入模块,使用import
#使用别名导入模块 import report as wr

#导入模块的一部分 from report import get_des
#取别名 from report import get_des as do_it

#模块的搜索路径

#类
class Person():
    # __init__()初始化方法，第一个参数必须是self
    # 类可以不必定义__init__
    def __init__(self):
        pass

#1. 继承：
class Car():
    pass
# Car 父类
class Yugo(Car):
    pass
#在子类中，可以覆盖任何父类的方法，包括 __init__()。

