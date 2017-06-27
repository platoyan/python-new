#列表(列表可变)
#1. 使用[]或list()创建列表
#2. 将其他类型数据转为列表 list()
# list(字符串) list(元组)
#3. [offset]获取元素
#4. 包含列表的列表
#5. 使用[offset]修改元素
#6. 指定范围并使用切片提取元素
#7. append()
#8. extend()或+=
#9. insert()
#10. del (不是方法)
#11. remove()
#12. pop() 可指定参数，也可以不指定
#13. index()
#14. in
#15. count()
#16. join()
#17. sort() sorted()
marxes=['Grou','Chico','Harpo']
sorted_marxes=sorted(marxes)  #产生排好序副本，原序列内容不变
marxes.sort() #原序列内容改变
marxes.sort(reverse=True) #降序排列
#18. len()
#19. 复制列表

#元组(不可变)
#1. 元组创建()
empty_tuple = ()
one_marx = 'Groucho',
#定义元组真正靠的是每个元素的后缀逗号,而不是括号
#2. 元组解包
marx_tuple=('ag','bc','yu')
a,b,c=marx_tuple
print(a,b,c)
#3. 利用tuple(),使其他类型数据创建元组
