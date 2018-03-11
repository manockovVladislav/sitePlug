from django.contrib import admin
from .models import Subscriber

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email']
    search_fields = ['name', 'email']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)