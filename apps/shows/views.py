from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Event

def index(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    context = {
        "my_events": Event.objects.filter(host=request.session["id"]),
        "logged": User.objects.get(id=request.session["id"])
    }
    return render(request, "shows/index.html", context)

#All Events page
def allevents(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    context = {
        "all_events": Event.objects.all(),
    }
    return render(request, "shows/allevents.html", context)

#Event Info Page
def info(request, id):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    event_id =  Event.objects.get(id=id)
    context = {
        "the_event": event_id,
        "going": event_id.attendees.all()
    }
    return render(request, "shows/info.html", context)

#Event Creator Page
def createeventpage(request):
    if "id" not in request.session:
        messages.error(request, 'You must be logged in to access that information') 
        return redirect("/")
    return render(request, "shows/createevent.html")

#Creates Events
def create(request, id):
    if request.method == "POST":
        hostid = int(id)
        if "id" not in request.session and request.session["id"] != hostid:
            messages.error(request, 'You can not do that') 
            return redirect("/")
        ti = request.POST["title"]
        ge = request.POST["genre"]
        da = request.POST["date"]
        lo = request.POST["location"]
        host = User.objects.get(id=hostid)
        new_event = Event.objects.create(name=ti, genre=ge, date=da, location=lo, host=host)
        print(new_event)
        return redirect("/shows")

#Adds Atendees
def attend(request, id):
    hostid = int(id)
    if "name" not in request.session and request.session["id"] != hostid:
        messages.error(request, 'You can not do that') 
        return redirect("/")
    userid = request.session["id"]
    user1 = User.objects.get(id=userid)
    event1 = Event.objects.get(id=id)
    event1.attendees.add(user1)
    return redirect("/shows")

#Cancel Event
def cancel(request, id):
    hostid = int(id)
    if "name" not in request.session and request.session["id"] != hostid:
        messages.error(request, 'You can not do that') 
        return redirect("/")
    delete = Event.objects.get(id=id).delete()
    return redirect("/shows")


