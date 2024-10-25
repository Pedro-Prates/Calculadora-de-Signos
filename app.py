from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Dicionário com características e símbolos dos signos
signos_info = {
    "capricornio": {"descricao": "Você é, é isso, cheio de si e cheio de certeza, consegue o que quer e faz o que for necessário para isso.", "simbolo": "♑"},
    "aquario": {"descricao": "Frio e calculista, muito metódico.", "simbolo": "♒"},
    "peixes": {"descricao": "Sensível, trouxa, sonhador, esponja (absorve os sentimentos alheios).", "simbolo": "♓"},
    "aries": {"descricao": "Dono da razão, pragmático e racional.", "simbolo": "♈"},
    "touro": {"descricao": "Adora comida, sensível e tranquilo, a não ser que esteja com fome.", "simbolo": "♉"},
    "gemeos": {"descricao": "Duas caras, manipula as coisas e muito convencido de si.", "simbolo": "♊"},
    "cancer": {"descricao": "Esponja, sensível, chorão, não esconde as emoções e é manipulável.", "simbolo": "♋"},
    "leao": {"descricao": "Autosuficiente e adora ser elogiado, você se acha muito.", "simbolo": "♌"},
    "virgem": {"descricao": "Leal, busca pela perfeição, prático, mas se critica muito.", "simbolo": "♍"},
    "libra": {"descricao": "Confuso, precisa de tempo para decidir as coisas, mas é leal.", "simbolo": "♎"},
    "escorpiao": {"descricao": "Dominador, gosta de controlar as coisas e tem um apetite sexual alto.", "simbolo": "♏"},
    "sagitario": {"descricao": "Pior signo.", "simbolo": "♐"},
}

# Função para determinar o signo com base no dia e no mês
def calcular_signo(dia, mes):
    if (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "capricornio"
    elif (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        return "aquario"
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        return "peixes"
    elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "aries"
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "touro"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        return "gemeos"
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
        return "cancer"
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "leao"
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return "virgem"
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "libra"
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "escorpiao"
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "sagitario"
    else:
        return None

# Rota para processar o formulário
@app.route('/process', methods=['POST'])
def process():
    dia = int(request.form['dia'])
    mes = int(request.form['mes'])

    signo_key = calcular_signo(dia, mes)

    if signo_key:
        signo = signo_key.capitalize()
        caracteristica = signos_info[signo_key]["descricao"]
        simbolo = signos_info[signo_key]["simbolo"]
        return render_template('resultado.html', signo=signo, caracteristica=caracteristica, simbolo=simbolo, signo_key=signo_key)
    else:
        return "<h1>Erro!</h1><p>Data de nascimento inválida.</p>"

if __name__ == "__main__":
    app.run(debug=True)
