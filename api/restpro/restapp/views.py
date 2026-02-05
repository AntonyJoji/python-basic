from django.shortcuts import render
from rest_framework.views import APIView
from.models import user
from .serializers import userserializer
from rest_framework.response import Response
# Create your views here.

class userprofile(APIView):
    def get(self,req):
        profile = user.objects.all()
        newdata =userserializer(profile,many=True)
        return Response(newdata.data)
    

    def post (self,req):
        newdata = userserializer(data=req.data)
        if newdata.is_valid():
            newdata.save()
            return Response(newdata.data)
        else:
            return Response("data is not valid")
