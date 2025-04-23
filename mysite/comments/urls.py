from django.urls import path
from .views import comment_list

app_name = 'comments'

urlpatterns = [
    path("", comment_list, name="comment_list"),
]
