from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import House, House_Spain, Rewiews, Rewiews_Spain
from .forms import BidCreation

def index(request):
    current_domain = request.get_host()
    print(f"Current domain: {current_domain}")  # Для отладки

    # Проверяем параметр языка в URL (?lang=en или ?lang=es)
    lang = request.GET.get('lang', None)

    # Если есть параметр lang, редиректим на нужный домен
    if lang == 'es' and current_domain != 'marbellacamper.es':
        return HttpResponseRedirect(f"http://marbellacamper.es{reverse('main_page')}")
    elif lang == 'en' and current_domain != 'marbellacamper.com':
        return HttpResponseRedirect(f"http://marbellacamper.com{reverse('main_page')}")

    # Определяем версию по домену
    if current_domain == 'marbellacamper.es':
        # Испанская версия
        rewiews = [{'name': r.name, 'rate': r.rate, 'text': r.text} for r in Rewiews_Spain.objects.all()]
        houses = [
            {
                'name': house.name,
                'description': house.description,
                'prices': house.prices.split('\n') if house.prices else [],
                'mileage': house.mileage.split('\n') if house.mileage else [],
                'photos': house.photos.all()
            }
            for house in House_Spain.objects.all()
        ]
        template = 'marbell/index_es.html'
    else:
        # Английская версия (по умолчанию для .com или неизвестного домена)
        rewiews = [{'name': r.name, 'rate': r.rate, 'text': r.text} for r in Rewiews.objects.all()]
        houses = [
            {
                'name': house.name,
                'description': house.description,
                'prices': house.prices.split('\n') if house.prices else [],
                'mileage': house.mileage.split('\n') if house.mileage else [],
                'photos': house.photos.all()
            }
            for house in House.objects.all()
        ]
        template = 'marbell/index.html'

    # Обработка формы
    if request.method == 'POST':
        form = BidCreation(request.POST)
        if form.is_valid():
            bid = form.save()
            subject = f"New Contact Form Submission from {bid.first_name} {bid.last_name}"
            message = (
                f"New message received:\n\n"
                f"First Name: {bid.first_name}\n"
                f"Last Name: {bid.last_name}\n"
                f"Email: {bid.email_address}\n"
                f"Phone: {bid.phone_number}\n"
                f"Message: {bid.message}\n"
            )
            from_email = 'marbell_django@mail.ru'
            recipient_list = ['zimarev.nazar131328@gmail.com', 'irwin76@gmx.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('main_page')
        else:
            print(form.errors)
            return render(request, template, {'form': form, 'houses': houses, 'rewiews': rewiews})

    form = BidCreation()
    return render(request, template, {'form': form, 'houses': houses, 'rewiews': rewiews})