import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from graphs.models import *

from IPython import embed

class Command(BaseCommand):

    help = 'Gimme a shell for graphs'

    def handle(self, *args, **kwargs):
        print("DB Models Loaded. Creating a dumb Graph of two nodes linked.")

        print("Creating graph with name=test")
        g = Graph.objects.create(name="test")

        print("Creating Node with name=FirstNode")
        n1 = Node.objects.create(graph=g, value="FirstNode")
        print("Creating Node with name=SecondNode")
        n2 = Node.objects.create(graph=g, value="SecondNode")

        print("Creating Edge with value=foobar")
        e1 = Edge.objects.create(graph=g, value='foobar')

        print("Relating Edge=foobar to node=FirstNode")
        ne1 = NodeEdge.objects.create(node=n1, edge=e1)
        print("Relating Edge=foobar to node=SecondNode")
        ne2 = NodeEdge.objects.create(node=n2, edge=e1)
        
        print("Done.")
