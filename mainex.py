from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 31},
    {"nome": "Pedro", "idade": 28},
    {"nome": "Ana", "idade": 22},
    {"nome": "Luiz", "idade": 35},
    {"nome": "Julia", "idade": 29},
    {"nome": "Carlos", "idade": 40},
    {"nome": "Beatriz", "idade": 26},
    {"nome": "Rafael", "idade": 33},
    {"nome": "Gabriela", "idade": 24},
    {"nome": "Fernando", "idade": 38},
    {"nome": "Leticia", "idade": 27},
    {"nome": "Matheus", "idade": 30},
    {"nome": "Aline", "idade": 23},
    {"nome": "Thiago", "idade": 36},
    {"nome": "Camila", "idade": 25},
    {"nome": "Vinicius", "idade": 32},
    {"nome": "Isabella", "idade": 21},
    {"nome": "Leonardo", "idade": 39},
    {"nome": "Sofia", "idade": 26}
]



@app.route('/')
def index():
    return render_template(
        'exindex.html',
        nome = 'Gabriel',
        usuarios = usuarios
    )


if __name__ == '__main__':
    app.run(debug=True)