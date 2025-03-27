from django.db import models
from django.urls import reverse_lazy

MAX_LENGHT_CHAR = 255

# Create your models here.
class Bid(models.Model):
    first_name = models.CharField(max_length=MAX_LENGHT_CHAR, verbose_name='Имя')
    last_name = models.CharField(max_length=MAX_LENGHT_CHAR, verbose_name='Фамилия')
    email_address = models.EmailField(max_length=MAX_LENGHT_CHAR, unique=False, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=15, unique=False, verbose_name = 'Номер телефона')
    message = models.TextField(max_length=MAX_LENGHT_CHAR, null=True, blank=True, verbose_name='Сообщение')

    def __str__(self):
        return f"{self.first_name} -- {self.last_name}"
    
    class Meta:
        verbose_name = 'Заявка клиента'
        verbose_name_plural = 'Заявки клиентов'

class House(models.Model):
    name = models.CharField(max_length=MAX_LENGHT_CHAR, verbose_name='Название дома')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    prices = models.TextField(blank=True, null=True, verbose_name='Цены')
    mileage = models.TextField(blank=True, null=True, verbose_name='Пробег')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

class HousePhoto(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='photos', verbose_name='Дом')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return f"Фото для {self.house.name}"
    
    class Meta:
        verbose_name = 'Фотография дома'
        verbose_name_plural = 'Фотографии домов'