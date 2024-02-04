from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


def get_hora_e_data():
    agora = datetime.now()
    hora_atual = agora.strftime('%H:%M:%S')
    data_atual = agora.strftime('%d / %m / %Y')
    return hora_atual, data_atual


@app.route('/')
def index():
    hora_atual, data_atual = get_hora_e_data()
    return render_template(
        'index.html', hora_atual=hora_atual, data_atual=data_atual
    )


if __name__ == '__main__':
    app.run(debug=True)
