from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime,timezone

from rest_framework import status
# Create your views here.



@api_view(['GET'])
def get_info(request):

    data ={
        'email':'lawalhussein775@gmail.com',
        'current_datetime': datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Tboiii-123/Hng-Task-0"  
    }


    return Response(data,status=status.HTTP_200_OK)








