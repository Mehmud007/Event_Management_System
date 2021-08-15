
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('signin', views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('u_logout',views.u_logout),
    path('book_event',views.book_event),
    path('view_packages',views.view_packages),
    path('show_data',views.show_data),
    path('<int:id>',views.read_more,name='read_more'),
    path('select_packages/<int:id>',views.select_packages,name='select_packages'),
    path('confirm_booking',views.confirm_booking),
    path('view_hall',views.view_hall,name='view_hall'),
    path('select_hall/<int:id>',views.select_hall,name='select_hall'),
    path('birthday_event',views.birthday_event),
    path('corporate_event',views.corporate_event),
    path('wedding_event',views.wedding_event),
    path('silver_package',views.silver_read_more),
    path('gold_package',views.gold_read_more),
    path('platinum_package',views.platinum_read_more),
    path('select',views.select),
    path('c_package',views.c_pack),
    path('services',views.services),
    path('confirm',views.confirm),
    path('profile',views.profile),
    path('wedding_silver_package',views.silver_read_more),
]
