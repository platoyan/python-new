#函数
#1. 定义函数的规范：def 函数名():
#最简单的函数
def do_nothing():
    pass  #pass表示函数没做任何事情
#函数不显式调用return , 默认返回None(None 在python是特殊的值，不表示任何数据)
print(do_nothing()) #打印None

#2. 位置参数
#传入的参数值是按照顺序复制过去
def menu(wine,entree,dessert):
    return {'wine':wine,'entree':entree,'dessert':dessert}

print(menu('wine','entree','dessert'))

#3. 关键字参数
#可以不顾及参数的顺序
print(menu(entree='entree',wine='wine',dessert='dessert'))

#4. 指定默认参数值
def menu1(wine,entree,dessert='dessert'):
    return {'wine':wine,'entree':entree,'dessert':dessert}
print(menu1('wine','entree'))
#默认参数值在函数被定义时已经算出来了，而不是在程序运行时
#注意不要把可变数据类型当作默认值
def buggy(arg,result=[]):
    result.append(arg)
    print(result)

buggy('a') #打印['a']
buggy('a') #打印['a','a']

#5. 使用*收集位置参数
# *将一组可变数量的位置参数集合成参数值的元组
def print_args(*args):
    print('Positional argument tuple:',args)

print_args('a','b',1) #Positional argument tuple: ('a','b',1)
