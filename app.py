from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Distribuidora Mari Água & Gás</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #007BFF, #00C6FF);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 90%;
                max-width: 400px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
            }
            h2 {
                color: #007BFF;
                margin-bottom: 20px;
            }
            input {
                width: 100%;
                padding: 12px;
                margin: 8px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 14px;
            }
            .total {
                margin-top: 10px;
                font-weight: bold;
                font-size: 18px;
                color: #007BFF;
            }
            button {
                width: 100%;
                padding: 14px;
                margin-top: 15px;
                border: none;
                border-radius: 8px;
                background-color: #25D366;
                color: white;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            }
            button:hover {
                background-color: #1ebe5d;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>💧 Peça sua Água Agora</h2>

            <input type="text" id="nome" placeholder="Seu Nome" required>
            <input type="number" id="quantidade" placeholder="Quantidade de Garrafões" required oninput="calcularTotal()">
            <input type="text" id="endereco" placeholder="Seu Endereço" required>
            <input type="text" id="validade" placeholder="Validade do Garrafão" required>

            <div class="total" id="total">Total: R$ 0,00</div>

            <button onclick="enviarWhatsApp()">Enviar Pedido no WhatsApp</button>
        </div>

        <script>
        function calcularTotal() {
            var quantidade = document.getElementById("quantidade").value;
            var preco = 7.00;
            var total = quantidade * preco;

            if (!quantidade || quantidade <= 0) {
                total = 0;
            }

            document.getElementById("total").innerHTML = 
                "Total: R$ " + total.toFixed(2).replace(".", ",");
        }

        function enviarWhatsApp() {
            var nome = document.getElementById("nome").value;
            var quantidade = document.getElementById("quantidade").value;
            var endereco = document.getElementById("endereco").value;
            var validade = document.getElementById("validade").value;
            var preco = 7.00;
            var total = quantidade * preco;

            if(nome === "" || quantidade === "" || endereco === ""){
                alert("Preencha os campos obrigatórios!");
                return;
            }

            var mensagem = "Olá segue abaixo o meu pedido! 💧%0A" +
                           "Nome: " + nome + "%0A" +
                           "Quantidade: " + quantidade + " garrafões%0A" +
                           "Total: R$ " + total.toFixed(2).replace(".", ",") + "%0A" +
                           "Endereço: " + endereco;

            if(validade !== ""){
                mensagem += "%0AValidade do Garrafão: " + validade;
            }

            var numero = "5581991488686";
            var url = "https://wa.me/" + numero + "?text=" + mensagem;

            window.open(url, "_blank");
        }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
