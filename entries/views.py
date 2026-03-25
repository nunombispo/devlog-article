# entries/views.py
from rest_framework import mixins, viewsets

from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
