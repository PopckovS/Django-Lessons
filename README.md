## Django-Lessons
На протяжении последнего года я изучал и 
документировал уроки, лекции, статьи по 
Python. Этот проект на Django сделан чтобы 
собрать все уроки в одном месте, и удобно
их все оформить.

**Почему Django ?** потому что в отличии от Flask, тут есть 
админка с CRUD операциями для подключеных моделей, и тут 
есть модуль для быстрого добавления HTML редактора 
чтобы редактировать статьи.

Html+CSS были взяты с разных бесплатных 
шаблонов.

Разделы сайта:
1) Python основы.
2) Python классы.
3) SQL.
4) Алгоритмы.
5) Сылки на видео, уроки, статьи, интересные ресурсы.

Для работы применить миграции:

    python3 manage.py makemigrations
    python3 manage.py migrate

Запуск сервера:

     python3 manage.py runserver

Установка ckeditor в Django:

    http://djangonauts.ru/content/ustanovka-vizualnogo-redaktora-ckeditor-v-django/


