from flask import Flask, render_template, request

app = Flask(__name__)

# Função que calcula a pegada de carbono baseada nos dados fornecidos pelo usuário
def calcular_carbono(consumo):
    # Fatores de emissão em kg CO2 por unidade de consumo
    fatores = {
        'gasolina': 2.31,  # Emissão por litro de gasolina
        'etanol': 1.51,    # Emissão por litro de etanol
        'diesel': 2.68,    # Emissão por litro de diesel
        'gnv': 2.75,       # Emissão por m³ de GNV
        'energia': 0.233,  # Emissão por kWh de eletricidade
        'gas': 2.10,       # Emissão por m³ de gás natural
        'carne_bovina': 27, # Emissão por kg de carne bovina
        'carne_suina': 6,   # Emissão por kg de carne suína
        'frango': 5,        # Emissão por kg de frango
        'leite': 1.32,      # Emissão por litro de leite
        'ovos': 0.15        # Emissão por unidade de ovo
    }

    # Cálculo das emissões por cada setor
    combustivel_emissao = (
        consumo['gasolina'] * fatores['gasolina'] +
        consumo['etanol'] * fatores['etanol'] +
        consumo['diesel'] * fatores['diesel'] +
        consumo['gnv'] * fatores['gnv']
    )
    
    energia_emissao = (
        consumo['energia'] * fatores['energia'] +
        consumo['gas'] * fatores['gas']
    )
    
    alimentos_emissao = (
        consumo['carne_bovina'] * fatores['carne_bovina'] +
        consumo['carne_suina'] * fatores['carne_suina'] +
        consumo['frango'] * fatores['frango'] +
        consumo['leite'] * fatores['leite'] +
        consumo['ovos'] * fatores['ovos']
    )

    # Soma total de emissões dividida por 1000 para converter em toneladas
    total_emissao = (combustivel_emissao + energia_emissao + alimentos_emissao) / 1000

    return total_emissao

# Rota principal que exibe o formulário
@app.route('/caminho do site')
def index():
    return render_template('calculadora.html')

# Rota para processar o formulário e calcular a pegada de carbono
@app.route('/calcular', methods=['POST'])
def calcular():
    # Coleta dos dados enviados pelo formulário
    consumo_usuario = {
        'gasolina': float(request.form['gasolina']),
        'etanol': float(request.form['etanol']),
        'diesel': float(request.form['diesel']),
        'gnv': float(request.form['gnv']),
        'energia': float(request.form['energia']),
        'gas': float(request.form['gas']),
        'carne_bovina': float(request.form['carne_bovina']),
        'carne_suina': float(request.form['carne_suina']),
        'frango': float(request.form['frango']),
        'leite': float(request.form['leite']),
        'ovos': float(request.form['ovos'])
    }

    # Cálculo da pegada de carbono com a função
    pegada_carbono = calcular_carbono(consumo_usuario)

    # Exibição do resultado em uma nova página
    return f"Sua pegada de carbono mensal é: {pegada_carbono:.2f} toneladas de CO2"

if __name__ == '__main__':
    app.run(debug=True)