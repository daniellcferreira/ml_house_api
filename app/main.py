from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import pickle
import os
import pandas as pd

# Carrega o modelo treinado
colunas = ['tamanho', 'ano', 'garagem']
modelo_path = os.path.join(os.path.dirname(__file__), 'modelo.pkl')
modelo = pickle.load(open(modelo_path, 'rb'))

# Configurações do Flask
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'teste'
basic_auth = BasicAuth(app)

# Rota principal
@app.route('/')
def home():
    return "API de Previsão de Preços de Imóveis"

# Rota para previsão de preços
@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    try:
        entrada_df = pd.DataFrame([dados], columns=colunas)  # Cria DataFrame com colunas esperadas
        preco = modelo.predict(entrada_df)
        return jsonify(preco=round(preco[0], 2))
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
