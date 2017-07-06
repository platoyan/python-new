import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hj")
def make_up():
	return tornado.web.Application([
		(r"/",MainHandler),
	])
if __name__=="__main__":
	app=make_up()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()