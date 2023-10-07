# Инструкция
>Для локального тестирования необходимо создать виртуальное окружение командой python -m venv venv и активировать его. Команда venv\Scripts\activate.bat - для Windows; source venv/bin/activate - для Linux и MacOS.
- **Необходимо установить зависимости командой pip install -r requirements.txt.**
* **Для того чтобы запустить сервер uvicorn main:app --reload**
+ **После этого можно зайти в браузере по адресу http://localhost:8000/docs для просмотра доступных эндпоинтов.**