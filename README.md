# TravelTime

<center><img src="https://github.com/AShedko/TravelTime/blob/master/logoTT.jpg" height="200" align="middle"> </center>

[![Build Status](https://travis-ci.org/AShedko/TravelTime.svg?branch=master)](https://travis-ci.org/AShedko/TravelTime)

YOUR travel planner

Docs:
https://docs.google.com/document/d/1wQIGpxLP6wt7ojlqp8-9iovufeXkW7DkO7VndmYaR2c/edit

SCRUM:
* https://trello.com/b/BU2KVZ6n/проект-по-технологиям-программирования (карточки)
* https://docs.google.com/spreadsheets/d/1EOpCVhoT_YQxw9-8FDo3KxqEk6uxJ1pJ2x_3qUZo8EI/edit#gid=0 (краткие отчёты по задачам)

Список версий:
https://docs.google.com/document/d/15kDblGW-fyCqJO53wpTI9ixilkwOz0zlRz9RIEcEhNE/edit

Как запускать:

перед запуском:
`
pip install -r requirements.txt
`
настройка postgres для джанго
https://djbook.ru/examples/77/

* `python3 manage.py runserver` запускает проект в режиме разработчка
* `python3 manage.py migrate` меняет модель данных в соответсвии с кодом
* `python3 manage.py migrate --run-syncdb` мигрируем базу
