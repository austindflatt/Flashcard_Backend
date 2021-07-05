from .serializers import FlashcardSerializer, CollectionSerializer
from .models import Flashcard, Collection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class FlashcardList(APIView):

    def get(self, request):
        card = Flashcard.objects.all()
        serializer = FlashcardSerializer(card, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetails(APIView):

    def get_by_card(self, pk, collection):
        try:
            return Flashcard.objects.get(pk=pk, collection=collection)
        except Flashcard.DoesNotExist:
            raise Http404

    def get(self, request, pk, collection):
        card = self.get_by_card(pk, collection)
        serializer = FlashcardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk, collection):
        card = self.get_by_card(pk, collection)
        serializer = FlashcardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, collection):
        card = self.get_by_card(pk, collection)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, collection):
        card = self.get_by_card(pk, collection)
        serializer = FlashcardSerializer(card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CollectionList(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionDetail(APIView):

    def get_by_id(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_by_id(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk):
        collection = self.get_by_id(pk)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        collection = self.get_by_id(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        collection = self.get_by_id(pk)
        serializer = CollectionSerializer(collection, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)