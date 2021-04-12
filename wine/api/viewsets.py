from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from wine.models import Evaluation, Grape, Wine, Tag
from .serializers import EvaluationSerializer, GrapeSerializer, WineSerializer, TagSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['wine__name', 'score']
    ordering_fields = ['date', 'score']


class GrapeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Grape.objects.all()
    serializer_class = GrapeSerializer


class WineViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'types__name']
    ordering_fields = ['name']

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
