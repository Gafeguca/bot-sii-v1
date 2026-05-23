from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    rut = data.get('rut')
    password = data.get('password')
    
    if not rut or not password:
        return jsonify({"error": "RUT y contraseña son obligatorios"}), 400
        
    # Aquí es donde el panel valida las credenciales y las deja listas
    return jsonify({"message": "Autenticación exitosa en el panel", "rut": rut})

@app.route('/api/run-bot', methods=['POST'])
def run_bot():
    # AQUÍ PROGRAMAREMOS EL PASO 2: EL MOTOR DEL SCRAPER
    try:
        # Aquí irá la lógica de Selenium/Playwright
        return jsonify({"message": "El bot terminó la simulación con éxito y leyó el SII."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
