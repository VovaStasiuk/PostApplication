from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from ..models import Profile
from .serializers import UserModelSerializer


class CreateUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserModelSerializer
    queryset = Profile.objects.all()


