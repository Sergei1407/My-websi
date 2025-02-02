from flask import Flask, render_template, request
# Импортируем Flask для создания веб-приложения,
# render_template для работы с HTML-шаблонами
# и request для обработки данных, переданных через запросы.

from model import predict
# Импортируем функцию predict из файла model.py.
# Эта функция используется для обработки введенных пользователем данных.

app = Flask(__name__)
# Создаем объект Flask для запуска приложения.

@app.route('/')
def form():
    # Декоратор указывает, что эта функция отвечает за обработку запросов к корневому URL ('/').
    # Функция возвращает HTML-шаблон form.html.
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    # Декоратор связывает функцию с URL '/result' и разрешает только POST-запросы.
    # Эта функция обрабатывает данные, отправленные из формы.
    value1 = request.form.get('value1')
    value2 = request.form.get('value2')
    value3 = request.form.get('value3')
    value4 = request.form.get('value4')
    value5 = request.form.get('value5')
    # Получаем значения из формы. request.form.get() извлекает данные, отправленные пользователем.

    try:
        # Конвертируем значения в список чисел
        inputs = [float(value1), float(value2), float(value3), float(value4), float(value5)]
        # Преобразуем строки в числа (float). Если хотя бы одно значение нечисловое, произойдет ошибка.

        # Вызываем симуляцию предсказания
        prediction = predict(inputs)
        # Передаем список чисел в функцию predict для обработки.

        # Передаем результат в шаблон
        return render_template('result.html', prediction=prediction)
        # Рендерим шаблон result.html и передаем туда результат предсказания.

    except ValueError:
        # Если пользователь ввел нечисловые данные
        return "Ошибка: Убедитесь, что все введенные значения являются числами!"
        # Возвращаем сообщение об ошибке, если невозможно преобразовать данные в числа.

if __name__ == '__main__':
    # Запуск сервера Flask
    app.run(debug=True)
    # Указываем, что приложение запускается как основное.
    # Параметр debug=True позволяет автоматически перезагружать сервер при изменении кода.
