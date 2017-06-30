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
