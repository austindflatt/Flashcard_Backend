from .models import Flashcard
from .models import Collection
from rest_framework import serializers


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = [
            'id', 'collection', 'card_question', 'card_answer',
        ]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'id', 'collection_name',
        ]