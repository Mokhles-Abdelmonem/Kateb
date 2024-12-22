from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    """
    API view to register a new user.
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
