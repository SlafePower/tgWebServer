# Web server for tg
Инструкция по запуску веб-сервера на localhost
1. Клонируем проект:
  `git clone https://github.com/SlafePower/tgWebServer.git`  
2. Создаем виртуальное окружение(ve, virtual environment) в папке проекта:
  `python -m venv ve`
3. Активируем ve: 
  `. ve/bin/activate`
  или
  `. ve/Scripts/Activate`  
4. Устанавливаем зависимости в ve:
  `pip install -r requirements.txt`  
5. Экспортируем переменные среды  
  `cd app/`  
  `export FLASK_APP=app.py`  
  `export FLASK_ENV=development`  
6. Запускаем веб-сервер:
  ../app/> flask run
  Сервер разворачивается на http://localhost:5000. Порт и адрес можно задать другими 
