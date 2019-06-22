from django.db import models

# Create your models here.

class Graph(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField('date published')

class Node(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

class Edge(models.Model):
    src_node = models.ForeignKey(Graph,
        on_delete=models.PROTECT,
        related_name='%(class)s_src_node'
    )
    dst_node = models.ForeignKey(Graph,
        on_delete=models.PROTECT,
        related_name='%(class)s_dst_node'
    )

