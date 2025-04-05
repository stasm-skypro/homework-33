# Домашняя работа к модулю 8
# Тема 33 Celery

## 1. Настройка проекта для работы с Celery

### Настройка Celery и Celery Beat
Пришлось немного повозиться с установкой 'django-celery-beat'. Т.к. Django обновилась до версии 5.2, то пришлось 
становить версию 'django-celery-beat' напрямую из репозитория командой 
```poetry add "django-celery-beat@git+https://github.com/celery/django-celery-beat.git@main"```
Можно было понизить версию Django до 5.1, но мы не ищем лёгких путей.

## 2.  Асинхронная рассылка писем пользователям об обновлении материалов курса.
Реализована асинхронная рассылка писем пользователям об обновлении материалов курса.

Как запустить задачу: 

#### В первом терминале запускаем брокер сообщений Redis. 
```bash```
```redis-server```

Его задача:

* хранение очереди задач,
* обмен данными между beat и worker.

 Если не запущен Redis, Celery не сможет:

* положить задачи в очередь,
* получить задачи для выполнения.

#### Во втором терминале запускаем worker.

```bash```
```celery -A config worker -l info```

#### В третьем терминале запускаем beat.

```bash```
```celery -A config beat -l info```

##### В чертвёртом терминале запускаем проект.

```bash```
```./manage.py runserver```

В программе Postaman отправляем запрос на http://127.0.0.1:8000/course/2/, предварительно залогинившись от того же 
пользователя (в данном случае id=1), который создал курс.

Получаем ответ:

```json
{
    "id": 2,
    "name": "Django с нуля",
    "description": "Создание веб-приложений на Django. Лучший курс по мнению экспертов.",
    "lessons_count": 1,
    "is_subscribed": false
}
```
и отправку письма с уведомлением на email пользователя.

### *Пользователь может обновлять уроки в курсе в любое время. Поэтому уведомление об обновлении курса отправляется* 
### *только в том случае, если с момента последнего обновления курса прошло более 4-х часов.*

## 3. Блокирование неактивных пользователей

Реализована блокировка неактивных пользователей. Создана задача в приложении users, которая блокирует пользователей, 
не входивших в свой аккаунт более 30 календарных дней. Задача зарегистрирована в signals.py в приложении users, с 
ежедневным периодом выполнения.

Задачу можно увидеть в админке

![periodic_task](/media/readme/periodic_task.png)
