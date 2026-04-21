# STRIPE_QUEST
Выполненые задания
1) Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
 - Django Модель Item с полями (name, description, price) 
 - API с двумя методами:
     - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
     - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
- Залить решение на Github, описать запуск в Readme.md
- Опубликовать свое решение онлайн, предоставив ссылку на решение и доступ к админке, чтобы его можно было быстро и легко протестировать. 

2) Бонусные задачи: 
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Запуск приложения на удаленном сервере, доступном для тестирования, с кредами от админки
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте


## Стек технологий

![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-API-008CDD?style=flat-square&logo=stripe&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-1.7-60A5FA?style=flat-square&logo=poetry&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-21.2-499848?style=flat-square&logo=gunicorn&logoColor=white)


## Запуск

### Клонирование репозитория

```bash
git clone https://github.com/WarfoIomey/stripe_quest.git
cd stripe_quest
```
## Настройки окружения

Перед запуском приложения настройте переменные окружения (пример в файле .env_example):

- `POSTGRES_USER`— пользователь базы данных.
- `POSTGRES_PASSWORD`— пароль пользователя базы данных.
- `POSTGRES_DB`— имя базы данных PostgreSQL.
- `SECRET_KEY` — секретный ключ Django.
- `DB_HOST` — хост базы данных.
- `DB_PORT` — порт для подключения к базе данных.
- `DEBUG` — статус отладки Django.
- `STRIPE_KEY` - секретный ключ Stripe API
- `PUBLIC_KEY_STRIPE` - публичный ключ Stripe API

## Развёртывание на сервер

Выполните следующие команды:
```bash
docker compose up --build
```
Для создания суперпользователя выполните следующую команду:
```bash
    docker compose exec web python manage.py createsuperuser
```

После успешного выполнения этих команд приложение будет доступно по адресу <http://localhost:8001/>.
