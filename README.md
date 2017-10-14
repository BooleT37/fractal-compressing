# Фрактальное сжатие изображений

### Для установки
1. Установите и запустите *virtualenv*:<br/>
    * Из *PyCharm*'а:<br/>
      File -> Settings -> Project Interpreter -> ⚙ -> Create VirtualEnv -> Имя: env, Interpreter: 3.6.3
    * Вручную:<br/>
        1. `pip install virtualenv` (если ещё не стоит; здесь важно его установить  помощью pip'а, идущего в комплекте с python'ом версии 3.6.3)
        1. `virtualenv env`
        1. `env/Scripts/activate`
1. `pip install -r requirements.txt`

### Для работы
* Запустить сервер: `python server/manage.py runserver [номер_порта]` (номер порта указывать не обязательно, по умолчанию 8000)