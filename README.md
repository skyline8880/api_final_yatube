# API для социальной сети Yatube
финальная версия

### Как запустить проект:

Клонировать репозиторий на компьютер:
(для Windows используйте GitBash)

```
git clone https://github.com/skyline8880/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

IOS:
```
python3 -m venv env
```
```
source env/bin/activate
```

Windows:
```
python -m venv env
```
```
venv\Scripts\activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

IOS:
```
python3 manage.py migrate
```
Windows:
```
python manage.py migrate
```

Запустить проект:

IOS:
```
python3 manage.py runserver
```
Windows:
```
python manage.py runserver
```