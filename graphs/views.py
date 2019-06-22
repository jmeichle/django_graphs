from django.shortcuts import render
from django.http import HttpResponse

# IT is bad practice to have views directly talk to models.
# Instead: define a service class for this (Which just provides the methods of DB model access you want for the view(s))
from graphs.models import *

def index(request):
    graphs = Graph.objects.all()
    # Also, use a rendered django template and not this crappy string HTML stuff.
    return HttpResponse(
        "Graphs! Graphs! Graphs!</br></br>Graph Names:</br>{}".format(
            "</br>".join(
                [
                    "Name: <b>{}</b> Created: <b>{}</b>".format(g.name, g.created_at)
                    for g in graphs
                ]
            )
        )
    )
