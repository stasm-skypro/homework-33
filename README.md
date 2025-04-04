# Домашняя работа к модулю 8
# Тема 33 Celery

## 1. Настройка проекта для работы с Celery

### Настройка Celery и Celery Beat
Пришлось немного повозиться с установкой 'django-celery-beat'. Т.к. Django обновилась до версии 5.2, то пришлось установить версию 'django-celery-beat' напрямую из репозитория командой 
```poetry add "django-celery-beat@git+https://github.com/celery/django-celery-beat.git@main"```
Можно было понизить версию Django до 5.1, но мы не ищем лёгких путей.

## 2.  Асинхронная рассылка писем пользователям об обновлении материалов курса.
