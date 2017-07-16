#1.解压序列赋值给多个变量
#现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
from collections import deque
def search(lines,pattern,history=5):
	previous_lines=deque(maxlen=history)
	for li in lines:
		if pattern in li:
			yield li,previous_lines
		previous_lines.append(li)

if __name__=='__main__':
	with open(r'some.txt') as f:
		for line,previous_lines in search(f,'python',5):
			for pline in previous_lines:
				print(pline,end=' ')
			print(line,end=' ')
			print('-'*20)
			print(previous_lines)
