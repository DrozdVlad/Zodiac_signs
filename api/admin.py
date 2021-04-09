from django.contrib import admin

from api.models import Client, Address


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    exclude = ('zodiac_signs',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
