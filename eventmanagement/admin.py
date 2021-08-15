from django.contrib import admin
from eventmanagement.models import Customer,Cateror,Decorator,Hall,Event,Event_Type,Package,Wedding_Package,Corporate_Package
admin.site.register(Customer)
admin.site.register(Decorator)
admin.site.register(Cateror)
admin.site.register(Hall)
admin.site.register(Event)
admin.site.register(Package)
admin.site.register(Event_Type)
admin.site.register(Wedding_Package)
admin.site.register(Corporate_Package)
# Register your models here.
