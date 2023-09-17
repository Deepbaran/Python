from django.urls import path
from . import views

# URLconf
app_name = "polls" # Differentiates the polls urls from other app urls 
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /specifics/polls/5/
    path("specifics/<int:question_id/", views.detail, name="detail"), # detail(request=<HttpRequest object>, question_id=34)
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]