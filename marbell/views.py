from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import House, House_Spain
from .forms import BidCreation

def simple_index(request):
    print("Method:", request.method)
    print("POST data:", request.POST)
    
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
            recipient_list = ['zimarev.nazar13@gmail.com']  # Email заказчицы
            
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
            return render(request, 'marbell/index.html', {'form': form, 'houses': houses})
    
    form = BidCreation()
    return render(request, 'marbell/index.html', {'form': form, 'houses': houses})


def simple_index_spain(request):

    # Формируем список домов с разбиением prices и mileage
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
            recipient_list = ['zimarev.nazar13@gmail.com']

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False
            )

            return redirect('main_page_es')

        else:
            print(form.errors)
            context = {
                'form': form,
                'houses': houses
            }
            return render(request, 'marbell/index_es.html', context)
    
    form = BidCreation()
    context = {
        'form': form,
        'houses': houses
    }
    return render(request, 'marbell/index_es.html', context)