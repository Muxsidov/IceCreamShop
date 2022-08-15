from rest_framework import authentication, generics, permissions

from .permissions import IsStaffEditorPermission
from .models import IceCream
from .serializers import IceCreamSerializer


class IceCreamCreateAPIView(generics.CreateAPIView):
    """
    Create
    """
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]


class IceCreamDetailAPIView(generics.RetrieveAPIView):
    """
    See one IceCream.
    """
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class IceCreamListAPIView(generics.ListAPIView):
    """
    List of IceCreams.
    """
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class IceCreamUpdateAPIView(generics.UpdateAPIView):
    """
    Update IceCream.
    """
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class IceCreamDestroyAPIView(generics.DestroyAPIView):
    """
    Delete IceCream
    """
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    lookup_field = 'pk'

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]
    
    def perform_destroy(self, instance ):
        super().perform_destroy(instance)