from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ARQUIVO = "pedidos.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Distribuidora Água</title>
<style>
body {
    font-family: Arial;
    background: #0d6efd;
    margin: 0;
    padding: 20px;
    color: white;
    text-align: center;
}
.container {
    background: white;
    color: black;
    padding: 20px;
    border-radius: 12px;
    max-width: 400px;
    margin: auto;
}
input, textarea {
    width: 100%;
    padding: 10px;
    margin: 8px 0;
    border-radius: 8px;
    border: 1px solid #ccc;
}
button {
    width: 100%;
    padding: 12px;
    background: #0d6efd;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
}
</style>
</head>
<body>
<h2>💧 Peça sua Água</h2>
<div class="container">
<input id="cliente" placeholder="Seu nome">
<input id="telefone" placeholder="Telefone">
<input id="endereco" placeholder="Endereço">
<input id="quantidade" type="number" placeholder="Quantidade">
<textarea id="obs" placeholder="Observação"></textarea>
<button onclick="enviar()">PEDIR AGORA</button>
<p id="msg"></p>
</div>

<script>
function enviar() {
    fetch('/pedido', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            cliente: document.getElementById('cliente').value,
            telefone: document.getElementById('telefone').value,
            endereco: document.getElementById('endereco').value,
            quantidade: document.getElementById('quantidade').value,
            obs: document.getElementById('obs').value,
            entregue: false
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('msg').innerHTML = "✅ Pedido enviado com sucesso!";
    });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/pedido", methods=["POST"])
def novo_pedido():
    dados = request.json
    pedidos = carregar()
    pedidos.append(dados)
    salvar(pedidos)
    return jsonify({"status": "Pedido recebido com sucesso!"})

@app.route("/pedidos", methods=["GET"])
def listar():
    return jsonify(carregar())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)