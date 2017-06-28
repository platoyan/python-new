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

#6. 使用**收集关键字参数
# 收集到一个字典当中
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(wine="merlot",entree="mutton")

#7. 文档字符串
# 建议在函数体开始的部分附上
def print_if_true(thing,check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check the *second* argument is true
        2. If it is,print the first
    '''
    if check:
        print(thing)

help(print_if_true)
print(print_if_true.__doc__) #打印说明文档

#8. 函数作为参数
def answer():
    print(42)
def run_something(func):
    func()
run_something(answer)

#9. 内部函数
# 在函数内定义另一个函数  在一个函数执行一复杂的任务时，可以定义内部函数
def knight(saying):
    def inner(quote):
        return "we are knight who say: '%s'" % quote
    return inner(saying)
print(knight('Ni!'))
#10. 闭包（函数）
# 由其他函数动态创建，可以记录函数外的变量值
def knight2(saying):
    def inner2():
        return "we are knight who say: '%s'" % saying
    return inner2

a=knight2("abc")
print(a())

#11. 匿名函数 lambda()函数
def edit_story(words,func):
    for word in words:
        print(func(word))
words=['thud','meow','thud','hiss']
edit_story(words,lambda word: word.capitalize()+"!")
