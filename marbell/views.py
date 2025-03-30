from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import House, House_Spain, Rewiews, Rewiews_Spain
from .forms import BidCreation
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def simple_index(request):
    print("Method:", request.method)
    print("POST data:", request.POST)

    # Формируем список для вывода отзывов
    rewiews = []

    for rewiew in Rewiews.objects.all():
        rewiew_data = {
            'name': rewiew.name,
            'rate': rewiew.rate,
            'text': rewiew.text
        }
        rewiews.append(rewiew_data)
    
    
    # Формируем список домов с разбиением prices и mileage
    houses = []
    for house in House.objects.all():
        house_data = {
            'name': house.name,
            'description': house.description,
            'prices': house.prices.split('\n') if house.prices else [],
            'mileage': house.mileage.split('\n') if house.mileage else [],
            'photos': house.photos.all()
        }
        houses.append(house_data)
    
    if request.method == 'POST':
        form = BidCreation(request.POST)
        if form.is_valid():
            # Сохраняем форму в базу
            bid = form.save()
            
            # Формируем письмо
            subject = f"New Contact Form Submission from {bid.first_name} {bid.last_name}"
            message = (
                f"New message received:\n\n"
                f"First Name: {bid.first_name}\n"
                f"Last Name: {bid.last_name}\n"
                f"Email: {bid.email_address}\n"
                f"Phone: {bid.phone_number}\n"
                f"Message: {bid.message}\n"
            )
            from_email = 'marbell_django@mail.ru'  # Ваш email из settings.py
            recipient_list = ['zimarev.nazar131328@gmail.com']  # Email заказчицы
            
            # Отправляем письмо
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            
            # Перенаправляем после успеха
            return redirect('main_page')
        else:
            print(form.errors)
            return render(request, 'marbell/index.html', {'form': form, 'houses': houses, 'rewiews': rewiews})
    
    form = BidCreation()
    return render(request, 'marbell/index.html', {'form': form, 'houses': houses, 'rewiews': rewiews})


def simple_index_spain(request):
    # Проверяем текущий домен
    current_domain = request.get_host()  # Получаем домен из запроса
    target_domain = 'marbellacamper.com'

    # Если текущий домен не совпадает с целевым, делаем редирект
    if current_domain != target_domain:
        # Формируем полный URL для редиректа
        redirect_url = f"https://{target_domain}{reverse('main_page_es')}"
        return HttpResponseRedirect(redirect_url)

    # Остальной код функции
    rewiews = []
    for rewiew in Rewiews_Spain.objects.all():
        rewiew_data = {
            'name': rewiew.name,
            'rate': rewiew.rate,
            'text': rewiew.text
        }
        rewiews.append(rewiew_data)

    houses = []
    for house in House_Spain.objects.all():
        house_data = {
            'name': house.name,
            'description': house.description,
            'prices': house.prices.split('\n') if house.prices else [],
            'mileage': house.mileage.split('\n') if house.mileage else [],
            'photos': house.photos.all()
        }
        houses.append(house_data)

    if request.method == 'POST':
        form = BidCreation(request.POST)
        if form.is_valid():
            bid = form.save()
            subject = f"New Contact Form Submission from {bid.first_name} {bid.last_name}"
            message = (
                f"New message received:\n\n"
                f"First Name: {bid.first_name}\n"
                f"Last name: {bid.last_name}\n"
                f"Email address: {bid.email_address}\n"
                f"Phone number: {bid.phone_number}\n"
                f"Message: {bid.message}"
            )
            from_email = 'marbell_django@mail.ru'
            recipient_list = ['zimarev.nazar131328@gmail.com', 'irwin76@gmx.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('main_page_es')
        else:
            print(form.errors)
            context = {'form': form, 'houses': houses, 'rewiews': rewiews}
            return render(request, 'marbell/index_es.html', context)

    form = BidCreation()
    context = {'form': form, 'houses': houses, 'rewiews': rewiews}
    return render(request, 'marbell/index_es.html', context)