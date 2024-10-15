from background_task import background
from django.core.mail import send_mail

@background(schedule=60)
def send_task_notification(email, title):
    subject = f"Notificación para la tarea: {title}"
    message = f"Hola, \n\nSe ha creado una nueva tarea: {title}."
    from_email = 'c.santiago.m@hotmail.com'
    
    # Enviar el correo electrónico
    send_mail(subject, message, from_email, [email])

    print(f"Notificación enviada a {email} para la tarea {title}")