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

        print("Creating Node with name=1")
        n1 = Node.objects.create(graph=g, value="1")
        print("Creating Node with name=2")
        n2 = Node.objects.create(graph=g, value="2")

        print("Creating Edge with value=e1")
        e1 = Edge.objects.create(graph=g, value='e1')

        print("Relating Edge=e1 to node=1")
        ne1 = NodeEdge.objects.create(node=n1, edge=e1)
        print("Relating Edge=e1 to node=2")
        ne2 = NodeEdge.objects.create(node=n2, edge=e1)


        print("Creating Node with name=3")
        n3 = Node.objects.create(graph=g, value="3")
        print("Creating Node with name=4")
        n4 = Node.objects.create(graph=g, value="4")
        print("Creating Node with name=5")
        n5 = Node.objects.create(graph=g, value="5")

        print("Creating Edge with value=e2")
        e2 = Edge.objects.create(graph=g, value='e2')
        print("Creating Edge with value=e3")
        e3 = Edge.objects.create(graph=g, value='e3')


        print("Relating Edge=e2 to node=3")
        ne1 = NodeEdge.objects.create(node=n3, edge=e2)
        print("Relating Edge=e2 to node=4")
        ne2 = NodeEdge.objects.create(node=n4, edge=e2)

        print("Relating Edge=e3 to node=4")
        ne1 = NodeEdge.objects.create(node=n4, edge=e3)
        print("Relating Edge=e3 to node=5")
        ne2 = NodeEdge.objects.create(node=n5, edge=e3)


        print("Creating Edge with value=e2")
        e4 = Edge.objects.create(graph=g, value='e4')
        print("Relating Edge=e4 to node=2")
        ne1 = NodeEdge.objects.create(node=n2, edge=e4)
        print("Relating Edge=e4 to node=4")
        ne2 = NodeEdge.objects.create(node=n4, edge=e4)
        
        print("Done.")
