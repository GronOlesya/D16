from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives,  mail_admins


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        subject = 'Приветствуем Вас на нашем новостном портале!',
        text = f'{user.username}, Вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, Вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/posts">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user

