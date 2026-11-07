"""Тестовий сервер: на GET / повертає JSON з кодом 200."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "ok", "message": "hello from test server"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # не засмічуємо термінал
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
