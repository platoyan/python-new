#requests
#requests库提供7个常用方法，request最基本方法，其余6个方法都是调用request方法实现的
#1.requests.get(url)构建一个向服务器请求资源的Request对象，返回的内容Response对象
#requests.get(url,params=None,**kwagrs)
#params: url中额外参数，字典或者字节流格式
#**kwargs: 12个控制访问的参数

#requests库的两个重要对象Request和Response

#Response常用的5个属性：
#	r.status_code	Http请求的返回状态，200表示连接成功，404表示失败
#	r.text			Http响应内容的字符串形式
#   r.encoding		从HTTP HEADER中猜测的响应内容编码方式
#   r.apparent_encoding	从内容分析出的响应内容编码方式(备选编码方式)
#	r.content		Http响应内容的二进制形式
#首先要判断状态码
#r.encoding 如果header中不存在charset, 则认为编码为ISO-8859-1
#r.apparent_encoding 根据网页内容，解析可能的编码

#Requests库的异常
#	requests.ConnectionError	网络连接异常，如DNS查询异常、拒绝连接
#	requests.HTTPError 			Http错误异常
#	requests.URLRequired		URL缺失异常
#	requests.TooManyRedirects	超过最大重定向次数
#	requests.ConnectTimeout		连接远程服务器超时异常
#	requests.Timeout 			从发出url请求到返回内容整个过程的超时异常

#通用代码框架
import requests
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()#如果状态不是200，引发HTTPError异常
		r.encoding=r.apparent_encoding
		return r.text
	except :
		return "产生异常"

if __name__=="__main__":
	url="http://www.baidu.com"
	print(getHTMLText(url))