from flask import Flask, request, jsonify
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

@app.route("/")
def home():
    return "Servidor da Distribuidora Online 🚀"

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