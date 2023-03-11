from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

def index(request):
    return render(request, 'index.html')

class ReactView(APIView):
    def get(self, request):
        output =  [{"name":output.name, "id": output.id, 
                    "zip_code":output.zip_code, "email":output.email,
                    "phone":output.phone, "age":output.age, "hobbies":output.hobbies,
                    "weather":output.weather, "budget":output.budget, "env_pref":output.env_pref,
                    "final_init":output.final_init}
                    for output in React.objects.all()]
        return Response(output)


    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    





