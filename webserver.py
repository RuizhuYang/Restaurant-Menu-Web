from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from database_setup import Restaurant, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#connect to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

###handler:indicate what code to execute based on the request sent to the server
#BaseHTTPRequestHandler must be subclassed to handle each request method (e.g. GET or POST)
class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                #Writes a specific HTTP header to the output stream
                #to show send back html to the client
                self.send_header('Content-type', 'text/html')
                #Sends a blank line, indicating the end of the HTTP headers in the response.
                self.end_headers()

                output = ""
                output += "<html><body><h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>
                          What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            
            if self.path.endswith("/hola"):
                self.send_response(200)
                #Writes a specific HTTP header to the output stream
                #to show send back html to the client
                self.send_header('Content-type', 'text/html')
                #Sends a blank line, indicating the end of the HTTP headers in the response.
                self.end_headers()

                output = ""
                output += "<html><body><h1>&#161Hola!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data'
                             action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" >
                             <input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/restaurant"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body><h1>Restaurants</h1><h2>"
                res = session.query(Restaurant).all()
                for each in res:
                    output += each.name
                    output += "<br/>"
                output += "</h2></body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)
    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

                output = ""
                output += "<html><body>"
                output += "<h2> OK, how about this: </h2>"
                output += "<h1> %s </h1>" % messagecontent[0]

                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'>
                          <h2>What would you like me to say?</h2><input name="message" type="text" >
                          <input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except:
            pass
    
###main:word port to listen on
def main():
    try:
        port = 8080
        ##create a HTTP server
        server = HTTPServer(('', port), webServerHandler)
        print "Web server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        ##shut down the server
        server.socket.close()     

if __name__ == '__main__':
    main()
