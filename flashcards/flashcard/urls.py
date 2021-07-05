from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectionList.as_view()),
    path('collection/<int:pk>', views.CollectionDetail.as_view()),
    path('flashcards', views.FlashcardList.as_view()),
    path('collection/<int:collection>/flashcards/<int:pk>', views.FlashcardDetails.as_view())
]