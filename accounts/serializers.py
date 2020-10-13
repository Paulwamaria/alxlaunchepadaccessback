from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        """Serializes and deserializes data matching the specied model and fields.


        Args:
            UserCreateSerializer (serializer): serializes and deserializes the user objects.
        """
        model = User
        fields = ('id', 'email', 'firstName', 'lastName', 'password')
