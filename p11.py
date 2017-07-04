#文件处理
#file=open(<name>,<mode>)
#mode: r, w, a, rb, wb, ab, r+
#读取
#file.read() 返回包含整个文件内容的一个字符串
#file.readline() 返回文件下一行内容的字符串
#file.readlines() 返回整个文件内容的列表，每项都是以换行符为结尾的一行字符串
#写入
#write() 把含有文本数据或二进制数据块的字符串写入文件中
#writelines() 针对列表操作，接受一个字符串列表作为参数，将他们写入文件，并且行结束符不会自动加入
#outfile=open("outfile.txt","w")
#outfile.writelines(["hello"," ","world"])
#outfile.close()

#文件遍历
#通用代码框架:
#file=open(someFile,"r")
#for line in file.readlines():
#	#处理一行内容
#file.close()
#简化通用代码框架:
#file=open(someFile,"r")
#for line in file:
#	#处理一行内容
#file.close()

#文件拷贝
def main():
	f1 = input("Enter a source file:").strip()
	f2 = input("Enter anthor source file:").strip()

	infile = open(f1,"r")
	outfile = open(f2,"w")

	countLines = countChars = 0

	for line in infile:
		countLines+=1
		countChars+=len(line)
		outfile.write(line)
	print(countLines,"lines and",countChars,"chars copied")
	infile.close()
	outfile.close()


main()
