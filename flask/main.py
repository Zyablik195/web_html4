from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"

@app.route('/promotion_image')
def index():
    items = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнём с марса!',
    'Присоединяйся!']
    return render_template('base.html', items=items)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')