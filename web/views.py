import json

from django.shortcuts import render
from django.http.response import HttpResponse

from web.models import Clients, Subscription, Feature

def index(request):
    client_s = Clients.objects.all()
    features = Feature.objects.all()
    context = {
        "client_s" :client_s,
        "features" :features
    }
    return render(request, "index.html", context=context)

def subscribe(request):
    email = request.POST.get("email")
    if not Subscription.objects.filter(email=email).exists():
        Subscription.objects.create(
            email = email
        )
        response_data = {
            "status" : "success",
            "title" : "successfully registered",
            "message": "You subscribed our newsletter successfully"
        }
    else:
         response_data = {
            "status" : "error",
            "title" : "you are already subscribed",
            "message": "You are already a member.No need to register again..!"
        }
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")
