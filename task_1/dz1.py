from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
'''
Веб-приложение, которое на любой GET запрос возвращает
текст “Hello, World wide web!”


На POST-запрос возвращает, а также печатает в консоль все
данные, которые были приняты от пользователя.
'''

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        header = self.headers.get("Content-Length")

        if header:
            c_len = int(header)
            text = self.rfile.read(c_len)
            print(text.decode())
        else:
            text = bytes("Ошибка получения данных", "utf-8")
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(text)

    def do_GET(self):
        text_answer = "Hello, World wide web!"
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(text_answer, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")