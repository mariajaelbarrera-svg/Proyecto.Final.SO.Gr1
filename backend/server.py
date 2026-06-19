from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            body = {
                "mensaje": "🚀 Backend Python activo - Grupo 1",
                "status": "ok",
                "infraestructura": {
                    "grupo": "1",
                    "distribuciones": "Ubuntu 24.04 / Debian 13.5",
                    "imagen_base": "ubuntu:24.04"
                },
                "equipo": [
                    "Duber Alvarez Ruiz (2260403)",
                    "Maria Jael Barrera Gómez (2369181)",
                    "Gustavo Adolfo Chilito (20XXXXXX)",
                    "Bradley Suescun Ramírez (2478054)"
                ]
            }
        elif self.path == '/salud':
            body = {"status": "ok", "servicio": "backend-python"}
        else:
            self.send_response(404)
            body = {"error": "ruta no encontrada", "ruta": self.path}
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(body).encode())
            return

        data = json.dumps(body).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(data)))
        # Crítico: Permite que el Frontend (puerto 80) se comunique con el Backend (puerto 5000)
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        # Muestra los logs en la consola del contenedor
        print(f"[{self.address_string()}] {fmt % args}")

if __name__ == '__main__':
    # El puerto 5000 es obligatorio para el Componente 2
    server = HTTPServer(('0.0.0.0', 5000), Handler)
    print("Backend Grupo 1 corriendo en http://0.0.0.0:5000")
    server.serve_forever()
