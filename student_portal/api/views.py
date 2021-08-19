from django.shortcuts import HttpResponse
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

def welcome(request):
    return HttpResponse("<h1>bsdk tm hamare ghar me aa gaye Nikal Laude</h1>")


class StudentView(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class GetStudent(APIView):
    def get(self, request,format=None):
        return HttpResponse("<h1>BSDK Aukat me madarchod tmhare baap ki api ni hai</h1>")
    serializer_class=StudentSerializer
    lookup_url_kwarg='user_name'
    lookup_url_kwarg_pass='password'
    def post(self,request,format=None):
        user_name=request.data.get(self.lookup_url_kwarg)
        password=request.data.get(self.lookup_url_kwarg_pass)
        if user_name!=None and password!=None:
            # print(user_name)
            # print(password)
            student=Student.objects.filter(user_name=user_name)
            if len(student)>0:
                # print(self.serializer_class(student[0]).data["password"])
                if password == self.serializer_class(student[0]).data["password"]:
                    datum = self.serializer_class(student[0]).data
                    return Response(datum,status=status.HTTP_200_OK)
                return Response({'Incorrect Password'},status=status.HTTP_401_UNAUTHORIZED)
            return Response({'Bad Request:','User Does not exist'},status=status.HTTP_204_NO_CONTENT)
        return Response({'Bad Request:','Request parameter Not meant'},status=status.HTTP_400_BAD_REQUEST)


