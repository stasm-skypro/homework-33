import logging
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from .models import Course

logger = logging.getLogger(__name__)


@shared_task
def send_course_update_email(course_id):
    from users.models import Subscription  # локальный импорт для избежания циклов

    try:  # Если курс с таким id не существует, то ничего не делаем
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return

    subject = "Обновление курса: %s" % course.name
    message = "Материалы курса «%s» были обновлены.\n\nОписание: %s" % (course.name, course.description)
    subscribers = Subscription.objects.filter(course=course).select_related("user")
    for sub in subscribers:
        if sub.user.email:
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [sub.user.email],
                fail_silently=True
            )
            logger.info("Письмо отправлено пользователю %s" % sub.user)
