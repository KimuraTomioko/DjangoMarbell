from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Bid)
class AdminBid(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email_address', 'phone_number')
    list_filter = ('first_name', )
    list_display_links = ('first_name', 'email_address')

class HousePhotoInline(admin.TabularInline):
    model = HousePhoto
    extra = 1  # Показывать 1 пустое поле для добавления фото
    max_num = 20  # Ограничение до 10 фотографий

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HousePhotoInline]
    list_display = ('name', 'description')

@admin.register(HousePhoto)
class HousePhotoAdmin(admin.ModelAdmin):
    list_display = ('house', 'photo')

#@admin.register(Rewiews)
#class RewiewAdmin(admin.ModelAdmin):
#    list_display = ('name', 'rate')
#    list_display_links = ('name',)