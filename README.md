# tgWebServer
Web server for tg
Инструкция по запуску веб-сервера на localhost
Клонируем проект:
> git clone https://github.com/SlafePower/tgWebServer.git
Создаем виртуальное окружение(ve, virtual environment) в папке проекта:
> python -m venv ve
Активируем ve: 
> . ve/bin/activate
или
> .ve/Scripts/Activate
Устанавливаем зависимости в ve:
> pip install -r requirements.txt
Экспортируем переменные среды
> cd app/
../app/> export FLASK_APP=app.py
../app/> export FLASK_ENV=development
Запускаем веб-сервер:
../app/> flask run
Сервер разворачивается на http://localhost:5000. Порт и адрес можно задать другими 
