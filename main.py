from flask import Flask, render_template

app = Flask(__name__)


links = [
    {'nome': 'Juvenaldo', 'url':'https://www.youtube.com/watch?v=dZvvKwfYnFo'
    },
    {'nome': 'ThingSpeak', 'url':'https://thingspeak.com/'}

]


@app.route('/')

def index():
    return render_template (
        'index.html',
        nome = 'Juvenaldo',
        titulo = 'Minha primeira página',
        teste = False,
        links = links
    
    )


if __name__ == '__main__':
    app.run(debug=True)