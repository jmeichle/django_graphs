from django.db import models

import networkx as nx

# Create your models here.

class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # A timestamp reprensenting when this object was last updated.
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ['-created_at', '-updated_at']


class Graph(TimestampedModel):
    name = models.CharField(max_length=200)

    def get_networkx_graph(self):
        nx_graph = nx.Graph()
        nodes = self.node_set.all()
        for node in nodes:
            nx_graph.add_node(node.value)
        
        edges = self.edge_set.all()
        for edge in edges:
            edge_node_relations = edge.nodeedge_set.all()
            # Only care about edges that exist with two related nodes.
            if len(edge_node_relations) == 2:
                # for the NodeEdge objects, that map this edge to two nodes, get the list of node values
                edge_node_values = [ ne.node.value for ne in edge_node_relations ]
                # not a digraph, so order does not matter when adding the edge
                nx_graph.add_edge(edge_node_values[0], edge_node_values[1])

        return nx_graph

class Node(TimestampedModel):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

class Edge(TimestampedModel):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

class NodeEdge(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    edge = models.ForeignKey(Edge, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('node', 'edge')
