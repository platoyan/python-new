#生成器
#用来创建python序列的对象。生成器不需要创建和存储所有序列
#生成器函数
# 返回生成器
def my_range(first=0,last=0,step=1):
    number=first
    while number<last:
        yield number #使用yield返回，不使用return
        number+=step
for a in my_range(0,10):
    print(a)


#装饰器
#也是一个函数。
#不改变源代码的情况下修改已经存在的函数。
#他把一个函数作为输入并返回另一个函数
def document_it(func):
    def new_function(*args,**kwargs):
        print("running function:",func.__name__)
        print("Positional arguments:",args)
        print("keyword arguments:",kwargs)
        result=func(*args,**kwargs)
        print(result)
        return result
    return new_function

#可以直接在要装饰的函数前添加装饰器名字
#一个函数可以有多个装饰器
#靠近函数定义（ def 上面）的装饰器最先执行，然后依次执行上面的

#@square_it
@document_it
def add_ints(a, b):
    return a + b
