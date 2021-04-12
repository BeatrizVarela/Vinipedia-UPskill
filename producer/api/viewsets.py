from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from producer.api.serializers import ProducerSerializer, ProducerPictureSerializer, PictureAuthorSerializer
from producer.models import PictureAuthor, Producer, ProducerPicture


class PictureAuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PictureAuthor.objects.all()
    serializer_class = PictureAuthorSerializer

class ProducerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['name']



class ProducerPictureViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ProducerPicture.objects.all()
    serializer_class = ProducerPictureSerializer

