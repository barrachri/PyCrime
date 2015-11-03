import tornado.ioloop
import tornado.web
from tornado.escape import json_encode
import json

with open("coord.json") as json_file:
    json_data = json.load(json_file)
    
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'application/javascript')
        self.write("eqfeed_callback(")
        self.write(json_encode(json_data))
        self.write(")")
        

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/data", JsonHandler)
])

if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.current().start()