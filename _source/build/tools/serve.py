"""Local preview server: serves public/ with Vercel-style clean URLs (/page -> page.html, /staff -> staff/index.html).
Usage: python3 -I _source/build/tools/serve.py [port]"""
import http.server, os, sys, functools
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "public"))
class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = super().translate_path(path)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "index.html")):
            return os.path.join(p, "index.html")
        if not os.path.exists(p) and os.path.exists(p + ".html"):
            return p + ".html"
        return p
    def log_message(self, *a): pass
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(H, directory=ROOT)).serve_forever()
