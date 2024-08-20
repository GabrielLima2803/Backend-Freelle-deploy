from django.core.mail import send_mail
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def ForgotPasswordUser(request):
    email = request.data.get("email")

    if not email:
        return Response({"message": "Email é necessario!"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(email=email)
    except:
        return Response({"message": "Usuário não encontrado com esse email"}, status=status.HTTP_404_NOT_FOUND)
    
    reset_code = get_random_string(length=6, allowed_chars='1234567890')
    user.reset_code = reset_code
    user.save()

    send_mail(
        'Redefinição de senha',
        f'Seu código de redefinição de senha é: {reset_code}',
        'gabriellima2803@gmail.com', 
        [user.email],
        fail_silently=False,
    )

    return Response({"message": "Código de redefinição enviado por e-mail."}, status=status.HTTP_200_OK)