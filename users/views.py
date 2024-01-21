from django.contrib.auth import authenticate, login, get_user_model
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer
from .models import CustomUser


class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Ak používateľ s takým emailom už existuje
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = authenticate(request, username=email, password=password)
    customUser = CustomUserSerializer(instance=user)

    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        return JsonResponse({'token': token.key, 'message': 'Login successful', 'user': customUser.data})
    else:
        return JsonResponse({'error': 'Login failed! Email or Password wrong'}, status=status.HTTP_401_UNAUTHORIZED)


User = get_user_model()
