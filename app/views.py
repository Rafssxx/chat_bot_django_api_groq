from django.shortcuts import render
from app.services.GroqService import GroqService

# Create your views here.
def index(request):
   return render(request,'app/index.html')

def send(request):
    if request.method=="POST":
        model = request.POST.get('model')
        message = request.POST.get('message')


        api_service = GroqService(model)

        response = api_service.request_prompt(None, message)

        return render(request,'app/response.html',{
            "response": response,
            "model" : model
        })
