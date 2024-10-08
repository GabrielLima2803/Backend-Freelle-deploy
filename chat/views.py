from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .redis_client import redis_client

class SendMessageView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        message = request.data.get('message')

        if not user_id or not message:
            return Response({'detail': 'user_id e message são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'user_id': user_id,
            'message': message
        }
        
        try:
            redis_client.publish('chat_messages', json.dumps(data))
            return Response({'detail': 'Mensagem enviada com sucesso!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)