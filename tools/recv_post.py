# Recebe um POST (form) do navegador e grava o campo "d" no arquivo indicado por "f" (dentro de dl/).
import http.server, urllib.parse, os

class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n).decode("utf-8")
        q = urllib.parse.parse_qs(body, keep_blank_values=True)
        name = os.path.basename(q.get("f", ["dump.json"])[0])
        data = q.get("d", [""])[0]
        path = os.path.join(os.path.dirname(__file__), "dl", name)
        open(path, "w", encoding="utf-8").write(data)
        self.send_response(200); self.send_header("Content-Type", "text/plain; charset=utf-8"); self.end_headers()
        self.wfile.write(f"OK {name} {len(data)}".encode())
    def log_message(self, *a):
        pass

http.server.HTTPServer(("127.0.0.1", 8769), H).serve_forever()
