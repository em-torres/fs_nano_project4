from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from constants import Paths
from helpers import read_file


class WebServerHandler(BaseHTTPRequestHandler):
    header = {
        'keyword': 'Content-type',
        'value': 'text/html'
    }

    def _send_response_and_header(self, response, header):
        """ Receive a response integer value and a header dictionary to set the response and headers of the service """
        self.send_response(response)
        self.send_header(header['keyword'], header['value'])
        self.end_headers()

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self._send_response_and_header(200, self.header)
                output = read_file(Paths.TEMPLATE_RESTAURANT) % "tesla"
                self.wfile.write(output)
                return

            if self.path.endswith("/hello"):
                self._send_response_and_header(200, self.header)

                output = "<html><body>Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>"
                output += "<h2>What would you like me to say?</h2>"
                output += "<input name='message' type='text'>"
                output += "<input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/hola"):
                self._send_response_and_header(200, self.header)

                output = "<html><body>&#161Hola! <a href='/hello'>Back to Hello</a>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>"
                output += "<h2>What would you like me to say?</h2>"
                output += "<input name='message' type='text'>"
                output += "<input type='submit' value='Submit'> </form>"
                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = "<html><body>"
            output += "<h3>Okay, how about this: </h3>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += "<form method='POST' enctype='multipart/form-data' action='/hello'>"
            output += "<h3>What would you like me to say?</h3>"
            output += "<input name='message' type='text'>"
            output += "<input type='submit' value='Submit'> </form>"
            self.wfile.write(output)
        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
