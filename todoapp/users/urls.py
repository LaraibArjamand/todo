from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home_page, name='home'),
    path('', views.sign_up, name='sign_up'),
    path("login", views.sign_in, name="login"),
    path("logout", views.signout, name="logout")
    # TODO: Add email verification
]
