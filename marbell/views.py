from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import House, House_Spain, Rewiews, Rewiews_Spain
from .forms import BidCreation

def index(request):
    current_domain = request.get_host()

    # Определяем, какой домен и какую версию показывать
    if current_domain == 'marbellacamper.com':
        # Английская версия
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
    elif current_domain == 'marbellacamper.es':
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
        # Если домен неизвестный, редиректим на .com (английская версия)
        redirect_url = f"http://marbellacamper.com{reverse('main_page')}"
        return HttpResponseRedirect(redirect_url)

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
            return redirect('main_page')  # Редирект на корень
        else:
            print(form.errors)
            return render(request, template, {'form': form, 'houses': houses, 'rewiews': rewiews})

    form = BidCreation()
    return render(request, template, {'form': form, 'houses': houses, 'rewiews': rewiews})