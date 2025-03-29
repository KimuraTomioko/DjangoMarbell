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
    max_num = 20  # Ограничение до 20 фотографий

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HousePhotoInline]
    list_display = ('name', 'description')

@admin.register(HousePhoto)
class HousePhotoAdmin(admin.ModelAdmin):
    list_display = ('house', 'photo')

class HousePhotoInline_Spain(admin.TabularInline):
    model = HousePhoto_Spain
    extra = 1  # Показывать 1 пустое поле для добавления фото
    max_num = 20  # Ограничение до 20 фотографий

@admin.register(House_Spain)
class HouseSpainAdmin(admin.ModelAdmin):
    inlines = [HousePhotoInline_Spain]
    list_display = ('name', 'description')

@admin.register(HousePhoto_Spain)
class HousePhotoSpainAdmin(admin.ModelAdmin):
        list_display = ('house', 'photo')



@admin.register(Rewiews)
class RewiewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')
    list_display_links = ('name',)

@admin.register(Rewiews_Spain)
class RewiewAdmin_Spain(admin.ModelAdmin):
    list_display = ('name', 'rate')
    list_display_links = ('name',)