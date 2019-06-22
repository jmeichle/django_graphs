import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from graphs.models import *

from IPython import embed

class Command(BaseCommand):

    help = 'Gimme a ipython shell with a networkx graph by id'

    def add_arguments(self, parser):
        parser.add_argument('-g', '--graph-id', dest='graph_id', type=int, help="Start an IPython shell with the graph available as a networkx graph")
        parser.add_argument('-l', '--list-graphs', dest='list_graphs', action='store_true', help='List created graphs with their id and names')

    def handle(self, *args, **kwargs):
        if kwargs['list_graphs']:
            for db_graph in Graph.objects.all():
                print("ID: {} Name: {}".format(db_graph.id, db_graph.name))
        elif not kwargs['graph_id']:
            print("No graph specified --graph-id. List graphs with --list-graphs, or use --help.")
        else:
            db_graph = Graph.objects.get(id=kwargs['graph_id'])
            print("Django graph model available as: db_graph")
            nx_graph = db_graph.get_networkx_graph()
            print("NetworkX graph available as: nx_graph")
            
            embed(using=False)
