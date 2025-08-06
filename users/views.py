from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from navat import settings
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, FeedbackSerializers
from .models import Feedback


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            login(request, user)
            return Response({"message": "Успешный вход"}, status=status.HTTP_200_OK)
        return Response({"error": "Неверные учетные данные"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Вы вышли из системы"}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class FeedbackSendView(generics.CreateAPIView):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        feedback = serializer.save()
        subject = f'Обратная связь от {feedback.name}'
        full_message = f'Имя: {feedback.name}\nEmail: {feedback.email}\nMessage: {feedback.message}'

        send_mail(
            subject,
            full_message,
            feedback.email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )