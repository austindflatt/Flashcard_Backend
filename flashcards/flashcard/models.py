from django.db import models


class Collection(models.Model):
    collection_name = models.CharField(max_length=100)


class Flashcard(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    card_question = models.CharField(max_length=120)
    card_answer = models.CharField(max_length=120)
