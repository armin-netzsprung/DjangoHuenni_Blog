from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginSeite, name ="login"),
    path('logout', views.logoutBenutzer, name ="logout"),
    path('reg', views.regBenutzer, name ="reg"),
]
