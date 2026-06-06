from rest_framework.viewsets import ModelViewSet
from users.api.serializers import UserSerializer
from users.models import User


class UserApiViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
