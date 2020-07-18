from graphene_django.views import GraphQLView

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .schema import schema

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login-user"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page="/login/"),
        name="logout-user"
        ),
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]