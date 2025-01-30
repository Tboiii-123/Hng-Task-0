from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
# Create your views here.



@api_view(['GET'])
def get_info(request):

    data ={
        'email':'lawalhussein775@gmail.com',
        'current_datetime':datetime.now().isoformat(),
        "github_url": "https://github.com/your_username/project_repo"  
    }


    return Response(data,status=status.HTTP_200_OK)








