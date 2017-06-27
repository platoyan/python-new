#1. 对应假值(False)：
# None  0   0.0   ''  ()   []   {}   set()
#2. while循环外使用else
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
        if number % 2 == 0:
            print('Found even number', number)
            break
            position += 1
else: #没有执行break
    print('No even number found')

#3. for循环外使用else
#4. zip()返回一个可迭代变量
#5. range()
#6. 列表推导[ expression for item in iterable ]
#   列表推导[expression for item in iterable if condition]
#7. 字典推导式{ key_expression : value_expression for expression in iterable }
#8. 集合推导式
#9. 生成器推导式
