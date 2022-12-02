from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import *


class DevViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Dev.objects.all()
    serializer_class = dev_serializer


class DevProjectViewSet(ModelViewSet):
    queryset = Dev.objects.all().select_related('dev')
    serializer_class = dev_serializer


class ProjectViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = project_serializer


class ClientViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = client_serializer


class InvoiceViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = invoice_serializer


class DevClientsViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializers = client_serializer
    def get_queryset(self):
        return Project.objects.filter(dev_id=self.kwargs['pk'])