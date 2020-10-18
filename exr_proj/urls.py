from django.contrib import admin
from django.urls import path
import registery.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registery.views.index, name='index'),
    path('login', registery.views.login, name='login'),
    path('logout', registery.views.logout, name='logout'),
    path('delete/<int:id>', registery.views.delete),
    path('edit/<int:id>', registery.views.edit)
]
