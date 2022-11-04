from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects':projects})

def sendemail(request):
    if request.method == 'GET':
        return render(request, 'portfolio/sendemail.html')
    else:
        message = request.POST['message']
        your_email = request.POST['your_email']
        try:
            send_mail('Сообщение с сайта', str(message +f'\nот: {your_email}'), 'todosergo@yandex.ru', ['todosergo@yandex.ru'], fail_silently=False, )
            site_message = 'Сообщение отправлено'
            return render(request, 'portfolio/sendemail.html', {'site_message': site_message})
        except Exception as e:
            site_message = 'Сообщение не отправлено. Что-то пошло не так. Сообщите администратору'
            print(e)
            return render(request, 'portfolio/sendemail.html', {'site_message': site_message})

